# Using dynamic content in messaging triggers

Source: https://support.zendesk.com/hc/en-us/articles/8989383314970-Using-dynamic-content-in-messaging-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

You can add dynamic content placeholders to the Send message to customer action in your
messaging triggers, allowing you to localize these responses and deliver them in your
end user’s preferred language through your web and mobile messaging channels.

This article includes the following topics:

- [About dynamic content in messaging triggers](#topic_pm5_4w1_p2c)
- [Using dynamic content in the Name of agent field](#topic_c2z_4w1_p2c)
- [Using dynamic content in the sent message](#topic_plf_pw1_p2c)

## About dynamic content in messaging triggers

In messaging triggers, you can only use dynamic content with the *Send message to
customer* action in the Name of agent field and the message text sent to the
end user.

To use dynamic content in a messaging trigger:

- Your account must be on the [improved messaging backend](https://support.zendesk.com/hc/en-us/articles/6041628932250)
- You’ll need to [create the dynamic content item](https://support.zendesk.com/hc/en-us/articles/4408882999066#topic_qcy_eci_je),
  and note the item’s [placeholder](https://support.zendesk.com/hc/en-us/articles/4408882999066#topic_enk_bdi_je).

Note: When a dynamic content placeholder used in a messaging trigger is deleted, the
content configured in the dynamic content will not be seen by the end user.

## Using dynamic content in the Name of agent field

The Name of agent field is required when using the Send message to customer action.
It defines the name that appears above the sent message in the conversation:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/agent_name.png)

By including the dynamic content placeholder in the Name of agent field, the agent
name can be selected based on the customer’s language setting.

**To use dynamic content in the Name of agent field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules > Messaging
   triggers**.
2. [Create and customize the trigger](https://support.zendesk.com/hc/en-us/articles/6058753945242#topic_w1p_vpn_q5b),
   selecting the *Send message to customer* action.
3. In the Name of agent field, enter the placeholder for the [dynamic content item](https://support.zendesk.com/hc/en-us/articles/4408882999066#topic_qcy_eci_je) you created
   for localizing agent names, for example `{{dc.agent_name}}`.
4. Click **Create**.

## Using dynamic content in the sent message

The Message field is where you define the text sent to a customer in the Send message
to customer action.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_message.png)

You can use a dynamic content placeholder to define all or part of the message
content. For example, you can create a generic greeting as a dynamic content item,
with variants for all of your supported languages. The message will appear in your
customer’s language setting.

**To use dynamic content in a sent message**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules > Messaging
   triggers**.
2. [Create and customize the trigger](https://support.zendesk.com/hc/en-us/articles/6058753945242#topic_w1p_vpn_q5b),
   selecting the Send message to customer action.
3. In the Message field, enter the message you want to send in your messaging
   conversation, and include any dynamic content placeholder you like.
4. Click **Create**.