"""What the site, the telemetry Worker and CI must agree on inside this repository."""

import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_DIR = ROOT / "site" / "latest-version"
WORKER = ROOT / "telemetry-worker"


def _worker_install_types() -> set[str]:
    source = (WORKER / "src" / "validate.js").read_text(encoding="utf-8")
    block = re.search(r"export const INSTALL_TYPES[^\[]*\[(.*?)\]", source, re.S)
    assert block, "validate.js no longer declares INSTALL_TYPES as an array"
    return set(re.findall(r"""["']([^"']+)["']""", block.group(1)))


def test_every_install_type_has_a_version_manifest():
    """A bucket with no file answers 404 HTML to the app's version check."""
    published = {p.stem for p in MANIFEST_DIR.glob("*.json")}
    assert published == _worker_install_types()


def test_version_manifests_agree_on_the_version():
    """All manifests carry the identical payload, as release-update.yml writes them."""
    payloads = {
        p.name: json.loads(p.read_text(encoding="utf-8"))
        for p in [ROOT / "site" / "latest-version.json", *MANIFEST_DIR.glob("*.json")]
    }
    assert len(payloads) > 1, "no version manifests found"
    distinct = {json.dumps(v, sort_keys=True) for v in payloads.values()}
    assert len(distinct) == 1, f"version manifests disagree: {payloads}"


def test_telemetry_worker_config_and_d1_contract_are_validated():
    """CI checks both Worker behavior and Wrangler's deploy-time config."""
    workflow = yaml.safe_load(
        (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    )
    steps = [
        step
        for job in workflow["jobs"].values()
        for step in job.get("steps", [])
        if step.get("working-directory") == "telemetry-worker"
    ]
    commands = "\n".join(step.get("run", "") for step in steps)
    for required in ("npm ci", "npm test", "npm run check:config"):
        assert required in commands, f"Telemetry CI is missing {required!r}"

    package = json.loads((WORKER / "package.json").read_text(encoding="utf-8"))
    config_text = (WORKER / "wrangler.jsonc").read_text(encoding="utf-8")
    config = json.loads(
        "\n".join(line.split("//", 1)[0] for line in config_text.splitlines())
    )
    scripts = package.get("scripts", {})
    assert scripts.get("test") == "npm run test:unit && npm run test:d1"
    assert scripts.get("test:d1") == "node --test test/d1-integration.test.js"
    assert (WORKER / "test/d1-integration.test.js").is_file()
    assert scripts.get("check:config", "").startswith(
        "WRANGLER_LOG_PATH=.wrangler/logs wrangler deploy --dry-run"
    )
    # The deploy runs through a script that injects the database id, so the
    # no-provisioning flags live there: every `wrangler deploy` it makes must
    # carry them.
    assert scripts.get("deploy") == "node scripts/deploy.mjs"
    deploy_script = (WORKER / "scripts/deploy.mjs").read_text(encoding="utf-8")
    assert (
        'export const DEPLOY_FLAGS = ["--no-x-provision", "--no-x-auto-create"];'
        in deploy_script
    )
    deploy_calls = re.findall(r'wrangler\(\["deploy",[^\]]*\]', deploy_script)
    assert deploy_calls, "deploy.mjs no longer runs wrangler deploy"
    assert all("...DEPLOY_FLAGS" in call for call in deploy_calls)
    d1_bindings = config.get("d1_databases", [])
    assert any(binding.get("binding") == "DB" for binding in d1_bindings)
    assert all("database_id" not in binding for binding in d1_bindings)
    assert config.get("triggers", {}).get("crons") == ["*/5 * * * *"]
    assert config.get("limits", {}).get("cpu_ms") == 30000
    assert config.get("observability", {}).get("enabled") is True
