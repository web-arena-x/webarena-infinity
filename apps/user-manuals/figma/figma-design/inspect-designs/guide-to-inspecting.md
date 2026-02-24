# Guide to inspecting

Source: https://help.figma.com/hc/en-us/articles/22012921621015-Guide-to-inspecting

---

Inspecting designs helps developers or other stakeholders understand the structure and properties of a design so they can more easily translate it to code.

How you inspect a design file depends on your [**plan type**](https://help.figma.com/hc/en-us/articles/360040328273), [**seat type**](https://help.figma.com/hc/en-us/articles/360039960434), and your **file permissions**. Use the tool below to see how to do common inspection tasks—exporting, measuring, generating code, viewing annotations, and using plugins for development—based on your personal access to the file you’d like to inspect.

No matter your file access, there is an inspect experience available to you.

First, check to see if you have access to Dev Mode in the file you’re inspecting by toggling to Dev Mode at the top of the file or by using the keyboard shortcut `Shift` `D`. If you don't have access to Dev Mode, you’ll be inspecting in Design Mode. You can select if you have `can edit` or `can view` access to see how to inspect.

## I don't have Dev Mode, and I have view-only access

**Need access to [Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247)**? If you’re on the Starter plan, you’ll need to [upgrade to a paid plan](https://figma.com/pricing) or [move your file](https://help.figma.com/hc/en-us/articles/360038511573) to a paid team. If you’re on a paid plan, you’ll need a Full or Dev seat.

With view-only access to a design, you can use inspection tools directly within Design Mode:

### Measure distances

You can measure distances between objects, even if they are nested within frames, groups, or components.

1. Select the first object on the canvas.
2. Hold down the modifier key:
   - Mac: ⌥ Option
   - Windows: Alt
3. Hover over the second object.

Figma will display a red line between the two objects, as well as horizontal and vertical measurements.

**Tip**: Having trouble measuring? Check out the [guide to measuring the distance between objects](../work-with-layers/measure-distances-between-layers.md).

### Generate code

You can copy auto-generated code snippets for CSS, iOS, or Android.

1. Select an object on the canvas.
2. Right-click on the object and select **Copy/Paste as** > **Copy as code**.
3. Select the code option that suits your needs.

### View properties

The **Properties** tab gives you a list of properties for objects on the canvas. This includes properties like: layout, color, typography, text strings, component properties, styles, and variables. To view the properties of an object:

1. Select an object on the canvas.
2. Click the **Properties** tab in the right sidebar.

### Export

1. Select the layers you want to export. If you want to export the entire canvas of the current page, deselect everything on the canvas.
2. In the **Export** tab, click the  plus icon to add an export configuration. You can add as many export configurations to a selection as needed.
3. Configure the export settings. Learn more about [Figma's export formats and settings](https://help.figma.com/hc/en-us/articles/13402894554519).
4. If needed, click **Preview** to see how your asset will look. If you have multiple objects selected, the **Preview** setting won’t display.
5. Click **Export.**

**Tip**: Want to learn more about exporting? Check out the full [guide to exports in Figma](https://help.figma.com/hc/en-us/articles/360040028114-Export-from-Figma).

### View or add comments

[Comments](https://help.figma.com/hc/en-us/articles/360041068574) help designers and developers collaborate by drawing attention to specific parts of the design. You can leave comments to share more context about how parts of the design should work.

1. Click  in the toolbar, or press `C` to enter comment mode. Your cursor will turn into a .
2. Select a location to comment on:
   - Click the location on the canvas where you'd like the comment to be pinned.
   - Or, click and drag your cursor to select a region to comment on.
3. Type your message in the field. Type `@` to [mention](../comments/add-comments-to-files.md#mention) a colleague or collaborator.
4. Click  to send your message.

### Use plugins

You’ll need `can edit` access to use plugins in a file.

## I don't have Dev Mode, and I have can edit access

**Need access to [Dev Mode](https://help.figma.com/hc/en-us/articles/15023124644247)**? If you’re on the Starter plan, you’ll need to [upgrade to a paid plan](https://figma.com/pricing) or [move your file](https://help.figma.com/hc/en-us/articles/360038511573) to a paid team. If you’re on a paid plan, you’ll need a Full or Dev seat.

With `can edit` access to a design, you can use inspection tools directly within Design Mode:

### Measure distances

You can measure distances between objects, even if they are nested within frames, groups, or components.

1. Select the first object in the canvas.
2. Hold down the modifier key:
   - Mac: ⌥ Option
   - Windows: Alt
3. Hover over the second object.

Figma will display a red line between the two objects, as well as horizontal and vertical measurements.

**Tip**: Having trouble measuring? Check out the [guide to measuring the distance between objects](../work-with-layers/measure-distances-between-layers.md).

### Generate code

You can copy auto-generated code snippets for CSS, iOS, or Android.

1. Select an object on the canvas.
2. Right-click on the object and select **Copy/Paste as** > **Copy as code**.
3. Select the code option that suits your needs.

### View properties

The **Design** tab gives you a list of properties for objects on the canvas. This includes properties like: layout, color, typography, text strings, component properties, styles and variables. To view the properties of an object:

1. Select an object on the canvas.
2. In the Design tab in the right sidebar, scroll to the section with the properties you’d like to inspect.

### Export

1. Select the layers you want to export. If you want to export the entire canvas of the current page, deselect everything on the canvas.
2. In the **Design** tab, click the  plus icon in the **Export** section to add an export configuration. You can add as many export configurations to a selection as needed.
3. Configure the export settings. Learn more about [Figma's export formats and settings](https://help.figma.com/hc/en-us/articles/13402894554519).
4. If needed, click **Preview** to see how your asset will look. If you have multiple objects selected, the **Preview** setting won’t display.
5. Click **Export**.

**Tip**: Want to learn more about exporting? Check out the full [guide to exports in Figma](https://help.figma.com/hc/en-us/articles/360040028114-Export-from-Figma).

### View or add comments

[Comments](https://help.figma.com/hc/en-us/articles/360041068574) help designers and developers collaborate by drawing attention to specific parts of the design. You can leave comments to share more context about how parts of the design should work.

1. Click  in the toolbar, or press `C` to enter comment mode. Your cursor will turn into a .
2. Select a location to comment on:
   - Click the location on the canvas where you'd like the comment to be pinned.
   - Or, click and drag your cursor to select a region to comment on.
3. Type your message in the field. Type `@` to [mention](../comments/add-comments-to-files.md#mention) a colleague or collaborator.
4. Click  to send your message.

### Use plugins

You can run a plugin from the Community or directly from a file in Figma or FigJam.

1. Click  **Resources** in the toolbar.
2. From the **Plugins** tab, select from your recently used or saved plugins or search for a plugin from the Community.
3. Click on a plugin to view its details.
4. Click **Run** to run the plugin in the current file.

[Learn more about using plugins in files.](https://help.figma.com/hc/en-us/articles/360042532714)

## I have Dev Mode

To inspect designs, enter Dev Mode by selecting the  Dev Mode toggle or by using the keyboard shortcut `Shift` `D`. From there, you can use the following inspection tools:

### Measure distances

You can measure distances between objects, even if they are nested within frames, groups, or components. In Dev Mode, select any parent or child layer on the canvas. When you hover over surrounding layers, Figma displays padding values or distances between the two objects. You can also measure the distance between specific objects:

1. Select the first object in the canvas.
2. Hold down the modifier key:
   - Mac: ⌥ Option
   - Windows: Alt
3. Hover over the second object.

Figma will display a red line between the two objects, as well as horizontal and vertical measurements.

### Generate code

Click any object on the canvas while in Dev Mode to populate the **Code** section in the inspect panel. Depending on what’s selected, a typographic preview or box model is displayed, followed by autogenerated code snippets for the object.

To change your language and unit selection, or use a codegen plugin:

1. In the top-right of the **Code** section, select a language or plugin from the dropdown.
2. If required, click  **Inspect settings** and select a unit from the dropdown.

[Learn how to use code snippets in Dev Mode.](https://help.figma.com/hc/en-us/articles/15023202277399)

**Note:** Some Dev Mode features like the **Code** section won't appear in the inspect panel if [copying and sharing are disabled on the file](https://help.figma.com/hc/en-us/articles/360040045574-Restrict-copying-and-sharing-on-files).

### View properties

In Dev Mode, the **Inspect** tab gives you a list of properties for objects on the canvas. This includes properties like: layout, color, typography, text strings, component properties, styles, and variables. To view the properties of an object:

1. In Dev Mode, select an object on the canvas.
2. In the Inspect tab in the right sidebar, scroll to the section with the properties you’d like to inspect.

**Tip:** When inspecting a component or instance, you'll see a component preview, a link to the main component, as well as any links to relevant documentation and dev resources. The component playground appears in the **Inspect** panel when a component instance is selected. Use the playground to experiment with the components different properties without changing the actual design.

### Explore variables

Dev Mode includes a few ways of working with variables when you're inspecting a design:

- [View details about a variable](variables-in-dev-mode.md#h_01JD03NW7F4WS8EXKQHS6E5M1V), including the value and mode. You can swap modes, and, if the value uses any aliases, the entire alias chain down to the variable's raw value.
- [Get suggested variables](variables-in-dev-mode.md#h_01JD03NW7FA3PYRN5PK9GD2VZ5) for raw values in a design, if the values match one or more of your existing variables.
- [Access the variable collections created in the current file](variables-in-dev-mode.md#h_01JD03NW7FX7SE3KQJQYQTZQ7K) and view all the variables and modes in a table.

For more details, see [Variables in Dev Mode](https://help.figma.com/hc/en-us/articles/27882809912471).

### Export assets

Dev Mode can automatically detect icons and present them as downloadable assets for developers. You’ll see these assets in the **Inspect** tab above the export settings. Hover over any item, select a file type, and click the download icon.

To set up a custom export:

1. In Dev Mode, select the layers you want to export.
2. In the **Inspect** tab, click the  plus icon in the **Export** section to add an export configuration. You can add as many export configurations to a selection as needed.
3. Configure the export settings. Learn more about [Figma's export formats and settings](https://help.figma.com/hc/en-us/articles/13402894554519).
4. If needed, click **Preview** to see how your asset will look. If you have multiple objects selected, the **Preview** setting does not display.
5. Click **Export**.

### Specify size of image export

Download any selected image on the canvas, and choose between downloading the image at its current size on the canvas or the original image at full resolution.

1. In Dev Mode, select the image you want to download.
2. From the **Assets** section in the right sidebar, hover over the image you want to download and click the  **Export** icon that appears.
3. From the dropdown, choose from one of the options:
   - **Source image file**: Download the original image that was used when the image was first imported into Figma.
   - **Layer export**: Download the image at its current layer size.

![Export settings with size options for source image and layer export, showing download icon in asset panel.](https://help.figma.com/hc/article_attachments/32594816553111)

**Tip**: If you’d like to do a **layer export**, you can choose which file format to export the image to. In the **Assets** section, click the **Open image export settings** icon, then use the dropdown to choose from PNG, JPEG, SVG, or PDF formats.

### View or add annotations

Before you Start

Who can use this feature

Available on all paid plans

Anyone with a [Full seat](https://help.figma.com/hc/en-us/articles/360039960434-Free-and-paid-seats-in-Figma#editor) and `can edit` access to a file can add measurements and annotations

Anyone with a [Full](https://help.figma.com/hc/en-us/articles/360039960434-Free-and-paid-seats-in-Figma#editor) or a [Dev seat](https://help.figma.com/hc/en-us/articles/19813618057623-Dev-Mode-GA-for-admins#h_01HKN19J4JJTKGMATHW6BP331A) and at least `can view` access to a file can view measurements and annotations

With annotations, designers can communicate key details about a design directly to developers. This includes highlighting important properties, visualizing spacing and sizing with measurements, or sharing context with text notes. For a more detailed explanation, see [Add measurements and annotate designs](https://help.figma.com/hc/en-us/articles/20774752502935).

In Dev Mode, annotations appear on the canvas as a green dot. Click an annotation to reveal its contents.

To add annotations to a design:

1. Click the Dev Mode toggle in the top-right of the toolbar or use the keyboard shortcut `Shift` `D`.
2. Click **Annotate** in the toolbar or use the keyboard shortcut `Shift` `T`.
3. Select the layer you’d like to annotate.
4. Write a note in the text field, or click **+ Property** to select a property from the list. You can include both plain text and properties in an annotation.

To add a measurement to a design:

1. Click **Measure** in the toolbar or use the keyboard shortcut `Shift` `M`.
2. Hover over a layer to see options for where to start your measurement.
3. Click and drag from your starting point to the layer where you want the measurement to end.
4. Click and drag the measurement so it doesn’t cover the design.

### Use plugins

The **Plugins** tab in Dev Mode shows your recently used plugins, as well as recommended plugins from the Figma Community.

[Learn how to use plugins in files](https://help.figma.com/hc/en-us/articles/360042532714-Use-plugins-in-files).

### Compare changes

If a frame or component has been updated since you last viewed it, you can compare its version history. This helps you track the latest updates and keep production code accurate.

You can also compare detached components—or instances with design overrides—against the base component.

1. Select a top-level frame or component.
2. In the Inspect tab of the right sidebar, click **Compare changes**.

**Tip:** Hold `Shift` and click to select two components on the canvas to compare them with each other.

[Learn more about comparing changes in Dev Mode](compare-changes-in-dev-mode.md).