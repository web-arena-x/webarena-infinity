# Troubleshooting Sell emails that are missing or not syncing

Source: https://support.zendesk.com/hc/en-us/articles/4408844117402-Troubleshooting-Sell-emails-that-are-missing-or-not-syncing

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

When you set up an [email integration in Sell](https://support.zendesk.com/hc/en-us/articles/4408821242266), the email messages from your external email account are synced with Sell and you’ll see those email messages in the Communications Center and also attached to relevant leads, contacts, and deals.

However, if you discover that some of the email messages are missing or have not synced with Sell, the following situations may apply.

This article covers the following topics

- [First steps](#sell_email_troubleshooting_emails_that_are_missing_or_not_syncing__h_01F128EYVK5JZA0A332273V9GV)
- [Email address has not been added to the lead or contact](#sell_email_troubleshooting_emails_that_are_missing_or_not_syncing__h_01EPC3773PHB1JEDM49YEQYTTD)
- [The email sender is on your blocklist](#sell_email_troubleshooting_emails_that_are_missing_or_not_syncing__h_01EPC37FPZFKT8K603K2SR6B2S)
- [Email not syncing due to permissions](#ariaid-title9)
- [An email address is being used by more than one person](#sell_email_troubleshooting_emails_that_are_missing_or_not_syncing__h_01EPC37R5DMAVKGJY4KTASMM4B)
- [An email message was deleted outside of Sell](#sell_email_troubleshooting_emails_that_are_missing_or_not_syncing__h_01EPC382MTX2X12Z56J96PG9P5)
- [Email messages are not displayed in the activity feed](#sell_email_troubleshooting_emails_that_are_missing_or_not_syncing__h_01EPC38AFCS6X00D93GM3XCYAC)
- [Emails in subfolders not syncing](#topic_ejx_d3l_crb)

Related article

- [Troubleshooting common email problems in Sell](https://support.zendesk.com/hc/en-us/articles/4408846892442)

## First steps

If you cannot find an email in your Sell account try the following options:

- Search for the email address in the global search bar.

 Searching across the entire account helps to catch duplicates. If you have an email address listed twice in your account, remove the duplicate as the email conversation will only appear in one location.
- Check the “To” and “From” recipient information.

 First, verify that the spelling of the email address is correct. Next, verify that you are using the email address that was integrated into your Sell settings, to send the email. If you ask the Zendesk customer support team to help troubleshoot this issue, they will also ask you for this information.

## Email address has not been added to the lead or contact

When a lead or contact’s profile contains an email address and the email messages synced from your external email account contain that same address, then their email messages will appear in Sell. If they don’t appear, check to make sure that their email address has been added to their profile. If their email address is included in their profile, check to see if the missing email messages contain the same email address that is in their profile. If not, the missing email messages may be in the Untracked Emails tab in the Communication Center (see [Adding an untracked email address as a lead or contact](https://support.zendesk.com/hc/en-us/articles/4408821622426)).

Another way to handle multiple email addresses for a lead or contact is to create a custom field for the alternate email address. For example, if you create a custom field called Email2 you can use it to store the additional email address. If the custom field type is set to Email, it is tracked in Sell (see [Creating and managing custom fields](https://support.zendesk.com/hc/en-us/articles/4408838289562)).

## The email sender is on your blocklist

The blocklist feature in Sell allows you to prevent Sell from tracking email conversations with specific leads and contacts. Check to see if the email sender has been added to the blocklist. If so, you can unblock their email messages and they will appear in Sell as expected (see [Blocklisting leads and contacts to prevent tracking of email conversations](https://support.zendesk.com/hc/en-us/articles/4408824429978)).

Note: By default, the email conversations that you have with your coworkers (the other users in your Sell account) are not tracked – they are automatically blocklisted.

## Email not syncing due to permissions

If you don't have permission to see specific leads or contacts, the emails for those leads and contacts will not sync. To resolve this you must ask the owner of those leads and contacts to grant you permission.

## An email address is being used by more than one person

If more than one lead or contact share the same email address, email messages will not sync to both records. Sell only syncs email messages to the first record that was created.

You can check to see if there are duplicated email addresses by searching for the email address using global search (see [Searching the data in your Sell account](https://support.zendesk.com/hc/en-us/articles/4408832124314)). All leads or contacts that have the same email address in their profile will be listed in the search results.

## An email message was deleted outside of Sell

The Sell email integration mirrors your external email account, meaning that if an email is deleted on your email server, then it will also be deleted in Sell.

If you can’t find an email in Sell, check your external email client to see if it was deleted there.

## Email messages are not displayed in the activity feed

On a lead, contact, or deal card, you can filter what is displayed in the activity feed. If your email messages are not displayed, it may be because the Emails activity type has been deselected.

![Sell email activity feed](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-card-activity-feed2.png)

## Emails in subfolders not syncing

Emails stored in subfolders will not sync as Sell only synchronizes the inbox and outbox folders.