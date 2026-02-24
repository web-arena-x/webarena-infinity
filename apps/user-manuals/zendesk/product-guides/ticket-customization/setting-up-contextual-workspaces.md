# Setting up contextual workspaces

Source: https://support.zendesk.com/hc/en-us/articles/4408833498906-Setting-up-contextual-workspaces

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Location:  Admin Center > Workspaces > Agent tools >
Contextual workspaces

Contextual workspaces enable you to present ticket tools and features based on specific
workflows. For example, your company might have a specific workflow to use when a customer
makes a return or when they have a billing issue. This article describes how to create a
contextual workspace and define the conditions that will launch the workspace.

This article contains the following topics:

- [About contextual workspaces](#topic_l1z_tvt_w2b)
- [Activating contextual workspaces](#topic_ryq_tzl_bcc)
- [Creating a contextual workspace](#topic_e3m_l5n_wcb)
- [Setting workspace conditions](#topic_xcq_sgt_w2b)
- [About the agent experience](#topic_wrs_ztv_bgb)

For information on how to manage contextual workspaces, see [Managing contextual workspaces](https://support.zendesk.com/hc/en-us/articles/4408822138522--Update-Managing-contextual-workspaces-Enterprise-).

## About contextual workspaces

Contextual workspaces optimize your support workflow, without restricting the tools agents need
to complete their jobs. With contextual workspaces, you can simplify the forms and
relevant macros that agents see when they first open a ticket, and you can expand,
collapse, or reorder apps. You can also create a [custom layout](https://support.zendesk.com/hc/en-us/articles/5447690090138) and assign it to a contextual workspace,
giving agents the ideal ticket interface to do their jobs, based on the criteria you
specify.

The set of contextual workspaces you define can be as simple or as detailed as you need. For
example, you could have a single workspace that defines the ticket form and tools
your Customer Support team uses, or you could define a full set of workspaces for
your Fulfillment Center based on different types of international shipping
locations, product types, and currencies.

Contextual workspaces are for recommendations, not restrictions. Agents can still search for
other macros that are available to them, apply other forms, or use other apps if
desired.

## Activating contextual workspaces

To get started with contextual workspaces

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Contextual
   workspaces**.

   You’ll see a Welcome page with a description of contextual workspaces.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual_workspaces_welcome_acf.png)
2. Click **Get started.**

   When you’re ready to start adding contextual workspaces, follow the instructions in
   [Creating a contextual workspace](#topic_e3m_l5n_wcb).

## Creating a contextual workspace

You create new contextual workspaces, and edit existing ones, from the Contextual
workspaces page. You can create up to 500 active workspaces for an account and include up to
10 conditions per
workspace.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual_workspaces_list_acf.png)

Note: Agents who have a [custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882) with permission to **Manage contextual
workspaces**, may not have permission to access all tabs when creating a contextual
workspace. For example, only admins can access the Apps tab.

**To create a contextual workspace**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Contextual
   workspaces**.
2. Click **Create Workspace**. A new workspace builder opens. The builder includes five
   tabs: Details, Layout, Ticket form, Macros, Knowledge, and Apps.
3. On the Details tab, enter a **Title** and **Description** for the workspace, then
   enter the conditions that will launch the workspace.

   For more information, see [Setting workspace conditions](#topic_xcq_sgt_w2b).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual_workspaces_details_acf.png)
4. On the Layout tab, select a layout to apply to the workspace. You can apply one layout
   to a contextual workspace. If you don’t assign a layout, the default ticket layout is
   used.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual_workspaces_layout_acf.png)

   Note: If you
   [change the default layout](https://support.zendesk.com/hc/en-us/articles/5447837810714#topic_dl4_nmp_qwb) on the Layouts page,
   the new default is automatically applied to any contextual workspaces that reference the
   default.
5. On the Ticket Form tab, use the **Active form** drop-down to select a predefined
   ticket form to associate with the workspace.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual_workspaces_forms_acf.png)

   You can begin
   typing the name of the form to filter the displayed list, or you can scroll through the
   list to locate the form you need. When you select a form, a read-only list of ticket
   fields appears.

   If you do not want to apply a ticket form, select **No
   change** from the menu.
6. On the Macros tab, select one or more macros to associate with the workspace.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual_workspaces_macros_acf.png)

   To select
   macros, you can begin typing the name of the macro to locate potential matches, filter
   the list by **Categories** or **Permissions**, or scroll through the list to
   locate the macro you need. Only shared macros are available when creating a
   workspace.

   If your macros are sorted into categories, you can click the category
   name to drill down the list.
7. On the Knowledge tab, add default filters to help agents find the content they need when
   using this workspace.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual_workspaces_knowledge2_acf.png)

   Settings
   include:

   - **Brand**: Choose the brands you want to include as default search
     filters.
   - **Language**: Choose the languages you want to include as default
     search filters.
   - **External source**: Choose the external source to show by default.
     This is content that is external to your help center, but that can be configured to
     appear in your help center's search results. External source options are available
     only when [federated search is configured](https://support.zendesk.com/hc/en-us/articles/4593564000410).
   - **Article placement**: For articles that are published in multiple locations,
     select the category or section of the article to show by default.

   Default search filters for **Brand** and **Language** are automatically
   applied to agent search queries unless they are manually changed or removed by agents.
   Configuring the filters that agents use the most reduces the time they spend customizing
   default search filters before searching for content. For example:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual_workspaces_knowledge_filters_acf.png)

   If you want
   to:
   - Remove the selected filters, click **X** to remove the filters displayed in the
     Default filters list.
   - Add new filters, use the drop-down menu to select the filters that you want to
     add.

     You can click the **>** icon to display the filters grouped under a
     filter type (for example, Brand or Language). Select up to five filters within
     each filter type that you want to use as default search filters.

   Note: To change knowledge section settings that are not part of this workspace,
   see [Configuring the knowledge section in the context
   panel](https://support.zendesk.com/hc/en-us/articles/7263163614874).
8. On the Apps tab, select one or more apps to expand in the Apps panel. Only apps in the
   ticket sidebar can be set in contextual workspaces.

   Note: If you’re using
   contextual workspaces with [custom layouts](https://support.zendesk.com/hc/en-us/articles/5447690090138), Zendesk recommends configuring apps as part of
   a layout (instead of using this Apps tab) to get the best experience for your
   agents.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual_workspaces_apps2_acf.png)

   You can begin
   typing the name of the app to filter the displayed list, or you can scroll through the
   list to locate the app you need.

   To change the order that apps appear in tickets,
   click the grabber at the end of an app and drag it to a new location. Alternatively, you
   can click the double up or down arrows next to the app to move it one location at a
   time. The apps order you set here takes priority over the order you set for tickets on
   the [My apps](https://support.zendesk.com/hc/en-us/articles/4409155972378#topic_tc5_qn4_ym) page.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual_workspaces_apps_handles2_acf.png)

   Agents can
   manually click the header of any app to expand or minimize it. The apps you select to
   **Expand by default** will be expanded for all tickets viewed in the workspace.
9. Click **Save and activate**. You are returned to the Workspace edit page, and the new
   workspace is added to the list.

## Setting workspace conditions

On the Details tab, you can set the conditions that launch the workspace. Each workspace
can include up to 10 conditions. For instance, in the example below, any *High*
priority ticket sent to the *VIP Triage* group will have the contextual workspace
applied.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual_workspaces_conditions_acf.png)

Note: Workspace conditions are very similar to [Trigger conditions](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_i3y_fkz_1cb), but with a subset of choices.
To see a list of supported conditions, open the drop-down menu.

**To add workspace conditions**

1. On the Details tab, click the **Add condition** button under one of these two
   categories: Meet ANY of the following conditions, Meet ALL of the following
   conditions.
   - If you add conditions under **Meet ALL of the following conditions**, all of
     the conditions must be true for the workspace to apply.
   - If you add conditions under **Meet ANY of the following conditions**, one or
     more of the conditions must be true for the workspace to apply.
2. Select a condition from the **Conditions** drop-down list.
3. Select a field operator.

   A *field operator*  determines the relationship
   between your condition and its value. For example, if you select the field operator
   **Is**, your condition must be equal to the value. Different conditions contain
   different field operators.
4. Select a value. Each condition contains a unique value.
5. Continue to add as many **ANY** and **ALL** conditions as needed to create the
   correct logic for the workspace.

   Zendesk recommends keeping your conditions simple so
   they are easier to troubleshoot and maintain. If you include conflicting conditions,
   an error message appears.

## About the agent experience

After the workspace is activated and the conditions are met, agents will see ticket
features that match the workspace definition. For example, when a US customer returns a
camera, the ticket might look like this:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cw_agent_view_annotated.png)

When agents click **Apply macros**, they will see a list of **Relevant macros** as
defined by the contextual workspace. They can click the return arrow (**<**) in the
**Relevant macros** heading to view and use all macros available for the ticket.

| Relevant macros (as defined by the workspace) | All macros |
| --- | --- |
|  |  |

Note: When the workspace is activated on a [closed ticket](https://support.zendesk.com/hc/en-us/articles/7335734335258), macros are unavailable, forms are read only, but
the layouts, apps and knowledge settings still apply.