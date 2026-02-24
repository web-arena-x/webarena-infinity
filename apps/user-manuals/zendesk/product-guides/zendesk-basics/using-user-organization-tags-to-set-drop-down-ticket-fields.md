# Using User / Organization Tags to Set Drop-Down Ticket Fields

Source: https://support.zendesk.com/hc/en-us/articles/6554073287706-Using-User-Organization-Tags-to-Set-Drop-Down-Ticket-Fields

---

Setting a drop-down ticket field adds the tag for that field value to the ticket. The inverse is also true: adding a tag to a ticket that corresponds to a drop-down field will cause that field to set to the value that corresponds to the tag. This behavior is documented [in this article](https://support.zendesk.com/hc/en-us/articles/4408881943194#:~:text=If%20you%20add,same%20associated%20tag.).

A newly created ticket automatically adds [the user and organization tags of its requester and organization](../end-users-and-organizations/adding-tags-to-users-and-organizations.md). These user/organization tags are applied to the ticket after its initial submission, but before conditional field rules and triggers are applied. This means they can overwrite field-selections made by the user and have the potential to impact business rules.

This "tag inheritance" can be used to one's advantage by creating user/organization fields which have tags identical to ticket fields. When that's the case, the values would function as follows:

1. **User field** setting applies a **User tag**
2. **User tag** gets applied as **Ticket tag** to tickets requested by that user
3. **Ticket tag** sets Ticket field to value that corresponds to the tag

This can be used in a few workflows, and is a relatively straightforward way to have certain types of user/organization fields set ticket fields. That said, there are a few areas that could interact with this sort of workflow. Here are two things to consider:

1. **Conditional Field requirements**This feature can cause ticket creation to fail if user/organization tags set a ticket field in a way that conditionally requires fields. Be mindful of this when creating user/organization fields which include tags (drop-down, multi-select, checkbox types)
2. **Automatic Ticket Tagging**Zendesk has a feature that can automatically apply tags to tickets at creation based on its text. This feature is [documented here](https://support.zendesk.com/hc/en-us/articles/4408829424794-Enabling-and-disabling-ticket-tags#topic_ynp_ds4_bfb). These automatic tags could set ticket fields. If using automatic ticket tagging, please ensure your ticket fields' tags are unique enough that they are unlikely collide with the automatic tagging feature. For example - having a field with the tag `other` or `email` is far more likely to collide than `field_name_value_other` or `ticket_channel_email`