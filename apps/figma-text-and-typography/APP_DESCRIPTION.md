# Figma Text & Typography

## Summary

A faithful replica of Figma's text and typography management interface. The app simulates Figma's right-panel typography controls, text layer management, text style system, font browser, and settings. Users can create, select, and modify text layers with full control over font properties, paragraph formatting, OpenType features, variable font axes, links, lists, text direction (LTR/RTL), truncation, and more.

## Main Sections / Pages

The app has 5 main sections accessible via the sidebar navigation:

1. **Layers** (`#/layers`) - Browse, search, create, and manage text layers
2. **Typography** (`#/properties`) - Edit all typography properties for the selected text layer (3 tabs: Basics, Details, Variable)
3. **Text Styles** (`#/styles`) - Create, edit, delete, and apply reusable text styles
4. **Fonts** (`#/fonts`) - Browse, search, and filter the font library; apply fonts to layers
5. **Settings** (`#/settings`) - Configure default text properties, smart features, spelling, and canvas preferences

## Implemented Features & UI Interactions

### Layers Panel
- List of all text layers with name, font info, style tag, and content preview
- Search/filter layers by name, content, or font family
- Create new text layer (opens modal with content textarea)
- Select a layer (click) to edit its properties in Typography panel
- Toggle layer visibility (eye icon)
- Toggle layer lock (lock icon)
- Double-click layer name to rename (opens rename modal)
- Delete layer (Delete/Backspace key opens confirmation modal)
- Duplicate layer via context actions

### Typography Panel (Basics Tab)
- **Text Style**: Shows applied style with detach button, or create/apply style buttons
- **Font family**: Click to open font picker modal (search + filter)
- **Font style/weight**: Dropdown with styles from the selected font (e.g., Thin, Light, Regular, Medium, Semi Bold, Bold, Extra Bold, Black)
- **Font size**: Number input (1-1000 px)
- **Line height**: Number input + unit dropdown (px or %). Empty = auto
- **Letter spacing**: Number input + unit dropdown (px, em, %)
- **Horizontal alignment**: Button group (Left, Center, Right, Justify) with alignment icons
- **Vertical alignment**: Button group (Top, Middle, Bottom) - only shown when resizing is "fixed"
- **Resizing mode**: Button group (Auto width, Auto height, Fixed)
- **Width/Height**: Number inputs shown when applicable based on resizing mode
- **Text decoration**: Button group (None, Underline, Strikethrough)
- **Letter case**: Dropdown (None, Uppercase, Lowercase, Capitalize, Small Caps)
- **Text direction**: Button group (LTR, RTL) with arrow icons
- **Live preview**: Shows rendered text with all applied formatting

### Typography Panel (Details Tab)
- **Paragraph spacing**: Number input (px)
- **Paragraph indent**: Number input (px)
- **Hanging punctuation**: Toggle
- **List style**: Dropdown (No list, Bulleted, Numbered)
- **List spacing**: Number input (px, shown when list style is not "none")
- **Hanging list**: Toggle (shown when list style is not "none")
- **Truncation**: Toggle + max lines number input
- **Vertical trim**: Toggle
- **Links**: List of links on the layer with text excerpt and URL; add/edit/remove link modals
- **OpenType features**: Collapsible categories (Letterforms, Stylistic Sets, Character Variants, Horizontal Spacing, Numbers, Letter Case) with toggles per feature

### Typography Panel (Variable Tab)
- Only shown when selected font is a variable font
- **Variable font axes**: Slider + number input per axis (e.g., Weight, Width, Slant, Optical Size)
- Shows axis name, tag, min/max range
- Real-time value adjustment

### Text Styles Panel
- List of all text styles as cards with preview, name, metadata, description, usage count
- Create new style (modal: name + description, optionally from selected layer)
- Edit style (modal: name, description, font family, font style, font size, letter case, decoration)
- Delete style (confirmation modal, detaches from layers)
- Editing a style auto-updates all layers using that style
- Apply style to layer from Typography panel

