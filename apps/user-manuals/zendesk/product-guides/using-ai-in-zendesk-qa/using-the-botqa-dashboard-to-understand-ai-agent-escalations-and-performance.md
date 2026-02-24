# Using the BotQA dashboard to understand AI agent escalations and performance 

Source: https://support.zendesk.com/hc/en-us/articles/7418648572826-Using-the-BotQA-dashboard-to-understand-AI-agent-escalations-and-performance

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

The BotQA dashboard helps you understand important metrics about your AI agent’s performance,
including how often:

- Bot conversations were escalated to human agents
- The bot got stuck in a loop
- The bot’s communication efficiency was marked lower compared to an average agent’s
- The bot exhibited a negative sentiment

This article contains the following topics:

- [Accessing the BotQA dashboard](#topic_ycs_ytg_3gc)
- [Filtering the BotQA dashboard](#topic_ntc_dqm_5hc)
- [Understanding the BotQA dashboard
  reports](#topic_sjj_m5g_3gc)

Related articles:

- [Evaluating the performance of AI agents using Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7418648293018)

## Accessing the BotQA dashboard

You can access the BotQA dashboard from the list of dashboards in Zendesk QA.

**To access the BotQA dashboard**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Dashboards**
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_dashboard_icon.png) in the sidebar.
2. From the list of dashboards, select **BotQA**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/botqa_dashboard.png)

## Filtering the BotQA dashboard

Dashboard filters allow you to narrow the data based on time period, specific bots, and
conversation outcome. See [About dashboards in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043701144858).

**To filter the BotQA dashboard**

1. [In the BotQA dashboard](#topic_ycs_ytg_3gc), select from
   the following filters:

   - **Date Filter**: Select the relative or exact dates for the bot conversations
     you want to see data for. By default, the dashboard returns data for the last
     month.
   - **Bot Name**: Select a specific bot or bots you want to see data for. By
     default, the dashboard returns data for all bots.
   - **Conversation Outcome**: Select either of the following options to toggle
     them on. By default, neither is selected.

     - **bot-only**: The customer interacted only with a bot, not an agent.
     - **escalated**: The customer asked to speak to a human agent.

## Understanding the BotQA dashboard

The BotQA dashboard contains the following reports:

- **Bot-only conversation rate**: Percentage of conversations without human agent
  involvement.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zendesk_qa_botqa_bot_only_conversion.png)
- **Escalation rate**: Percentage of conversations where the customer asked to talk to
  a human agent.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zendesk_qa_botqa_escalation_rate.png)
- **Escalation rate over time**: Percentage of conversations where the customer asked
  to talk to a human agent by week of conversation creation date.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zendesk_qa_botqa_escalation_over_time.png)
- **Breakdown by conversation outcome**: Comparison of the count of conversations
  without human agent involvement (bot-only conversations) and the count of conversations
  where the customer asked to talk to a human agent (escalated conversations).

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zendesk_qa_botqa_breakdown_conversation_outcome.png)
- **Bot looping rate**: Percentage of conversations where the bot gave the same answer
  multiple times in a row.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zendesk_qa_botqa_bot_looping_rate.png)
- **Bot low communication efficiency rate**: Percentage of conversations where the bot
  handled the conversation less efficiently than an average agent.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zendesk_qa_botqa_bot_low_communication_efficiency.png)
- **Bot negative sentiment rate**: Percentage of conversations where the bot expressed
  dissatisfaction or frustration.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zendesk_qa_botqa_bot_negative_sentiment_rate.png)