# Manage and share styles

Source: https://help.figma.com/hc/en-us/articles/360039820134-Manage-and-share-styles

---

Before you start

Who can use this feature

 

Anyone on any plan can create styles. To publish styles to libraries, you'll need to be on an [Education, Professional, Organization, or Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273).

Anyone with `can edit` access to a file can create and edit styles.

Anyone with `can view` access to a published file can use styles from that library in files they can edit.

Styles allow you to define a set of properties or attributes and reuse them across your designs. You can create styles for colors, text, effects, and layout guides.

# View styles

View styles available to you in this file from the style picker, or view styles that live in the file from the right sidebar when nothing is selected. Styles living in a file are do not include styles from other libraries that are in use.

To view styles from other published files, you can view them in the style picker for a selected property if the style's library is enabled. Learn more about [enabling libraries in a file](https://help.figma.com/hc/en-us/articles/360038743434-Enable-libraries-in-drafts-teams-and-files).

## Right sidebar

Once you have created at least one style within a file, you can view a list of styles living in the file from the right sidebar:

1. From the file, navigate to the **Design** panel in the right sidebar.
2. Deselect everything on the canvas:
   - Click on an empty spot in the canvas
   - Press `Esc` to deselect your current selection

From there, view styles living in the file from the **Styles** section.

