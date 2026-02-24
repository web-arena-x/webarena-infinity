# Add descriptions to styles, components, and variables

Source: https://help.figma.com/hc/en-us/articles/7938814091287-Add-descriptions-to-styles-components-and-variables

---

Documentation makes sure the people using your design system have the right information and context. It can help guide proper application, variant and state usage, and accessibility and contrast requirements.

Documentation is not just for designers, it’s also important to consider other people who will be using your design system. This includes the developers who will be implementing your designs.

At the moment, there are a few ways to incorporate design system documentation in your Figma libraries:

- Give [styles](https://help.figma.com/hc/en-us/articles/360039820134), [components](https://help.figma.com/hc/en-us/articles/360038663994), and [variables](https://help.figma.com/hc/en-us/articles/15145852043927) meaningful names
- Add short descriptions to styles, components, and variables
- Add links to external documentation to components
- Add descriptions to any library updates

**Tip!** Looking for more guidance around style and component libraries? Check out these best practice guides:

- [Components, styles, and shared libraries](https://www.figma.com/best-practices/components-styles-and-shared-libraries/)
- [Component architecture in Figma](https://www.figma.com/best-practices/component-architecture/)

## Components

You can attach a short **description** and a **link** to your components. This allows you to better communicate a component’s intended use.

Figma will look at component descriptions when returning search results. So you can use descriptions to tag components with relevant keywords. It won’t be possible to capture every detail in this description field, so have a think about what information will be most important.

If you have design system documentation in an external tool, you can add a link to that documentation.

![Component documentation panel showing a "Save button (secondary)" description and a GitHub link for further details.](https://help.figma.com/hc/article_attachments/26967247045911)

**Note:** If you combine existing components as a component set, Figma will apply any existing links and descriptions to the individual variants. You can view and edit this description when you have the variant selected.

### Add descriptions and links

Add a description and any links to your main components. You’ll need edit access to the library file to add or update descriptions. You can add descriptions and links to:

- Main components, including those with component properties
- Entire component sets and individual variants in a component set

1. Open the file where your component library lives. If you have an instance selected, you can select **Go to main component in library** to view the component in the library file.
2. Select main component, component set or a specific variant within the component set.
3. Click to open the **Component configuration** details: ![Component configuration panel showing fields for description and documentation link entries.](https://help.figma.com/hc/article_attachments/26967232720151)
4. Add a **description** for this component. Figma will look at this description when searching for components, so you can use this field to tag relevant keywords.
5. Add a **link** to external documentation, or another file with further explanations or guidance.
6. Click or anywhere outside the modal to apply changes.

Figma will show descriptions and links in common style and component locations in files. [**View component descriptions and links ↓**](#view-descriptions)

## Styles

There are a few tools you can use to help guide people toward the right styles for their designs.

You can use the slash or dash naming process to organize your styles into groups. We recommend giving your [styles](https://help.figma.com/hc/en-us/articles/360039238753) names that are relevant to their use case.

You can also add descriptions to styles. Descriptions allow you to show extra information about a style’s intended usage. You can [view a style’s description](#style-picker) when you hover over the style in the style picker.![Color picker with highlighted pink color shows description for use in light theme designs.](https://help.figma.com/hc/article_attachments/26967247046551)

### Add style descriptions

Add a description to the style definition in the library file. You need to [create a style](https://help.figma.com/hc/en-us/articles/360038746534) before you can add a description to it.

1. Click an empty spot in the canvas.
2. In the **Design** panel, view any style definitions in the file.
3. Hover over the style and click when it appears:![Edit color style window with a purple color swatch, showing name and description fields, alongside a list of local styles.](https://help.figma.com/hc/article_attachments/26967232721559)
4. In the **Edit style** menu add a **Description** using the field.
5. Click outside the menu or use the to close the menu.

**Tip!** You can find and open the style definition from any layer that uses that style:

1. Select a layer that supports that style.
2. Click to open the style picker.
3. Right-click the style and select **Edit style**.

## Variables

You can use the slash naming process to organize your variables into groups. We recommend giving your variables names that are relevant to their use case.

You can also add descriptions to variables. Descriptions allow you to show extra information about a variable's intended usage.

1. From the file where the variable lives, click an empty spot on the canvas to deselect any objects.
2. From the right sidebar, find the **Local variables** section.
3. Click  **Open variables.**
4. Find the variable from the Variables modal. Hover over the variable row, right-click, and select **Edit variable**.
5. Enter your description into the description box.

## Libraries

You can also add descriptions when publishing updates to your library. These descriptions show in both the library modal and in the file’s version history and are great for communicating high-level changes to your library.

![Publish library window showing changes to color styles, with options to add descriptions for high-level updates.](https://help.figma.com/hc/article_attachments/26967232721943)

We recommend using these descriptions in addition to component and style descriptions. Style and component descriptions are visible to anyone who interacts with the style or description. Library descriptions are only available at a file and library level, so have much less visibility.

Figma will show a notification in any files with styles and components from that library. You can view a list of updated styles and components and the description (if included). [**Review and accept library updates →**](https://help.figma.com/hc/en-us/articles/360039234193)

# View descriptions and documentation

You can view descriptions and links when interacting with styles and components in these places:

- [Instance menu in right sidebar](#instance-menu)
- [Assets panel in left sidebar](#assets-panel)
- [Style picker from properties in the right sidebar](#style-picker)
- [Inspect panel in Dev Mode](#inspect)
- [Properties panel (if you have view only access to the file)](#properties-panel-view)

## Instance menu in right sidebar

View component details in the instance section of the **Design** panel in the right sidebar. You need **edit** access to the file to access the **Design** panel.

1. Figma shows a preview of the description underneath the component / instance name.
2. Click **Show more** to view the full description and link in the documentation window. Click outside of the modal or use the button to close.
3. Collaborators can also click to view the original library file. This is great if you have additional guidance for how to use components.

![Two card components labeled "time" with descriptions. Right card is selected; details are in sidebar panel.](https://help.figma.com/hc/article_attachments/26967232722839)

## Assets panel

You can view component names and descriptions in the **Assets** panel. Figma will also use component descriptions when you search for a component.

Hover over the component in the **Assets** panel of the left sidebar to view the component’s details. You can see both the component **name** and **description** from list or grid view.

You need to have **can edit** access to a file to open the **Assets** panel. You’ll only need view access to the library to use components from that library.

## Libraries picker

View the name and description of a style or variable from the **Libraries** picker.

1. From the Fill or Stroke section of the right sidebar, click **Apply styles and variables** to open the **Libraries** picker.
2. Hover over a style or variable to view its description in a tooltip: ![Color picker highlighting a pink multiplayer color with a tooltip description, for managing design library styles.](https://help.figma.com/hc/article_attachments/26967247046551)

## Dev Mode

If you have access to [Dev Mode](https://help.figma.com/hc/en-us/sections/15023066873239-Dev-Mode), you can view style and components descriptions in the **Inspect** panel. View component descriptions in the **Component** section, underneath the component preview.

![Component example with a clock icon labeled "time" and description about scheduling. Includes settings and description panel.](https://help.figma.com/hc/article_attachments/26967232723479)

## Properties panel (view only access)

If you have view access to the file, and don't have access to Dev Mode, you can view component descriptions in the **Properties** panel of the right sidebar.

1. View the name of the component or instance. If the component lives in another file, you’ll also see the **Go to main component in library** icon to view the component in the library file.
2. View the description. If the component or instance is a variant, you’ll see descriptions for both the component set and the variant.
3. View other documentation and properties attached to the component.

![Light and dark mode info banners with title, message, and link examples; component details in sidebar.](https://help.figma.com/hc/article_attachments/26967247048727)