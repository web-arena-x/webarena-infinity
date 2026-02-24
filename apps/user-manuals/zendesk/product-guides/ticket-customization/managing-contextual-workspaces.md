# Managing contextual workspaces

Source: https://support.zendesk.com/hc/en-us/articles/4408822138522-Managing-contextual-workspaces

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Location: Admin Center > Workspaces > Agent tools > Contextual workspaces

Workspaces optimize your support workflow, without restricting the tools agents need to complete their jobs. With workspaces, you can simplify the forms and macros that agents see when they first open a ticket, and you can expand, collapse, or reorder apps. To manage contextual workspaces, you can view and edit existing workspaces or change the run order. You can also delete or deactivate workspaces.

This article contains the following topics:

- [Viewing contextual workspaces](#topic_ts4_3xm_w2b)
- [Editing and duplicating contextual workspaces](#topic_t4b_vwm_w2b)
- [Changing the contextual workspace run order](#topic_odf_2tv_5fb)
- [Deleting and deactivating contextual workspaces](#topic_ogq_31n_w2b)

Administrators, advisors, and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can manage contextual workspaces. To create a new workspace, see [Setting up contextual workspaces](https://support.zendesk.com/hc/en-us/articles/4408833498906--Update-Setting-up-contextual-workspaces-Enterprise-).

## Viewing contextual workspaces

**To view workspaces**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Contextual workspaces**.

 This page includes a list of Active and Inactive workspaces defined for your account. You can have up to 500 active workspaces in your account.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual_workspaces_list_acf.png)

 Note: If you have [custom layouts](https://support.zendesk.com/hc/en-us/articles/5447690090138) activated on your account, you’ll see a column that shows the layout assigned to each contextual workspace. If you don't have custom layouts, the standard layout is applied by default.

## Editing and duplicating contextual workspaces

You can edit and duplicate workspaces. Duplicating (cloning) a workspace creates a copy that you can modify and use for some other purpose.

**To edit an existing workspace**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Contextual workspaces**.
2. Click the title of the workspace you want to change. The workspace edit page opens.
3. Update the information as needed. See [Setting up contextual workspaces](https://support.zendesk.com/hc/en-us/articles/4408833498906--Update-Setting-up-contextual-workspaces-Enterprise-) for information on the fields on this page.
4. **Save** your changes.

   You can save the workspace as **Active** or **Inactive**.

**To clone (duplicate) a workspace**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Contextual workspaces**.
2. Locate the workspace you want to clone.
3. Hover your mouse over the workspace to display the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)).
4. Open the menu and select **Clone**.
5. Modify the name, description, and settings as needed.
6. **Save** your changes.

   You can save the workspace as **Active** or **Inactive**.

## Changing the contextual workspace run order

Similar to [SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866-Defining-and-using-SLA-policies-Professional-and-Enterprise-#topic_pz5_zzv_rr), it's possible to create logically overlapping workspaces, but at any given time a single ticket can have only one workspace applied. When you have multiple workspaces that match a ticket, Zendesk uses the order of the workspace to break any ties. To make sure the correct workspace is applied, change your workspace run order so that workspaces with the most-specific (restrictive) conditions are run first.

For example, you might have one **International Purchases** workspace that includes macros for international purchases and another **Singapore Purchases** workspace that includes all the macros for international purchases and an additional macro that is required for Singapore purchases. Set the workspace run order so that the **Singapore Purchases** workspace runs first. Otherwise, the **International Purchases** workspace will be incorrectly applied to tickets for Singapore purchases.

**To change the workspace run order**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Contextual workspaces**.
2. Click **Edit order**.

   An Edit order list of workspaces appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual_workspaces_edit_order_acf.png)

   An **Edit order** list of workspaces appears. You can change how workspaces with similar conditions are prioritized.
3. To change the run order, click the grabber at the end of a workspace and drag it to a new location within the list.
4. Continue to reorder workspaces as needed.
5. **Save** your changes.

## Deleting and deactivating contextual workspaces

If you decide that you no longer need a workspace, you can either delete it or deactivate it. Deleting a workspace means that it's gone and can't be retrieved. Instead of deleting a workspace, you can change it from active to inactive. Inactive workspaces can be reactivated if needed.

Tip: You can use the **Filter** at the top of the page to show only active or inactive workspaces.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contextual_workspaces_active_inactive_acf.png)

Without the default **Active** filter, both active and inactive workspaces are listed on the Contextual workspaces page.

Note: When you delete or deactivate a workspace, the ticket forms, macros, and apps are no longer applied to tickets associated with that workspace.

**To deactivate/activate a workspace**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Contextual workspaces**.
2. Locate the workspace you want to deactivate.
3. Hover your mouse over the workspace to display the Options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Deactivate**. The workspace changes from active to inactive.
4. To reactivate the workspace, select it from the list of inactive workspaces and select **Activate**. When you reactivate a workspace, it does not retroactively work on past tickets. Also, when you deactivate a workspace then reactivate it, it does not go back to it’s previous position in the run order. You have to reset it.

**To delete a workspace**

To permanently delete a workspace, you must first deactivate it as described above. Once the workspace is inactive, you can delete it.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Contextual workspaces**.
2. Locate the inactive workspace you want to delete.
3. Hover your mouse over the workspace to display the Options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Delete**.