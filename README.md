# pixlstash.dev

The [PixlStash](https://github.com/Pikselkroken/pixlstash) website, its assets,
and the telemetry Worker that sits beside it.

| Path | What |
|---|---|
| `site/` | The site, exactly as served: static HTML, `assets/`, the API reference under `api/`, the version manifests the app's update check reads (`latest-version*`), and the training recipes installs fetch (`training-presets/`). No build step. |
| `scripts/` | The release-candidate mirror builder and the release update. |
| `telemetry-worker/` | The Cloudflare Worker behind `t.pixlstash.dev`. Deployed by hand; see its README. |
| `screenshots/` | Which picture each page shows (`script.json`) and where each one came from (`inventory.md`). |

Preview locally: `python3 -m http.server -d site`.

## Deploying

**Pushing a tag deploys that tag to pixlstash.dev.** Nothing else does: `main`
can carry copy for a version that is not out yet.

```
git tag v2.0.1
git push origin v2.0.1
```

Name the tag for the app release the site describes, with a suffix for a
site-only change in between (`v2.0.1-1`). To deploy a tag again, as a rollback
or to refresh `/prerelease/`:

```
gh workflow run deploy.yml --ref v2.0.0
```

### The release-candidate mirror

While the app has a release candidate newer than its stable release, every
deploy also publishes `site/` **as it is on `main`** under `/prerelease/`, with
the download links and install commands pointed at that candidate. Otherwise
`/prerelease/` redirects to the stable site.

## When the app releases

`release-update.yml` checks a few times a day for a new PixlStash release and
opens a pull request with its API reference, raised version manifests and
training recipes. Merge it, then tag the merge to deploy. To run it now:

```
gh workflow run release-update.yml -f tag=v2.0.1
```

The app's update notice reads the version manifests, so installs hear about a
release once that pull request is merged **and tagged**.

## Checks

```
python -m pytest tests                          # needs pytest and pyyaml
python3 scripts/check_against_app.py --app <a pixlstash checkout>
cd telemetry-worker && npm ci && npm test
```

## Screenshots

The captures are made from the app, in the PixlStash repository:

```
cd <pixlstash>/frontend
PIXLSTASH_WEBSITE=<this checkout> npm run screenshots 2.0.0
```

They land in the gitignored `screenshots/output/`; copy the ones `inventory.md`
names into `site/assets/` by hand. After adding or removing a picture on a page,
run `node screenshots/extract-script.mjs` to refresh `script.json`.

## Repository settings this relies on

- **Pages**: source *GitHub Actions*, custom domain `pixlstash.dev`.
- **Environment `github-pages`**: deployment from tags allowed (a tag rule `*`).
- **Secret `RELEASE_BOT_TOKEN`**: a token that may write contents and pull
  requests here, for the release update. The organisation does not let the
  default Actions token open pull requests.
