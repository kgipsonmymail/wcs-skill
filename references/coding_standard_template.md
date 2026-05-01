# Portable Coding Standard Template

Use this template as a starting point for `docs/CODING_STANDARDS.md` in a new project.

## 1. Must-Follow Rules

1. Commit only after verification passes
2. Record implementation and verification in `docs/dev_log.md`
3. Record bug root cause and fix in `docs/error_book.md`
4. Update impacted project docs after successful verification
5. Keep docs concise, linked, and non-duplicative

## 2. Development Principles

- Implement correctness first, then optimize
- Keep modules/functions single-responsibility
- Prefer explicit naming and clear boundaries
- Externalize environment/configuration values

## 3. Naming Conventions

- Files/modules: project convention (`snake_case` or `kebab-case`)
- Functions/methods: language convention
- Classes/types: language convention
- Constants: uppercase snake case (if language commonly uses it)

Document language-specific exceptions if needed.

## 4. Commit Convention

Format:

`<type>: <summary>`

Types:

- `feat`: new capability
- `fix`: bug fix
- `refactor`: structural improvement without behavior change
- `docs`: documentation update
- `chore`: maintenance task

## 5. Verification Policy

Before commit:

- Pass relevant tests
- Pass lint/type/build checks for changed scope
- **Validate results against user requirements:**
  - Software/website outputs (high complexity): validate via API, UI, or code/interface inspection as fallback
  - Content outputs: open/read actual files to confirm content correctness
- If full verification is infeasible, perform highest available tier and document limitation

If verification fails, fix first and do not commit.

## 6. Documentation Sync Policy

After verification passes, update:

- `docs/dev_log.md`
- `docs/error_book.md` (if applicable)
- `docs/features.md` (if capability changed)
- `docs/project_status.md` (if behavior/architecture changed)
- `docs/dev_plan.md` (progress and pending tasks)
- `README.md` and `docs/structure.md` when required

## 7. Collaboration and Handoff Policy

- Keep records factual and concise
- List assumptions explicitly
- Provide next actionable steps
- Ensure another AI/engineer can continue without hidden context