### Font Browser Panel
- Browse all fonts with preview, metadata (category, source, styles count, variable axes)
- **Search**: Filter fonts by name
- **Filter chips**: All fonts, In this file, Popular, Used at Acme Corp, Installed by you, Google fonts, Variable fonts
- Font count display
- Each font card shows: name, badges (Variable, Popular, language, RTL), preview text, category, source, style chips, axis chips
- "Apply to layer" button when a layer is selected

### Settings Panel
- **Smart quotes**: Toggle (convert straight to curly quotes)
- **Smart symbols**: Toggle + reference table of all conversions (`->` to arrow, `(c)` to copyright, etc.)
- **Default font family**: Dropdown of all available fonts
- **Default font style**: Dropdown (Thin through Black)
- **Default font size**: Dropdown of presets (8-128px)
- **Default alignment**: Dropdown (Left, Center, Right, Justify)
- **Default text direction**: Dropdown (Left to Right, Right to Left)
- **Spelling language**: Dropdown (23 languages including CJK, Arabic, Hebrew)
- **Snap to grid**: Toggle
- **Show font preview**: Toggle
- **Nudge amount**: Number input (px)
- **Big nudge amount**: Number input (px)
- **Recent fonts**: Ordered list of recently used fonts

## Data Model

### Text Layer (`textLayers[]`)
| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique ID (e.g., `tl_001`) |
| name | string | Layer display name |
| content | string | Text content (supports newlines) |
| fontFamily | string | Font family name |
| fontStyle | string | Font style/weight |
| fontSize | number | Size in px |
| lineHeight | object | `{value: number|'auto', unit: 'px'|'%'|'auto'}` |
| letterSpacing | object | `{value: number, unit: 'px'|'em'|'%'}` |
| paragraphSpacing | number | Spacing between paragraphs (px) |
| paragraphIndent | number | First-line indent (px) |
| horizontalAlign | string | `left|center|right|justify` |
| verticalAlign | string | `top|middle|bottom` |
| textDecoration | string | `none|underline|strikethrough` |
| letterCase | string | `none|uppercase|lowercase|capitalize|small-caps` |
| textDirection | string | `ltr|rtl` |
| resizing | string | `auto-width|auto-height|fixed` |
| truncation | object | `{enabled: boolean, maxLines: number|null}` |
| listStyle | string | `none|bulleted|numbered` |
| listSpacing | number | Spacing between list items (px) |
| hangingPunctuation | boolean | Move quotes outside bounding box |
| hangingList | boolean | Move bullets/numbers outside bounding box |
| verticalTrim | boolean | Remove extra space above/below text |
| links | array | `[{id, startIndex, endIndex, url}]` |
| openTypeFeatures | object | `{featureTag: boolean}` (e.g., `{liga: true, kern: true}`) |
| textStyleId | string|null | Reference to applied text style |
| variableAxes | object | `{axisTag: value}` (e.g., `{wght: 450, slnt: -5}`) |
| width | number|null | Bounding box width (px) |
| height | number|null | Bounding box height (px) |
| x | number | X position |
| y | number | Y position |
| locked | boolean | Whether layer is locked |
| visible | boolean | Whether layer is visible |
| createdAt | string | ISO 8601 timestamp |
| updatedAt | string | ISO 8601 timestamp |

### Text Style (`textStyles[]`)
| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique ID (e.g., `ts_001`) |
| name | string | Style name (e.g., `Heading/H1`) |
| fontFamily | string | Font family name |
| fontStyle | string | Font style/weight |
| fontSize | number | Size in px |
| lineHeight | object | `{value, unit}` |
| letterSpacing | object | `{value, unit}` |
| paragraphSpacing | number | Spacing between paragraphs |
| paragraphIndent | number | First-line indent |
| textDecoration | string | Decoration type |
| letterCase | string | Case transform |
| listStyle | string | List type |
| openTypeFeatures | object | Feature toggles |
| description | string | Optional description |
| createdAt | string | ISO 8601 timestamp |
| updatedAt | string | ISO 8601 timestamp |

