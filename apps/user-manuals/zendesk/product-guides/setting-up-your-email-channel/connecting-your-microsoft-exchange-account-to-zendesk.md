# Connecting your Microsoft Exchange account to Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/8994395472922-Connecting-your-Microsoft-Exchange-account-to-Zendesk

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Connect your Microsoft Exchange account to automatically convert emails into tickets and manage them through your support system. Ensure the Exchange account is not used elsewhere and test in a sandbox first. Manage connections by checking status, disconnecting, or reconnecting as needed. Troubleshoot permissions and avoid duplicate emails by following best practices. Consider FAQs for switching methods and handling shared mailboxes.

As described in [About the Microsoft Exchange connector](https://support.zendesk.com/hc/en-us/articles/8979947090586), you can connect your non-Zendesk email servers, based on Microsoft Exchange, directly to your Zendesk Support account. Once connected, the connector uses an Exchange API to fetch email from your Exchange inbox and automatically convert email messages to tickets. The API is also leveraged to deliver outbound email from Zendesk to your Exchange mailbox.

The Zendesk Exchange connector is compatible with Microsoft Exchange Online only.
Exchange Server on-premises versions are not supported.

You must be a Zendesk administrator to connect your Exchange account to Zendesk. Zendesk recommends testing this feature in your Zendesk [sandbox environment](https://support.zendesk.com/hc/en-us/articles/6150628316058) before using it in production.

This article includes the following topics:

- [Important considerations](#topic_onl_frc_mgc)
- [Connecting your Exchange account to Zendesk](#topic_bpc_xzz_m2c)
- [Managing your Exchange connections](#topic_ofg_gb1_n2c)
- [Troubleshooting your connection](#topic_jlg_pgk_42c)
- [Frequently asked questions](#topic_wjg_m31_p2c)

## Important considerations

- Do not make a newly added address the default support address until you have verified that it is functioning correctly. Doing so will risk locking yourself out of your account if you can't receive password reset and access emails.
- Ensure the Exchange mailbox isn't used by any other connection method (such as email forwarding) or any agent or end user in your Zendesk account.
- See [About the Microsoft Exchange Connector](https://support.zendesk.com/hc/en-us/articles/8979947090586)
 for technical details, requirements, and limitations.

## Connecting your Exchange account to Zendesk

When you connect your Exchange account to Zendesk, make sure you sign in to the Exchange account you want to connect to. If you sign in to a different Exchange account in the same browser as your instance of Zendesk Support, you will connect to the wrong account.

**To connect your Exchange account to Zendesk**

1. Sign in to the Exchange account you want to connect to Zendesk.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
3. Click **Manage support addresses**.
4. Click **Add address**, then click **Connect external address**.
5. If you have multiple brands, select the brand for the email address from the drop-down menu.
6. Select **Microsoft Exchange connector**.
7. You have the option to **Create tickets from last 300 emails**. When selected, the 300 most recent emails in your account are imported as tickets, regardless of whether they've been read. The import can take up to 15 minutes to complete. Zendesk suppresses ticket triggers at creation for those 300 tickets.

   If you don't want to import pre-existing emails as tickets, deselect **Create tickets from last 300 emails**.
8. Click **Next**.
9. Click **Accept** to approve access to the email account.

   You may need to sign in to Microsoft using your account credentials for that email address.
10. Click **Done**.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/exchange_connector_finish.png)

Your Zendesk Support account is connected to your Microsoft account. If you want to connect to multiple accounts, repeat these steps.

## Managing your Exchange connections

In Admin Center, admins can check the status of their Exchange connections, as well as disconnect or reconnect Exchange accounts as needed.

### Checking the status of a connection

Checking the connection status of your Exchange account helps you confirm the setup was successful and emails are being received from Exchange. Properly configured connections show a Verified label in the Status column. If the account isn't connected, you'll see a Failed message in the Status column, and can access a details page to learn more.

**To check the status of an Exchange connection**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. Click **Manage support addresses**.
3. Locate the Exchange connection by expanding the name of the brand associated with the connection.

   Exchange connections display "MS Exchange connector" in the Connection type column.
4. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the address, then click **View details** to view the connection status.

### Disconnecting an Exchange account

You can disconnect an Exchange account anytime to stop importing email from that inbox.

If you want to disconnect the inbox tied to your [default support address](https://support.zendesk.com/hc/en-us/articles/5279521301914#topic_btc_h1f_bwb), you must set a different default support address before continuing.

**To disconnect an Exchange account**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. Click **Manage support addresses**.
3. Locate the Exchange connection by expanding the name of the brand associated with the connection.

   Exchange connections display "MS Exchange connector" in the Connection type column.
4. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the address, then click **Delete**.

   If you don’t see the Delete option, it means the connection is set up as the default connection. You must set a different [default support address](https://support.zendesk.com/hc/en-us/articles/5279521301914#topic_btc_h1f_bwb) before continuing.
5. Confirm you want to delete the connection by clicking **Delete address**.

### Reconnecting an Exchange account

If you see a warning in the Support addresses section indicating that your Exchange account has been disconnected, you can restore the connection.

When a support address is disconnected, outgoing email is not sent from that address, and Zendesk doesn’t fall back to other connections you may have set up.

**To reconnect an Exchange account**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. Click **Manage support addresses**.
3. Locate the Exchange connection by expanding the name of the brand associated with the connection.

   Exchange connections display "MS Exchange connector" in the Connection type column.
4. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the address, then click **Reconnect**.

   If the account has disappeared from the Support addresses list, try [reconnecting it as a new connection](#topic_bpc_xzz_m2c) or contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).

Once re-authorized, the connector will restart fetching any unfetched emails. You should continue to receive all new emails sent to that Exchange account.

## Troubleshooting your connection

- If you see error messages regarding permissions (such as, "Couldn't verify your Microsoft account. Check your permissions and try again"), review the permissions on the Exchange account you’re connecting to Zendesk. The following permissions are required:
 - openid
 - offline\_access
 - email
 - User.Read
 - Mail.Send
 - Mail.ReadWrite
- The Microsoft email address you’re connecting to Zendesk can’t be used by any other connection method, agent, or end user in your Zendesk instance. If the email address is in use, you’ll receive the following message and will be unable to connect: “This email is used by Support and can’t be added. Ensure the email address isn’t already connected or in use by an agent or end user.”

## Frequently asked questions

**How do I switch from email forwarding to using the Exchange connector? If I have existing email channels, what's the best way to convert them to use the Exchange connector? Can I delete the channel and re-add it as an Exchange connector?**

To switch from email forwarding to the Exchange connector, you must first remove all previous connections and configurations associated with the email address you wish to configure in the Exchange connector. Additionally, ensure that email forwarding is turned off on your email server.

**What happens to existing emails in the Exchange mailbox when I connect that mailbox to Zendesk?**

When you [connect your Exchange account to Zendesk](#topic_bpc_xzz_m2c), you have the option to **Create tickets from the last 300 emails**. When selected, the 300 most recent emails in your account are imported as tickets, regardless of whether they've been read. Zendesk suppresses ticket triggers at creation for those 300 tickets. If you don't want to import pre-existing emails as tickets, deselect **Create tickets from last 300 emails**.

**How are duplicate emails managed?**

Duplicate emails are managed by existing deduplication mechanisms, including those that may have reached Zendesk through different methods (for example, once through forwarding and again through the Exchange connector). However, due to the complexity of email protocols, deduplication may not always be possible. For more detailed information about the underlying mechanisms, see [Understanding how incoming emails are matched to tickets](https://support.zendesk.com/hc/en-us/articles/4408887388058#topic_r1f_4gd_v3).

**What happens to emails after they are fetched?**

All emails that are successfully fetched are marked as read and categorized under "Zendesk." These emails can be safely removed; however, Zendesk strongly recommends archiving them instead of deleting them.

**Can I connect to a shared mailbox?**

To connect the Microsoft Exchange Connector to a shared mailbox, you must first convert the shared mailbox into a regular user mailbox. Once converted, you can set a password for it like any other user mailbox. For more information, see the [Exchange Online](https://learn.microsoft.com/en-us/exchange/exchange-online) documentation.