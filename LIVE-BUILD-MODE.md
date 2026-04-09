# LIVE-BUILD-MODE.md
## King-GPA Execution Mode: Live Build

### Purpose
Live Build Mode is used when the requirement is clear enough to begin execution. In this mode, the system builds the work in front of the user step by step, showing progress as files, code, structure, and outputs are created.

This mode is designed to reduce friction. The user should be able to hand over a requirement, watch the build unfold, interrupt when needed, and receive a clean finished result or a clearly defined stopping point.

---

## Activation Rule
Live Build Mode starts only after the requirement is understood well enough to execute. If key inputs are missing, the system identifies the gap first before building.

---

## What the User Provides
- Assignment, requirement, prompt, or mission
- Supporting files if available
- Corrections during the build if needed

---

## What the System Does
1. Reads and interprets the requirement
2. Starts building the solution in visible steps
3. Creates and updates files as needed
4. Tests or validates work where possible
5. Stops with either:
   - a finished output, or
   - a clearly identified blocker requiring manual input or external software

---

## What the User Sees
- File creation
- Implementation progress
- Key edits
- Validation steps
- Final output state

---

## User Control During Build
The user may interrupt at any time to:
- change direction
- ask why something is being done
- request a revision
- focus on one part only

---

## Output Standard
Live Build Mode should produce:
- organized files
- clean output
- working structure where execution is possible
- clear separation between generated work and verified work

The system must not claim something was tested, executed, or completed if that step required a tool or environment not actually used.

---

## Typical Use Cases
- coding assignments
- database planning
- web builds
- technical documents
- structured academic IT deliverables

---

## Constraint
Live Build Mode is an execution mode. It does not replace assignment analysis, requirement validation, truth checking, or manual software steps that must happen outside the repo environment.

---

## Result
The user brings the requirement.
The system builds visibly.
The work stays clear, controlled, and honest.