### Font Family (`fontFamilies[]`)
| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique ID |
| name | string | Font family name |
| category | string | `sans-serif|serif|monospace` |
| source | string | `google|installed|organization` |
| isVariable | boolean | Whether it's a variable font |
| variableAxes | array | `[{tag, name, min, max, default}]` |
| styles | array | Available styles (e.g., `['Regular', 'Bold']`) |
| openTypeFeatures | array | Supported feature tags |
| popular | boolean | Whether font is popular |
| language | string | Optional language label (e.g., `Japanese`) |
| rtl | boolean | Optional RTL flag |

### Preferences (`preferences`)
| Field | Type | Description |
|-------|------|-------------|
| smartQuotes | boolean | Auto-convert straight to curly quotes |
| smartSymbols | boolean | Auto-convert symbol character combos |
| defaultFontFamily | string | Default font for new layers |
| defaultFontStyle | string | Default style for new layers |
| defaultFontSize | number | Default size for new layers |
| defaultLineHeight | object | Default line height |
| defaultLetterSpacing | object | Default letter spacing |
| defaultHorizontalAlign | string | Default alignment |
| defaultTextDirection | string | Default direction |
| showFontPreview | boolean | Show preview on hover |
| recentFonts | array | Recently used font names |
| fontFilter | string | Last used font filter |
| snapToGrid | boolean | Snap to grid |
| nudgeAmount | number | Arrow key nudge (px) |
| bigNudgeAmount | number | Shift+arrow nudge (px) |
| spellingLanguage | string | Spelling check language |

### Relationships
- Text Layer -> Text Style: `textStyleId` references `textStyles[].id` (many-to-one)
- Text Layer -> Font Family: `fontFamily` references `fontFamilies[].name` (many-to-one)
- Text Layer -> Links: `links[]` embedded array (one-to-many)
- Text Style -> Font Family: `fontFamily` references `fontFamilies[].name` (many-to-one)

## Navigation Structure

| Section | Hash Route | How to Reach |
|---------|-----------|--------------|
| Layers | `#/layers` | Click "Layers" in sidebar (default view) |
| Typography | `#/properties` | Click "Typography" in sidebar |
| Text Styles | `#/styles` | Click "Text Styles" in sidebar |
| Fonts | `#/fonts` | Click "Fonts" in sidebar |
| Settings | `#/settings` | Click "Settings" in sidebar |

## Available Form Controls

### Dropdowns (Custom, not native `<select>`)
- Font style/weight (dd-font-style): options from selected font's styles array
- Line height unit (dd-line-height-unit): px, %
- Letter spacing unit (dd-letter-spacing-unit): px, em, %
- Letter case (dd-letter-case): None, Uppercase, Lowercase, Capitalize, Small Caps
- List style (dd-list-style): No list, Bulleted, Numbered
- Default font family (dd-default-font): all font family names
- Default font style (dd-default-style): Thin through Black
- Default font size (dd-default-size): 8-128px presets
- Default alignment (dd-default-align): Left, Center, Right, Justify
- Default direction (dd-default-direction): Left to Right, Right to Left
- Spelling language (dd-spelling-lang): 23 languages

### Toggles
- Hanging punctuation (toggle-hanging-punct)
- Hanging list (toggle-hanging-list)
- Text truncation (toggle-truncation)
- Vertical trim (toggle-vertical-trim)
- Smart quotes (toggle-smart-quotes)
- Smart symbols (toggle-smart-symbols)
- Snap to grid (toggle-snap-grid)
- Show font preview (toggle-font-preview)
- OpenType feature toggles (per feature tag)

### Button Groups (Segmented Controls)
- Horizontal alignment (bg-h-align): left, center, right, justify
- Vertical alignment (bg-v-align): top, middle, bottom
- Resizing mode (bg-resizing): auto-width, auto-height, fixed
- Text decoration (bg-decoration): none, underline, strikethrough
- Text direction (bg-direction): ltr, rtl

