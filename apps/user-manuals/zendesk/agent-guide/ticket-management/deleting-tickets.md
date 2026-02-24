# Deleting tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408883872538-Deleting-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Some support teams never delete tickets; they instead move them through their workflow to
close them using an automation. You can, however, delete a ticket if you want. Deleted tickets
are moved into a Deleted Tickets view, where you can restore them or permanently delete them.
After 30 days deleted tickets are permanently deleted and removed from the Deleted Tickets
view.

Note: If you want your agents to be able to delete tickets, you must grant them permission.
For help, see [Enabling agents to delete tickets](https://support.zendesk.com/hc/en-us/articles/4408832689818).

This article contains the following sections:

- [Deleting a ticket](#topic_2xq_jm4_xw)
- [Deleting tickets from user profiles and views](#topic_wkz_q2p_2fc)
- [Undoing a ticket deletion](#topic_yy4_wm4_xw)
- [Permanently deleting a ticket](#topic_5ll_km4_xw)

Related topics:

- [Viewing and recovering deleted tickets](https://support.zendesk.com/hc/en-us/articles/4408835089050)

## Deleting a ticket

If needed, you can delete a ticket. Deleted tickets are moved into a Deleted tickets view for 30
days, where you can restore them or permanently delete them.

You can also delete multiple tickets at the same time. For more information, see [Bulk deleting tickets](https://support.zendesk.com/hc/en-us/articles/4408886890906#topic_d5y_3mf_wf).

[AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346) can’t be deleted unless they’re in the Solved or
Closed status.

**To delete a ticket**

1. Open the ticket that you want to delete.
2. Click the Ticket options menu in the upper right, then select **Delete**.

   The Ticket
   options menu looks slightly different in the [Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) (shown on the left) and the standard
   agent interface (shown on the right).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_options_delete.png)
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket-options-menu.png)

   You'll be asked to confirm that you want to delete the
   ticket.
3. Click **OK** to confirm that you want to delete the ticket.

   The ticket is deleted and
   moved to the Deleted tickets view for 30 days until it is permanently deleted.

## Deleting tickets from user profiles and views

In addition to deleting tickets from the ticket itself, you can also delete them from user
profiles and views.

**To delete tickets from a user profile**

1. Open a [user profile](https://support.zendesk.com/hc/en-us/articles/4408835078810).
2. On the Tickets tab, select the tickets you want to delete.
3. Click the dropdown arrow next to **Edit ticket(s)** > **Delete** .

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/prof-rjs-1.png)

**To delete tickets from a view**

1. Open a [view](https://support.zendesk.com/hc/en-us/articles/4408888828570).
2. Select the tickets you want to delete.
3. Click **Delete**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/prof-rjs-2.png)

## Undoing a ticket deletion

When you delete a ticket, you can quickly undo the deletion and recover the ticket if you
need to.

**To undo a ticket deletion**

- Click **Undo** in the message about the ticket deletion.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/deleted_ticket_undo.png)

  The message only displays for a few seconds. If you
  miss the option in the message, you can restore the deleted ticket from the Deleted
  Ticket view (see [Restoring a deleted ticket](https://support.zendesk.com/hc/en-us/articles/4408835089050#topic_zmy_j24_xw)).

## Permanently deleting a ticket

Deleted tickets appear in a Deleted tickets view for 30 days. After that time, they are
automatically permanently deleted.

If a ticket is in an [archived state](../../product-guides/ticket-management/about-ticket-archiving.md) (greater than 120 days since marked
as solved) before being deleted, it will not display in the deleted tickets view. By
default, views do not display archived tickets.

You can manually permanently delete tickets before that time, if you want. If you do so,
the ticket disappears from the Deleted tickets view, and there is *no way* to recover
the permanently deleted ticket.

Auditing and reporting on deleted tickets works as follows:

- **Reporting overview**: Deleted tickets are not excluded from the reporting
  overview. The ticket ID for a permanently deleted ticket is stored as a record, but no
  other information or ticket fields is stored for a permanently deleted ticket.
- **Explore**: Deleted tickets are excluded from most Explore reports by default.

  If you want to report on ticket deletion events, create a report in the [Updates history dataset](https://support.zendesk.com/hc/en-us/articles/4408827693594#topic_as3_slp_4y) using the
  **Activity** > **Deletions** metric. This report will show the ticket ID
  and when the ticket was deleted. Information about the ticket, including the ticket's
  subject and the requester's name and email address, are not available. SLA data from
  deleted tickets is also retained in the SLAs
  dataset.
- **Audit log**: When an agent permanently deletes a ticket manually, the event is
  tracked in the audit log with the activity type **Permanently deleted**. Tickets that
  are automatically permanently deleted by Zendesk after 30 days are not tracked in the
  audit log.

**To permanently delete a ticket**

1. Select the tickets you want to permanently delete.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tickets_delete_restore.png)

   A toolbar appears at the bottom of the
   list.
2. Click **Delete permanently**.
3. Confirm that you want to permanently delete the selected tickets.

   You can't recover permanently
   deleted tickets. All attachments associated with the tickets are also deleted.

   Note: When
   you permanently delete a ticket, the record remains but all user-submitted content is
   scrubbed. As a result, scrubbed versions of deleted tickets still appear in the
   results of the Incremental Ticket Export API because the ticket records still exist.
   See [Excluding deleted tickets](https://developer.zendesk.com/documentation/ticketing/managing-tickets/using-the-incremental-export-api/#excluding-deleted-tickets) in the developer
   docs for more information.