# Merging tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408882445594-Merging-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

If needed, you can merge one or more tickets into another ticket. You might do this if you receive two support requests about the same issue from the same end-user, for example.

Note: If you are on the Enterprise plan, ticket merging is not automatically enabled for agents. You must check the **Can merge tickets** box for your agent roles. See [Creating custom roles and assigning agents](https://support.zendesk.com/hc/en-us/articles/4408882153882-Creating-custom-roles-and-assigning-agents-Enterprise-#topic_cxn_hig_bd).

It's also possible to merge a group of tickets into a single ticket. See [Bulk merging tickets](https://support.zendesk.com/hc/en-us/articles/4408886890906#topic_k5w_mnf_wf).

Ticket merging rules:

- The tickets must be less than Solved. You can merge an unsolved ticket into a Solved ticket. Doing this will not reopen the Solved ticket.

 If an admin has [activated custom ticket statuses,](https://support.zendesk.com/hc/en-us/articles/4412575841306) then the tickets must have a status that belongs to a status category that is less than Solved.
- The tickets can't be shared with another Zendesk Support instance via Ticket sharing. If you unshare a ticket, it can be merged.
- If you have ticket CCs enabled:
 - You can merge two tickets with different requesters. The requester of the ticket you close with the merge is added as a CC to the new ticket.

    Note: A message appears when you merge tickets with different requesters. Make sure that you're not unintentionally sharing sensitive information when merging tickets across requesters before you continue.
 - If anyone was CC'd on an original ticket, they are also added as a CC on the merged ticket.
- If you don't have ticket CCs enabled, you can only merge two tickets if they are from the same requester.
- The most recent public comment from the ticket being closed with the merge appears in the merge window. You can choose to remove or edit the comment.
 Otherwise, the most recent public comment is included in the new ticket's comment with a link to the closed ticket. You can review previous comments in the closed ticket. No other comments appear directly in the new ticket.
- Ticket fields, including Tags, Type, Priority, and Status, aren't carried over from the ticket being closed with the merge. Only fields that are filled out in the new ticket are saved.
- Merges are permanent and can't be undone.
- The ticket that's closed with the merge has the tag *closed\_by\_merge* added.
- You can use [this Explore report](https://support.zendesk.com/hc/en-us/articles/4408843359898) to exclude tags with the *closed\_by\_merge* tag. However, you can't produce reports based on the fields of the ticket that was closed by the merge. For more details, see [What Explore reporting options are available for merged tickets?](https://support.zendesk.com/hc/en-us/articles/4419174418202)
- Merged tickets lose any HTML formatting.
- [AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346) can’t be merged.

**To merge one ticket into another ticket**

1. Open the ticket that you want to merge into another ticket.
2. Click the Ticket options menu in the upper right, then select **Merge into another ticket**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket-options-menu.png)
3. You can enter a ticket number, select one of the ticket requester's open tickets, or select one of your recently viewed tickets.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/merge_tickets_1.png)

   If you’re attempting to merge a ticket into a ticket with a different organization, brand, or requester, a message appears.
4. Make sure that you aren’t unintentionally sharing sensitive information by merging the tickets, then click **Continue Merge**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/merge_tickets_warning_PII.png)
5. When you select a ticket to merge into, you'll be prompted to confirm the merge.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/merge_tickets_2.png)

   Note: There is a known issue where Markdown might inappropriately render in merged ticket comments, even if Markdown is not enabled.
6. Decide if you want the requester to see the merge comments.

   You can edit the merge comments that are added to each ticket and choose whether you want the requester can see the comments.

   To hide merge comments from requesters, deselect **Requester can see this comment** for both merge comments. Admins can also [set the default privacy for all ticket comments](https://support.zendesk.com/hc/en-us/articles/4408822560410) to make merge comments deselected by default.

   If you remove all text from the comment box, the most-recent comment from the merged ticket will appear as the updated ticket comment.
7. Select **Confirm and Merge**.

   Be sure that you merge the correct tickets. Ticket merges are final; you cannot undo or revert a ticket merge.

   The ticket that was merged into another ticket is closed.