# Creating sales triggers

Source: https://support.zendesk.com/hc/en-us/articles/4418343631002-Creating-sales-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

Admins can use sales triggers in Sell to automate specific parts of the
workflow of every sales rep. This means that when an event you specified occurs, and the
conditions you configured are met, then an action that you defined is carried out. For
example, you can automate the workflow of all sales reps so that every time a trigger
event (such as a deal being updated) occurs in Sell, and meets its pre-defined
conditions (such as, “Deal value is greater than 1000”), then Sell automatically
attempts to carry out the actions defined for that trigger, for example “Update Deal
Owner to Valerie Golden”.

You must be an admin to create triggers. However, all Sell users can cause a
trigger event that prompts the evaluation of conditions and carries out the predefined
action if the trigger conditions are met.

This article covers the following topics:

- [Building condition statements for
  sales triggers](#topic_t4b_rk5_msb)
  - [Using 'and' 'or'
    operators](#topic_ils_rk5_msb)
  - [Using a nullifying
    condition](#topic_cbn_4c5_4sb)
- [Building action statements for
  sales triggers](#topic_xq2_sk5_msb)

Related articles:

- [Editing, deactivating, and deleting sales
  triggers in Sell](https://support.zendesk.com/hc/en-us/articles/4423402721818)
- [Popular recipes for sales
  triggers](https://support.zendesk.com/hc/en-us/articles/4422774699930)

## Building condition statements for sales triggers

You can define conditions to specify when trigger actions are implemented
after a trigger event occurs. Every time it occurs, the sales triggers that use it
will evaluate their conditions against the object that caused the trigger event.
Trigger actions are carried out every time a trigger event occurs and the trigger
conditions are met.

To avoid repetitive triggers, if trigger A, for example, carries out actions on
object B, then object B causes a trigger event and the trigger A conditions are met,
you want to ensure that the actions will not be carried out again and again.

The following sample recipe avoids this sort of problem. The Sales Trigger
conditions assign any deal that is updated to a worth of 1,000 or more in value to
be assigned to the sales rep in New York, Valerie Golden.

**When**

Deal is updated

**If**

`Deal Value` is greater than `1000`

AND

`Deal State` is `New York`

**Then**

Update `Deal Owner` to `Valerie Golden`

Note: Currently, the only trigger condition available is "Deal is updated".

**To create a trigger**

1. On the Sell sidebar, click **Settings** > **Business rules** >
   **Triggers**.
2. On the **Triggers** page, click **Add trigger**.
3. In the **Name** field, name your trigger (for example `Deal owner
   updated`).
4. Select the **Set as active** checkbox if you want this trigger to be
   active.
5. Under **When**, click the event that will cause the trigger (for example,
   `Deal is updated`).
6. Under **If**, click **+Add condition**.
7. Enter information about the trigger in the following fields:
   - **Object**: Deal is the only object currently supported.
   - **Field**: choose the type of field you want the object to refer
     to (for example, `Value`).
   - **Operator**: choose from the dropdown menu that relates to the
     field you've chosen (for example, `Is greater
     than`).
   - **Value**: enter the value that relates to your choice from the
     Field menu (for example `Greater than 1000`)
8. Click **Add**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_triggers_create.png)

### Using 'and' 'or' operators

After you've added the first condition, an AND operator appears beneath
it. The operator determines the relationship between conditions for the logic
behind the trigger. You can set it to AND or change it to OR.

AND - use this operator if you have two or more conditions that must be
met for the trigger evaluation to succeed. You can also use the AND operator to
connect conditions across clauses.

OR - use this operator when you have two or more conditions in a
clause, but only one of the conditions must be met for the trigger to be
successful.

Note: Changing the AND or OR operator between conditions changes it between all
of the conditions in the clause.

The following example, uses a set of conditions that evaluate to true
in two independent scenarios:

- First scenario: Requires only one condition to be met: if the
  `Deal Value` is greater than `1000`.
- Second scenario: If three conditions are met: the `Deal
  Country` is the `USA`, the `Deal
  Source` is a `Tradeshow`, and the
  `Deal primary contact` is `VIP
  Company`.

If

`Deal.Value` is greater than `1000`

OR

(`Deal.Country` is `USA` AND
`Deal.Source` is `Tradeshow` AND `Deal
primary contact` is `VIP Company`)

### Using a nullifying condition

Sometimes the logic for a trigger requires a nullifying condition, for
example, to prevent a trigger from looping. As the following scenario shows, a
nullifying condition will prevent your trigger from performing further actions
if that condition has already been met.

**Scenario: a looping trigger**

In this scenario, the logic for an ownership trigger assigns
`Deal.Owner` to `Distribution` >
`Distribution` assigns a user from its pool as a new
`Deal.Owner` > The result is that the deal is updated.
This triggers a new trigger event, causing the trigger to run again on the same
object, assigning another owner from the Distribution pool, and repeating the
cycle again, and again.

**To prevent a looping trigger**

Add a nullifying condition that allows the trigger to run only once on
a given object. For example,

IF

`Deal.Owner` is not `Distribution`

Adding this condition means a distribution will act on a deal only when
the conditions are met. When the trigger acts again on the deal, it will check
if the deal owner belongs to that distribution. If that’s true, then the
condition IF `Deal.Owner` is not `Distribution`
will be met, causing the evaluation logic of the trigger to be false and
preventing the trigger from repeating the same action over and over again.

## Building action statements for sales triggers

After setting the trigger event and conditions, you can determine the
actions that will happen if the trigger evaluation is successful.

Actions perform on objects that are the subject of the trigger event and
have met the trigger conditions that you specified for it.

You select which fields of an object you want to add values for, or update.
For example selecting the `Owner` field and “Valerie Golden” as the
value will cause the owner of the deal to change to Valerie Golden every time a
trigger event happens and the conditions are met to incur that action.

**To create the action for the trigger**

1. Under **Then**, click **Add action**.
2. Under **Update**, in the **Object to update** field, choose an object from
   the dropdown menu (Deal is currently the only supported object).
3. Under **Update field values**, enter information about the actions that the
   trigger will set into motion:
   - **Field to update**: choose from the dropdown menu (for example
     `Owner` or `Value`).
   - **Value**: available on the **Field to update** menu, choose from
     the Value dropdown menu the value that relates to your choice (for
     example, the name of the person you want the deal to be owned by).
4. Add as many relevant fields and values as is necessary for your trigger (up to
   200). When you are finished, click **Add**.
5. Click **Save**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_triggers_conditions_actions_owner_update.png)