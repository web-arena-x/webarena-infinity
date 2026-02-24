# Best practices for creating answer flows in an AI agent (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4965031536794-Best-practices-for-creating-answer-flows-in-an-AI-agent-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Tip: This article describes functionality available only to customers who had a drafted or published AI agent as of February 2, 2025.

After you [create AI agent](https://support.zendesk.com/hc/en-us/articles/4408824263578) for a messaging channel, there are a number of best practices regarding answer flows that can make your AI agent more effective.

This article contains the following sections:

- [Planning your answers](#topic_amz_g3x_tbc)
- [Building answers](#topic_mq4_xw1_1vb)
- [Improving answer-to-question matching](#topic_evs_xw1_1vb)

## Planning your answers

Before you start creating answers for your AI agent, consider these planning best practices:

- **Identify questions that users ask regularly.** Look at your top ticket issues, review common help center search terms, and talk to your agents to plan answers you want to create for the AI agent.
- **Create answers first for questions that can be resolved on their own** and don’t need an agent to take action. Examples of common, easily-answered questions might include:
 - Operating hours
 - Reset password
 - Store locations
- **Start by answering the most common questions first.** It's a good idea to have answers for about 20 of your most common questions, then build up coverage over time. Don't try to address every issue right away.

## Building answers

As you [create your answers](https://support.zendesk.com/hc/en-us/articles/4422584657434) for your AI agent, consider these best practices for how to structure your answers for better performance.

### Engaging the user

When you are thinking about the start of your answer to engage the user, keep these best practices in mind:

- **Start each answer by echoing the user's issue back to them.** This reduces the risk of confusion if the Ai agent matches to the wrong answer. For example, if a user enters "Cancel my account," the AI agent response should be, "Sorry to hear you want to cancel your account."
- **Help end-users understand how they should navigate the AI agent.** Depending on how the AI agent is designed, different end-user interaction styles can impact the AI agent's performance. Make it clear to the user how they should navigate the AI agent to find answers.
 - **Ask the user to select from provided options** throughout the answer, if the AI agent is designed to provide a navigation experience (one large answer flow).
 - **Create a separate agent transfer answer** to enable the user to contact support. [Link the agent transfer answer](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_bq2_232_d1c) throughout the main navigation experience as an alternative option if the presented options aren’t what the user needs.
- **Create separate answers to handle small talk.** For example, you might create a sign off response, such as "Thanks, goodbye."

### Finding a solution

As you build the answer to guide the user to a solution, keep these general best practices in mind:

- **Avoid building out overly complex flows to specific articles.** Instead, leverage generative replies to automatically return an answer.
 This helps minimize answer maintenance for your.
- **Personalize your customer experience.** Create personalized experiences by [requiring authentication](https://support.zendesk.com/hc/en-us/articles/4411666638746), [including conditional scenarios](https://support.zendesk.com/hc/en-us/articles/5280598023450), or [using intents](https://support.zendesk.com/hc/en-us/articles/5537827011994).
- **Create autonomous actions for the user** by [making an API call](https://support.zendesk.com/hc/en-us/articles/4572971586586) to another system. Doing so, you can automate a majority of user requests, such as making a return, from end-to-end.
- **Provide a resolution** to ensure each answer addresses a question.
 For example, state the answer to the question in an AI agent message, provide a link to a help article, or perform a task with an API call.

### Closing out the conversation

When you are thinking about the end of your answer and how to close it out, keep these best practices in mind:

- **Ask for feedback to confirm the user's problem has been resolved.** You can [ask if question was resolved](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_n2v_p23_q5b)
 to ensure the user's issue is revolved. You can also use this feedback to analyze AI agent effectiveness later.
- **Provide alternative options to eliminate dead ends.**
 - **If an API call fails**, provide an option to [transfer to agent](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_zqr_gwc_k4b) or [link to related answers](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_bq2_232_d1c). For example, if an order status retrieval fails, provide a link to an article about how users can manually check their order status.
 - **If you ask for feedback**, and the user indicates that the problem has not been solved, provide alternative options. Consider adding an option to transfer to agent or link to related answers that might help.
 - **If a user contacts you outside of business hours,** provide an escalation option to transfer to agent, so the user can create a ticket and an agent can respond later asynchronously.

## Improving answer-to-question matching

You can improve the chances of the AI agent suggesting the right answer or article to a user by manually adding training phrases or by assigning intents to answers. To use intents, you must have an intent model assigned.

### Using training phrases

You can [use training phrases in answers](https://support.zendesk.com/hc/en-us/articles/4422584657434) to improve the AI agent matching performance. If you have an intent model, you should use intents instead of training phrases.

When you use training phrases, keep these best practices in mind:

- **Make note of how users word common questions** and use similar language in training phrases for the answer.
- **Group common topics together in one answer.** For example, include international shipping and domestic shipping in one answer.
- **Use phrases with similar or related meanings.** Zendesk AI utilizes a model that employs semantic matching, where the model considers the overarching meaning of the question. For example, "solar power" and "renewable" are semantically related, and the model can recognize this connection. The model may also suggest two texts as a match if they are likely to co-occur, such as "credit card" and "bank account."
- **Add a variety of phrases** to improve the match rate.
 However, you don’t need to add every single variant for how the question might be asked. For example, a user might misspell something or phrase it a little differently and still get a match.
- **Aim for a minimum of 3-5 training phrases** for each answer.
- **Avoid adding single words.** AI agent training works best with short, multiple-word phrases that provide enough details for context. For example, use “Refund order” instead of “Refund," or use "Renew membership" instead of "Renew."
- **Avoid using unnecessary words and generic phrases** such as "Hi" or “I want to” or "How do I." These can dilute the question's core meaning. For example, instead of "Hi, I want to get a refund," use “Get a refund."
- **Do not add training phrases in multiple languages.** Training phrases are auto-translated, if enabled.

### Using pre-trained intents

If you have an intent model, you can assign [pre-trained intents](https://support.zendesk.com/hc/en-us/articles/5537827011994) to answers instead of manually adding training phrases. When you use intents, keep these best practices in mind:

- **Assign pre-trained intents to answers** to significantly improve the question-answer match performance.
- **Use generative replies for intents that are frequently asked questions.** These common questions can typically be resolved by the AI agent using information from your help center articles.