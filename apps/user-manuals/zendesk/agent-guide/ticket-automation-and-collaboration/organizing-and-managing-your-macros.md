# Organizing and managing your macros

Source: https://support.zendesk.com/hc/en-us/articles/4408884166554-Organizing-and-managing-your-macros

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Most support teams create and use lots of macros. As your list of macros grows, you may find it difficult to quickly locate macros when you’re trying to apply one to a ticket. You can remedy this by organizing and sorting your macros using a number of different techniques.

This article discusses the following topics related to organizing and managing macros:

- [Accessing the Macros page](#topic_dgn_12j_mw)
- [Browsing and searching the macros list](#topic_ldp_cyj_mw)
- [Editing, cloning, deactivating, and deleting macros](#topic_mtv_gmx_tb)
- [Categorizing macros](#topic_dpr_k1j_mw)
- [Sorting the list of macros](#id_box_qtk_kd)
- [Reordering macros manually](#topic_dgr_jhv_zbc)
- [Turning off the most-used macros option](#topic_jf5_2cc_dx)

Related articles:

- [Using macros to update tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602)
- [Creating macros for tickets](https://support.zendesk.com/hc/en-us/articles/4408844187034)
- [Building macro action statements](https://support.zendesk.com/hc/en-us/articles/4408832783642)
- [Creating macros from existing tickets](https://support.zendesk.com/hc/en-us/articles/4408886850586)
- [Creating macros from macro suggestions for admins](https://support.zendesk.com/hc/en-us/articles/5217191091354)

## Accessing the Macros page

All of your available macros can be managed through the Macros page.

**To access the Macros page**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Macros**.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_consolidated_settings.png)

On the **Macros** tab, you can browse, categorize, sort, reorder, and filter your macros. Read on for more information.

On the **Suggestions** tab, you can create and manage macro suggestions for admins. See [Creating macros from macro suggestions for admins](https://support.zendesk.com/hc/en-us/articles/5217191091354) for more information.

## Browsing and searching the macros list

Macros are divided by activation status. The default view on the Macros page is the list of **Active** macros. You can view macros that have been deactivated by clearing the **Active** filter. For more information on activation status, see [Editing, cloning, deactivating, and deleting macros](#topic_mtv_gmx_tb).

By default, macros are listed in alphabetical order. If you have a large number of macros, the list will be paginated. You can scroll through the pages using the controls at the bottom of the page.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/pagination.png)

If you know the name, or partial name, of the macro you want to view, you can enter it into the search box at the top of the page.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_consolidated_settings_search.png)

All macros containing the search term appear in the list.

Click **Clear search** to return to the full list.

## Editing, cloning, deactivating, and deleting macros

You can edit, clone, deactivate, or delete a macro by selecting the checkbox next to its name.

![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/macros_consolidated_settings_checkbox.png)

- **Edit** allows you to modify the title, actions, and permissions used.
- **Clone** creates a copy that you can modify and repurpose.
- **Deactivate** removes the macro from the Active macros list, and moves it onto the Inactive macros list, making it unavailable to Agents. Deactivated macros can be activated if needed.
- **Delete** permanently removes the macro. Only deactivated macros can be deleted. Deleted macros cannot be recovered.

Agents can only use these actions on their personal macros. Administrators can use them on their personal macros and all shared macros.

Additionally, admins can view and clone agents' personal macros. For example, admins may want to clone an agent's personal macro so that it can be created as a shared macro for all agents to use.

Note: The options menu also includes controls for changing the macro's position in the list. This functionality is covered in [Reordering macros manually](#topic_dgr_jhv_zbc).

**To edit a macro**

1. On the Macros page, locate the macro you want to edit.
2. Select the checkbox next to the macro's name.
3. In the action bar at the bottom of the list, click **Edit**.
4. Modify the title and actions as needed.
5. Click **Save**.

**To clone a macro**

1. On the Macros page, locate the macro you want to clone.
2. Select the checkbox next to the macro's name.
3. In the action bar at the bottom of the list, click **Clone**.
4. Enter a new title for your macro and modify the actions as needed.
5. Click **Create**.

**To deactivate a macro**

1. On the Macros page, locate the macro you want to deactivate.
2. Select the checkbox next to the macro's name.
3. In the action bar at the bottom of the list, click **Deactivate**. The macro's status is updated to Inactive.

   Note: You cannot deactivate macros that include unavailable values in the action statements. Attempting to deactivate the macro will fail, and the macro will remain in the Active macros list, marked with a red exclamation point.

**To activate a deactivated macro**

1. On the Macros page, clear the **Active** filter to include inactive macros in the list.
2. Select the checkbox next to the macro's name.
3. In the action bar at the bottom of the list, click **Deactivate**. The macro's status is updated to Active.

**To delete a macro**

1. On the Macros page, clear the **Active** filter to include inactive macros in the list. If the macro is currently active, use the instructions above to deactivate it.
2. Select the checkbox next to the macro's name.
3. In the action bar at the bottom of the list, click **Delete**. The macro is permanently deleted.

## Categorizing macros

Sorting your macros into categories can make locating a specific macro, or type of macro, much simpler. Categorizing allows agents to quickly [apply macros](https://support.zendesk.com/hc/en-us/articles/4408887656602#topic_kda_eew_uf) when working with a ticket, and gives you an option for [filtering macros](#topic_n5c_blj_mw) on the Macros management page.

You categorize macros by including the categories in your macro titles and separating them with two colons (::), as in this example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macro_name_entry.png)

**To create nested macro categories**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Macros**.
2. Click **Add Macro**.
3. Create a macro title that contains the top level category and subcategories you want to use followed by the macro name, each separated by two colon symbols as shown here:

   **Assign to::me::question**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macro_nested_title.png)

   The macro title in this example indicates that you’re assigning the ticket to yourself and setting the Type property to Question. The top level category is 'Assign to' and the subcategory is 'me'. The macro name is 'question'. You can use any category and title naming structure that you prefer.
4. Create any other macros that you want to include in this category structure or modify the titles of existing macros to follow the same pattern.

To organize your macros, you can create as many top level catgories and subcategories as you need.

## Filtering the list of macros

You can filter the displayed macros based on status, who they're available for, and category.

**To filter the list of macros**

1. At the top of the macros table, click the **Filter** button.
2. In the **Filter** pane that appears, select any of the following filtering options:
   - **Status**: Includes **Active** and **Inactive**
   - **Available for**: Includes the following options:
     - **All shared macros**: Macros that are shared, either to the whole account or to one or more groups
     - **All agents**: Macros available to all agents (No group-only macros)
     - **You**: Macros available only to you
     - **Individual agents**: Personal macros owned by all other agents (Visible to admins only)
     - **Group**: Macros available only to agents in the group specified
   - **Categories**: Includes any [categories you've created](#topic_dpr_k1j_mw)
3. Click **Apply filters**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_consolidated_settings_pane.png)

To clear your filters and return to the full list of macros, click **Clear filters** at the top of the macros list.

## Sorting the list of macros

The Macros page includes options for viewing and sorting your macros. You can sort macros by name, creation date, and date last updated. If you're on a Suite Growth or Support Professional plan or higher, you can also sort by usage. The total number of macros in the view appears above the list of macros.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_consolidated_settings_columns.png)

**To sort your list of macros**

- On the Macros page, click the column header you want to sort by.

The first click sorts in ascending alphabetical (A–Z) or chronological (oldest to newest) order. You can click the column header again to reverse the sort order.

You can sort by only one column at a time.

## Reordering macros manually

If you turn on the manual ordering setting, you can reorder your macros by dragging and dropping them in the list on the Macros page.

If the order of your macros isn't essential to your workflow, however, we recommend disabling manual order mode so all newly created macros will snap into place without manual intervention.

**To turn on manual reordering**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Macros**.
2. Click **Actions** > **Manage settings**.
3. Select **Turn on manual ordering**.
4. Click **Save**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_macros_manage_settings_manual_ordering.png)

**To reorder macros manually**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Macros**.
2. Click **Actions** > **Edit order**.
3. Click and hold the drag-and-drop handle for the macro you want to move. Drag the macro into position and release the handle. Repeat as needed to reorder your macros list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_macros_manual_reordering_drag_drop.png)
4. Click **Save**.

## Turning off the most-used macros option

By default, the three most-used macros from the past week are displayed at the top of the macros list. You can turn off this feature if it doesn't fit into your workflow.

**To disable the most-used macros option**

1. On the Macros page, click **Actions** > **Manage settings**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_consolidated_settings_manage.png)
2. On the Manage settings page, deselect **Display agents' most-used macros**.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/macros_consolidated_settings_most_used.png)
3. Click **Save**.