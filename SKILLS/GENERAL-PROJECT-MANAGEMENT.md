# SKILL.md — General Project & Assignment Management

## Domain
Cross-project assignment principles: Requirement analysis, project planning, task breakdown, time estimation, quality validation, submission preparation, rubric interpretation, deadline management

## When to Use
- ANY assignment across ANY IT course or domain
- Initial assignment analysis and planning
- Task sequencing and prioritization
- Progress tracking and validation
- Submission checklist creation
- Rubric comprehension and validation

---

## Universal Assignment Analysis Process

### PHASE 1: Intake & Comprehension

**Goal:** Understand the complete assignment before taking action

1. **Read Full Assignment Document**
   - Read 100% of the assignment (don't skim)
   - Highlight or note: objectives, requirements, constraints, deadlines
   - Flag ambiguities or unclear sections

2. **Identify Assignment Type**
   - What domain? (Web, Database, Office, etc.)
   - What's the primary deliverable? (Website, report, presentation, code, data)
   - What's the learning outcome? (What skill are they testing?)

3. **Extract Success Criteria**
   - What does completion look like?
   - What's the grading rubric?
   - What are minimum requirements vs. bonus points?
   - When is it due?

4. **Flag Assumptions & Ambiguities**
   - What's unclear or contradictory?
   - What constraints are implicit (not stated)?
   - What prerequisites are assumed?
   - When should we ask for clarification?

---

### PHASE 2: Requirements Breakdown

**Goal:** Transform fuzzy assignment into crystal-clear requirements list

1. **List ALL Requirements** (Explicit + Implicit)
   ```
   Explicit Requirements:
   - "Form must include 4+ text inputs" ✓
   - "Must be styled with external CSS" ✓
   
   Implicit Requirements:
   - Form must be usable (keyboard accessible)
   - Form must work across browsers
   - Styling must be professional (inferred from "good design")
   - Documentation/comments must exist
   ```

2. **Categorize Requirements**
   - **Must Have** (deal-breaker if missing)
   - **Should Have** (expected, impacts grade)
   - **Nice to Have** (bonus, beyond requirements)

3. **Identify Conflicts**
   - Do any requirements conflict?
   - Which takes priority if conflict exists?
   - Escalate if unresolvable

4. **Define Acceptance Criteria**
   - How will we validate each requirement?
   - What does "done" look like for each?
   - What's the measurable test?

---

### PHASE 3: Task Sequencing

**Goal:** Create ordered, dependent task list

1. **Break Into Tasks**
   - What are the logical work units?
   - Each task should be 15-120 minutes effort
   - Each task should be testable independently

2. **Map Dependencies**
   - Which tasks must complete before others?
   - Identify blockers or bottlenecks
   - Can any tasks run in parallel?

3. **Estimate Effort**
   - Simple (15-30 min), Moderate (30-90 min), Complex (90+ min)
   - Be realistic; double initial estimates if uncertain
   - Include buffer time (20-30%) for unexpected issues

4. **Sequence Logic**
   - Plan before code/design
   - Build foundation before details
   - Test throughout, not just at end
   - Leave integration/final testing for end

---

### PHASE 4: Validation Planning

**Goal:** Define how we'll prove completion

1. **Create Validation Checklist**
   ```
   ✅ Requirement 1: Form has 4+ text inputs
      Test: Count input elements of type="text"
      Expected: 4 or more
      Status: [Will check at end]
   ```

2. **Identify Test Cases**
   - Happy path (normal use)
   - Edge cases (minimum/maximum inputs)
   - Error cases (invalid data)
   - Boundary conditions

3. **Plan for Rubric Validation**
   - Check 100% of rubric items before submission
   - Document where each rubric item is met
   - Flag any rubric items unclear or impossible

4. **Plan for Quality Gates**
   - Code review points
   - User testing checkpoints
   - Final validation before submission

---

## Assignment Architecture Template

Use this structure for EVERY assignment:

```
📋 MISSION BRIEF: [Assignment Name]
   Course: [Course ID & Name]
   Due Date: [Date]
   Submission Format: [How/where to submit]

🎯 MISSION: [1-2 sentence executive summary]

📚 CORE OBJECTIVES: 
   - [Learning objective 1]
   - [Learning objective 2]

✅ REQUIREMENTS (Categorized):
   MUST HAVE (5 total):
   - [ ] Requirement 1
   - [ ] Requirement 2
   
   SHOULD HAVE (3 total):
   - [ ] Requirement 3
   
   NICE TO HAVE (1 total):
   - [ ] Requirement 4

⚠️ CRITICAL CONSTRAINTS:
   - Deadline: [Date & Time]
   - Format: [File formats accepted]
   - Size limits: [If any]
   - Academic integrity: [Any special notes]

🚀 TASK SEQUENCE (with dependencies):
   1. [Task 1] - [Effort] - [Prerequisites: none]
   2. [Task 2] - [Effort] - [Prerequisites: Task 1]
   3. [Task 3] - [Effort] - [Prerequisites: Tasks 1-2]

📐 ACCEPTANCE CRITERIA:
   For each requirement, HOW will we validate it?
   Requirement 1: ✓ [Test method]
   Requirement 2: ✓ [Test method]

⚠️ GOTCHAS & COMMON MISTAKES:
   - [Pitfall 1 and how to avoid]
   - [Pitfall 2 and how to avoid]

📅 TIMELINE:
   Task 1-3: Week 1 (3 hours)
   Task 4: Week 2 (2 hours)
   Testing & Validation: Final 2 hours before due

🏁 SUBMISSION CHECKLIST:
   Before submitting, verify:
   - [ ] All requirements met
   - [ ] Quality standards met
   - [ ] Testing complete
   - [ ] File formats correct
   - [ ] Naming convention correct
   - [ ] Rubric 100% validated
   - [ ] Submission method correct
```

---

## Requirement Validation Strategies

### The Rubric is Ground Truth
```
Rubric says: "Form includes at least one fieldset and legend"
Assignment says: "Use semantic HTML"

Conflict? No, they complement.
But IF conflict exists → Follow RUBRIC (it's the grading guide)
```

### Implicit vs. Explicit Requirements

Ask yourself:
- Is it stated directly? (explicit - follow exactly)
- Is it heavily implied? (implicit - incorporate)
- Is it assumed knowledge? (implicit - incorporate)
- Is it optional? (nice to have - good to include)

### When Requirements Are Unclear

```
Unclear requirement: "Make form look professional"

Resolution Steps:
1. Check if rubric provides specifics ✓
2. Look for examples or screenshots ✓
3. Check course materials for style guide ✓
4. Ask instructor for clarification ✓
5. Use reasonable professional standards ✓
```

---

## Deadline & Timeline Management

### Work Backwards from Due Date

```
Due Date: Friday, 11:59 PM

Buffer (1 hour before deadline): Friday 10:59 PM
  - Final submission upload
  - Breathing room for technical issues

Testing & QA (1 day): Thursday-Friday
  - Run complete validation checklist
  - Fix any issues found

Execution (3-4 days): Monday-Wednesday
  - Do the work
  - Test incrementally

Planning & Setup (1 day): Sunday
  - Create mission brief
  - Set up project structure
  - Gather resources

Result: Start Sunday for Friday deadline (7 days total)
```

### Red Flags for Timeline Issues

- ❌ Assignment requires more days than available
- ❌ Prerequisites not yet completed
- ❌ Unclear requirements blocking progress
- ❌ Tools/software not yet learned

**Action:** Escalate to instructor or adjust scope/timeline

---

## Rubric Interpretation Guide

### Common Rubric Levels

```
Exemplary (A/4.0): Exceeds requirements
- All requirements met
- High quality execution
- Goes beyond minimum

Proficient (B/3.0): Meets requirements
- All requirements met
- Good quality execution
- Exactly as specified

Developing (C/2.0): Partially meets requirements
- Most requirements met
- Some quality issues
- Missing minor elements

Beginning (D/1.0): Minimally meets requirements
- Some requirements met
- Multiple quality issues
- Major elements missing

Incomplete (F/0): Does not meet requirements
- Requirements not met
- Submission incomplete
-Not graded
```

### Strategy: Aim for Exemplary

To score highest:
1. ✅ Meet all "Proficient" criteria
2. ✅ Add polish, refinement, edge case handling
3. ✅ Include thoughtful comments and documentation
4. ✅ Go slightly beyond stated requirements
5. ✅ Test thoroughly

---

## Quality Standards Across All Assignments

### Baseline Quality (Required for Any Score)
- [ ] Requirements met (100% of rubric items)
- [ ] No errors or crashes
- [ ] Clean, professional presentation
- [ ] Proper file naming and format
- [ ] Complete submission (all files included)

### Professional Quality (Aim for This)
- [ ] Requirements met + well-executed
- [ ] Code/work is clean and well-organized
- [ ] Thoughtful design choices
- [ ] Documentation/comments where helpful
- [ ] Thoroughly tested before submission
- [ ] Validated against rubric

### Exemplary Quality (Go Here If Time)
- [ ] Professional quality + refinement
- [ ] Attention to edge cases
- [ ] Performance or optimization
- [ ] Accessibility or usability enhancements
- [ ] Clear explanation of design decisions
- [ ] Goes slightly beyond assignment scope

---

## Submission Readiness Checklist

### 24 Hours Before Due Date

- [ ] **Functionality**
  - [ ] Works as specified (no errors)
  - [ ] All requirements met
  - [ ] Tested on submission platform
  - [ ] No files missing

- [ ] **Quality**
  - [ ] Professional presentation
  - [ ] Code/work is clean
  - [ ] No hardcoded test data
  - [ ] Proper file naming

- [ ] **Documentation**
  - [ ] Rubric items mapped (know where proof is)
  - [ ] Comments/documentation clear
  - [ ] Instructions included if needed
  - [ ] Screenshots or proof attached (if required)

- [ ] **Format**
  - [ ] File format correct
  - [ ] Naming convention correct
  - [ ] All files included
  - [ ] Compression if needed

- [ ] **Submission**
  - [ ] Know exactly where to submit
  - [ ] Know deadline (date AND time)
  - [ ] Submission format confirmed
  - [ ] Receipt/confirmation plan

### Final 1 Hour Before Deadline

- [ ] Log into submission system
- [ ] Verify no submission yet
- [ ] Upload/submit with 30 minutes to spare
- [ ] Confirm receipt/email confirmation
- [ ] Take screenshot of confirmation
- [ ] Breathe (you're done!)

---

## Escalation Criteria

Escalate to instructor/commander when:

- ❌ Requirements seem impossible or contradictory
- ❌ Prerequisites not yet covered in course
- ❌ Deadline conflicts with other assignments
- ❌ Rubric unclear or subjective
- ❌ Technical issues prevent completion
- ❌ Assignment scope seems inappropriate
- ❌ Academic integrity questions
- ❌ Need extended deadline or accommodations

**How to Escalate:** Email instructor with:
1. Specific issue (clear, not vague)
2. What you've tried
3. What you need (extension, clarification, accommodation)
4. Timeline if urgent

---

## Resources & References

- **MIT Time Management:** How to Manage 40 Hours a Week (students)
- **Rubric Interpretation:** Understanding Grade Rubrics
- **Project Planning:** Gantt Chart Basics
- **Requirements Gathering:** User Story Template

---

## When to Use Domain-Specific Skills

- HTML/CSS/JavaScript work → [WEB-DEVELOPMENT.md](WEB-DEVELOPMENT.md)
- Database or SQL → [DATABASE-DESIGN.md](DATABASE-DESIGN.md)
- Word/Excel/PowerPoint → [MICROSOFT-OFFICE.md](MICROSOFT-OFFICE.md)
- Google Docs/Sheets/Slides → [GOOGLE-WORKSPACE.md](GOOGLE-WORKSPACE.md)
- PDFs, diagrams, images → [DOCUMENTS-DIAGRAMS.md](DOCUMENTS-DIAGRAMS.md)
- Other domains → Ask, and we'll create the skill
