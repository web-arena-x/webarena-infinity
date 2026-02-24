# Managing object triggers

Source: https://support.zendesk.com/hc/en-us/articles/7313294079130-Managing-object-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Admin Center > Objects and rules > Business rules >
Triggers

After you [create](https://support.zendesk.com/hc/en-us/articles/7313293890970) an [object trigger](https://support.zendesk.com/hc/en-us/articles/7313350767514), you might need to change its order or
otherwise modify it.

This article contains the following topics:

- [Ordering object triggers](#topic_fph_dpb_fzb)
- [Editing object triggers](#topic_w3n_vlb_fzb)
- [Cloning object triggers](#topic_fhz_l4b_fzb)
- [Activating and deactivating object triggers](#topic_fdp_xlb_fzb)
- [Deleting object triggers](#topic_hzm_gmb_fzb)
- [Viewing an object trigger's revision history](#topic_npx_hct_mbc)

## Ordering object triggers

The Object triggers list is organized by object. Each object that has at least one
trigger is ordered alphabetically, with the object's triggers below it. Whenever a
record is created or updated for an object with triggers, the object triggers are
all evaluated and then all actions happen at once. That means the first object
trigger's actions can't influence whether the record satisfies the conditions for
subsequent object triggers in the list.

Object triggers can be reordered, but only relative to other triggers for that same
object. Object triggers can't be moved or reordered across objects.

**To reorder object triggers**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Objects** tab at the top of the page.
3. Click **Edit order**.
4. Select the **Trigger object** for which you'd like to reorder the
   triggers.
5. Drag and drop the triggers into the desired order.
6. Click **Save**.

## Editing object triggers

Everything except the trigger object value can be edited after an object trigger is
created.

**To edit an object trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Objects** tab.
3. Click the name of the object trigger you want to edit.
4. Modify the name, description, [conditions](https://support.zendesk.com/hc/en-us/articles/7313293784218#topic_ey3_bbb_fzb), and [actions](https://support.zendesk.com/hc/en-us/articles/7313293784218#topic_rzv_bbb_fzb) as needed.
5. Click **Save**.

## Cloning object triggers

Sometimes you want to create a new trigger that is *almost* identical to an
existing trigger, but adjusted slightly. In this case, you can clone the existing
trigger.

**To clone an object trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Objects** tab.
3. Click the name of the object trigger you want to clone.
4. Click **Actions** and select **Clone**.

   A copy of the trigger is opened
   to edit.
5. Adjust the cloned object trigger as needed, then click **Create** and set the
   trigger to **Active** or **Inactive**.

## Activating and deactivating object triggers

When you create an object trigger, you can decide whether to save it as active or
inactive. After it's activated, you may decide you no longer need the trigger. In
that case, you can either delete it or deactivate it. [Deleting](#topic_hzm_gmb_fzb) a trigger means that
it's gone and can't be retrieved. If you may want to use a trigger again in the
future but don't currently need it, you can deactivate it. Deactivated triggers are
found by selecting **Inactive** from the **Status** drop-down at the top of
the trigger list, and can be reactivated if needed. If you reactivate a trigger, it
won't retroactively run on object records that were previously created or
updated.

**To deactivate an object trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Objects** tab.
3. Click the name of the object trigger you want to deactivate.
4. Click **Actions** and select **Deactivate**.
5. In the confirmation dialog, click **Deactivate**.

**To deactivate multiple object triggers at once**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Objects** tab.
3. Check the box next to each trigger you want to deactivate and then click
   **Deactivate** at the bottom of the page.
4. In the confirmation dialog, click **Deactivate**.

**To activate an object trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Objects** tab.
3. Click the name of the object trigger you want to deactivate.
4. Click **Actions** and select **Activate**.

**To activate multiple object triggers at once**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Objects** tab.
3. Check the box next to each trigger you want to activate and then click
   **Activate** at the bottom of the page.

## Deleting object triggers

If you decide that you no longer need a trigger, you can either delete it or
deactivate it. Deleting a trigger means that it's gone and can't be retrieved. If
you decide to permanently delete a trigger, you must first [deactivate](#topic_fdp_xlb_fzb) it.

Note: If you delete a custom object, all of the object triggers for that object are also
deleted, regardless of whether they're active or inactive.

**To delete an object trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Objects** tab.
3. Filter the list to view **Inactive** object triggers.
4. Find the object trigger you want to delete, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_trigger_options.png)) and select **Delete**.

   If you're already
   viewing an inactive object trigger, click **Actions** and select
   **Delete**.
5. In the confirmation dialog, click **Delete trigger**.

**To delete multiple object triggers at once**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Objects** tab.
3. Filter the list to view **Inactive** object triggers.
4. Check the box next to each trigger you want to delete and then click
   **Delete** at the bottom of the page.
5. In the confirmation dialog, click **Delete**.

## Viewing an object trigger's revision history

Changes you make to an object trigger can be viewed in the trigger revision history.
The revision history displays:

- The currently-viewed version's configuration
- Who made the changes
- When the change was made
- The change made to the trigger in the displayed revision (optional)

Note: Updating the order of your object triggers isn't reflected as a change in
the revision history. It is, however, reflected in the last updated
timestamp.

An object trigger's revision history is visible to anyone with permission to manage
business rules.

**To view an object trigger's revision history**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Objects** tab.
3. Click the name of the object trigger you want to view, then click
   **Revision history** below the trigger title.
4. On the trigger history page, you'll see all the available versions in a
   panel on the right. Click the version you want to view.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_rev_history_view.png)
5. From here, you can:
   - Toggle to show or hide the changes made to the selected version
   - View the read-only configuration of the selected version
   - Click another version to view
   - Return to the edit page