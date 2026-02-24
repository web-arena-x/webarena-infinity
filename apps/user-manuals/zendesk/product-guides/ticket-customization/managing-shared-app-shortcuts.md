# Managing shared app shortcuts

Source: https://support.zendesk.com/hc/en-us/articles/6866142556954-Managing-shared-app-shortcuts

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

Location: Admin Center > Workspaces > Agent tools > Layouts

Admins can create app shortcuts as part of a custom ticket layout and share them with agents. You must have a Professional plan or above with [the Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) to create custom layouts and share app shortcuts.

This article includes:

- [About app shortcuts](#topic_sk4_3j5_51c)
- [Creating shared app shortcuts](#topic_crz_lk5_51c)
- [Editing shared app shortcuts](#topic_kc4_mz5_51c)
- [Reordering shared app shortcuts](#topic_ahg_sbv_51c)
- [Setting a shared app to open by default](#topic_h5h_vwf_bbc)
- [Removing shared app shortcuts](#topic_hqj_tbv_51c)

**Related articles**

- [Managing your installed apps](https://support.zendesk.com/hc/en-us/articles/4409155972378)
- [Managing personal app shortcuts](https://support.zendesk.com/hc/en-us/articles/6066877041690)

## About app shortcuts

The [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362) in the Zendesk Agent Workspace includes an Apps panel (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_apps.png)) that shows the apps agents can use to solve tickets. However, if you have a lot of [apps installed](https://support.zendesk.com/hc/en-us/articles/4409155972378), it can be time-consuming for agents to scroll through the list of apps in the panel and find the ones they need at the moment.

Here are some options to help agents find apps quickly:

- Using [custom layouts](https://support.zendesk.com/hc/en-us/articles/5447690090138), admins can create shortcuts for individual apps and pin them to the context panel. Any agent working on a ticket with that layout can see and use these *shared app shortcuts,* wherever that custom layout is applied. See [Creating shared app shortcuts](#topic_crz_lk5_51c).
- If [activated by an admin](../apps-and-the-zendesk-marketplace/managing-your-installed-apps.md#topic_nc4_t2c_4yb), agents can also create their own *personal app shortcuts* and pin them to the context panel. These app shortcuts are available to the agent who created them, but other agents cannot see or use them. See [Managing personal app shortcuts](https://support.zendesk.com/hc/en-us/articles/6066877041690).
- Using [custom layouts](https://support.zendesk.com/hc/en-us/articles/5447690090138), admins can add apps to the main ticket layout. Any agent working on tickets with that layout will see these apps in the ticket interface. See [Adding and removing components in a layout](creating-custom-layouts-to-improve-agent-workflow.md#topic_tb4_tcv_qwb).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shared_app_shortcuts_all_composite.png)

Agents can use shared app shortcuts added by an admin along with any personal app shortcuts they added themselves, if personal app shortcuts are enabled by their admins.

### How personal and shared app shortcuts interact

Here are some guidelines for how shared app shortcuts added by admins interact with personal app shortcuts added by agents.

- Agents who have personal app shortcuts enabled will see a horizontal separator line that delineates shared apps shortcuts pinned by an admin vs. the personal app shortcuts the agent pinned for themselves.
- Shared app shortcuts added by admins in a ticket layout take priority over personal app shortcuts added by agents.
 - If an admin has pinned an app as a shared app shortcut in the ticket layout, agents can’t pin that same app as a personal app shortcut.
 - Agents cannot pin an app that is already included in the main ticket layout.

## Creating shared app shortcuts

Admins can add app shortcuts to a custom layout and share them with agents. You share app shortcuts by pinning them to the context panel. You must be an admin on a Professional plan or above with custom layouts enabled to add app shortcuts.

Admins can configure the context panel to contain a maximum of 15 components (system components and app shortcuts). This maximum does not impact the number of personal apps agents can pin.

**To create shared app shortcuts**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Layouts**.

   A list of layouts appears.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shared_app_options_menu_icon.png)) next to the layout you want to edit, then select **Edit** from the menu.

   The layout opens in layout builder.
3. Click **Customize layout** to make changes to your layout.
4. In the component area of the layout, select the app you want to add as a shortcut and drag it to the context panel in the main ticket layout.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/app_drag_to_panel2.png)

   A shortcut for the app appears in the context panel.

   You can also move an app from the main ticket layout to the context panel and vice versa.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/app_move_to_panel_from_main_layout.png)
5. Continue to drag apps as needed to pin them to the context panel.
6. **Save** your changes.

   The app shortcuts you added to the context panel appear in the custom ticket layout. Agents who use this ticket layout can use these shortcuts to open apps.

After you’ve finished adding app shortcuts to the context panel, you [edit](#topic_kc4_mz5_51c) the shared app shortcuts to make changes, including [reordering](#topic_ahg_sbv_51c) and [removing](#topic_hqj_tbv_51c) shortcuts.

## Editing shared app shortcuts

You can change the shared app shortcuts as needed in a layout.

**To edit shared app shortcuts**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Layouts**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shared_app_options_menu_icon.png)) next to the layout you want to edit, then select **Edit** from the menu.
3. In the Components area of the layout builder, click **Manage context panel**.

   Layout details for the context panel appear, including the shared app shortcuts that are already pinned to the panel.
4. Update your shared app shortcuts as needed. You can:
   - [Create new shared app shortcuts](#topic_crz_lk5_51c).
   - [Reorder shared app shortcuts](#topic_ahg_sbv_51c).
   - [Setting a shared app to open by default](#topic_h5h_vwf_bbc)
   - [Remove shared app shortcuts](#topic_hqj_tbv_51c).
5. **Save** your changes.

## Reordering shared app shortcuts

You can change the order of how app shortcuts appear in the context panel.

**To reorder shared app shortcuts**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Layouts**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shared_app_options_menu_icon.png)) next to the layout you want to edit, then select **Edit** from the menu.
3. In the Components area of the layout builder, click **Manage context panel**.

   Layout details for the context panel appear, including the shared app shortcuts that are already pinned to the panel.
4. Hold your mouse over the grabber at the end of the app shortcut you want to reorder, then drag the app shortcut to another position within the component list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shared_app_shortcuts_reorder_content_panel.png)
5. Continue to reorder as desired.

   Along with the app shortcuts, you can reorder any component in the context panel, including the system components such as User, Knowledge, Side conversations, and Apps.
6. **Save** your changes.

Note: You can also use a keyboard to reorder app shortcuts in the context panel. Use the Tab key to select a shared app shortcut, then press the up or down arrow on the keyboard to move it.

## Setting a shared app to open by default

For shared apps you add to the context panel, you can choose to have one of the apps open by default.

**To make a shared app open by default**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Layouts**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shared_app_options_menu_icon.png)) next to the layout you want to edit, then select **Edit** from the menu.
3. In the Components area of the layout builder, click **Manage context panel**.

   Layout details for the context panel appear, including the shared app shortcuts that are already pinned to the panel.
4. Open the **Default selection** menu and select the shared app you want to open by default in the context panel.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shared_app_shortcuts_open_default.png)

   You can choose any one of the components in the context panel to open by default. This includes shared apps and the system components such as User, Knowledge, Side conversations, and Apps.
5. **Save** your changes.

   When agents work on tickets with this layout, they will see the shared app you selected open by default in the context panel.

Note: You can set the **Default selection** to **None** if you don’t want any system components or shared apps to open by default.

## Removing shared app shortcuts

You can remove shared app shortcuts from the context panel. You can remove the app shortcut completely. You can also move the app shortcut out of the context panel and add the app to the main ticket layout. Removing a shared app shortcut unpins it from the context panel. It doesn’t uninstall the app itself.

**To remove shared app shortcuts**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Layouts**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shared_app_options_menu_icon.png)) next to the layout you want to edit, then select **Edit** from the menu.
3. In the Components area of the layout builder, click **Manage context panel**.

   Layout details for the context panel appear, including the shared app shortcuts that are already pinned to the panel.
4. To completely remove an app shortcut, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shared_app_options_menu_icon.png)) next to the app shortcut and select **Remove component**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shared_app_shortcuts_remove.png)

   You can also select **Move to main layout** to move the app into the main ticket layout.
5. **Save** your changes.