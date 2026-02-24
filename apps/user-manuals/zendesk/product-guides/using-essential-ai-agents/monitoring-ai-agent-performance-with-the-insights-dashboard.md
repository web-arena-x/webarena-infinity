# Monitoring AI agent performance with the Insights dashboard

Source: https://support.zendesk.com/hc/en-us/articles/6847708774554-Monitoring-AI-agent-performance-with-the-Insights-dashboard

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article applies to [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690) and [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality).

The Insights dashboard provides detailed information about your AI agent's performance.
By offering a comprehensive overview of metrics, response performance, and coverage gaps, the dashboard can help you optimize your AI agent configuration and improve the self-service experience for your end users.

Some of the information in the Insights dashboard is also available in Explore. See [Analyzing your autoreplies with articles](https://support.zendesk.com/hc/en-us/articles/4409155069466) and [Analyzing your bot builder activity (Legacy)](https://support.zendesk.com/hc/en-us/articles/4408829761690).

This article contains the following sections:

- [Opening the Insights dashboard](#topic_yst_4nm_bbc)
- [Understanding the dashboard metrics](#topic_vz2_pnm_bbc)
- [Next steps to improve performance](#topic_eny_wnm_bbc)

## Opening the Insights dashboard

You can open the Insights dashboard to view information about your AI agent's performance.

**To view the dashboard**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to monitor.
3. Click the **Insights** tab to display the dashboard.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_agents_insights_overall.png)

## Understanding the dashboard metrics

The dashboard provides a comprehensive overview of AI agent performance metrics and response performance.

The information on the dashboard is updated hourly. However, note that an interaction cannot be considered *resolved* (handled entirely by an AI agent) until at least 72 hours has passed since the last end-user activity. This means you might notice a three-day gap in data regarding resolutions.

This section describes the following areas of the dashboard:

- [Performance metrics](#topic_w3k_wnm_bbc)
- [AI agent responses (Legacy)](#topic_qrs_wnm_bbc)

### Performance metrics

The dashboard performance metrics offer you a quick glance at the AI agent's overall performance.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/insights_dashboard-performance.png)

These metrics include:

- **Active users**: Total number of unique users who actively participated in the conversation, meaning they were sent messages or selected options presented by the AI agent. This metric is updated hourly and includes all interactions, *resolved* and *unresolved*, from the last 30 days.
- **Transferred to agent**: Percentage of unique users who engaged with the AI agent and were handed over to a live agent, resulting in a ticket. These interactions are considered *unresolved*.
- **Automated resolutions**: Percentage of AI agent conversations *resolved* by the AI agent.

For detailed information about how a conversation is resolved by the AI agent, see [About automated resolutions for AI agents](https://support.zendesk.com/hc/en-us/articles/5352026794010).

### AI agent responses (Legacy)

Note: This section appears in the dashboard only if you had a draft or published AI agent as of February 2, 2025.

The AI agent responses chart breaks down the ratios of the types of responses the AI agent presented to end users over the course of their conversations.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/insights_dashboard-chart.png)

Response types include:

- **Recommended an article**: The AI agent found a relevant help center article and presented a link to it.
- **Generated a reply**: The AI agent found one or more relevant help center articles that addressed the question and shared a summary with the customer in the conversation. Generative replies include a link to the most relevant article.
- **Showed an answer**: The AI agent presented a custom answer flow.
- **Couldn't answer**: The AI agent couldn't provide an answer.

The numbers displayed in this chart represent *all* responses given to users over the previous 30 days. However, responses to the Present options step—either the end user selecting an option or entering free text matching a presented option—are not counted.

## Next steps to improve performance

The Next steps to improve performance section includes information you can use to update your AI agent to boost its effectiveness.

### **Review conversations**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_agents_review_conversations_next_step.png)

The Review conversations section displays links to transcripts of conversations between the AI agent and an end user from the last 30 days, including:

- **Unresolved conversations**: AI agent conversations that were not resolved by the AI agent, including those that remained unresolved and those that were solved by a live agent.
- **Automated resolutions**: AI agent conversations that were resolved by the AI agent.

For more information, see [Reviewing AI agent conversation transcripts](https://support.zendesk.com/hc/en-us/articles/7043105495706).

### Improve your help center

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_agents_improve_HC_next_steps.png)

This section links you to your help center, where you can create or edit articles to help the AI agent address topics identified in unresolved conversations.

### **Resolve intents without answers (Legacy)**

Note: This section appears in the dashboard only if you had a draft or published AI agent as of February 2, 2025, and your account has been matched to an intent model.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/insights_dashboard-intents.png)

You can view at a glance the top topics customers ask about during AI agent conversations that do not have existing AI agent answers. Zendesk AI uses past AI agent conversations to identify these top customer topics, known as *intent suggestions*, based on the following:

- The intent is not linked to an existing answer.
- The intent has been matched to a customer question or comment at least three times over the last 30 days.
- The intent is related specifically to the conversation AI agent the questions came through.

This helps you understand which actions your should take to improve AI agent performance. You can review your top intents without answers, then click through to the full list of intents to create an answer for an intent or to link an intent to an existing answer. Doing so might increase the number of customer support requests resolved and, in turn, lower the percentage of no AI agent responses.

For more information, see [Reviewing and assigning intents for common questions without AI agent answers (Legacy).](https://support.zendesk.com/hc/en-us/articles/5537827011994)