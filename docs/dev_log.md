# Development Log

## 2026-04-13 - Planning-document maintenance

### What changed

- Reworked `docs/dev_plan.md` into a clearer roadmap board with `done`, `next`, `todo`, and `watch` states
- Updated `README.md` and `docs/project_status.md` to point maintainers to the planning source of truth
- Updated `docs/features.md` so the capability index reflects the improved roadmap visibility

### Verification

- Reviewed `README.md`, `docs/dev_plan.md`, `docs/project_status.md`, and `docs/features.md` for consistent terminology
- Confirmed the repository still matches the WCS baseline document set

### Rollback

- Revert the latest documentation commit if the repository should return to the initial publication wording

## 2026-04-13 - Open-source packaging and publication

### What changed

- Copied the local `wcs` skill into a clean standalone repository
- Added `README.md`, `LICENSE`, `.gitignore`, and placeholder keep files
- Added the baseline `docs/` set required by WCS

### Verification

- Confirmed the original local skill existed at `C:\Users\wind\.codex\skills\wcs`
- Confirmed the copied repository contains `SKILL.md` and all `references/*.md` files
- Confirmed the local source did not contain `wcs-cn`, so the public package documents that gap explicitly

### Rollback

- Remove the `wcs-skill` working directory if publication should be abandoned

## 2026-04-13 - Add paired Chinese mirror

### What changed

- Copied the local `wcs-cn` skill into `wcs-cn/`
- Updated repository docs to reflect that both language editions are now published
- Added keep files so Git can retain the empty `wcs-cn/assets` and `wcs-cn/scripts` directories

### Verification

- Confirmed the local source existed at `C:\Users\wind\.codex\skills\wcs-cn`
- Confirmed `wcs-cn/` contains `SKILL.md` and the full `references/*.md` set
- Confirmed the repository remained on a clean `main` branch before the new commit

### Rollback

- Remove `wcs-cn/` and revert the documentation update commit if the mirror should not be published

## 2026-04-13 - Reorganize repository layout

### What changed

- Moved the English skill payload into `wcs/`
- Kept `wcs-cn/` as a sibling directory so both language editions now have parallel top-level locations
- Updated repository docs to point at `wcs/` and `wcs-cn/` instead of assuming the English edition lives at the repo root

### Verification

- Confirmed `wcs/` contains `SKILL.md`, `references/*.md`, `assets/.gitkeep`, and `scripts/.gitkeep`
- Confirmed `wcs-cn/` remains intact after the reorganization
- Confirmed repository-level docs reference the new paths

### Rollback

- Move the English payload back to the repository root and revert the documentation update commit if the split layout should be abandoned