![Right sidebar displaying text and color styles in a Figma design panel, highlighting style organization and editing features.](https://help.figma.com/hc/article_attachments/31358570041879)

## Style picker

View styles from the current file and styles from other libraries from the style picker.

Click the  styles icon next to the relevant property in the right sidebar. Figma will open the style picker which lets you to view any styles available for that property.

The default order for styles in the style panel is:

- Alphabetically by team name
- Alphabetically by file name
- Individual styles are in the same order as they appear in the right sidebar

You can toggle between  list and  grid views.

![Style picker panel showing color style options for a button in different libraries.](https://help.figma.com/hc/article_attachments/31358570044695)

# Manage styles

To make changes to a style, you will need to edit the style definition in its original file. It's not possible to make changes to the style from another file.

## Group styles

To make finding and selecting styles easier, you can organize your styles into groups. This can be done by using the `/` naming convention and by creating folders.

### Group by folder

You can group styles by creating folders from the **Design** tab of the right sidebar. Folders will be reflected from the **Local styles** section of the right sidebar and in the style picker when you click  for a given property.

To create a folder:

1. Select one or more styles:
   - Press `Shift` and click to select a range styles
   - Press `⌘ Command` / `Control` and click to select multiple non-adjacent styles.
2. Right-click the selected style(s) and click **Add new folder**.
3. Name the new folder and press `Return` / `Enter` to save.

Once created, the styles in the folder will be renamed according to their new heirarchy within the styles list. For example, if we have a style `Brand / Fuchsia` that was moved to the `Blog` folder within the `Brand` folder, it'll be renamed to `Brand / Blog / Fuchsia`.

To delete a folder and the styles in it, right-click the folder name and select **Delete.** You can also move all styles to another location to keep the styles and delete the folder.

### Group by name

Grouping styles using the slash naming convention involves adding a prefix to your style names so Figma groups them under the same heading.

In the example below, we use the slash naming convention to name and organize our styles:

- `Blog/color`
- `Brand Style Guide/Color`
- `Secondary/Color`

**Tip** Styles appear in the styles panel in the order they appear in the **Local styles** list. To change the order your styles appear, you can update by clicking and dragging them in the **Local styles** list from the file in which they were created.

## Reorder and move styles

When you view the **Styles** section in the right sidebar, you can see every style in the current file, grouped by the style type: text, color, effect, and layout guides.

By default, Figma will show styles in the order they were added. To make them easier to find and navigate, you can change the order or folder in which they appear.

1. Select one or more styles:
   - Press and hold `Shift` and click to select a range styles.
   - Press and hold `⌘ Command` / `Control` and click to select multiple non-adjacent styles.
2. Drag the style to change the order or move them to a new folder.

Moving a style from one folder to another changes the name for the style to reflect its place in the hierarchy. For example, moving the color style `Brand Style Guide / blue` to the `Blog` folder will also change the style name to `Blog / blue`.

Note: You can only adjust the order for styles that live in the current file you're in, Figma sorts styles in the style picker differently.

## Edit styles

You can edit styles that live in the file from the right sidebar and from the style picker.

- **Right sidebar:** hover over the style, then click the  **adjust** icon when it appears.
- **Style picker:** right-click on the style and select **Edit style** from the options.

View styles and their properties at the top of the **Edit style** panel.

- View or update the **Name** of the style.
- Add or update the style description, which displays when hovering over the style in the style picker.
- View or make changes to any properties of the style.
- Click on the  icon to hide or show the property on any objects the style is applied to
- Click the  icon to remove the property from the style

Any changes you make to the style here will update any objects in the file that use this style.

**Tip:** Access the original style when you view the style in the right sidebar. Right-click the style and select **Go to style definition** to open the file and edit the style there.![Style panel showing color palettes with a highlighted "Go to style definition" tooltip, indicating navigation to edit style details.](https://help.figma.com/hc/article_attachments/31358576137111)

## Copy and paste styles

You can copy existing styles from one file and paste them into another.

To copy and paste a style:

1. Click an empty spot on the canvas to de-select all layers.
2. Locate the style you wish to copy under the Styles section in the right sidebar.
3. Right-click the style and select **Copy style** from the dropdown menu, or use the keyboard shortcut:
   - Mac: `^Command` `C`
   - Windows: `Control` `C`
4. Open the destination file where you want to paste your style.
5. Right-click the canvas and select **Paste here**, or use the keyboard shortcut:
   - Mac: `^Command` `V`
   - Windows: `Control` `V`

Your pasted style will appear at the bottom of the Styles list in the destination file.

## Move styles between files

Warning: Before attempting to move styles between files, keep in mind that the only way to reverse the action is to repeat the entire process. It's not possible to reverse this action by using the undo keyboard shortcut or by restoring the file to a previous version.

To move styles between files:

1. Open the library file where the styles currently live. This is the source file.
2. Select styles or style folders:
   - Hold `Shift` and click to select a range of styles.
   - Hold `⌘ Command`/`Control` and click to select multiple non-adjacent styles.
3. Right-click the selected styles > **Cut styles** to add them to your clipboard. You can also use the shortcut:
   - Mac: `⌘ Command` `X`
   - Windows: `Control` `X`
4. Open the file you want to move the styles to. This is the destination file.
5. Right-click on the canvas > **Paste here** to paste the styles into the file. You can also use the shortcut:
   - Mac: `⌘ Command``V`
   - Windows: `Ctrl``V`

### Publish library changes

When you move published styles between files, Figma prompts you to publish your changes to any affected libraries.

You must publish these changes to complete the move process. Figma pushes updates to all subscribed files when you publish your changes.

1. Click **Publish** in the notification window, or use the shortcut to open the library modal:
   - Mac: `⌥ Option` `3`
   - Windows: `Alt` `3`
2. Add a description of your changes. Figma shows this in the file’s version history.
3. Click **Publish.**

Figma pushes updates to any file that uses those styles. You'll see the usual bell notification and a prompt to receive updates from the library. Learn how to [review and accept updates from libraries](https://help.figma.com/hc/en-us/articles/360039234193).

### Reverse or undo a style move

It's not possible to undo the action of moving styles using any of these methods:

- ❌ Using the undo keyboard shortcut
- ❌ Restoring an earlier version of either file

To reverse a style move, we recommend repeating the method outlined in the previous sections to move the style back to its original file. Be sure to publish and accept the changes afterwards.

## Duplicate styles

To save time when creating styles for your design system, you can duplicate existing styles instead of creating new ones each time.

To duplicate a style:

1. Click an empty spot on the canvas to de-select all layers.
2. Locate the style you plan to duplicate under the Styles section in the right sidebar.
3. Right-click the style and select **Duplicate style** from the dropdown menu.

The duplicated style will appear in the Styles list directly below your selection.

## Delete styles

If you would like to remove one or more styles, you can do this directly from the panel.

1. Select one or more styles:
   - Press and hold `Shift` and click to select a range styles.
   - Press and hold `⌘ Command` / `Control` and click to select multiple non-adjacent styles.
2. Select **Delete style** from the options.
3. Figma will remove the style and you will no longer be able to use it. Any objects using that style will keep their properties, but are detached from the style.

# Share styles

To access your styles in other files and projects, you can publish them to a [team library](https://help.figma.com/hc/en-us/articles/360041051154). You can publish styles on their own, or alongside any components.

Note: Publishing assets—styles, components, and variables—to team libraries is available on [paid plans](https://help.figma.com/hc/en-us/articles/360040328273).

## Publish styles to a library

1. Open the **Assets** panel in the left sidebar and click the  **Library** icon. Or, use the keyboard shortcuts:
   - Mac: `⌥ Option` `3`
   - Windows: `Alt` `3`
2. In the **This file** section, click **Publish** next to the file name.
3. Add a **description** of the changes you've made to the file. Figma will include your description in the [version history](https://help.figma.com/hc/en-us/articles/360038006754) of the file.
4. Click **Publish** to share them as a library.

When you publish changes to a library, Figma will prompt anyone using this library to receive updates. This makes sure any layers that use these styles use the most recent version.

## Use styles from a library

When you enable a library for a file, anyone with `can edit` access to that file can access those styles and components.

- View any style from that library in the style picker.
- View any styles from that library as a separate palette in the color picker.
- Use any styles that are shared with you. Learn how to [apply styles](https://help.figma.com/hc/en-us/articles/360040316193).
- Edit styles from files you have `can edit` access to.