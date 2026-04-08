# SKILL.md — Documents, Diagrams & Visual Artifacts

## Domain
Document handling and visualization: PDF creation and editing, image creation and optimization, Visio diagramming (flowcharts, ERDs, network diagrams), infographics, wireframes, screenshots with annotations

## When to Use
- Document conversion or PDF manipulation assignments
- Image editing or graphic creation requirements
- Diagram creation (flowcharts, process diagrams, system architecture)
- Visual design or prototype assignments
- Screenshots and visual documentation
- Presentation mockups or wireframes

---

## Assignment Analysis Pattern for Visual Work

### 1. **PDF Requirements**
   - Creation from existing documents
   - Merging multiple PDFs
   - Extracting specific pages
   - Annotation or markup needs
   - Form filling and flattening
   - Compression or optimization
   - Security (encryption, password protection)

### 2. **Image & Graphics Requirements**
   - Format needed (PNG, JPG, GIF, SVG, WebP)
   - Resolution and size specifications
   - Color space (RGB, CMYK, grayscale)
   - Transparency or opacity needs
   - Compression without quality loss
   - Accessibility (alt text, descriptive filenames)

### 3. **Diagram Requirements**
   - Diagram type (flowchart, ERD, wireframe, network, org chart)
   - Notation standard (Crow's Foot, UML, DFD, etc.)
   - Symbol meanings and legend
   - Connections and relationships
   - Labels and annotations
   - Professional appearance and consistency

### 4. **Infographic/Design Requirements**
   - Visual hierarchy and layout
   - Color palette and branding
   - Typography choices
   - Data visualization (charts, graphs)
   - Accessibility compliance
   - Print vs. web optimization

### 5. **Wireframe/Prototype Requirements**
   - Low-fidelity vs. high-fidelity
   - Responsive breakpoints (mobile, tablet, desktop)
   - Interactive elements or annotations
   - User flow or navigation
   - Accessibility annotations

---

## Requirement Extraction Checklist

- [ ] **PDFs**
  - [ ] Source format (Word, images, website)
  - [ ] Merge or separate required?
  - [ ] Editable or flattened PDF?
  - [ ] Page orientation (portrait/landscape)
  - [ ] Compression level acceptable?
  - [ ] Password protection or encryption?
  - [ ] Metadata or properties needed?

- [ ] **Images**
  - [ ] Format requirements (PNG/JPG/GIF/SVG)
  - [ ] Resolution (72 DPI web, 300 DPI print)
  - [ ] Size/dimensions specifications
  - [ ] Color space (RGB/CMYK/grayscale)
  - [ ] Transparency support needed?
  - [ ] Optimization for web or print?
  - [ ] Alt text or caption required?

- [ ] **Diagrams**
  - [ ] Diagram type (flowchart, ERD, wireframe, org chart)
  - [ ] Notation standard or template
  - [ ] Shapes and symbols needed
  - [ ] Connections (solid, dashed, directional)
  - [ ] Labels and legend
  - [ ] Color scheme requirements
  - [ ] Export format (PNG, PDF, Visio, SVG)

- [ ] **Infographics/Design**
  - [ ] Data to visualize
  - [ ] Visual style (minimalist, detailed, cartoon, realistic)
  - [ ] Color palette (branded colors)
  - [ ] Typography (font families, sizes)
  - [ ] Layout style (vertical, horizontal, modular)
  - [ ] Print or digital format?
  - [ ] Accessibility requirements (high contrast, readable fonts)

- [ ] **Wireframes/Prototypes**
  - [ ] Fidelity level (low/medium/high)
  - [ ] Responsive breakpoints to show
  - [ ] Interactive elements (buttons, forms)
  - [ ] User flow or navigation paths
  - [ ] Annotations or notes
  - [ ] Tool requirements (Figma, Adobe XD, paper?)
  - [ ] Export format (PDF, PNG, interactive link)

---

## Common Pitfalls in Visual Assignments

### PDF Pitfalls
- ❌ Scanned pages too light/dark (hard to read)
- ❌ Image-based PDF (can't search or copy text)
- ❌ Wrong page order after merging
- ❌ File size too large (uncompressed images)
- ❌ Links broken in PDF (relative vs. absolute)
- ❌ Fonts embedded but display incorrectly

**Fix:** Convert to PDF (not scan). Optimize images before embedding. Test PDF on multiple readers.

### Image Pitfalls
- ❌ Wrong format for use case (JPG for diagrams should be PNG)
- ❌ Resolution too low (pixelated or blurry)
- ❌ Color space wrong (RGB for print CMYK source)
- ❌ Transparency lost in export
- ❌ File size unnecessarily large
- ❌ No alt text for accessibility
- ❌ Cropping loses important content

**Fix:** Choose format based on content type. Optimize for use case. Always include alt text.

### Diagram Pitfalls
- ❌ Symbol meanings inconsistent or undefined
- ❌ No legend explaining notation
- ❌ Overcrowded (too many elements on one diagram)
- ❌ Connections unclear (which arrows connect?)
- ❌ Labels too small or hard to read
- ❌ Mixed notation standards (flowchart + UML together)
- ❌ Missing start/end points or entry/exit nodes

**Fix:** Define notation first. Keep diagrams simple. Use legend. Test readability.

### Infographic Pitfalls
- ❌ Too much text (defeats purpose of visual)
- ❌ Data visualization inaccurate or misleading
- ❌ Color scheme unprofessional or unreadable
- ❌ Fonts too decorative (hard to read)
- ❌ Not accessible (low contrast, no alt text)
- ❌ Inconsistent style (mixing design elements)

**Fix:** Prioritize visuals over text. Ensure data accuracy. Test color contrast. Keep design consistent.

### Wireframe Pitfalls
- ❌ Too detailed too early (should be low-fidelity first)
- ❌ Missing responsive breakpoints
- ❌ No explanation of interactive elements
- ❌ User flow not obvious
- ❌ Annotations missing or unclear
- ❌ Inconsistent spacing and alignment

**Fix:** Start low-fidelity. Show multiple breakpoints if responsive. Annotate interaction and flow.

---

## Validation Framework

### PDF Validation
```
Requirement: "Create PDF from Word doc, 3-year financial summary"
Validation:
✅ All pages converted to PDF
✅ Text searchable and copyable
✅ File size reasonable (< 5MB)
✅ All images visible and clear
✅ Page order correct
✅ Headers/footers preserved

Status: PASS
```

### Image Validation
```
Requirement: "Logo in PNG with transparent background, 300x300px"
Validation:
✅ Format: PNG (supports transparency)
✅ Dimensions: 300x300 pixels
✅ Background: Transparent (no white fill)
✅ Quality: Not pixelated
✅ Color space: RGB (web standard)

Status: PASS
```

### Diagram Validation
```
Requirement: "Database ERD using Crow's Foot notation"
Validation:
✅ Crow's Foot symbols used correctly
✅ All entities labeled
✅ All relationships shown
✅ Cardinality marked (1:1, 1:N, M:N)
✅ Primary/foreign keys identified
✅ Legend present and clear
✅ Professional appearance

Status: PASS
```

### Wireframe Validation
```
Requirement: "Mobile-first responsive wireframe for checkout flow"
Validation:
✅ Low-fidelity (boxes, not detailed design)
✅ Mobile layout shown (< 768px)
✅ Tablet layout shown (768px - 1024px)
✅ Desktop layout shown (> 1024px)
✅ User flow annotations present
✅ Form fields and buttons labeled
✅ Navigation indicated

Status: PASS
```

---

## Testing Checklist (Visual Artifacts)

### PDFs
- [ ] **Technical**
  - [ ] Opens in standard PDF reader ✓
  - [ ] All pages present ✓
  - [ ] Page order correct ✓
  - [ ] Text searchable ✓
  - [ ] File size reasonable ✓

- [ ] **Content**
  - [ ] All content visible (nothing cut off) ✓
  - [ ] Text readable and clear ✓
  - [ ] Images display correctly ✓
  - [ ] Headers/footers intact ✓
  - [ ] Hyperlinks functional ✓

### Images
- [ ] **Format & Dimensions**
  - [ ] Format correct (PNG/JPG/SVG) ✓
  - [ ] Resolution appropriate ✓
  - [ ] Dimensions match specs ✓
  - [ ] File size optimized ✓

- [ ] **Quality**
  - [ ] Not pixelated or blurry ✓
  - [ ] Colors accurate ✓
  - [ ] Transparency correct (if applicable) ✓
  - [ ] Alt text present ✓

### Diagrams
- [ ] **Notation & Symbols**
  - [ ] Notation standard consistent ✓
  - [ ] All symbols correct ✓
  - [ ] Legend present and accurate ✓
  - [ ] Labels clear and readable ✓

- [ ] **Content & Relationships**
  - [ ] All elements present ✓
  - [ ] Relationships shown correctly ✓
  - [ ] Connections unambiguous ✓
  - [ ] Flow logical and clear ✓

- [ ] **Design**
  - [ ] Professional appearance ✓
  - [ ] Consistent sizing and spacing ✓
  - [ ] Color scheme appropriate ✓
  - [ ] Readable at normal size ✓

### Wireframes
- [ ] **Structure**
  - [ ] All screens shown ✓
  - [ ] Responsive breakpoints included ✓
  - [ ] Navigation indicated ✓
  - [ ] User flow clear ✓

- [ ] **Content**
  - [ ] Form fields labeled ✓
  - [ ] Buttons and actions indicated ✓
  - [ ] Annotations explain interactions ✓
  - [ ] Hierarchy and emphasis shown ✓

---

## Resources & References

- **PDF Tools:** Adobe Acrobat, Preview (Mac), Small PDF
- **Image Editing:** Photoshop, GIMP, Figma, Canva
- **Diagramming:** Microsoft Visio, Lucidchart, Draw.io, Creately
- **Wireframing:** Figma, Adobe XD, Balsamiq, Sketch
- **Infographics:** Canva, Piktochart, Venngage

---

## When to Escalate to Commander

- Complex 3D visualization or rendering
- Animation or interactive prototypes
- Custom branding or design guidelines
- Accessibility compliance testing
- Large-scale data visualization
- Animation or motion graphics
