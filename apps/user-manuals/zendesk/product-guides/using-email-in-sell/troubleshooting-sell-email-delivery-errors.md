# Troubleshooting Sell email delivery errors

Source: https://support.zendesk.com/hc/en-us/articles/4408838259226-Troubleshooting-Sell-email-delivery-errors

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

This article describes the errors that might occur when sending email messages from Sell, including why they occurred and what you can do to fix the problem.

## Error 001: Email(s) failed to send

**What Happened:**We tried sending your email(s) from Sell, but something interfered and caused it to fail.

|  |  |  |
| --- | --- | --- |
|  | **What does that mean?** | **What can I do about it?** |
| Possibility #1 | The cause is unknown. | **Solution:** Try sending an email from your email account (outside of Sell) to see if you're able to successfully send email messages. If the issue persists, contact [Sell Support](https://support.getbase.com/hc/en-us/requests/new). |

## Error 002: Email(s) failed to send due to your sending limit

**What Happened:**Every email host (Gmail, Office365, etc.) has defined sending limits that determine how many emails can be sent daily, hourly, and sometimes even per minute. For example, some email servers allow for 500 emails to be sent per day and only 100 emails per hour. This means that you’re only able to send as many emails from Sell as your email provider's sending limit allows. For a list of common hosts and sending limits, see [Lists of hosts and their email sending limits](https://kb.mailpoet.com/article/150-lists-of-hosts-and-their-email-sending-limits).

This error indicates that a sending limit on your email account has been exceeded, so your server has blocked any further emails from being sent. This means you won't be able to send anymore emails from your email account or Sell, until the limit resets.

- By default, we allow you to send up to 300 emails per day from your Sell account, but this limit can be increased in Sell if your email server's sending limit allows for more sends per day.
- Verify your email account sending limits first, then contact [Sell Support](https://support.getbase.com/hc/en-us/requests/new) to increase the number of emails you can send per day from Sell.
- We strongly recommend increasing each user's sending limit in Sell no more than 1,000 emails per day.

|  |  |  |
| --- | --- | --- |
|  | **What does that mean?** | **What can I do about it?** |
| Possibility #1 | You've sent more email messages than your email host allows. Exceeding your email (per day) sending limit means you won't be able to send anymore emails from your email client or from Sell, until the 24-hour rolling limit resets. | Solution: Wait some time then try to send the email message again. |
| Possibility #2 | You've sent too many emails at one time. Every email host has an email sending rate limit that defines how many email messages can be sent at one time.  For example, if your email host's rate limit allows 200 emails to be sent at once, but you try sending a bulk email to 400 prospects, you'll exceed your email sending rate limit.  In some cases, this can cause your email account to be blocked and you won't be able to send any kind of email for 24 or more hours. | Solution: Check your email host's sending limits to verify how many email messages you're able to send daily, hourly, and per minute. You can find this information by:  1. Checking your email account settings (outside of Sell). 2. Search the internet for something such as "What is [insert email host] email sending limits?".  If you're sending a bulk email message, try splitting it up into smaller groups. For example, if you're sending an email to 400 recipients, but you can only send 200 emails at once (due to your rate limit), then try splitting it up into a few separate bulk email messages. |
| Possibility #3 | Your email provider has detected your email behavior as potential spamming. These triggers can differ depending on your provider. | Solution: Review your email provider's best practices to ensure that you aren't performing what are considered unusual activities. For example, here's an example from Google: [Best practices for accounts](https://support.google.com/a/answer/1409688?hl=en&ref_topic=28609). If you're not violating best practices, try sending the email message again. |

## Error 003: Recipient's email address is not valid

**What Happened:**We use the email address in the lead or contact profile to send email messages to your leads and contacts. This error indicates that we tried to send your email message, but the lead or contact's email address is not valid.

|  |  |  |
| --- | --- | --- |
|  | **What does that mean?** | **What can I do about it?** |
| Possibility #1 | There's a typo in the lead or contact's email address. | 1. Navigate to the lead or contact card. 2. Click **Edit** (next to lead/contact name). 3. Locate the **Email** field and review the email address to ensure it's correct:  - No extra characters - No extra spaces - No misspellings - Only one email address is listed in this field |
| Possibility #2 | The person's email address has changed and/or is no longer in use. | Solution:  1. Try contacting the recipient by phone to request a valid email address. 2. Try [Reach](https://www.zendesk.com/sell/products/reach/) (or your preferred data provider) to uncover this person's valid email address. |