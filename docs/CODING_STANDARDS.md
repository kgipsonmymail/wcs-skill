# Coding Standards

## Must-Follow Rules

1. Keep repository changes focused on the published `wcs` skill and its supporting docs.
2. Record implementation and verification facts in `docs/dev_log.md`.
3. Update affected docs after successful verification.
4. Keep repository text concise and avoid duplicated guidance across files.
5. Do not publish sensitive local environment details.

## Naming and Structure

- Markdown and reference files use existing `kebab-case` or established filenames
- The public repository preserves the local skill layout where possible
- New supporting files should remain clearly separated from the canonical skill content

## Verification Policy

- Validate that required files exist after structural changes
- Validate public-facing docs and links after documentation changes
- Do not create a release commit until the changed repository contents have been reviewed

## Commit Policy

- Use `<type>: <summary>`
- Keep the initial publication commit scoped to repository packaging and docs

## Documentation Policy

- Update `README.md` when installation or repository scope changes
- Update `docs/project_status.md` and `docs/structure.md` when structure changes
- Update `docs/features.md` when capabilities or packaged contents change
