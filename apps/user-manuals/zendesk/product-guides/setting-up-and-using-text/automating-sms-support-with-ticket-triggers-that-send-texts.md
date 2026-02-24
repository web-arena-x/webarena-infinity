# Automating SMS support with ticket triggers that send texts

Source: https://support.zendesk.com/hc/en-us/articles/4408885601178-Automating-SMS-support-with-ticket-triggers-that-send-texts

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

Important: You are responsible for using the call and text features in Zendesk in compliance with all applicable laws. Certain jurisdictions may require end-user consent prior to initiating telephonic outreach. By enabling these features, you agree that you have received the required consent.

Just as with tickets from other Zendesk channels, you can set up [ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) to manage your text tickets. In addition to the actions and conditions available for all tickets, there are a few text-specific options you can use. For step-by-step instructions and ideas, see [Sending outbound texts: Recipes and tips](https://support.zendesk.com/hc/en-us/articles/4408882005402).

This article contains the following topics:

- [Considerations when using ticket triggers to send text messages](#topic_wsh_jnf_fdc)
- [Text conditions and actions for ticket triggers](#topic_ysr_4nf_fdc)
- [Understanding responses to notifications](#topic_wgt_l4b_2y)

For general information about setting up triggers, see [About Zendesk triggers and how they work](https://support.zendesk.com/hc/en-us/articles/4408822236058-About-triggers-and-how-they-work) and [Triggers resources](https://support.zendesk.com/hc/en-us/articles/4408843730458-Triggers-resources).

Important: In the United States, you must register your number to use A2P 10DLC, a mandatory requirement to send business text messages. See [Registering to use A2P 10DLC for text messaging](https://support.zendesk.com/hc/en-us/articles/4408837560730).

## Considerations when using ticket triggers to send text messages

Keep in mind the following when using triggers to send text messages:

Warning: If your Zendesk account has a high ticket turnover and you are using text triggers, this will generate a high number of outgoing text messages. When a high number of text messages are sent from the same number, they might be marked as spam by the mobile networks. Before you configure text triggers, consider if this is the right solution for you.

- Keep the body text short or it might be broken into multiple messages. Remember that placeholders will be expanded. A text message (including expanded placeholders) cannot exceed 1,600 characters. If your text message goes over this limit, you'll receive a delivery failure.
- You'll be limited to approximately 250 notifications a day before a carrier's spam detectors might block your number, so avoid using these for mass outbound notifications.
- The end-user's phone number should be set as their direct line (see [Identifying the caller and handling new user accounts](https://support.zendesk.com/hc/en-us/articles/4408885601178)). If this isn't set, a new user will be created when the end-user replies.
- We will capture replies to these notifications as tickets for processing by agents.
- You don't need to set up a trigger to send updates to requesters when updates to a ticket are made. This is built into Text and happens automatically.
- If an end user has more than one phone number associated with their profile and you send them a text message, the message is sent to the first phone number that was added to their user profile. If you want text messages to be sent to another phone number, you’ll need to remove all phone numbers from the profile and re-add them, ensuring that the first phone number you add is the one you want text messages sent to.
- In the Zendesk Agent Workspace, if a ticket fires a trigger that sends text messages, neither the text messages nor the trigger that fired them show in the [events log](https://support.zendesk.com/hc/en-us/articles/4408829602970) for the ticket.

## Text conditions and actions for ticket triggers

To configure a ticket trigger to act on tickets received by SMS texts ([via type 57](https://developer.zendesk.com/documentation/ticketing/reference-guides/via-types/)), use the following condition:

- **Ticket > Channel** | **Is** | **Text**

To configure a ticket trigger to send text message notifications, you can use the following actions:

- **Notify by > Group text**: Specify a group of users to receive a text message notification.
- **Notify by > User text**: Select (current user), (requester), (assignee), or a specific user from the drop-down menu to receive a text message notification.

For both actions, you need to specify the SMS number to send the message from as well as the SMS message itself.

## Understanding responses to notifications

Responses to notifications are placed into a Text ticket, like other inbound Text messages.
If the end-user's number doesn't currently have an open ticket, a new ticket is created. If the end-user's number does already have an open ticket, the response is added to that existing ticket.

When the last message sent to a customer in a ticket is a Text notification, the notification appears in the ticket as a private comment. This way, agents addressing the ticket can get the appropriate context from the Text conversation.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/text_notification.png)