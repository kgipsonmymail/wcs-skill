---
name: wcs
description: Unified cross-project coding standard skill that enforces document maintenance and pre-development gates before implementing any feature or bug fix. This skill should be used when starting, continuing, or reviewing software development tasks in any repository.
---

# WCS (Wind Code Standard)

## Purpose

Standardize development execution across different projects by enforcing:

1. Mandatory core document maintenance
2. Pre-development coding-standard gate
3. Test-first commit policy
4. Structured handoff records for multi-AI collaboration

Use this skill as a process controller, not only as writing guidance.

## When To Use

Trigger this skill in any of the following situations:

- Start a new feature in any repo
- Fix a bug or regression
- Continue unfinished work from another AI or engineer
- Prepare a commit or release handoff
- Audit whether project docs and implementation are aligned

## Core Rules

Execute all rules below unless the user explicitly overrides them.

1. Read project coding standards before writing code
2. Run implementation only after requirements and constraints are clear
3. **Verify all results against user requirements before reporting completion:**
   - Software/website outputs: validate via API, frontend functionality, or UI checks; fall back to code/interface inspection if runtime unavailable
   - Content outputs (docs, copy, configs): open and read the actual files to confirm content matches intent
4. Commit only after functional verification succeeds
5. Sync key docs after implementation and verification
5. Keep docs non-duplicative by linking to source docs instead of copy-pasting
6. Record issues and resolutions for future debugging and AI handoff

## Required Documents Baseline

Maintain the following documents in every project. If missing, create them first using `references/core_docs_template.md`.

- `README.md` (entry point, quick usage, doc navigation)
- `docs/project_status.md` (current architecture and feature status)
- `docs/structure.md` (directory and module mapping)
- `docs/dev_plan.md` (roadmap and pending tasks)
- `docs/dev_log.md` (implementation and verification logs)
- `docs/error_book.md` (bug root cause and resolution playbook)
- `docs/features.md` (implemented capability index)
- `docs/CODING_STANDARDS.md` (project coding standard charter)
- `docs/workflow.md` (execution flow agreement)
- `docs/prompt.txt` (AI collaboration prompts or constraints, if used by the project)

Allow project-specific additions, but do not remove the baseline set without user approval.

## Operating Workflow

Follow the checklist in `references/workflow_checklists.md`.

### Phase 0 - Initialize and Align

1. Locate existing coding standard docs (prefer `docs/CODING_STANDARDS.md`)
2. Detect missing baseline docs and scaffold them
3. Clarify feature/bug scope, constraints, and acceptance criteria
4. Confirm where source-of-truth content lives to avoid duplicated docs

### Phase 1 - Pre-Development Gate (Mandatory)

Before code edits, complete all items:

- Read coding standard and workflow docs
- Define implementation plan tied to acceptance criteria
- Define validation plan (unit/manual/integration as applicable)
- Identify files and modules that will change
- Prepare rollback strategy for risky changes

Stop implementation if this gate is not completed.

### Phase 2 - Implement with Standard Discipline

- Implement minimal, correct solution first; optimize second
- Preserve single responsibility and explicit naming
- Externalize environment-specific configuration
- Add or update tests relevant to the change
- Keep diffs focused; avoid unrelated refactors

### Phase 3 - Verify Before Commit

- Run required tests/checks for changed scope
- Verify affected user flow end-to-end
- Confirm no blocker-level lint/type/build failures
- **Self-verify results against user requirements before reporting completion:**
  - For software/website outputs: validate via backend API checks, frontend functionality tests, or UI verification
  - For content outputs (docs, copy, configs): open or read the relevant files to confirm actual content matches intent
  - If full verification is infeasible (e.g., missing runtime), perform the highest available validation tier and document the limitation
- Summarize verification evidence in `docs/dev_log.md`

Do not commit when verification fails.

### Phase 4 - Documentation Sync After Verification

Update docs after tests pass:

- `docs/dev_log.md`: what changed, issues faced, how verified
- `docs/error_book.md`: root cause, failed attempts, final fix (if bug involved)
- `docs/project_status.md`: new behavior and usage impacts
- `docs/features.md`: new/updated capability items
- `docs/dev_plan.md`: mark done items and refine pending work
- `README.md`: update quickstart/doc index if user-facing behavior changed
- `docs/structure.md`: only if files/modules changed

### Phase 5 - Collaboration Handoff

Produce a concise handoff block containing:

- Task scope and outcome
- Files changed
- Verification performed
- Known limitations or risks
- Next recommended actions

Keep handoff machine-readable and easy for another AI to continue.

## Multi-AI Collaboration Conventions

- Use stable headings and consistent document schemas from `references/core_docs_template.md`
- Write change logs as factual records, not chat transcripts
- Record assumptions explicitly to reduce context loss
- Prefer link references across docs to avoid conflicting duplicated content
- Keep terminology consistent across planning, implementation, and status docs

## Output Contract For This Skill

When this skill is triggered, produce:

1. A pre-development gate checklist result
2. The implementation result and verification summary
3. A post-update document sync report (what was updated and why)
4. A final handoff note ready for another AI or engineer

## Paired Edition (wcs-cn)

A Simplified Chinese 1:1 mirror is maintained at `wcs-cn` in the same parent directory (`skills/wcs-cn`). Directory layout and `references/*.md` filenames match this skill.

- When editing this skill (`SKILL.md` or any file under `references/`), apply the same structural and semantic updates to `wcs-cn` in lockstep.
- If `wcs-cn` is edited first, mirror changes back to `wcs` so English and Chinese stay aligned.
- Keep file paths, commands, and commit-type tokens (for example `feat`, `fix`) identical to this edition; only natural-language prose differs in `wcs-cn`.
