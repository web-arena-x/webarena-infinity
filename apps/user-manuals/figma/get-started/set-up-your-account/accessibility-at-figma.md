# Accessibility at Figma

Source: https://help.figma.com/hc/en-us/articles/35063862380311-Accessibility-at-Figma

---

At Figma, we’re actively working to make design in Figma accessible to all. This means working towards making our product WCAG 2.2 AA compliant, the current recommended standard for accessibility guidelines on web. Below is our guide to help enable a more accessible experience in Figma.

Accessibility features in Figma are available when using Figma in a web browser, the [Figma Desktop app](https://help.figma.com/hc/en-us/articles/5601429983767), and [Figma for iOS and Android](https://help.figma.com/hc/en-us/articles/1500007537281).

## Make Figma accessible to you

### Turn on Figma accessibility settings

Once you’ve set up accessibility features on your computer, you can adjust your **Accessibility settings** in Figma. To do so:

1. Press `F6` on Mac or `Control` `F6` on Windows to select the main menu in the top left and press `Enter` to open the menu.
2. Use arrow keys to navigate to **Preferences** and press `Enter` to open the submenu.
3. Use the arrow keys to navigate to **Accessibility settings** and press `Enter` to open the modal.

With the Accessibility settings open, press `Enter` to toggle the switches and `Tab` to move between settings.

From here, you can adjust your preferences to:

- Adapt content to screen readers
- Simplify focus navigation in the [**Actions** menu](../../figma-design/file-utilities/use-the-actions-menu-in-figma-design.md)
- Toggle [enhanced contrast](https://help.figma.com/hc/en-us/articles/5576781786647-Change-themes-in-Figma#h_01K57AMY9Y08P2656MNM2HDS1H) for the Figma UI
- Ignore Figma-specific shortcuts in text fields
- Toggle automatically following a collaborator when they turn on [spotlight](../../figma-design/multiplayer-tools/present-to-collaborators-using-spotlight.md#file) in a file

### Navigate Figma products with a keyboard

- Use `F6` / `Control` `F6` to navigate between top-level areas of the interface
- Use `Tab` / `⇧Shift` `Tab` to navigate within sections of the interface and layers on the canvas
- Use `Return` / `Enter` or `⇧Shift` `Return` / `Enter` to navigate in and out of layers on the canvas
- Use `⌘Command` `K` to search actions and tools

### Figma for mobile apps

Figma mobile apps are available for iOS and Android:

- Both Figma mobile apps are compatible with built-in mobile screen readers.
- Figma for iOS is compatible with VoiceOver, and Figma for Android is compatible with TalkBack.
- Both apps support enhanced contrast mode

### Use the actions menu in Figma

**Actions** offers a fast and easy way to access features in Figma files.

Press `⌘Command` `K` on Mac or `Control` `K` on Windows to open the **Actions** menu, then type relevant keywords into the **Search** field to quickly find the action you need. For example, typing ‘align’ will show all alignment-related actions.

[Learn more about the Actions menu.](../../figma-design/file-utilities/use-the-actions-menu-in-figma-design.md#h_01J0XWBCYBAPNE2615C6JGM75Q)

### Adjust your zoom and view options

Use the following keyboard shortcuts to change the zoom percentage:

- **Zoom in**: `⇧Shift` `+`
- **Zoom out**: `⇧Shift` `-`
- **Zoom to fit**: `⇧Shift` `1`
- **Zoom to selection**: `⇧Shift` `2`

### Adjust the scale of the Figma UI

Use your keyboard to adjust the scale of the Figma interface. Resize the toolbar, side panels, and menus to your need.

**Mac:**

- Reset to Default: `⌥ Option` `⇧ Shift` `⌘ Command` `0`
- Make Larger: `⌥ Option` `⇧ Shift` `⌘ Command` `=`
- Make Smaller: `⌥ Option` `⇧ Shift` `⌘ Command` `-`

**Windows:**

- Reset to Default: `Control` `⇧Shift` `Alt` `0`
- Make Larger: `Control` `⇧Shift` `Alt` `=`
- Make Smaller: `Control` `⇧Shift` `Alt` `-`

### Change themes in Figma

To change your theme from the Actions menu:

1. Open any file you have access to.
2. Select the **Actions** menu in the toolbar or use the keyboard shortcut:
   - Mac: `⌘Command` `K`
   - Windows: `Control K`
3. Type in search terms and select the theme you want to use
   - **Use dark mode**
   - **Use light mode**
   - **Use system theme**

[Learn more about adjusting the Figma theme and contrast.](https://help.figma.com/hc/en-us/articles/5576781786647-Change-themes-in-Figma)

### Pan and zoom the canvas

With nothing selected, you can use the arrow keys to pan around the canvas. You can also pan while a tool is active, such as the Frame or Text tool.

Hold `⇧Shift` while pressing the arrow keys to increase the pan distance and move faster. The distance changes based on your current zoom level. To zoom in or out, hold `⌘Command`/`Control` and press `+` or `-`.

### Add objects to the canvas

You can create new objects like frames, shapes, or text layers using keyboard controls.

To create a new object:

1. Enable the desired tool using its keyboard shortcut, the **Actions** menu, or press `F6`/`Control` `F6` until the toolbar is focused, then use the arrow keys to select the tool.
2. Use the arrow keys to activate the crosshair cursor. It will appear in the middle of the viewport indicating where the new object will be placed.
3. Use the arrow keys to move the crosshair around the canvas or board, then press `Return`/`Enter` to place the object.

### Select objects on the canvas

The Keyboard box selection tool lets you select objects on the canvas using your keyboard. Use the shortcut to activate the keyboard selection tool:

- **Mac:** `Option` `Space`
- **Windows:** `Control` `Space`

Once activated, a pink cursor appears on the canvas. Use the arrow keys to position the cursor over and object and press `Return`/`Enter` to select it. If the selected object is a parent layer, use `Tab` and `⇧Shift` `Tab` to move between its child layers.

To select multiple layers at once, draw a selection box by holding `⌘Command` (Mac) or `Control` (Windows) and use the arrow keys to resize the box. You can hold `⇧Shift` while resizing to increase the adjustment size. As you move the box, the viewport adjusts to ensure the full selection is visible.

Press `Esc` to close the keyboard box selection tool.

There are two ways to select objects on the canvas with your keyboard:

- **Box select** lets you select a contiguous group of objects on the canvas. Move and expand the box cursor over an object or group of objects to make your selection.
- **Pick select** lets you cycle through objects on your canvas using your keyboard.

Activate the **Select** tool by pressing `⌥Option` `Space`/`Control` `Space`. This activates the box select tool and places a pink box cursor on the canvas. Press `Tab` to switch to pick select, or use `⌥Option` `Space` / `Control` `Space` to switch between the two select tool types.

#### Box select

Once activated, a pink dashed box cursor appears on the canvas at the center of the viewport. Use the arrow keys to position the cursor over and object, holding `⇧Shift` for big nudges, and press `Return` / `Enter` to select it. If the selected object is a parent layer, use `Tab` and `⇧Shift` `Tab` to move between its child layers.

To select multiple layers at once, draw a selection box by holding `⌘Command` (Mac) or `Control` (Windows) and use the arrow keys to resize the box. You can hold `⇧Shift` while resizing to increase the adjustment size. As you move the box, the viewport adjusts to ensure the full selection is visible.

Press `Esc` to close the keyboard box selection tool.

#### Pick select

Once activated, a pink outline is placed on a selected objects on the canvas, or any node if nothing is selected. The `Tab` and `Enter` keys that normally select objects now move the pick cursor structurally among children and sibling layers of a parent object, like a frame, component, or group following the **Layers** panel outline.

To use pick select:

1. Press `⌥Option` `Space`/`Control` `Space` to activate the **Select** tool.
2. Press `Tab` or `⌥Option` `Space` / `Control` `Space` again to switch to pick select.
3. Use `Tab` to move between parent objects on the canvas, and `Return`/`Enter` and `⇧Shift` `Return` / `Enter` to move between parent and child layers.
4. Press `Space` to make you selection.

Press `Esc` or click anywhere on the canvas to exit selection mode.

### Rotate objects with a keyboard

Use your keyboard to rotate an object in a Figma Design, FigJam, or Slides file from the **Accessibility settings** section of the main menu.

- Press `⌘Command`  `⌥Option` `↑`/ `↓` on Mac or `Control` `Alt` `↑`/`↓` on Windows to rotate an object one degree at a time
- Press `⌘Command`  `⌥Option` `⇧Shift` `↑`/ `↓` on Mac or `Control` `Alt` `Shift` `↑`/`↓` on Windowsto rotate an object 15 degrees at a time

### Activate links on the canvas and in text

When editing text, press `⌥Option` `Return`/`Alt` `Enter` to activate a focused link.

### Add, manage, and move comments

To access comments, press `C` and use `F6` or `Control` `F6` to navigate to the canvas and `Tab` through comments pins. Press `Return`/`Enter` to select a pin. You can also tab through the comments panel.

#### Add a comment to an object

- [Select an object on the canvas](#h_01K7FGP0TSK59TNV5TBCSZWHV0).
- Press `⌘Command` `K` to open the **Actions** menu.
- Select **Create new comment** from the menu.

A comment will be created + it’ll be anchored to the selected node

#### Move through comments on the canvas:

1. Press `C` to enter comment mode.
2. Use `F6`/`Control` `F6` to move through regions until you see a comment icon appears in the middle of the viewport or hear an announcement to **Create new comment**.
3. Use `Tab` to move between comment pins.

#### Relocate comment pins:

1. Press `C` to enter comment mode.
2. Use `F6`/`Control` `F6` to move through accessible areas until you see a comment icon.
3. Use `Tab` to move between comment pins.
4. Once you’re focused on the comment pin you want to relocate, use the arrow keys and hold `⇧Shift` to move with big nudges.

### Ignore Figma shortcut override

Toggle the option to ignore Figma shortcuts when using special characters in text fields:

1. Press `⌘Command` `K` or `Control` `K` to open the **Actions** menu.
2. Type **Accessibility settings** in the search bar.
3. Toggle the option to **Ignore Figma shortcuts**.

### Turn off automatic follow for spotlight

Toggle the option to automatically follow a presenter using spotlight:

1. Press `⌘Command` `K` or `Control` `K` to open the **Actions** menu.
2. Type **Accessibility settings** in the search bar.
3. Toggle the option to **Automatically follow spotlight**.

## Figma Design

### Measure distance between objects

1. Select an object on the canvas to measure from.
2. Press `⌥Option` `Space`/`Control` `Space` to activate the **Select** tool again.
3. Press `Tab` or `⌥Option` `Space` / `Control` `Space` again to switch to pick select.
4. Use `Tab` / `Shift` `Tab` to move between parent objects on the canvas, and `Return`/`Enter` and `⇧Shift` `Return` / `Enter` to move between parent and child layers.
5. Press `⌥Option` to activate the measurement tool.

At this point you will see measurements between the first selected object, and the one highlighted using `Tab`. If you're using a screen reader, hover your mouse over a measurement and press `Space` to repeat the value of the measurement.

### Add and adjust guides

Before you can add and view page ruler guides, make sure they are turned on by going to the **File** menu > **View** > and checking **Rulers**.

To add and adjust ruler guides with a keyboard:

1. Press `⌘Command` `K` or `Control` `K` to open the **Actions** menu.
2. Type **Adjust ruler guides** in the search bar.
3. Use `F6`/`Control` `F6` to move through accessible areas until you reach the right sidebar.
4. Use `Tab` to navigate to the **Page ruler Guides** section of the sidebar.

Once there, press `Return`/`Enter` when focused on the **Plus** icon for the **Vertical** and **Horizontal** sections to add a guide, enter a value in the text field, and press the **Minus** icon to remove the guide.

To exit, press `Esc`, or click **Close** in the right sidebar.

### Add, view, and manage annotations

To get started from a file in Design or Dev Mode, go to > **Preferences** > **Accessibility settings** > and toggle on **Adapt content for screen readers**.

#### Add an annotation

1. [Select the object](#h_01K7FGP0TSK59TNV5TBCSZWHV0) you want to annotate.
2. Press `⇧Shift` `T` to activate the **Annotation** tool.
3. Open the context menu by pressing:
   1. VoiceOver on Mac: `⌃Control` `⌥Option` `⇧Shift` `M`
   2. Full Keyboard Access on Mac: `Tab` `M`
   3. Windows: `⇧Shift` `F10`
4. Select **Add annotation**.
5. Add you annotation, then use `Tab` to add a property or `Return`/`Enter` to close the modal.

Note: It’s currently not possible to add measurements using a keyboard.

#### Select an annotation

1. Select the parent frame for the annotation.
2. Use `F6`/`Control` `F6` to move through the accessible areas until the first annotation of the target node is selected.
3. Use `Tab`/`⇧Shift` `Tab` to toggle through the sibling annotations.
4. Press `Enter` to edit.

#### Edit or delete annotation

With an annotation selected:

- Press `Return`/`Enter` to enter edit mode
- Press `Tab` to move between the annotation modal’s properties
- Press `Delete`/`Backspace` to delete it

[Learn more about annotating designs.](../../figma-design/inspect-designs/add-measurements-and-annotate-designs.md)

### Change the background color of the canvas

To change the background color:

1. Deselect any layers on the canvas.
2. From the **Page** section of the properties panel on the right side of the screen, click the color fill to select a new color. You can also enter a specific hex value if you prefer.
3. If needed, set the opacity on the background by clicking **100%** and entering a new value.

[Learn more about changing the background color of the canvas.](../../figma-design/explore/change-the-background-color-of-the-canvas.md)

## FigJam

### Add connectors and lines to the board

#### Add connectors and lines to your FigJam board using your keyboard.

1. Activate the connector or line tool:
   - Press `X` to add a bent connector or `L` to add a straight line
   - Or, navigate to the toolbar, press `Return`/`Enter` to pick a line style > `Esc` to refocus the canvas.
2. Use the arrow keys to move the crosshair cursor to the line’s starting point.
3. Press `Return`/`Enter` to set the starting point.
4. Use the arrow keys to navigate to the end point.
5. Press `Return`/`Enter` or `Esc` to set the end point.

#### Add text to a connector or line:

1. Select the connector and press `Return`/`Enter` to edit.
2. Add your text to the field.
3. Press `Esc` when finished.

#### Move a connector or line:

1. Select the connector or line.
2. Use the arrow keys to move, and use `⇧Shift` with the arrow keys to move in bigger nudges.

To edit a connector or line:

1. With a line selected, use `F6`/`Control` `F6` to navigate to the selection menu to adjust color, typeface, font size, and formatting.
2. Press `Return`/`Enter` to open a property submenu, then use `Space` to apply a new line style, color, or end point.

### Add stamps and cast votes in FigJam with a keyboard

To add a stamp:

1. Press `E` to open the stamp and emote wheel.
2. Use `Tab` to move between the stamps and press `Return` / `Enter` to select it.
3. Use the arrow keys to pick a spot to stamp, then press `Return` / `Enter` to place it on the board.

### Edit tables in FigJam with a keyboard

To edit a table on the FigJam board:

1. Select the table by navigating to it or using `⌥Option` `Space`.
2. Press `⌘Command` `⌥Option` `Space` on Mac / `Control` `Alt` `Space`on Windows to select a cell. Press `Return` / `Enter` to enter text edit mode for a cell.
3. Edit your cell’s text.

With a cell selected, use `F6`/`Control` `F6` to navigate to the text properties menu to adjust color, typeface, font size, and formatting.

#### Keyboard shortcuts for editing tables in FigJam

| **Action** | Mac | Windows |
| --- | --- | --- |
| Selection | | |
| Select cell | Command+Option+Space | Control+Alt+Space |
| Select current column | Command+↑, Command+↓ | Control+↑, Control+↓ |
| Select current row | Command+←, Command+→ | Control+←, Control+→ |
| Cell navigation | | |
| Move cell selection left | ← | ← |
| Move cell selection right | → | → |
| Move cell selection up | ↑ | ↑ |
| Move cell selection down | ↓ | ↓ |
| Extend selection | | |
| Extend cell selection left | Shift+← | Shift+← |
| Extend cell selection right | Shift+→ | Shift+→ |
| Extend cell selection up | Shift+↑ | Shift+↑ |
| Extend cell selection down | Shift+↓ | Shift+↓ |
| Insert rows and columns | | |
| Add row above | Option+Shift+Enter | Alt+Shift+Enter |
| Add row below | Option+Enter | Alt+Enter |
| Add column before | Option+[ | Alt+[ |
| Add column after | Option+] | Alt+] |
| Resize rows and columns | | |
| Increase row height | Option+↓ | Alt+↓ |
| Decrease row height | Option+↑ | Alt+↑ |
| Increase row height (large step) | Option+Shift+↓ | Alt+Shift+↓ |
| Decrease row height (large step) | Option+Shift+↑ | Alt+Shift+↑ |
| Increase column width | Option+→ | Alt+→ |
| Decrease column width | Option+← | Alt+← |
| Increase column width (large step) | Option+Shift+→ | Alt+Shift+→ |
| Decrease column width (large step) | Option+Shift+← | Alt+Shift+← |
| Reorder rows and columns (must select entire row/column) | | |
| Move row up | Command+Shift+↑ | Control+Shift+↑ |
| Move row down | Command+Shift+↓ | Control+Shift+↓ |
| Move column left | Command+Shift+← | Control+Shift+← |
| Move column right | Command+Shift+→ | Control+Shift+→ |
| Deletion | | |
| Delete selection | Backspace | Backspace |

## Dev Mode

### View annotations in Dev Mode

To get started from a file in Design or Dev Mode, go to > **Preferences** > **Accessibility settings** > and toggle on **Adapt content for screen readers**.

#### Add an annotation

1. [Select the object](#h_01K7FGP0TSK59TNV5TBCSZWHV0) you want to annotate.
2. Press `⇧Shift` `T` to activate the **Annotation** tool.
3. Open the context menu by pressing:
   1. VoiceOver on Mac: `⌃Control` `⌥Option` `⇧Shift` `M`
   2. Full Keyboard Access on Mac: `Tab` `M`
   3. Windows: `⇧Shift` `F10`
4. Select **Add annotation**.
5. Add you annotation, then use `Tab` to add a property or `Return`/`Enter` to close the modal.

Note: It’s currently not possible to add measurements using a keyboard.

## Slides

### Tone dial

You can use Figma AI to adjust the tone of any text within your slides.

1. In **Slide** view, use `F6`/`Control` `F6` to navigate to the right sidebar.
2. Focus on the **Adjust tone** icon > press `Return`/`Enter`.
3. Press `Tab` once to focus the tone dial.
4. Use arrow keys to progress left to right and top to bottom. The tone adjusts as you move around the grid.

[Learn more about adjusting tone with Figma AI.](https://help.figma.com/hc/en-us/articles/24244814883735-Adjust-tone-using-Figma-AI)

### Presenter notes

To add presenter notes:

1. In **Slide** view, use `F6`/`Control` `F6` to navigate to the handle for presenter notes. Use `↑` and `↓` arrows to adjust the size of the notes field.
2. Press `Tab` to focus the presenter notes field, then `Return`/`Enter` to enter edit mode and add text.

[Learn more about using presenter notes in Figma Slides.](../../figma-slides/present-slide-decks/add-and-view-presenter-notes.md)