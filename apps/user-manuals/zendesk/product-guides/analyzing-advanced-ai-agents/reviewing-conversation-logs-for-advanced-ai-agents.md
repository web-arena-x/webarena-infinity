# Reviewing conversation logs for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749580186-Reviewing-conversation-logs-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Conversation logs allow you to review all messages that have been exchanged between an AI agent and end users during automated conversations. From here, you can review details for specific messages and whole conversations as part of your ongoing AI agent monitoring and analysis.

This article contains the following topics:

- [Viewing the conversation logs for an advanced AI agent](#topic_nxy_tgf_52c)
- [Filtering the list of conversations](#topic_y3w_5gf_52c)
- [Reviewing details for a whole conversation](#topic_rt5_vgf_52c)
- [Reviewing details for a single message](#topic_uys_wgf_52c)
- [Reviewing API integration information](#topic_djg_kgx_c3c)

Related articles:

- [Using labels to tag conversation content for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749583130)

## Viewing the conversation logs for an advanced AI agent

You can view the conversation logs for an advanced AI agent to see the conversations they’ve had with users and drill deeper into specific responses.

**To view the conversation logs for an advanced AI agent**

1. IIn AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Conversation logs** in the sidebar.

   A list of conversations appears for the default time frame (the past 7 days). If you don’t see any conversations, [adjust the time frame](#topic_y3w_5gf_52c).
3. (For messaging AI agents only) Toggle the **Status** / **Custom resolutions** setting at the bottom to switch between showing either the conversation status or custom resolution values.

   For an explanation of the values, see the table in the next section.

## Filtering the list of conversations

You can filter the list of conversations by time frame or other filters, such as language, status, labels, and more.

**To filter the list of conversations by time frame**

Note: The time frame filter uses UTC (Coordinated Universal Time), even though conversations in the conversation logs show timestamps in the user's browser's time zone.

1. [In the conversation logs](#topic_nxy_tgf_52c), in the upper-right corner, click **Time frame**.
2. Using one of the following methods, select the dates you want to view conversations for:
   - On the right, select one of the predefined time frames:
     **Today**, **Yesterday**, **Last 7 days**, **Last 30 days**, **This month**, **Last month**
   - Select specific beginning and end dates on the calendar.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_conversation_logs_time_frame.png)

**To filter the list of conversations by other filters**

1. [In the conversation logs](#topic_nxy_tgf_52c), in the upper-left corner, click **Add filter**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_conversation_logs_add_filter.png)
2. Select and configure one or more of the following filters:

   | | |
   | --- | --- |
   | **Filter** | **Configuration details** |
   | Message text | In the Message text field, enter a specific word or phrase you want to search for within the conversations. |
   | Language | Select the languages you want to see conversations for. |
   | Conversation source | Select one or more of the following options: - **AI agent**: Conversations between the AI   agent and end users. - **Testing**: Conversations created through   the test widget. - **Imported**: Conversations imported from a   different system. |
   | Conversation type | Select one or more of the following options: - **Conversations with messages not   understood**: Conversations with at least one   message that was not understood below the   threshold. - **Actions applied**: Conversations   with applied actions. - **Conversations with interrupted   dialogues**: Conversations where customers   interrupted the conversation (for example, by   triggering another use case or loops). - **Conversations with drop-offs**:   Conversations where users left before completing a   dialogue. - **Hide in-progress sessions**:   Hide conversations with sessions still within   their duration threshold. - **Show only automated resolution   conversations**: Show only AI agent-handled   conversations that have passed [verification](https://support.zendesk.com/hc/en-us/articles/5352026794010#topic_t1f_bqb_g2c). - **Hide automated resolution   conversations**: Hide all conversations that   have passed [verification](https://support.zendesk.com/hc/en-us/articles/5352026794010#topic_t1f_bqb_g2c). - **Conversations with knowledge   answers**: Conversations in which the AI agent   responded with a generated knowledge source–based   answer. This excludes generative replies. - **Conversations without knowledge   answers**: Conversations in which none of the AI   agent messages were created with a generated   knowledge source–based answer. This excludes   generative replies. - **Conversations with procedures   used**: Conversations in which the AI agent   responded with a generated message based on a   [procedure](https://support.zendesk.com/hc/en-us/articles/8979864563610) at   least once. - **Conversations without procedures   used**: Conversations in which the AI agent has   not responded with a generated message based on a   [procedure](https://support.zendesk.com/hc/en-us/articles/8979864563610). |
   | Conversation status | Select one or more of the following statuses. For messaging AI agents: - **Agent escalation**: The   conversation was successfully transferred to a   human agent. - **AI agent handled**: The   conversation had a meaningful intent, did not   attempt escalation, and ended without the AI agent   misunderstanding a message. - **Custom escalation**: The   conversation had a custom escalation attempt. - **Email escalation**: The   conversation was successfully emailed to the   support team. - **Escalation failed**: The   conversation had an unsuccessful escalation   attempt. - **No status** For email AI agents: - **Not understood**: The last message was   not understood, and no actions or replies were   triggered. - **Recognized intent**: The last message was   understood, and no actions or replies were   triggered. - **Processed**: Actions were taken, but no   reply was sent or the reply was empty. - **Answered**: The last message was   understood, and one of the following is true: The   AI agent sent a reply, or the AI agent triggered a   macro that added a public comment to a   ticket. - **Escalated**: A reply was sent by the AI   agent and a human agent. - **No status** |
   | BSAT | Select one or more of the last BSAT rating responses, or select **Not now**. |
   | Custom resolutions | Select one or more of the following custom resolution states: - **Resolved**: A meaningful custom   resolution was provided, and there are no further   questions. - **Informed**: Instructions or guidance was   provided. - **Escalated to agent**: The conversation   was successfully transferred to a human   agent. - **Escalated via email**: The conversation   was successfully converted into an email ticket   for the support team. - **Unresolved**: The AI agent didn’t answer   or resolve the issue. - **Escalation failed**: The conversation   wasn’t escalated successfully because no agent was   available, or there was a technical error. - **Undefined**: No custom resolution is   associated with the conversation. |
   | Labels | Select whether you want to see conversations with **Any of the selected labels**, **All of the selected labels**, or **None of the selected labels**, then select specific labels. See [Using labels to tag conversation content for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749583130). |
   | Intents | Select a specific use case. See [Creating use cases for advanced AI agents to identify what customers are asking about](https://support.zendesk.com/hc/en-us/articles/9041901679130). This filter applies only to use cases that were detected during a conversation, not use cases that were linked to from other replies. |
   | Segments | Select whether you want to see conversations with **Any of the selected segments**, **All of the selected segments**, or **None of the selected segments**, then select specific segments. See [Creating segments to target specific customer groups in advanced AI agent conversations](https://support.zendesk.com/hc/en-us/articles/9413046533530). |
   | Duration | Select an **operator** and a number of **seconds** to determine the duration of the conversations you want to see. |
   | Platform conversation ID | In the **Platform conversation ID** field, enter an ID from your CRM to see a specific conversation. This is useful when comparing logs between your CRM and your AI agent. |
   | Generative replies | Select one or more of the following options: - **Generative replies used** - **Generative replies not   used** - **Feedback shared** - **Feedback not shared** |
   | Generative replies status | Select one or more of the following options: - **Response generated** - **Not understood** - **Escalation needed** - **An error occurred** |
3. Click **Apply**.

## Reviewing details for a whole conversation

You can review the details for a conversation to get more information about the overall interaction between the user and the AI agent.

**To review details for a whole conversation**

1. [In the conversation logs](#topic_nxy_tgf_52c), click the conversation you want to view.

   The conversation appears on the right half of the page, and includes any messages sent as well as any [actions](https://support.zendesk.com/hc/en-us/articles/8357756651290) or [events](https://support.zendesk.com/hc/en-us/articles/8357749555610) that were applied.
2. In the upper-right corner, click **Details**.
3. Review the following details in the **Conversation overview** pane:
   - **Date and time**: The date and time the conversation took place.
   - **Duration**: How long the conversation lasted.
   - **Custom resolution**: Which [custom resolution state](https://support.zendesk.com/hc/en-us/articles/8357756466586)
     applied to the conversation.
   - **Test conversation**: Whether the conversation was a test (as determined by whether it was created using the Test Bot, Test Dialogue, or Test Branch options).
   - **Platform conversation ID**: A unique identifier for the conversation in the CRM your AI agent is integrated with. This is used for finding the same conversation in your CRM. Not supported for Zendesk messaging integrations.
   - **Labels**: Which labels were added to the conversation. You can add additional labels by clicking Add.
   - **Presumed use case**: (Appears only for [zero-training AI agents](https://support.zendesk.com/hc/en-us/articles/8357749447194).)
     The [use case](https://support.zendesk.com/hc/en-us/articles/8357733365402) that best fits the conversation. An AI-generated explanation describes why the use case was selected.
   - **Automated resolution**: Whether the conversation [consumed an automated resolution](https://support.zendesk.com/hc/en-us/articles/5352026794010#topic_t1f_bqb_g2c), including an explanation.
4. Click **Segment matches** to see which [segments](https://support.zendesk.com/hc/en-us/articles/9413046533530) applied to the conversation.

   You can click a segment name to be taken directly to its configuration to view or edit it.
5. Click **Session data** to show the following additional information:
   - The actions and events that occurred throughout the conversation.
   - The active language set.
   - The last detected language.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_conversation_overview_example_Jun25.png)

## Reviewing details for a single message

You can review the details for a single message within a conversation to get more information about why the message was generated (in the case of an AI agent message)
or how the AI agent interpreted the message (in the case of a user message).

**To review details for a single message**

1. [In the conversation logs](#topic_nxy_tgf_52c), click the conversation you want to view.

   The conversation appears on the right half of the page, and includes any messages sent as well as any [actions](https://support.zendesk.com/hc/en-us/articles/8357756651290) or [events](https://support.zendesk.com/hc/en-us/articles/8357749555610) that were applied.
2. Hover over the message you want to see more information about and click the **View details** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_view_details_icon.png)) that appears.

   The icon appears to the left of AI agent messages and to the right of user messages.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_conversation_logs_view_details_button.png)
3. Review the message details that appear in the pane on the right.
   - For user messages, the pane is called **Message overview** and shows the following information:
     - **Message**: The exact text of the user’s message.
     - **Presumed use case**: (Appears only for [zero-training](https://support.zendesk.com/hc/en-us/articles/8357749447194) and [agentic](https://support.zendesk.com/hc/en-us/articles/8966284087066) AI agents.) The [use case](https://support.zendesk.com/hc/en-us/articles/9041901679130) that best fits the conversation. An AI-generated explanation describes why the use case was selected.

       ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_message_overview_example.png)
   - For AI agent messages associated with a [dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810), the pane is called **Reply overview** and shows the following details:
     - **Details**
       - **Used reply**: Dialogue the message came from.
       - **Reply type**: Type of reply.
       - **Intent**: Use case the dialogue is associated with.
     - **Edit reply**
       - **Edit dialogue**: Opens the [dialogue builder](https://support.zendesk.com/hc/en-us/articles/8357749494810) for the dialogue that the message came from.

         ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_reply_overview_example.png)
   - For AI agent messages associated with a [generative procedure](https://support.zendesk.com/hc/en-us/articles/8979864563610), the pane is called **AI agent message overview** and shows the following details:
     - **Details**
       - **Use case**: Which use case the generative procedure is associated with.
       - **Plan**: The AI agent’s reasoning in determining how to resolve the user’s issue.
       - **Procedure step**: Click to view the specific step within a generative procedure that produced the message.
       - **Response before customization**: The response text that the AI agent generated before the [AI agent persona](https://support.zendesk.com/hc/en-us/articles/8357758773658) or any [instructions](https://support.zendesk.com/hc/en-us/articles/8357749291290)
         were applied.
     - **Active instructions**: Any instructions you’ve created that are currently active. These instructions affect the AI agent’s ultimate response to the user.
     - **Personalization**
       - **AI agent name**: Name of the AI agent.
       - **Company name**: Name of your company.
       - **Tone**: [Tone of voice](https://support.zendesk.com/hc/en-us/articles/8357758773658-Customizing-the-persona-and-tone-of-voice-for-your-advanced-AI-agent#:~:text=Click%20the-,Tone%20of%20Voice,-tab%20and%20fill) you selected for the AI agent.
       - **Answer length**: [Answer length](https://support.zendesk.com/hc/en-us/articles/8357758773658-Customizing-the-persona-and-tone-of-voice-for-your-advanced-AI-agent#:~:text=throughout%20the%20conversation.%E2%80%9D-,Answer%20Length,-%3A%20Select%20one%20of) you selected for the AI agent.

         ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_ai_agent_message_overview_example.png)

## Reviewing API integration information

You can review information about API requests that take place during conversations between your AI agent and customers. This information includes when the calls were made and details of the calls, including request and session parameters, the response, any errors, and more. This information can be especially useful for troubleshooting.

Note: Legacy API integrations don’t appear in conversation logs.

**To review API request information**

1. In the conversation logs, click the conversation you want to view.

   Look for entries in the conversation labeled **Integration triggered** or **Integration parameter requested**.
2. Click an integration entry to see the specific API request or requests.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_convo_log_integration_triggered.png)
3. Click an API request to open the Integration details panel.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_convo_log_integration_details.png)

   Here, you can review the following details about the API request:
   - **Date and time**: The timestamp of when the API request was triggered during the conversation.
   - **Source**: The name of the dialogue that triggered the API request. You can click the name to open the dialogue in the dialogue builder.
   - **API integration**: The name of the integration.
   - **Scenario**: Which scenario (success, failure, fallback, or custom) was triggered as part of the API integration block in the dialogue.
   - **Request parameters**: Any [request parameters](https://support.zendesk.com/hc/en-us/articles/8357756844442#h_01HAY9KGH06WFPD1BMJAPA3D0Q)
     (inputs) that were configured for the API request. Errors due to missing required values or data type mismatches are highlighted in red.
   - **Session parameters**: Any [session parameters](https://support.zendesk.com/hc/en-us/articles/9522180655386#topic_lf5_pzp_xfc)
     (outputs) that were configured for the API request.
   - **API error**: (Appears only if an error occurred.) Details about the error.
4. (Optional) Click **View integration** to open the integration in the [integration builder](https://support.zendesk.com/hc/en-us/articles/8357756844442).