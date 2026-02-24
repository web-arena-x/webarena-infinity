# Creating quick connects for transferring calls in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9790964307098-Creating-quick-connects-for-transferring-calls-in-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Quick connects let you transfer calls to a queue, agent, or external number with fewer steps. You can set up multiple quick connects in routing profiles, giving agents flexible transfer options. When creating a quick connect, specify the type, destination, description, and phone type, ensuring the use of E.164 format for external numbers. This streamlines call handling and enhances customer interactions.

[Quick connects](https://docs.aws.amazon.com/connect/latest/adminguide/quick-connects.html) in Amazon Connect are shortcuts
for transferring contacts to a queue, a specific agent, or an external number. They help
agents efficiently handle contacts by reducing the steps required for a transfer.

Quick connects are available to agents in routing profiles. You can assign
multiple quick connects to a routing profile, providing agents with various transfer
options based on the current contact or situation.

**To create a quick connect**

1. In the [Amazon Connect Dashboard](https://aws.amazon.com/connect/), select **Routing** >
   **Quick connects**.
2. Click **Add quick connect**.
3. Complete the following:
   - **Type** determines where the contact can be transferred. It
     could be a queue, a user, or an external number.
   - **Destination** indicates the specific queue, user, or number
     where the contact will be transferred.
   - **Description** is a short note to describe the purpose of the
     quick connect.
   - **Phone type** is either a soft phone or a desk phone. For
     external numbers, you also specify whether it's a Direct Inward Dial number
     (DID) or a toll-free number. For quick connects to external phone numbers,
     E.164 format is required.
4. Click **Save**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_extra_18.png)