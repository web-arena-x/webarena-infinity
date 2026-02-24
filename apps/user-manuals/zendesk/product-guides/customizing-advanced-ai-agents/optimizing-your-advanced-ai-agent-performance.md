# Optimizing your advanced AI agent performance

Source: https://support.zendesk.com/hc/en-us/articles/8357751836314-Optimizing-your-advanced-AI-agent-performance

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Optimize the performance of your advanced AI agent by using analytics to identify
opportunities for improvement and by building smarter dialogues.

This article covers the following topics:

- [Using analytics to improve the AI
  model](#topic_lvj_zlg_p2c)
- [Using smarter dialogues to improve user
  experience](#topic_imm_ylg_p2c)

## Using analytics to improve the AI model

Use analytics to learn where you can improve AI agent understanding and the deflection
rate.

This section covers the following topics:

- [Improving deflection rate](#topic_rj4_1mg_p2c)
- [Reviewing other key metrics](#id_pzd_f44_wfc)

### Improving deflection rate

Any conversation that doesn’t end in escalation is considered deflected. Review
conversations that were not deflected and take steps to improve your deflection rate.

Read through [conversation logs](https://support.zendesk.com/hc/en-us/articles/8357749580186) to see how well your dialogues
work, looking for the following:

- **Broken dialogues**: A user might break a dialogue by not using the buttons provided,
  or by asking about their order number in the middle of the escalation flow. Consider
  including free text to guide users through the flow.
- **Misunderstanding instructions**: Users generally don’t always read
  long messages. Consider making the message shorter and easier to follow.
- **Missing information**: The user may lack key information to help
  them through the flow. In that case, think about what a live agent would do and add
  as much of that information in the dialogue as possible.

Take the following actions to improve deflection:

- **Adjust the default reply:** Manage expectations and guide users
  through flows. See [About system replies for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749481882).
- **Use content coverage analysis:** Identify potential new use cases that can be
  automated. See [Performing content coverage analysis](https://support.zendesk.com/hc/en-us/articles/8357758759322).
- **Use an API integration:** Identify suitable use cases for an API
  integration to automate more conversations. See [Preparing to create a custom integration](https://support.zendesk.com/hc/en-us/articles/8357756827674).

After taking steps to improve your deflection rate, review [resolution states](https://support.zendesk.com/hc/en-us/articles/8357756466586) as another way to improve your AI agent
performance. Filter conversation logs by custom resolution to review escalated and
unresolved conversations. Look for trends over time.

## Reviewing other key metrics

In the left sidebar of the AI agent, click Reporting for additional key metrics. To
optimize the AI agent’s performance, focus on the following metrics:

- Total conversations as compared to Understood conversations
- Assisted conversations and Handled conversations as compared to Escalated
  conversations
- Automated resolutions

For more, see [Analyzing advanced AI agent performance with the Reporting
dashboard](https://support.zendesk.com/hc/en-us/articles/9510024609178).

## Using smarter dialogues to improve user experience

Use the following tools to create smarter dialogues and improve your customers’ experience
with the AI agent:

- **Backend integrations**: Use [backend integrations](https://support.zendesk.com/hc/en-us/articles/8357756844442) where possible to fetch data that the
  advanced AI agent can provide to users.
- **Conditional blocks**: Use [conditional blocks](https://support.zendesk.com/hc/en-us/articles/8357733406234) to jump into another flow based on certain
  keywords. This provides a more streamlined conversation before escalation if the user
  has been through the flow before.
- **Escalation templates:** Streamline replies by managing the escalation
  process in one centralized [template](https://support.zendesk.com/hc/en-us/articles/8357756562330), rather than in each specific flow. Set [operating hours](https://support.zendesk.com/hc/en-us/articles/8357749686554) to manage expectations and [escalate](https://support.zendesk.com/hc/en-us/articles/8357756604186) appropriately.
- **A/B testing**: Use A/B testing to optimize dialogue flows with
  data-driven decisions. See [Performing A/B
  testing for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357758896410).
- **Confidence score**: (Expression-based AI agents only) Use the native parameter
  `confidence_score` in a conditional block to provide a fallback in
  replies where the AI agent might be less [confident](https://support.zendesk.com/hc/en-us/articles/8357749625498).
  - For messaging AI agents, if the score is below 90%, the AI agent can
    confirm the intent another way. For example, “I want to make sure I understand
    correctly. You’ve forgotten your password and want to reset it. Is that correct?”
  - For email AI agents, if the AI agent is less confident about a topic,
    you might omit a reply and only trigger the actions.