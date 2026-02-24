# Creating an advanced AI agent to automatically resolve customer issues

Source: https://support.zendesk.com/hc/en-us/articles/8357749415066-Creating-an-advanced-AI-agent-to-automatically-resolve-customer-issues

---

AdvancedAI agentsinteract with customers on messaging and email channels to resolve issues without human intervention, freeing up your support team to spend more time on more complex issues.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

For equivalent functionality for [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690#topic_zps_zmk_f2c) and [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality), see [Creating an AI agent to automatically resolve customer issues](https://support.zendesk.com/hc/en-us/articles/4408824263578).

Advanced [AI agents](https://support.zendesk.com/hc/en-us/articles/6970583409690) interact with customers on messaging and email channels to resolve issues without human intervention, freeing up your support team to spend more time on more complex issues.

You must be a [client admin in AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/4408832171034#topic_thq_lnf_dgc) to create an advanced AI agent.

This article contains the following topics:

- [About advanced AI agents](#topic_cck_r12_fhc)
- [Creating an advanced AI agent](#topic_nyf_s12_fhc)
- [Cloning an advanced AI agent](#topic_mkr_hb3_23c)

## About advanced AI agents

Advanced AI agents offer deeper functionality and more configurability than [essential AI agents](https://support.zendesk.com/hc/en-us/articles/6970583409690#topic_zps_zmk_f2c). Essential AI agents offer generative replies only, while advanced AI agents also include features such as [scripted conversation flows](https://support.zendesk.com/hc/en-us/articles/8357749494810), [generative procedures](https://support.zendesk.com/hc/en-us/articles/8979864563610), [full API access and orchestration](https://developer.ultimate.ai/), and [advanced analytics](https://support.zendesk.com/hc/en-us/articles/9510024609178).

Within the AI agents - Advanced add-on, there are three types of advanced AI agents:

- **AI agents with agentic AI**: These AI agents can use [generative procedures](https://support.zendesk.com/hc/en-us/articles/8979864563610) to interact with users in a more natural, human-like way, engaging in small talk and working through complex or vague issues by identifying the necessary next steps and asking follow-up questions where needed. AI agents with agentic AI can also use generative AI-powered [use cases](https://support.zendesk.com/hc/en-us/articles/9041901679130) when you need more fine-tuned control.

 On messaging channels, all newly created AI agents use agentic AI by default, and the type can't be changed.
- **Zero-training AI agents**: These AI agents use generative AI-powered [use cases](https://support.zendesk.com/hc/en-us/articles/9041901679130) to understand a customer's message and link to an appropriate scripted conversation flow, which may also include AI-generated responses.

 On email channels, all newly created AI agents are zero-training by default, and the type can't be changed. Zero-training AI agents can no longer be created on messaging channels, but you may have already created some that you continue to maintain.
- **Expression-based AI agents (Legacy)**: These legacy AI agents use manually trained [expressions](https://support.zendesk.com/hc/en-us/articles/8357751704474) to understand a customer’s message and link to an appropriate scripted conversation flow.

 Expression-based AI agents can no longer be created, but you may have already created some that you continue to maintain.

## Creating an advanced AI agent

You can create an advanced AI agent in the AI agents - Advanced add-on.

By default, all newly created AI agents use [agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066) for messaging channels and [zero-training](https://support.zendesk.com/hc/en-us/articles/8357749447194) for email channels, and this cannot be changed.

**To create an advanced AI agent**

1. In [AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8357756913178), click **AI agent management** in the sidebar, then select **Create AI agent**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_create_ai_agent.png)
2. In **AI agent name**, enter a descriptive name for your AI agent.
3. In **Channel**, select either **Messaging** or **Email**, depending on what type of channels you want your AI agent to work for.
4. In **Industry**, select one of the following options that best fits the industry the AI agent will be used for:
   - **Airline**
   - **Gaming**
   - **Telecommunication**
   - **E-Commerce**
   - **Banking**
   - **Other** 

     If your exact industry isn't available as an option, select the closest fit. This setting impacts benchmarks and other industry-related settings throughout your account.
5. In **Select language**, select the language your AI agent should use.

   Tip: You can [add more supported languages](https://support.zendesk.com/hc/en-us/articles/8357749666714)
   later.
6. In **Icon**, select an icon that should be associated with the language you selected.
7. Click **Create**.

Your AI agent is created, but it won’t interact with your customers until you [connect it to your chosen channels](https://support.zendesk.com/hc/en-us/articles/8724978128282#topic_tn3_bd2_fhc).

Note: Currently, you can’t delete an AI agent. To request that an AI agent be deleted, [contact Zendesk customer support](https://support.zendesk.com/hc/en-us/articles/4408843597850).

## Cloning an advanced AI agent

You can clone an existing advanced AI agent. This is helpful if you want to use it as a starting point for a new AI agent, or if you want to copy an AI agent between your production and sandbox environments.

When you clone an advanced AI agent from one environment to another (such as from production to sandbox), any [API integrations](https://support.zendesk.com/hc/en-us/articles/8357756844442) in the source environment are also cloned to the target environment, if they don’t already exist. When this happens:

- The cloned API integration is named “<API integration name> (Clone)”.
- If the source API integration has an authentication integration, that’s cloned too.
- No changes are made to the source API integration.
- API integrations in dialogue flows in the cloned AI agent are automatically replaced with the cloned versions of the API integrations.

**To clone an advanced AI agent**

1. In [AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_vtf_2vd_mgc), click **Organization management** in the sidebar, then select **Organization management**.
2. In the AI agents list, find the AI agent you want to clone.
3. Click the **Duplicate** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/duplicate_icon.png)) icon.

   A dialog appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_cloning_ai_agent.png)
4. In **AI agent name**, enter a name for the cloned AI agent.
5. In **Select organization**, select the organization you want to clone the AI agent to (either your production or sandbox environment).
6. Click **Duplicate**.

If you clone an advanced AI agent within the same environment, the integration with messaging or email is automatically configured, and you don’t need to do any additional setup to integrate it.

If you clone a messaging AI agent between your production and sandbox environments, the integration with messaging is automatically configured. If you clone an email AI agent between production and sandbox, you must [connect the AI agent to email](https://support.zendesk.com/hc/en-us/articles/8357750858010) in the new environment.