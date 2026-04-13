# WCS Skill

WCS (Wind Code Standard) is a reusable skill for agent-driven software work. It enforces a stable execution model across repositories by requiring core project docs, a pre-development gate, verification before commit, and a structured handoff after delivery.

## What It Includes

- `SKILL.md`: the skill definition and operating contract
- `references/`: reusable templates and workflow checklists
- `assets/`: reserved for future supporting assets
- `scripts/`: reserved for future automation helpers
- `docs/`: repository governance and maintenance records for this open-source package

## Quick Start

1. Copy this directory into your local Codex skills folder as `wcs`.
2. Trigger the skill by name when starting, continuing, or reviewing work in a repository.
3. Follow the generated gate, verification, document-sync, and handoff outputs.

## Repository Notes

- This repository was published from the local `wcs` skill found under `~/.codex/skills/wcs`.
- `SKILL.md` references a paired `wcs-cn` mirror. That mirror was not present in the local source at publish time, so this repository currently contains only the English edition.

## Docs

- [Project status](docs/project_status.md)
- [Structure](docs/structure.md)
- [Development plan](docs/dev_plan.md)
- [Development log](docs/dev_log.md)
- [Error book](docs/error_book.md)
- [Features](docs/features.md)
- [Coding standards](docs/CODING_STANDARDS.md)
- [Workflow](docs/workflow.md)
- [Prompt constraints](docs/prompt.txt)

## License

MIT
