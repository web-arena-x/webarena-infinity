# Creating Quick Connects (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731437749658-Creating-Quick-Connects-Engage-Legacy

---

Quick connects in Amazon Connect are shortcuts for transferring contacts to a queue, a specific agent, or an external number. They help agents efficiently handle contacts by reducing the steps required for a transfer.

‍

## Creating quick connects

When you create a Quick Connect, you specify the following:

‍

- **Type:** Determines where the contact can be transferred. It could be a queue, a user, or an external number.
- **Destination:** The specific queue, user, or number where the contact will be transferred.
- **Description:** A short note to describe the purpose of the quick connect.
- **Phone Type:** For 'External Number' type, you also specify whether it's a Direct Inward Dial number (DID) or a Toll-Free number.

Note: E.164 format is required for external phone-number-based quick connects

Here's how to create quick connects:

1. In the [Amazon Connect Dashboard](https://aws.amazon.com/connect/) go to **Routing** and then **Quick connects**.
2. Click **Add quick connect**.
3. Fill out the details like name, description, type, and contact destination.
4. **Save** the quick connect.

![](https://support.zendesk.com/hc/article_attachments/9731466162074)

Remember, Quick Connects are made available to agents through routing profiles. You can assign multiple Quick Connects to a routing profile, providing agents with various transfer options based on the current contact or situation.

For more information on quick connects please see the AWS documentation:

<https://docs.aws.amazon.com/connect/latest/adminguide/quick-connects.html>

‍