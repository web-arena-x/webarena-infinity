# Creating an AI agent to automatically resolve customer issues

Source: https://support.zendesk.com/hc/en-us/articles/4408824263578-Creating-an-AI-agent-to-automatically-resolve-customer-issues

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article applies to [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690#topic_zps_zmk_f2c) and [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality). For
equivalent functionality for [AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/6970583409690#topic_zps_zmk_f2c), see [Creating an advanced AI agent to automatically resolve customer
issues](https://support.zendesk.com/hc/en-us/articles/8357749415066).

[AI agents](https://support.zendesk.com/hc/en-us/articles/6970583409690) interact with customers on
messaging, email, API, and web form channels to resolve issues without human
intervention. You can create an AI agent that responds to your customers in a
conversational manner using information sourced from your existing help center.

You must be an admin in both Support and Knowledge to create an AI agent.

This article contains the following topics:

- [About AI agents for messaging, email, API, and web form](#topic_vb2_ynd_f2c)
- [Creating an AI agent](#topic_dw4_xnd_f2c)
- [Cloning an AI agent](#topic_rts_jfr_r5b)
- [Deleting an AI agent](#topic_r5b_xnm_dgc)

Related articles:

- [Viewing and configuring settings for AI
  agents](https://support.zendesk.com/hc/en-us/articles/6447052708762)
- [Publishing an AI agent to make it live for
  customers](https://support.zendesk.com/hc/en-us/articles/7232810932250)

## About AI agents for messaging, email, API, and web form

If you have an active help center, AI agents deliver automated, AI-generated answers
in response to customer requests, with information from your own trusted help center
content.

On messaging channels, when an AI agent identifies a relevant help center article, it
sends the customer a single conversational message with a link to the source
article. These replies are always followed by a request for end-user feedback (“Was
this helpful? Yes/No”).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_ai_agent_coffee_example.png)

On email, API, and web form channels, an AI agent sends a longer generative AI
response based on relevant help center content, including direct links to the
articles.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_ai_agent_email_example.png)

Note: AI-generated replies on email, API, and web form channels
aren't visible to the customer when they [check the request from the help
center](https://support.zendesk.com/hc/en-us/articles/4408846805530#topic_zhh_w2k_cgc).

If you’re using restricted help center content, AI agent
responses respect the article view permissions, which means:

- If the customer is authenticated, the AI agent can use relevant restricted
  articles to generate its response.
- If the customer is unauthenticated, the AI agent can use only public articles to
  generate its response.

For more information, see [Using restricted help center content in AI agent
responses](https://support.zendesk.com/hc/en-us/articles/8087943201306).

## Creating an AI agent

Creating an AI agent means you’re adding the ability to use the AI agent as a
responder for that channel. Until you [add an AI agent to a specific channel and publish it](https://support.zendesk.com/hc/en-us/articles/7232810932250),
the default response remains active for that channel.

These instructions assume you've already created a [messaging](https://support.zendesk.com/hc/en-us/articles/4408827701530), [email](https://support.zendesk.com/hc/en-us/articles/4887918604058), [API](https://support.zendesk.com/hc/en-us/articles/4408889192858), or [web form](https://support.zendesk.com/hc/en-us/articles/4408882701338) channel.

**To create an AI agent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click **Create AI agent**.

   The Create an AI agent page
   opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_create_ai_agent.png)
3. In **Name**, enter a name for the AI agent.

   This name appears at the
   top of the Web Widget in messaging conversations and as the sender in
   emails. Choose a name that makes it clear customers are not talking to a
   human.
4. Select a **Tone of voice**:
   - **Professional**: (Default) A polite and direct tone.
   - **Informal**: A casual and friendly tone.
   - **Enthusiastic**: An upbeat and friendly tone.
5. In the **Brand** drop-down, select a brand to apply to the AI
   agent.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_create_ai_agent_brand.png)

   If the help center for
   the brand you selected is not active, you’ll see an error message with a
   link to the help center that needs to be activated before you can
   proceed.
6. Click **Next**.

   A test version of your AI agent appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_create_ai_agent_test.png)
7. Test your AI agent to be sure it performs the way you expect.

   For help,
   see [Testing an AI agent before publishing
   it for customers](https://support.zendesk.com/hc/en-us/articles/9462994470810).
8. Choose your next step:
   - Click **Advanced settings** to configure additional settings that
     affect the AI agent’s behavior. See [Viewing and configuring settings
     for AI agents](https://support.zendesk.com/hc/en-us/articles/6447052708762).
   - Click **Go to publish** to publish the AI agent. The AI agent
     won’t be available to customers until it’s published. See [Publishing an AI agent to make it
     live for customers](https://support.zendesk.com/hc/en-us/articles/7232810932250).

## Cloning an AI agent

You can clone an existing AI agent, then use it as the starting point for
building a new one.

**To clone an AI agent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Find the AI agent you want to clone.
3. Click the AI agent's options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Clone**.

   The AI agent is
   copied and added to the end of your AI agent list. It has the same
   name as the original AI agent, appended with "(copy)".
4. Choose your next step:
   - Configure additional settings that affect the AI agent’s
     behavior. See [Viewing and configuring
     settings for AI agents](https://support.zendesk.com/hc/en-us/articles/6447052708762).
   - Publish the AI agent. The AI agent won’t be available to
     customers until it’s published. See [Publishing an AI agent to
     make it live for customers](https://support.zendesk.com/hc/en-us/articles/7232810932250).

## Deleting an AI agent

If you’re no longer using an AI agent and don’t plan on using it in the future, you
can delete it. When you delete an AI agent, any connected channels revert to their
default response settings.

Important: Deleting an
AI agent cannot be undone.

**To delete an AI agent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Find the AI agent you want to delete.
3. Click the AI agent’s options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Delete**.
4. In the confirmation dialog, review the information and click
   **Delete**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_delete_ai_agent.png)

   The AI agent is removed
   from the list.