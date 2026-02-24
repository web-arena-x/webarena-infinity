# Viewing Zendesk error logs for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357765445274-Viewing-Zendesk-error-logs-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

You can view the Support error logs for advanced AI agents to review failures related to the following actions:

- Add tag
- Update ticket info
- Add internal note
- Get ticket tag
- Get ticket info
- Get organization info

The Chat error logs show failures for escalations, actions, and replies. The Sunshine Conversation error logs show failures for get user, update user, get conversation, update conversation, and Sunshine Conversations actions.

Errors in the Support error logs might include, for example:

- The data type that was expected, such as string or boolean, was not received.
- The conversation or user field doesn't exist.
- A mandatory or dependent field was not completed.
- The API call failed.

**To view the error logs**

1. [In AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png) **Settings** in the sidebar, then select **CRM integration** > **Error logs**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_9455156903314.png)
2. View the following information for each item:
   - **Timestamp**: Time the error was triggered.
   - **Details**: Type of error that occurred with information on which field, ID, or structure was impacted.
   - **Type**: Kind of error that occurred, for example, a failed action.
   - **Conversation ID**: Clickable link to the log for the conversation where the error occurred.
   - **Ticket ID**: ID number of the ticket corresponding to the conversation.
   - **Recommended action**: Next steps to resolve the issue and prevent it from reoccurring.
3. Refine your view by taking any of the following actions:

   - **Search** by entering the conversation ID if you know it.
   - **Filter** by action failed, reply failure, or escalation failure using the Type dropdown.
   - **Apply date range** using the Timeframe calendar.
   - **Sort** by timestamp or conversation by clicking the top of the column.