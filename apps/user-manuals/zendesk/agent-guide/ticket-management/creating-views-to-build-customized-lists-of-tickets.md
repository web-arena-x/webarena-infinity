# Creating views to build customized lists of tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408888828570-Creating-views-to-build-customized-lists-of-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Create views to organize tickets into lists based on criteria like status or assignee. Use views to prioritize tasks, align with support structures, and manage workflows. Admins can create shared views for teams, while agents can create personal views. Clone existing views to customize them for different needs. Avoid broad exclusionary conditions when building view conditions.

Location:  Admin Center > Workspaces > Agent tools > Views

Views are a way to organize your tickets by grouping them into lists based on certain criteria. For example, you can create a view for unsolved tickets that are assigned to you, a view for new tickets that need to be triaged, or a view for pending tickets that are awaiting response. Using views can help you determine what tickets need attention from you or your team and plan accordingly.

Many support teams use views to guide the workflow by requiring agents to address tickets in one view first and then others in a specific order. Views can also mirror the support structure you've created. For example, if you provide different levels of service for different customers or manage escalation using a tiered support group structure (Level 1, Level 2), you can create views for each of these scenarios.

This article covers the following topics:

- [About view types](#topic_emv_1tp_tz)
- [Creating views](#topic_vcr_xfp_ec)
- [Building view condition statements](#topic_tpp_zfp_ec)
- [Cloning a view](#topic_fjf_vev_ec)

Related articles:

- [Managing your views](https://support.zendesk.com/hc/en-us/articles/4408832792986)
- [Categorizing your views](https://support.zendesk.com/hc/en-us/articles/8009260752794)
- [Accessing your views of tickets](https://support.zendesk.com/hc/en-us/articles/4408829483930)

## About view types

Zendesk Support includes the following types of views:

- **Standard views**: There are a number of [standard views](https://support.zendesk.com/hc/en-us/articles/4408829483930#topic_gnx_2tm_vt) created when
  you open a Zendesk Support account. You can deactivate or edit most of these views;
  however, the Suspended tickets and Deleted tickets views cannot be edited or removed
  from your list of views. Note that your suspended and deleted ticket views appear at the
  bottom of the views list and don't count towards the number of views displayed in the
  shared views lists.
- **Shared views**: Admins can create views that are available to all agents or to
  all agents in a specific group. The first 100 shared views are accessible in the Views
  list (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) .
- **Personal views**: Agents can create views that are available to themselves only.
  Their first 10 personal views are accessible in the Views list (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)).

Note: On Enterprise plans, admins can create or update custom roles to limit agents to the
previous default amount of views, which was 12 shared and 8 personal views. See [Creating custom agent roles](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd).

## Creating views

Views are a way to organize tickets by grouping them into lists based on certain
criteria.

Agents can create views for their own personal use only. Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can create personal views,
as well as shared views for use by multiple agents. To help admins get started with views,
Zendesk provides a [setup wizard for views](https://support.zendesk.com/hc/en-us/articles/9954751708826#topic_lhf_5jc_x2c).

Note: If you want to view tickets to understand trends or history, then it’s better to [create a report](https://support.zendesk.com/hc/en-us/articles/4408821589530). If, in fact, you need to access ticket data
from a large number of tickets, such as hundreds of thousands of tickets, then it’s better
to [export the data](https://support.zendesk.com/hc/en-us/articles/4408886165402).

The following video gives you an overview of how to create views.

Creating views to filter tickets [1:23]

**To create a view**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. Click **Create view**.

   This creates a view in the last
   position of the list. To pick a view's position as you're creating it, hover over an
   existing view, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Create view
   below**.

   Alternatively, you can clone an existing view (see [Cloning a
   view](#topic_fjf_vev_ec)).
3. Enter a **Title** for the view:
   - Use [placeholders](https://support.zendesk.com/hc/en-us/articles/4869979117210) so titles are translated to the
     agent's language. For example, *{{zd.all\_unsolved\_tickets}}* for all unsolved
     tickets.
   - Add emojis to help agents differentiate views by pasting the emoji’s image into
     the title. On [this
     website](https://getemoji.com/) you click the emoji to copy it.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_views_emojis_title.png)
   - Categorize your views into folders, in Agent Workspace, by entering the double
     colon (::) syntax in the title. See [Categorizing your views](https://support.zendesk.com/hc/en-us/articles/8009260752794) for more information.
4. Enter a **Description** for the view.
5. Select an option to determine **Who has access**:

   - **Any agent**, available to all agents.
   - **Agents in specific groups**, available to agents in specified groups.
     Select groups from the menu, then click away when finished.
   - **Only you**, available to you as a personal view.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_access3.png)
6. Click **Add condition** to set up the view to meet **All** or **Any**
   conditions.

   The conditions define this collection of tickets.
7. Select a **Condition**, **Field operator**, and **Value** for each condition
   you add.

   See [Building
   view condition statements](#topic_tpp_zfp_ec).
8. Click **Preview** to test the conditions.
9. Set the formatting options:

   1. Drag the **Columns** into the order you want and click **Add column** to
      add up to 15 columns.

      Multi-select fields are not
      supported.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_workspace_views_create_selectdata.png)
   2. Under **Group by**, select the ticket field you want to use to group tickets,
      then select **Ascending** or **Descending**.

      Keep in
      mind the following when grouping views:
      - If you select **Request date** from the **Group by** drop-down list,
        any settings you change in the **Order by** drop-down list will not be
        applied.
      - If you select a custom field value from the **Group by** drop-down
        list, the tickets in the view are ordered alphabetically by the field's tag,
        not its name. See [Understanding custom ticket fields and
        views](https://support.zendesk.com/hc/en-us/articles/4408834953114#topic_znk_mnk_xj).
   3. Under **Order by**, select a ticket field to use as the default data to order
      tickets, then select **Ascending** or **Descending**.
10. Click **Save**.

    The view is created. Views do not include [archived tickets](https://support.zendesk.com/hc/en-us/articles/4408887617050-Ticket-Archiving).

You can manage your view (edit, deactivate, and so on) on the view's
page (see [Managing your views](https://support.zendesk.com/hc/en-us/articles/4408832792986)).

## Building view condition statements

As with the other business rules, you select collections of tickets using conditions,
operators, and values.

Displaying a view involves searching all unarchived tickets to find matches for
the conditions defined in your views. It’s always best to define views that look for what’s
there, rather than what’s not there. With that in mind, when building view condition
statements, avoid the following:

- Checking several text fields.
- Checking for a null value. For example, "Assignee is ( - )".
- Using broadly exclusionary conditions. For example, "NOT" statements.

  Instead, use inclusive conditions that are as specific as possible.
- Checking for tags.
- Checking for a ticket description with a condition that "does not contain the following
  string".

  Checking for a string or word introduces greater complexity than checking for a tag.
  Conditions that check for tags are preferred over those checking for a word or string,
  but neither is ideal.

Your view condition statements must have at least one of the following ticket properties in
the Meet all of the following conditions section:

- Status
- Status category
- Type
- Group
- Assignee
- Requester

Some conditions may not be available, depending on your plan.

| Condition | Description |
| --- | --- |
| Ticket: Status | Note: If you’ve [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), existing standard ticket statuses become status categories. If you have existing conditions that use Status, they’re updated to the corresponding Status category.  The standard ticket status values are:  **New** is the initial status of a newly created ticket (not assigned to an agent).  **Open** means that the ticket has been assigned to an agent.  **Pending** is used to indicate that the requester has been asked for information and the ticket is therefore on hold until that information has been received.  **On-hold** means that the support request is awaiting a resolution from a third party—someone who is not a member of your support staff and does not have an agent account in your Zendesk account. This status is optional and must be added (see [Adding the On-hold ticket status](https://support.zendesk.com/hc/en-us/articles/4408889282458-Adding-the-On-hold-ticket-status-to-your-Zendesk)).  **Solved** indicates that the customer’s issue has been resolved. Tickets remain solved until they are closed.  **Closed** means that the ticket has been locked and cannot be reopened or updated.  When selecting a status, you can use the field operators **Less Than** and **Greater Than** to specify a range of tickets based on their status. **New** is the lowest value, with values increasing until you get to **Closed** status. For example, a condition statement that returns only New, Open, and Pending tickets looks like this:  **Status is less than Solved**. |
| Ticket: Status category | Note: If you’ve [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), standard ticket statuses and custom ticket statuses are grouped into status categories. Each status category has a default ticket status. See [Managing ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575941402-Managing-ticket-statuses-#topic_zgh_dbh_vrb).  The status category values are:   - **New** is the initial status category of a newly created ticket (not   assigned to an agent). - **Open** is for grouping ticket statuses that indicate when tickets are   ready to be worked on by your support team. - **Pending** is for grouping ticket statuses that are used to indicate that   the support team is waiting for the requester to reply. - **On-hold** contains ticket statuses used to indicate that the support   request is awaiting a resolution from a third party—someone who is not a member   of your support staff and does not have an agent account in your Zendesk   account. This status category is optional and must be added (see [Activating the On-hold status category](https://support.zendesk.com/hc/en-us/articles/4408889282458#topic_zqr_jfz_kxb)). - **Solved** contains ticket statuses that indicate that the customer’s issue   has been resolved. - **Closed** contains the Closed standard ticket status that indicates that   the ticket has been locked and cannot be reopened or updated. |
| Ticket: Ticket status | If you’ve [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), you can select standard ticket statuses and custom ticket statuses as conditions. |
| Ticket: Brand | Include (*is*) or exclude (*is not*) a brand using the drop-down menu. |
| Ticket: Form | Select the required ticket form. For more information on ticket forms, see [Creating ticket forms to support multiple request types](https://support.zendesk.com/hc/en-us/articles/4408846520858). |
| Ticket: Service catalog form | Used to check that the ticket uses a specific [service request forms](https://support.zendesk.com/hc/en-us/articles/4408836460698#topic_p3b_rwv_dgc). Available only when the [service catalog is turned on](https://support.zendesk.com/hc/en-us/articles/9443951511450). |
| Ticket: Type | The ticket type values are:  **Question**  **Incident** is used to indicate that there is more than one occurrence of the same problem. When this occurs, one ticket is set to Problem and the other tickets that are reporting the same problem are set to Incident and linked to the problem ticket.  **Problem** is a support issue that needs to be resolved. **Task** is used by the support agents to track various tasks. |
| Ticket: Support type | (Applicable only for messaging tickets) Indicates whether a ticket was handled entirely by an AI agent or whether a human agent was involved. Possible values are **AI agent** and **Agent**. For more information, see [Understanding and viewing AI agent tickets for AI agent–only conversations](https://support.zendesk.com/hc/en-us/articles/9204149016346). |
| Ticket: Priority | There are four values for priority: **Low**, **Normal**, **High**, and **Urgent**.  As with status, you can use the field operators to select tickets that span different priority settings. For example, this statement returns all tickets that are not urgent: Priority is less than Urgent |
| Ticket: Group | The ticket group values are:  - **(—)**, which indicates that no group is assigned to the ticket. - **(current user's groups)**, which includes all the groups to which the   agent viewing the view belongs. - **(assigned group)**, the group assigned to the ticket. - **Group name**, the name of the group that is assigned to the ticket.   **Group name** is the actual name of the group that is assigned to the ticket. |
| Ticket: Assignee | The assignee values are:   - **(—)** or leaving the field empty indicates that the ticket is unassigned. - **(requester)** is the ticket requester. You can select   this option to return tickets that were opened by and then assigned to the same   agent, for example. - **Agent name** is the actual name of the person assigned to the   ticket.   Additional value for views:   - **(current user)** is the person who is currently viewing the view. For   example, if the view condition was **Assignee** > **Is** > **(current   user)** then the agent viewing the view would be shown all the tickets for   which they are the assignee. This enables one view to show relevant tickets to   each agent, without having to create a specific view for each individual agent. |
| Ticket: Requester | The requester values are:   - **(assignee)** is the person   assigned to the ticket. The condition statement ‘Requester is Assignee’ is true if   the requester is also the person assigned to the ticket.  This is possible if an   agent created a ticket and was then assigned to it. - **Agent name** is the actual name of the agent.   Additional value for views:   - **(current user)** is the person currently looking at the view. If you are   looking at the view, you will see tickets for which you are the requester. |
| Ticket: Organization | The organization values are:   - **(—)** indicates that no organization has been added to the ticket. If you   have multiple organizations, **(—)** displays for a certain number of   organizations, but is a blank value above that number. If you have a large   number of organizations, start typing the organization name to find a   match. - **Organization name** is the name of an organization. |
| Ticket: Tags | Determine whether tickets contain a specific tag or tags. You can include or exclude tags in the condition statement by using the operators **Contains at least one of the following** or **Contains none of the following**. More than one tag can be added. Press Enter between each tag you add. |
| Ticket: Description | The description is the first comment in the ticket. It does not include the text from the subject line of the ticket. If you are using the **Contains at least one of the following** or **Contains none of the following** operators, the results will consider words containing part of the entered search terms. For example, using "none" for this condition will return (or exclude) ticket descriptions containing "nonetheless".  The description condition also pulls data contained within the HTML and the original source of a ticket. |
| Ticket: Channel | The ticket channel is where and how the ticket was created. The contents of this list will differ depending on the channels you have active, and any integrations you are using.  For more information about the channels you can configure, see [About Zendesk Support channels](https://support.zendesk.com/hc/en-us/articles/4408824097050-About-Zendesk-Support-channels) and [Understanding ticket channels in Explore](https://support.zendesk.com/hc/en-us/articles/4408836378394). |
| Ticket: Integration Account | Include (*is*) or exclude (*is not*) an installed Support or messaging integration using the drop-down menu. |
| Ticket: Received at | This condition checks the email address from which the ticket was received and the email address from which the ticket was originally received. These values are often, but not always, the same. The ticket can be received from a Zendesk email domain such as sales@mondocam.zendesk.com, or from an external email domain such as support@acmejetengines.com. The external email domain must be set up as described in [Forwarding incoming email to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408886828698) or the condition won't work.  Note that this condition doesn't check the channel from which the ticket originated and can be true for tickets that weren't received through email. For example, when using the [Select an Address app](https://support.zendesk.com/hc/en-us/articles/4408830888730) you can specify a recipient email address and therefore meet this condition even though the ticket was created in the agent interface. |
| Ticket: Satisfaction | Supports the following customer satisfaction rating values: - **Unoffered** means that the survey has not previously been sent - **Offered** means that the survey has already been sent - **Bad** means that the ticket has received a negative rating - **Bad with comment** means that the ticket has received a negative rating   with a comment - **Good** means that the ticket has received a positive rating - **Good with comment** means that the ticket has received a positive   rating with a comment |
| Ticket: Satisfaction Reason | Include (*is*) or exclude (*is not*) the selected satisfaction reason, if activated, using the drop-down menu. |
| Ticket: Hours since... | These conditions allow you to select tickets based on the hours that have passed since the ticket was updated in the following ways:  - Hours since created - Hours since open - Hours since pending - Hours since on-hold - Hours since solved - Hours since closed Note: If you've [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), the   Hours since [*ticket status*] conditions are updated to Hours since   [*status category*]. - Hours since assigned - Hours since update - Hours since requester update - Hours since assignee update - Hours since last SLA breach - Hours until next SLA breach - Hours since due date (for tickets with the type set to Task) - Hours until due date (for tickets with the type set to Task) - Hours since [*ticket status name*] (this condition is available only if   you've [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306).   You can specify only whole hours, not days or fractional hours. The hours value must be at least zero.  Note: These conditions are not available when you use the option **Tickets can meet any of these conditions to appear in the view**.  Note: If you have [multiple schedules](https://support.zendesk.com/hc/en-us/articles/4408842938522), views based on business hours use your *default* schedule (that is, the first schedule in your schedules list). |
| Ticket: *Custom fields* | Custom fields that set tags (drop-down list and checkbox) are available as conditions. You can select the drop-down list values and Yes or No for checkboxes. You can also use date conditions to specify if the date value is before, after, or on a certain date. For example, you could look for all tickets created in the last hour by using the condition **Hours since created** > **Is** > **1**. The following field types aren't available as view conditions: Text, Multi-line, Numeric, Decimal, Credit Card, Regex.  Note: Each custom checkbox field must have an associated tag. Otherwise, when you create or edit a view, it won't appear as an available condition. |
| Ticket: Privacy | Checks the privacy settings on ticket comments. See [Adding comments to tickets](https://support.zendesk.com/hc/en-us/articles/4408828489370) for information on public vs. private comments. |
| Ticket: Skills | See [Creating skills-based views](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_m52_vhh_ldb). |
| Ticket: CC'd | Checks whether a ticket has any of the specified users as CCs. |
| Ticket: Followers | Checks whether a ticket has any of the specified users as followers. |
| Ticket sharing: Sent to | Checks whether a ticket was shared to another Zendesk Support account via a specific ticket sharing agreement |
| Ticket sharing: Received from | Checks whether a ticket was shared from another Zendesk Support account via a specific ticket sharing agreement |
| Requester: Language | Checks the language used by the end user. Include (*is*) or exclude (*is not*) languages using the drop-down list of supported languages. |

## Cloning a view

You can clone an existing view to create a copy that you can modify and use for some other
purpose. You can clone a view from the Views admin page or from the views list.

If you're on an Enterprise plan and using custom roles, agents need permission to add and
edit personal, group, and global views (see [Creating custom agent roles](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd)). Agents will receive
an error message if not given the permission.

**To clone a view from the Views admin page**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. Hover your mouse over the view you want to clone, then click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) and select **Clone**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_workspace_views_optionsmenu.png)
3. Modify the title, conditions, formatting, and availability as needed.
4. Click **Save**.