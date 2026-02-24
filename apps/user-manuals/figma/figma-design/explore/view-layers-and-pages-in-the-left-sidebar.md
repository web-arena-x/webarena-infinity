# View layers and pages in the left sidebar

Source: https://help.figma.com/hc/en-us/articles/360039831974-View-layers-and-pages-in-the-left-sidebar

---

**We're slowly rolling out the new left navigation bar to users in Figma Design.** The navigation bar will provide access to your most essential workflows in a single place. Here is what's coming:

- Currently, the **variables modal** is not discoverable if you have a layer selected. With this update, the variables modal entry point is moving from the properties panel to the navigation bar, so you can access your variable collections anytime.
- The **assets tab** and **find and replace** are moving to the navigation bar
- File notifications, such as library updates and missing font alerts, will be found at the bottom of the navigation bar
- Property labels, which are labels that provide context for different sections of your properties panel and navigation bar, will be renamed to **Additional labels**. You’ll be able to toggle the labels by clicking > **View**.

If you need a bit more room on the canvas, you can still minimize your UI, which will collapse the navigation bar, navigation panel, and properties panel for an expanded view. To do this, click  **Minimize UI** from the top of the navigation panel (left panel) or press `Shift` `\`.

![left-navigation-bar.png](https://help.figma.com/hc/article_attachments/37506155851799)

The navigation bar will be available to everyone with a [Full seat](https://help.figma.com/hc/en-us/articles/360039960434-Manage-seats-in-Figma). During the rollout period, you may see a different experience than your teammates as this feature becomes available.

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Anyone with `can edit` access can interact with all panels in the left panel

Anyone with only `can view` access can view layers and navigate between pages

Figma Design files have four distinct interactive areas: a toolbar, two panels, and a scrollable canvas. These areas allow you to access, create and adjust elements of your design.

In this article, we're going to cover the **Navigation panel** (left panel) which gives you access to layers and pages in your file. You can also use the left panel to view components created in the current file and access components from any libraries added to the file.

![The navigation panel sits on the left against a light purple background.](https://help.figma.com/hc/article_attachments/24376960530839)

## Open the Navigation panel

There are a two tabs in the Navigation panel: **File** and **Assets**. You can click to switch between each view in the panel, or use keyboard shortcuts:

Mac

- **File tab**: `⌥ Option` `1`
- **Assets tab**: `⌥ Option` `2`

Windows

- **File tab**: `Alt` `1`
- **Assets tab**: `Alt` `2`

### Minimize or expand panels

To **Minimize** or **Expand** the left and right panels, click in the left panel, or using the keyboard shortcut `Shift` `\`.

If you select an object while the panels are minimized, the left panel remains minimized while the right panel expands so you can update the properties of the selected object. Once all objects are deselected, the right panel minimizes again.

![A design file containing various mobile app frames. A cursor clicks the minimize/expand ui button in the left panel. Both left and right panels minimize to show only the upper most sections of each panel. The cursor selects a frame on the canvas, and the right panel expands.](https://help.figma.com/hc/article_attachments/24376974686999)

### Hide or show UI

Toggle visibility of the entire Figma UI to make more space to view designs. Find **Hide/Show UI** from Actions, or use the keyboard shortcut:

- **Mac**: `⌘ Command` `\`
- **Windows**: `Ctrl` `\`

![The Actions menu opens at the bottom, and the cursor checks the Show/Hide UI. The left panel, right panel, and toolbar disappears. When the cursor unchecks the Show/Hide UI, the panels and toolbar reappear. ](https://help.figma.com/hc/article_attachments/24376974688663)

**Tip:** You can adjust the width of the left sidebar. This allows you to better see layer or asset names.

1. Hover your cursor over the right-edge of the sidebar. A bidirectional arrow will appear.
2. Click and drag to adjust the width of the panel.
3. Release to set the sidebar width.

## Pages

Within a file, you can create as many pages as you need. Each page has its own canvas, where you can explore and iterate on your designs. You can even create separate [prototypes](https://help.figma.com/hc/en-us/articles/360040314193) on each page. [Create and manage pages →](https://help.figma.com/hc/en-us/articles/360038511293)

## View layers

Any frames, groups, or objects you add to the canvas will be visible in the **Layers** section of the **File** tab. New layers are added to the top of the list, or to the top of the group, frame, or section it is contained within. Or, just above the layer you currently have selected.

You can determine if a layer is a frame, group or a specific type of object by the icon next to it:

- Frame
- Group
- Component
- Instance
- Text
- Shape—Icon varies depending on the shape. [Learn more →](https://help.figma.com/hc/en-us/articles/360040450133-Basic-shape-tools-in-Figma-design)
- Image
- Auto layout—icon varies depending on the auto layout configuration. [Learn more →](https://help.figma.com/hc/en-us/articles/360040451373-Explore-auto-layout-properties)
- Section
- Animated GIF or video

Figma nests any child objects within their parent group or frame. This allows you to collapse and expand layers within a group or Frame.

To collapse all expanded layers, click **Collapse layers** in the top right corner of the Layers panel. If you've already selected a layer when you collapse layers, all expanded layers collapse except for your selection.

There are many other ways to interact with layers:

- [Select layers, groups, and frames](https://help.figma.com/hc/en-us/articles/360040449873)
- [Adjust the z-index with layer order](https://help.figma.com/hc/en-us/articles/360039956914#Change_layer_order)
- [Rename layers individually or in bulk](https://help.figma.com/hc/en-us/articles/360039958934)
- [Toggle layer visibility](https://help.figma.com/hc/en-us/articles/360041112614)
- [Lock and unlock layers](https://help.figma.com/hc/en-us/articles/360041596573)

**Tip:** You can enable or disable the **Highlight layers on hover** setting. Go to **Menu** > **Preferences** > **Highlight layers on hover**.

## View components in the assets tab

[Components](https://help.figma.com/hc/en-us/articles/360038662654) are aspects of your designs that you can reuse. These could be buttons or icons, or more complex UI elements like navigation menus or status bars.

You can find all of your components in the **Assets** tab. You can drag any component from the assets view onto the canvas to create an instance of the component.

To open the assets view, click the **Assets** tab in the left sidebar, or use the keyboard shortcut:

- **Mac**: `⌥ Option` `2`
- **Windows**: `Alt` `2`

Once you've opened the assets view, you can:

- Open the [Libraries](https://help.figma.com/hc/en-us/articles/360041051154) modal.
- Use the search field to find a specific component. Figma looks for components in the current file, as well as any libraries you can access.
- Open **Libraries and settings** to filter through available libraries, and to switch between **Grid** and **List** views.
- Browse through **All libraries** that have been added to the file.

![The left panel sits at the very left end of the image on a gray background. The Assets tab is open with a list of libraries.](https://help.figma.com/hc/article_attachments/24376965531543)

**Note:** Figma groups components in the assets view by heading. If you have many components, Figma will present them as a path: **file** > **page** > **frame**

- Explore a file, page, or frame by clicking on the arrow to expand it
- Figma lists team or organization libraries added to the file, and enabled UI kits, in the assets view
- Create an instance by dragging a component from the assets view on to the canvas

[Learn how to insert components from the assets tab →](https://help.figma.com/hc/en-us/articles/360039150173)

## Libraries

Libraries allow you to publish styles, components, and variables from your files as a library. You can then apply styles and variables, or create instances of your components across files. [Get started with libraries →](../create-and-share-libraries/guide-to-libraries-in-figma.md)

To access your libraries from the assets view panel, click **Libraries** to open the libraries modal.