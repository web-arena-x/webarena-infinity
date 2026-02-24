# Viewing and managing custom layouts

Source: https://support.zendesk.com/hc/en-us/articles/5447837810714-Viewing-and-managing-custom-layouts

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

Location: Admin Center > Workspaces > Agent tools > Layouts

Enterprise plans can have multiple layouts active at the same time for different types of tickets. Professional plans can have only one active layout. See [Plan requirements for custom layouts](https://support.zendesk.com/hc/en-us/articles/5447690090138#topic_bt5_nq1_4bc).

Ticket layouts control the look and feel of the ticket interface. Admins can create multiple layouts and apply them to different types of tickets. See [About custom layouts](https://support.zendesk.com/hc/en-us/articles/5447690090138) for more information. This article describes how you can view and manage custom layouts.

This article contains the following sections:

- [Viewing custom layouts](#topic_eyp_5rl_znb)
- [Editing layouts](#topic_rsb_zlp_qwb)
- [Setting the default layout](#topic_dl4_nmp_qwb)
- [Deactivating and deleting layouts](#topic_fnn_dpp_qwb)
- [Assigning a layout to a contextual workspace](#topic_gxp_dyx_txb)

**Related articles**

- [About custom layouts with layout builder](https://support.zendesk.com/hc/en-us/articles/5447690090138)
- [Creating custom layouts to improve agent workflow](https://support.zendesk.com/hc/en-us/articles/5447837546138)
- [Best practices for creating custom layouts](https://support.zendesk.com/hc/en-us/articles/6259543948442)

## Viewing custom layouts

You can have up to 20 custom layouts in your account.

**To view custom layouts**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Layouts**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_layouts_list2.png)

   This page displays a list of layouts defined for your account. The list includes a standard layout for your account and any additional custom layouts that have been [created](https://support.zendesk.com/hc/en-us/articles/5447837546138).

   The **Default** tag next to a layout shows which layout is currently [set as the default](#topic_dl4_nmp_qwb) for your account. A lock icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/builder_lock_icon.png)) next to a layout indicates the layout can't be edited.

   From the list you can see and sort by the following information for each layout:

   - **Name**: The name of the layout.
   - **Description**: A brief description of the layout.
   - **Updated**: Date the layout was last updated.
   - **Contextual workspaces** (Enterprise only): The number of contextual workspaces that use the layout.

   Tip: Click a number in the **Contextual workspaces** column to see a list of workspaces that use the layout. Click a contextual workspace name to open it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual_workspaces_using_layout.png)

## Editing layouts

You can't edit the standard layout, but you can edit any other layout in the list. When you edit a layout, the changes apply to all tickets that use the layout. You’ll see the changes when you open or refresh a ticket.

**To edit a layout**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Layouts**.

   A list of layouts appears.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) next to the layout you want to edit, then select **Edit** from the options menu.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_layouts_edit_reduced.png)

   The layout opens in layout builder.
3. Click **Customize layout**, then update the layout as needed.

   Alternatively, you can click a layout in the list. When the layout opens, click **Customize layout**.

   See [Creating custom layouts](https://support.zendesk.com/hc/en-us/articles/5447837546138) for details about the types of changes you can make to a layout. You can add or remove components in the layout. You can also move and resize components, or make changes to the context panel.
4. When you’ve finished making layout changes, click **Save**.

## Setting the default layout

Zendesk provides a [standard ticket layout](https://support.zendesk.com/hc/en-us/articles/5447690090138#topic_eyp_5rl_znb) that is automatically treated as the default layout and applied to any ticket. You can replace this standard layout by creating a custom layout, then setting it as the default. While only one layout can be set as the global default, on Enterprise plans you can associate any active layout with one or more contextual workspaces.

**To set the default layout**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Layouts**.

   A list of layouts appears.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) next to the layout you want to make the default, then select **Edit**.

   The layout opens for editing.
3. Click **Set as default layout**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_layout_set_default_on.png)

   If you change the default layout, the new default is automatically applied to any [contextual workspaces](https://support.zendesk.com/hc/en-us/articles/440883349890) that reference the default.

Note: When you first create a ticket, the [standard ticket layout](https://support.zendesk.com/hc/en-us/articles/5447690090138#topic_eyp_5rl_znb) is used no matter what default layout or contextual workspace is configured for the ticket. You need to submit and reopen the ticket before you see a custom layout applied.

## Deactivating and deleting layouts

If you decide that you no longer need a layout, you can either "deactivate" it or delete it. You can deactivate a layout by making sure the layout is not set to be the default layout; and, on Enterprise plans, removing it from any contextual workspaces that were using the layout. Deactivated layouts remain in your list of layouts and can be reactivated if needed. Deleting a layout means that it's gone and can't be retrieved.

**To deactivate a layout**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Layouts**.
2. Locate the layout you want to deactivate.
3. If the layout you want to deactivate was the default layout, [pick another layout to use as the default](#topic_dl4_nmp_qwb).
4. (Enterprise only) Make sure no contextual workspaces are assigned to the layout. If so, assign another layout to the workspace. See [Assigning a layout to a contextual workspace](#topic_gxp_dyx_txb).

   A deactivated layout remains in the layout list but it's not assigned to any contextual workspaces. You can reactivate it anytime by making it the default or assigning it to a contextual workspace.

**To delete a layout**

To permanently delete a layout, first make sure the layout is not being used as the default layout.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Layouts**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) next to the layout you want to edit, then select **Delete** from the options menu.
3. Click **Delete** to confirm the deletion.

   The layout is deleted and removed from the layout list.

   For Enterprise plans only:

   If the layout is being used in a contextual workspace, you’ll receive a warning message before the layout is deleted.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_layout_delete_warning.png)

   When you delete a layout that’s being used in a contextual workspace, the workspace will revert to the layout that’s set as the active default.

   If the layout you’re deleting is a custom layout that you’re using as the active default, the contextual workspace will revert to the Zendesk standard layout.

## Assigning a layout to a contextual workspace

Note: You must have an Enterprise plan to use the features described in this section.

You can assign any layout to one or more contextual workspaces. This enables the workspace and the layout to work in conjunction to make sure your agents see the right ticket layouts at the right times. When you create or edit a contextual workspace, use the Layouts tab in the workspace editor to assign a custom layout. See [Setting up contextual workspaces](https://support.zendesk.com/hc/en-us/articles/4408833498906).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_layouts_cw_layouts_tab.png)