# Using an AI agent in the Slack Direct Messages channel

Source: https://support.zendesk.com/hc/en-us/articles/5501378203802-Using-an-AI-agent-in-the-Slack-Direct-Messages-channel

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article applies to [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690) and [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality).

You can add an AI agent to your [Slack Direct Messages channel](https://support.zendesk.com/hc/en-us/articles/4629038081306) to deliver automated AI
agent functionality to your Slack-messaging connection.

Note: This doesn't apply to the [Slack for Zendesk Support integration](https://support.zendesk.com/hc/en-us/articles/4408833756698).

This article contains the following topics:

- [Account requirements, feature limitations, and best practices](#topic_rrv_cpp_zxb)
- [Adding an AI agent to your Slack DM channel](#topic_cdz_cpp_zxb)
- [Removing an AI agent from your Slack DM channel](#topic_mxc_dpp_zxb)

## Account requirements, feature limitations, and best practices

Before adding an AI agent to your Slack DM configuration, your account must meet the following
requirements:

- [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4581758611866) and [messaging](https://support.zendesk.com/hc/en-us/articles/4408827701530) activated
- At least one [Chat-enabled agent](https://support.zendesk.com/hc/en-us/articles/4408882929946)
- The [Slack Direct Messages channel for Zendesk
  messaging](https://support.zendesk.com/hc/en-us/articles/4629038081306) activated
- An AI agent (You can use a previously built AI agent or [create a new one](https://support.zendesk.com/hc/en-us/articles/4408824263578).)

Some AI agent features perform differently in the Slack DM channel than in other messaging
channels:

- The [greeting response](https://support.zendesk.com/hc/en-us/articles/7510607688730#topic_e41_f1q_hvb) does not appear in the
  conversation.
- (Legacy AI agent functionality) The [Ask for details step](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_i5r_grz_n5b) is not available in the
  Slack DM channel. If it is included as part of an answer in your
  conversation flow, it will be bypassed.
- (Legacy AI agent functionality) Panels in the [Add carousel](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_il3_pmj_tvb) step are displayed in a list,
  rather than as a scrollable array. Otherwise, they function as expected.

Because of the above limitations, there are a number of best practices we recommend when creating
your AI agent:

- Turn off the [automated fallback response](https://support.zendesk.com/hc/en-us/articles/7510607688730#topic_umz_cft_byb).
- Create a trigger to [immediately close solved tickets](https://support.zendesk.com/hc/en-us/articles/4408824482586#topic_xbt_3sq_5pb).
- (Legacy AI agent functionality) Because the greeting response is not active
  in the conversation, we recommend [creating an answer](https://support.zendesk.com/hc/en-us/articles/4422584657434) that includes a welcome
  message, with conversation starters (such as “hello”) as intents.

## Adding an AI agent to your Slack DM channel

When your account is ready, you can integrate the AI agent with your Slack DM channel.

**To add the AI agent to your Slack DM channel**

1. Sign in to Slack using the [dedicated Zendesk user account](https://support.zendesk.com/hc/en-us/articles/4629038081306#topic_rtk_w2w_v5b).
2. In Admin Center, [configure the AI agent's
   channels](https://support.zendesk.com/hc/en-us/articles/9543022336794) so that the Slack DM channel is
   selected.
3. [Publish the AI
   agent](https://support.zendesk.com/hc/en-us/articles/7232810932250).

## Removing an AI agent from your Slack DM channel

If you no longer want to include an AI agent in your Slack DM channel, you can disconnect it. The
channel will then resume Slack DM Support functionality.

When you disconnect the AI agent from the channel:

- Conversations that have been handed off to an agent are
  unaffected.
- If the end user interacts with the AI agent, for example by entering text or clicking a button,
  they are handed off to an agent. This is a “silent handoff”, and the end
  user will not receive an automated response or notification of the handoff
  until the agent responds.

**To remove the AI agent from your Slack DM channel**

1. In Admin Center, [configure the AI agent's
   channels](https://support.zendesk.com/hc/en-us/articles/9543022336794) so that the Slack DM channel is deselected.
2. [Publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250).

Note: Adding the AI agent to another channel automatically removes it from the Slack DM
channel.