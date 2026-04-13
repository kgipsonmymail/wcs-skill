# WCS Workflow Checklists

Use these checklists as mandatory execution gates.

## 1) Intake Checklist

- Confirm task type: `feature` / `bugfix` / `refactor` / `docs`
- Confirm acceptance criteria
- Confirm constraints (performance, security, compatibility, deadline)
- Confirm affected modules/files

## 2) Pre-Development Gate (Must Pass Before Coding)

- Read `docs/CODING_STANDARDS.md` (or equivalent standard file)
- Read project workflow and current status docs
- Write brief implementation plan
- Define verification strategy and commands
- Identify required docs to update after delivery

If any item is missing, pause coding and complete the gap.

## 3) Implementation Checklist

- Keep change scoped to the task
- Follow naming and module responsibility conventions
- Externalize config; avoid hardcoded sensitive values
- Add/update tests when feasible
- Keep backward compatibility unless requirements say otherwise

## 4) Verification Checklist

- Run relevant test commands
- Run lint/type/build checks relevant to changed scope
- Validate core user flow or API flow
- Capture key evidence in `docs/dev_log.md`

## 5) Docs Sync Checklist (After Verification Passes)

- Update `docs/dev_log.md`
- Update `docs/error_book.md` for bug or incident tasks
- Update `docs/features.md` for capability changes
- Update `docs/project_status.md` for behavior/architecture impact
- Update `docs/dev_plan.md` progress and next steps
- Update `README.md` index or usage notes if user-facing behavior changed
- Update `docs/structure.md` if directory/module structure changed

## 6) Commit Checklist

- Ensure verification passed
- Ensure required docs updated
- Use commit message format: `<type>: <summary>`
- Keep commit focused and reviewable

## 7) Handoff Checklist (For Multi-AI Collaboration)

- State objective and completion status
- List changed files
- List verification results and remaining risks
- List pending tasks and recommended next action
- Record assumptions and unresolved questions
