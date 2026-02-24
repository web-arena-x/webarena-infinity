# Creating and managing automations for time-based events

Source: https://support.zendesk.com/hc/en-us/articles/4408883801626-Creating-and-managing-automations-for-time-based-events

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Objects and rules > Business rules >
Automations

Automations are similar to triggers because both define conditions and actions that modify ticket properties and optionally send email notifications to customers and the support staff.
Where they differ is that automations execute when a time event occurs after a ticket property was set or updated, rather than immediately after a ticket is created or updated.

Administrators can create, edit, and manage default and custom automations.

Topics covered in this article:

- [Creating automations](#topic_adj_pzy_tb)
- [Editing and cloning automations](#topic_rsh_miv_ub)
- [Reordering your automations](#topic_agt_ojv_ub)
- [Deleting and deactivating automations](#topic_wsq_xjv_ub)

More information:

- [About automations and how they work](https://support.zendesk.com/hc/en-us/articles/4408832701850)
- [About the standard Support automations](https://support.zendesk.com/hc/en-us/articles/4408835051546)
- [Automation conditions and actions reference](https://support.zendesk.com/hc/en-us/articles/4408885654298)

Tip: To learn more about setting up automations, check out the [On demand: Automations](https://training.zendesk.com/on-demand-automations) training video.

## Creating automations

Administrators can create automations from scratch, as shown here, or create copies of existing automations to modify and use (see [Editing and cloning automations](#topic_rsh_miv_ub)).

Before creating automations, review the [Essential facts for automations](https://support.zendesk.com/hc/en-us/articles/4408832701850#topic_ft5_n3z_sm). You can have up to 500 active automations at a time. Each automation must be less than 65kb.

**To add an automation**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Automations**.
2. Select **Add Automation**.
3. Enter a title for your automation.
4. Add the conditions and actions for your automation (see [Automation conditions and actions reference](automation-conditions-and-actions-reference.md)).

   An automation is made up of three parts:

   - Conditions to be met for the automation to run
   - Actions to perform when the conditions are met
   - At least one of the following: one action that cancels a condition after the conditions are met or a condition than can only be true once (see [Ensuring your automation only runs once](https://support.zendesk.com/hc/en-us/articles/4408832701850#topic_mbl_q4f_tm))
5. Test your automation by clicking **Preview match for the conditions** to preview tickets that match the conditions you specified.

   This lists the tickets that match the conditions you specified. The automation will have no effect on any closed ticket listed in your preview. For more information, see [Understanding when automations run](https://support.zendesk.com/hc/en-us/articles/4408832701850#topic_h3z_svn_fm).
6. Save your new automation by clicking **Create automation**.

## Editing and cloning automations

You can edit and clone automations. Cloning an automation creates a copy that you can modify and use for some other purpose.

**To edit an automation**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Automations**.
2. Locate the automation you want to edit.
3. Hover your mouse over the automation to display the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)), then click the icon and select **Edit** from the options menu.
4. Modify the title, conditions, and actions as needed.
5. Select **Update** and **Submit** your changes.

You can create a copy of an existing automation to use as the basis of a new automation.

**To clone an automation**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Automations**.
2. Locate the automation you want to clone.
3. Hover your mouse over the automation to display the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)), then click the icon and select **Clone** from the options menu.
4. Enter a new name for your automation and modify the conditions and actions as needed.
   Note that all active automations can have some overlapping conditions, but they can't be identical.
5. Click **Create automation**.

## Reordering your automations

You can reorder your automations, but keep in mind that the order of your automations is important because all automations run (first to last) every hour. Actions in one automation may affect the actions in another.

**To reorder the list of automations**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Automations**.
2. Open the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png) ) at the top of the list of active automations, then click **Reorder page**.
3. Click and drag automations to new locations as needed.
4. Click **Save**.

## Deleting and deactivating automations

If you decide that you no longer need an automation you can either delete it or deactivate it. Deleting it of course means that it’s gone and can’t be retrieved. You can instead deactivate automations. Deactivated automations are listed in a separate table on the **Automations** page and can be reactivated if needed.

**To delete an automation**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Automations**.
2. Locate the automation you want to delete.
3. Hover your mouse over the automation to display the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)), then click the icon and select **Edit** from the options menu.
4. Choose **Delete** from the actions menu at the bottom of the page, then click **Submit**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/automation_action-menu.png)

**To deactivate/activate an automation**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Automations**.
2. Locate the automation you want to deactivate.
3. Hover your mouse over the automation to display the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)), then click the icon and select **Deactivate** from the options menu.

   The automation is deactivated and displayed in the list of inactive automations.
4. To reactivate the automation, select it from the list of inactive automations and select **Activate** from the options menu.