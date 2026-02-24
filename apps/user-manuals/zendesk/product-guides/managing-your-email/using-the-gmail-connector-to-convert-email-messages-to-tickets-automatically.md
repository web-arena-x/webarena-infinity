# Using the Gmail connector to convert email messages to tickets automatically

Source: https://support.zendesk.com/hc/en-us/articles/4408835030426-Using-the-Gmail-connector-to-convert-email-messages-to-tickets-automatically

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Automatically convert Gmail emails into tickets by connecting your Gmail account. This feature checks for new emails every minute, sending ticket notifications from your Gmail. Be aware of Google's sending limits and set up SPF or DKIM for email authorization. You can manage multiple Gmail connections, import recent emails, and disconnect or reconnect accounts as needed.

Important: Enabling this functionality leverages Google API
Services. Zendesk’s use and transfer to any other app of information
received through the Google API Services connecting Zendesk Support
to your Gmail accounts will adhere to Google's Limited Use
Requirements described in the [Google API Services: User
Data Policy](https://developers.google.com/terms/api-services-user-data-policy).

You can import email from one or more Gmail inboxes and automatically convert
email messages to tickets. Zendesk Support will check for new email in your
Gmail inbox every minute. Only new, unread email messages in the inbox will
be converted into tickets.

When **Send email via Gmail** is turned on, ticket notifications will be sent
from your Gmail using Google mail servers instead of Zendesk mail servers.
You need to [set up SPF or DKIM](https://support.zendesk.com/hc/en-us/articles/4408832543770#topic_oct_kvr_42b) to
authorize Zendesk Support to send email on your behalf (in the event that
traffic needs to be sent from Zendesk servers for any reason). Notifications
will be in your Sent folder in your Gmail. It's important to note that if
you use the **Send email via Gmail** feature, you can't use real
attachments (attachments in emails instead of links). If you have [attachments turned on](https://support.zendesk.com/hc/en-us/articles/4408832757146), email
notifications with real attachments are sent from Zendesk mail servers
instead.

You can connect to multiple Gmail accounts. When you do, each Gmail address is
automatically added as a support address. You don't need to add it manually.
When you set up the connection, you can choose to create tickets from the
last 300 emails or not create any tickets. When you add a new Gmail address,
Zendesk will import unread emails from the inbox that arrived within the
last hour.

Before you connect to your Gmail account, make sure you sign in to the Gmail
account you want to connect to. If you sign in to a different Gmail account
in the same browser as your instance of Zendesk Support, you will connect to
the wrong account.

This article includes these topics:

- [About Google sending limits](#topic_gkv_qzg_v5)
- [Connecting to your Gmail account](#topic_zdl_rzg_v5)
- [Managing Gmail connections](#topic_oww_k1h_v5)

## About Google sending limits

Google limits daily sending to 500 messages for Gmail or 2000 for Google Apps. Unless you're a
small business with low traffic, we recommend Google Apps for this
integration. Check Google's support site for additional
information.

If you approach the limit, based on the number of email notifications sent through your Gmail,
you will receive a warning, and notifications will temporarily be
sent from Zendesk mail servers instead of Google mail servers. If
you continue to have this issue, you should consider deselecting the
**Send email via Gmail** option and setting up forwarding
and an SPF record to send notifications from Zendesk mail servers.
Deselecting this option will make the Zendesk verification code you
need to set up SPF visible. See [Forwarding incoming email from your existing email address to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408886828698).

## Connecting to your Gmail account

You can link one or more Gmail accounts. When you do, all new, unread email messages in the inbox
are imported and converted to tickets. If you want to connect to
multiple accounts, repeat these steps.

**To connect to your Gmail account**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. Click **Manage support addresses**.
3. Click **Add address**, then click **Connect external
   address**.
4. If you have multiple brands, select the brand for which
   you're connecting your Gmail account.
5. Select **Gmail connector**.
6. You have the option to **Create tickets from last 300
   emails**. When selected, the 300 most recent
   emails in your account are imported as tickets,
   regardless of whether they've been read. Zendesk
   suppresses ticket triggers at creation for those 300
   tickets.

   If you don't want to import
   pre-existing emails as tickets, deselect **Create
   tickets from last 300 emails**. Unread emails
   that arrived in the inbox within the last hour
   will be imported.
7. Click **Next**.
8. If requested, sign in to your Gmail account, then click
   **Continue**.
9. Follow the on-screen prompts to connect to your Gmail
   account.

   Be sure to select **Read, compose, and
   send emails from your Gmail
   account**.

   Your Zendesk Support is
   connected to your Gmail account. Zendesk Support
   will check for new email in your Gmail inbox every
   minute and convert email messages to tickets.
   Ticket notifications will be sent from your Gmail
   account. The `Zendesk` label is
   added to all emails that have been imported as
   tickets.

## Managing Gmail connections

You can disconnect a Gmail inbox at any time if you want to stop
importing email from that inbox.

Note: If you want to disconnect the inbox tied to your [default
Support address](https://support.zendesk.com/hc/en-us/articles/5279521301914#topic_btc_h1f_bwb), you
need to create a new default Support address before continuing.

**To disconnect a Gmail account**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. Click **Manage support addresses**.
3. Locate the Gmail account. Any support address connected
   to a Gmail account indicates that it has the
   connection type of **Gmail connector**.
4. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the support
   address, then click **Disconnect**.
5. Confirm you want to delete the connection by clicking
   **Delete address**.

If your Gmail account entry displays a warning saying it has been
disconnected, you can reestablish the connection. In this case, if
you reconnect, any emails that have already been imported will
*not* be imported again as duplicate tickets.

**To reconnect a disconnected Gmail account**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. Click **Manage support addresses**.
3. Locate the Gmail account. Any support address connected
   to a Gmail account indicates that it has the
   connection type of **Gmail connector**.
4. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the support
   address, then click **Reconnect**.

   If the Gmail
   account has disappeared from the Support addresses
   list, reconnect it using the instructions in [Connecting to your Gmail account](#topic_zdl_rzg_v5).

Once re-authorized, you should continue to receive all emails sent to
that Gmail account.