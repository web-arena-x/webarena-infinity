# Using AI to generate replies in an AI agent for messaging (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/6138268212634-Using-AI-to-generate-replies-in-an-AI-agent-for-messaging-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

This article applies only to
customers who had any drafted or published AI agents before February 2,
2025. Customers on [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690) have
access to AI agents that, by default, [use generative AI to respond to
customer requests](https://support.zendesk.com/hc/en-us/articles/4408824263578#topic_vb2_ynd_f2c).

Generative replies allow your AI agent to deliver automated, AI-generated answers in
response to customer requests. These replies:

- Use information from your own trusted help center content.
- Give end users the information they need without having to leave the
  conversation to read an article.
- Don't require you to create or maintain custom [answer flows](https://support.zendesk.com/hc/en-us/articles/4422584657434).

Data shows that generative replies are typically three times more capable of
returning relevant responses to customer questions as opposed to answer flows.

This article contains the following topics:

- [About generative replies in legacy AI agents for messaging](#topic_uxm_2lp_zyb)
- [Activating generative replies](#topic_hxr_2lp_zyb)
- [Using generative replies with intents](#topic_qzx_2lp_zyb)

## About generative replies in legacy AI agents for messaging

If you have an active help center, your AI agent can use generative replies to immediately
respond to questions from your end users. These responses use generative AI
to evaluate all the articles in your help center, then use that knowledge to
provide concise, contextually relevant answers within the ongoing
conversation.

When a relevant help center article is identified, generative replies are
displayed as a single message. These messages are short (generally under 100
words) and reflect the [AI agent’s persona](https://support.zendesk.com/hc/en-us/articles/8753435048474). Any articles
used to generate the response appear as links underneath the message.

Generative replies are always followed by a standard request for end-user
feedback (“Was this helpful - yes/no”). You can [configure how the AI agent responds to
this feedback](https://support.zendesk.com/hc/en-us/articles/7510607688730#topic_m5t_41n_gbc).

For generative replies, the language the AI agent uses depends on the language
of the user’s initial message:

- If the user’s language is [supported](../multiple-language-support/zendesk-language-support-by-product.md#h_01GYJ1PBVKD26QN3E8JNS3X3TX:~:text=Languages%20supported%20by%20Zendesk%20AI%20agents), the AI agent
  replies in that language.
- If the user’s language is not supported, the AI agent replies in the
  [account’s default
  language](https://support.zendesk.com/hc/en-us/articles/4408887059866#topic_rtc_42j_1y).

For [standard responses](https://support.zendesk.com/hc/en-us/articles/8774095741466) and messages
sent as part of an [answer flow](https://support.zendesk.com/hc/en-us/articles/4422584657434) (legacy), the AI
agent uses the [language set on the Settings
tab](https://support.zendesk.com/hc/en-us/articles/4408842754202#topic_rzn_3cj_bpb).

If some or all of your help center is restricted, generative replies respect the view permissions
set on articles. For details, see [Using restricted help center content in
AI agents for messaging](https://support.zendesk.com/hc/en-us/articles/8087943201306).

If your account doesn't have an assigned intent model, your AI agent uses
generative replies to respond to customer questions as soon as you [activate generative
replies](#topic_hxr_2lp_zyb). If your account *does* have an assigned intent
model, your AI agent uses generative replies to respond to customer
questions only in the following scenarios:

- An intent matching that question is configured to generate a reply.
- No intents are detected for that question.

For details, see [Using generative replies with intents](#topic_qzx_2lp_zyb).

## Activating generative replies

When you [create a new AI agent,](https://support.zendesk.com/hc/en-us/articles/4408824263578) generative replies are
activated by default. If you have any existing AI agents that don’t use
generative replies yet, you can update the [“If the AI agent finds relevant
information” standard response](https://support.zendesk.com/hc/en-us/articles/7510607688730#topic_nvy_p3b_ccc) so that the AI agent uses
generative replies.

**To activate generative replies in an existing AI agent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to activate generative replies
   for.
3. Select the **Messaging behavior** tab.
4. Click the **If the AI agent finds relevant information**
   section to expand it.
5. Select **Generate a reply**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/generative_replies_relevant_info_updated.png)
6. (Optional) Click **Test AI agent**, then enter phrases the AI
   agent can match to existing help center content to view samples
   of replies your end users might receive.
7. Click **Publish AI agent** to apply your changes.

If your account doesn't have an assigned intent model, your AI agent now
uses generative replies to respond to customer questions. If your
account has an assigned intent model, proceed to the next section to
make sure generative replies are active for all intents.

## Using generative replies with intents

Note: Your account must have an assigned intent model to use generative replies
with intents. If you don't have an intent model, you can apply for
eligibility by [contacting your Zendesk Sales representative](https://support.zendesk.com/hc/en-us/articles/4408843597850-).

When you [activate generative replies](using-ai-to-generate-replies-in-an-ai-agent-for-messaging-legacy.md#topic_hxr_2lp_zyb),
replies are generated for questions that match intents without assigned
answers and for questions without a matching intent.

This section covers the following topics:

- [Using generative replies for questions with specific intents](#topic_xpr_3l2_ybc)
- [Using generative replies for questions without matching intents](#topic_nzq_jl2_ybc)

### Using generative replies for questions with specific intents

By default, any intent without an assigned answer will generate a reply.
For each intent, you can leave this setting as-is (recommended),
update it to not generate a reply, or add the intent to an answer in
your AI agent for messaging.

**To use generative replies for questions with specific intents**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to manage generative replies for.
3. Select the **Intents** tab.
4. In the **Answer** column, click the drop-down to select an
   option for each intent you want to update:
   - **Generate a reply** (recommended) lets the AI
     agent create an AI-generated response to a
     customer’s matching free-text entry.
   - **Don’t generate a reply** prevents the AI agent
     from responding to a customer’s matching free-text
     entry. Instead, it replies with the standard
     fallback response (“Sorry I couldn't answer your
     question”).
   - **Show an answer** lets you connect the intent to
     an existing answer or [create a new
     answer](https://support.zendesk.com/hc/en-us/articles/4422584657434) for it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/generative_replies_intent_options.png)
5. Click **Publish AI agent** to apply your changes.

### Using generative replies for questions without matching intents

You can generate a reply for any question asked by an end user that does
not have a matching intent.

**To use generative replies for questions without matching
intents**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to manage generative replies for.
3. Select the **Intents** tab.
4. In the **Questions without matching intents** drop-down, select
   one of the following options:
   - **Generate a reply** (recommended) lets the AI
     agent create an AI-generated response to a
     customer’s matching free-text entry.
   - **Don’t generate a reply** prevents the AI agent
     from responding to a customer’s matching free-text
     entry. Instead, it replies with the standard
     fallback response (“Sorry I couldn't answer your
     question”).

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/generative_replies_intent_tab.png)
5. Click **Publish AI agent** to apply your changes.