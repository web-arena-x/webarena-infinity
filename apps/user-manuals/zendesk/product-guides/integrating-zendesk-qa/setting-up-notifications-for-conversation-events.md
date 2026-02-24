# Setting up notifications for conversation events

Source: https://support.zendesk.com/hc/en-us/articles/7043662243226-Setting-up-notifications-for-conversation-events

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

This article describes how to set up notifications to review conversations based on help desk events. By following these steps, you can ensure timely reviews and improve the quality of your customer support.

This article contains the following topics:

- [About notifications for conversation events](#about-notifications)
- [Setting up webhooks](#setting-up-webhooks)
- [Configuring triggers](#configuring-triggers)

## About notifications for conversation events

Notifications for conversation events help you stay informed about important interactions in your help desk. This guide uses Zendesk as an example.

For more information on webhooks, see [Zendesk's general guide](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks-to-interact-with-third-party-systems) and [how to send them to Slack](https://support.zendesk.com/hc/en-us/community/posts/4409515187866-Push-notifications-from-Zendesk-to-Slack).

## Setting up webhooks

To set up notifications for conversation events, you need to create a webhook in Slack and configure it in Zendesk.

**To set up a webhook in Slack**

1. Go to [Incoming webhook](https://api.slack.com/incoming-webhooks) in Slack and set up a new webhook.

**To configure the webhook in Zendesk**

1. As a Zendesk admin, navigate to **Settings** > **Extensions** > **Add target**.
2. Choose **HTTP Target**.
3. Add the Incoming webhook's URL that you generated in step 1 as the target URL.
4. Set the target's **method** to `POST` and the **Content type** to `JSON`.
5. Test the target by passing in an example message, such as `{ "text": "Hello Zendesk QA!" }`.
6. If you receive the message on Slack, submit your new HTTP target. If not, check the **API** > **Target Failures** page for debugging information.

## Configuring triggers

Once the webhook is set up, you can configure triggers in Zendesk to send notifications to Slack based on specific events.

**To configure triggers in Zendesk**

1. Navigate to **Settings** > **Business Rules** > **Triggers**.
2. Click **Add Trigger** and give it a name.
3. Set the conditions for the trigger. For example, `Satisfaction` `Is` `Bad`.
4. Click **Add action** and select `Notify target` from the first dropdown, then select the name of the target you created.
5. In the **Message** field, enter the following JSON payload:

```
{
 "text": "You received some feedback on a ticket. "
}
```

For more details on constructing the link and the `externalTicketId` query parameter, see our article about [linking to Zendesk QA from your help desk](https://support.zendesk.com/hc/en-us/articles/7043760015642).

Whenever your trigger's conditions are fulfilled, you will receive a Slack notification.

*(Optional)* You can enhance the Slack message with [advanced formatting](https://api.slack.com/messaging/webhooks#advanced_message_formatting) and add custom buttons. Use Slack's [Message Formatting](https://api.slack.com/docs/messages/builder) tool to preview the JSON payload as a real Slack message.