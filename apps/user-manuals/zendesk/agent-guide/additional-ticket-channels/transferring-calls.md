# Transferring calls

Source: https://support.zendesk.com/hc/en-us/articles/4408838843546-Transferring-calls

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

You can transfer calls to another group, agent, or external number.

This article includes the following topics:

- [Considerations for transferring calls](#topic_rt2_vbl_1fc)
- [Transferring a call](#topic_e1c_ncl_1fc)

## Considerations for transferring calls

Consider the following when deciding to transfer a call:

- To transfer calls, at least one phone number must have outbound calling enabled. This setting is on by default.
- When you transfer a call, call charges continue to be applied to both the incoming call and the outgoing call.
- When using omnichannel routing, if you're using ticket triggers to assign a group to tickets for calls, when an agent transfers the call to another group, it can cause the ticket trigger to fire and overwrite the agent's call transfer to another group. To avoid this, you can update your ticket triggers that assign a group to call tickets to include one of the following conditions:
 - **Ticket | Is | Create**: The ticket trigger fires only on newly created tickets rather than updates, such as a group transfer.
 - **Ticket > Comment text | Does not contain the following string | Call transferred**: The ticket trigger fires only on tickets that haven't been transferred.

## Transferring a call

When you transfer a call to a group, the call is added to the queue for that group until an agent from the group answers it; this is compatible with omnichannel routing through the standard queue. When you transfer a call directly to an agent, you can consult with the other agent before handing off the call.

With all types of transfers, the call's existing ticket opens automatically when the next agent takes the call.

**To transfer a call**

1. After you answer a call or make an outbound call, the associated ticket automatically opens. Click the transfer button from the ticket or the call console. The customer is placed on hold and hears the hold greeting.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_transfer_button.png)
2. Start typing the agent, group, or end user's name or phone number. The search will automatically suggest five results to choose from. If the agent or group you're looking for does not appear within the list of suggestions, type out the full agent or group name. To force an exact string match when searching the full name, enclose the name in quotes ("").
3. Click the agent or group's name to transfer a call. The list displays the state for each agent.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/transfer_3.png)
4. **If transferring to another agent:** You'll first be connected to the agent while the caller remains on hold. When you've finished consulting with the agent, click **Transfer**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_make_transfer.png)

   **If transferring to an external number**: You'll need to dial the number, including the country code. When the receiver is picking up, the **Transfer** option appears. You can then introduce your caller to the receiver, and click **Transfer**.

   Note: If an agent tries to transfer the call to an external number from a number that does not have outbound calling enabled, the call transfer is initiated from the phone number selected in the outbound caller ID of the agent transferring the call as shown in their call console.
5. The message **The call has been transferred successfully** appears in the window. At this point, the related ticket is also assigned to the other agent. A note is added to the ticket, indicating the call was transferred.
   Click **Close**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_transfer_success.png)