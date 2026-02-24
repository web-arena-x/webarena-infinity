# Configuring auto assist to work with messaging tickets originated from AI agents (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9696147377562-Configuring-auto-assist-to-work-with-messaging-tickets-originated-from-AI-agents-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

This article describes functionality
available only to customers who
had a drafted or published an AI agent as of February 2, 2025.

Auto assist is an AI-powered assistant for your agents. Using large language
model (LLM)
technology, auto assist understands the contents of submitted tickets
and makes
suggestions to your agents on how to solve them.

After you've
[turned on auto assist](https://support.zendesk.com/hc/en-us/articles/8013454025114),
you can select which AI
agents should work with auto assist. The AI agent will hand off a conversation
to auto
assist when the customer requests to speak to an agent. From the customer’s
point of
view, they are still transferred to a human agent because auto assist
answers are
reviewed by the agent and sent under their name.

The instructions below assume
you’ve
already
[created an AI agent](https://support.zendesk.com/hc/en-us/articles/4408824263578)
and
[added an answer](https://support.zendesk.com/hc/en-us/articles/4422584657434)
that includes the
[Transfer to agent](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_zqr_gwc_k4b)
step type.

**To connect an AI agent with auto assist**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Select the AI agent you want to connect with auto assist.
3. On the **Answers** tab, select an existing
   answer that includes the Transfer
   to agent step type.
4. In bot builder, select the Transfer step.
5. In the **Tags** field in the panel
   on the right, enter
   **agent\_copilot\_enabled**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_auto_assist_adding_tag_bot_builder.png)
6. (Optional) Add another tag to identify which
   [procedure you’ve created](https://support.zendesk.com/hc/en-us/articles/7924047699738)
   for auto
   assist to follow in this situation (for example,
   *copilot\_order\_cancellation*). Later, you
   can
   [create an Explore report](https://support.zendesk.com/hc/en-us/articles/7739110419610)
   that uses
   this tag to identify tickets where a specific procedure was followed
   on a
   ticket.
7. If possible, update the **Bot message**
   field to reiterate what issue the
   customer needs help with. For example, “Let me connect you with
   a customer
   support agent to help with canceling your order.” This helps
   auto assist
   identify the right procedure to use when assisting the agent.
8. Click **Done**.
9. Click **Publish bot**.

   The next time the AI agent transfers a customer to
   an agent who has access to auto assist, auto assist will
   suggest replies for
   the agent in the Agent Workspace composer.