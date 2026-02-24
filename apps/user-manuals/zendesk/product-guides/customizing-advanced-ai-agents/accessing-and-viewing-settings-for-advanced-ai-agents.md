# Accessing and viewing settings for advanced AI agents 

Source: https://support.zendesk.com/hc/en-us/articles/8357756721178-Accessing-and-viewing-settings-for-advanced-AI-agents

---

This article explains how to view and configure settings for an advanced AI agent on the Settings page.User roledetermines which settings a user has access to. Client admins can access all settings.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

This article explains how to view and configure settings for an advanced AI agent on the
Settings page. [User role](https://support.zendesk.com/hc/en-us/articles/4408832171034#topic_thq_lnf_dgc) determines which settings a user has access
to. Client admins can access all settings.

This article covers the following topics:

- [Accessing the advanced AI agents settings
  page](#topic_jb3_qbl_42c)
- [About the general settings](#topic_ygm_pbl_42c)
- [About the generative AI settings](#topic_mpv_sj4_lfc)

## Accessing the advanced AI agents settings page

The AI agent settings page opens on General settings. Tabs provide access to other types of
settings.

**To access the AI agents settings page**

1. In AI agents - Advanced, in the top-right corner, use the AI agent drop-down field to
   select the AI agent you want to access the settings for.
2. In the left sidebar, click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)
   **Settings**.

   The AI agent settings page opens with the general settings
   displayed.
3. View and edit the **General** settings as needed.

   See [About the general settings](#topic_ygm_pbl_42c).
4. Click each tab to access these other settings:
   - **Languages**. See [Managing languages for expression-based AI agents](https://support.zendesk.com/hc/en-us/articles/8357749666714).
   - **Events and actions**. See [About actions for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756651290).
   - **Operating hours**. See [Setting operating hours for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749686554).
   - **Advanced settings**. See [Managing advanced settings for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/9094002847130).
   - **Change log**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_settings.png)

## About the general settings

The General settings page allows you to control the following for advanced AI agents:

| Setting | Description |
| --- | --- |
| AI agent name | Name that appears in the AI agent selection drop-down field. |
| Display name | Name that appears in the messaging widget. For messaging AI agents only. |
| Organization | Which organization the AI agent is for. |
| Channel | Whether the AI agent is for messaging or email. |
| Industry | Industry applicable to your business. Selection impacts benchmark and industry-related settings. |
| Confidence threshold for language detection | For expression-based AI agents only. Confidence level required for the AI agent to automatically use the [detected language](https://support.zendesk.com/hc/en-us/articles/8357756692890). Below the threshold, the AI agent uses the default language. |
| Confidence threshold for default messages | For expression-based AI agents only. Confidence level required to recognize an [intent](https://support.zendesk.com/hc/en-us/articles/8357751694362). If a message falls below this threshold, the AI agent uses the default reply and takes no action. For guidance in threshold setting, see [About confidence thresholds](https://support.zendesk.com/hc/en-us/articles/8357749625498). |
| Reply delay (minutes) | Amount of time to delay email replies. Recipients are more likely to open a response that doesn’t arrive immediately after the original email. It does not apply to test conversations. It’s recommended to [hide pending replies](https://support.zendesk.com/hc/en-us/articles/8357772433562) so they’re not mistaken for open tickets. For email AI agents only. |
| Generative AI | Settings relating to generative AI and large language model (LLM) activation. Options differ between AI agents that use expressions, zero-training, and agentic AI. See [About the generative AI settings](#topic_mpv_sj4_lfc) for details. |
| Tokens | Unique access token provided during [CRM integration](https://support.zendesk.com/hc/en-us/articles/8357758272154). |
| Webhook | Can be used to track AI agent performance. See [Setting up real-time alert webhooks for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357764521626). |

## About the generative AI settings

Within the general settings, you can configure how the AI agent uses generative AI.
Available options depend on the type of AI agent you’re using (expression-based,
zero-training, or agentic) and when your AI agent was created.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_settings_generative_ai.png)

| Setting | Description |
| --- | --- |
| Activate LLM | Makes generative AI responses available to the AI agent and indicates agreement with terms of service. AI agents created after March 4, 2025 cannot opt out of this selection. |
| Activate zero-training interface | Switches the AI agent to zero-training, no longer requiring intent training. Used when [converting to zero-training](https://support.zendesk.com/hc/en-us/articles/8357749441690). AI agents created after March 4, 2025 cannot opt out of this selection. |
| Use zero-training AI model | Switches the AI agent from using expressions to use cases. Used when [converting to zero-training](https://support.zendesk.com/hc/en-us/articles/8357749441690). AI agents created after March 4, 2025 cannot opt out of this selection. |