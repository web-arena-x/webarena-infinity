# Importing historical data from a file into AI agents - Advanced

Source: https://support.zendesk.com/hc/en-us/articles/8357758700570-Importing-historical-data-from-a-file-into-AI-agents-Advanced

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

You can import historical data to the conversation logs to help your AI agent learn about your customers' behavior faster. Historical data is all the conversations your customers have had with your support team.

You can import data [directly from your CRM](https://support.zendesk.com/hc/en-us/sections/8264312522394) platform or manually in a TSV file as described in this article.

This article covers the following topics:

- [About historical data](#topic_hb1_1t1_n2c)
- [Creating the file](#topic_jcc_ct1_n2c)
- [Importing the file](#topic_vwj_ct1_n2c)

## About historical data

Historical data is all the conversations your customers have had with your support team. It gives the AI agent an accurate picture of your most frequent inquiries.

By running the data through a pre-trained model and using AI-based clustering, you can identify the most frequent topics in your historical data. These topics are a great starting point for you to create the initial [intents](https://support.zendesk.com/hc/en-us/articles/8357751694362). The initial intents and their structure is the foundation of your AI model that directly impacts your AI agent's ability to understand different inquiries from your customers.

All imported data is sanitized and GDPR compliant. No PII data is imported. To learn more about how data is processed, see [About data processing in AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8357751648666).

## Creating the file

You must create a file with your historical data to upload. The file should contain the necessary parameters, separated with a tab, and be saved as TSV format. A sample file and a template are attached to the bottom of this article.

The following table lists the parameters to include in the file.

Table 1.

| Parameter | Description |
| --- | --- |
| conversationId | Identifies messages that are part of the same conversation. Messages in the same conversation have the same conversationId. Format is up to you. |
| sendTime | Timestamp when the message was sent. Format should follow the ISO 8601 standard. For example, 2025-03-22T04:55:51+00:00. |
| senderType | Indicates who the message is from, either "agent" or "customer." |
| text | Message that was sent. |
| agentId | (Optional) Identifier for the customer support agent. This is used for agent statistics. |

## Importing the file

After you create your file, you can import it.

**To import the file**

1. [In AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Conversation logs** in the sidebar.
2. Click the options menu in the bottom right corner, then select **Import TSV**.
3. Click **Select a file**, then select the import file you created.
4. Under **Benchmark Model**, select one of the following:
   - **Clustering** generates a report based on clustering. Select this if your AI agent has been running for a while and you want to gain insights into how you can improve your AI agent.
   - **Import only** does not generate an automation report. Select this if your AI agent is new and you're just importing historical data. You can generate a report later, if you want.
5. Click **Import**.

The imported data appears in the conversation logs. If you receive an error message importing the file, see [Data import error](https://support.zendesk.com/hc/en-us/articles/8357751691034).