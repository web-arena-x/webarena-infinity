# Viewing intelligent triage predictions in tickets

Source: https://support.zendesk.com/hc/en-us/articles/4685355428250-Viewing-intelligent-triage-predictions-in-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

View and update ticket predictions for intent, language, and sentiment to gain insights and context for resolving customer requests faster. Use the ticket properties panel or ticket header to see these predictions and adjust them if needed. Access the update history in the ticket's events to track changes. This feature helps you understand customer needs and improve response quality.

From within a ticket, you can see the ticket’s predicted intent, language, and sentiment.
This information comes from [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538) and gives you additional context about
the ticket to help you resolve the customer’s request more quickly.

Tip: If you expect to see intelligent triage
predictions on tickets but don't, see [Why didn't intelligent triage add predictions to a
ticket?](https://support.zendesk.com/hc/en-us/articles/5798063767066)

This article contains the following topics:

- [Viewing and updating intelligent triage predictions in tickets](#topic_uqd_3kh_xcc)
- [Viewing and updating a ticket's intent and sentiment in the ticket header](#topic_scj_kl2_32c)
- [Viewing a ticket's intent and sentiment update history](#topic_tml_24x_s2c)

## Viewing and updating intelligent triage predictions in tickets

The ticket properties panel within a ticket shows the intelligent triage predictions.
From here, you can change a ticket’s intent, language, or sentiment if the original
prediction isn't accurate.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ml_intelligent_triage_ticket_fields.png)

**To view intelligent triage predictions within a ticket**

1. In the [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930), open any ticket.
2. In the ticket properties panel on the left, view the following ticket
   fields:
   - **Intent and Intent confidence**: A prediction of what the
     customer is asking about and how likely the prediction is correct.
     Confidence is either High, Medium, or Low.
   - **Language and Language confidence**: A prediction of the
     language the ticket is written in and how likely the prediction is
     correct. Confidence is either High, Medium, or Low.
   - **Sentiment and Sentiment confidence**: A prediction of how the
     customer feels about their request and how likely the prediction is
     correct. Confidence values include:
     - **Very positive**: The message likely contains
       strong positive words (like “brilliant” or “perfect”),
       positive words modified by intensity adverbs, or multiple
       positive sentences.
     - **Positive**: The message likely contains
       phrases expressing gratitude, or one to two positive
       sentences.
     - **Neutral**: The message likely contains
       factual statements without additional negative quantifiers
       (like “any” or “always”), or a mix of positive and negative
       statements.
     - **Negative**: The message likely contains
       phrases expressing frustration, complaints containing
       negative words, or repetition of the same
       dissatisfaction.
     - **Very negative**: The message likely contains strong
       negative words, capitalized text, multiple exclamation
       marks, or multiple negative phrases.
3. (Optional) To change any of the values, click the appropriate field and
   select a new value from the drop-down list.

   Most intelligent triage
   predictions are based on a ticket’s first message only. Any updates you
   make to these fields should still be based on the first message.
   Additionally, updating these fields doesn't train the machine learning
   model responsible for intelligent triage.

   If configured by an
   admin, the intent and sentiment predictions update based on the latest
   message from the end user. You can make updates based on their latest
   message.

## Viewing and updating a ticket's intent and sentiment in the ticket header

If configured by an admin, you can also view the intent and sentiment in the ticket
header.

**To view a ticket’s intent and sentiment**

1. In the [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930), open any ticket.
2. In the ticket header, view the intent and sentiment.

   You can hover over
   it to see the full text if necessary.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/agent_copilot_ticket_header_sentiment_intent.png)
3. (Optional) To change the intent or sentiment, click the current value and
   select a new value from the drop-down list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/agent_copilot_ticket_sentiment_update.png)

## Viewing a ticket's intent and sentiment update history

You can view a ticket's intent and sentiment update history from the [ticket's events](https://support.zendesk.com/hc/en-us/articles/4408829602970).

**To view a ticket's intent and sentiment update history**

1. In the [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930), open any ticket.
2. Click the events icon ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_events_icon.png)) in the [conversation header](https://support.zendesk.com/hc/en-us/articles/4408823962906#topic_n4m_fyc_zlb).

   If there
   have been updates to the ticket's intent or sentiment, the events
   display the system update with the previous intent or sentiment and the
   new intent or sentiment, after the end user last commented.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/agent_copilot_sentiment_intents_events_log.png)