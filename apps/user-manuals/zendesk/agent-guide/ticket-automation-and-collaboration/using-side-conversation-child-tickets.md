# Using side conversation child tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408836521498-Using-side-conversation-child-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Collaboration add-on |

You can create side conversation child tickets and assign them to groups that you have access to or specific agents within those groups.

A side conversation child ticket is a separate ticket that is subordinate to a side conversation. Child side conversation tickets are useful when you need a formal way to track and measure requests associated with a side conversation. Side conversation tickets can also be routed to agents with [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514).

Side conversation child tickets must be [activated](https://support.zendesk.com/hc/en-us/articles/4408832279962) by an admin.

This article includes these sections:

- [About side conversation child tickets](#topic_gql_rlg_2nb)
- [Understanding light agent interaction with side conversation child tickets](#topic_vmd_yzq_3qb)
- [Creating side conversation child tickets](#topic_hbc_vmg_2nb)
- [Copying fields to child tickets](#topic_pyp_gcg_qtb)
- [Limitations](#topic_i1n_bng_2nb)

Related articles:

- [About side conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746)
- [Configuring side conversation child ticket settings](https://support.zendesk.com/hc/en-us/articles/8364222553498)

## About side conversation child tickets

When you create a side conversation child ticket, you're creating a side conversation on the original ticket and a new, separate, subordinate ticket that is assigned to a specific agent or group.

Side conversation and child ticket definitions:

- **Originating side conversation**: The side conversation on the original ticket used to create a side conversation child ticket.
- **Side conversation child ticket**: A ticket created from a side conversation.

There's a connection between the originating side conversation and the side conversation child ticket. This is a parent-child relationship. The originating side conversation is the “parent” and the child ticket is the “child.” You might think of these as linked tickets.

The child ticket inherits replies from the originating side conversation. When an agent replies to the side conversation on the original ticket, the replies are added to the child ticket. Depending on how an admin has configured side conversation child tickets, replies may be added as public comments or internal notes.

Child tickets have a unique external ID which is used to link the child ticket with a parent ticket. If you change a child ticket's external ID for any reason, the relationship with the parent ticket is broken and the child ticket no longer inherits data from the parent ticket.

Child tickets don’t inherit other forms of ticket data from the parent ticket. For example, if the status of the parent ticket changes, the status of the child ticket doesn’t automatically change. The same is true for adding tags to a ticket, and adding or removing CCs.

Some ticket fields can be copied from the parent ticket to the child ticket at the time of ticket creation (see [Copying fields to child tickets](#topic_pyp_gcg_qtb)).

Generally, there isn’t a reverse connection between parent and child tickets. The exceptions are that public comments on a child ticket become part of the side conversation and events in the parent ticket, and the status and assignee of the child ticket is displayed on the side conversation in the parent ticket.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conv_link_to_child.png)

When an [SLA is applied to a child ticket](https://support.zendesk.com/hc/en-us/articles/4408846166426), marking the side conversation as [Done](https://support.zendesk.com/hc/en-us/articles/4408844206746#topic_nj2_jj4_l2b) in the parent ticket doesn’t fulfill **First time reply** and **Next time reply** metrics because the child ticket isn't updated by that action.

## Understanding light agent interaction with side conversation child tickets

Light agents can't create, send, or be assigned side conversation child tickets.

[Light agents have permission to make private comments](https://support.zendesk.com/hc/en-us/articles/4408846501402), so it's possible for them to open an existing child ticket Support and add a private comment to the ticket. However, because of the inheritance pattern between parent and child tickets, that private comment won't appear in the side conversation interface of the parent ticket.

## Creating side conversation child tickets

You can create, send, and be assigned to side conversation child tickets. The child tickets you create can be assigned only to groups that you have access to or specific agents within those groups.

You may notice some minor differences in the side conversations user interface, depending on which side conversation channels your administrator has activated.

Side conversations are created from the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sc_context_panel_start.png)

**To create a side conversation child ticket**

1. In a ticket, open the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362) and click the **Side conversations** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_side_conversations.png)) icon, then click the plus sign (+).
2. Select **Ticket**.

   Note: The composer opens immediately if no other side conversation channels are available.

   The side conversation child ticket composer opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conv_child_new_composer.png)
3. In the **To** field, specify an agent or group.

   Note: You can assign child tickets only to groups that you have access to and the agents within those groups. Light agents can’t be assigned to child tickets.
4. Fill out the subject and message body, including any inserted comments and attachments as needed (see [Using side conversations in tickets](https://support.zendesk.com/hc/en-us/articles/4408844206746)).
5. (Optional) Click the **Set child tickets fields** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conv_copy_to_child_ticket_icon.png)), specify which types of ticket field data you want copied from the parent ticket to the child ticket, and click **Add**. See [Copying fields to child tickets](#topic_pyp_gcg_qtb).
6. Click **Send**.

## Copying fields to child tickets

When you create a side conversation child ticket, you may be able to copy the following ticket fields from the parent ticket [depending on how an admin has configured your account](https://support.zendesk.com/hc/en-us/articles/8364222553498):

- **Tags**: The tags on the parent ticket, at the time the child ticket was created, will be added to the child ticket.
- **Followers**: The followers of the parent ticket, at the time the child ticket was created, will be added as followers on the child ticket.
- **Ticket form**: The parent ticket's form and field values, at the time the child ticket was created, will be set on the child ticket.
- **Requester**: The ticket requester.

An admin may configure certain ticket fields to be copied to the child ticket by default.
When this occurs, the default fields appear in the list of fields to be copied to the child ticket but aren’t available in the selector.

Copying fields to a child ticket is a one time-event that occurs only when the ticket is created. For example, if the parent ticket is updated later on, and the data in those ticket fields change, the child ticket is not updated to match.

**To include ticket fields in a side conversation child ticket**

1. [Create a side conversation child ticket](https://support.zendesk.com/hc/en-us/articles/4408836521498#topic_hbc_vmg_2nb).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sc_child_ticket_create_fields.png)

   The ticket fields that are available to be copied appear in the **Fields** section
2. Click the **Set child ticket fields** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conv_copy_fields_icon.png)).
3. Select the fields that you want to copy from the parent ticket to the child ticket, then click **Add**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sc_child_ticket_fields_selector.png)
4. Click **Send**.

## Limitations

The following limitations exist for side conversation child tickets:

- Notification emails will trigger twice.
- When side conversation child tickets are enabled, [ticket triggers for side conversations](https://support.zendesk.com/hc/en-us/articles/4408893545882) will fire twice. For example, once for the originating side conversation, and once for the side conversation child ticket.
- For agents assigned to custom roles to create child tickets through side conversations, they must have permission to create side conversations and make public comments in tickets. See [Creating custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882).
- In certain cases, agents may be able to assign child tickets to groups that they don’t have access to. For example, if they use a macro that’s available to them that assigns a child ticket to a group to which they don’t have access.
- When a side conversation ticket is assigned to a [private group](https://support.zendesk.com/hc/en-us/articles/4767122732058), it is visible to members who don't belong to the group.