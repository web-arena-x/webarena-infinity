# Configuring an AI agent's brand and channels

Source: https://support.zendesk.com/hc/en-us/articles/9543022336794-Configuring-an-AI-agent-s-brand-and-channels

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article applies to [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690) and [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality).

After you [create an AI agent](https://support.zendesk.com/hc/en-us/articles/4408824263578), you can configure which
brand and channels it’s associated with.

- **The brand** determines which help center your AI agent uses to create
  generative replies in response to customer questions.
- **The channels** determine where your AI agent is able to interact with
  customers.

You must be an admin to configure an AI agent’s brand and channels.

This article contains the following topics:

- [Configuring which brand's help center an AI agent uses](#topic_lnq_mbt_dgc)
- [Configuring which channels an AI agent is available on](#topic_bmj_nbt_dgc)

Related article:

- [Connecting external content sources to an AI
  agent to power AI-generated answers](https://support.zendesk.com/hc/en-us/articles/9521463831578)
- [Viewing and configuring settings for AI
  agents](https://support.zendesk.com/hc/en-us/articles/6447052708762)

## Configuring which brand's help center an AI agent uses

The brand associated with an AI agent determines which help center it uses to create
generative replies. You picked a brand for your AI agent when you created it, but
you can update the brand at any time.

**To update an AI agent’s brand**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the name of the AI agent you want to update.
3. Click the **Settings** tab.
4. Click the **Brand and channels** section to expand it.
5. Under **Brand**, click the drop-down and select the brand the AI agent
   should be associated with.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_ai_agent_brand_configure.png)
6. (Optional) Select **Always show title and preview for restricted
   articles** if you want unauthenticated users to see a title and short
   snippet of [restricted help center
   articles](https://support.zendesk.com/hc/en-us/articles/8087943201306).

Your changes are automatically saved, but updates to the AI agent’s brand won’t be
presented to customers until you [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250).

## Configuring which channels an AI agent is available on

The first time you publish an AI agent, you select the channels it’s associated with.
However, at any time you can update which channels an AI agent is available to
customers on. You can select only channels that are associated with the [AI agent’s brand](#topic_lnq_mbt_dgc).

**To configure an AI agent’s channels**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the name of the AI agent you want to update.
3. Click the **Settings** tab.
4. Click the **Brand and channels** section to expand it.
5. In the **Messaging** and **Email and web form** sections, select one
   or more channels the AI agent should be available on.

   Note: When you enable an email or web form channel for a
   brand, the API channel is automatically enabled as well.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_ai_agent_channels_configure.png)

Your changes are automatically saved, but updates to the AI agent’s channels won’t be
presented to customers until you [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250).

For more information about what happens when you publish an AI agent to selected
channels, see [About publishing AI agents](https://support.zendesk.com/hc/en-us/articles/7232810932250).