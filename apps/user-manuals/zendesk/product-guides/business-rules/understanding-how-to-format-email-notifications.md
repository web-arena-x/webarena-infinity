# Understanding how to format email notifications

Source: https://support.zendesk.com/hc/en-us/articles/8407456809754-Understanding-how-to-format-email-notifications

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

[Ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) are the primary method by which notifications are sent to end users from your account. However, they can also be sent by automations and other business rules. Notifications to users can be sent by email, text message, or posts on X (formerly Twitter). Of these, only email supports formatted content. Text messages and X posts must be in plain text.

There are two layers to consider when formatting email notifications:

- **HTML template**: The HTML template for emails controls the overall design and structure of email notifications. See [Customizing your email templates for notifications](https://support.zendesk.com/hc/en-us/articles/4408886168090).
- **Notification body**: The body of the notification is the text inserted into the `{{content}}` placeholder of the email templates. This can be plain text or formatted text, and is defined within the trigger's notification action.

This article describes the following options and considerations for formatting the content of email notifications:

- [Using HTML](#topic_cbj_ytg_ldc)
- [Using Liquid markup](#topic_c1f_ttg_ldc)

## Using HTML to format the content of email notifications

HTML tags can be used to format the body of email notifications sent by ticket triggers and other business rules. However, there are a few considerations to keep in mind:

- The content you specify for an email notification in a ticket trigger is inserted into the `{{content}}` placeholder in the [email templates](https://support.zendesk.com/hc/en-us/articles/4408886168090). Ensure the content you enter in the trigger notification action is compatible with the content of your email templates.
- The way email clients and web browsers render HTML varies. To provide a more consistent experience and to reduce issues, such as being interpreted as spam, follow these [guidelines for customizing HTML emails](https://support.zendesk.com/hc/en-us/articles/4408886168090#topic_i3y_3vc_x3).
- You might need to compress the HTML for some triggers. You can use compression tools, such as [Text Fixer](https://www.textfixer.com/html/compress-html-compression.php).
- If you see extra gaps or spaces in the content emailed to customers, remove all unnecessary characters, such as line breaks.
- HTML isn't supported when using dynamic content in the body of the email notification action for ticket triggers.

## Using Liquid markup to format the content of email notifications

[Liquid](https://shopify.github.io/liquid/) is a templating language for rendering HTML. It's the mechanism that enables the automated placement of data in email notifications using placeholders. In addition to placeholders, Liquid can also be used to create simple programming logic about how the content is expressed in the notification, such as if/else statements, case statements, and variable assignments.

For more information and examples, see [Understanding Liquid markup and Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408883291290).