# Website and docs screenshots: inventory

Every image and video under `site/`, and (in the pixlstash repository) under `docs/` and the API-docs images
in `pixlstash/data/scalar-assets/`, as of 2.0.0. **Last changed** and
**version** are the commit that last touched the file before this inventory
and the newest release tag at that commit, which is the UI it shows.

Status:

- **regenerated**: re-captured from the 2.0 Electron app by `npm run screenshots 2.0.0`
  (`frontend/e2e/screenshots/scenes.js` names the scene; Getting started videos
  02, 03 and 06 are `videos.spec.js`). A run writes every
  scene to the gitignored `screenshots/output/`; nothing reaches
  `site/assets/` until it is copied there, and this table is what says which
  files to copy. Scenes for **historical** files still run, so a release that
  shows one again has a current capture ready.
- **restored**: put back from git; an earlier harness run had overwritten it.
- **stale, manual**: on a current page, shows an older UI, and needs a person to
  capture it (the reason says why).
- **historical**: only on What's New, beside the release it announces. Left as it is.
- **external**: not PixlStash's UI (ComfyUI, LM Studio, Windows, a terminal).
- **unreferenced**: no page links it. Left alone; a candidate for deletion.
- **current**: branding.
- **deleted**: removed with the page section that showed it.

Pages are those that link the file; README is the repository README.

