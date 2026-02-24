# Viewing, recovering, and deleting suspended tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408893392922-Viewing-recovering-and-deleting-suspended-tickets

---

Some emails may be flagged as spam and be either completely rejected or sent to the suspended tickets queue, where they may be permanently deleted or recovered.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Some emails may be flagged as spam and be either completely rejected or sent to the suspended tickets queue, where they may be permanently deleted or recovered.

Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can view, recover, and delete suspended tickets.

All unrecovered suspended tickets are automatically deleted after 14 days.
Suspended tickets that are automatically deleted cannot be recovered and are permanently removed.

This article covers the following topics:

- [Viewing suspended tickets](#topic_ukg_lbf_kd)
- [Recovering or deleting suspended tickets](#topic_too_xnk_ae)
- [Using export to analyze suspended tickets](#topic_v5w_wgd_s5b)
- [Light agent recovery of suspended comments with CCs](#topic_bpp_rlm_hlb)

Related articles:

- [Understanding suspended tickets and spam](https://support.zendesk.com/hc/en-us/articles/4408889141146)

## Viewing suspended tickets

Suspended tickets appear in your list of views as a system-generated view called Suspended tickets.

On non-Enterprise plans, agents must have permission to view all tickets to access the Suspended tickets view and its tickets. On Enterprise plans, agents must be in a custom role with permission to view, recover, and delete suspended tickets to access the Suspended tickets view and its tickets.

Agents with permission to access the Suspended tickets view can delete any tickets included in that view, even if ticket deletion is not enabled for them.

Agents with the Play views only permission can't access the Suspended tickets view.

**To view your suspended tickets**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Views** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar.
2. Click **Suspended tickets**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/suspended_tickets_view.png)

Selecting the view allows you to manage the suspended tickets. You can view detailed information for each, including the reason for suspension, and then recover or delete them.

## Recovering or deleting suspended tickets

Suspended tickets can be manually unsuspended and placed back into your ticket queue. You can unsuspend tickets in the Suspended tickets view one at a time or in bulk. You can also delete suspended tickets.

See [Guidelines for reviewing suspended tickets](https://support.zendesk.com/hc/en-us/articles/4408832102042) for recommendations and see [Causes of ticket suspension](https://support.zendesk.com/hc/en-us/articles/4408828416282) for a list of reasons that tickets get suspended.

**To bulk recover or delete suspended tickets**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Views** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar.
2. Click the **Suspended tickets** view.
3. Select the tickets you want to recover or delete. You can select all the tickets in the view by clicking the selection check box in the table header.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bulk_delete_suspended.png)

   A toolbar appears at the bottom of the list.
4. Click either **Recover** or **Delete**, depending on what action you want to take.

The tickets you recover are unassigned and have a New status. They will appear in views that show unassigned tickets. They will also be available by search. Deleted tickets are deleted permanently and can't be recovered.

**To recover or delete a single ticket**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Views** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar.
2. Click the **Suspended tickets** view.
3. Click the Subject of the ticket you want to recover or delete.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/recover_single_ticket.png)
4. Select **Delete**, **Recover Manually**, or **Recover Automatically**.

   The automatic recover option immediately recovers the ticket.
   The manual recover option allows you to edit the ticket properties first and then recover the ticket.

   If you recover a ticket manually, the recovered ticket functions as a copy of the original ticket. It only pulls a plain text version of the original email that excludes the full HTML content and any attachments. The original ticket remains in the Suspended tickets view.

When you recover a suspended ticket in the Zendesk Agent Workspace, your name is not listed as the submitting agent. Instead, the via field is typically shown as System or Email.

## Using export to analyze suspended tickets

If you have a large number of suspended tickets, you can export the list to a CSV file for further analysis. Exporting the suspended ticket list lets you use your own spreadsheet software to sort, filter, and view all your suspended tickets in a single page.

The exported list also provides additional columns of data about the tickets that aren’t visible in the Suspended tickets view. This can be helpful when investigating tickets. For example, you can export the suspended ticket list to obtain the suspension *Cause ID* for each ticket. Then, cross-reference the cause ID with the [Cause of suspension reference](https://developer.zendesk.com/documentation/ticketing/reference-guides/suspensions-reference/).

The export feature gives visibility into the types of tickets you receive and helps identify patterns when [managing suspended tickets](https://support.zendesk.com/hc/en-us/articles/4408889141146#topic_ewp_qrl_zsb).

See [Guidelines for reviewing suspended tickets](https://support.zendesk.com/hc/en-us/articles/4408832102042) for tips on reviewing your suspended tickets regularly.

**To export the suspended ticket list**

1. Select the **Suspended tickets** view.
2. Click **Export CSV** in the upper-right corner.

You'll receive an email notification containing a download link for your CSV file. The email is sent to your primary email account in your user profile.

## Light agent recovery of suspended comments with CCs

You can recover a suspended comment that includes CCs and followers just like any other comment. However, it’s important to note that the behavior with [light agents](https://support.zendesk.com/hc/en-us/articles/4408846501402) is slightly different when CCs are involved. If a light agent recovers a suspended comment, CCs from the last end user email reply will not be added to the ticket. This is because light agents can't add or remove CCs from tickets.

If your company uses CCs and light agents, ask your admin whether your company has an internal policy or best practice that says light agents do not recover suspended tickets.