# Core Docs Template (Cross-Project)

Use this template to enforce a stable documentation system across different repositories.

## Required Files and Minimal Sections

### `README.md`
- Project overview
- Quick start
- Common commands
- Link map to `docs/` files

### `docs/project_status.md`
- Tech stack and architecture snapshot
- Implemented modules and current capabilities
- Runtime status, constraints, and known limitations

### `docs/structure.md`
- Directory tree (top-level and key submodules)
- Responsibility mapping for major files/modules
- Navigation tips for maintainers

### `docs/dev_plan.md`
- In-progress and pending tasks
- Priority, owner (optional), and target milestone
- Risk or dependency notes

### `docs/dev_log.md`
- Date and task title
- What was changed
- Validation evidence
- Rollback notes if relevant

### `docs/error_book.md`
- Symptom
- Root cause
- Failed attempts (optional but recommended)
- Final fix and prevention notes

### `docs/features.md`
- Feature list by module/domain
- Current status (`done`, `partial`, `planned`)
- Links to implementation docs or key files

### `docs/CODING_STANDARDS.md`
- Must-follow rules
- Naming and structure rules
- Testing and commit policy
- Documentation update policy

### `docs/workflow.md`
- End-to-end process from intake to handoff
- Quality gates
- Roles and collaboration conventions

### `docs/prompt.txt` (optional but recommended for AI-heavy workflows)
- Stable prompt constraints
- Collaboration principles across AI agents

## Granularity Rules

- Keep `README.md` concise and navigational
- Keep details in dedicated docs, referenced by links
- Avoid duplicated paragraphs across multiple files
- Prefer bullet records for logs and plans

## Update Trigger Rules

- Change in architecture/files: update `docs/structure.md` and `docs/project_status.md`
- New or changed capability: update `docs/features.md` and `docs/project_status.md`
- Bug fix: update `docs/error_book.md` and `docs/dev_log.md`
- Any delivered change: update `docs/dev_log.md`
