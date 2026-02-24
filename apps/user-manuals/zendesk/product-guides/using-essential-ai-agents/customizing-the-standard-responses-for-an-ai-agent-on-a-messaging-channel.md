# Customizing the standard responses for an AI agent on a messaging channel

Source: https://support.zendesk.com/hc/en-us/articles/8774095741466-Customizing-the-standard-responses-for-an-AI-agent-on-a-messaging-channel

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article applies to [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690).

If you’ve [created an AI agent](https://support.zendesk.com/hc/en-us/articles/4408824263578) for a messaging channel,
there are several standard responses you can customize to define the AI agent's default
responses to customer input during a live conversation:

- **Start of the conversation**: Initial greeting when a messaging conversation is
  started.
- **After the AI agent replies**: Response to customer feedback.
- **Escalation**: What happens when the customer wants to talk to a human.
- **If the AI agent can't answer the question**: Response when the customer's
  comment does not match any answer, known as a fallback response.

This article contains the following sections:

- [Viewing the standard responses](#topic_bqy_ycd_f2c)
- [Customizing the greeting message](#topic_z34_zcd_f2c)
- [Customizing the response to customer feedback](#topic_q5m_1dd_f2c)
- [Customizing the escalation response](#topic_tzc_bdd_f2c)
- [Customizing the fallback response](#topic_b5p_bdd_f2c)
- [Best practices for customizing the standard responses](#id_nn1_drx_vgc)

Related articles:

- [Viewing and configuring settings for AI agents
  for messaging](https://support.zendesk.com/hc/en-us/articles/6447052708762)

## Viewing the standard responses

The AI agent has several standard responses that you can customize as needed.

**To view the AI agent standard responses**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the name of the AI agent you want to edit.
3. Click the **Messaging behavior** tab, then click each message to view it:
   - [Start of the
     conversation](#topic_z34_zcd_f2c)
   - [After the AI agent
     replies](#topic_q5m_1dd_f2c)
   - [Escalation](#topic_tzc_bdd_f2c)
   - [If the AI agent can't
     answer the question](#topic_b5p_bdd_f2c)

## Customizing the greeting message

When your customers first open a messaging conversation in the Web Widget or mobile
SDK, they’re met with an initial greeting message. You can update the greeting
message or leave it as-is.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_agents_greeting_message_new.png)

**To customize the greeting message**

1. [On the Messaging behavior
   tab](#topic_bqy_ycd_f2c), expand the **Start of the conversation** section.
2. In the **Greeting** field, enter your initial message or leave the
   default message. *(Hi there. Got a question? I'm here to help.)*
3. Select **Add option to talk to a human** if you want a button labeled
   “Talk to a human” to appear after the greeting message.

   If a customer
   clicks “Talk to a human,” the [escalation response](#topic_tzc_bdd_f2c) is triggered.

The response is saved automatically as you edit it, but updates will not be presented
to customers until you [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250).

## Customizing the response to customer feedback

When the AI agent presents an answer, it follows up by asking whether the answer was
helpful. The "After the AI agent replies" response lets you configure the AI agent
response when an end user says the answer was helpful or unhelpful.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_agents_response_message_new.png)

**To customize the response to customer feedback**

1. [On the Messaging behavior
   tab](#topic_bqy_ycd_f2c), expand the **After the AI agent replies** section.
2. On the **Helpful answer** tab, in the **Message** field, enter a
   message to display when the end user says the suggested article was helpful,
   or use the default message provided. *(Great. You can ask another question
   anytime.)*
3. Click **Add option to talk to a human** if you want a button labeled
   “Talk to a human” to appear after the AI agent’s response to customer
   feedback.

   If a customer clicks “Talk to a human,” the [escalation response](#topic_tzc_bdd_f2c)
   is triggered.
4. Click the **Unhelpful answer** tab and configure the options as described
   above.

The response is saved automatically as you edit it, but updates will not be presented
to customers until you [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250).

## Customizing the escalation response

The escalation response determines what happens when the customer wants to talk to a
human. This response is triggered either when:

- The AI agent determines that a human agent is needed in order to solve the
  customer’s request.
- The customer clicks the “Talk to a human” button that appears after the AI
  agent’s response. This button appears if you configure the [greeting message](#topic_z34_zcd_f2c), [response to customer
  feedback](#topic_q5m_1dd_f2c), or [fallback
  response](#topic_b5p_bdd_f2c) to include it.

**To customize the escalation response**

1. [On the Messaging behavior
   tab](#topic_bqy_ycd_f2c), expand the **Escalation** section.
2. Under the **Business hours** heading, use the drop-down to select a
   schedule to set the AI agent’s business hours, or select **Always
   online**.

   For more information about schedules, see [Setting your schedule with business
   hours and holidays](https://support.zendesk.com/hc/en-us/articles/4408842938522).
3. Under the **Responses** heading, on the **During business hours** tab,
   select one of the following options:
   - **Create a ticket**: Select this option if you want a ticket to
     be created when the customer escalates an AI agent conversation to a
     human.

     If you select this option, configure the following fields:

     - **Message**: Enter a message asking the customer to
       provide details about their request.
     - **Customer details**: Select the fields a customer should
       fill out when escalating.
     - **Follow-up message**: Enter a message telling the
       customer what to expect after they’ve provided their
       details.
   - **Show a custom response**: Select this option if you don’t want
     a ticket to create a ticket when a customer escalates an AI agent
     conversation to a human, and instead show the customer a pre-written
     message. If you select this option, configure the following fields:
     - **Message**: Enter a message directing the customers to a
       website, form, email address, or telephone number.
4. Click the **Outside business hours** tab and configure the options as
   described above.

The response is saved automatically as you edit it, but updates will not be presented
to customers until you [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250).

## Customizing the fallback response

The fallback response is triggered when there is no answer that matches the end
user's question or comment.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_agents_fallback_response_new.png)

**To customize the fallback response**

1. [On the Messaging behavior
   tab](#topic_bqy_ycd_f2c), expand the **If the AI agent can't understand the
   question** section.
2. Enter a message the AI agent will send if it can’t provide an answer based
   on the information the customer entered.

   The default fallback response is,
   *Sorry I couldn’t answer your question*.
3. Click **Add option to talk to a human** if you want a button labeled
   “Talk to a human” to appear after the fallback response.

   If a customer
   clicks “Talk to a human,” the [escalation response](#topic_tzc_bdd_f2c) is triggered.

The response is saved automatically as you edit it, but updates will not be presented
to customers until you [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250).

## Best practices for customizing the standard responses

When defining the standard responses, keep these best practices in mind:

- **Encourage users to keep questions short** and to the
  point.
- **Encourage users to ask a single question at a time.** Rather
  than presenting "I want to cancel but I can't log in," for example, pose two
  separate questions.
- **Don’t hide the fact that the user is talking to an AI
  agent.** If the user thinks they’re talking to a human, they’re likely
  to write long, conversational messages. The AI agent might have trouble
  understanding, and the user might feel that they’ve been misled.
- **Ask the user to freely ask their question with context** if
  the AI agent is configured with generative replies or multiple answers. The
  user should freely ask the question instead of using single keywords. For
  example, a single word, such as “refund,” can lead to confusion about the
  user’s intent, because it's not clear if they are interested in "refund
  request" or "refund policy."
- **Pin common answers and clarify if there is an option to speak to an
  agent** in your greeting or fallback responses. This can help reduce
  customer frustration and prevent conversation loops.
- **Offer the option to speak to an agent.** If you can’t offer a real
  person, let the user know that up front to avoid frustration.