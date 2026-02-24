# Amazon Connect attributes for Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9459017998618-Amazon-Connect-attributes-for-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Amazon Connect contact attributes are key-value pairs that store customer interaction data, helping you customize and optimize contact center operations. Key attributes include ticket ID for linking calls to tickets, conversation title for ticket naming, user ID for matching users by phone number, agent ID for identifying call responders, and call ID for tracking call objects. These attributes enhance your contact management capabilities.

Amazon Connect contact attributes are key and value pairs that store information about a customer interaction. Think of them as labels or tags that carry data throughout the lifecycle of a call, chat, or task within your contact center. Contact attributes are versatile and fundamental to customizing and optimizing your contact center operations.

The following are examples of Zendesk-specific contact attributes that you can use with Zendesk for Contact Center.

| | | |
| --- | --- | --- |
| **Contact attribute** | **Description** | **Notes** |
| zendesk\_ticket\_id | If this attribute is set in the contact flow, it's used to attach the call to the corresponding ticket with that ID or to create a new ticket with that ID. | |
| conversation\_title | This attribute is used for the ticket and voice comment title, otherwise it uses the default. | |
| zendesk\_user\_id | This attribute is set based on matching the user and phone number. | Using the value of this attribute from the contact flow is not currently supported. |
| zendesk\_agent\_id | The ID of the Zendesk user that answers the call. | |
| zendesk\_call\_id | The ID of the call object that Contact Center creates when an agent accepts a call. | |