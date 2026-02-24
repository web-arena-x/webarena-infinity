# About AI agents with agentic AI

Source: https://support.zendesk.com/hc/en-us/articles/8966284087066-About-AI-agents-with-agentic-AI

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

AI agents that use agentic AI are designed to solve complex user requests with limited direct human supervision. These AI agents are capable of autonomous decision-making, planning, and adaptive execution throughout the course of a conversation. This means they can interact with users in a more natural, human-like way, engaging in small talk and working through complex or vague issues by identifying the necessary next steps and asking follow-up questions where needed.

By leveraging agentic AI, AI agents increase your automation rates and reduce the load on human agents and admins, while still providing the level of service your customers expect.

This article contains the following topics:

- [Benefits of AI agents with agentic AI](#topic_lf2_g42_52c)
- [Capabilities of AI agents with agentic AI](#topic_dgw_h42_52c)
- [Considerations and current limitations of AI agents with agentic AI](#topic_ecj_k42_52c)
- [Next steps](#topic_w4t_l42_52c)

Related articles:

- [Getting started with AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8724978128282)
- [Creating generative procedures for AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8979864563610)

## Benefits of AI agents with agentic AI

AI agents with agentic AI accelerate your path to 80% automation with minimal setup, full control, and built-in transparency. Powered by adaptive reasoning, these AI agents autonomously determine the most effective path to a resolution, handling even the most nuanced queries across every channel.

AI agents with agentic AI shift the paradigm of automated conversations. Instead of relying on rigid dialogue flows, they:

- **Are purpose-built for service**: Unlike other solutions that focus on broad enterprise workflows, these AI agents are designed for service to resolve even the most nuanced queries.
- **Are easier to deploy and scale**: Deploy these AI agents in minutes, not months—no complex flows, rigid templates, or manual training required.
- **Provide better customer experiences**: These AI agents don’t just execute tasks—they ask clarifying questions, determine the best actions, and adjust in real-time for natural, contextual interactions.
- **Offer quality you control**: Stay in command with full visibility into AI decision-making and the flexibility to let these AI agents operate autonomously or follow controlled workflows, ensuring every resolution meets your standards.

Ultimately, AI agents with agentic AI move past the limitations of scripted chatbots and first-wave generative bots, delivering higher automated resolution rates, lower operational costs, and a more engaging experience for end users.

## Capabilities of AI agents with agentic AI

The table below summarizes the main capabilities of AI agents with agentic AI.

| Capability | Description |
| --- | --- |
| Upgraded AI agent builder | Move away from fully scripted dialogues by simply describing your business policies and letting the AI agent create generative procedures that run the conversation autonomously. However, you still retain the ability to decide which topics should remain under scripted dialogues and which should use generative procedures. Also, generative procedures power multilingual AI agents. You can write a procedure once, in a single language, and it can serve all the languages your AI agent supports. |
| Integrations and actions | The AI agent uses AI-driven procedures that can integrate your existing session and CRM actions, API calls, and more. All you need to do is to provide the AI agent with additional context in the form of an API description. |
| Adaptive reasoning | The AI agent analyzes each request from the user, identify the issue, determine the best next actions, and adapt dynamically within the boundaries of your business procedures. They evaluate context, pinpoint missing information, and ask follow-up questions. Most powerfully, AI agents with agentic AI are capable of addressing multiple distinct issues within the same user request. |
| Reasoning controls | In the conversation logs, you can see the reasons behind an AI agent’s actions and decisions. Monitor how they solve problems, audit every conversation, and refine behaviors to ensure confidence in each resolution. |

## Considerations and current limitations of AI agents with agentic AI

As you get started with AI agents with agentic AI, keep in mind the following considerations and current limitations:

- **Not available for email**: These AI agents are not available on the email channel.
- **No support for rich-text formatting in generative procedures**: The generative procedures used by these AI agents don’t support rich-text formatting (for example, buttons and carousels). However, rich-text formatting is supported in dialogues.
- **No support for search rules in generative procedures**: The generative procedures used by these AI agents don’t work with [search rules for knowledge sources](https://support.zendesk.com/hc/en-us/articles/8357749301658#h_01HA1SAF2KBZFV3H010JCCDN47).
 That means you cannot have multiple knowledge sources and ask the AI agent to use only specific ones for certain users. However, search rules still work with AI agents that use dialogues.
- **Must have a persona**: These AI agents must have an [AI agent persona configured](https://support.zendesk.com/hc/en-us/articles/8357758773658). Without a persona, a technical error will appear for every message the AI agent receives.
- **Modifications to the escalation reply**: These AI agents introduce a new escalation system reply, which is triggered automatically whenever a user asks to be escalated or if an admin references "escalation" inside a [generative procedure](https://support.zendesk.com/hc/en-us/articles/8979864563610). For AI agents converted from zero-training to agentic AI, you should copy your current escalation reply and paste it inside the new escalation system reply, then deactivate or delete your old escalation reply.

## Next steps

See [Getting started with AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8724978128282)
to learn how to create and configure an AI agent with agentic AI.