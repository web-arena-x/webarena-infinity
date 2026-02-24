# Understanding object triggers

Source: https://support.zendesk.com/hc/en-us/articles/6294230624410-Understanding-object-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

In addition to using custom objects related to tickets in ticket triggers, you can also define triggers that run any time an object's record is created or updated. These are called *object triggers*. For example, when an agent creates a new custom object record, the object triggers defined for that custom object fire and can update the record accordingly.

This article contains the following topics:

- [Requirements and limitations](#topic_fw4_q1t_mbc)
- [Understanding object triggers for custom objects](#topic_rpy_4ch_2zb)
- [Determining which type of trigger to use](#topic_b2z_2fh_2zb)

Related articles:

- [Creating object triggers](https://support.zendesk.com/hc/en-us/articles/7313293890970)
- [Object triggers conditions and actions reference](https://support.zendesk.com/hc/en-us/articles/7313293784218)
- [Managing object triggers](https://support.zendesk.com/hc/en-us/articles/7313294079130)

## Requirements and limitations

To create and use object triggers, the following must be true:

- You've [activated custom objects](https://support.zendesk.com/hc/en-us/articles/6073693948058).
- You've [created at least one custom object](https://support.zendesk.com/hc/en-us/articles/5392409465370).

Consider the following limitations when creating and using object triggers:

- Object triggers only support custom objects.
- You can have a maximum of 100 active triggers per object.
- You can create a maximum of 500 triggers total, including active and inactive triggers, per object.
- An object trigger can contain a maximum of 50 total conditions. This includes both "all" and "any" conditions.
- Within an object trigger condition that supports multi-select, you can select a maximum of 50 values.
- An object trigger can contain a maximum of 25 actions.
- An object trigger can't exceed 64 KB in size.

## Understanding object triggers for custom objects

Object triggers are created and managed on the Object tab of the Triggers page in Admin Center.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/object_triggers_page.png)

Object triggers can be created only for custom objects. Just as ticket triggers run when a ticket is created or updated, object triggers run when the specified custom object's records are created or updated. When a custom object record event occurs, any triggers that exist for that object are evaluated. After all of that object's triggers are evaluated, one update is made to the record with all applicable changes. If there are two applicable actions that set a value for the same field, the last write will be the one you see.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/object-trigger-cycle.png)

For example, let's say you're an IT department using custom objects to manage assets, such as software licenses and laptop assignments. You have a custom object named *Asset*, which has a custom drop-down field named *Type*, a checkbox named *Requires approval*, and a lookup relationship field pointing to users named *Asset owner*. If you define an object trigger for the Asset object, any time an agent creates or updates an asset record, the trigger fires. You might create a trigger that automatically assigns a default user as the owner if *Requires approval* is checked and no *Asset owner* is specified in the record, or you might want to define a trigger that notifies the asset owner any time their asset's record is updated or a new asset is created and they're listed as the owner.

## Determining which type of trigger to use

Determining which type of trigger to use is based largely on the type of event that results in the trigger running. If you want the trigger to run when a ticket is created or updated, use a ticket trigger. If you want the trigger to run when a custom object record is created or updated, use an object trigger. Both ticket triggers and object triggers can update fields on the object it's based on as well as fields related to the object. That means a ticket trigger can have conditions and actions based on a custom object as long as there is a ticket lookup relationship field pointing to that custom object. Likewise, an object trigger can have conditions and actions based on tickets if the custom object contains a lookup relationship field pointing to a ticket.

Ticket triggers can update fields on the object it's based on (tickets) as well as some fields related to the object, such as requester (user) and organization. A ticket trigger can have conditions and actions based on a custom object as long as there is a ticket lookup relationship field pointing to the custom object.