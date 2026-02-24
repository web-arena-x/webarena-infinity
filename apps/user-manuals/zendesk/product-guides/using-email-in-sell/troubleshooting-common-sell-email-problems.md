# Troubleshooting common Sell email problems

Source: https://support.zendesk.com/hc/en-us/articles/4408846892442-Troubleshooting-common-Sell-email-problems

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

As described in [Connecting your email with Zendesk Sell](https://support.zendesk.com/hc/en-us/articles/360041032054), with the Sell email integration you can sync with an external email system such as Google Mail and Microsoft Office 365. Setting up an integration means that email messages in your external email server are mirrored into Sell and paired with your leads and contacts.

When you set up this integration, you may encounter problems and need to do some troubleshooting to resolve your issues. This article provides an overview of what you may encounter and where to find troubleshooting information.

This article covers the following topics:

- [Email connection requirements and limitations](#topic_qvc_svl_crb)
- [Common email connection issues](#topic_d3k_svl_crb)
- [Common email delivery issues](#topic_lk5_svl_crb)
- [Email not syncing or missing email messages](#topic_ecf_tvl_crb)
- [Disassociated emails reattaching to deal threads](#topic_lpc_rrg_zrb)

Related article:

- [Troubleshooting emails that are missing or not syncing](https://support.zendesk.com/hc/en-us/articles/4408844117402)

## Email connection requirements and limitations

Sell provides support for Google Mail and Microsoft Office 365, meaning that when you follow instructions to set up your email integration in Sell, you should have no issues with syncing your email and using the integration. However, if you’re using a different email system, you should be aware of the following requirements.

- You need a valid third party Secure Sockets Layer (SSL) or Transport Layer Security (TLS) certificate. TLS is a predecessor of the SSL certificate, now deprecated, that may still be in use.
- You need to know your IMAP and SMTP settings. If you have a different protocol enabled (for example, POP3, which is not supported) you'll still need to enable IMAP and SMTP to connect your email to Sell. See [Email troubleshooting: SMTP and IMAP Settings](https://support.zendesk.com/hc/en-us/articles/360041032094).
- Sell only supports OAuth2 for Gmail and Microsoft Office 365 for 2-step verification. If you have any form of 2-step verification enabled on your email (and you don't use Gmail/Microsoft Office 365), try checking to see if you can create an app-specific password.
- Each Sell user can only integrate with one email address. You also have the option of using a BCC email address to send to and attach email messages from email addresses that are not connected to Sell. See [Using the BCC email address for external email messages](https://support.zendesk.com/hc/en-us/articles/360041032234).

## Common email connection issues

The errors that you might encounter when integrating your external email with Sell are usually related to the SSL (or TLS) certificate and the IMAP and SMTP settings. For information about the errors you might encounter, see [Email troubleshooting: Email integration errors](https://support.zendesk.com/hc/en-us/articles/4408829007514). If you see the error message, **Authentication: Cannot Authenticate**, when trying to integrate your Office 365 email with Sell, see [When I try to "Sign in with Microsoft" I am getting a "Cannot Authenticate" error message](https://support.zendesk.com/hc/en-us/articles/4408823174042).

## Common email delivery issues

After you’ve successfully set up an email connection, you might encounter an error related to the delivery of your messages. For example, the recipient (a lead or contact) not receiving the message you sent. For more information about these errors, see [Email troubleshooting: Email delivery errors](https://support.zendesk.com/hc/en-us/articles/4408838259226).

## Email not syncing or missing email messages

If you’re expecting to see email messages in your Sell account that you can't find, there may be a fairly simple reason that has nothing to do with configuring your email integration. For example, as Sell only synchronizes the inbox and outbox folders, any emails stored in subfolders will not sync (see [Troubleshooting emails that are missing or not syncing](https://support.zendesk.com/hc/en-us/articles/4408844117402)).

If an email has more than 100 recipients, then Sell cannot sync the emails. This also applies for emails that have more than 100 BCC contacts (whether these contacts are part of Sell or not).

## Disassociated emails reattaching to deal threads

Currently, if you disassociate an email from a deal, the next reply in that email chain will re-associate the message back to the deal you've just removed it from. This is a known issue. For more information about adding and removing email messages, see [Adding and removing email messages from lead, contact, and deal cards](https://support.zendesk.com/hc/en-us/articles/4408821860634).