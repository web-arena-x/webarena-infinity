# Improve the accessibility of your site

Source: https://help.figma.com/hc/en-us/articles/31242789265431-Improve-the-accessibility-of-your-site

---

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the file

You can make your site more accessible by applying the correct HTML tags and accessibility properties to each element in your design.

This improves usability for people who rely on screen readers or keyboard navigation. Semantic HTML also clarifies your site’s structure and can boost search engine optimization (SEO).

**Tips for making your site more accessible**

- [Add alt text to images](#h_01K5C8GB5DGZPBSP2NQFRRANYM) that need description, or mark it as decorative. Keep alt text concise and functional—focus on purpose, not appearance.
- [Set the correct HTML tag](#h_01K5C8GB5DF4Q04NTVZ8Y91Y0F). Use a [role](#h_01K5C8GB5ENXMKZWB16HQ1996Z) only when no semantic tag fits.
- Add [labels](#h_01K5C8GB5DRW3GCBW15VFCNN2S) when visible text is missing or unclear.
- Mark purely decorative elements as [hidden](#h_01K5C8GB5D5XRV812QEQE9TRNF).
- [Use the color contrast tool in the color picker](https://help.figma.com/hc/en-us/articles/360041003774-Apply-paints-with-the-color-picker#h_01HBXR3HXS1ZR3K24YBY4A7XH0) to improve readability.

**Note:** These guidelines are for informational purposes only. Please consult with a lawyer to ensure you understand your legal obligations with respect to accessibility. Do not rely on these guidelines or Figma Sites to make sure you are in compliance with the law.

## Set the HTML tags for layers

The **Layers** panel shows each layer’s assigned HTML. By default, most layers will use a `div` tag. Figma also automatically applies these tags:

- Text layers use the `p` tag.
- Frames and rectangles with a media fill use `img` or `video`.
- Layers with a link applied use an `a` tag.
- Layers with **on click** interactions use the `button` tag.

To update an element’s tag:

1. Select one or more layers on the canvas.
2. In the right sidebar, navigate to the **Accessibility** section and choose a new tag.

**Tip**: You can also right-click a layer on the canvas or in the **Layers** panel and select **HTML tag** from the contextual menu.

**Note:** If you can’t see the HTML tags listed in the **Layers** panel, click  **Zoom/view options** at the top of the right sidebar and enable **Show HTML tags on layers**.

### Set accessibility landmarks

Landmarks are specific HTML tags that help people using assistive technologies navigate a site quickly and easily.

**Tip**: Learn more about landmarks by visiting the [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/).

| Landmark | HTML Tag | What it means |
| --- | --- | --- |
| Container | div | A general container for grouping elements, often used for styling and layout. |
| Section | section | A segment of a webpage that groups related content, usually with a heading. |
| Article | article | A self-contained piece of content—like a blog post, press release, or help center article—that can stand on its own. |
| Aside | aside | Contains content related to the main content, like sidebars or extra information. |
| Navigation | nav | A section with navigation links. |
| Header | header | The top of a section or page, usually with a title or navigation links. |
| Footer | footer | The bottom part of a page or section, usually with information like copyright notices or links. |
| Main Content | main | The primary content area of a page; usually excludes headers and footers. |
| Button | button | Represents a clickable element that can trigger an action or event, such as submitting a form or opening a dialog. |
| Media container | figure | Used to group media content—like images, illustrations, code snippets, videos—with an optional `<figcaption>` that provides a caption or description. |
| Ordered list | ol | Represents a list of items in a specific sequence or order, typically displayed with numbers. |
| Unordered list | ul | Represents a list of items without inherent order, usually displayed with bullets. |

**Note**: By default, a `div` provides no meaning to assistive technologies like screen readers. Adding attributes such as a [label](#h_01K5C8GB5DRW3GCBW15VFCNN2S) alone often has no effect unless you also [apply a role](#h_01K5C8GB5ENXMKZWB16HQ1996Z)**.**

For example:

- `<button aria-label="Close">` works because `<button>` already has a semantic role.
- `<div aria-label="Close">` does not work unless you add `role="button"`.

### Set heading tags for text layers

Use heading tags define structure. Screen readers use these tags to help users navigate sections quickly.

- `h1` marks the main heading of the page. Avoid using multiple `h1` tags on one page.
- `h2` to `h6` create subheadings that show content hierarchy.

**Tip**: Avoid skipping heading levels. Start your page with an `h1` tag, followed by `h2`, and so on. This helps enforce a proper hierarchy and structure.

### Set list tags to group related items

Use list tags to define groups or collections of related layers. Screen readers use these tags to help users understand relationships between items, improving readability and navigation.

- `ul` marks an unordered list for related but unordered content.
- `ol` marks an ordered list when sequencing or priority matters.
- `li` represents an item in a list; they are automatically applied to any layers nested within the `ul` or `ol` tags.

Using bullets in text automatically applies these tags accordingly.

## Configure accessibility properties

You can add properties that give assistive technologies more context about each element. Options include:

- [Set alt text for images and video](#h_01K5C8GB5DGZPBSP2NQFRRANYM)
- [Add a label](#h_01K5C8GB5DRW3GCBW15VFCNN2S)
- [Hide decorative content](#h_01K5C8GB5D5XRV812QEQE9TRNF)
- [Identify the current item](#h_01K5C8GB5EPMD3P79XF15E947W)
- [Add a role](#h_01K5C8GB5ENXMKZWB16HQ1996Z)

To configure accessibility properties for elements on your site:

1. Select the element you’d like to adjust.
2. Click  **Add accessibility settings** in the **Accessibility** section of the right sidebar.
3. Choose from the available options. You can find more information about each property type below.

### Set alt text for images and video

Images in your site are automatically assigned the `img` tag, while elements with a video fill are assigned the `video` tag.

Select **Alt text** to write a brief description of the image or video that provides context to users who cannot see it, such as those using screen readers.

You can also mark the element as decorative so they’re ignored by screen readers. Use this when the element provides no functional purpose, or is already described by visible text on the screen. This is the same as [making it hidden](#h_01K5C8GB5D5XRV812QEQE9TRNF).

This maps to the `alt` attribute.

**Tip**: Looking for more guidance on how to write effective alt text? Check out [Alt text: What to write](https://www.nngroup.com/articles/write-alt-text/) from Nielsen Norman Group.

### Add a label

Labels provide names for elements without clear visible text. For example, an icon-only button— like a magnifying glass that opens a search box—can be labelled `search`.

This maps to the `aria-label` attribute.

**Tip:** If the selected element already has a readable label in your design, you usually don’t need to add an accessibility label.

### Hide decorative content

Mark decorative elements as **Hidden** so screen readers skip them. For example, you might hide background shapes or ornamental illustrations.

This maps to the `aria-hidden` attribute.

**Tip:** Marking an element as **Hidden** means that any other accessibility settings are ignored.

### Identify the current item

Use **Current** **item** to mark which item in a set is active right now. This helps screen readers announce the correct context.

This maps to the `aria-current` attribute.

| Value | What it means | Example use |
| --- | --- | --- |
| page | The link to the current page within a set of navigation links. | A nav menu item for the page the user is currently on. |
| step | The current step in a process or progress tracker. | Step two of a multi-step checkout flow. |
| location | The current location within a physical or virtual map interface. | The active marker on a store locator map. |
| date | The currently selected date in a calendar or date picker. | Showing the currently selected day in a calendar widget. |
| time | The currently selected time in a time picker. | Marking the active time slot in a booking interface. |
| true | A generic indicator that the element is the current item in its context. | Highlighting the active tab in a tabbed interface. |
| false | Default state; the element is not the current item. | All other inactive links or options. You generally don’t need to set these manually; it’s the same as not applying `true`. |

### Add a role

Roles describe how an element works for assistive technologies. Use semantic HTML tags—like `button` or `nav`—wherever possible, and a role in situations like:

This maps to the `role` attribute.

- You’re using a generic element like a `div` but need to convey meaning.
- You’ve customized an element’s behavior and need to reflect that behavior programmatically. For example, treating a tabbed container as a `tablist` with `tab` children.
- You want to provide context beyond the default HTML tag. For example, marking a section as a `form` to highlight its purpose.

Roles don’t affect how elements look or behave visually, but they redefine an element’s semantic meaning. This change gives assistive technologies the context they need to present robust, meaningful information to users.

They are grouped into categories such as **Regions**, **Document**, and **Interactive**—each with specific roles for navigation, structure, or user controls.

#### Regions

These roles define major sections of a page, making it easier for screen readers to offer quick navigation.

| Role | What it means | Example use |
| --- | --- | --- |
| banner | A site-wide header, usually at the top of the page. | The global header with logo and site-wide navigation. |
| complementary | A supporting section of content. | A sidebar with related links or ads. |
| contentinfo | Info about the parent document, often a footer. | The bottom of a page with copyright text. |
| form | A region containing form elements. | A login or checkout form. |
| main | The primary content of the page. | The main article content in a blog. |
| navigation | A region with navigation links. | A site-wide nav menu or secondary navigation. |
| region | A labeled, significant area of the page. | A labeled panel in a dashboard. |
| search | A region for search functionality. | A search bar at the top of the page. |

#### Document

These roles describe the structure of page content. They help communicate the hierarchy and semantics of your content.

| Role | What it means | Example use |
| --- | --- | --- |
| article | A self-contained composition. | A blog post or press release. |
| blockquote | A section quoted from another source. | Pull quotes in an article. |
| caption | A description or title for media. | Caption for a figure or table. |
| cell | A single cell in a table. | A table cell with data. |
| code | Programmatic text. | Displaying a snippet of code. |
| definition | The definition of a term. | Glossary entries. |
| directory | A list of references or navigation. | A table of contents. |
| document | Represents an entire embedded document. | Embedding a PDF viewer. |
| emphasis | Text with emphasized meaning. | Highlighted words in a paragraph. |
| feed | A dynamic list of articles or updates. | A news feed or activity stream. |
| figure | Independent content with a caption. | An image with a caption. |
| group | A collection of items that form a logical set. | A set of related form fields. |
| heading | A heading in the document outline. | Section headings. |
| img | An image. | Decorative or meaningful images. |
| list | A group of list items. | A bulleted or numbered list. |
| listitem | An item in a list. | A single list entry. |
| math | Mathematical content. | A complex equation. |
| note | Supporting information. | Side notes or annotations. |
| paragraph | A block of text. | A standard paragraph. |
| presentation | Layout-only content. | A decorative container. |
| row | A row of cells in a table. | Table row in a spreadsheet. |
| rowgroup | A grouping of table rows. | A tbody element. |
| rowheader | A header cell for a row. | Row titles in a table. |
| separator | A divider between sections. | A horizontal rule. |
| strong | Strong importance. | Bold text for emphasis. |
| subscript | Subscript text. | Chemical formulas. |
| superscript | Superscript text. | Footnote references. |
| table | A table of tabular data. | Product pricing table. |
| term | A word or phrase being defined. | Dictionary entry. |
| time | A time value or timestamp. | Publication date. |
| toolbar | A container of controls. | Text editor toolbar. |
| tooltip | A brief label that appears on hover or focus. | Tooltip for an icon button. |

#### Interactive

These roles define user interface controls. They communicate what users can do with them and how they behave.

| Role | What it means | Example use |
| --- | --- | --- |
| button | A clickable button. | Submit button in a form. |
| checkbox | A checkbox that can be checked or unchecked. | Newsletter subscription checkbox. |
| gridcell | A cell in a grid. | Data cell in a spreadsheet app. |
| link | A hyperlink to another page or resource. | A navigation link. |
| menuitem | An option inside a menu. | “Save As” in a dropdown menu. |
| menuitemcheckbox | A menu item like a checkbox. | Toggle “Show Line Numbers”. |
| menuitemradio | A menu item like a radio button. | Choose theme: Light or Dark. |
| option | An option in a listbox. | Dropdown options. |
| progressbar | Shows task progress. | Upload progress indicator. |
| radio | A single radio button. | Select payment method. |
| scrollbar | A scrollbar for scrolling content. | Custom scrollable area. |
| searchbox | A search input field. | Search field in a header. |
| slider | A slider for selecting values. | Volume control slider. |
| spinbutton | A numeric input with controls. | Quantity selector in a cart. |
| switch | A toggle switch. | Dark mode toggle. |
| tab | A tab in a tabbed interface. | “Details” vs “Reviews” tab. |
| tabpanel | The panel linked to a tab. | The “Reviews” content panel. |
| textbox | A text entry field. | Comment box. |
| treeitem | An item in a hierarchical tree. | A folder in a file tree. |
| combobox | Combined input box and dropdown. | Searchable dropdown. |
| grid | A grid layout with rows and cells. | Spreadsheet grid. |
| listbox | A list of options. | Dropdown list of countries. |
| menu | A container of menu items. | File menu in an app. |
| menubar | A horizontal set of menu items. | Top navigation in a desktop app. |
| radiogroup | A group of radio buttons. | Shipping method options. |
| tablist | A list of tabs. | Tabs above a panel area. |
| tree | A tree widget for hierarchical data. | File explorer tree. |
| treegrid | A grid with expandable rows. | Interactive data grid with nested rows. |
| alert | A high-priority message. | Error alert banner. |
| log | A region that logs messages dynamically. | Chat log panel. |
| marquee | A scrolling region of text. | News ticker. |
| status | A region that presents status messages. | Connection status indicator. |
| timer | A time-based status region. | Countdown timer. |
| alertdialog | A dialog that interrupts the user. | “Are you sure?” confirmation. |
| dialog | A generic dialog box. | Settings modal window. |
| comment | A region that contains comments. | Comment thread. |
| suggestion | A proposed change. | Suggested edits in a doc. |