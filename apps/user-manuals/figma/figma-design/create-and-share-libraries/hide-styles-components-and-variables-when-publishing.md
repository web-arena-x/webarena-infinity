# Hide styles, components, and variables when publishing

Source: https://help.figma.com/hc/en-us/articles/360039238193-Hide-styles-components-and-variables-when-publishing

---

Who can use this feature

Supported on [paid plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Anyone with can edit can remove styles and components from a library

New to components? [Guide to libraries →](https://help.figma.com/hc/en-us/articles/360041051154)

There are a couple of ways to remove a style, component, or variable: you can hide it when publishing, or delete it entirely.

Are you a member of an organization? Use [Library analytics](https://help.figma.com/hc/en-us/articles/360039238353) to track component usage, including when components are detached.

## Hide a style

### Hide a style when the style is already published

To hide a style when it is already published in a library, you need to unpublish it. You can only hide a style from the original file where the style is defined.

You can access the original style from any object that is currently using it:

1. Select an object in the canvas that uses that style.
2. Click on the style in the right sidebar
3. Click the icon to edit the style.
4. Click **Go to style definition** to open the style in the library.

Note: You will also see an option to **Move style definition into this file**. This allows you to edit or delete that style without leaving the current file. Moving a style removes it from the original file. If you re-publish the original file, the style would no longer be included.

### Hide a style when publishing it for the first time

You can hide a style from a library without deleting the style itself. You can only do this from the original style, the style definition.

1. Open the file where the style lives.
2. Click **Assets** in the left sidebar, then click the **Libraries** icon. The tooltip may read **Review library updates** if there are updates to libraries you are using in the file, or **Review unpublished changes** if you have unpublished updates in your file.
3. Click **Publish # changes**.
4. Right-click the style and select **Hide when publishing**.
5. Repeat for any other style you want to unpublish.
6. Click **Publish** to apply your changes and remove the styles.

Note: If the library is published and up to date, you need to make changes to it to remove the style. Make changes to a library by editing or creating a main component or style. Then follow the instructions above starting with step 2.

### Delete a style

If you don't want to use a style at all, you can delete it. This won't update the properties of any layers using those styles, but will detach them from the style. You can only delete the style definition in the file it originates from.

1. Click an empty spot on the canvas or press `Esc` to deselect all layers.
2. From Local styles in the right sidebar, select one or more styles:
   - Hold down `Shift` and click to select a range styles
   - Hold down `⌘ Command` / `Control` and click to select multiple non-adjacent styles.
3. Select **Delete style** or **Delete all** from the options. Figma will remove the style and you will no longer be able to use it.
4. [Publish your changes to your library](https://help.figma.com/hc/en-us/articles/360038682574).

## Hide a component

You can hide components when you publish your library. You can only hide components from the file they originate from.

Note: You can open the file for any component from any file with access to those components. Right-click on an instance of that component in the canvas and select **Go to Main component**.

1. Open the library file which contains your main component.
2. Open the **Assets** panel in the left sidebar.
3. Right-click on the component and select **Hide when publishing**.
4. Figma will move the component(s) to the **Hidden** section.
5. [Publish the changes to your Team library](https://help.figma.com/hc/en-us/articles/360038682574).

Tip: You can also quickly remove a component from your Team library via the **Layers Panel.** Add a period `.` to the beginning of the component's name.

## Hide a variable

Like styles and components, you can hide variables when publishing your library. You can only hide variables from the file they originate from.

1. Open the library file where the variable is defined.
2. Click an empty spot on the canvas or press `Esc` to deselect all layers.
3. From **Local variables** in the right sidebar, click the **Open variables** icon.
4. From the **Variables** modal, find the variable you’d like to hide and click the **Edit variable** icon at the end of the row.
5. Check the **Hide from publishing** box and [publish your changes](https://help.figma.com/hc/en-us/articles/360038682574).

### Hide a variable collection

To hide an entire collection of variables from publishing to team libraries, prefix the collection name with `_` or `.`. For example, rename a Tokens collection to `_Tokens` or `.Tokens` to prevent it from being published. Remove the prefix to unhide it from publishing.

[Learn how to rename a variable collection →](https://help.figma.com/hc/en-us/articles/15145852043927-Create-and-manage-variables#Create_and_manage_variable_collections)