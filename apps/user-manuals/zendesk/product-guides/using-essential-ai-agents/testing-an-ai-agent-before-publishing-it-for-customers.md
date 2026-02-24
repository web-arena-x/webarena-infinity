# Testing an AI agent before publishing it for customers

Source: https://support.zendesk.com/hc/en-us/articles/9462994470810-Testing-an-AI-agent-before-publishing-it-for-customers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article applies to [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690) and [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality).

At any point in an AI agent’s lifecycle, you can test its behavior to make sure it
performs the way you expect it to. This helps you iron out any issues with its
configuration before you make the AI agent live for your customers for the first time,
or before rolling out any changes to its settings.

You must be an admin to test an AI agent.

This article contains the following topics:

- [About testing AI agents](#topic_abn_l3m_dgc)
- [Testing a messaging AI agent](#topic_pjc_m3m_dgc)
- [Testing an email or web form AI agent](#topic_gp1_n3m_dgc)

## About testing AI agents

You can use the Test AI agent button in Admin Center to test your AI agent. When you
do, you have a chance to examine its behavior from initiating a conversation to
closing a ticket, including:

- How its [standard responses](https://support.zendesk.com/hc/en-us/articles/8774095741466) work, including
  greeting, feedback, fallback, and escalation messages
- How well its AI-generated responses address potential customer questions
- How other settings affect the conversation, such as the [persona](https://support.zendesk.com/hc/en-us/articles/8753435048474), [instructions](https://support.zendesk.com/hc/en-us/articles/9203004883994), or [language support](https://support.zendesk.com/hc/en-us/articles/4408842754202)
- How and when triggers run, including [out of office](https://support.zendesk.com/hc/en-us/articles/4408842866074) and [CSAT](https://support.zendesk.com/hc/en-us/articles/4408886173338) messaging triggers

When testing your AI agent, real tickets are created, so you might want to let your
agents know that you’re testing before you begin. However, test conversations
created using the Test AI agent button don't count toward your account's [automated resolutions](https://support.zendesk.com/hc/en-us/articles/5352026794010) and don't appear in related
Explore reports or dashboards.

Additionally, when you use the Test AI agent button, the system evaluates all [instructions](https://support.zendesk.com/hc/en-us/articles/9203004883994) with a status of Active and To be
activated.

Note: Testing an AI agent using the Test AI agent button, or
testing an AI agent in a [sandbox environment](https://support.zendesk.com/hc/en-us/articles/6150628316058), does not count
against the default allocation of [automated resolutions](https://support.zendesk.com/hc/en-us/articles/5352026794010) for your
account.

### Limitations of testing AI agents

You can't use the Test AI agent button to test the following:

- [Restricted help center content](https://support.zendesk.com/hc/en-us/articles/8087943201306)
  (where sign-in is required to see content)
- [Proactive messages](https://support.zendesk.com/hc/en-us/articles/5381304334234)
- (AI agent legacy functionality) [Answers](https://support.zendesk.com/hc/en-us/articles/4422584657434) that contain errors or
  that reference restricted help center content

### Options for testing your AI agent

Some account plans have options for testing an AI agent without exposing it to
customers by creating a test brand or using a sandbox.

- **Test brand**: On certain plans, you can create multiple brands. If
  you’re on a supported plan, you can create a brand with a help center
  specifically for testing purposes. See [Setting up multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829476378).
- **Sandbox**: On Enterprise plans, you can create a [sandbox environment](https://support.zendesk.com/hc/en-us/articles/6150628316058) for testing.
  Messaging configurations and AI agents are not automatically copied into the
  sandbox environment and must be manually recreated. See [Testing messaging in your sandbox](https://support.zendesk.com/hc/en-us/articles/4408844075930)
  and [Creating an AI agent to automatically
  resolve customer issues](https://support.zendesk.com/hc/en-us/articles/4408824263578).

## Testing a messaging AI agent

You can use the Test AI agent button to test the behavior of an AI agent on a
messaging channel.

**To test a messaging or web form AI agent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the name of the AI agent you want to test.
3. Click **Test AI agent**.

   The testing sidebar opens with the Messaging tab
   selected.
4. Have a conversation with the AI agent by entering messages or selecting
   options.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_test_ai_agent_messaging.png)
5. To change the AI agent’s language, use the language drop-down.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_test_ai_agent_change_language.png)

   Note: The language drop-down doesn't affect
   AI-generated answers, which are sent in the same language you use to ask
   the question. For more information, see [Understanding language support in AI
   agents](https://support.zendesk.com/hc/en-us/articles/4408842754202#topic_x2q_3ff_3fc).
6. To reset and start a new conversation, click the Reload icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_refresh_icon.png)).

## Testing an email or web form AI agent

You can use the Test AI agent button to test the behavior of an AI agent on an email
or web form channel.

**To test an email or web form AI agent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the name of the AI agent you want to test.
3. Click **Test AI agent**.

   The testing sidebar opens.
4. Select **Email** tab.
5. Enter a **Subject line** and **Email text**, then click
   **Send**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_test_ai_agent_email.png)

   After a moment, the AI
   agent’s response is returned.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_test_ai_agent_email_response.png)
6. To change the AI agent’s language, use the language drop-down.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_test_ai_agent_change_language.png)
7. To reset and start a new conversation, click **Test again**.