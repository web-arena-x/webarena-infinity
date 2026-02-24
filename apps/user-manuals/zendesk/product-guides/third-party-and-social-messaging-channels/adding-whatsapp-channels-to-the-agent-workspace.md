# Adding WhatsApp channels to the Agent Workspace

Source: https://support.zendesk.com/hc/en-us/articles/4408842821786-Adding-WhatsApp-channels-to-the-Agent-Workspace

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Social Messaging add-on |

Customers without Zendesk Suite must have Support and Chat with the Social Messaging add-on to use this feature.

Location:  Admin Center > Channels > Messaging and social >
Messaging

This article describes how you can add WhatsApp social messaging channels to the Zendesk
Agent Workspace. WhatsApp is a popular chat and voice messaging app with more than 2.78
billion users in over 180 countries. WhatsApp usage-based charges may apply. See the [WhatsApp pricing page](https://developers.facebook.com/docs/whatsapp/pricing) for more information.

After you add your WhatsApp number for messaging, you will no longer be able to use that
number to receive calls in WhatsApp.

This article contains the following sections:

- [Understanding the requirements and impacts of adding a WhatsApp channel](#topic_epp_lqt_hnb)
- [Adding a WhatsApp channel](#topic_vvb_zqt_hnb)
- [Editing your WhatsApp business profile](#topic_mvs_fvk_55b)
- [Next steps](#topic_ptn_lqn_1mb)

## Understanding the requirements and impacts of adding a WhatsApp channel

Before adding a WhatsApp channel, make sure you meet and understand the following
requirements and impacts:

- You can connect multiple WhatsApp numbers to your Zendesk account. WhatsApp Business
  Accounts are limited to 20 numbers by default. To connect more than 20 numbers, you can
  connect multiple WhatsApp Business Accounts to a single Zendesk account.
- Once you connect your phone number with WhatsApp Business API, you will no longer be
  able to use that phone number to receive calls in WhatsApp (Meta limitation).
- You need to have a Meta Business Manager that belongs to your own business.
- The person who is connecting the phone number must be an Admin within their own Meta
  Business Manager (Meta requirement). If you are unable to access the existing Meta
  Business Manager, you must create one, which can be done as part of the setup flow. See
  [Adding a WhatsApp channel](#topic_vvb_zqt_hnb).
- The phone number used needs to be able to receive international phone calls/SMS (Meta
  requirement). See [Meta's documentation](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) for more information. If
  you decide to use a Zendesk phone number, you will need to disable IVR and voicemail to
  complete the self-service process. After the phone number is connected to the WhatsApp
  Business API you can reconnect the Zendesk numbers in Zendesk.

  If your phone
  number is currently in use with the WhatsApp for Business mobile app, follow Meta's
  [process](https://developers.facebook.com/docs/whatsapp/on-premises/get-started/migrate-existing-whatsapp-number-to-a-business-account) to remove the account before following
  Zendesk's instructions below.

  Note: A phone number can't be connected with the
  WhatsApp for Business mobile app and the WhatsApp Business API at the same time (Meta
  limitation).
- The display name needs to match your business name/branding, otherwise, WhatsApp will
  reject it. See Meta's [WhatsApp documentation](https://developers.facebook.com/docs/whatsapp/guides/display-name) for more information.
- If you connected your phone number with another Business Solutions Provider (BSP), you
  can migrate it to Zendesk. See [Migrating WhatsApp numbers](https://support.zendesk.com/hc/en-us/articles/6586365564826).
- If you used the WhatsApp Business API to connect your phone number, you can still use
  it with WhatsApp for Small Business or any WhatsApp app on a mobile device. To do so,
  you must delete the WhatApp Business API integration and [disable the 2FA attached to the number](https://developers.facebook.com/docs/whatsapp/on-premises/reference/settings/two-step-verification#resetting-verification-code-in-whatsapp-manager), then
  manually [delete the number from your WhatsApp Business
  Account](https://developers.facebook.com/docs/whatsapp/phone-numbers/#delete-phone-number-from-a-waba). A few minutes after doing so, you will be able to use the phone number
  with the WhatsApp standard app.
- Due to limitations with the Meta API, the status for the WhatsApp number is not
  customizable. WhatsApp users will see the standard status message "Hey there! I am using
  WhatsApp" for your WhatsApp number.
- WhatsApp group messages are not supported by the Zendesk WhatsApp channel.

## Adding a WhatsApp channel

To support WhatsApp social messages in the Zendesk Agent Workspace, you can add one or more
WhatsApp channels to Admin Center. You must be an administrator to add WhatsApp channels.
For more information about how to find the information required to add a WhatsApp channel,
see [Editing your WhatsApp business
profile](#topic_mvs_fvk_55b).

Important: If your WhatsApp business account hasn't been approved, you will only
be able to add one WhatsApp channel. This channel will be restricted and only allow you to
message a maximum of 10 users. Once your WhatsApp business account is approved, this
messaging restriction will be lifted and you will be able to add additional WhatsApp
channels using the self-service flow.

Topics in this section include:

- [Starting the setup flow](#topic_ery_fcv_hnb)
- [Finishing up](#topic_brq_sbv_hnb)

The following video takes you through the flow for adding WhatsApp.

WhatsApp Zendesk Self-Serve (2:37)

### Starting the setup flow

Follow the instructions in this section to use the self-service process for adding a
WhatsApp channel. If your WhatsApp business account has not been verified, you can only go
through the flow once. Adding additional numbers can only be done once the WhatsApp
business account has been verified.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wa_ss_flow2.png)

**To add a WhatsApp channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click **Add channel** and select **WhatsApp** from the drop-down.
3. Click **Continue with WhatsApp** to open the WhatsApp setup flow.

   The set-up flow
   will ask you for the following information. Follow the instructions in the flow to add
   this information.

   | Action | Description |
   | --- | --- |
   | Authenticate to your Facebook profile | This is your profile that's linked to your company's Meta Business Manager. You can **Continue** with the existing profile or sign in to another account. |
   | Provide permission to share your WhatsApp business account and phone number with Zendesk. | Zendesk needs this permission to host the number and connect it to the Agent Workspace. |
   | Select a Meta Business Manager for your WhatsApp number. | You can select an existing Business Manager or create a new one. |
   | Select the business account you want to share with Zendesk. | You can select an existing WhatsApp Business Account or create a new one. If you already connected a number via your Zendesk account, we recommend that you select the existing WhatsApp Business Account to add additional phone numbers. In order to know the limit of phone numbers per business, see Meta's [documentation](https://developers.facebook.com/docs/whatsapp/overview/business-accounts/#limitations). |
   | Set up your business profile | See [Editing your WhatsApp business profile](#topic_mvs_fvk_55b) for the type of information you need to provide in the profile. |
   | Set up your phone number | If you don't already have a phone number set up, add a phone number and verify it.  If the business account you selected already has a phone number you want to use, click **Cancel** to skip this part. |
4. When you've finished the setup flow, click **Done**.
5. From the drop-down in the Admin Center channel configuration, select the number you’d
   like to activate and click **Next**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wa_ss_ac_pick_number.png)

   If the number is dimmed and marked
   (pending) you will need to [complete your Meta Business Manager’s
   verification](https://www.facebook.com/business/help/2058515294227817?id=180505742745347) and wait for the phone number display name to be approved. Once
   you receive an email from Meta that your business account and display name have been
   approved, [restart the setup flow](#topic_ery_fcv_hnb)
   and follow the instructions to finish connecting your phone number.
6. Assign a name to the new WhatsApp channel you are connecting, then click **Add
   channel**.

   Use a name that makes it easy to identify the channel in the
   **Channels** list.

   Adding the channel may take up to 5 minutes as Zendesk sets
   up hosting for your new number. When the channel connects successfully, a **Channel
   added** message appears.
7. You host and own your [WhatsApp Business Account](https://business.facebook.com/wa/manage/phone-numbers/) through your Meta Business Manager.
   From there, you will be able to monitor the display name, the messages usages, your
   quality rating, etc.

Once this is done, you can access your WhatsApp Business Account Manager through your own
[Facebook Business Manager](https://business.facebook.com/settings/). In Facebook Business Manager, click **Accounts >
WhatsApp accounts**, locate the WhatsApp Business Account, then open **Settings >
WhatsApp Manager.** From there, you can monitor the display name, the message usage,
your quality rating, and the like.

### Finishing up

To successfully spin up your WhatsApp number there are a few things to double
check:

- **Has your Meta Business Manager been [verified](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)?** Before your WhatsApp business
  account can be approved, your Business Manager will need to be approved as outlined
  above.
- **Are you eligible to use WhatsApp per [WhatsApp’s Commerce Policy](https://www.whatsapp.com/legal/commerce-policy/) and has your WhatsApp business
  account been approved?** This takes approximately 1-2 weeks. If you fall in the list
  of prohibited businesses, you will unfortunately not be able to use this channel.
- **Does your selected display name align with [WhatsApp’s guidelines](https://developers.facebook.com/docs/whatsapp/guides/display-name/)?** If you don’t select
  a display name that falls within WhatsApp’s guidelines, you will end up delaying the
  launch of your WhatsApp number.

If
you don't go through Business Verification, you will have restricted access. Restricted
access includes:

- Unlimited customer-initiated conversations.
- The ability to send notifications to 250 unique customers in a rolling 24-hour
  period.
- The ability to register up to two phone numbers.
- You cannot apply for an [Official Business Account](https://developers.facebook.com/docs/whatsapp/overview/business-accounts#official-business-account) until the Meta
  Business Manager verification is complete.

You can go through the verification at any time to lift these restrictions.

## Editing your WhatsApp business profile

When you add a WhatsApp channel in Admin Center, you can include business profile
details for your account. These details are visible to your customers from WhatsApp.

Business profile details include:

- **Channel name**: Enter a unique name to identify the channel.
- **Brand** (for accounts with multiple brands): Select a brand to associate
  with the channel.
- **Profile picture**: Upload a profile picture. This picture appears in
  your WhatsApp business profile and in WhatsApp conversations.
- **Description**: Enter a brief description of your business. This
  information will appear at the top of your WhatsApp business profile.
- Enter more information about your business, including your business
  **Address**, **Email**, **Industry**, and **Websites**.

**To add a WhatsApp business profile**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Locate the WhatsApp channel you want to edit and click to open it.
3. Enter the business profile details about your WhatsApp channel.
4. When you've finished adding these details, click **Save**.

## Next steps

After you've configured your WhatsApp channel and edited your business profile, you can:

- [Enable access for agents](https://support.zendesk.com/hc/en-us/articles/6073485578010) who will participate in social
  messaging conversations.
- Configure [automatic responses](https://support.zendesk.com/hc/en-us/articles/4408838007578) to messages.
- [Add the Message Us button](https://support.zendesk.com/hc/en-us/articles/4408846651290) to your website, mobile app, or help
  center to help users discover and connect to your WhatsApp channel.
- Request an [Official Business Account](https://developers.facebook.com/docs/whatsapp/overview/business-accounts#official-business-account).
- [Bypass the WhatsApp 24-hour rule](https://support.zendesk.com/hc/en-us/articles/5869718332954).