| File | Last changed | Version | Pages | Status | Note |
|---|---|---|---|---|---|
| `docs/design/assets/logo/PixlStash-Logo.png` | 2026-07-24 | v1.7.1 | docs/design/visual-language.md | current | branding |
| `docs/design/assets/logo/PixlStash-Watermark.png` | 2026-06-20 | v1.7.0-dev.1 | docs/design/visual-language.md | current | branding |
| `site/assets/01-PictureImport.mp4` | 2026-05-30 | v1.4.1 | introduction | stale, manual | screen recording; a drag in from the desktop, by hand |
| `site/assets/02-CharacterAssignment.gif` | 2026-04-13 | v1.0.0 |  | unreferenced | no page links it |
| `site/assets/02-CharacterAssignment.mp4` | 2026-05-30 | v1.4.1 | introduction | regenerated | recorded from the 2.0 Electron app (`frontend/e2e/screenshots/videos.spec.js`) |
| `site/assets/03-Tagging.gif` | 2026-05-18 | v1.2.1 |  | unreferenced | no page links it |
| `site/assets/03-Tagging.mp4` | 2026-05-30 | v1.4.1 | introduction | regenerated | recorded from the 2.0 Electron app (`frontend/e2e/screenshots/videos.spec.js`) |
| `site/assets/04-SmartScore.mp4` | 2026-05-30 | v1.4.1 | introduction | stale, manual | screen recording; needs a library with its own tags and scores, by hand |
| `site/assets/05-SemanticSearch.mp4` | 2026-05-30 | v1.4.1 | introduction, index | stale, manual | screen recording; needs a library with its own embeddings, by hand |
| `site/assets/06-Export.mp4` | 2026-05-30 | v1.4.1 | introduction | regenerated | recorded from the 2.0 Electron app (`frontend/e2e/screenshots/videos.spec.js`) |
| `site/assets/07-CreatingToken.mp4` | 2026-05-30 | v1.4.1 | introduction | stale, manual | screen recording |
| `site/assets/08-ComfyUI-FaceSearch.mp4` | 2026-05-30 | v1.4.1 | comfyui, introduction | stale, manual | screen recording with ComfyUI |
| `site/assets/09-ComfyUI-OutPaint.mp4` | 2026-05-30 | v1.4.1 | comfyui, introduction | stale, manual | screen recording with ComfyUI |
| `site/assets/ComfyAdapterLoader.jpg` | 2026-10-18 | v1.12.0rc3 | comfyui | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ComfyAdapterPicker.jpg` | 2026-10-18 | v1.12.0rc3 | comfyui | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ComfyCheckpointPicker.jpg` | 2026-10-18 | v1.12.0rc3 | comfyui | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ComfyFaceLikenessGate.jpg` | 2026-06-05 | v1.5.1 | comfyui | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ComfyFaceLikenessGateUpscale.jpg` | 2026-06-05 | v1.5.1 | comfyui | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ComfyImageEdit.jpg` | 2026-06-05 | v1.5.1 | comfyui | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ComfyInstallation.jpg` | 2026-06-05 | v1.5.1 | comfyui | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ComfyOutpaint.jpg` | 2026-06-05 | v1.5.1 | comfyui | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ComfyPictureLikenessGate.jpg` | 2026-10-18 | v1.12.0rc3 | comfyui | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ComfyResult.jpg` | 2026-06-05 | v1.5.1 | comfyui | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ComfyUpscale.jpg` | 2026-06-05 | v1.5.1 | comfyui | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ComfyWorkflow.png` | 2026-05-18 | v1.2.1 | api, comfyui | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ComfyWorkflow2.jpg` | 2026-05-18 | v1.2.1 |  | unreferenced | no page links it |
| `site/assets/ComparisonSlider.mp4` | 2026-10-25 | v1.13.0rc1 | features | stale, manual | 1.13 screen recording |
| `site/assets/ConnectComfyUI.jpg` | 2026-10-18 | v1.12.0rc3 | comfyui | stale, manual | needs a live ComfyUI passing the checks |
| `site/assets/DownloadQwen21.jpg` | 2026-10-25 | v1.13.0rc1 |  | unreferenced | no page links it |
| `site/assets/DuplicatesReview.mp4` | 2026-08-03 | v1.9.0-dev.2 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/EditInComfyUI.jpg` | 2026-10-18 | v1.12.0rc3 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/FaceLikenessSearch.jpg` | 2026-05-27 | v1.4.0 | comfyui, whatsnew | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/FixingWorkflows.mp4` | 2026-10-18 | v1.12.0rc3 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/InpaintAxe.gif` | 2026-10-25 | v1.13.0rc1 |  | unreferenced | no page links it |
| `site/assets/InpaintAxe.mp4` | 2026-10-25 | v1.13.0rc1 |  | unreferenced | no page links it |
| `site/assets/InpaintBlueLipstick.gif` | 2026-10-25 | v1.13.0rc1 |  | unreferenced | no page links it |
| `site/assets/InpaintBlueLipstick.mp4` | 2026-10-25 | v1.13.0rc1 |  | unreferenced | no page links it |
| `site/assets/InpaintBoth.gif` | 2026-10-25 | v1.13.0rc1 |  | unreferenced | no page links it |
| `site/assets/InpaintBoth.mp4` | 2026-10-24 | v1.13.0rc1 | features, index, whatsnew | stale, manual | 1.13 screen recording with ComfyUI |
| `site/assets/Inpainting.mp4` | 2026-10-24 | v1.13.0rc1 | features, whatsnew | stale, manual | 1.13 screen recording with ComfyUI |
| `site/assets/InpaintingFlux2.gif` | 2026-10-25 | v1.13.0rc1 |  | unreferenced | no page links it |
| `site/assets/InpaintingFlux2.jpg` | 2026-10-25 | v1.13.0rc1 |  | unreferenced | no page links it |
| `site/assets/InpaintingFlux2.mp4` | 2026-10-25 | v1.13.0rc1 |  | unreferenced | no page links it |
| `site/assets/InpaintingFlux2Klein.jpg` | 2026-10-25 | v1.13.0rc1 |  | unreferenced | no page links it |
| `site/assets/InpaintingOwnWorkflow.mp4` | 2026-10-24 | v1.13.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/InpaintingQwenImageEdit.jpg` | 2026-10-25 | v1.13.0rc1 |  | unreferenced | no page links it |
| `site/assets/LinkingComfyUIAndCharacter.mp4` | 2026-10-18 | v1.12.0rc3 | comfyui, introduction, whatsnew | stale, manual | 1.12 screen recording with ComfyUI |
| `site/assets/ModelDownload.jpg` | 2026-10-24 | v1.13.0rc1 | index, whatsnew | stale, manual | 1.13; needs a model download in flight |
| `site/assets/MultiLikenessSearch.jpg` | 2026-05-27 | v1.4.0 | comfyui, whatsnew | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/NewGridView.mp4` | 2026-07-27 | v1.8.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/OpenInComfyUI.jpg` | 2026-10-18 | v1.12.0rc3 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/OpenOriginalInComfyUI.jpg` | 2026-10-18 | v1.12.0rc3 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ReverseImageSearch.jpg` | 2026-09-02 | v1.11.0rc1 | features, whatsnew | regenerated | captured from the 2.0 Electron app |
| `site/assets/RunWorkflow.jpg` | 2026-10-18 | v1.12.0rc3 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/RunningWorkflow.mp4` | 2026-10-18 | v1.12.0rc3 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/SaveToPixlStash.jpg` | 2026-10-18 | v1.12.0rc3 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotAddLibrary.jpg` | 2026-09-02 | v1.11.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotAiToolkitImport.jpg` | 2026-08-18 | v1.10.0-dev.4 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotApp.jpg` | 2026-09-02 | v1.11.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotBackend.jpg` | 2026-09-02 | v1.11.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotBreadcrumb.jpg` | 2026-09-02 | v1.11.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotCharacters.jpg` | 2026-09-02 | v1.11.0rc1 | features | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotChat1.jpg` | 2026-05-30 | v1.4.1 | api | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ScreenshotChat2.jpg` | 2026-05-30 | v1.4.1 | api | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ScreenshotChat3.jpg` | 2026-05-30 | v1.4.1 | api | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ScreenshotCli.jpg` | 2026-08-18 | v1.10.0-dev.4 | whatsnew | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ScreenshotCliLibraries.jpg` | 2026-08-18 | v1.10.0-dev.4 | whatsnew | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ScreenshotCliPlugins.jpg` | 2026-08-18 | v1.10.0-dev.4 | whatsnew | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ScreenshotComfyUi.jpg` | 2026-05-15 | v1.2.0rc4 | features, index | regenerated | the 2.0 Workflows page, with the capture's seeded workflows; no ComfyUI connected |
| `site/assets/ScreenshotContext.jpg` | 2026-09-02 | v1.11.0rc1 | features, whatsnew | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotDeleteLora.jpg` | 2026-08-18 | v1.10.0-dev.4 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotDemo.jpg` | 2026-05-16 | v1.2.0 | features | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotDragCharacters.jpg` | 2026-05-31 | v1.5.0.dev0 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotDuplicates.jpg` | 2026-08-03 | v1.9.0-dev.2 | features, whatsnew | stale, manual | needs a finished duplicate scan with useful groups |
| `site/assets/ScreenshotEmptyLibrary.jpg` | 2026-09-02 | v1.11.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotExportFolder.jpg` | 2026-09-02 | v1.11.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotFileManager.jpg` | 2026-06-13 | v1.6.0rc2 |  | unreferenced | no page links it |
| `site/assets/ScreenshotGrid.jpg` | 2026-09-02 | v1.11.0rc1 | features, README.md | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotGridDark.jpg` | 2026-04-01 | v1.0.0rc1 |  | unreferenced | no page links it |
| `site/assets/ScreenshotGridGlobal.jpg` | 2026-04-01 | v1.0.0rc1 |  | unreferenced | no page links it |
| `site/assets/ScreenshotGridSelection.jpg` | 2026-09-02 | v1.11.0rc1 | features | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotGridSimilarity.jpg` | 2026-09-02 | v1.11.0rc1 | features | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotIconColor.jpg` | 2026-05-15 | v1.2.0rc4 | features, whatsnew | stale, manual | set icon picker; could become a scene |
| `site/assets/ScreenshotImageOverlay.jpg` | 2026-09-02 | v1.11.0rc1 | features | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotImageOverlay2.jpg` | 2026-09-02 | v1.11.0rc1 | features | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotImageOverlay3.jpg` | 2026-04-01 | v1.0.0rc1 |  | unreferenced | no page links it |
| `site/assets/ScreenshotInstallId.jpg` | 2026-08-03 | v1.9.0-dev.2 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotJoyCaption.jpg` | 2026-05-25 | v1.3.0 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotKeepCoverOnly.jpg` | 2026-08-03 | v1.9.0-dev.2 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotKeepCoverOnly2.jpg` | 2026-08-03 | v1.9.0-dev.2 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotKeyboard.jpg` | 2026-05-31 | v1.5.0.dev0 | features | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotLibraries.jpg` | 2026-08-18 | v1.10.0-dev.4 | features, whatsnew | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotLibrariesManage.jpg` | 2026-09-02 | v1.11.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotLmStudio.jpg` | 2026-05-30 | v1.4.1 | api | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ScreenshotLockSets.jpg` | 2026-07-20 | v1.7.0rc5 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotMain.jpg` | 2026-09-02 | v1.11.0rc1 | index | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotMapPreview.jpg` | 2026-09-02 | v1.11.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotMapTree.jpg` | 2026-09-02 | v1.11.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotMixedStacks.jpg` | 2026-09-02 | v1.11.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotModelShelf.jpg` | 2026-08-18 | v1.10.0-dev.4 | features, whatsnew | regenerated | captured from the 2.0 Electron app; the shelf shows the capture's stand-in models only |
| `site/assets/ScreenshotMultiProject.jpg` | 2026-08-03 | v1.9.0-dev.2 | features, whatsnew | stale, manual | needs a person in two projects |
| `site/assets/ScreenshotMutuallyExclusive.jpg` | 2026-04-01 | v1.0.0rc1 |  | unreferenced | no page links it |
| `site/assets/ScreenshotOverlap.jpg` | 2026-04-27 | v1.1.0rc10 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotOverlapNew.jpg` | 2026-05-15 | v1.2.0rc4 | features | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotPermissionRepair.jpg` | 2026-08-18 | v1.10.0-dev.4 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotPhotographySaver.jpg` | 2026-05-30 | v1.4.1 | api | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/ScreenshotPictureStatistics.jpg` | 2026-09-02 | v1.11.0rc1 | features, whatsnew | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotPlugins.jpg` | 2026-05-15 | v1.2.0rc4 | features | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotPrivacy.jpg` | 2026-09-02 | v1.11.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotProject.jpg` | 2026-09-02 | v1.11.0rc1 | features | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotProject.png` | 2026-04-01 | v1.0.0rc1 |  | unreferenced | no page links it |
| `site/assets/ScreenshotReferenceFolders.jpg` | 2026-04-27 | v1.1.0rc10 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotReferenceFoldersNew.jpg` | 2026-05-15 | v1.2.0rc4 | (features) | deleted | the Reference folders card was dropped from the features page |
| `site/assets/ScreenshotReview1.jpg` | 2026-07-20 | v1.7.0rc5 | features, whatsnew | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotReview2.jpg` | 2026-07-20 | v1.7.0rc5 |  | unreferenced | no page links it |
| `site/assets/ScreenshotReview3.jpg` | 2026-07-20 | v1.7.0rc5 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotSearchEdit.jpg` | 2026-09-02 | v1.11.0rc1 | comfyui | restored | v1.4.1 original restored (the 1.11 run had overwritten it with the search box) |
| `site/assets/ScreenshotSegmentation.jpg` | 2026-07-20 | v1.7.0rc5 | features, whatsnew | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotSelectiveRestore.jpg` | 2026-09-02 | v1.11.0rc1 | features, whatsnew | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotSemanticSearch.jpg` | 2026-11-01 | v2.0.0.dev.1 | features | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotSettings.jpg` | 2026-07-20 | v1.7.0rc5 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotShare1.jpg` | 2026-05-15 | v1.2.0rc4 | features, whatsnew | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotShare2.jpg` | 2026-05-18 | v1.2.1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotSidebar1.jpg` | 2026-05-15 | v1.2.0rc4 |  | unreferenced | no page links it |
| `site/assets/ScreenshotSidebar2.jpg` | 2026-09-02 | v1.11.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotSnapshots.jpg` | 2026-09-02 | v1.11.0rc1 | features, whatsnew | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotStackFilter.jpg` | 2026-08-03 | v1.9.0-dev.2 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotStudio.jpg` | 2026-05-30 | v1.4.1 |  | unreferenced | no page links it |
| `site/assets/ScreenshotTagStatistics.jpg` | 2026-09-02 | v1.11.0rc1 | features, whatsnew | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotTaggers.jpg` | 2026-05-25 | v1.3.0 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotTagging.jpg` | 2026-09-02 | v1.11.0rc1 | features | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotTaskManager.jpg` | 2026-05-15 | v1.2.0rc4 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotToken.jpg` | 2026-05-29 | v1.4.1 |  | unreferenced | no page links it |
| `site/assets/ScreenshotTokens.jpg` | 2026-05-29 | v1.4.1 |  | unreferenced | no page links it |
| `site/assets/ScreenshotToolbar.jpg` | 2026-09-02 | v1.11.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotUndoHistory.jpg` | 2026-08-03 | v1.9.0-dev.2 | features, whatsnew | stale, manual | needs recent operations in the history |
| `site/assets/ScreenshotUrl.jpg` | 2026-05-25 | v1.3.0 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotUserSettings.jpg` | 2026-09-02 | v1.11.0rc1 |  | unreferenced | no page links it |
| `site/assets/ScreenshotWhatsNew1_2.jpg` | 2026-05-15 | v1.2.0rc4 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotWizard.jpg` | 2026-09-03 | v1.11.0rc1 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ScreenshotsJustified.jpg` | 2026-07-27 | v1.8.0rc1 | features, whatsnew | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotsJustifiedSettings.jpg` | 2026-07-27 | v1.8.0rc1 | features, whatsnew | regenerated | captured from the 2.0 Electron app |
| `site/assets/ScreenshotsUserSettings.jpg` | 2026-09-02 | v1.11.0rc1 |  | unreferenced | no page links it |
| `site/assets/ScreenshotsUserSettings.png` | 2026-05-29 | v1.4.1 |  | unreferenced | no page links it |
| `site/assets/SemanticSearch.jpg` | 2026-09-02 | v1.11.0rc1 | comfyui, whatsnew | restored | v1.4.0 original restored (the 1.11 run had overwritten it with the search box) |
| `site/assets/SmartScreen.jpg` | 2026-07-31 | v1.8.2rc1 | install | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/SmartScreen2.jpg` | 2026-07-31 | v1.8.2rc1 | install | external | ComfyUI / LM Studio / Windows / terminal, not the app |
| `site/assets/SuggestMorePictures.mp4` | 2026-08-03 | v1.9.0-dev.2 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/TemplateDownloads.jpg` | 2026-10-24 | v1.13.0rc1 | index, upgrade, whatsnew | stale, manual | 1.13; needs a live ComfyUI |
| `site/assets/Testimonial1.jpg` | 2026-03-13 | v0.9.7 |  | unreferenced | no page links it |
| `site/assets/Testimonial1.png` | 2026-03-09 | v0.4.0 |  | unreferenced | no page links it |
| `site/assets/Testimonial2.jpg` | 2026-03-13 | v0.9.7 |  | unreferenced | no page links it |
| `site/assets/Testimonial2.png` | 2026-03-09 | v0.4.0 |  | unreferenced | no page links it |
| `site/assets/VideoHat.webp` | 2026-03-22 | v1.0.0b4 |  | unreferenced | no page links it |
| `site/assets/VideoMain.mp4` | 2026-08-04 | v1.9.0-dev.2 | index | stale, manual | screen recording (home page hero) |
| `site/assets/VideoMain.webp` | 2026-05-15 | v1.2.0rc4 |  | unreferenced | no page links it |
| `site/assets/VideoScaling.webp` | 2026-03-22 | v1.0.0b4 |  | unreferenced | no page links it |
| `site/assets/VideoSimilarity.webp` | 2026-03-22 | v1.0.0b4 |  | unreferenced | no page links it |
| `site/assets/WaitingForGPU.png` | 2026-10-24 | v1.13.0rc1 | index, whatsnew | stale, manual | 1.13; needs a live ComfyUI run |
| `site/assets/WhereIsUserSettings.jpg` | 2026-05-29 | v1.4.1 |  | unreferenced | no page links it |
| `site/assets/WorkflowClementine.mp4` | 2026-10-18 | v1.12.0rc3 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/WorkflowParameters.mp4` | 2026-10-18 | v1.12.0rc3 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/WorkflowPictures.mp4` | 2026-10-18 | v1.12.0rc3 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/WorkflowSetMOSS.mp4` | 2026-10-21 | v1.12.0 |  | unreferenced | no page links it |
| `site/assets/WorkflowSets.jpg` | 2026-10-18 | v1.12.0rc3 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/WorkflowSets.mp4` | 2026-10-18 | v1.12.0rc3 |  | unreferenced | no page links it |
| `site/assets/Workflows.jpg` | 2026-10-18 | v1.12.0rc3 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/WorkflowsMOSS.mp4` | 2026-10-21 | v1.12.0 |  | unreferenced | no page links it |
| `site/assets/WorkflowsMultipleLoRAs.mp4` | 2026-10-18 | v1.12.0rc3 | whatsnew | historical | only in What's New, beside the release it shows |
| `site/assets/ai-toolkit.gif` | 2026-05-18 | v1.2.1 |  | unreferenced | no page links it |
| `site/assets/ai-toolkit.mp4` | 2026-05-30 | v1.4.1 | api | stale, manual | screen recording |
| `site/assets/demo-banner.svg` | 2026-05-10 | v1.1.2 | README.md | current | branding |
| `site/assets/docker-mark-black.svg` | 2026-03-12 | v0.4.0 | install | current | branding |
| `site/assets/install-banner.svg` | 2026-03-12 | v0.4.0 | README.md | current | branding |
| `site/assets/logo.png` | 2026-07-24 | v1.7.1 | demo-holiday, nav.js | current | branding |
| `site/assets/upgrade-banner.svg` | 2026-03-12 | v0.4.0 | README.md | current | branding |
| `pixlstash/data/scalar-assets/ScreenshotsUserSettings.jpg` | 2026-05-29 | v1.4.1 | API docs | regenerated | captured from the 2.0 Electron app; the next API-docs build publishes it |
| `pixlstash/data/scalar-assets/ScreenshotToken.jpg` | 2026-05-29 | v1.4.1 | API docs | regenerated | captured from the 2.0 Electron app; the next API-docs build publishes it |
| `pixlstash/data/scalar-assets/ScreenshotTokens.jpg` | 2026-05-29 | v1.4.1 | API docs | regenerated | captured from the 2.0 Electron app; the next API-docs build publishes it |
| `pixlstash/data/scalar-assets/WhereIsUserSettings.jpg` | 2026-05-29 | v1.4.1 | API docs | regenerated | captured from the 2.0 Electron app; the next API-docs build publishes it |

## Versioned API docs

`site/api/v1.3/` to `site/api/v1.12/` each hold a copy of
`scalar-assets` as it was when that version's docs were published: the four
screenshots above and `logo.png` (branding, not listed).
They are **historical** and unchanged: each documents its own version. The 2.0
docs (`scripts/generate_openapi_docs.py`) will copy the regenerated set above.

