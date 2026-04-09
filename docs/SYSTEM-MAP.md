# docs/SYSTEM-MAP.md

## Purpose

This file gives a simple map of the current King-GPA repo so a human can understand the system quickly. It is an orientation document — not full documentation. Use it to see how the pieces fit together and where to look for each part of the workflow.

---

## Core Control Files

These live at the repo root and define how King-GPA operates across every assignment:

- [README.md](../README.md) — Top-level overview
- [KING-GPA-DOCTRINE.md](../KING-GPA-DOCTRINE.md) — Operating doctrine and truth boundaries
- [ARCHITECTURE.md](../ARCHITECTURE.md) — System architecture
- [TEAM-ROLES.md](../TEAM-ROLES.md) — Human and agent roles
- [LIVE-BUILD-MODE.md](../LIVE-BUILD-MODE.md) — Live build workflow rules
- [AGENTS.md](../AGENTS.md) — Agent coordination
- [CLAUDE.md](../CLAUDE.md) — Claude-specific guidance
- [.github/copilot-instructions.md](../.github/copilot-instructions.md) — Copilot-specific guidance

---

## Workflow Folders

Each folder holds a different stage of the King-GPA workflow:

- [docs/](../docs/) — Documentation, system maps, repo state
- [intake/](../intake/) — Assignment intake manifests and templates
- [pipelines/](../pipelines/) — Shared workflow stages (classification, gap detection, packaging)
- [skills/](../skills/) — Assignment-type support modules (database, programming, etc.)
- [templates/](../templates/) — Reusable output structures and checklists
- [qa/](../qa/) — Validation, requirement, completeness, and proof-boundary checks
- [outputs/](../outputs/) — Generated deliverables and prepared final artifacts
- [assignments/](../assignments/) — Real assignment working space

---

## Example Database Lane

The first full end-to-end example in the repo is the vet clinic database assignment. It exercises every stage of the workflow:

- [intake/examples/vet_clinic_assignment_manifest.example.json](../intake/examples/vet_clinic_assignment_manifest.example.json) — Intake manifest
- [skills/database/examples/vet_clinic_physical_model.md](../skills/database/examples/vet_clinic_physical_model.md) — Physical model
- [skills/database/examples/vet_clinic_access_build_sheet.md](../skills/database/examples/vet_clinic_access_build_sheet.md) — Microsoft Access build sheet
- [skills/database/examples/vet_clinic_part1_writeup_support.md](../skills/database/examples/vet_clinic_part1_writeup_support.md) — Part 1 writeup support
- [skills/database/examples/vet_clinic_part2_writeup_support.md](../skills/database/examples/vet_clinic_part2_writeup_support.md) — Part 2 writeup support
- [skills/database/examples/vet_clinic_workflow_summary.md](../skills/database/examples/vet_clinic_workflow_summary.md) — Workflow summary
- [qa/examples/vet_clinic_assignment_qa.md](../qa/examples/vet_clinic_assignment_qa.md) — QA snapshot
- [outputs/examples/vet_clinic_output_package.md](../outputs/examples/vet_clinic_output_package.md) — Output package definition

Supporting database skill files used by this lane:

- [skills/database/skill.md](../skills/database/skill.md)
- [skills/database/README.md](../skills/database/README.md)
- [skills/database/access_execution_boundary.md](../skills/database/access_execution_boundary.md)
- [skills/database/physical_model_template.md](../skills/database/physical_model_template.md)

---

## Current System State

King-GPA now has a **functioning database assignment support lane**. Intake, classification, gap detection, model planning, build support, writeup support, execution boundary, QA, and output packaging are all wired together through the vet clinic example and can be reused for real database assignments.

The system still needs:

- More skills built out (programming, web-development, networking, cybersecurity, systems-analysis, technical-writing, presentation, spreadsheet)
- Live execution testing against real assignments end-to-end
- Real proof artifacts (actual Access builds, real screenshots, assembled final documents) to validate the packaging and QA stages against completed work

---

## Rule

The system map should stay simple, current, and useful for orientation.
