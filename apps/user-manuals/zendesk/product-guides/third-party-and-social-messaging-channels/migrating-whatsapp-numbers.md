# Migrating WhatsApp numbers

Source: https://support.zendesk.com/hc/en-us/articles/6586365564826-Migrating-WhatsApp-numbers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Location:  Fastpath: Admin Center > Channels > Messaging and social >
Messaging

You can migrate your WhatsApp numbers from one WhatsApp Business Account (WABA) to
another. This article describes how to migrate your WhatsApp numbers if you're moving to
Zendesk from a different Business Solution Provider (BSP), or if you are moving from
Zendesk to another Business Solution Provider.

The BSP-to-Zendesk migration process described in this article is also helpful
if you connected your WhatsApp numbers before Zendesk introduced the WhatsApp
self-service flow in Admin Center and you'd like more visibility into your WhatsApp
numbers. The process grants you ownership over your WABA, including access to the
insights tool, message templates and number quality rating.

Migrating your numbers carries over the number’s display name, quality rating,
messaging limit, official business account status, and any high-quality message
templates that had previously been approved.

This article covers the following topics:

- [Before you start](#topic_x5z_pqj_1cc)
- [Migrating a WhatsApp number from a different BSP to Zendesk](#topic_wd4_vqj_1cc)
- [Migrating a WhatsApp number from Zendesk to a different BSP](#topic_rsd_drj_1cc)
- [Moving a WhatsApp number from a Zendesk-hosted WABA to a self-hosted WABA](#topic_wyc_rrj_1cc)
- [Troubleshooting your migration](#topic_vyc_2sj_1cc)

## Before you start

Before you begin migrating WhatsApp numbers, review the following sections to learn
about terminology and requirements related to the migration process:

### Key terminology

Understanding the following terms and concepts will help your migration
process run more smoothly.

- **Meta Business Manager (FBM)** is a central space to manage
  your business on the Meta platform, separate from your personal Facebook
  profile. You can access your FBM by going to <https://business.facebook.com/>.
- **WhatsApp Business Account (WABA)** is similar to a folder in
  your Facebook Business Manager where the telephone number you added as a
  WhatsApp Messaging channel to your Zendesk subdomain resides
- **Zendesk-hosted WhatsApp Business Account** is a WABA hosted
  by Zendesk. Customers with WhatsApp numbers in a Zendesk WABA do not have
  access to a WABA through their FBM. Applies to existing Zendesk customers
  only.
- **Self-hosted WhatsApp Business Account** is a WABA owned by
  the customer and accessed through their Meta Business Manager. Customers add
  their telephone number as a WhatsApp messaging channel to their Zendesk
  subdomain through the [self-service process](adding-whatsapp-channels-to-the-agent-workspace.md).
  Additionally, this WABA is shared with Zendesk.
- **Business Solution Provider (BSP)** is a third-party company
  authorized by WhatsApp to offer API access and support to businesses. BSPs
  act as intermediaries, making it possible for businesses to use the WhatsApp
  Business API. For example, when you add a number as a WhatsApp messaging
  channel in your Zendesk subdomain, Zendesk becomes your BSP.

  Note: Phone numbers added as a WhatsApp Messaging Channel in your Zendesk subdomain are numbers that
  have been registered with the WhatsApp Business API platform.

### Requirements

Ensure you understand the following requirements before you begin your
migration.

- You'll need access to the phone number that you are moving, as
  you’ll need to be able to receive an SMS or a voice call with a 6-digit
  verification pin (required by Meta).
- The phone number must be able to receive international phone calls
  and SMS messages.
- The phone number must not have any IVR (interactive voice
  response) system enabled at the time of the procedure.
- You must have admin privileges to your Zendesk instance.
- You must have admin privileges to your Meta Business Manager.

## Migrating a WhatsApp number from a different BSP to Zendesk

Complete the following process to migrate a WhatsApp number that is in use
with another Business Solution Provider to Zendesk.

**To migrate WhatsApp numbers to Zendesk**

1. Submit a request with your current Business Solution Provider to
   deactivate the two-factor authentication PIN for the number you want to migrate.
   You can't fully migrate a number until this step is complete.
2. Add a WhatsApp channel using the self-service process described in
   [Adding WhatsApp channels to the Agent
   Workspace](https://support.zendesk.com/hc/en-us/articles/4408842821786).

During this process, use the same Meta Business Manager ID and display name
used in the WhatsApp configuration with your current BSP. Using a different Meta
Business Manager ID or display name will result in an error and you won't be able to
complete the migration process.

If you have questions about this process, contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).

## Migrating a WhatsApp number from Zendesk to a different BSP

Complete the following process to migrate a WhatsApp number from Zendesk to
a different BSP.

**To migrate a WhatsApp number from Zendesk to another BSP**

1. In your WhatsApp account, click the number you want to migrate, then click
   **Turn off two-step verification**.
2. Follow your new BSP’s steps for connecting the WhatsApp number with the new
   BSP.

## Moving a WhatsApp number from a Zendesk-hosted WABA to a self-hosted WABA

Complete the following process to migrate a WhatsApp number from a
Zendesk-hosted WABA to a WABA hosted in your Meta Business Manager. Your WhatsApp
number might be temporarily unavailable during this process.

1. Contact [Zendesk customer support](https://support.zendesk.com/hc/en-us/articles/4408843597850) and request
   removal of two-factor authentication (2FA) for the WhatsApp number that you want
   to move to a WABA hosted within your Meta Business Manager.
2. After you receive confirmation from Zendesk support that the 2FA has
   been disabled, remove the integration from your Zendesk instance. This will take
   the number offline. To remove the integration, in Admin center, click the
   options menu next to your WhatsApp number, then select **Delete**.
3. Follow the instructions in [Adding WhatsApp channels to the Agent
   Workspace](https://support.zendesk.com/hc/en-us/articles/4408842821786).

Note: Ensure you use the same Meta Business Manager ID you provided to Zendesk when requesting the
original WhatsApp Business Account to be created through the assisted process.
If you provide a different Meta Business Manager ID during the flow, you'll
receive an error and won’t be able to complete the migration process.Also, you
must use the same display name for the WhatsApp number when following the
self-service process.

## Troubleshooting your migration

Use the following information to help you troubleshoot any problems with your number
migration.

- If you request the WhatsApp verification code several times within a
  short time period, this might lead to the number being restricted. For that
  reason, we recommend only attempting three times to receive the code. If you are
  not able to successfully receive the code after three attempts, wait
  approximately 8 hours and then try again. If the problem persists, [check you meet the
  requirements](#topic_x5z_pqj_1cc) for migrating. If you're still having problems, [contact us](https://support.zendesk.com/hc/en-us/articles/4408843597850).
- Zendesk cannot unblock or unban a Facebook Business Manager, WhatsApp
  Business Account, or WhatsApp phone number that has been blocked or banned by
  Meta. However, we can raise an appeal to Meta on your behalf.