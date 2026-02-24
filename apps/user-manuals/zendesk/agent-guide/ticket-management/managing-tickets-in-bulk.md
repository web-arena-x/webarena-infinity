# Managing tickets in bulk

Source: https://support.zendesk.com/hc/en-us/articles/4408886890906-Managing-tickets-in-bulk

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Using your views, you can make ticket updates to many tickets at the same time. For example,
if you want to assign yourself to a number a tickets, you just select them in a view and then
set yourself as the assignee. You can also delete, merge, or mark as spam the selected
tickets. If you navigate to different pages, your tickets will remain selected.

Note: [AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346) cannot be managed in bulk.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/announce_bulk.gif)

Topics covered in this article:

- [About making bulk ticket updates](#topic_j4s_rd1_d3c)
- [Bulk updating tickets](#topic_oth_lkp_gk)
- [Bulk deleting tickets](#topic_d5y_3mf_wf)
- [Bulk merging tickets](#topic_k5w_mnf_wf)
- [Bulk marking tickets as spam](#topic_qrv_crm_t4)

## About making bulk ticket updates

When a bulk action is initiated, the system records each ticket’s last-updated timestamp
and sends that timestamp with the request. During the update, the system compares the
timestamp in the database to the timestamp sent with the bulk action.

If the timestamps match, the update proceeds for that ticket. If the timestamps differ,
meaning that the ticket was modified after the bulk action began, the system skips that
ticket, returns an error for that update, and continues processing the remaining
tickets.

## Bulk updating tickets

The maximum number of tickets you can update at one time is 100 tickets. You cannot bulk
update closed tickets. You can bulk update most of the same properties as an individual
ticket, including ticket status, fields, subject, and comments.

For information about how specifying a default X (formerly Twitter) account affects bulk
ticket updates, read about the **Make this the default account setting** described in
[Setting up your X (formerly Twitter) channel](https://support.zendesk.com/hc/en-us/articles/4408883122714-Setting-up-your-Twitter-channel).

**To update multiple tickets in a view**

1. Open one of your views and select the tickets you want to update.

   You can pick and
   choose the tickets you want to update or select the entire list by clicking the check
   box at the top left of the view.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tickets_bulk_select_all.png)

   When you
   select one or more tickets in a view, a toolbar appears at the bottom of the
   list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tickets_bulk_menu.png)
2. Click **Edit**.
3. In **Edit tickets** you can update ticket properties and add a comment for all of
   the tickets you selected.

   To help with accessibility, you can use keyboard navigation
   to select toolbar menu items and apply formatting before submitting the
   comment.

   You can also apply a macro to all the tickets by selecting it from the
   **Apply Macro** menu. If you apply a macro that includes [attachments](https://support.zendesk.com/hc/en-us/articles/4408844187034#topic_xb4_4nw_4y) to ticket comments, the
   attachments will not be included in the bulk update.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bulk_update_ticket4.png)

   If you bulk update tickets by applying a macro that uses dynamic
   content or placeholders in the ticket subject, then the updated tickets' subjects
   will be saved with the bracketed version of the subject. For example,
   `{{ticket.created.at}}`  may be displayed in the subject instead of
   `March 2, 2023`. Additionally, dynamic content doesn't render
   correctly in the composer when bulk updating tickets with a macro.

   Most
   active ticket fields (including [system fields](https://support.zendesk.com/hc/en-us/articles/4408886739098), [custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4408883152794), [custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575861018), and [conditional ticket fields](https://support.zendesk.com/hc/en-us/articles/4408834799770)) display in the Edit tickets
   dialog box during a bulk update, regardless of the ticket forms applied to the
   selected tickets. However, the bulk editor doesn't support [CC, followers, or @mentions](https://support.zendesk.com/hc/en-us/articles/4408822451482).

   For example, if you
   attempt to @mention someone from the bulk editor, the text in the comment remains
   plain text, and the person isn't CCed on the ticket. There's also no visible fields
   for CCs or followers in the bulk editor. You also can't use the bulk editor
   to apply macros that have an action to add a CC. The CC will not be
   added if the macro is applied this way.
4. Click **Submit** to save your ticket updates.

When you make bulk updates to tickets (edit, delete, merge, or mark as spam),
the [event](https://support.zendesk.com/hc/en-us/articles/4408829602970) is recorded as a **Web Service (API)** update. See the
example below. If you have [triggers](https://support.zendesk.com/hc/en-us/articles/4408893545882) based on **Ticket: Updated via** conditions, make sure
you take this into account.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bulk_export_event.png)

## Bulk deleting tickets

You can select multiple tickets in a view and delete them at the same time. Deleting a
single ticket is described in [Deleting tickets](deleting-tickets.md).

Once deleted, tickets are moved into a Deleted Tickets view, where you can [restore them](https://support.zendesk.com/hc/en-us/articles/4408835089050#topic_zmy_j24_xw) or [permanently delete them.](https://support.zendesk.com/hc/en-us/articles/4408883872538#topic_5ll_km4_xw) After 30 days deleted
tickets are permanently deleted and removed from the Deleted Tickets view. You cannot bulk
delete Closed tickets. For details, see [Deleting tickets](deleting-tickets.md).

Note: Administrators must enable agents to delete tickets. See [Enabling agents to delete tickets](https://support.zendesk.com/hc/en-us/articles/4408832689818).

**To delete multiple tickets in a view**

1. Open one of your views and select the tickets you want to delete.

   You can pick and
   choose the tickets you want to delete or select the entire list by clicking the check
   box at the top left of the view.
2. Select **Delete** from the toolbar at the bottom of the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tickets_bulk_menu.png)
3. When prompted, click **OK** to confirm that you want to delete the tickets, which are
   then moved into the Deleted Tickets view.

## Bulk merging tickets

You can select multiple tickets in a view and merge them into another ticket. Merging one ticket
into another ticket is described in [Merging tickets](zag_tickets_merging.html#topic-1).

Be sure that you merge the correct tickets. Ticket merges are final. You cannot undo or revert a
ticket merge. You cannot merge tickets with a ticket that's shared, or with one that's
already closed.

**To merge multiple tickets in a view into another ticket**

1. Open one of your views and select the tickets you want to merge.

   You can pick and
   choose the tickets you want to merge or select the entire list by clicking the check
   box at the top left of the view.
2. Select **Merge** from the toolbar at the bottom of the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tickets_bulk_menu.png)

   **Tip:**  Be sure to have the ticket
   number of the ticket you want to merge into handy before you start the merge
   process.
3. In the **Merge ticket** dialog, enter the ticket number for the ticket you'd like
   to merge the selected tickets into, then click **Merge**. Alternatively, you can
   select a recently-viewed ticket.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bulk_ticket_merge_aw.png)

   If you’re
   attempting to merge tickets into a ticket with a different organization, brand, or
   requester, a message appears.
4. Make sure that you aren’t unintentionally sharing sensitive information by merging the
   tickets, then click **Continue Merge**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/merge_tickets_warning_PII.png)
5. When prompted, click **Confirm and Merge** to confirm the merge. If you want to
   cancel the merge, click **Cancel** instead.

   Be sure that you merge the correct
   tickets. Ticket merges are final. You cannot undo or revert a ticket merge.

## Bulk marking tickets as spam

You can select several tickets in a view to mark as spam and suspend the requesters.
Marking a single ticket as spam is described in [Marking a ticket as spam and suspending the requester](https://support.zendesk.com/hc/en-us/articles/4408842999066).

Tickets marked as spam are moved to the deleted ticket view and the requesters are
suspended at the same time. You can unsuspend suspended users if necessary.

Note: Administrators must enable agents to delete tickets. See [Enabling agents to delete tickets](https://support.zendesk.com/hc/en-us/articles/4408832689818).

**To mark multiple tickets in a view as spam and suspend the requesters**

1. Open one of your views and select the tickets you want to mark as spam.

   You can
   pick and choose the tickets you want to mark as spam or select the entire list by
   clicking the check box at the top left of the view.
2. Select **Mark as spam** from the toolbar at the bottom of the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tickets_bulk_menu.png)
3. When prompted, click **Mark as spam** to confirm the deletion.

   Tickets marked as
   spam are moved to the Deleted tickets view.