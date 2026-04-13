# Structure

## Top-Level Layout

- `wcs/`: English canonical skill package
- `wcs-cn/`: Simplified Chinese 1:1 mirror of the skill
- `README.md`: public entry point and installation guidance
- `LICENSE`: open-source license
- `docs/`: repository governance, status, and maintenance records

## Reference Files

- `wcs/references/api_reference.md`: index for loading WCS references
- `wcs/references/core_docs_template.md`: baseline doc-set template
- `wcs/references/coding_standard_template.md`: portable coding standard template
- `wcs/references/workflow_checklists.md`: end-to-end delivery checklists

## Maintainer Navigation

- Change the English skill behavior in `wcs/SKILL.md`
- Keep `wcs-cn/` structurally and semantically aligned when the English skill changes
- Change reusable process guidance in both `wcs/references/` and `wcs-cn/references/` as needed
- Record repository-level changes in `docs/dev_log.md`
- Keep public positioning in `README.md`
