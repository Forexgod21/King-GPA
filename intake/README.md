# intake/

## Purpose

The intake folder holds structured assignment metadata before execution begins. Every assignment enters King-GPA through the intake phase.

---

## Workflow

1. Assignment is received
2. Manifest is created from assignment_manifest.template.json
3. Manifest is populated with assignment details
4. Manifest is validated to identify blockers before build begins
5. Assignment moves to execution when ready

---

## Manifest Fields

Every assignment gets a manifest first. The manifest identifies:

- **assignment_id** - unique identifier
- **assignment_title** - clear name
- **course** - course code or name
- **assignment_type** - identifies which workflow or skill applies
- **source_files** - list of provided files or attachments
- **required_outputs** - what the assignment asks for
- **software_required** - tools or software needed to execute
- **missing_inputs** - blockers or gaps detected before build
- **manual_steps_required** - steps that require external software or manual execution
- **ai_assistance_used** - whether AI is supporting the work
- **ai_assistance_scope** - what the AI is responsible for
- **current_stage** - where the assignment is in the workflow
- **status** - draft, ready, in_progress, done
- **notes** - any additional context or observations

---

## Rule

Do not start building until the manifest is complete and all blockers are identified.

If the manifest shows missing inputs or manual steps that require software outside the repo environment, that boundary must be clear before execution starts.

---

## Result

A clean intake manifest makes the rest of the workflow cleaner.

You know what you're building before you start.
You know what's blocked before wasting time.
You know what's manual vs. automated before execution.
