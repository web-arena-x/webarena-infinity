# About events for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749555610-About-events-for-advanced-AI-agents

---

Add-on | AI agents - Advanced

Add-on | AI agents - Advanced

Events occur during conversations and are used to trigger [AI agent-level actions](https://support.zendesk.com/hc/en-us/articles/8357756651290#topic_nnm_znl_rgc) within the conversation
or in a CRM platform. This setup allows you to automate responses and processes based on
specific events within the conversation.

Which events are available depends on whether your advanced AI agent is configured for
email or messaging.

This article contains the following topics:

- [Available events for messaging AI agents](#topic_gg5_hvl_rgc)
- [Available events for email AI agents](#topic_lpq_3vl_rgc)

Related articles:

- [About actions for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756651290)
- [Creating and adding actions for advanced AI
  agents](https://support.zendesk.com/hc/en-us/articles/8357756623770)
- [Reviewing and managing actions for advanced AI
  agents](https://support.zendesk.com/hc/en-us/articles/8566644914202)

## Available events for messaging AI agents

The table below describes the events available for messaging AI agents.

|  |  |
| --- | --- |
| **Event name** | **Description** |
| Session ended | The AI agent automation has completed. This event occurs when the conversation ends, an escalation attempt happens, or the conversation reaches the end of the session duration. After this event, the conversation is ready to be evaluated for an [automated resolution](https://support.zendesk.com/hc/en-us/articles/8357756668186).  Any further messages from the AI agent will be part of a new session, which is evaluated separately. As an action trigger, you might want to use session end to mark the end of the automation with a tag or label. |
| Conversation ended | The conversation was ended by the customer, or the conversation ended after the configured session duration. |
| Conversation escalated to human | The conversation was successfully handed over from the AI agent to a human agent. |
| Conversation escalation attempt | The AI agent attempts to hand over the conversation to a human agent. |
| Conversation escalation failed | The AI agent attempted to hand over the conversation to a human agent, but encountered an issue. |
| Conversation started | A new conversation has started. |
| Conversation inactive | The conversation has been inactive (no end-user messages) for the configured session inactivity duration. |
| Suggestion used | A human agent used a suggested answer. |
| The end of a procedure is reached | (Available only for AI agents with agentic AI) The AI agent has reached the end of a generative procedure and the specified amount of time has passed. |
| A knowledge answer is shared | (Available only for AI agents with agentic AI) The AI agent has shared an AI-generated answer. |

## Available events for email AI agents

The table below describes the events available for email AI agents.

|  |  |
| --- | --- |
| **Event name** | **Description** |
| Ticket received by AI agents - Advanced | A message is received by AI agents - Advanced and a ticket is created in your CRM platform.  This event is best used for actions that affect the rest of the process, like collecting user information. AI agents - Advanced will process the contents of the message only after this event. |
| Ticket processed by AI agents - Advanced | The contents of the message have been processed by AI agents - Advanced.  This event is best used to update the platform with dynamic session data, like phone number or email, using [entities](https://support.zendesk.com/hc/en-us/articles/8357749723546). |
| Reply delay timer started | The AI agent reply node has been reached and the delay timer started. This event is selectable only if you’ve [set up a ticket reply delay](https://support.zendesk.com/hc/en-us/articles/8357772433562).  This event can be used to add tags and internal notes to your tickets. Scheduled messages are not visible in CRM platforms, so we recommend setting up an agent view in a way that issues with scheduled answers are hidden and not mistaken for open tickets. |
| Reply sent after delay | The AI agent reply has been sent after the set delay. This event is selectable only if you’ve [set up a ticket reply delay](https://support.zendesk.com/hc/en-us/articles/8357772433562).  This event can be used to add post-reply updates to your tickets, ensuring your agents will be able to see issues that were previously hidden, but later were answered with delay. |

### Sequence of events for email AI agents

Events for email AI agents are always triggered in the following order:

1. **Ticket received by AI agents - Advanced** event and related
   actions
2. Use case–level actions and block-level actions
3. **Ticket processed by AI agents - Advanced** event and related
   actions
4. **Reply delay timer started** event and related actions
5. **Reply sent after delay** event and related actions