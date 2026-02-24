# Hiding credit card numbers in chats and chat history

Source: https://support.zendesk.com/hc/en-us/articles/4408881881882-Hiding-credit-card-numbers-in-chats-and-chat-history

---

Using the automatic credit card number redaction feature, you can automatically hide credit card numbers when chatting and in your chat history.

The checks don't guarantee that all credit card numbers will be identified. They also don't guarantee that some numbers that aren't credit card numbers will be skipped. The system does check for phone number and URL patterns and skips them. For example, some international phone numbers may pass the [Luhn check](https://en.wikipedia.org/wiki/Luhn_algorithm), but if the numbers start with a +, they won't be redacted.

**To enable automatic credit card redaction**

1. Select **Settings**>**Account**, then the **Security**tab.
2. Under **Automatic Redaction**, check the **Enable automatic redaction of credit card numbers.**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/turn_on_auto_redaction.png)

After credit card redaction is enabled, only the first six numbers and last four numbers of the credit card will be displayed. The tag “ chat\_system\_credit\_card\_redaction” will be added.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/auto_redaction_chat_example.png)