# Updating visitor information for advanced AI agents and Zendesk Chat (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/8357757815450-Updating-visitor-information-for-advanced-AI-agents-and-Zendesk-Chat-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Configuring chat channels for advanced AI agents is no longer recommended.
Instead, consider [configuring messaging channels](https://support.zendesk.com/hc/en-us/sections/8264312886554) or [configuring email channels](https://support.zendesk.com/hc/en-us/sections/8264365933210).

There are two pieces of visitor information that can be updated in Zendesk:
**Email** and **notes**.

- Email refers to the visitor’s email
- Notes are for agents to see only

This article shows what both actions look like in Dialogue Builder in our Dashboard, also what they look like in Zendesk from an agent’s viewpoint.

- [In Dialogue Builder](#h_01F6VXV2T0CJ0PYZEBTTF02X92)
 - [How to set it up](#h_01F6VXV7QGCK51ZZVFBASG5RRX)
- [Agent's viewpoint](#h_01F6VXWGJMFG3MRQ341XNVXED0)

## In Dialogue Builder

If **update visitor notes** is used, there needs to be an action set up on the AI agent level to reset it. This is because the notes field follows the user and not the chat. (See step 3 below).

![ZDChat-_dialogue_builder.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_ZDChat-_dialogue_builder.png)

## How to set it up

1. Check the box for **C****ollect Parameter** and use **Entity recognition** to verify input.

![75266616-bba6-4ae2-b93c-014adbb907d2.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_75266616-bba6-4ae2-b93c-014adbb907d2.png)

![d652190f-2079-4305-8529-e10e7e8f0e19.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_d652190f-2079-4305-8529-e10e7e8f0e19.png)

2. Add action to update email and notes.

![02ba5386-e047-4757-8085-5b6b792d73b1.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_02ba5386-e047-4757-8085-5b6b792d73b1.png)

3. Reset Notes by adding an action in Settings > Actions.

![7fb40428-ad72-4670-9fab-e2b36af80e9f.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_7fb40428-ad72-4670-9fab-e2b36af80e9f.png)

#### This is needed because the notes field follows the user and not the chat. And if it’s not reset, the information would stay there and could cause confusion when the user chats again.

4. That’s it! You’re ready to go
🙂 Don’t forget to test it. In addition, letting your client know (and making sure they give their support team a visual heads up) what the agent view is like helps shorten Agent Handle Time!

## 

## Agent’s viewpoint

1. Both Email and Notes are updated instantly BEFORE the chat ends.
2. Agent sees a message in the chat log indicating the email change but not Notes.

![90621f99-ae9c-45bf-9484-fbcce6c8f71b.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_90621f99-ae9c-45bf-9484-fbcce6c8f71b.png)