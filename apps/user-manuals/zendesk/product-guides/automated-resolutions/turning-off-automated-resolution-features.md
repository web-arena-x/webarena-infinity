# Turning off automated resolution features

Source: https://support.zendesk.com/hc/en-us/articles/7460877856026-Turning-off-automated-resolution-features

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

You can manage automated resolutions usage for [AI agents](https://support.zendesk.com/hc/en-us/articles/6970583409690) by turning off some or all of the features that [consume automated resolutions](https://support.zendesk.com/hc/en-us/articles/5352026794010#topic_m1n_sq4_jwb) in your Zendesk configuration.

This article contains the following topics:

- [Preventing automated resolution usage for AI agents in messaging](#topic_twf_vh3_5bc)
- [Turning off automated resolution usage in email notifications](#topic_trk_vh3_5bc)
- [Turning off automated resolution usage in web forms](#topic_ufp_vh3_5bc)
- [Preventing automated resolution usage for zero-training AI agents (AI agents - Advanced add-on)](#topic_vtx_q1x_k2c)
- [Turning off Article Recommendations in Web Widget (Classic)](#topic_nqt_vh3_5bc)
- [Finding more information](#topic_kqn_rp1_ccc)

Related articles:

- [About automated resolutions for AI agents](https://support.zendesk.com/hc/en-us/articles/5352026794010)
- [Managing your automated resolutions](https://support.zendesk.com/hc/en-us/articles/6958358659226)
- [Monitoring automated resolution usage](https://support.zendesk.com/hc/en-us/articles/8922391373978)

## Preventing automated resolution usage for AI agents in messaging

Messaging AI agents are deployed through [messaging channels](https://support.zendesk.com/hc/en-us/articles/7232810932250) like the messaging Web Widget. You can prevent messaging AI agents from consuming automated resolutions by [disconnecting or deleting them](#topic_pkz_f33_5bc)
from messaging channels, or by [turning off article-based behavior in a messaging AI agent](#topic_trk_vh3_5bc).

### Disconnecting and deleting messaging AI agents

When you disconnect a messaging AI agent from a channel, it is replaced by the [default messaging response](https://support.zendesk.com/hc/en-us/articles/4500737327258) unless another AI agent is connected to that channel. Before disconnecting an AI agent, make sure your default messaging response is properly configured.

**To disconnect an AI agent from a channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to disconnect.
3. In the **Settings** tab, expand the **Channels** section and deselect the channel you want to disconnect.
4. At the top of the page, click **Publish AI agent**, then confirm your changes.

   Your changes are saved, the AI agent is disconnected, and the default messaging response is activated.

If you are no longer using an AI agent, and do not plan on using it in the future, you can delete it. When you delete an AI agent, any connected channels will revert to their [default response settings](https://support.zendesk.com/hc/en-us/articles/4500737327258#topic_kzg_ync_gnb).

**To delete an AI agent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent's **Options icon** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)), then select **Delete**.

   The AI agent is removed from the list. This action cannot be undone.

## Turning off automated resolution usage in email notifications

Autoreplies in email notifications are ticket trigger-based, and can consume automated resolutions when their triggers include the *Autoreply with articles* or *Autoreply* action. You can prevent automated resolution usage by deactivating or deleting these triggers.

In an email notification, a ticket trigger with the *Autoreply with articles* action adds a list of recommended articles to the body of the email. A ticket trigger with *Autoreply* action uses intelligent triage to identify and incorporate help center content into your notification email.

You can deactivate ticket triggers that include the *Autoreply* actions. After the triggers have been deactivated, you can delete them, but it isn't required.
Deactivating the triggers prevents them from running, which means they will not consume automated resolutions.

**To deactivate and delete ticket triggers using autoreply actions**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. On the Triggers page, click the **Ticket** tab.
3. Filter the triggers list to display only triggers that include the *Autoreply* or *Autoreply with articles* action, using the following criteria:

   - Type: **Actions**
   - Category: **Notify by**, and select **Autoreply** or **Autoreply with articles**.
4. Select the triggers you want to deactivate.
5. Click **Deactivate** at the bottom of the page, then confirm your selection.
6. [Delete the triggers](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_fqc_2m2_zsb) if needed.

## Turning off automated resolution usage in web forms

Web forms can consume an automated resolution when autoreplies are toggled on. You can turn off autoreplies for each active web form in your account.

**To turn off autoreply with articles in web forms**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click **Manage AI agents for email and web form**.
3. Click the **Web form** tab.
4. Under Active web forms, use the toggles to turn off autoreplies for all ticket forms.

## Preventing automated resolution usage for zero-training AI agents (AI agents - Advanced add-on)

If you have the [AI agents - Advanced add-on](https://support.zendesk.com/hc/en-us/articles/8725042447002), a [zero-training AI agent](https://support.zendesk.com/hc/en-us/articles/8357749447194) can consume an automated resolution for any conversation that is considered AI agent Handled.

**To disconnect an AI agentbot from a channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click **Manage AI agents - Advanced**.
3. Click the AI agent you want to disconnect.
4. In the **Channel** section, deselect the channel you want to disconnect.
5. At the top of the page, click **Publish AI agent**, then confirm your changes.

## Turning off Article Recommendations in Web Widget (Classic)

If you’re using the legacy [Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408843471642), automated resolutions can be consumed when the AI agent suggests an article in the conversation using Article Recommendations.

**To turn off Article Recommendations in Web Widget (Classic)**

1. In Admin Center, click **Channels** in the sidebar, then select **Classic > Web Widget**.
2. Click the **Basics** tab. If you have multiple brands, select the widget for the brand you want to use with the AI agent, then click **Basics**.
3. Deselect the **Help Center** checkbox.
4. At the bottom of the widget settings, click **Save**.

## Finding more information

If you have feedback or questions related to AI agents, visit our [community forum](https://support.zendesk.com/hc/en-us/community/posts/7155717341594) where we collect and manage customer product feedback. For general assistance with your Zendesk products, contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).