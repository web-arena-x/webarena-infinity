# Available CRM actions for advanced AI agents and Zendesk Chat (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/8357750804250-Available-CRM-actions-for-advanced-AI-agents-and-Zendesk-Chat-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Configuring chat channels for advanced AI agents is no longer recommended.
Instead, consider [configuring messaging channels](https://support.zendesk.com/hc/en-us/sections/8264312886554) or [configuring email channels](https://support.zendesk.com/hc/en-us/sections/8264365933210).

- [Trigger reply](#h_01F4S0HEAF5BZNJWM90KPKGDG6)
- [Add tag](#h_01F4W2AQF5RZVJJZWTFFBWW77Z)
- [Get tag](#h_01F4W2C27KEVRGJSHMGQD275HT)
- [Leave channel](#h_01F4W3DD0JQYJPVK1GEQ6094EH)
- [Get visitor info](#h_01F4W3D0MF56GKE0388JPYMAEC)
- [Update visitor info](#h_01F4W3D0MF56GKE0388JPYMAEC)

Tip: For advice on configuring your AI agent to shorten handle time and manage chat history, see [Best practices for creating CRM actions for advanced AI agents in Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/8357720370330).

### Trigger reply

This is most commonly used to trigger a specific reply/intent, e.g. welcome reply, when a selected event happens.

## mceclip0.png

### Add tag

This action adds custom tags to a chat which helps you and your agents manage to get gain insights into your tickets in Zendesk Support. Understand more about [Reporting with tags in this Zendesk article](https://support.zendesk.com/hc/en-us/articles/360022183574-Reporting-with-tags).

This action can be used with the events below at the AI agent level:

- Chat started
- Chat escalation attempt
- Chat escalation failed
- Chat inactive

For example:![mceclip2.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip2_hsRqo.png)

It is also often used at intent and dialogue message levels to help your agent categorize tickets.

For example:

![mceclip2.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip2_PrlmN.png)

### Get tag

The Get Tag action allows you to pull existing tags from Zendesk Chat into the AI agents - Advanced Dashboard. By doing so we can trigger reply variation to give a more personalized dialogue flow.

In addition, by setting **Add Label** to be "true", you can view the same tags you have in Zendesk in our Conversation Logs as well for easier conversation data management.

The Get Tag action can be configured at the following chat events at the AI agent level:

- chat started
- chat escalation attempt
- chat escalation failed
- chat inactive

For example:

![mceclip1.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip1_CixTY.png)

### Leave channel

If you have high volumes and longer queues, it can be better to show the user their queue position when escalating. In the example below, the AI agent leaves the chat immediately and the user will see the queue and be able to rate the chat until a human agent picks up the conversation.

![mceclip0.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip0_Yi5lP.png)

### Get visitor info

This action allows you to retrieve visitor information on Zendesk. This information can then be saved to personalize your messages or create reply variations.

You can retrieve the information below:

- email
- current country
- current\_device\_type
- external\_id
- display\_name
- phone
- notes
- current\_tags
- current\_region
- current\_city

For example:

![mceclip0.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip0_jZi7Y.png)

### Update visitor info

This action allows the AI agent to fetch the information visitors offer during a conversation and update it on the visitor's Zendesk ticket.

You can update the information below:

- email
- notes

Updating email ensures the agent has the latest information to contact a visitor and notes act as a way for the AI agent to communicate to the agent.

Learn how to set it up in [Update Visitor Information - Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/8357757815450)

The notes field follows the visitor and not the chat. When using this please add another Update visitor info action to update the notes field with "-". Otherwise, the information in notes could cause confusion the next time the visitor chats again.