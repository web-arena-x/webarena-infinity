# Publish a library

Source: https://help.figma.com/hc/en-us/articles/360025508373-Publish-a-library

---

Who can use this feature

Available on all [paid plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Requires a [Full seat](https://help.figma.com/hc/en-us/articles/360039960434) with edit access to the library's source file

Publish a [library](https://help.figma.com/hc/en-us/articles/360041051154) to share common design elements—like buttons, icons, pieces of UI, colors, or values for certain properties—with the rest of your team. Other people can use these design elements in their files, which helps everyone stay consistent.

When you first create a [style,](https://help.figma.com/hc/en-us/articles/360039238753) [component](https://help.figma.com/hc/en-us/articles/360038662654), or [variable](https://help.figma.com/hc/en-us/articles/15339657135383) in a file, it is only accessible from that file. To make it available in other files, you need to publish it as a [library](https://help.figma.com/hc/en-us/articles/360041051154).

If you make changes to these assets or add new ones, you can publish them as updates to the library. People using the library in their files can quickly [review the changes](https://help.figma.com/hc/en-us/articles/360039234193) and automatically update their designs.

**Note:** Libraries are only available on [paid plans](https://help.figma.com/hc/en-us/articles/360040328273). You can still create components and styles on the free Starter plan, but you can't publish them in a library to access them in other files.

## Publish a library

To publish a design file as a library, there needs to be at least one component, style, or variable in the file. If the file is in your drafts, you’ll need to move it to a project before publishing.

Once published, anyone with access to the library’s source file can use the library in their files.

**Tip**: A library inherits its name from the source file. Make sure you give your file a clear, meaningful name that helps people understand what it’s for, like ‘Habitz design system’, ‘UI3 library’, or ‘Website design kit’.

![Figma interface showing the Assets tab with a highlighted Libraries icon for managing design libraries.](https://help.figma.com/hc/article_attachments/25924848370327)

1. In a file with components, styles, or variables you’d like to share, select the **Assets** tab in the left sidebar.
2. Click the  **Libraries** icon. The tooltip may read **Review library updates** if there are updates to libraries you are using in the file, or **Review unpublished changes** if you have unpublished updates in your file.
3. From the **This file** section, find your current file and click **Publish**.
4. Add a description of the library's purpose, or a summary of any decisions or changes.
5. From the list of styles, components, or variables that have been added, modified, or removed, uncheck any assets you don't want to publish. You can also uncheck **Changes** to deselect everything.
6. *Organization and Enterprise plans only:* Use the dropdown menu to choose [where to publish the library](https://help.figma.com/hc/en-us/articles/360025508373#h_01J688PTA7N7AHMGZMA6QA1F1V).
7. Click **Publish**. A notification will appear confirming your library has been successfully published.

**Tip**: If you want to make sure certain components, styles, or variables never get published, you can [hide them in the publishing flow](https://help.figma.com/hc/en-us/articles/360039238193). Right-click on any asset in the library modal and select **Hide when publishing**. To undo, right-click it again and select **Show when publishing.**

**Why is the publish button not working?**

If the publish button is deactivated, it might be one of the following reasons:

- There are no [components](https://help.figma.com/hc/en-us/articles/360038662654), [styles](https://help.figma.com/hc/en-us/articles/360039238753), or [variables](https://help.figma.com/hc/en-us/articles/15339657135383) in the file. Try creating a new one to see if the option to publish appears.
- The library has no publishable changes. In this case, nothing has changed since the last time the library was published. Try editing a component, style or variable in the library. You may also need to check whether the design elements you’re editing are [hidden from publishing](https://help.figma.com/hc/en-us/articles/360039238193).

### Choose where to publish a library Organization and Enterprise

![Publish library panel showing component changes with dropdown for publishing to team, workspace, or organization.](https://help.figma.com/hc/article_attachments/25924823045655)

Organization or Enterprise plan users can publish libraries to a specific team or the whole organization. Enterprise plan users can also publish libraries to workspaces.

This helps libraries reach the right audience. For example, you might publish a company-wide design system library to the organization, or a library with mobile app components to the specific team working on the mobile app.

If the library’s source file has sharing permissions that are too restrictive, Figma will prompt you to change them. For example, if your file is set to **Only invited people can access** and you want to publish a library to the organization, you’ll be asked to change the file’s permissions to **Everyone at your organization can access**.

## **Publish updates to a library**

If you make changes to a style, component, or variable in a library’s source file, those changes will only appear in the current file until you publish them. Publishing updates to a library follows the same process as [publishing a library for the first time](https://help.figma.com/hc/en-us/articles/360025508373#h_01J688PTA7SPRDKBNDJ5RYVSP4).

**Note**: Once you’ve publish updates to a library, people using the library will see a blue badge on the library icon in the left sidebar of their file. They can then [review and accept the updates](https://help.figma.com/hc/en-us/articles/360039234193).

![Cursor hovering over 'Review library updates' tooltip next to the Libraries icon in the UI3 Library file panel.](https://help.figma.com/hc/article_attachments/25924848390679)

**Tip:** Every time you publish updates to a library, you'll be prompted to add a description. This allows you to communicate decisions and changes to the people who use your library.

Figma shows descriptions when [accepting updates from a library](https://help.figma.com/hc/en-us/articles/360039234193), as well as in the file's version history.