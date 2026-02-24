# Sending bulk email messages in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408828307226-Sending-bulk-email-messages-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on Sell Growth plans and above](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_pee.png)

You can use the views provided in the **Leads**, **Contacts**, and **Deals** pages to select multiple recipients for a single email message.
This feature is not available on the lowest Sell plan.

This article covers the following topics:

- [Sending a bulk email message](#topic_s2k_xgw_3tb)
- [Bulk send limitations](#topic_psy_xgw_3tb)

Note: To send emails in Sell, you have to first set up an email integration in your Sell account (see [Integrating email with Zendesk Sell](https://support.zendesk.com/hc/en-us/articles/4408821242266-Integrating-email-with-Zendesk-Sell)).

## Sending a bulk email message

In Sell, you can send emails in bulk using the following instructions, or you can set up the MailChimp email integration in Sell to send emails in bulk (see [MailChimp Integration](https://support.zendesk.com/hc/en-us/articles/4408832300442)).

**To send a bulk email message**

1. Select the **Leads** or **Contacts** or **Deals** page.
2. You can use either the Index or Table views on the **Leads** and **Contacts** pages, or the Stage or Table views on the **Contacts** page.
3. Select the checkbox next to the name of the lead or contact or deal.
4. (Alternatively) If you want to select all items in a view, click the **Select All** checkbox at the top of the list.
5. When you’ve selected all the leads or contacts you want to send the email message to, click **Email** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_email.png)).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-email-contacts.png)
6. The Communication Center is displayed with a blank email message addressed to the leads, contacts, or primary contacts of the deals you selected. Enter your email message, then click **Send Email**.

The recipients of a bulk email message are not aware that the message has been sent to other recipients.

## Bulk send limitations

Zendesk Sell allows each user on an account to [send up to 300 emails](https://support.zendesk.com/hc/en-us/articles/4408827866266) per rolling 24 hour period. Since certain email providers often limit the number of emails allowed to be sent out within a day, this limit helps to prevent you from exceeding that limit. If you reach the 300 emails limit in Sell, [reach out to the Zendesk Customer Support team](https://support.zendesk.com/hc/en-us/articles/4408843597850) to increase your daily limit to match your email server's limits.

Note: To prevent the risk of failed or undelivered emails, confirm the rate limits from your email server.

Increasing beyond 1,000 emails per day can cause email delivery issues. For example, an email server can have an email sending limit of 2,000 emails per day, but a rate limit that allows no more than 300 emails to be sent at one time (bulk email) or no more than 200 emails in 5 minutes. Sending a bulk email from Sell that exceeds your rate limit can result in emails showing as sent from Sell, but not actually getting sent because your email server blocked all emails after the rate limit was reached.