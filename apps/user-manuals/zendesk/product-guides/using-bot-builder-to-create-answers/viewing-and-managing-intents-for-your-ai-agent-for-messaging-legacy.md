# Viewing and managing intents for your AI agent for messaging (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/6038620020762-Viewing-and-managing-intents-for-your-AI-agent-for-messaging-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

This article describes functionality available only to customers who had a drafted or published AI agent as of February 2, 2025.

If you have an intent model assigned to your account, you can view a list of the intents associated with your assigned intent model. The list includes up to 250 industry-relevant intents, ordered by how frequently customers ask questions related to the intent in the AI agent for messaging.

On the Intents page for an AI agent, you can view a list of intents, how often they match customer queries, and the answers they are assigned to.

This article includes the following sections:

- [About the intents list for your AI agent](#topic_t4q_ypw_xbc)
- [Accessing the list of intents for your AI agent](#topic_qz5_hrw_xbc)
- [Finding intents in your intents list](#topic_nq4_jrw_xbc)

Related article:

- [Reviewing and assigning intents for common questions without AI agent answers (Legacy)](https://support.zendesk.com/hc/en-us/articles/5537827011994)

## About the intents list for your AI agent

If you have an intent model assigned to your account, you can view a list of intents for each AI agent.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bot_intents_tab.png)

The Intents page includes the intents list, which displays data relevant to intent usage and categorization. The list includes these columns:

- **Topic**: The intent text.
- **Category**: The subcategory of the intent.
- **Frequency**: The number of matched customer queries in the set period where the end user asked a question relating to that intent and the bot responded with the [fallback response](https://support.zendesk.com/hc/en-us/articles/7510607688730#topic_umz_cft_byb). This count is recorded only for intents not assigned to an answer and is intended to encourage you to link answers or generate a reply for the intent.
- **Answer**: The intent’s behavior when matched to a customer query. You can use the drop-down in this column to set or update the intent’s behavior. Options include:
 - **Generate a reply** (default setting for AI agents with generative AI only): The AI agent creates a response to a customer’s matching question.
 - **Don’t generate a reply** (AI agents with generative replies only): The AI agent replies with the standard AI agent response (“Sorry I couldn't find a good answer to your question. Here are some topics that might help though”).
 - **Add an answer** (default setting for AI agents without generative replies): The AI agent replies with the standard response (“Sorry I couldn't find a good answer to your question. Here are some topics that might help though”).
 - **Listed answer**: The AI agent replies with the displayed answer.

## Accessing the list of intents for your AI agent

You can view a list of the intents associated with your assigned intent model.

**To access the intents list**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to work with.
3. Click the **Intents** tab.
4. On the intents page, you can do any of the following:
   - Find intents by [searching](#topic_dxv_qrw_xbc), [filtering](#topic_hw2_dt4_qbc), or [sorting](#topic_ifd_ysw_xbc).
   - [Manage generative reply settings](https://support.zendesk.com/hc/en-us/articles/6138268212634#topic_qzx_2lp_zyb) for specific intents and for questions without matching intents.

## Finding intents in the intents list

You can search the intents list, sort the list according to any column, or filter based on time or subcategory.

### Searching the intents list

You can search the intents list by topic to locate a specific intent.

**To search the intents list**

1. [Open the intents page](https://support.zendesk.com/hc/en-us/articles/6038620020762#topic_qz5_hrw_xbc) for your AI agent.
2. Enter your search term or keywords in the search bar.

   The list displays all intents matching your search term. Current filtering and sorting settings apply to the search results.

### Filtering the intents list

You can narrow down the intents displayed in the list by time period, category, and exclusion options.

**To filter the intents list**

1. [Open the intents page](https://support.zendesk.com/hc/en-us/articles/6038620020762#topic_qz5_hrw_xbc) for your AI agent.
2. Click **Filter** at the top of the intents list.
3. In the Filter options window, fill in the following information:
4. Select a **Time period** during which the intents were matched to a customer’s question.

   You can select 7, 14, or 30 days.
5. Select a subcategory from the **Category** list to filter on.

   You can select as many subcategories as needed.
6. Select an **Exclude** rule:

   - **Answered**: Intents currently assigned to answers. This is a helpful option if you want to find a list of intents that are not currently assigned to answers.
   - **Generate a reply** (AI agents with generative replies only): Intents that use generative replies to send a response to matching customer queries without an assigned answer.
   - **Never asked**: Intents not matched to a customer query in the set time period.
7. Click **Apply filters**.

   The intents list is filtered based on your settings.

You can clear the filters by clicking any of the criteria at the top of the list or by clicking **Clear filters**.

### Sorting the intents list

By default, the list of intents is ordered by how frequently customers ask questions related to the intent. You can sort based on any column.

**To sort the intents list**

1. [Open the intents page](https://support.zendesk.com/hc/en-us/articles/6038620020762#topic_qz5_hrw_xbc) for your AI agent.
2. Click the **Sort** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon-sort.png)) at the top of the column you want to use to order the list.

   The intents list sorts in ascending order based on the column you selected.

You can click the column heading a second time to change from ascending to descending order. Click the column heading a third time to return to the default sort order.