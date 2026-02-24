# A complete guide to understanding email in Zendesk - Part 4: Common email channel problems

Source: https://support.zendesk.com/hc/en-us/articles/4408887479834-A-complete-guide-to-understanding-email-in-Zendesk-Part-4-Common-email-channel-problems

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Channels > Talk and email > Email

Articles in the series

- [Introduction: A complete guide to understanding email in Zendesk](https://support.zendesk.com/hc/en-us/articles/4887918604058)
- [Part 1: How the email channel works](https://support.zendesk.com/hc/en-us/articles/4408888639258)
- [Part 2: Incoming email requests and notifications](https://support.zendesk.com/hc/en-us/articles/4408887388058)
- [Part 3: Outgoing email notifications](https://support.zendesk.com/hc/en-us/articles/4408893474202)
- [Part 4: Common email channel problems](https://support.zendesk.com/hc/en-us/articles/4408887479834)

In the last part of this guide, we explain what you can do when things go wrong with the email channel and how you can fix them.

The most common email problem that Zendesk Support customers contact us for support about is that their customers are not receiving outgoing email notifications. This is often the result of issues that are easily resolved.

Here are the common reasons that your customers are not receiving outgoing email notifications:

- You’ve set up an external email domain but haven't added an SPF record to your external domain’s DNS. See [Setting up SPF for Zendesk to send email on behalf of your email domain](https://support.zendesk.com/hc/en-us/articles/4408832543770-Setting-up-SPF-for-Zendesk-to-send-email-on-behalf-of-your-email-domain).
- The email notification has been caught in the spam filter in the customer’s email application. To verify that the email notification was sent to the customer, you can easily check the [ticket events](https://support.zendesk.com/hc/en-us/articles/4408829602970-Viewing-all-events-of-a-ticket), which will show you each action that was taken on a ticket. If the notification was successfully sent, the problem is likely on the recipient's end of the email exchange.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/allevents1.png)
- You’ve deactivated one or more of the default email notification triggers.
- The conditions contained with a notification trigger (or automation) have not been met.
- The customer’s user account does not include their email address.

Read more about troubleshooting and resolving these problems in [Customers are not receiving emails](https://support.zendesk.com/hc/en-us/articles/4408823742618).

Another email problem that occurs far less often but that you should still be aware of is the result of automated email replies created both inside and outside of your Zendesk Support account generating more email notifications than you want. This is called a mail loop and occurs when two automated email reply systems start exchanging messages.

As an example, you might imagine that a trigger such as the Notify requester of received request, which generates an automatic reply, may start a mail loop if the email address it sends an email notification to has been set to generate any automated response that does not announce itself as such, like an out-of-office response. Zendesk Support prevents mail loops like this from occurring, but they sometimes occur under certain circumstances. You can read an in-depth explanation of how Zendesk Support manages mail loops in [About mail loops and Zendesk email](../../product-guides/managing-your-email/about-mail-loops-and-zendesk-email.md).