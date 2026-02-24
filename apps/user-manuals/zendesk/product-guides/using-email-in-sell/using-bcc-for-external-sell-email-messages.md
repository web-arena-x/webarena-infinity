# Using BCC for external Sell email messages

Source: https://support.zendesk.com/hc/en-us/articles/4408828858906-Using-BCC-for-external-Sell-email-messages

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

Use the Sell global BCC address if any of the following apply:

- You have not yet connected your external email account with Sell
- You are sending emails from an external email address (i.e. not the email address you are using for your Sell account)
- You are receiving emails from your Sell contacts at an email address that is not the email address you are using for your Sell account

You can add a BCC email address to your outgoing messages or forward email messages to your Sell account using that BCC email address.

This allows you to attach email messages that are sent or received from external email addresses (that are not used in your Sell account) to a contact’s card and to specific deals that you have with a contact.

This article covers the following topics:

- [Using a Bcc email address for contacts](#topic_mnq_pw1_b5b)
- [Using a Bcc email address for deals](#topic_ely_pw1_b5b)
- [Changing the BCC email address](#topic_uj1_2wg_m5b)

Related articles:

- [Sell email resource guide](https://support.zendesk.com/hc/en-us/articles/4627545703322)

## Using a Bcc email address for contacts

On each contact card, there is a global getbase.com BCC email address that is dedicated for contacts in Sell and specific to your Sell account. If you want to add an email message to a contact card in Sell when receiving, sending, or forwarding emails from your external email account, use this global BCC email address.

When you send a message to Sell using a global BCC email address, Sell matches the contact using the contact’s email address in Sell. If their email address doesn’t exist in Sell, then Sell automatically creates a new contact card to attach the email to.

Note: The dedicated BCC email address uses getbase.com because Zendesk Sell was formerly called Base.

The following scenarios outline how to best use the global getbase.com BCC email address:

**Scenario 1: Forwarding an external email (Gmail for example) to a contact card in Sell**

As a sales rep, you're about to take some extended leave from work and you want to handover your client to another sales rep at your company while you're away. Your company uses an external email account through Gmail. However, you want to ensure this email is added to your client's history in Sell, by adding it to the emails on their contact card in Sell.

**To forward an email from your external email address to a contact card in Sell**

1. In your external email composer, click **Forward** (**Fw: Fwd:**) to forward the email message.

   Important: If you forward an email, do not change the subject line or remove the – Forwarded message – details that were automatically added to the content of the email you are forwarding (otherwise the message will not forward to Sell).
2. On the sidebar in Sell, click **Contacts**.
3. Click a contact to access a contact page (any contact will do).
4. Beneath the contact name and details, next to the getbase.com global email address, click the **Copy to Clipboard** icon.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_email_bcc_copy_to_clipboard.png)
5. Paste the getbase.com global email address in the **TO** field of your external email.
6. Click **Send**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_email_bcc_fwd_to_field.png)

**Scenario 2: Sending an email directly from your external email account (Gmail for example).**

As a sales rep you would like to send an email to your new client from your Gmail account. However, you have not yet connected your Gmail account with Sell. As there can be multiple sales reps attending to a single client at your company, it's important that there is a continuous customer record, with everything in one place.

When you send this email to your client, a copy will be BCC'd to the client's contact card in Sell. As they are a new client, their email address details do not yet exist in Sell and there is no contact card for them, so Sell automatically creates a new contact card to attach the email to.

**To send an external email to your customer and a copy of the email to their contact card in Sell**

1. In your external email composer, in the **TO** field, enter your customer's email address (for example, email@sample.com).
2. On the sidebar in Sell, click **Contacts**.
3. Click a contact to access a contact page (any contact will do).
4. Beneath the contact name and details, next to the getbase.com global email address, click the **Copy to Clipboard** icon.
5. In your external email, in the **BCC** field, paste the getbase.com global email address.
6. Click **Send**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_email_bcc_sending_bcc_field.png)

**Scenario 3: An email I sent to my client and my new coworker, with the global email address in BCC, is not visible in Sell.**

As a sales rep, you have invited the new intern on your team to attend an upcoming client meeting with you. To help your intern prepare for the meeting you added them to the email that you sent your client from your external email composer (for example Gmail). You also added the getbase.com global email in BCC so the email would attach to the client's contact card in Sell. However, after you've sent the email, you cannot see it attached to the client's contact card.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_email_bcc_blocklist.png)

Answer - As the intern is your colleague, they have likely been assigned to a blocklist in Sell if you are sharing an account. If an email address is blocklisted in any of the fields, (TO, CC, BCC,) this prevents the email being sent to the getbase.com global email address and the email will not attach to that contact's card in Sell.

Note: To have a colleague's name removed from the blocklist, you must ask your administrator to contact support. As individual users cannot be removed from the blocklist, everyone's email address will be removed from the blocklist on the account.

## Using a Bcc email address for deals

The Bcc email address for deals is not the same as the Bcc email address for contacts. For deals, the deal identifier is also included in the Bcc email address. This means the Bcc address for each deal is unique and if you want to Bcc email messages from an external email account, you must use the deal specific Bcc email address provided on the deal card.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-email-bcc-deal.png)

Note: The unique email address uses getbase.com because Zendesk Sell was formerly called Base.

## Changing the BCC email address

You can change the dedicated BCC email address if you want to by generating a new one.

**To change the dedicated BCC email address**

1. In Sell, on the sidebar, click **Contacts**.
2. Click a contact to open their contact card (any contact will do).
3. On the contact card, next to the global getbase.com BCC email address, click the **Generate new address** icon (located next to the Copy to Clipboard icon). A new address loads automatically

Tip: As a shortcut, you can create a contact in your external email called BCC Sell that uses the getbase.com global email address as its email address. This saves you having to cut and paste the global getbase.com email address every time. However, if you change the dedicated global getbase.com email address in Sell, you must update the email address of your BCC Sell contact in your external email.