# WCS Skill

WCS (Wind Code Standard) is a reusable skill for agent-driven software work. It enforces a stable execution model across repositories by requiring core project docs, a pre-development gate, verification before commit, and a structured handoff after delivery.

## What It Includes

- `SKILL.md`: the skill definition and operating contract
- `wcs-cn/`: the Simplified Chinese 1:1 mirror of the skill
- `references/`: reusable templates and workflow checklists
- `assets/`: reserved for future supporting assets
- `scripts/`: reserved for future automation helpers
- `docs/`: repository governance and maintenance records for this open-source package

## Quick Start

1. Copy the repository root into your local Codex skills folder as `wcs`.
2. If you want the Chinese mirror as well, copy `wcs-cn/` into the same parent skills directory.
3. Trigger `wcs` or `wcs-cn` by name when starting, continuing, or reviewing work in a repository.
4. Follow the generated gate, verification, document-sync, and handoff outputs.

## Repository Notes

- This repository was published from the local `wcs` and `wcs-cn` skills found under `~/.codex/skills/`.
- The repository root is the English `wcs` edition, and `wcs-cn/` contains the paired Simplified Chinese mirror.

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
