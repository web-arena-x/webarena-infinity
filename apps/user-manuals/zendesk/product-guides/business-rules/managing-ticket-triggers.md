# Managing ticket triggers

Source: https://support.zendesk.com/hc/en-us/articles/4408882237722-Managing-ticket-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article discusses the following topics related to managing your ticket triggers:

- [Editing and cloning ticket triggers](#topic_dwq_zoy_tb)
- [Reordering triggers](#topic_vnl_zpy_tb)
- [Searching for ticket triggers](#topic_xxv_2kz_pbc)
- [Sorting the list of triggers](#topic_zxc_hjd_dx)
- [Deactivating ticket triggers](#topic_jvv_kqy_tb)
- [Deleting ticket triggers](#topic_fqc_2m2_zsb)
- [Activating ticket triggers](#topic_vcz_cfy_2lb)
- [Viewing the trigger revision history](#topic_syw_z14_lbb)

Related articles:

- [Creating triggers for ticket updates and notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466)
- [Creating ticket trigger categories](https://support.zendesk.com/hc/en-us/articles/4408834781594)
- [Managing ticket trigger categories](https://support.zendesk.com/hc/en-us/articles/4408832263066)

## Editing and cloning ticket triggers

You can edit and clone ticket triggers. Cloning a ticket trigger creates a copy that you can modify and use for some other purpose. If your ticket trigger notifies users, the notification body text will reset if you change the notification destination.

**To edit a ticket trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. Click the **Tickets** tab.
3. Click the name of the trigger you want to edit.
4. Modify the name, description, conditions, and actions as needed.
5. When you are finished, click **Save**.

**To clone a ticket trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. Click the **Tickets** tab.
3. Click the name of the trigger you want to clone.
4. At the top of the page, click **Actions** and select **Clone**.

   A copy of the trigger is created and automatically opened for editing.
5. Modify the name, conditions, and actions of the new trigger as needed.
6. Click **Save**.

## Reordering triggers

You can reorder your list of ticket triggers to designate the order they're fired in. Ticket trigger order is important. Remember that all of your active ticket triggers run each time a ticket is created or updated and actions in one ticket trigger can affect the actions in another. See [Understanding when triggers run and fire](https://support.zendesk.com/hc/en-us/articles/4408822236058#h_15524764971513292862138).

As a best practice the following order is recommended for your ticket triggers:

1. **Changes or updates to ticket values.** Any triggers that change ticket values, such as status, priority, or any other field value, should be listed first. These triggers can impact ticket assignments and notifications.
2. **Ticket assignments.** Triggers that assign tickets to groups or individual agents should be listed after triggers that update any other value on the ticket.
3. **Notifications.** Triggers that send notifications to users or targets should be listed last. This is because you want the system to make any necessary changes before you send out email notifications.

You can use trigger categories to reorder multiple ticket triggers at the same time. See [Reordering trigger categories](https://support.zendesk.com/hc/en-us/articles/4408832263066#topic_avl_ksn_tnb) and [Organizing ticket triggers within categories](https://support.zendesk.com/hc/en-us/articles/4408834781594#topic_cdk_m1n_tnb).

Updating the order of your ticket triggers is not reflected as a change in the revision history. It is, however, reflected in the trigger's last updated timestamp.

**To reorder ticket triggers using drag-and-drop**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. Click the **Tickets** tab.
3. Click **Edit order** in the upper right.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/triggers_edit_order_button.png)

   You'll see a list of ticket triggers in the default sort order.
4. Select the ticket triggers you want to move.
5. Click and hold the drag-and-drop handle (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/drag_and_drop_handle.png)) for the ticket triggers you want to move.
6. Drag the triggers into position and release the handle. Repeat as needed to reorder your ticket triggers list.
7. Click **Save**.

Note: If you receive a "Trigger order wasn't updated" error message when you reorder your triggers, see [Trigger order wasn't updated](https://support.zendesk.com/hc/en-us/articles/4408881509914).One reason you may see this error message is if the trigger references any invalid fields or values.

## Searching for ticket triggers

Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) to manage business rules can search for ticket triggers and filter the list based on a number of factors. You can define a simple filter based on a single criteria such as name, description, condition, or action, or you can create advanced filters based on multiple filters.

For more information, see [Searching triggers](https://support.zendesk.com/hc/en-us/articles/4408838286106).

## Sorting the list of triggers

By default, ticket triggers are sorted by position (the order in which they fire). You can change the sort order by clicking the column headings that appear on the triggers page. You can sort based on a number of properties, including:

- Name
- Last updated
- Date created
- Triggered (last 1 hour, last 24 hours, last 7 days, or last 30 days).

Sorting your ticket triggers doesn't affect the order your triggers run and fire in. If you want to select a new order to fire your ticket triggers, follow the steps in [Reordering triggers](#topic_vnl_zpy_tb).

**To sort your ticket triggers**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. Click the **Tickets** tab.
3. Click the column heading you want to use to sort your ticket triggers.

   The triggers are reorganized based on that property.
4. Click the column heading again to change from ascending to descending order.
5. Click the column heading a third time to return to the default sort order.
6. To return to the default sort order, click the **Undo sort** button.
7. You can increase your sorting options by changing some of the column headings that appear in the list. At the top of the ticket triggers list, click the columns icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/show_columns_icon.png)) and then select and deselect columns as needed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/triggers_show_columns4_tm.png)

## Deactivating ticket triggers

If you decide that you no longer need a ticket trigger, you can either delete it or deactivate it. Deleting a trigger means that it's gone and can't be retrieved. If you may want to use a trigger again in the future but don't currently need it, you can deactivate it. Deactivated triggers are found by selecting **Inactive** from the **Status** drop-down at the top of the ticket trigger list, and can be reactivated if needed. If you reactivate a ticket trigger, it won't retroactively run on past tickets.

You can use ticket trigger categories to delete multiple triggers at the same time. See [Deleting ticket trigger categories](https://support.zendesk.com/hc/en-us/articles/4408832263066#topic_df5_y5n_tnb).

**To deactivate a ticket trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. Click the **Tickets** tab and locate the trigger you want to deactivate.
3. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_trigger_options.png)) and select **Deactivate**.

   The trigger’s status is changed to Inactive.

**To deactivate multiple ticket triggers at once**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. Click the **Tickets** tab.
3. Check the box next to each ticket trigger you want to deactivate and then click **Deactivate** at the bottom of the page.
4. In the confirmation dialog, click **Deactivate**.

## Deleting ticket triggers

If you decide that you no longer need a trigger, you can either delete it or deactivate it. Deleting a trigger means that it's gone and can't be retrieved. Triggers must be deactivated before they can be deleted.

**To delete a trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. Click the **Tickets** tab.
3. If the trigger you want to delete is still active, follow the steps to [deactivate the trigger](#topic_jvv_kqy_tb).
4. In the **Status** drop-down at the top of the triggers list, select **Inactive**.
5. Next to the trigger you want to delete, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_trigger_options.png)) and select **Delete**.

   If necessary, click the expander (>) next to a category to show triggers within a category.
6. In the confirmation dialog, click **Delete trigger**.

Note: If you accidentally delete your [standard triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346), you can quickly rebuild them. For more information, see [About the standard Support triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346).

**To delete multiple ticket triggers at once**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. Click the **Tickets** tab.
3. Select **Inactive** from the **Status** drop-down at the top of the trigger list.
4. Check the box next to each trigger you want to deactivate and then click **Delete** at the bottom of the page.
5. Click **Delete** in the confirmation dialog.

## Activating ticket triggers

Usually, new triggers are activated automatically. However, you can choose to create them as inactive triggers and then activate them at a later time. Additionally, there are some cases when you might need to [deactivate](#topic_jvv_kqy_tb) and then reactivate a trigger.

**To activate a trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. Click the **Tickets** tab.
3. In the **Status** drop-down at the top of the triggers list, select **Inactive**.
4. Next to the trigger you want to activate, click the options menu icon (![Trigger options menu](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_trigger_options.png)) and select **Activate**.

   If necessary, click the expander (>) next to a category to show triggers within a category.

**To activate multiple ticket triggers at once**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. Click the **Tickets** tab.
3. In the **Status** drop-down at the top of the triggers list, select **Inactive**.
4. Check the box next to each trigger you want to activate and then click **Activate** at the bottom of the page.

## Viewing the ticket trigger revision history

If you're on an Enterprise plan, changes you make to a ticket trigger can be viewed in the **trigger revision history**.

The revision history displays:

- The currently-viewed version's configuration
- Who made the changes
- When the change was made
- The changes made to the trigger in the displayed revision (optional)

Note: Updating the order of your triggers is not reflected as a change in the revision history. It is, however, reflected in the last updated timestamp.

The history is available to anyone with permission to manage business rules.

**To view the ticket trigger revision history**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. Click the **Tickets** tab.
3. Click the trigger you want to view, then click **Revision history**, located below the trigger title.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_rev_history_link.png)

   This opens the ticket trigger history page.
4. On the trigger history page, you’ll see all the available versions in a sidebar. Click the version you want to view.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_rev_history_view.png)
5. From here, you can:
   - Toggle to show or hide the changes made to the selected version
   - View the read-only configuration of the selected version
   - Click another version to view
   - Return to the edit page

For more information, see the [viewing a ticket trigger's revision history](http://fast.wistia.com/embed/iframe/rqy6x5i5rc) video.