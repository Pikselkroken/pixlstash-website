"""Check this site against a checkout of the PixlStash app.

    python scripts/check_against_app.py --app release

Two things here are only correct relative to the app, and nothing else couples
them. ``release-update.yml`` runs this against each release it publishes.

* The telemetry Worker must accept every install type the backend can report
  (``Server.INSTALL_TYPES``), or those installs' pings are rejected.
* ``install.html``'s download buttons build a GitHub asset URL by hand, so the
  filename has to match the template electron-builder names the artifacts with.

Standard library only: it reads the app's source, it does not import it.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# electron-builder's ${ext} for a target, where the two differ.
_TARGET_EXTENSIONS = {"nsis": "exe"}


def _strings(block: str) -> set[str]:
    return set(re.findall(r"""["']([^"']+)["']""", block))


def check(app: Path, site_root: Path = ROOT) -> list[str]:
    """Return one message per disagreement between *site_root* and *app*."""
    problems = []

    server = (app / "pixlstash" / "server.py").read_text(encoding="utf-8")
    backend = re.search(r"^\s*INSTALL_TYPES = \((.*?)\)", server, re.S | re.M)
    worker_js = (site_root / "telemetry-worker" / "src" / "validate.js").read_text(
        encoding="utf-8"
    )
    worker = re.search(r"export const INSTALL_TYPES[^\[]*\[(.*?)\]", worker_js, re.S)
    if not backend or not worker:
        problems.append("could not read INSTALL_TYPES from the app or the Worker")
    elif _strings(backend.group(1)) != _strings(worker.group(1)):
        problems.append(
            f"the backend reports {sorted(_strings(backend.group(1)))} but the "
            f"telemetry Worker accepts {sorted(_strings(worker.group(1)))}"
        )

    build = json.loads((app / "electron" / "package.json").read_text(encoding="utf-8"))[
        "build"
    ]
    template = build["artifactName"]
    html = (site_root / "site" / "install.html").read_text(encoding="utf-8")
    prefix = template.split("${version}")[0].replace(
        "${productName}", build["productName"]
    )
    if f'{prefix}"' not in html:
        problems.append(
            f"install.html does not build the {prefix!r} prefix that artifactName "
            f"{template!r} produces; the download buttons would 404"
        )
    if not template.endswith("${version}-${os}-${arch}.${ext}"):
        problems.append(
            f"artifactName {template!r} no longer ends with the "
            "'<version>-<os>-<arch>.<ext>' tail install.html appends"
        )
    assets_block = re.search(r"const DESKTOP_ASSETS = \{(.*?)\};", html, re.S)
    assets = dict(
        re.findall(r'(\w+):\s*"([^"]+)"', assets_block.group(1) if assets_block else "")
    )
    if set(assets) != {"win", "mac", "linux"}:
        problems.append(
            f"expected a download button per platform, got {sorted(assets)}"
        )
    for platform, asset in sorted(assets.items()):
        extension = asset.rsplit(".", 1)[1]
        configured = {
            _TARGET_EXTENSIONS.get(target, target)
            for target in build.get(platform, {}).get("target", [])
        }
        if extension not in configured:
            problems.append(
                f"install.html offers a .{extension} download for {platform}, but "
                f"the app builds {sorted(configured)} there"
            )
    return problems


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--app", type=Path, required=True)
    problems = check(parser.parse_args().app)
    for problem in problems:
        print(f"::error::{problem}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
