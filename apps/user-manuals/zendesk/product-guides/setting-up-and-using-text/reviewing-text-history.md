# Reviewing text history

Source: https://support.zendesk.com/hc/en-us/articles/4408846819226-Reviewing-text-history

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

You can review the transactions and message information associated with your text account by
viewing the text history page.

**To review text history**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social > Text**.
2. Click the **History** tab.

The text history page is displayed, and includes the following tables:

- [The Transactions table](#topic_fkr_c5q_xdb)
- [The Message details table](#topic_b4l_f5q_xdb)
- [About text statuses](#topic_aqk_q2y_xdb)

## The Transactions table

In the **Transactions** table, you can review a detailed list of charges including the
type, date, amount, and overall totals.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/text_history_transactions.png)

## The Message details table

In the **Message details** table, view information about each of the texts sent to and
from your account, including linked tickets and agents.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/text_history_messagedetails.png)

This table includes the following columns:

- **Message ID**, the unique identification number given to the text.
- **Ticket ID**, the ticket number associated with the text. You can click the number
  in this column to view the ticket.
- **Date**, the time and day the text was sent/received.
- **Direction**, whether the text was from a customer, or to a customer.
- **From**, the phone number that sent the text.
- **To**, the phone number that received the text
- **Status**, the current status of the text. See [About text statuses](#topic_aqk_q2y_xdb).
- **Agent ID**, the unique identification number for the agent assigned the text. You
  can click the number in this column to view the agent's profile.

## About text statuses

There are several stages a SMS message goes through before it is delivered to the customer.
You can find the current status of a SMS message in the [Message details table](#topic_b4l_f5q_xdb), described above. This article goes through
each status and what they mean.

- **Accepted**: When a request is first sent to Twilio through an API request to
  create a new text message, this is the first response received by the client. Twilio
  will now try to associate the correct ‘From’ phone number for the message.
- **Queued**: Once Twilio finds the correct ‘From’ phone number, the message is now
  queued to be sent out.
- **Sending**: Twilio will now start the process of sending out your message to the
  nearest upstream carrier in the SMS network.
- **Sent**: The message was successfully sent to the nearest upstream carrier and has
  been accepted for delivery.
- **Delivered**: Twilio has received confirmation from the upstream carrier that the
  message was delivered to the recipient.
- **Failed**: The upstream carrier did not accept the message from Twilio.
- **Received**: Each incoming message to your text number will have a received status
  associated with it.
- **Undelivered**: The message was not delivered and can be caused by a variety of
  reasons listed [here](https://www.twilio.com/docs/api/rest/message#error-values).