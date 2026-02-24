# Creating object triggers to update records and send notifications

Source: https://support.zendesk.com/hc/en-us/articles/7313293890970-Creating-object-triggers-to-update-records-and-send-notifications

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Location: Admin Center > Objects and rules > Business rules >
Triggers

[Object triggers](https://support.zendesk.com/hc/en-us/articles/6294230624410) are business rules that run based on custom object record events and automatically perform actions when specified conditions are met. All triggers in Zendesk are composed of two parts: *conditions* and *actions*. Conditions are the qualifications needed for the trigger to fire, and actions are performed when those qualifications are met.

Before creating and using object triggers, review the [requirements and limitations](https://support.zendesk.com/hc/en-us/articles/6294230624410#topic_fw4_q1t_mbc).

**To create an object trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Objects** tab at the top of the page, then click **Create trigger**.
3. Enter a **Name** for your trigger.
4. (Optional) Enter a **Description** for your trigger.

   You can provide details about what the trigger does. You'll be able to search for triggers based on description.
5. Select the **Trigger object**.

   This can't be changed after the trigger is saved.
6. Click **Add condition** to set up the trigger to meet **All** or **Any** conditions.
7. Select a **Category**, **Operator**, and **Value** for each condition you add.

   The field operator determines the relationship between the condition and the value. For example, if you select the field operator "Is", your condition will need to be equal to the value. See [Building object trigger condition statements](https://support.zendesk.com/hc/en-us/articles/7313293784218#topic_ey3_bbb_fzb).
8. Click **Add action** to set the actions that occur when trigger conditions are met.
9. Select an **Action** and specify a **Value** for each action you add. See [Building object trigger action statements](https://support.zendesk.com/hc/en-us/articles/7313293784218#topic_rzv_bbb_fzb).
10. Click **Create** and set the trigger to **Active** or **Inactive**.

    If you need to modify an object trigger after you create it or adjust the order of your object triggers, see [Managing object triggers](https://support.zendesk.com/hc/en-us/articles/7313294079130).