# Evaluating the performance of AI agents using Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/7418648293018-Evaluating-the-performance-of-AI-agents-using-Zendesk-QA

---

Verified AI summary ◀▼

Use the QA feature to assess AI agent performance in customer interactions. Configure which bots to evaluate, and use scorecards to review conversations manually or automatically. Analyze results with the Reviews dashboard and monitor key metrics like escalations with the BotQA dashboard. This helps you refine AI workflows and improve customer support quality.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

Add-on | Quality Assurance (QA) or Workforce Engagement Management (WEM)

Zendesk QA can help you evaluate how well your [AI agents](https://support.zendesk.com/hc/en-us/articles/6970583409690) perform in conversations with your customers. You can use this information to update your AI agents and workflows based on the results.

This article contains the following topics:

- [Configuring which AI agents are evaluated](#topic_wrh_gzs_rdc)
- [Evaluating AI agent conversations](#topic_kyy_xvm_5hc)

Related articles:

- [Manually identifying AI agents in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/8071540887450)
- [Using the BotQA dashboard to understand bot escalations and performance](https://support.zendesk.com/hc/en-us/articles/7418648572826)

## Configuring which AI agents are evaluated

Zendesk QA automatically detects the following types of AI agents:

- [Zendesk AI agents](https://support.zendesk.com/hc/en-us/articles/6970583409690)
- [Sunshine Conversations bots](https://support.zendesk.com/hc/en-us/articles/6380323137306)

You can also manually report other users as AI agents so they can be reviewed using the correct resources. See [Manually identifying AI agents in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/8071540887450)

By default, bots are included in reviews. You can configure the review settings for each bot on the Bots page.

**To configure whether or not a bot is reviewable**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right corner, then select **Users, bots, and workspaces**.
2. Select **Bots**.
3. The list of bots appears, including the following columns:
   - **Bot name:** The name of the bot.
   - **Last chat:** When the last conversation with the bot took place.
   - **Reviewable:** If the bot is included in reviews.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_bots.png)Find the bot in the list, then select a value in the **Reviewable** column:
   - **Yes**: The bot is configured to be reviewed. If [autoscoring](https://support.zendesk.com/hc/en-us/articles/7043747123354) is turned on, this will happen automatically.
   - **No**: The bot is excluded from reviews, which means it will not be included in autoscoring or assignments. Non-reviewable bots are also not displayed in [filters](https://support.zendesk.com/hc/en-us/articles/7043669455130). Additionally, new data will not appear in dashboards. This option is useful if you lack sufficient context to evaluate the bot.

## Evaluating AI agent conversations

You can use Zendesk QA to evaluate the performance of your bots across various categories just like you can for human agents.

To do so, you must [set up a scorecard](https://support.zendesk.com/hc/en-us/articles/7043760215194) for the categories you want to evaluate the bot on.

If [autoscoring](https://support.zendesk.com/hc/en-us/articles/7043747123354) is turned on, bots are reviewed automatically. However, you can also review your bots manually.

**To review a bot’s performance manually**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Conversations**
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_conversations_icon.png) in the sidebar.
2. Select an existing filter, or [create a new filter](https://support.zendesk.com/hc/en-us/articles/7043759449114) to identify the bot conversations that you want to review. For example, you might use any of the following filter conditions:
   - **Participant | is | *<name of your bot>***
   - **Bot | is | *<name of your bot>***
   - **Bot type | is | *<workflow or generative>***
   - **Bot reply count | more than | 0**

   Alternatively, [use a Spotlight filter](https://support.zendesk.com/hc/en-us/articles/7043759586074) to find bot conversations.
3. Select the conversation you want to review.
4. In the **Review this conversation** panel, select the bot you want to review in the **Reviewee** field, then select the **Scorecard**.
5. Rate the bot’s performance for each category. See [Grading conversations](https://support.zendesk.com/hc/en-us/articles/7043669307418#topic_ows_lv2_p2c).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_bot_review.png)
6. (Optional) In the free-text field, enter comments about the bot’s performance.
7. Click **Submit**.

Tip: Use the [Reviews dashboard](https://support.zendesk.com/hc/en-us/articles/7043724913690) to analyze the results of a bot’s performance evaluation. Use the [BotQA dashboard](https://support.zendesk.com/hc/en-us/articles/7418648572826) to understand other important metrics about your AI agent’s performance, including how often bot conversations were escalated to human agents.