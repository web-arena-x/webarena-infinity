# Checking operating hours and agent availability during conversations with advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749686554-Checking-operating-hours-and-agent-availability-during-conversations-with-advanced-AI-agents

---

During conversations between users and advanced AI agents, operating hours and agent availability can be used to determine how the AI agent should respond based on those factors.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

During conversations between users and advanced AI agents, operating hours and agent
availability can be used to determine how the AI agent should respond based on those factors.

You might leverage operating hours and agent availability in the following scenarios:

- **Escalation flows**: When a user asks to be escalated to a human agent, the AI agent
  can check whether it's within operating hours and whether any team members are
  available.
- **Processes with team-specific transfer flows**: For teams working different hours,
  the AI agent can check hours and change the response as needed.
- **System replies for welcome, default, and failed escalation**: When system replies
  are sent, the AI agent can provide different responses based on operating hours.

This article contains the following topics:

- [Setting operating hours](#topic_p3s_mjr_m2c)
- [Checking operating hours in a conversation flow](#topic_rlj_4jr_m2c)
- [Checking team availability in a conversation flow](#topic_epb_pjr_m2c)

Related article:

- [About escalation strategies and flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756604186)

## Setting operating hours

Operating hours define the working hours for your human agents. You can define different
time zones and operating hours for different teams to support multi-region teams. Operating
hours are available for email and chat.

**To set operating hours**

1. In AI agents - Advanced, in the top-right corner, use the AI agent drop-down field to
   select the AI agent you want to set operating hours for.
2. In the left sidebar, click **Settings** > **AI agent settings**
3. Select the **Operating hours** tab.
4. Click **Create rule**.
5. In **Rule name**, enter a descriptive name for the rule
6. In the **Time zone** drop-down, select a time zone.
7. Select the appropriate days of the week and specify the operating hours for each
   day.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_operating_hours_rule.png)
8. Click **Save**.

## Checking operating hours in a conversation flow

After you define your operating hours, you can check them during conversations to determine
how your AI agent should respond.

**To check operating hours**

1. [Create a new dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810#topic_ygq_4ym_g2c) or [open an existing one](https://support.zendesk.com/hc/en-us/articles/9066753203738#topic_nvb_tzl_52c).
2. Add an **Availability** block.

   For help, see [Using the dialogue builder to create conversation flows for advanced
   AI agents](https://support.zendesk.com/hc/en-us/articles/8357749494810).
3. In the first drop-down, leave **Operating hours** selected.
4. In the second drop-down, select the operating hours rule you created above.
5. Define the AI agent's response based on the branch:
   - **Open**: Add an **Escalation** block with a message and escalation
     method.

   - **Closed**: Add an **AI agent message** block explaining your hours, or
     additional follow-up options for the customer as needed.

     For additional help, see
     [About escalation strategies and flows for
     advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756604186).

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_operating_hours_simple_example.png)
6. Click **Save** to save your work for later, or click **Publish** to make your
   changes live.

## Checking team availability in a conversation flow

You can check whether agents are available before escalating or offering additional
options.

Regardless of whether you use [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514), this check assesses the Support status for
the agents within the escalation group. If any agent is online, the team is considered
available. If you want to check for agents' messaging status instead, [contact Zendesk customer support](https://support.zendesk.com/hc/en-us/articles/4408843597850) and ask that messaging-based team
availability be turned on.

**To check team availability**

1. [Create a new dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810#topic_ygq_4ym_g2c) or [open an existing one](https://support.zendesk.com/hc/en-us/articles/9066753203738#topic_nvb_tzl_52c).
2. Add an **Availability** block.

   For help, see [Using the dialogue builder to create conversation flows for advanced
   AI agents](https://support.zendesk.com/hc/en-us/articles/8357749494810).
3. In the first drop-down, select **Team availability**.
4. In the second drop-down, enter the ID of the team (group) you want to check availability
   for.

   For help, see [How can I retrieve the group ID in Support?](https://support.zendesk.com/hc/en-us/articles/4408837673114)
5. Define the AI agent's response based on the branch:
   - **Open** (agents are available): Add an **Escalation** block with a message
     and escalation method.
   - **Closed** (no agents are available): Add an **AI agent message** block
     explaining that no agents are available, or additional follow-up options for the
     customer as needed.

     For additional help, see [About escalation strategies and flows for advanced AI
     agents](https://support.zendesk.com/hc/en-us/articles/8357756604186).

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_agent_availability_simple_example.png)