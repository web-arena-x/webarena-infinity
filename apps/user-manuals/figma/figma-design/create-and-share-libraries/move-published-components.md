# Move published components

Source: https://help.figma.com/hc/en-us/articles/4404848314647-Move-published-components

---

Who can use this feature

Available on [paid plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan).

Only people with Can edit access to both the origin file and the destination file can move components between files.

**Want to move styles to another file?** Check out our [Manage and share styles](https://help.figma.com/hc/en-us/articles/360039820134) article for step-by-step instructions.

Move published components and component sets between files, without breaking links to instances. Use this process to split up large libraries into smaller files.

You can only use this process to move published components. You can still copy and paste main components and their instances between files. Figma will keep connections between components and instances as long as they remain in the same file.

Warning: Before attempting to move published components, please familiarize yourself with the process from start to end. Keep in mind, the only way to reverse this action is to repeat the entire process by moving the components back to their original file. It's not possible to reverse this action by using the undo keyboard shortcut or restoring the file to a previous version.

This is a multi-step process: cut and paste the components and publish the changes to the library. You must do both of these steps to move the component and update any connected instances. We also recommend review your components—for hidden components and deleted variants—before you move them.

![Button component being published in the Figma libraries panel.](https://help.figma.com/hc/article_attachments/4406218355351)

### How does it work?

Every component has a unique id. Figma uses this id to maintain the connection between the main component and any instances of that component.

When you cut and paste a component between files, Figma treats the pasted component as a new component. The new component has a unique id that's different from the original main component.

When you publish the duplicate to a library, Figma notifies any subscribed files of the changes. It's only when you accept these updates that Figma swaps to instances from the destination library.

Because of how this works behind the scenes, it's not possible to undo or reverse this process. The only way to [undo this action](#undo) is to move components back to their original file.

**Using library analytics?** Figma treats moved components as new components in your organization's Library analytics. Learn more [about library analytics](https://help.figma.com/hc/en-us/articles/360039238353).

View glossary of terms

- **Published component**: A component that is published to a team or organization library. Instances across files, projects, or team can receive updates from published components.
- **A component 'created in this file'**: A main component created in the current file.
- **Origin file:** Specific to the action of moving a component. The origin file is the file where components live(d) before being moved to a new location.
- **Destination file:** Specific to the action of moving a component. The destination file is the file where components are moved to, this can be a new or existing file/library.
- **Subscribed file**: A Figma Design or FigJam file with styles and instances that are linked to an active published library.

## 1. Review components

Before you start moving components, there are a few things to consider. We recommend reviewing any applicable steps to make sure your components work as intended in their new location.

1. Publish any hidden components you want to keep

Hidden components are components that you haven't published to your library. It's not possible to move hidden components between files.

If you have components that use nested instances of a hidden component, you need to [publish hidden components](https://help.figma.com/hc/en-us/articles/360025508373#individual), before you can move them to another file. Once you've moved those components and published the changes to the library, you can hide them again.

The entire process looks like this:

1. [Publish hidden components to library](https://help.figma.com/hc/en-us/articles/360025508373#individual)
2. [Cut and paste components into the destination file](#cut-paste)
3. [Publish the destination file as a library](#publish)
4. [Hide components to remove them from the library](https://help.figma.com/hc/en-us/articles/360025508373#private)

2. Check nested instances and overrides

If you have main components that use nested instances, you need to consider where the main components live. Especially if there are overrides applied to them.

If the main components are within the same file, we recommend you move and publish components together. If the main components for nested instances are hidden, you'll need to publish them first.

If components use main components from another published library, Figma will keep the connection to that library.

We recommend publishing components from the destination library, before you start making changes to those components.

**Let's explore an example**

You have a main component of a dialog window. In that component, are nested instances of a button component and an icon component. Both the icon and the button are hidden components.

In an instance of the dialog component, the generic information icon was swapped with a warning icon and color overrides were applied to both the icon and primary button.![Comparison of dialog components in Figma: an information dialog with blue button and warning dialog with red button.](https://help.figma.com/hc/article_attachments/4407467171991)

To successfully move these component and preserve overrides:

1. Publish icon and button components to the library. Learn how to [publish hidden components](https://help.figma.com/hc/en-us/articles/360025508373#individual).
2. Cut all components from the current file — this includes the icon and button components and the dialog component that uses instances of those components.
3. Paste those components into the destination file. [See below](#cut-paste).
4. Publish the destination file as a library. [See below](#publish).
5. [Accept updates from the library](https://help.figma.com/hc/en-us/articles/360039234193) in any subscribed files.
6. Hide both the icon and button main components. Learn how to [hide components when publishing](https://help.figma.com/hc/en-us/articles/360025508373#private).

3. Restore any deleted variants you want to keep

To move a component set, you need to cut and paste them between files. Figma will only copy the variants that exist at the time you cut and pasted them.

If you have deleted a variant, but want to use it again in the future, you need to restore the variant from the origin file. We recommend doing this before moving the component set. You can restore a deleted variant after you've moved the component set, as long as the origin file still exists.

1. Restore deleted variants from any instances. This will restore those variants as main components in the origin file.
2. Publish these restored components to the library in the origin file—you can only move published components.
3. Move the restored components to the destination file using the [cut and paste method](#cut-paste).
4. Drag any restored component into the existing component set.

## 2. Cut and paste components

You can now move **published components** and component sets between files and their libraries using cut and paste. You can choose to keep any existing connections between components and instances, or treat them as entirely new components.

You can paste main components into a branch of a file. Figma won't update the libraries and any subscribed files until the branch is merged and the library published.

To move a component or component set:

1. Open the file where the main component lives, this is the **origin** file.
2. Select the main components or component sets you want to move.
3. Use the cut shortcut to add them to your clipboard:
   - Mac: `⌘ Command` - `X`
   - Windows: `Ctrl` + `X`
4. Open the file and you want to move components to, this is the **destination** file.
5. Make sure you have nothing selected, then paste components into the file.
   - Mac: `⌘ Command` - `V`
   - Windows: `Ctrl` + `V`

**Note:** It's possible to make changes to the components before publishing. We recommend publishing the library first, before making any structural changes to components and variants.

## 3. Publish library changes

When you move published components between files, Figma will prompt you to publish your changes to any affected libraries. When changes have been made to a library, the  **Libraries** icon in the left sidebar will display a blue badge.

You need to publish these changes to complete the move process. Figma will push updates to all subscribed files when you publish your changes.

1. Click the  **Review unpublished changes** icon to open the **Libraries** modal.  The icon’s tooltip may read **Review library updates** if there are updates to libraries you are using in the file.
2. Select the **This file** tab then click **Publish** next to the library.
3. Figma lists any changes to the library, including every component you've moved to this file. For each component, choose to **Move to this file** or **Publish as a copy**.

   1. Select **Move to this file** for all moved components. This makes sure Figma keeps connections between the main components and any existing instances.
   2. Select **Publish as copy** to publish them as new main component. This will break the connection between the component and any instances, instances won't receive further updates.![Publish library dialog showing option to move components to a file or publish as a copy, highlighting update choices.](https://help.figma.com/hc/article_attachments/26974914319767)
4. Add a description of your changes, Figma shows this in the file's version history.
5. Click **Publish** to publish your changes to the library.

[Learn how to publish updates to a library.](https://help.figma.com/hc/en-us/articles/360025508373#updates)

## 4. Accept updates from library

Figma will push updates to any file that uses those styles and components. When updates are available for a style, component, or variable on the current page, the  **Libraries** icon in the left sidebar will display a blue badge.

![Sidebar showing Figma pages: Metadata and instructions, Images, Playground, Archive.](https://help.figma.com/hc/article_attachments/26974914323991)

[Learn about reviewing and accepting updates from libraries.](https://help.figma.com/hc/en-us/articles/360039234193)

Instances will stay linked to deleted components in the origin file until you review and accept updates. Accept updates in subscribed files to update instances.

**Subscribed files**

If you select or edit an instance before receiving updates, this will still point to the deleted main component in the origin file. Once you receive updates from the library, Figma will point to the main component in the destination file.

**Instances in the origin file**

Instances of the moved component in the origin file won't receive updates until those components are published in the destination file.

Click **Update** to receive updates and make sure those instances are now linked to components in their new location.

**Instances in destination file**

If instances in the destination file are linked to components you've moved from the original file, Figma will automatically update them to point to the newly moved components. ![Notification tooltip indicating moved components with options to review or dismiss updates.](https://help.figma.com/hc/article_attachments/4406443468951)

**Note:** If the new library isn't enabled in a subscribed file, Figma will enable the library in that file when instances receive updates.

## Reverse or undo move component

It's not possible to undo the action of moving components using any of these methods:

- Using the undo keyboard shortcut
- Restoring deleted components from an instance![Warning against restoring components in the origin file after they have been moved, highlighting irreversibility in process.](https://help.figma.com/hc/article_attachments/4406473246871)
- Restoring an earlier version of the file's version history

While you can still take these actions in a file, this won't return components to their original location and you may end up with other unintended consequences.

We recommend using the [move component process outlined above](#cut-paste) to move components back to their original location.