### Number Inputs
- Font size (input-font-size): 1-1000
- Line height (input-line-height): 0-500
- Letter spacing (input-letter-spacing): -1 to 10
- Paragraph spacing (input-para-spacing): 0-200
- Paragraph indent (input-para-indent): 0-500
- List spacing (input-list-spacing): 0-100
- Max lines (input-max-lines): 1-100
- Width (input-width): 1-10000
- Height (input-height): 1-10000
- Nudge amount (input-nudge): 0.1-100
- Big nudge amount (input-big-nudge): 1-100

### Sliders (Variable Font Axes)
- One slider per axis on the selected variable font (e.g., slider-wght for Weight, slider-slnt for Slant)

### Filter Chips
- Font filters: All fonts, In this file, Popular, Used at Acme Corp, Installed by you, Google fonts, Variable fonts

## Seed Data Summary

### Text Layers (20 layers)
1. **Page Title** - "Welcome to the Design System" - Inter Bold 48px, style Heading/H1
2. **Body Text** - Long body paragraph - Inter Regular 16px, style Body/Regular, has link
3. **Section Header** - "Typography Settings" - Montserrat Semi Bold 32px, style Heading/H2, variable wght:600
4. **Feature List** - 8-item bulleted list - Inter Regular 14px, hanging list enabled
5. **Pricing Tiers** - 4-item numbered list - Inter Medium 14px
6. **Call to Action** - "Get Started for Free" - Poppins Semi Bold 18px, uppercase, centered, fixed size, has link
7. **Copyright Notice** - Copyright text - Inter Regular 12px, centered, 2 links
8. **Arabic Welcome** - Arabic text - Noto Sans Arabic Bold 28px, RTL, variable
9. **Hebrew Body** - Hebrew text - Noto Sans Hebrew Regular 16px, RTL
10. **Japanese Heading** - Japanese text - Noto Sans JP Bold 24px
11. **Truncated Preview** - Long text truncated - Roboto Regular 14px, fixed, truncation 3 lines, variable
12. **Code Sample** - Code snippet - JetBrains Mono Regular 13px, slashed zero, variable
13. **Variable Font Demo** - Description text - Inter Regular 20px, vertical trim, variable wght:450 slnt:-5
14. **Strikethrough Example** - Struck-through text - Inter Regular 14px
15. **Underlined Link Text** - Linked text - Inter Medium 14px, underline, has link
16. **Indented Quote** - Quote with indentation - Playfair Display Regular 22px, paragraph indent 24px, hanging punctuation, variable
17. **Small Caps Header** - "Design Principles" - Montserrat Medium 14px, small-caps, style Label/SmallCaps, variable
18. **Mixed Direction Text** - LTR with embedded Arabic - Inter Regular 16px
19. **Release Notes Header** - "What's New in v4.2" - DM Sans Bold 36px, vertical trim, variable wght:700 opsz:36
20. **Step Instructions** - 6-item numbered list - Inter Regular 14px, list spacing 6px

### Text Styles (12 styles)
Heading/H1, Body/Regular, Heading/H2, Heading/H3, Button/Primary, Caption/Small, Code/Inline, Label/SmallCaps, Body/Large, Heading/Display, Body/Small, Label/Overline

### Font Families (30 fonts)
Includes popular Google Fonts (Inter, Roboto, Open Sans, Lato, Montserrat, Poppins, Playfair Display, etc.), installed fonts (Helvetica Neue, Arial, SF Pro, Georgia, Fira Code), CJK/RTL fonts (Noto Sans SC/TC/JP/KR/Arabic/Hebrew), and monospace fonts (JetBrains Mono, Source Code Pro, Fira Code). 13 are variable fonts with axes. 7 are marked popular.

### Smart Symbols (13 conversions)
Arrow symbols, copyright/registered/trademark, checkbox, ellipsis, em dash, fractions

### File Info
Design System v4.2, Product Design project, Acme Corp Design Team, Typography page active

### Current User
Sarah Chen, Editor role, Organization plan
