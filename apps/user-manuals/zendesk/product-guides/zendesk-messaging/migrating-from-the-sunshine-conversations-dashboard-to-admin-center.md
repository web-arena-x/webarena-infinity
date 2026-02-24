# Migrating from the Sunshine Conversations dashboard to Admin Center

Source: https://support.zendesk.com/hc/en-us/articles/6893953548442-Migrating-from-the-Sunshine-Conversations-dashboard-to-Admin-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

Note: This article applies to [legacy Sunshine Conversations accounts](about-sunshine-conversations-platform-access-and-support.md#topic_uny_ffc_pt)
created before April 6, 2023, connected to an active Zendesk account.

After you migrate from a legacy Sunshine Conversations plan to a Zendesk Suite plan,
integrations are accessed in Admin Center rather than the Sunshine Conversations
dashboard. This move consolidates several settings in a single location, making
integration management easier.

This article describes the changes in the following areas:

- [Sub-Accounts](#topic_ept_qqc_t1c)
- [Channels and Integrations Lists](#topic_fyd_rqc_t1c)
- [API Keys and Conversation Integrations](#topic_f43_rqc_t1c)
- [Account Settings](#topic_rdn_rqc_t1c)
- [Unsupported Business Systems](#topic_fhr_rqc_t1c)

## Sub-Accounts

The Sunshine Conversations dashboard allows you to purchase
multiple apps (or sub-accounts) housed in a single account. Historically,
customers have utilized these accounts to represent different brands or
development environments and have been able to purchase usage that spans
across all apps within the account.

However, Zendesk subdomains have a
1:1 relationship with each app and do not support sub-accounts. Instead, use
[Zendesk sandboxes](https://support.zendesk.com/hc/en-us/articles/4408844075930-Using-messaging-in-your-sandbox) to preview and test
your app configurations. If you find that the sandbox options do not meet your
needs, [contact](https://support.zendesk.com/hc/en-us/articles/4408843597850) your account executive or
technical architect for assistance.

## Channels and Integrations Lists

In the Sunshine Conversations dashboard, you access configured channels,
third-party bots, and conversation integrations (previously named Custom Webhooks)
through the Channels and Integrations List.

In Admin Center, this information is located across the UI.

- [Channels](#topic_zfj_tqc_t1c)
- [Third-party bots](#topic_gmn_tqc_t1c)
- [Conversations integrations](#topic_f1s_tqc_t1c)

### Channels

Not all channels specific to Sunshine Conversations are visible in Admin Center.
However, they will continue to work.

**To view the channels list in Admin Center**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
  **Channels** in the sidebar, then select **Messaging and social >
  Messaging**.

To view the entire list of channels, you can use the API for a
GET calling the following endpoint:

`https://api.smooch.io/v2/apps/{appId}/integrations`

See
the [Sunshine Conversations API reference](https://docs.smooch.io/rest/#operation/listIntegrations)
for more information.

### Third-party bots

Your third-party bots are organized with conversation bots in Admin
Center.

**To view previously integrated third-party bots**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.

   Third-party bots are listed under the Marketplace bots heading.

### Conversations integrations

Conversations integrations are included with apps and integrations in
Admin Center.

**To view Conversations integrations (custom webhooks)**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
  **Apps and integrations** in the sidebar, then select **Integrations > Conversations
  integrations**.

## API Keys and Conversation Integrations

See the following articles for information on managing API keys and
conversation integrations:

- [Using the Conversations API
  keys](https://support.zendesk.com/hc/en-us/articles/4576088682266)
- [Creating conversations integrations in
  Admin Center](https://support.zendesk.com/hc/en-us/articles/4576083789850)

## Account Settings

Legacy Sunshine Conversations users can establish settings that trickle
down to their sub-accounts.

After the move to Admin Center, you’ll need to re-apply these settings
using [API keys](https://support.zendesk.com/hc/en-us/articles/4576088682266).

Use the appKeyID and appSecret to make app setting changes that previously
could only be changed with [account keys](https://docs.smooch.io/rest/#operation/updateApp):

- "appLocalizationEnabled": true
- "echoPostback": true
- "maskCreditCardNumbers": true
- "useAnimalNames": true
- "conversationRetentionSeconds": 3600

## Unsupported Business Systems

The following business systems are no longer supported:

- **Email for Business**: Review [Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4887918604058) as an
  alternative.
- **Help Scout**: Review [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930-) as an
  alternative.
- **Stripe Connect**
- **Office Hours**: Review [Zendesk Support business hours](https://support.zendesk.com/hc/en-us/articles/4408842938522) as
  an alternative.
- **Slack**: Review the [Zendesk Slack Channel
  Integration](https://support.zendesk.com/hc/en-us/articles/4408833756698).