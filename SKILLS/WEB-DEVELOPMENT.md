# SKILL.md — Web Development (HTML/CSS/JavaScript)

## Domain
Web Development: HTML5 form building, CSS styling, JavaScript interaction, browser validation, deployment

## When to Use
- Any HTML/CSS/JavaScript assignment (forms, websites, dynamic content)
- Web-based projects or components
- Browser-based validation or interactivity
- Responsive design requirements

---

## Assignment Analysis Pattern for Web Dev

When analyzing a web development assignment:

### 1. **Markup Requirements** (HTML Layer)
   - Form elements vs. semantic structure vs. layout
   - Accessibility requirements (labels, alt text, ARIA)
   - Nesting and hierarchy rules
   - Required attributes (type, name, value, id)
   - Form submission behavior (action, method)

### 2. **Styling Requirements** (CSS Layer)
   - Layout system (flexbox, grid, float, positioning)
   - Visual styling (colors, borders, shadows, spacing)
   - Responsive breakpoints and media queries
   - Form element styling constraints
   - Pseudo-classes and states (:hover, :focus, :disabled)

### 3. **Interaction Requirements** (JavaScript Layer)
   - Client-side validation rules
   - Event handlers and listeners
   - DOM manipulation and updates
   - Form submission handling
   - Error messaging and feedback

### 4. **Deployment Requirements**
   - File naming conventions (.html, .css, .js separation)
   - Folder structure and path references
   - Server deployment (if required)
   - Testing across browsers
   - URL validation for submissions

---

## Requirement Extraction Checklist

For HTML/CSS/JavaScript missions, extract:

- [ ] **HTML Structure**
  - [ ] Form vs. page layout requirements
  - [ ] Required elements (form, fieldset, legend, label, input, textarea, select, button)
  - [ ] Input types needed (text, email, tel, date, time, password, checkbox, radio, submit)
  - [ ] Accessibility requirements (ARIA, semantic HTML)
  - [ ] Content and placeholder requirements

- [ ] **CSS Styling**
  - [ ] Layout approach (flexbox/grid/float)
  - [ ] Color scheme (background, borders, text)
  - [ ] Typography (font, size, weight, line-height)
  - [ ] Spacing (margin, padding)
  - [ ] States (:focus, :hover, :disabled)
  - [ ] Responsive design (mobile-first or breakpoints)

- [ ] **JavaScript Interaction**
  - [ ] Form validation (client-side rules)
  - [ ] Error message display
  - [ ] Form submission handling
  - [ ] Event listeners and triggers
  - [ ] Dynamic element creation or updates

- [ ] **Testing & Validation**
  - [ ] Browser compatibility (Chrome, Firefox, Safari, Edge)
  - [ ] Responsive testing (mobile, tablet, desktop)
  - [ ] Form submission and server integration
  - [ ] Accessibility testing (keyboard nav, screen readers)
  - [ ] Cross-page consistency (if multiple pages)

---

## Common Pitfalls in Web Dev Assignments

