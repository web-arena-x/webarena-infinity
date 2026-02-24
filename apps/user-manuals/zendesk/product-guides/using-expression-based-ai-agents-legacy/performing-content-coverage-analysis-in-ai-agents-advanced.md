# Performing content coverage analysis in AI agents - Advanced

Source: https://support.zendesk.com/hc/en-us/articles/8357758759322-Performing-content-coverage-analysis-in-AI-agents-Advanced

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

The functionality described in this article applies only to expression-based AI agents. For zero-training AI agents or AI agents with agentic AI, [use the use case suggestions report](https://support.zendesk.com/hc/en-us/articles/9041901679130#topic_gr4_l5n_s2c) instead.

Content coverage analysis helps determine whether you have the right intents in place by reviewing the reasons customers are contacting customer support. The analysis is a manual process that involves validating frequently asked questions and identifying the relevant intents.

Using those findings, you can determine the content coverage percentage for your existing intents. You can also create new intents to help the AI agent understand and handle more incoming, repetitive customer requests.

**To perform content coverage analysis**

1. [In AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/4408838272410), select the AI agent where you want to perform content coverage analysis.
2. Click **Conversation logs** in the sidebar.
3. Select a timeframe in the top-right corner.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_360026438799.png)
4. Read through 100 conversations, one by one, and find the first message in each conversation where the customer clearly states their reason for contacting support.
5. Hover over each conversation, click the **Labels** icon, then enter a name for the label and click the **Add** + icon to create it.

   Add a label for the intent of each conversation, whether or not it has an intent. You can use multiple labels on each conversation. Add a label to indicate conversations that have intents (an "Existing" label, for example) and a different label to indicate conversations that don't have intents (a "Non-existing" label, for example).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_360026439259.png)
6. Filter on messages that have the label for existing intents.

   The number of messages out of 100 that have the label applied is your percentage of messages that have an intent. This represents your content coverage. A content coverage of 60% to 80% can be viewed as a sufficient baseline for a functional AI solution.

Next, you can use the label you applied to messages without intents to identify repeated questions that might require a new intent. A topic is a good candidate for a new intent if 10% of the messages analyzed are related to that topic.