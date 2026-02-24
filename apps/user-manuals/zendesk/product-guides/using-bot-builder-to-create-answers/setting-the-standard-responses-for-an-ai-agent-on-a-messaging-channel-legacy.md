# Setting the standard responses for an AI agent on a messaging channel (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/7510607688730-Setting-the-standard-responses-for-an-AI-agent-on-a-messaging-channel-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article applies only to customers who had any drafted or published AI agents as of February 2, 2025. Customers on [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690) should see [Customizing the standard responses for an AI agent for messaging](https://support.zendesk.com/hc/en-us/articles/8774095741466) instead.

If you’ve [created an AI agent](https://support.zendesk.com/hc/en-us/articles/4408824263578) for a messaging channel, there are several standard responses you can customize to define the AI agent's default responses to customer input during a live conversation.

This article contains the following sections:

- [Overview of the standard AI agent responses](#topic_nvy_p3b_ccc)
- [Setting up the standard responses](#topic_slx_n4p_qtb)

## Overview of the standard AI agent responses

The standard AI agent responses include:

- **Start of conversation**: Initial greeting when a messaging conversation is started.
- **If the AI agent finds relevant information**: Response when a possible solution is found in your help center.
- **After the AI agent answers**: Response to customer feedback.
- **If the AI agent can't answer a question**: Response when the customer's comment does not match any answer.

## Setting up the standard responses

There are several standard responses that you can edit as needed to customize your AI agent's responses.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bot_settings-behavior_tab_Mar25_update.png)

**To edit the AI agent standard responses**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the name of the AI agent you want to edit.
3. Click the **Messaging behavior** tab, then click each message to edit it:
   - [Start of the conversation](#topic_e41_f1q_hvb)
   - [If the AI agent finds relevant information](#topic_o1b_m1n_gbc)
   - [After the AI agent answers](#topic_m5t_41n_gbc)
   - [If the AI agent can't answer the question](#topic_umz_cft_byb)

Each response is saved automatically as you edit it, but updates will not be presented to customers until you [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250).

### Start of the conversation

When your customers first open a messaging conversation in the Web Widget or mobile SDK, they’re met with an initial welcome message.

There are two types of welcome messages:

- [A standard, configurable welcome message](#topic_ms5_ngt_byb)
- [A specific answer in your AI agent for messaging](#topic_n5g_4gt_byb)

#### Configuring the standard greeting message

By default, the AI agent is configured with a basic greeting message and a suggested answer. You can update the greeting message, add or remove answers (up to 10 answers), or leave them as-is. Answers selected here are presented to your customers as [options](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_mnf_gwc_k4b).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bot_setup_greeting_Mar25_update.png)

**To configure a welcome message**

1. [On the Messaging behavior tab](https://support.zendesk.com/hc/en-us/articles/7510607688730#topic_slx_n4p_qtb), expand the **Start of the conversation** section.
2. Select **Send a greeting and suggest answers**.
3. Enter your initial message or leave the default message (*Hi there. Got a question? I'm here to help.*).
4. Use the **Answers** drop-down to select up to 10 answers to present to customers as preconfigured options.

   One suggested answer is included by default ( *Talk to a human* ).

#### Using an answer as the welcome message

You can also choose a [custom-built answer](https://support.zendesk.com/hc/en-us/articles/4422584657434) to start the conversation.
When the end user first interacts with the AI agent, the selected answer is sent. This option can be used to immediately transfer your customer to an agent, for example.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bot_setup_greeting-answer.png)

**To use an existing answer as your welcome message**

1. [On the Messaging behavior tab](https://support.zendesk.com/hc/en-us/articles/7510607688730#topic_slx_n4p_qtb), expand the **Start of the conversation** section.
2. Select **Start with an answer**.
3. Use the drop-down to select the answer that will welcome your customers when they initiate a conversation.

### If the AI agent finds relevant information

If you have an active help center, you can configure how your AI agent replies when it locates one or more help center articles that can address the end user's question.

It’s strongly recommended to [use generative replies](https://support.zendesk.com/hc/en-us/articles/6138268212634) for this standard response. With generative replies, your AI agent uses generative AI to evaluate articles in your help center and provide concise answers within the ongoing conversation. Using this option gets your AI agent up and running immediately without needing to build answer flows.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bot_settings-relevant_articles_updated.png)

**To set up AI agent replies for help center results**

1. [On the Messaging behavior tab](https://support.zendesk.com/hc/en-us/articles/7510607688730#topic_slx_n4p_qtb), expand the **If the AI agent finds relevant information** section.
2. Select one of the following response options:
   - **Generate a reply**: (Recommended) The AI agent creates AI-generated answers in response to customer questions based on your help center content. These short, summarized answers are delivered as part of the ongoing conversation and don’t require the customer to open a separate help center article. See [Using AI to generate replies in an AI agent for messaging (Legacy)](https://support.zendesk.com/hc/en-us/articles/6138268212634).
   - **Don't answer based on articles**: The AI agent does not reference help center content.
     Instead, it displays a relevant [answer](https://support.zendesk.com/hc/en-us/articles/4422584657434) if you've created one, or replies that it can't answer the question using the response configured in "If the AI agent can't answer the question." Choosing this type of reply hides the "After the AI agent answers" response.

### After the AI agent answers

Note: This section doesn't appear if you have selected the **Don't answer based on articles** option in the "If the AI agent finds relevant information" response.

When the AI agent presents an answer based on help center content, it follows up by asking whether suggested content was helpful. The "After the AI agent answers" response lets you configure the AI agent response when an end user says the answer was helpful or unhelpful.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bot_setup-after_bot_responds_Mar25_update.png)

**To configure the AI agent's response to customer feedback**

1. [On the Messaging behavior tab](https://support.zendesk.com/hc/en-us/articles/7510607688730#topic_slx_n4p_qtb), expand the **After the AI agent answers** section.
2. Click the **Helpful answer** tab and configure the following options:

   - **Message**: Enter a message to display when the end user says the suggested article was helpful, or use the default message provided. (*Great, knowledge is power. You can ask me another question at any time.*)
   - **Answers**: Use the drop-down to select up to 10 answers to present to customers as preconfigured options.
3. Click the **Unhelpful answer** tab and configure the options as described above.

   Offering an answer that includes the [Transfer to agent](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_zqr_gwc_k4b) step is a recommended best practice.

### If the AI agent can't answer the question

This response, also known as the fallback response, is triggered when there is no answer that matches the end user's question or comment.

You can configure this response to have the AI agent recommend relevant help center topics. This section is required. It must be configured before you can publish your AI agent.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bot_setup-no_relevant_answer_Mar25_update.png)

**To configure the fallback response**

1. [On the Messaging behavior tab](https://support.zendesk.com/hc/en-us/articles/7510607688730#topic_slx_n4p_qtb), expand the **If the AI agent can't understand a question** section.
2. Enter a message the AI agent will send if no help center articles are found, or if you do not have an active help center.

   The default fallback response is, *Sorry, I can't answer that. Here are some topics that might help though.*.
3. If you want, use the **Answers** drop-down to select up to 10 of your already-created answers to present to the customer.