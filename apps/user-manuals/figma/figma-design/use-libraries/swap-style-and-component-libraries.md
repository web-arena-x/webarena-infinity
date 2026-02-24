# Swap style and component libraries

Source: https://help.figma.com/hc/en-us/articles/4404856784663-Swap-style-and-component-libraries

---

Who can use this feature

Available on [paid plans](https://help.figma.com/hc/en-us/articles/360040328273-Choose-a-Figma-Plan)

Only people with `can edit` access to the file, and at least `can view` access to affected libraries

Swap libraries lets you ‌quickly update instances in a file so they use components from another library. Use swap library to:

- Use a different or newer version of a library
- Swap to external or agency-provided libraries
- Manage instances from missing or unpublished libraries

Note: Library swap currently supports swapping components and styles, but not variables. However, if you swap a component or style out for an asset that contains variables applied to it, the variable will remain attached to the asset. You can also head to the [Figma Community](https://www.figma.com/community) to find plugins that allow you to swap variables between libraries.

![An animation showing button components being swapped between different libraries with varied styles and colors.](https://help.figma.com/hc/article_attachments/4406220597911)

## How does swap library work?

Swap library lets you replace styles and component instances in a current file with those of another published library. You can swap any library you have at least `can view` access to.

Swap library only works if the assets you want to replace originate from a different library. In other words, you cannot replace assets that live in the same file as their main source by swapping them with another library.

When swapping, Figma looks for any styles and components in the selected library with matching names. This includes components sets and the variants within them.

If you've deleted components, or recreated them with different names, Figma won't recognize or match these components.

### Unmatched assets

If a matching style or component isn't found in the selected library, Figma won't swap those assets and they'll remain connected to the original library.

You can choose to ignore these styles and instances, delete them from the file, or manually swap instances using the **Instance menu**. [Swap between component instances →](https://help.figma.com/hc/en-us/articles/360039150413)

### Swap or override styles

The **Swap default styles in instances** setting allows you to control how styles are applied to instances and whether they'll be treated as overrides.

- **Checked**: Figma applies matching styles to instances as overrides. If you swap the instance via swap libraries, the applied matching styles will be preserved.
- **Unchecked**: Figma applies matching styles to instances as normal. If you swap the instance via swap libraries, the applied matching styles will not be preserved.

If you're swapping to an updated version of a library or replacing a missing library, you'll likely have both styles and components available for swap. If you want to swap only the instances and continue using the styles defined on the main components, leave this setting unchecked.

The swapped instances will continue to receive updates from their main components and any changes you applied to them via swap libraries will be overwritten.

Regardless of whether this box is checked, Figma will preserve any overrides—which aren’t related to swapped styles—applied to instances. [Learn more about override preservation →](https://help.figma.com/hc/en-us/articles/360039150733#Preserve_overrides)

## Swap between libraries

Swap styles and components in the current file with instances from another library. This replaces instances with matching instances from another library.

Before you swap, make sure:

- The current file you're working from contains at least one instance or style that you wish to swap, and the asset is from a different library.
- Both libraries involved in the swap (the library being replaced and the soon-to-be-used library) are published to team libraries.
- Any assets you wish to swap have matching names.

To swap between libraries:

1. Select the **Assets** tab in the left sidebar.
2. Click the  **Library** icon to open the **Libraries** modal.  The icon’s tooltip may read **Review library updates** if there are updates to libraries you are using in the file, or **Review unpublished changes** if you have unpublished updates in your file.
3. Select **This file** and locate the library you want to replace.
4. Select the library and click **Swap library** at the bottom of the modal.![](https://help.figma.com/hc/article_attachments/27999055994135)
5. From the **Choose library** dropdown, find a select a replacement library.
   - View libraries available to the entire organization
   - Explore published libraries by team![](https://help.figma.com/hc/article_attachments/27999055999767)
6. Figma looks for any styles and components with a matching name. Use the checkboxes on the left to choose which assets to swap.
   - If a matching style or component is found, the box next to the asset is checked and you'll see a preview in the selected library.
   - If no matching styles or components are found, the box is unchecked and you'll see a **None found** message.
   - If there are incorrect or undesired matches, use the checkbox to remove the asset from the swap.
7. Decide whether to apply matched styles as overrides using the [swap default styles in instances](#overrides) setting.
   - Check to apply matched styles as overrides.
   - Leave unchecked to swap instances and use the default styles defined on the main components. Figma will preserve any supported overrides you've applied (default).
8. Click **Swap library** to replace assets with assets from your selected library.

## Manage missing libraries

Styles and instances can be disconnected from their library when the original file is unpublished, deprecated, or moved to a team you can't access.

Use the library modal to view styles and instances in the current file that aren't connected to an active library. Then use **Swap library** to replace any instances in the current file with instances from another library.

Figma matches styles and components by name only. It's not possible to manually select a new style or component, or match it to an asset with a slightly different name. Figma won't swap any styles and components without a match. You can also deselect any matched assets you don't want to swap.

### Swap missing libraries

Before you swap to replace a missing library, make sure:

- The current file you're working from contains at least one instance or style that you wish to swap, and the asset is from a different library.
- The replacement library is published to team libraries.
- Any assets you wish to swap have matching names.

1. Select the **Assets** tab in the left sidebar.
2. Click the  **Library** icon to open the **Libraries** modal.  The icon’s tooltip may read **Review library updates** if there are updates to libraries you are using in the file, or **Review unpublished changes** if you have unpublished updates in your file.
3. From **This file**, scroll down and click **View missing libraries** at the bottom of the modal. ![](https://help.figma.com/hc/article_attachments/27999040350231)
4. If there is more than one missing library, styles and components are grouped by their origin library along with details of the number of missing assets. Select a library to view the affected styles and components.![](https://help.figma.com/hc/article_attachments/27999056004375)
5. Use the **Choose library** dropdown to find and select a replacement library.
   - View libraries available to the entire organization
   - Explore published libraries by team![](https://help.figma.com/hc/article_attachments/27999040356887)
6. Figma looks for any styles and components with a matching name. Use the checkboxes on the left to choose which assets to swap.   
   - If a matching style or component is found, the box next to the asset is checked and you'll see a preview in the selected library.
   - If no matching styles or components are found, the box is unchecked and you'll see a **None found** message.
   - If there are incorrect or undesired matches, use the checkbox to remove the asset from the swap.
7. Decide whether to apply match styles as overrides using the [Swap default styles in instances ↑](#overrides) setting.
   - Check to apply matched styles as overrides.
   - Leave unchecked to swap instances and use styles defined on the main components. Figma will preserve any supported overrides you've applied (default).
8. Click **Swap library** to replace affected instances with instances from your selected library.

## Undo swap library

You have a few options for reversing your changes:

- If you're still working in the same session, undo the previous action by pressing `⌘ Command` `Z` / `⌃ Control` `Z`.
- Swap the library back using the same method described above.
- Restore a previous version of the library to a version before the swap.

If you checked "**Swap default styles in instances**" when swapping libraries, you can reset overrides to revert to the previous library. [Learn how to reset overrides.](https://help.figma.com/hc/en-us/articles/360039150733#Reset_overrides)