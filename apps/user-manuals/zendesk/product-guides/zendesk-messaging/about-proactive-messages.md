# About proactive messages

Source: https://support.zendesk.com/hc/en-us/articles/5381304334234-About-proactive-messages

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Verified AI summary ◀▼

Proactive messaging lets you initiate conversations with customers through your Web Widget or mobile SDK based on set conditions. Use it to offer support, engage customers, and boost sales. Configure messages by adding content, setting rules, and choosing timing. Manage messages via the admin page, and choose between agent or AI agent responses to enhance customer interactions.

Note: This functionality is part of [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690).

With proactive messaging, you can deliver targeted messages to your customers through your Web Widget or mobile SDK channel without waiting for them to start the conversation.

This article includes the following topics:

- [Overview of proactive messaging](#topic_tsn_shy_wwb)
- [The Proactive messages admin page](#topic_yl5_shy_wwb)
- [Agent response types](#topic_sgz_shy_wwb)
- [Requirements and limitations](#topic_gcf_thy_wwb)
- [The customer experience](#topic_e5j_thy_wwb)

See [Creating proactive messages for the Web Widget](https://support.zendesk.com/hc/en-us/articles/5511266103834) and [Creating proactive messages for mobile SDK channels](https://support.zendesk.com/hc/en-us/articles/5511216991898)
for more information.

## Overview of proactive messaging

Proactive messaging lets you automatically initiate conversations with customers based on specified conditions that you define. Your customers can then choose whether or not to respond.

This can be useful in a number of ways, including:

- Providing proactive support, such as offering automated self-service based on user behavior and interaction history, as well as show delays on product delivery and scheduled maintenance.
- Driving customer engagement, acquisition and retention with custom greetings, guided onboarding and announcements.
- Increasing sales and conversion rates with targeted messages based on user events and past interactions.

Setting up a proactive message includes the following tasks:

- **Adding the proactive message**. This creates a framework for the message and adds it to the Proactive messages list.
- **Composing the message**. Write and format a message for your customers using text and emojis, capture customer data if needed, select a messaging channel, and choose whether to have an AI agent initially manage the conversation or to pass responding customers to a human agent instead. See [Agent response types](#topic_sgz_shy_wwb)for more information.
- **Setting the rules**. This is where you define the conditions a customer must meet to receive the message, and optionally create tags to add to any tickets generated from the conversation.
- **Choosing when to send the message**. Here, you’ll indicate when a proactive message can be sent: During or outside business hours, or any time of the day. You’ll also select how often a message can be sent to a customer: One time only, once per customer visit, or every time the customer meets the defined conditions for receiving the message.
- **Publishing the message**. This simple click of a button makes the message live, meaning any customers who meet the message’s conditions will immediately begin receiving those messages.

For more information, see the following articles:

- [Creating proactive messages for the Web Widget](https://support.zendesk.com/hc/en-us/articles/5511266103834)
- [Creating proactive messages for mobile SDK channels](https://support.zendesk.com/hc/en-us/articles/5511216991898)

## The Proactive messages admin page

The Proactive messages page in Admin Center is your starting point for the tasks described above, as well as a list of existing messages. You can click the message to view its configuration page.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/PM-admin_page.png)

The list of existing messages includes columns displaying the following information:

- **Name**: A short, descriptive name for the message.
- **Status**: The current state of the message. You can sort the list by this column.

 - **Live**: The proactive message has been published and the message is being sent to customers who meet the conditions.
 - **Draft**: Message creation is in progress, and the message has not been previously published.
 - **Paused**: The proactive message campaign has been temporarily halted. This can happen when:

    - An admin has manually paused a previously live proactive message.
    - The proactive message uses AI agent capability (such as generative replies) and your account is configured to pause AI agent functionality when it [reaches its automated resolution limit](https://support.zendesk.com/hc/en-us/articles/6958358659226#topic_iw3_b2h_bdc). These campaigns will [resume](https://support.zendesk.com/hc/en-us/articles/5511266103834#topic_szk_tjd_42c) when automated resolutions are available. Proactive messages paused for this reason are indicated by a warning icon in the Proactive messages list:

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/pm_paused_ar_limit.png)
 - **Contains errors**: Previously published message is no longer active due to errors. Most often this status appears when the connected messaging channel is deleted or altered in a way that makes it incompatible with the proactive message, such as deleting the connected AI agent.
    You can view the message for information on missing or inadequate information.
- **Channel**: The channel on which you want to run your proactive message.
- **Sent**: The number of customers who have been sent the proactive message. You can sort the list by this column.
- **Opened**: The number of customers who have viewed the proactive message and clicked on the message. You can sort the list by this column.
- **Replied to**: The number of customers who have interacted with the proactive message, which means engaged with the AI agent or shared details when the agent response type was configured. You can sort the list by this column.
- **Updated**: The date of the most recent update to the proactive message.
 You can sort the list by this column.

Each message in the list has an options menu (
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)), visible when you hover over the message. The
following options may be available from this menu, depending on the message’s current status:

- **Edit**: Opens the message’s configuration page. Option appears on all messages regardless of status.
- **Clone**: Creates a copy of the message and adds a draft of it to the message list. Option appears when message status is *Live*, *Draft,* or *Paused*.
- **Publish**: Activates the proactive message. Option appears when message status is *Draft*.
- **Pause**: Temporarily stops a published proactive message. Option appears when message status is *Live*.
- **Resume**: Restarts a proactive message. Option appears when message status is *Paused*.
- **Delete**: Permanently deletes the message. Option appears on all messages regardless of status.

When you first visit the Proactive messages admin page, there are three partially-configured messages in draft form. Each one is configured to address a common use case for proactive messages. You can use these messages as a starting point for creating your own messages by cloning or editing them.

## Agent response types

There are two agent response types you can choose to use in your proactive messages:

- **Agent**: This is the simpler response type, which requires you to compose a short text-only message for the customer (no emojis) and optionally request the customer’s name and/or email address before handing off the conversation to a live agent.
- **AI agent**: AI agent responses allow you to create your message by referring to an answer in an active, published AI agent *within the same brand*.
 After the initial message appears, the connected [AI agent](https://support.zendesk.com/hc/en-us/articles/6970583409690) manages the conversation.

See [The customer experience](#topic_e5j_thy_wwb)for more information and examples of these message response types.

## Requirements and limitations

Consider the following requirements and limitations before getting started with proactive messaging.

### Requirements

Your account must meet the following requirements to use proactive messaging:

- Agent Workspace must be activated.
- Messaging must be activated.
- At least one messaging Web Widget OR one mobile SDK channel must exist to publish a proactive message.
- To use an AI agent response, the connected channel must have one active, successfully published AI agent .
- (Legacy AI agents) When using an [AI agent response](#topic_sgz_shy_wwb), you can only choose from successfully published answers in the connected AI agent as your follow-up message.

### Limitations

The following limitations apply to the current version of proactive messaging:

- You can create up to 140 proactive messages.
- Proactive messages aren't sent to customers in currently active messaging conversations.
- Proactive messages are only available for the Web Widget and Mobile SDK messaging channels.
- Proactive messages aren't supported for third-party bots and social messaging channels.
- Proactive messages can't be used with [AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/6970583409690).
- Proactive messages can only be used on one channel at a time. Channels, however, can have multiple proactive messages running simultaneously.
- Proactive conditions with two conditions or less can't use nested conditions.

## The customer experience

The customer experience with proactive messages varies – not only with your specific settings and messages, but depending on whether you’re using a live or AI Agent response.

### Customer experience: Agent response

When the customer meets the defined criteria for activating a proactive message using the Agent reply type:

- A message appears above the messaging launcher button, displaying the text defined in the message configuration.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/PM_agent_reply_initial.png)

 This message is sent from the default sender defined in the channel settings, and overrides previously-configured launcher text.

If the customer chooses to click the message text to open the messaging window, any data capture requests are displayed. The customer can then choose to:

- Enter the requested information. The follow-up message is displayed, and the conversation is handed off to a live agent.
- Close the messaging window using the close launcher button. The message disappears. It may appear at another time, depending on the configured frequency settings.
- Ignore the message.

If the customer chooses to click the **X** to hide the message without opening it:

- The message disappears. It may appear at another time, depending on the configured frequency settings.

### Customer experience: AI agent response

When the customer meets the defined criteria for activating a proactive message using the AI agent reply type:

- A message appears above the messaging launcher button, displaying the text defined in the message configuration.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/PM_bot_reply_inital.png)

 This message is sent from the conversation AI agent.

If the customer chooses to click the message text to open the messaging window, the answer selected in the message configuration appears. The customer can then choose to:

- Interact with the answer.
- Close the messaging window using the close launcher button. The message disappears. It may appear at another time, depending on the configured frequency settings.
- Ignore the message.

If the customer chooses to click the **X** to hide the message without opening it:

- The message disappears. It may appear at another time, depending on the configured frequency settings.