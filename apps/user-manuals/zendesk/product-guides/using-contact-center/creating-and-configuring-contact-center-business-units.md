# Creating and configuring contact center business units

Source: https://support.zendesk.com/hc/en-us/articles/10252798826650-Creating-and-configuring-contact-center-business-units

---

In Contact Center, business units allow you to control contact center availability, emergency closures, and public holidays. They allow you to group queues together and apply closure rules consistently across departments and individual queues without modifying individual contact flows.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

In Contact Center, business units allow you to control contact center availability,
emergency closures, and public holidays. They allow you to group queues together and
apply closure rules consistently across departments and individual queues without
modifying individual contact flows.

Admins can access the business unit settings in the Zendesk for Contact Center
admin interface. If you can't access the settings, then contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to request the activation of the
Business Unit solution on your CloudFormation stack.

This article contains the following topics:

- [Understanding business units](#topic_l13_fxz_d3c)
- [Creating business units](#topic_wqt_q11_23c)
- [Adding queues to business units](#topic_xxq_v11_23c)
- [Adding public holidays](#topic_wcn_w11_23c)

## Understanding business units

A business unit represents a logical department or area of your contact center and
groups one or more Amazon Connect queues under a single operational profile.

With business units admins can:

- Apply emergency closures at the business unit level (affects all associated
  queues) or at an individual queue level within the unit.
- Define public holidays per business unit to manage non-standard operating
  days.

## Creating business units

Create a business unit to group related queues under a shared operational profile.
Business unit settings are evaluated at runtime within Amazon Connect contact
flows.

**To create a business unit**

1. In [Contact Center](https://support.zendesk.com/hc/en-us/articles/9696121449114), click **Admin
   Settings**.
2. Click the settings icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_cogs_icon.png)) in the
   sidebar.
3. Click the **Business Units** tab at the top.
4. Click **Add new business unit**.
5. Enter a unique name that identifies the business unit.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_bizunit_new.png)
6. (Optional) Enter a description to clarify the unit’s scope and purpose.
7. (Optional) Configure business unit–level emergency closure settings:
   - **Emergency close**: Activate to stop call handling for all
     queues in the unit.
   - **Close message**: Add a message to play to callers when the unit
     is closed.
8. Select **Create business unit**.

## Adding queues to business units

Add one or more Amazon Connect queues to a business unit so the unit’s emergency
closure and public holiday settings apply to those queues. Each queue can be
associated with only one business unit.

**To add a queue to a business unit**

1. In [Contact Center](https://support.zendesk.com/hc/en-us/articles/9696121449114), click **Admin
   Settings**.
2. Click the settings icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_cogs_icon.png)) in the
   sidebar.
3. Click the **Business Units** tab at the top.
4. Click the name of the business unit you want to update.
5. Under **Manage Queues and Holidays**, click **Add queue**.
6. Select a queue to assign to the business unit.

   You can assign a queue to
   only one business unit. To change a queue's business unit, you must
   first unassign the queue from the original unit.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_bizunit_queue_add.png)
7. (Optional) Set queue–level emergency closure:
   - **Emergency close**: Activate to stop call handling for this
     queue.
   - **Close message**: Add a message to play to callers when this
     queue is closed.
8. Cick **Add queue**

## Adding public holidays

Configure public holidays to manage non-standard operating days for each business
unit. Public holidays are evaluated at runtime and can be combined with hours of
operation logic in contact flows.

**To add public holidays for a business unit**

1. In [Contact Center](https://support.zendesk.com/hc/en-us/articles/9696121449114), click **Admin
   Settings**.
2. Click the settings icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_cogs_icon.png)) in the
   sidebar.
3. Click the **Business Units** tab at the top.
4. Click the name of the business unit you want to update.
5. Under **Manage Queues and Holidays**, click **Add holiday**.
6. Enter the holiday details:
   - **Holiday Name**: A short, descriptive name.
   - **Holiday Date**: The calendar date for the holiday.
   - **Closed**: Activate to close the business unit for the full
     day.
   - **Close message**: The message played to callers when the unit is
     closed for this holiday.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_bizunit_pubhols_add.png)
7. Click **Add holiday**.

Tip: Holidays are specific to the selected business unit and apply to full
days. If you need reduced hours, leave **Closed** off and [set hours-of-operation in the contact
flow](https://docs.aws.amazon.com/connect/latest/adminguide/set-hours-operation.html).