# Add measurements and annotate designs

Source: https://help.figma.com/hc/en-us/articles/20774752502935-Add-measurements-and-annotate-designs

---

Before you Start

Who can use this feature

Available on all paid plans

Anyone with a [Full seat](https://help.figma.com/hc/en-us/articles/360039960434-Free-and-paid-seats-in-Figma#editor) and `can edit` access to a file can add measurements and annotations

Anyone with a [Full](https://help.figma.com/hc/en-us/articles/360039960434-Free-and-paid-seats-in-Figma#editor) or a [Dev seat](https://help.figma.com/hc/en-us/articles/19813618057623-Dev-Mode-GA-for-admins#h_01HKN19J4JJTKGMATHW6BP331A) and at least `can view` access to a file can view measurements and annotations

Use annotations and measurements to create speedier and more transparent handoffs that stay up-to-day, even as designs change.

With annotations, designers can communicate and connect key details directly to designs:

- Highlight important properties so developers can't miss them
- Help developers quickly visualize specs like spacing and sizing
- Share additional context with text notes
- Create and categorize annotations for easier navigation

Developers can see annotations update in real time as they work in Dev Mode, ensuring they don’t miss any crucial callouts during handoff.

![Figma annotation menu with options to add text, property, and category, highlighting an accessibility label.](https://help.figma.com/hc/article_attachments/31044023651223)

# Add measurements to a design

Adding measurements to quickly visualize spacing and sizing between components.

To add a measurement to a design:

1. Click **Measurement** in the toolbar or use the keyboard shortcut `Shift` `M`.
2. Hover over a layer to see options for where to start your measurement.
3. Click and drag from your starting point to the layer where you want the measurement to end.
4. Click and drag the measurement so it doesn’t cover the design.
5. You can double-click on the measurement to customize its text.

**Note:** The measurement feature, which lets you apply visible measurements for others to view, is different than measuring by holding `Alt` (Windows) or `Option` (Mac). Any plan can use `Alt` or `Option` to [measure the distance](https://help.figma.com/hc/en-us/articles/360039956974) between a selected layer and another layer, but that measure can't be saved and shared with others.

![Measurement being manually added to a design](https://help.figma.com/hc/article_attachments/31044023651863)

**Tip:** To delete a measurement, click it and press the `Delete` or `Backspace` key.

# Add annotations to a design

Designers can add annotations to provide context, define design properties, or communicate other relevant information for developers to turn design into code. You can annotate a layer’s defined properties, like alignment direction or sizing, or provide additional details with free text. Even if designs are later updated, annotation properties stay-up-to-date and accurate, ensuring nothing gets lost in translation.

You can add annotations from Design or Dev Mode. To add annotations to a design:

1. Click **Annotation** in the toolbar or use the keyboard shortcut `Shift` `T`.
2. Select the layer you’d like to annotate.
3. Write a note in the text field, or click **+ Property** to select a property from the list. You can include both plain text and properties in an annotation.

## Categorize annotations

Give annotations even more clarity by categorizing them. Categories help distinguish different types of annotations, making it easier to scan for relevant information.

Editors can use the default labels, as well as edit or delete those categories. Category labels only apply to the current file *-* nothing will change in other files when you edit or delete the default categories.

![Annotation menu in Figma showing an added "Accessibility" label with category options such as Development and Interaction.](https://help.figma.com/hc/article_attachments/31044023652247)

Figma design files come with preset annotation categories:

- Development
- Interaction
- Accessibility
- Content

To add a new category:

1. Select an existing annotation or create a new one, then click the category dropdown.
2. Click **Edit categories…**
3. Click , then select a color and type in a name for your new category label.

**Note:** Copying layers that have annotations with categories will copy over the category from the source file to the target file. If there is no exact match in the target file (color and label), a new category is defined.

![Annotation menu for adding and categorizing design annotations with options for development, interaction, accessibility, and content.](https://help.figma.com/hc/article_attachments/31043996133015)

**Tip:** With the plugin API, teams can build custom Dev Mode plugins to create and manage annotations in bulk.

[Check out the Figma Plugin API reference to learn how you can automate and customize annotations with plugins.](https://www.figma.com/plugin-docs/api/Annotation/)

### Filter by category

You can filter annotations by category, making it even easier to find the details you need on the canvas. There are a couple of ways to filter annotations by category:

**Right-click menu**

1. Right-click an annotation on the canvas.
2. Select **Filter by**.
3. Select which category you want to filter by, or select **All categories**.

**Zoom menu in Dev Mode**

1. Click the zoom dropdown in the Dev Mode right sidebar.
2. Hover over **Annotations**.
3. Select which category you want to filter by, or select **All categories**.

## Hide annotations

All annotations on a Figma Design file are visible in Dev Mode by default. To hide annotations:

1. Click  Main menu in the toolbar.
2. Hover over **View** in the dropdown.
3. Deselect **Annotations**.

**Tip:** To delete an annotation, click it and press the `Delete` or `Backspace` key.