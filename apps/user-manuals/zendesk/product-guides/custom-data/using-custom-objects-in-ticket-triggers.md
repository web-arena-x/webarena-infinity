# Using custom objects in ticket triggers

Source: https://support.zendesk.com/hc/en-us/articles/5928347565082-Using-custom-objects-in-ticket-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Location: Admin Center > Objects and rules > Business rules > Triggers

Admins can [create](https://support.zendesk.com/hc/en-us/articles/5392409465370) [custom objects](https://support.zendesk.com/hc/en-us/articles/5914453843994) to capture data that doesn't fit into Zendesk's standard objects (tickets, users, and organizations). Then, agents can add that information to Zendesk by creating custom object records. To use custom objects and their records with ticket triggers, a ticket must have a defined lookup relationship field that points to a custom object.

## Using custom objects in ticket triggers

Note: A custom object can't be deleted if it's referenced in a Support ticket trigger.

**To use a custom object in a ticket trigger**

1. Create a [custom ticket field](https://support.zendesk.com/hc/en-us/articles/4408883152794) that's a [lookup relationship field](https://support.zendesk.com/hc/en-us/articles/4591924111770) pointing to a custom object.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
3. Click **Add trigger**.
4. Enter a **Name** and **Description**, and then select an existing **Trigger category** for your trigger or [create a new one](https://support.zendesk.com/hc/en-us/articles/4408834781594).
5. Click **Add condition** to set up the trigger to meet **All** or **Any** conditions.
6. Use the **Category** dropdown to select the lookup relationship field or a related object's field or record that you want to use as a condition. Then select an **Operator** and **Value** for the condition. See [Building trigger condition statements](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_i3y_fkz_1cb).
7. Click **Add action** to set the actions that occur when the trigger conditions are met.
8. Select an **Action** and a **Value** for each action you add. See [Building trigger action statements](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_ncz_4kz_1cb).

   Note: Lookup relationship fields can only be used in notification actions. Specifically, when the lookup relationship field exists on the ticket object and points to a custom object that is related to a user, you can email a user and assign a ticket to a user.
9. Click **Save**.

## Using custom objects in object triggers

In addition to using custom objects related to tickets in ticket triggers, object triggers provide a way for admins to create triggers oriented around custom object record creation and updates. The conditions and actions available depend entirely on the [fields defined for the custom object](https://support.zendesk.com/hc/en-us/articles/5392409465370#topic_cq4_1sn_lwb) itself.

For more information, see [Creating and using object triggers](https://support.zendesk.com/hc/en-us/articles/6294230624410).