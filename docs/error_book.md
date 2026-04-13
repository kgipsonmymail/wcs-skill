# Error Book

## Current Known Issues

### Missing paired mirror

- Symptom: `SKILL.md` references `wcs-cn`, but no local `wcs-cn` directory was available during publication
- Root cause: local source inventory contained only the English `wcs` skill
- Final handling: publish the English edition only and document the missing mirror in `README.md` and `docs/project_status.md`
- Prevention: when `wcs-cn` is created or recovered, publish it in lockstep with `wcs`
