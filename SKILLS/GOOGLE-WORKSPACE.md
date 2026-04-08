# SKILL.md — Google Workspace & Cloud Tools

## Domain
Google Workspace: Google Docs (document creation, collaboration, comments), Google Sheets (spreadsheets, formulas, data analysis), Google Slides (presentations), Google Forms (surveys, data collection), Google Drive (file organization, sharing, permissions)

## When to Use
- Collaborative document editing assignments (Google Docs)
- Spreadsheet analysis or data projects (Google Sheets)
- Presentation delivery on web (Google Slides)
- Survey or data collection projects (Google Forms)
- File sharing or team project requirements
- Cloud-based coursework or group work

---

## Assignment Analysis Pattern for Google Workspace

### 1. **Google Docs Requirements**
   - Collaborative editing (multiple contributors)
   - Comment and suggestion tracking
   - Document structure (headings, outline)
   - Formatting consistency
   - Sharing and permission settings
   - Comment resolution workflow
   - Version history tracking

### 2. **Google Sheets Requirements**
   - Real-time data updates
   - Formula sharing and collaboration
   - Data validation and input restrictions
   - Protection of key ranges
   - Sharing calculated results
   - Conditional formatting visibility
   - Integration with Forms if data collection needed

### 3. **Google Slides Requirements**
   - Web-based presentation (no download needed)
   - Presenter view for remote presentations
   - Speaker notes
   - Shared editing capabilities
   - Animation and transition support
   - Embedded media (videos, images)

### 4. **Google Forms Requirements**
   - Survey design (question types)
   - Response collection and analysis
   - Automatic grading (if quiz)
   - Response notifications
   - Data export to Sheets
   - Branching or conditional questions

### 5. **Collaboration & Sharing**
   - Permission levels (viewer, commenter, editor)
   - Access control (who can view/edit)
   - File organization in Drive
   - Folder structure
   - Naming conventions
   - Backup and archival requirements

---

## Requirement Extraction Checklist

- [ ] **Google Docs**
  - [ ] Collaborative editing required?
  - [ ] Comment feature needed?
  - [ ] Outline/TOC requirements
  - [ ] Formatting style guide
  - [ ] Who has editor/viewer access?
  - [ ] Sharing link type (link only, domain, specific people)
  - [ ] Version history tracking needed?

- [ ] **Google Sheets**
  - [ ] Data structure and columns
  - [ ] Real-time collaboration required?
  - [ ] Protected ranges (what data is locked?)
  - [ ] Formulas and calculations
  - [ ] Data validation rules
  - [ ] Conditional formatting
  - [ ] Who can edit vs. view?

- [ ] **Google Slides**
  - [ ] Slide count
  - [ ] Real-time editing by team?
  - [ ] Presenter view requirements
  - [ ] Speaker notes per slide
  - [ ] Animation/transition types
  - [ ] Embedded media (videos, YouTube)
  - [ ] Download/export format needed?

- [ ] **Google Forms**
  - [ ] Question types (multiple choice, short answer, ranking)
  - [ ] Required vs. optional questions
  - [ ] Branching logic
  - [ ] Automatic grading (if quiz)
  - [ ] Response notifications
  - [ ] Data export requirements
  - [ ] Form submission settings (single vs. multiple)

- [ ] **Sharing & Permissions**
  - [ ] Who needs access?
  - [ ] Permission level per person (editor/commenter/viewer)
  - [ ] Public vs. restricted
  - [ ] Link sharing vs. domain only
  - [ ] Requires password?

---

## Common Pitfalls in Google Workspace Assignments

### Google Docs Pitfalls
- ❌ Not enabling comments/suggestion mode for feedback
- ❌ Too many people with editor access (chaos)
- ❌ Lost work because version history wasn't checked
- ❌ Broken sharing link (link requires being logged in)
- ❌ Copy-paste from other sources loses formatting
- ❌ Not resolving all comments before submission

**Fix:** Use suggestion mode for feedback. Set proper access levels. Resolve comments explicitly.

### Google Sheets Pitfalls
- ❌ Unprotected key ranges (can be accidentally edited)
- ❌ Formulas referencing deleted rows (breaks calculations)
- ❌ Not using data validation (garbage data entered)
- ❌ Hardcoded values instead of formulas
- ❌ Color formatting only (colorblind accessibility issue)
- ❌ Shared sheet with incorrect permission levels

**Fix:** Protect input areas. Use data validation. Use formulas, not values. Set minimum access needed.

