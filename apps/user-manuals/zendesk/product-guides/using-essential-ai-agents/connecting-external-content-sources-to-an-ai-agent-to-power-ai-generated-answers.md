# Connecting external content sources to an AI agent to power AI-generated answers

Source: https://support.zendesk.com/hc/en-us/articles/9521463831578-Connecting-external-content-sources-to-an-AI-agent-to-power-AI-generated-answers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article applies to [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690) and [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality). For equivalent functionality on AI agents - Advanced, see [Importing knowledge sources to power generative replies in advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749301658).

After you [create an AI agent](https://support.zendesk.com/hc/en-us/articles/4408824263578), you can configure the content sources it uses to create AI-generated answers to customer questions.

You must be an admin to configure content sources for an AI agent.

This article contains the following topics:

- [About content sources](#topic_cx3_rgn_3hc)
- [Viewing all connected content sources](#topic_arz_5gn_3hc)
- [Connecting an external content source](#topic_l1v_wgn_3hc)
- [Disconnecting an external content source](#topic_rzt_xgn_3hc)

Related article:

- [Configuring an AI agent's brand and channels](https://support.zendesk.com/hc/en-us/articles/9543022336794)

## About content sources

Content sources are the information your AI agent uses to generate answers to questions from your customers. Adding content sources to your AI agent lets it generate answers to help customers without requiring you to script every response.

Your Zendesk help center is your default content source. It’s automatically connected to your AI agent when you select a brand while creating your AI agent. You can change which help center your AI agent is connected to (this is done by [changing the AI agent’s brand](https://support.zendesk.com/hc/en-us/articles/9543022336794#topic_lnq_mbt_dgc)), but your AI agent must always have exactly one connected Zendesk help center. An AI agent cannot be connected to multiple Zendesk help centers at the same time.

You can also connect additional, external content sources to your AI agent. This is helpful if the information you want to power your AI agent’s generative answers is already contained in a different platform besides your Zendesk help center.

You can connect the following different types of external content sources to an AI agent:

- **Web crawler**: A web crawler connects external website content to your AI agent. You must first [set up a web crawler](https://support.zendesk.com/hc/en-us/articles/4593564000410) in Knowledge admin before you can connect it to your AI agent. An AI agent can be connected to multiple web crawlers at the same time.
- **Confluence**: A Confluence connection connects a Confluence space to your AI agent. You must first [set up a Confluence connection](https://support.zendesk.com/hc/en-us/articles/9796599390874) in Knowledge admin before you can connect it to your AI agent. An AI agent can be connected to multiple Confluence spaces at the same time.
- **External records**: The Federated Search API connects external records to your AI agent. You must first [configure Federated Search API calls](https://support.zendesk.com/hc/en-us/articles/4408830243482#topic_n5q_nvc_x4b)
 before your AI agent can use these external records.

You can connect multiple types of content sources to a single AI agent. For example, an AI agent can be connected to a Zendesk help center and one or more web crawlers and Confluence spaces at the same time.

The web crawler refreshes content every 30 minutes. Confluence connections refresh content every 24 hours, but you can [manually refresh Confluence content](https://support.zendesk.com/hc/en-us/articles/9796584600218#topic_x2c_xlb_xgc) if needed. External records ingested through the Federated Search API refresh based on your configuration.

## Viewing all connected content sources

In your AI agent’s settings, you can view all the content sources currently connected to it. The AI agent will use these sources to generate answers to customer questions.

**To view all connected content sources**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the name of the AI agent you want to update.
3. Click the **Settings** tab.
4. Click the **Brand and channels** section to expand it.

   Under Brand, the help center of the brand selected in the dropdown is used as the AI agent’s default content source.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_brands_and_channels_brand_dropdown.png)

   Below that, the External content sources section shows all external content sources connected to your AI agent.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_brands_and_channels_external_content_sources.png)

## Connecting an external content source

You can connect an external content source to an AI agent so it uses the information from that source when generating answers to customer questions.

The available types of external content sources are web crawlers, Confluence spaces, and external records ingested through the Federated Search API. Before you can add an external content source to your AI agent, you must have already [set up a web crawler](https://support.zendesk.com/hc/en-us/articles/4593564000410), [set up a Confluence connection](https://support.zendesk.com/hc/en-us/articles/9796599390874#topic_ftg_xjt_wgc), or [configured a Federated Search API call](https://support.zendesk.com/hc/en-us/articles/4408830243482#topic_n5q_nvc_x4b).

**To add an external content source source**

1. [In the list of content sources](#topic_arz_5gn_3hc), click **Edit sources**.

   A new dialog opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_external_content_sources_select.png)
2. Select one or more external content sources you want to connect your AI agent to.

   If you don’t see the source you want, click either **Manage crawlers** or **Manage Confluence** to be taken to Knowledge admin to [set up a new web crawler](https://support.zendesk.com/hc/en-us/articles/4593564000410) or [set up a new Confluence connection](https://support.zendesk.com/hc/en-us/articles/9796599390874#topic_ftg_xjt_wgc). Or, [configure a Federated Search API call](https://support.zendesk.com/hc/en-us/articles/4408830243482#topic_n5q_nvc_x4b).
3. Click **Save**.

   The selected sources are added to your list of external content sources.

Updates to the AI agent’s connected content sources won’t be presented to customers until you [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250).

## Disconnecting an external content source

You can disconnect an external content source from an AI agent to prevent it from using the information in that source when generating answers to customer questions.

Note: You can’t disconnect a Zendesk help center. An AI agent must always be connected to one Zendesk help center.

**To disconnect an external content source**

1. [In the list of content sources](#topic_arz_5gn_3hc), click **Edit sources**.
2. Deselect the external content source you want to disconnect from your AI agent.
3. Click **Save**.

Updates to the AI agent’s connected content sources won’t be presented to customers until you [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250).