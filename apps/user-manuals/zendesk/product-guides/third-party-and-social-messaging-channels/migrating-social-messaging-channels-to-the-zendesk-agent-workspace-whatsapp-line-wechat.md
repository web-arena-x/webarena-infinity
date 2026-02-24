# Migrating social messaging channels to the Zendesk Agent Workspace (WhatsApp, LINE, WeChat)

Source: https://support.zendesk.com/hc/en-us/articles/4408824569114-Migrating-social-messaging-channels-to-the-Zendesk-Agent-Workspace-WhatsApp-LINE-WeChat

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Location: Admin Center > Channels > Messaging and social > Messaging

This article describes how you can use self-service to migrate your social messaging channels to the improved social messaging experience in the Zendesk Agent Workspace. When you migrate your channels, you’ll get the full unified conversation experience provided by the agent workspace.

This migration article applies to the following social messaging channels:

- WhatsApp
- WeChat
- LINE

Note that this article does not include instructions for migrating Facebook Messenger and X (formerly Twitter) DM channels. To migrate these channels, see [Migrating your Facebook Messenger and X (formerly Twitter) DM channels to the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408832576410).

This article contains the following sections:

- [Migrating your channels](#topic_svb_g3s_xlb)
- [Migrating triggers, automations, and views](#topic_o42_gsz_qmb)
- [Next steps](#topic_ckw_qsz_qmb)
- [Who can't migrate?](#topic_lyx_p5z_qmb)

## Migrating your channels

Important: This section assumes you have not enabled the Agent Workspace in your account. Before you migrate, make sure you are familiar with the [messaging limitations](https://support.zendesk.com/hc/en-us/articles/4408821805338) in the Zendesk Agent Workspace. Also, make sure you are familiar with the types of accounts that [can't migrate](#topic_lyx_p5z_qmb).

**To migrate your channels**

1. Make sure your agents close all their current social messaging tickets.
2. Follow the steps described in [Migrating to the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4583448479514) to migrate your account and enable the Zendesk Agent Workspace, if you haven't already done so.
3. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png) **Channels** in the sidebar, then select **Messaging and social > Messaging**.
4. If applicable, locate your social messaging channels in the Channels list to verify they have been migrated.

   After migration, WhatsApp and LINE channels appear in Admin Center. Sunshine Conversations channels remain in the Sunshine Conversations Admin Dashboard.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_channels_list3b_crop.png)

## Migrating triggers, automations, and views

In the Zendesk Agent Workspace, when you add a **Channel is** condition or action, you can choose which social messaging channel you want to include. You can pick a specific social messaging channel or add multiple channels.

After migration, you need to update your **Channel is** conditions and actions in triggers, automations, and views to match the available options in the Agent Workspace. Making this change is important. If you don’t, your existing conditions and actions will not be recognized.

**To update your conditions and actions**

1. Open the trigger, automation, or view you want to edit.
2. Locate a **Channel is** condition or action. See example below.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_migration_channels_condition_before.png)
3. Change **Channel is** to a specific channel type. For example, **LINE**. See example below.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_migration_channels_condition_after.png)

   If you want to cover all social messaging channels, include a separate condition or action for each channel type.
4. **Save** your changes.
5. Repeat these steps for each **Channel is** condition or action you have in triggers, automations, and views.

## Next steps

After you’ve migrated your channels, make sure your agents are aware of the following:

- To learn more about how social messages work in the Zendesk Agent workspace, see [Receiving and sending messages](https://support.zendesk.com/hc/en-us/articles/4408843683226).
- The social messaging [Notifier](https://support.zendesk.com/hc/en-us/articles/4408839412634#topic_kny_kf3_n3b) will not be available. Instead agents can use [ticket tabs](https://support.zendesk.com/hc/en-us/articles/4408844108826) and [notifications lists](https://support.zendesk.com/hc/en-us/articles/4408829025690) in Agent Workspace to monitor end-user activity.
- Social messages are marked by **Via** types in the [conversation header](https://support.zendesk.com/hc/en-us/articles/4408823962906#topic_n4m_fyc_zlb). To give you better granularity, types are listed per channel. For example, WhatsApp.
- For channels that were configured in **Support > Channel integrations**:
 - The **Social Messaging Channel Info** [ticket field](https://support.zendesk.com/hc/en-us/articles/4408839412634#topic_u3s_pnx_lkb) is not available for new social messaging tickets.
 - The **Social Messaging User Info** field in end-user [profiles](https://support.zendesk.com/hc/en-us/articles/4408839412634#topic_yx5_3f3_n3b) is not available for new social messaging tickets.
 - Tickets from social messaging channels do not have **whatsapp\_support** and **line\_support** [tags](https://support.zendesk.com/hc/en-us/articles/4408839412634#topic_u3s_pnx_lkb) added by default.
 - The **Integration account** [condition](https://support.zendesk.com/hc/en-us/articles/4408838090266#topic_k2p_5b3_n3b) is not supported in triggers and automations.
- New tickets are created when your end users start a conversation over social messaging channels. A new end-user profile is created when an end user sends a message for the first time after migrating your social messaging channels to the Zendesk Agent Workspace.

## Who can't migrate?

This section describes which accounts are not eligible for self-service migration.

- If you already enabled the Zendesk Agent Workspace before self-serve migration was available, you have to manually migrate your social messaging channels. Zendesk will contact you regarding help with this process.
- If you want to include Facebook and X (formerly Twitter) DM channels in the Agent Workspace, see these articles:

 - [Adding Facebook DM channels for the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408835753370)
 - [Adding X (formerly Twitter) DM channels for the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408832388250)
 - [Migrating Facebook Messenger and X (formerly Twitter) DM channels to the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408832576410)