### Google Slides Pitfalls
- ❌ Presenter view not tested for remote presentation
- ❌ Embedded videos not working (file size, permissions)
- ❌ Speaker notes not visible or complete
- ❌ Animations that play during actual presentation unexpectedly
- ❌ Slides that need speaker to comment (should be on slide)
- ❌ Not testing link sharing (what if others can't access?)

**Fix:** Test presenter view. Include speaker notes. Keep text minimal. Test sharing link as guest.

### Google Forms Pitfalls
- ❌ Form still accepting responses after deadline
- ❌ No confirmation message after submission
- ❌ Responses not linked to Google Sheet for analysis
- ❌ Required questions that prevent form completion
- ❌ Images or formatting not displaying correctly
- ❌ Auto-grading with insufficient answer key

**Fix:** Close form after deadline. Test all question types. Link to Sheets for analysis. Test as respondent.

### Sharing & Permissions Pitfalls
- ❌ Using "anyone with link" for sensitive documents
- ❌ Giving editor access to people who only need to view
- ❌ Sharing link that requires login (excludes external viewers)
- ❌ Not verifying who has access before submission
- ❌ Forgetting to revoke access after project ends

**Fix:** Use minimum required access. Test links as non-owner. Verify final access levels before submission.

---

## Validation Framework

### Google Docs Validation
```
Requirement: "Submit document with tracked comments resolved"
Validation:
✅ All comments addressed or resolved
✅ Document shared with correct access (comment link)
✅ No unresolved suggestions
✅ Final version clean for submission

Status: PASS
```

### Google Sheets Validation
```
Requirement: "Data validated and formulas calculate correctly"
Validation:
✅ Data validation applied to input columns
✅ All calculations use formulas (not hardcoded)
✅ Results match expected values
✅ Sheet protected where required
✅ Sharing permissions correct

Status: PASS
```

### Google Forms Validation
```
Requirement: "Survey with 10 questions, auto-scored, links to Sheets"
Validation:
✅ 10 questions present and properly formatted
✅ Auto-scoring configured
✅ Form linked to response sheet
✅ Responses auto-populate in Sheets
✅ Form closes on deadline

Status: PASS
```

---

## Testing Checklist (Google Workspace)

### Google Docs
- [ ] **Sharing & Access**
  - [ ] Document accessible via link ✓
  - [ ] Access level appropriate (viewer/commenter/editor) ✓
  - [ ] Non-owners can open without login (if public) ✓
  - [ ] Comments visible and resolvable ✓

- [ ] **Content & Formatting**
  - [ ] All required content included ✓
  - [ ] Formatting consistent ✓
  - [ ] Headings use proper hierarchy ✓
  - [ ] Comments/suggestions resolved ✓
  - [ ] No placeholder text remaining ✓

### Google Sheets
- [ ] **Data Integrity**
  - [ ] Data validation applied ✓
  - [ ] No invalid entries in validated cells ✓
  - [ ] Data types correct ✓
  - [ ] Protected ranges prevent accidental edits ✓

- [ ] **Calculations**
  - [ ] Formulas present (not hardcoded) ✓
  - [ ] Results accurate ✓
  - [ ] Formulas update with data changes ✓
  - [ ] No error values (like #REF!) ✓

- [ ] **Sharing**
  - [ ] Accessible via link ✓
  - [ ] Correct access level (can view but not edit?) ✓
  - [ ] Comments enabled if feedback expected ✓

### Google Slides
- [ ] **Functionality**
  - [ ] Link opens presentation ✓
  - [ ] Slide count meets requirements ✓
  - [ ] Presenter view works ✓
  - [ ] Speaker notes present ✓
  - [ ] Embedded media loads ✓

- [ ] **Design**
  - [ ] Consistent layout across slides ✓
  - [ ] Text readable ✓
  - [ ] Images high-resolution ✓
  - [ ] Master slide applied ✓

### Google Forms
- [ ] **Question Design**
  - [ ] All question types work ✓
  - [ ] Required vs. optional marked ✓
  - [ ] Branching logic functions ✓
  - [ ] Answer choices clear ✓

- [ ] **Responses & Scoring**
  - [ ] Responses collect properly ✓
  - [ ] Auto-scoring accurate (if applicable) ✓
  - [ ] Responses export to Sheets ✓
  - [ ] Confirmation message shows ✓

---

## Resources & References

- **Google Docs:** Google Docs Help Center
- **Google Sheets:** Google Sheets Function List
- **Google Slides:** Google Slides Templates
- **Google Forms:** Form Best Practices
- **Google Drive:** File Organization & Sharing

---

## When to Escalate to Commander

- Complex form branching with conditional logic
- API integrations (Zapier, Make, custom scripts)
- Advanced analytics or pivot tables
- Large-scale data collection (thousands of responses)
- Custom automation or App Script requirements
- Security or compliance requirements (data privacy)
