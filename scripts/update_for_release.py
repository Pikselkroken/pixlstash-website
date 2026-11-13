"""Write what a PixlStash release changes on the site, besides its API reference.

    python scripts/update_for_release.py --app release --tag v2.0.0

``release-update.yml`` runs this with the release checked out at ``--app`` and
installed, so ``pixlstash`` imports as the released code.

* ``site/latest-version.json`` and one ``site/latest-version/<type>.json`` per
  install type the release can report, all with the identical payload. They
  are raised only when the release is strictly newer than the one published.
  The per-type files back the app's version-check URLs; a type with no file
  answers 404 HTML, so the list comes from the release itself.
* ``site/training-presets/v1/``, the training recipes the release ships, which
  older installs fetch from the site. Left alone for a release older than the
  one published.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from packaging.version import InvalidVersion, Version

SITE = Path(__file__).resolve().parent.parent / "site"


def security_level(changelog: Path) -> str | None:
    """Return the ``[Security: LEVEL]`` of the newest version heading, if any."""
    if not changelog.exists():
        return None
    for line in changelog.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("#"):
            match = re.search(
                r"\[Security:\s*(Critical|High|Moderate|Low)\]", line, re.IGNORECASE
            )
            # Only the first (latest) version heading counts.
            return match.group(1).capitalize() if match else None
    return None


def published_version(site: Path) -> Version | None:
    """Return the version ``latest-version.json`` names, if it names one."""
    try:
        return Version(
            str(json.loads((site / "latest-version.json").read_text())["version"])
        )
    except (OSError, KeyError, InvalidVersion, json.JSONDecodeError):
        return None


def update_manifests(
    site: Path, tag: str, install_types: tuple[str, ...], security: str | None
) -> bool:
    """Raise the version manifests to *tag*; return whether they changed."""
    new_version = Version(tag.removeprefix("v"))
    current_path = site / "latest-version.json"
    current = published_version(site)
    if new_version.is_prerelease or (current is not None and new_version <= current):
        print(f"{new_version} is not newer than {current}; manifests left alone.")
        return False

    payload = {"version": str(new_version)}
    if security:
        payload["security"] = security
    text = json.dumps(payload) + "\n"
    current_path.write_text(text)
    per_type = site / "latest-version"
    per_type.mkdir(exist_ok=True)
    for install_type in install_types:
        (per_type / f"{install_type}.json").write_text(text)
    print(f"Version manifests now say {payload} for {sorted(install_types)}")
    return True


def update_presets(site: Path, files: dict[str, bytes]) -> None:
    """Make ``training-presets/v1`` hold exactly *files*."""
    out = site / "training-presets" / "v1"
    out.mkdir(parents=True, exist_ok=True)
    for stale in out.iterdir():
        if stale.name not in files:
            stale.unlink()
    for name, raw in files.items():
        (out / name).write_bytes(raw)
    print(f"Wrote {len(files)} training recipe files")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--app", type=Path, required=True)
    parser.add_argument("--tag", required=True)
    args = parser.parse_args()

    # The release under --app, installed by the workflow.
    from pixlstash.server import Server
    from pixlstash.training.preset_updates import site_files

    # Read before the manifests move: a run for an older release (to redo its
    # API reference) must not put its older recipes back on the site.
    current = published_version(SITE)
    update_manifests(
        SITE, args.tag, Server.INSTALL_TYPES, security_level(args.app / "CHANGELOG.md")
    )
    if current is None or Version(args.tag.removeprefix("v")) >= current:
        update_presets(SITE, site_files())
    else:
        print(f"{args.tag} is older than {current}; training recipes left alone.")


if __name__ == "__main__":
    main()
