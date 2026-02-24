# Viewing and recovering deleted tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408835089050-Viewing-and-recovering-deleted-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

When you [delete a ticket](https://support.zendesk.com/hc/en-us/articles/4408883872538), it isn't actually permanently deleted. Instead, it is moved into the Deleted tickets view, where you can restore it (move it back into its original view) or permanently delete it.

Administrators can view and recover deleted tickets. Agents must be granted permission to view and recover deleted tickets (see [Enabling agents to delete tickets](https://support.zendesk.com/hc/en-us/articles/4408832689818)).

This article contains the following sections:

- [Viewing deleted tickets](#topic_g5g_j24_xw)
- [Restoring a deleted ticket](#topic_zmy_j24_xw)

Related topic:

- [Permanently deleting tickets](https://support.zendesk.com/hc/en-us/articles/4408883872538#topic_5ll_km4_xw)

## Viewing deleted tickets

Deleted tickets are moved into a Deleted tickets view for 30 days, where you can restore them or permanently delete them. After 30 days they are automatically permanently deleted.

Note: If you delete an archived ticket, it doesn't move to the Deleted tickets queue and cannot be searched for or restored from the agent interface, even during the normal 30-day recovery window. If you have the ticket IDs, you can use the Zendesk [API](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets) to restore these tickets [individually](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#restore-a-previously-deleted-ticket) or [in bulk](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#restore-previously-deleted-tickets-in-bulk).

If an agent's permission to delete tickets, or to view deleted tickets, is removed, then the agent will no longer be able to access the Deleted tickets view.

**To open the Deleted tickets view**

- Click the **Views** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar, then click **Deleted tickets** in the Views list.

  The deleted tickets appear in the main window.

You cannot open tickets directly from the Deleted tickets view. To view a previously-deleted ticket you'll need to restore it. Restoring a ticket returns it to its original view, exactly as it was before it was deleted.

## Restoring a deleted ticket

While a ticket is in the Deleted tickets view (for up to 30 days), you can restore it if you need to. When you restore a deleted ticket, it is removed from the Deleted tickets view and appears in the view it was in before it was deleted.

**To restore a deleted ticket**

1. Click the **Views** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar, then click **Deleted tickets** in the Views list.
2. Select the tickets you want to recover. You can select one or more tickets.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/restore_ticket.png)

   A toolbar appears at the bottom of the list.
3. Click **Restore**.

   The recovered tickets are removed from the Deleted tickets view and appear in the view they were in before they were deleted.