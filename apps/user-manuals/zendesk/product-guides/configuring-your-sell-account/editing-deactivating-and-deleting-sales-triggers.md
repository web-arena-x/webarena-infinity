# Editing, deactivating, and deleting sales triggers

Source: https://support.zendesk.com/hc/en-us/articles/4423402721818-Editing-deactivating-and-deleting-sales-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

Note: This feature is currently in a closed beta and is only available to select customers.

You can save sales triggers as active or inactive. By default, new sales triggers are saved as inactive.

An active sales trigger evaluates the conditions you've assigned to it each time a trigger event happens, then it tries to carry out the specified actions. You can deactivate an active trigger when you no longer want it to perform the actions that you specified for it (for example, if the trigger is for a seasonal campaign).

This article covers the following topics:

- [Editing the conditions of a sales trigger](#topic_zkl_mvh_psb)
- [Deactivating sales triggers](#topic_ent_mvh_psb)
- [Deleting sales triggers](#topic_frb_nvh_psb)

Related articles:

- [Creating sales triggers](https://support.zendesk.com/hc/en-us/articles/4418343631002)
- [Popular recipes for sales triggers](https://support.zendesk.com/hc/en-us/articles/4422774699930)

## Editing the condition of a sales trigger

You can define more conditions for your sales trigger by using logical expressions.
The trigger evaluates the logical expression against the object that caused the trigger event immediately after the trigger event happens. If the evaluation is successful (true), the trigger attempts to carry out the actions that you specified for it. If it’s unsuccessful (false) nothing happens.

Conditions are comprised of three fundamental components:

- **Object.Field** — this is the subject of a condition that refers to the object of a condition and its associated field. For example a subject such as a `Deal` refers to an object field, for example the monetary `Value` of the deal reaching a certain amount.
- **Operator** — this key determines the relationship between a condition's subject and its value (for example, `Is greater than`).
- **Value** — the reference data the trigger uses to evaluate a given condition.

### Editing or deleting conditions

You can edit the conditions of a trigger at any point and if a specific condition is no longer necessary, you can delete it from the trigger.

**To edit or delete a condition or nested condition**

1. Click the **Options** menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) next to the condition or nested condition.
2. Click either **Edit** or **Delete** as appropriate.

![Sell triggers, edit or delete a condition](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_triggers_conditions_edit_delete.png)

### Adding extra conditions

You can add up to 200 conditions for a trigger, although it is best practice to not over complicate a trigger with too many conditions. Be sure the conditions do not conflict with each other and try to keep them simple and logical.

**To add another condition**

1. In **Settings** > **Business rules** > **Triggers**, click the trigger you want to edit.
2. Under **When**, click (**+**) to open the dropdown menu, then click **Add condition** to configure an extra condition.

   ![Sell add a nested condition](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_triggers_condition_nested_add.png)
3. Enter the details for that condition, then click **Add** to save it.
4. Click **Save** to save the updated trigger.

### Adding nested conditions

Nested conditions are essentially a set of conditions in parentheses (a clause)
that are evaluated together, which allows you to create more advanced logical expressions. You can create up to two levels of nested conditions.

**To add a nested condition**

1. In **Settings** > **Business rules** > **Triggers**, click the trigger you want to edit.
2. Under **When**, click (**+**) to open the dropdown menu, then click **Add nested condition**.

   ![Sell triggers create nested condition](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_triggers_condition_nested_create.png)
3. Enter the extra qualifying details for that condition, then click **Add** to save it.
4. Click **Save** to save the updated trigger.

   ![Sell triggers nested condition](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_triggers_conditions_nested_and_or.png)

## Deactivating sales triggers

An inactive trigger does nothing. You can always activate inactive triggers again if you want them to start operating.

**To deactivate a trigger**

1. Click the **Options** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) menu next to the trigger you want to make inactive.
2. Click **Deactivate**.

## Deleting sales triggers

If you want to delete a trigger completely, it must be inactive as you cannot delete active triggers.

**To delete a trigger**

1. First, deactivate the trigger (see above).
2. Click the **Inactive** tab, then click the **Options** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) menu next to the trigger you want to delete.
3. Click **Delete**.

   ![Sell delete a trigger](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_triggers_delete.png)