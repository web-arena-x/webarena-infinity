# Getting started with text

Source: https://support.zendesk.com/hc/en-us/articles/4408823788314-Getting-started-with-text

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

You can respond to inbound text messages, automate alerts, or [send proactive messages](https://support.zendesk.com/hc/en-us/articles/4408882005402#start) using your Zendesk phone number. For example, you can send an automated text response when a customer submits a request or alert an agent via text when a ticket needs attention (for examples, see [Text recipes](https://support.zendesk.com/hc/en-us/articles/4408882005402)).

Texts automatically create tickets so you can apply all the advantages of automated workflows, centralized reporting and full customer history to text support. There’s no coding or additional software required, so you and your team can get started in minutes.

Note: Text messaging is not available for trial accounts or sandbox environments. Due to a change in US telecom regulations, businesses that want to send and receive texts must first register for A2P10DLC, otherwise all texts will be blocked (see, [Registering to use A2P 10DLC for text messaging](https://support.zendesk.com/hc/en-us/articles/4408837560730)). This registration will take longer than the Suite trial period. For more information about text, see [Getting started with Text](https://support.zendesk.com/hc/en-us/articles/4408823788314) and [Text recipes](https://support.zendesk.com/hc/en-us/articles/4408882005402).

**Text message support**

- Text messages can be up to the standard 160 character limitation in length.

  If you type a longer message, it will be split into multiple messages, each 153 characters in length. For example, if you type a message of 161 characters, it will be split into two messages; one of 153 characters, and one of 8 characters.
- You can send up to 250 simultaneous text messages from the same number. If you exceed this, messages will no longer be sent, and you'll see a warning that the message was rejected by the provider.
- Text does not support short codes or alphanumeric sender ID
- You can receive inbound MMS messages on US local numbers, but Text does not currently support outbound MMS messages.

To learn about the supported countries, and prices for Text, see [Zendesk Text number availability and pricing](https://support.zendesk.com/hc/en-us/articles/4408843672346).

This article contains the following topics:

- [Setting up text](#topic_fbx_msd_4kb)
- <#topic_ybz_rsd_4kb>

## Setting up text

Use the following topics to help you set up text:

- [Choosing a text number](#topic_ndl_nsd_4kb)
- [Sending an inbound text](#topic_ggw_nsd_4kb)
- [Automating an outbound text](#topic_l3x_nsd_4kb)

### Choosing a text number

You set up a new text number in Admin Center under **Messaging and social** > **Text**.

If you want to add text to an existing Zendesk phone number, see [Enabling a Zendesk phone number for text](https://support.zendesk.com/hc/en-us/articles/4408823877146-Managing-individual-number-settings#topic_gcs_vf3_ccb).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/text_GS_one.png)

For detailed steps, see [Adding and managing Text numbers](https://support.zendesk.com/hc/en-us/articles/4408885904922-Setting-up-the-Text-channel-WIP-).

### Sending an inbound text

Now you can send a test text from a mobile phone to your text number. You’ll see that your text will automatically create a ticket. Public replies in the ticket will send a text back to you.

The following example show what a text ticket looks like and the texts the customer sees on their phone.

![Sample text ticket](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/image1.png)

![Sample text ticket](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/image0.png)

Note: To take advantage of user identification for inbound texts, set the mobile phone number you use for testing as the “direct line” for an end-user profile. Learn more [here](https://support.zendesk.com/hc/en-us/articles/4408821302810-Understanding-how-Talk-calls-become-tickets#topic_hz3_5nm_sx).

### Automating an outbound text

Now that you’ve received and responded to an inbound text, take it to the next level and set up an automated outbound text using a trigger.

The following example shows a trigger that responds to text messages with a standard message and the text the customer sees on their phone.

![Sample text trigger](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/image2b.png)

![Sample text trigger](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/image0%20(1).png)

For more help creating Text triggers, see [Automating SMS support with Text triggers](https://support.zendesk.com/hc/en-us/articles/4408885601178).