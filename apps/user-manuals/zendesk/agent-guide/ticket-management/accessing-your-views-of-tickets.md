# Accessing your views of tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408829483930-Accessing-your-views-of-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Access your ticket views to organize and manage customer inquiries based on specific criteria. You can use standard, shared, or personal views to streamline your workflow. Customize views to suit your needs, and easily navigate through ticket statuses and actions. This feature helps you prioritize tasks and improve response times, ensuring effective customer support across various channels.

Location: 
In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Views** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar.

Views are a way to group tickets based on certain criteria. You can access your views list and open any view to see the tickets associated with that view.
The views list includes up to 100 active standard and shared team views and up to 10 personal views.

Admins and [agents with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can use or modify the standard views, as well as create shared team views and personal views. Agents can use the standard views, any shared team views to which they have access, and create their own personal views. (see [Creating views to build customized lists of tickets](https://support.zendesk.com/hc/en-us/articles/4408888828570)).

This article contains the following sections:

- [About standard views](#topic_gnx_2tm_vt)
- [Opening a view](#topic_1nl_ftm_vt)
- [Working with tickets in a view](#topic_ocm_vkx_cfc)

Related articles:

- [Resources for working with tickets](https://support.zendesk.com/hc/en-us/articles/4408882039450)
- [Updating and solving tickets](https://support.zendesk.com/hc/en-us/articles/4408832151834)

## About standard views

There is a pre-defined set of views provided for the essential day-to-day support workflow. These include:

- Your unsolved tickets
- Unassigned tickets
- All unsolved tickets
- Recently updated tickets
- Unsolved tickets in your groups
- New tickets in your groups
- Pending tickets
- Recently solved tickets

### Additional standard views for employee services

In addition to the standard views that are pre-defined and available to all Zendesk accounts, additional HR- and IT-specific views are provided for the Employee Services Suite. These views provide common day-to-day workflow needs that are specific to employee services. Each of these views is configured to display tickets that use the ticket form of the same name, such as *New hire onboarding*.

The names of all standard employee service views are prefaced with *[SAMPLE]*. These views are activated by default, but can be [deactivated](https://support.zendesk.com/hc/en-us/articles/4408832792986#topic_vnx_wev_ec) if you choose not to use them.

The following employee service views are provided:

- [SAMPLE] New hire onboarding
- [SAMPLE] Parental leave questions
- [SAMPLE] Payroll questions/issues
- [SAMPLE] Hardware support
- [SAMPLE] Software support

See [Using the sample data for employee services](https://support.zendesk.com/hc/en-us/articles/9012803758362).

### Standard views for approval requests

When the approval request feature is [turned on](https://support.zendesk.com/hc/en-us/articles/9475816348442), two additional pre-defined views are activated:

- **Tickets with pending approvals**: A list of tickets assigned to the current user's group with approval requests awaiting a response.
- **Your tickets with approval requests**: A list of tickets assigned to the current user that have approval requests. This includes approval requests of all statuses.

After these views are activated, admins and agents with permissions can edit, manage, and deactivate them as needed.

## Opening a view

Views are displayed as a list in the Views pane. The first 100 of your shared views and 10 of your personal views appear in collapsible lists. If you've [categorized your views](https://support.zendesk.com/hc/en-us/articles/8009260752794), they appear in the folder structure you defined.

Additionally, you can view your suspended and deleted tickets at the bottom of the list.

Note: On Enterprise plans, admins can limit [agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd)
to the previous default number of views, which was 12 shared and 8 personal views.

**To select and display a view**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Views** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar.

   Views are separated into shared and personal, if you've created personal views.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_list_for_agents.png)

   Depending on your permissions, you may see the Deleted tickets view.
   See [Viewing deleted tickets](https://support.zendesk.com/hc/en-us/articles/4408835089050#topic_g5g_j24_xw).
2. Select a view from the list.

   Use the arrow (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon-sort-path-up.png)) to collapse the views in the shared or personal list. If you have more views than appear, click **Manage views** at the bottom of the list to access them. You can [change the order](https://support.zendesk.com/hc/en-us/articles/4408842965530#topic_tmy_3hd_jjb) views appear in, if needed.

The view opens and displays the associated tickets. [Archived tickets](../../product-guides/ticket-management/about-ticket-archiving.md) are not shown in views. You can [sort and filter tickets](https://support.zendesk.com/hc/en-us/articles/5430058226330) in a view as needed.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_sort_order_reset.png)

To preview a ticket in a view, hover your mouse over a ticket title or ticket status icon.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_ticket_hover_new.png)

Tip: Admins can click the Views button (+) at the top of the Views list as a shortcut to create new shared views. See [Creating ticket views to improve team priorities and workflows](https://support.zendesk.com/hc/en-us/articles/9954751708826).

## Working with tickets in a view

Tickets in a view are preceded with a colored icon indicating each ticket's current status.

The following standard ticket statuses are included by default:

| Standard ticket statuses | Icons | Custom ticket statuses |
| --- | --- | --- |
| New Open Pending On-hold Solved | | If an admin has [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306) in the account, then you may see additional ticket statuses. For example: |

Note: The On-hold ticket status is available only if an admin has [activated the On-hold status](https://support.zendesk.com/hc/en-us/articles/4408889282458).

Within a ticket, comments use background colors to indicate the type of comment, such as yellow for private comments or blue (temporarily)
for comments and other ticket updates added while you're viewing the ticket. The exception is the [Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) which doesn't support blue (temporary)
colors for comments.

**Actions you can take on a ticket include**:

- Click a ticket in the view list to open it.
- Click the **Next ticket** button in the upper-right corner of the ticket to go to the next ticket in a view.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_nextbutton2.png)
- Click the menu to the left of the **Submit** button to set what happens after you submit a ticket.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_menu_stayonticket_closetab_gotonext.png)

 - **Close tab** returns you to the view list.
 - **Next ticket in view** opens the next ticket in the view.
 - **Stay on ticket** keeps the ticket open.

For more information, see [Resources for working with tickets](https://support.zendesk.com/hc/en-us/articles/4408882039450).