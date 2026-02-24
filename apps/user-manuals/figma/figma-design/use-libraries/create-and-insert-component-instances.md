# Create and insert component instances

Source: https://help.figma.com/hc/en-us/articles/360039150173-Create-and-insert-component-instances

---

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone with `can edit` access to a file in a paid team has access to the component playground

Anyone with `can view` access to the file can use components from that library

New to components? [Guide to style and component libraries →](https://help.figma.com/hc/en-us/articles/360041051154)

Components are UI elements that you can reuse across your designs.

- The **main component** defines the properties of the element.
- The **instance** is a copy of the component you can reuse in your designs.

![](https://help.figma.com/hc/article_attachments/4406611319447)

There are a few ways to create and insert component instances into your designs:

- From the [assets panel](#assets-panel) in the left sidebar
- From the [component details modal](#h_01H967BDDFRX012YSNY661ZZBJ), accessible from the assets panel
- Using the asset tab of the [actions menu](#quick-insert)
- By [copying or duplicating](#copy-duplicte) an instance

**Tip:** You can handoff component instances for development without reorganizing your file by [marking instances as ready for dev in Dev Mode →](../tour-the-interface/guide-to-dev-mode.md#View_which_sections_are_ready_for_development)

## Assets panel

The **Assets** panel in the left sidebar allows you to search for components to add to your file. You can choose which libraries are available in the **Assets** panel.

![](https://help.figma.com/hc/article_attachments/24434523914391)

To open the Assets panel:

1. Select the **Assets** tab in the left sidebar, or use the shortcut:
   - **Mac**: `⌥ Option` `2`
   - **Windows:** `Alt` `2`
2. Select a library with the component you'd like to use
3. Find the component you want to use
4. Click and drag the component onto the canvas to create an instance of that component.

**Tip**: You can customize the appearance of the Assets tab to match your preferences. Click to switch between a grid or list view, and show or hide sub-folders.

**Note**: Is the library you need missing from the Assets panel? Click to browse available libraries in your team or organization and add them to your file.

- [Manage libraries for your drafts](https://help.figma.com/hc/en-us/articles/360038743434)
- [Manage libraries in design files](https://help.figma.com/hc/en-us/articles/1500008731201)
- [Manage libraries in teams](https://help.figma.com/hc/en-us/articles/360039234953)
- [Manage default organization libraries](https://help.figma.com/hc/en-us/articles/360040530413)

## Component details modal

The component details modal shows you:

- The component’s documentation
- The library it lives in
- A preview of the component’s default state

If you have can edit access to a library in a paid team, you’ll have additional access to a component playground.

From the component playground, you can:

- Preview the component’s variants
- View and set component properties
- View and set nested component properties, if [nested instances are exposed](https://help.figma.com/hc/en-us/articles/5579474826519#exposed-instances)
- View and change variable modes for any variables applied to the component
- Insert the component onto the canvas

1. Select the **Assets** tab in the left sidebar, or use the shortcut:
   - **Mac**: `⌥ Option``2`
   - **Windows:** `Alt``2`
2. Find the component and select it to open the component details modal.
3. Use the controls to configure your component.
4. To insert the instance, click **Insert instance** or drag the preview onto the canvas.

![](https://help.figma.com/hc/article_attachments/24434477868183)

## Quick insert from the actions menu

Insert instances of components from your keyboard using quick insert. Quick insert opens the Actions menu where you can find and view components from libraries that have been added to the file.

![](https://help.figma.com/hc/article_attachments/24434367845399)

1. Use the shortcut `Shift` `I` to open quick insert.
2. Use the search bar to find a specific component.

**Tip:** Need to locate a main component from one of its instances? Right-click any instance and select **Go to main component** or use the keyboard shortcut:

- **Mac:** `^ Control``⌥ Option``⌘ Command``k`
- **Windows:**`Control``Alt``Shift``k`

[Learn more about finding main components.](../create-and-share-libraries/edit-main-components.md#find-components)

## Copy or duplicate an instance on the canvas

### Duplicate using the keyboard shortcut

If you're working in the same file, you can duplicate a component to create an instance. Duplicate using the keyboard shortcut:

- **Mac**: `⌘ Command` `D`
- **Windows**: `Ctrl` `D`

### Drag to copy

You can also drag to copy a component within the same file:

1. Hold down `⌥ Option` for Mac or `Alt` for Windows and drag to create an instance.
2. Release the click **before** you release the modifier key. Otherwise, Figma will move the original component instead of duplicate it.

### Copy and paste

You can copy and paste any component within the same file to create an instance.

Component instances and published main components can be copied and pasted across files.

- **Mac:** `⌘ Command``C` and `⌘ Command``V`
- **Windows**: `Ctrl``C` and `Ctrl``V`