# King-GPA
 [![How to Use](https://img.shields.io/badge/guide-HOW--TO--USE-blue)](HOW_TO_USE.md)

King-GPA is an academic IT support system built to help turn assignment requirements into organized, high-quality deliverables through structured intake, execution support, validation, and packaging.

The system is designed for IT-focused academic work such as databases, programming assignments, web projects, networking tasks, cybersecurity papers, systems analysis work, and other technical deliverables.

King-GPA is built around a simple workflow:

1. intake the assignment
2. identify the assignment type
3. detect missing inputs or blockers
4. execute in the correct mode
5. validate against requirements
6. package final artifacts

The repo is also designed for coordinated multi-agent work:
- Codex = repo builder
- Claude = analyst and architect
- Copilot = Codespaces accelerator

King-GPA does not fake testing, screenshots, execution, software use, or proof of completion. It keeps generated work separate from verified work and makes manual boundaries explicit when required.

## Core Files
- `KING-GPA-DOCTRINE.md`
- `ARCHITECTURE.md`
- `TEAM-ROLES.md`
- `LIVE-BUILD-MODE.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/copilot-instructions.md`

## Quick Start / User Guide
- See the user-facing guide: `HOW_TO_USE.md` for a concise how-to and workflow steps.
- Example intake manifest: `intake/examples/intake_manifest.example.json` demonstrates the fields to collect during intake.

## Current Goal
Build a controlled, reusable repo system that can support a wide range of academic IT assignments without confusion, drift, or fake completion states.