# Setting up automatic messages in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9696142110618-Setting-up-automatic-messages-in-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Set up automatic messages to enhance customer interactions by configuring welcome and idle messages. Customize these messages using personalization tokens for a more tailored experience. Admin access is required to manage these settings. Choose whether messages are sent automatically or with agent prompts, and specify idle times for triggering messages. This feature helps maintain communication flow and improves customer engagement.

Automatic messages are triggered when a new conversation comes into the inbox or when the agent or customer has been idle for a while. You need admin access in Contact Center in order to configure automatic messages.

This article contains the following topics:

- [Configuring your welcome message](#topic_dpq_psb_qgc)
- [Configuring your idle message](#topic_j2m_qsb_qgc)
- [Configuring personalization tokens](#topic_ymn_qsb_qgc)

## Configuring your welcome message

Welcome messages can be set up as a default for your organization and at a queue level.

**To configure your welcome message**

1. In Contact Center, click the settings icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_cog.png)) to access the admin settings.
2. Click the **Workflows** tab.
3. Click **Edit workflow** and scroll down the page to **Automatic Messages**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zen_contact_cent_2-1.png)
4. Click **New Conversation**.
5. Add a custom welcome message and select whether it must be sent automatically or if the agent should be prompted before sending it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zen_contact_cent_2-2.png)
6. Once you have completed the welcome message, click **Save Workflow**.

## Configuring your idle message

There are two kinds of automatic messages: , and .

- Agent idle sends a message when the agent hasn’t responded for a set amount of time.
- Customer idle sends a message when the customer hasn’t responded.

**To add an idle message**

1. In Contact Center, click the settings icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_cog.png)) to access the admin settings.
2. Click the **Workflows** tab.
3. In the **Automatic Messages** section, click either **Agent idle** or **Customer idle**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zen_contact_cent_2-1.png)
4. Enter your custom message, the idle time in seconds, and select how often this message will be triggered. Then, select if the message will be sent automatically or if it should prompt the agent before sending.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zen_contact_cent_2-2.png)

Click **Save workflow**.

## Configuring personalization tokens

Welcome and idle messages can be customized using personalization tokens to improve the customer experience. The screenshot below shows an example.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zen_contact_cent_2-3.png)

For more information, see [Using personalization tokens in Contact Center](https://support.zendesk.com/hc/en-us/articles/9696137593626).