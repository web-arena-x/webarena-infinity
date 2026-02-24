# Routing tickets to groups with advanced AI agents and  Zendesk Chat (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/8357765404058-Routing-tickets-to-groups-with-advanced-AI-agents-and-Zendesk-Chat-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Configuring chat channels for advanced AI agents is no longer recommended.
Instead, consider [configuring messaging channels](https://support.zendesk.com/hc/en-us/sections/8264312886554) or [configuring email channels](https://support.zendesk.com/hc/en-us/sections/8264365933210).

Routing here refers to the logic of setting the AI agent department to be
the first to take incoming chats, and escalating to the transfer department,
or, the human department when needed.

This article is part of the steps to take to
[connect your AI agent to Zendesk Chat.](https://support.zendesk.com/hc/en-us/articles/8357757747354)

## Before you start

- Rule of thumb: Each AI agent needs its own department. The human-agent
  department can have many human agents, but the AI agent should
  never be in the human-agent department.
- Routing logic: The AI agent department is the default department
  and only escalates to the human department based on your dialogue
  flow.

## Creating departments

1. Go to **Zendesk Chat**
   > **Settings** >
   **Groups**, then click
   **Add group**

   - Once you click on
     **Add group, a** new
     tab might open and take you to
     **Zendesk Support**
     > **People**
     > **Group.** This
     is normal and you can just continue as below.

#### The AI agent department should ONLY have the AI agent's admin account and the AI agent's admin account should ONLY be in the AI agent's department.

![Screen_Shot_2022-04-15_at_3.08.29_PM.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_Screen_Shot_2022-04-15_at_3.08.29_PM.png)

2. Enter
a name (e.g. "EN AI agent Department") for the group. Add only the new AI
agent's admin account created in
[preparation](https://support.zendesk.com/hc/en-us/articles/8357765350682)
to the group, then
click **Create group**

The new AI agent's admin account should be the only member in the
AI agent's group.

3. Repeat the steps above and create a transfer group for human agents that
will be taking escalated chats from the AI agent if needed. The AI agent
should not be in this group. This group should not be set as the default
group.

## Enabling the groups

If you are doing these in advance, keep these AI agent and human
agent groups disabled - and only
**enable them on launch day.**

If you’re doing these on launch day, make sure the groups are enabled
before you continue.

Go back to
[connecting your AI agent to Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/8357757747354)