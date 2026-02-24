# Add or remove a library from a design file

Source: https://help.figma.com/hc/en-us/articles/1500008731201-Add-or-remove-a-library-from-a-design-file

---

Before you start

Who can use this feature

Available on [paid plans](https://help.figma.com/hc/en-us/articles/360040328273).

Anyone with `can edit` access to a file can manage libraries for that file.

This article applies to Figma Design files only. Learn how to [manage libraries in FigJam files](https://help.figma.com/hc/en-us/articles/1500004290841).

When you add a library to a file, you’ll be able access its components, styles, and variables and use them in the file. Components can be accessed from the **Assets** tab, and styles and variables can be accessed from the styles and variables picker on various properties.

A library must be published before you can add it to a different file.

Adding or removing a library from a file will apply to everyone with access to the file.

**Note**: In order to access a library’s styles, components, and variables, users need at least `can view` access to the library.

## Add a library to a file

To add a library to a file, the [library needs to be published to team libraries](https://help.figma.com/hc/en-us/articles/360025508373) first.

To add a library:

1. In a design file, select the **Assets** tab in the left sidebar.
2. Click the **Libraries** icon to open the **Libraries** modal. The icon’s tooltip may read **Review library updates** if there are updates to libraries you are using in the file, or **Review unpublished changes** if you have unpublished updates in your file.
3. Locate the library you want to enable. Use the search bar to search your library by name. If available, use the sections under **Browse libraries** to find relevant libraries across your team or organization.
4. Click the library to view its assets. From there you can:
   - Click **Add to file** to enable the library in the file
   - Click **Open file** to view the library file
5. Click to close the modal.

![Libraries modal showing Habitz Design System assets with Add to file button highlighted in the upper right corner.](https://help.figma.com/hc/article_attachments/27999040559767)

Tip: If a library has a check mark next to its name, it means the library has been [approved by an admin](https://help.figma.com/hc/en-us/articles/21310245473815). Available on the [Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273) only.

In the **Libraries** modal, you can browse libraries available to you and add them to the current file. The **Browse libraries** section has a few tabs you can use to browse:

### Browse libraries

- **Recommended**: Contains approved libraries ([Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features) only) and default libraries provided by the admin of your organization or team.
- **Teams / Your teams**: Browse libraries in teams you belong to
- **Your organization**: Browse libraries by workspace.
- **UI kits**: UI kits are a set of libraries curated by Figma and partners. This tab is available if UI kits are enabled by admins for your team or organization.

![Libraries modal with tabs for Recommended, Your teams, Your organization, and UI kits highlighted in the left sidebar.](https://help.figma.com/hc/article_attachments/27999056226711)

## Remove a library from a file

To remove a library from a file:

1. In a design file, select the **Assets** tab in the left sidebar.
2. Right-click the library you want to remove and select **Remove library from file**.

Any components, styles, or variables used from the removed library will remain on the canvas.

## Access styles, components, and variables in a library

When you make a library available in a design file, everyone in the file can access assets from it.

Styles Components Variables

Find and apply styles using the  **Style and variables** picker in the right sidebar. Learn how to [apply styles in Figma Design](https://help.figma.com/hc/en-us/articles/360040316193). ![Cursor pointing to style and variables picker in Figma's Fill section for applying styles. The icon for the picker is four small circles arranged in a 2 by 2 square.](https://help.figma.com/hc/article_attachments/27999040564887)

Drag components into the canvas from the **Assets** tab in the left sidebar. Learn how to [add components to your designs](https://help.figma.com/hc/en-us/articles/360039150173). ![Assets tab open in Figma, displaying search bar and library options, cursor pointing at tab label.](https://help.figma.com/hc/article_attachments/27999040567063)

Variables can be applied to various properties from the right sidebar. Learn how to [apply variables to designs](https://help.figma.com/hc/en-us/articles/15343107263511). ![Cursor pointing at the border radius input field set to a variable with the value of 2. The value is enclosed in a small white box to indicate it is provided by a variable.](https://help.figma.com/hc/article_attachments/27999040574231)