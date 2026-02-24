# Object trigger conditions and actions reference

Source: https://support.zendesk.com/hc/en-us/articles/7313293784218-Object-trigger-conditions-and-actions-reference

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

All Zendesk triggers are based on the same structure of conditions and actions. The types
of conditions and actions available vary by trigger type and, in the case of object
triggers, by the custom objects themselves. This article describes the different
conditions and actions you can use when creating an object trigger.

This article contains the following topics:

- [Building object trigger condition statements](#topic_ey3_bbb_fzb)
- [Building object trigger action statements](#topic_rzv_bbb_fzb)

Related articles:

- [Understanding object triggers](https://support.zendesk.com/hc/en-us/articles/6294230624410)
- [Creating object triggers](https://support.zendesk.com/hc/en-us/articles/7313293890970)
- [Managing object triggers](https://support.zendesk.com/hc/en-us/articles/7313294079130)

## Building object trigger condition statements

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/object_trigger_conditions.png)

Condition statements are essentially "if" statements that are evaluated to determine
whether the specified criteria is met. In a trigger, you can define two sets of
conditions: *all* and *any*. When conditions are specified under **Meet
ALL of the following conditions**, the custom object record must meet all of
these conditions to be considered a match. Alternatively, a custom object record is
considered a match if it meets at least one of the conditions specified under
**Meet ANY of the following conditions**.

Condition statements are composed of a **Category**, an **Operator**, and a
**Value**. For triggers based on standard objects, such as tickets, there's a
predefined list of conditions available. That isn't possible for custom objects
because all of the custom object's properties are defined with custom fields.
Instead, a predefined list of operators is supported for each type of custom field.
**Current user** and **Update** conditions are available in addition to
the conditions based on the custom object's fields.

The following conditions:

| Field type | Operators | Values |
| --- | --- | --- |
| **Object** (available options vary based on the fields defined for the object) | | |
| Object: Checkbox | is | Select *True* or *False*. |
| Object: Current user | is, is not | Select from agent roles and users. |
| Object: Date | is, is not, present, not present, before, before or on, after, after or on | Select a date. |
| within previous X days, within next X days | Enter a whole number. |
| Object: Decimal | is, is not, present, not present, less than, less than or equal to, greater than, greater than or equal to | Enter any decimal value. |
| Object: Drop-down | is, is not, present, not present | Select from the field's options. |
| Object: Integer | is, is not, present, not present, less than, less than or equal to, greater than, greater than or equal to | Enter a whole number. |
| Object: Multi-line | is, is not, present, not present, includes, doesn't include, includes string, doesn't include string | Enter any text-based value. |
| Object: Number | is, is not, present, not present, less than, greater than, less than or equal to, greater than or equal to | Enter a numeric value. |
| Object: Regex | is, is not, present, not present, includes, doesn't include, includes string, doesn't include string | Enter any value. |
| Object: Text | is, is not, present, not present, includes, doesn't include, includes string, doesn't include string | Enter any text-based value. |
| Object: Update | is | A record was created or updated for the specified custom object. |
| **Lookup relationships** | | |
| Lookup relationship | is, is not, present, not present | Select from records of that target object. You can also refer to the related record's fields with placeholders. |

## Building object trigger action statements

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/object_trigger_actions.png)

Action statements define what occurs if the condition statements are true and the
trigger fires. Essentially, these are "then" statements. *If* your conditions
are true, *then* perform these actions. Similar to the conditions, the
available actions are determined based on the custom object's fields. However, there
are also predefined notification actions.

The following actions are supported:

| Field type | Action |
| --- | --- |
| **Object** (available options vary based on the fields defined for the object) | |
| Object: Checkbox | *True* or *False* |
| Object: Date | Set a date. |
| Object: Decimal | Specify a decimal value. |
| Object: Drop-down | Select one of the field's options. |
| Object: Integer | Specify a whole number value. |
| Object: Multi-line | Set a text-based value. |
| Object: Number | Set a numeric value. |
| Object: Regex | Set a value. |
| Object: Text | Set a text-based value. |
| **Lookup relationships** | |
| Lookup relationship | Select the related object and specify an action for records of the related object. |
| **Other** |  |
| Notify by: Active webhook | Set the active webhook to notify. For more information about using webhooks, see [Creating a webhook](https://support.zendesk.com/hc/en-us/articles/4408839108378). If you select a different notification destination when editing a trigger action, the body text resets. |
| Notify by: Group email | If the object is related to tickets, you select the group to notify. If you select a different notification destination when editing a trigger action, the body text resets. |
| Notify by: Text group | If you are using Zendesk Text, you can configure a text to be sent to a group of users when the trigger conditions are met. See [Using text notifications with triggers: recipes and tips.](https://support.zendesk.com/hc/en-us/articles/4408882005402) |
| Notify by: Text user | If you are using Zendesk Text, you can configure a text to be sent to a user when the trigger conditions are met. See [Using text notifications with triggers: recipes and tips.](https://support.zendesk.com/hc/en-us/articles/4408882005402) |
| Notify by: User email | Select a user related to the object or a related object to notify. You can set the email user to any of the following:  - **(current user)**: The last person who updated the   record - **(all non-restricted agents)**: Includes all agents that   have unrestricted access to the object - **Email user**: The actual, registered name of the agent   you want to notify.   Adding the email user action allows you to enter the email subject and body text. Body text can be formatted using HTML or placeholders. See [Using placeholders](../business-rules/using-placeholders.md) for more information on formatting with placeholders.  If you select a different notification destination when editing a trigger or automation, the body text will reset. |