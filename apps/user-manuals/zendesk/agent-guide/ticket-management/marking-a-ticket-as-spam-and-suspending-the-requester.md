# Marking a ticket as spam and suspending the requester

Source: https://support.zendesk.com/hc/en-us/articles/4408842999066-Marking-a-ticket-as-spam-and-suspending-the-requester

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

You can mark a ticket as spam and suspend the requester at the same time. When you mark a ticket as spam, the following happens:

- The ticket is deleted and moved to the Deleted tickets view for 30 days until it is permanently deleted.
- The ticket requester is suspended and cannot submit or access tickets, or access your Help Center.

A ticket must be active (not Closed) to mark it as spam.

To recover a deleted ticket, you can [restore the deleted ticket](https://support.zendesk.com/hc/en-us/articles/224908967#topic_zmy_j24_xw) and [unsuspend the user](https://support.zendesk.com/hc/en-us/articles/203690976-Suspending-a-user). Any further tickets that the suspended user submits are added to the Suspended tickets view where you can review them (see [Understanding and managing suspended tickets and spam](https://support.zendesk.com/hc/en-us/articles/4408889141146-Understanding-and-managing-suspended-tickets-and-spam)).

You can also mark multiple tickets as spam at the same time. See [Bulk marking tickets as spam and suspending the requesters](https://support.zendesk.com/hc/en-us/articles/4408886890906#topic_qrv_crm_t4).

You can't mark tickets as spam if the ticket is associated with a user who was shared to your account.

Note: Agents must have the correct permissions to mark spam and suspend users. On non-Enterprise plans, agents must have access to all tickets set in their profile, as well as [permission to delete tickets](https://support.zendesk.com/hc/en-us/articles/4408832689818). On Enterprise, agents must be able to delete users and delete tickets [in their custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882).

Tip: Community tip from Colin: You can only assign the Spam permission to agents if you are willing to give them rights to delete tickets. Currently I give them a SPAM macro which simply puts the tickets in a queue for me to delete.

**To mark a ticket as spam and suspend the requester**:

1. Open the ticket you want to mark as spam.
2. Click the Ticket options menu in the upper right, then select **Mark as spam**.

   You will only see this option on tickets where the requester is an end-user.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket-options-menu.png)
3. Click **Immediately mark as spam** to confirm that you want to continue.

   The ticket will be deleted and cannot be recovered. The requester will be suspended. Alternatively you can click **Cancel**.

## Reporting on tickets marked as spam

You can't run reports on tickets marked as spam. This is because tickets marked as spam are deleted, and Explore only reports on active ticket data.

However, as a workaround, you can have your agents add a tag that indicates the ticket is spam. You can then use that information to generate reports on tags. For more information, see [Reporting with tags](https://support.zendesk.com/hc/en-us/articles/4408838151450).

This workaround is also helpful for some companies, such as regulated companies, that may not want to use the Mark as spam feature.

**To report on tickets marked as spam**

1. [Create a macro](https://support.zendesk.com/hc/en-us/articles/4408844187034) that adds a tag called *Spam* and then routes the tickets to a certain group or agent.
2. Train your agents to use this macro when they spot spam tickets.
3. [Create a view](https://support.zendesk.com/hc/en-us/articles/4408835059482#topic_cvw_rma_vb) of tickets with that tag.
4. Once a week or a month, have an agent or a group of agents check the view to ensure no tickets are miscategorized.

You can then use the tag to run reports on these tickets.