### HTML Pitfalls
- ❌ Forgetting `name` attribute on form inputs (can't submit data)
- ❌ Using `<button>` instead of `<input type="submit">` (wrong element type)
- ❌ Not wrapping labels with form elements properly
- ❌ Mixing up `<fieldset>` purpose (it's for grouping RELATED fields, not layout)
- ❌ Radio buttons/checkboxes with wrong `name` attribute (breaks grouping logic)

**Fix:** Every form element MUST have `name` and `id`. Labels must reference inputs via `for` attribute.

### CSS Pitfalls
- ❌ Overly specific selectors that prevent reusability
- ❌ Using `!important` to "fix" styling problems (masks real issues)
- ❌ Inline styles instead of external stylesheet
- ❌ Not testing on mobile (responsive design broken)
- ❌ Form elements display inline when they should be block (or vice versa)

**Fix:** Use classes, avoid inline styles, test responsive at each step.

### JavaScript Pitfalls
- ❌ Validation only on submit instead of during input
- ❌ Not preventing default form submission `e.preventDefault()`
- ❌ Selecting DOM elements after page load completes (timing issues)
- ❌ Not clearing form data after successful submission
- ❌ Error messages not visible or easily readable

**Fix:** Add event listeners early, validate as user types, handle edge cases.

### Deployment Pitfalls
- ❌ Relative paths broken when moved to server
- ❌ Not testing on actual deployed URL before submission
- ❌ Uploading to wrong folder/path
- ❌ Forgetting to upload all files (CSS, JS files left local)
- ❌ Mixed protocols (http vs https) causing security warnings

**Fix:** Test everything on the actual server URL before final submission.

---

## Validation Framework

### During Development (Per-Requirement Validation)
Each requirement should be tested independently:

```html
✅ Form element requirement:
   - Does the input have name attribute? YES
   - Does the input have type attribute? YES
   - Does the label reference this input? YES
   - Does the input display correctly? YES
   
✅ CSS requirement:
   - Is the style in external stylesheet? YES
   - Does the style apply to all form elements? YES
   - Does it work on mobile? YES
```

### Before Submission (Rubric Validation)
Check 100% of rubric requirements:

```
Rubric Item: "Form includes 4+ text-based input fields"
   Required: text, email, tel, password (or similar)
   Status: ✅ 5 text inputs found (exceeds requirement)
   
Rubric Item: "CSS includes border or background color for form"
   Required: Either border OR background color
   Status: ✅ Border #333 and background #f5f5f5 applied
```

---

## Code Quality Standards for Web Dev

### HTML Standards
- Valid HTML5 (use validator.w3.org)
- Proper semantic structure
- ARIA roles where needed
- No empty or unused elements
- Consistent indentation

### CSS Standards
- Organized by component (form, inputs, buttons, responsive)
- No unused or dead CSS
- Consistent naming (BEM or similar)
- Mobile-first approach if responsive
- Comments for complex selectors

### JavaScript Standards
- No console errors or warnings
- Proper error handling (try/catch)
- Comments explaining complex logic
- No global variables
- Follows DRY principle (Don't Repeat Yourself)

---

## Testing Checklist (Web Dev)

Before marking complete:

- [ ] **Functionality**
  - [ ] Form submits without errors
  - [ ] All inputs capture user data correctly
  - [ ] Validation works (prevents invalid submission)
  - [ ] Error messages display properly
  - [ ] Success messages/redirects work

- [ ] **Styling**
  - [ ] Form has border or background color ✓
  - [ ] Form has defined width ✓
  - [ ] All form elements have defined display property ✓
  - [ ] Inputs and labels are properly sized ✓
  - [ ] Padding and spacing are consistent ✓

- [ ] **Compatibility**
  - [ ] Works in Chrome ✓
  - [ ] Works in Firefox ✓
  - [ ] Works on mobile (< 768px) ✓
  - [ ] Keyboard navigation works (Tab through form) ✓

- [ ] **Accessibility**
  - [ ] All inputs have labels ✓
  - [ ] Labels associate with inputs ✓
  - [ ] Form can be completed with keyboard only ✓
  - [ ] Error messages are screen-reader friendly ✓

- [ ] **Code Quality**
  - [ ] No console errors ✓
  - [ ] Indentation is consistent ✓
  - [ ] No unused code ✓
  - [ ] Comments explain complex sections ✓

---

## Resources & References

- **HTML Form Reference:** MDN Web Docs - HTML Forms
- **CSS Reference:** MDN Web Docs - CSS Learning Area
- **JavaScript Validation:** Form Validation Best Practices
- **Accessibility:** WCAG 2.1 Guidelines
- **Testing:** Browser DevTools (F12 or Cmd+Option+I)

---

## When to Escalate to Commander

- Security requirements beyond basic client-side validation
- Complex form workflows with multiple steps
- Backend integration or server-side processing
- Accessibility requirements beyond WCAG 2.1 Level A
- Conflicting requirements between HTML and styling
