# Using the Zendesk Support for Jira integration (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4408827996058-Using-the-Zendesk-Support-for-Jira-integration-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

The legacy Jira integration enhances collaboration
between support and product teams. You can create or link Jira issues
from tickets, track issue progress, and share comments between platforms.
Customize views and add labels to issues. Ensure smooth functionality
by using compatible browsers and consider migrating to the current version
for continued support.

The Jira integration encourages collaboration between product teams and
the support team. For
example, after a customer reports a bug in a ticket, the agent can file
a bug in Jira directly
from your Zendesk. After fixing the bug, a developer can add a comment
to the ticket directly
from Jira.

For information on configuring the Zendesk Support for Jira integration,
see
[Setting up Zendesk Support for Jira integration](https://support.zendesk.com/hc/en-us/articles/4408837969946).

Note: Jira uses
[security headers](https://confluence.atlassian.com/jirakb/security-headers-in-jira-939919914.html)
that affect the behavior of the
Jira app within Firefox web browsers and may cause problems loading
content. If your team
uses the Jira integration and experiences problems, use another web
browser, such as Google
Chrome, to ensure that the Jira app functions as intended.

This article covers the following topics:

- [Using the integration in Zendesk
  Support](#topic_qx5_2gl_xm)
- [Using the integration in Jira](#topic_wgy_wwc_zm)
- [Commenting and comment sharing](#topic_cc3_bcz_42b)

Related articles:

- [Setting up Zendesk Support for Jira integration](https://support.zendesk.com/hc/en-us/articles/4408837969946)
- [Updating a ticket when the status of a Jira issue changes](https://support.zendesk.com/hc/en-us/articles/4408832025114)
- [Reporting on the number of Zendesk tickets linked to a Jira
  issue](https://support.zendesk.com/hc/en-us/articles/4408843823642)
- [Using the Jira field syncing feature](https://support.zendesk.com/hc/en-us/articles/4408825394458)

## Using the integration in Zendesk Support

As an agent, you can create a new Jira issue from a ticket, or link
to an existing Jira
issue from a ticket. You can then use the link to track the progress
made by the product
team on addressing the issue. For example, within Zendesk Support
you can view details about
a bug you filed in Jira to see if the engineering team fixed it.

A single Jira issue can be linked to up to 200 Zendesk Support tickets.

Topics covered in this section:

- [Creating a Jira issue from a
  ticket](#topic_fwb_hwc_zm)
- [Creating a link to an existing Jira issue
  from a ticket](#topic_thj_3wc_zm)
- [Tracking a Jira issue from a
  ticket](#topic_jr2_bzc_zm)
- [Customizing the summary and details
  views](#topic_frt_jyr_zm)
- [Adding a label to a Jira issue from a
  ticket](#topic_okj_r5d_zm)
- [Unlinking a Jira issue from a
  ticket](#topic_ghb_wbd_zm)
- [Searching Jira issues](#topic_brp_wqh_4bb)

You can also automatically notify an agent or a customer when somebody
changes the status
of an issue in Jira. See
[Updating a ticket when the status of a Jira issue changes](https://support.zendesk.com/hc/en-us/articles/4408832025114).

### Creating a Jira issue from a ticket

You can create a Jira issue from a ticket in Support, for example,
when the ticket is a
feature request or a bug report from a customer.

**To create a Jira issue from a ticket**

1. In Zendesk Support, go to the ticket you want to use as a
   basis for a new Jira
   issue.
2. Click **Create Issue** in the Jira
   app next to the ticket.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/create_issue_in_zd.png)

   **Note**:
   If the Jira app is not displayed on the right side of
   the agent interface, click
   **Apps**.
3. Click the **Project** drop-down
   options to display available Jira projects. If you
   start typing the name of the Jira project for the issue,
   the list of suggested projects
   is filtered to match.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_support_select_project.png)
4. Enter the details about the issue.

   - If you’ve selected the option to transfer
     information from your ticket, this
     information is already entered.
   - You can click
     **Copy fields from this ticket** (see
     below) to populate the
     fields, then select the
     **Always copy** checkbox
     to make this the default
     behavior.

     Note that
     **Copy fields from this ticket** only
     copies the subject
     and most recent comment. It does not copy
     any additional custom fields.
   - Select the reporter for the issue. By default,
     the reporter is set to the last
     reporter that was selected when an issue was
     created in this browser. If the
     assignee or reporter you're looking for doesn't
     appear in the suggested user list,
     enter the exact Jira username.

   The default fields are displayed in the image below.
   Administrators can add
   additional fields to this form. For information, see
   [Adding fields to the Jira app in Zendesk
   Support](https://support.zendesk.com/hc/en-us/articles/4408837969946#topic_mgd_rj4_qz).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/default_issue_fields_in_zd.png)
5. (Optional) Click
   **Add reporter as a watcher** to
   include the reporter as a watcher
   to the newly-created issue. See
   [Commenting
   and comment sharing](#topic_cc3_bcz_42b)
   for more information.
6. Click **Create issue**.

A new issue is created in Jira and the ticket is linked to it.
In Zendesk Support, the
Jira app in the sidebar displays the Jira issue name, summary,
and description.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/issue_in_zd.png)

For more information, see
[Customizing the
summary and details views](#topic_frt_jyr_zm).

### Creating a link to an existing Jira issue from a ticket

If you know that an issue is tracked in Jira and you receive
a support request that's
related to it, you can link the ticket to the issue. You can
also link the same ticket to
other issues in Jira.

You can keep track of the number of tickets linked to Jira issues,
and use that metadata
to prioritize your work. See
[Jira: Linked tickets reporting](https://support.zendesk.com/hc/en-us/articles/4408843823642)
for more information.

**To link to an existing Jira issue**

1. In Zendesk, go to the ticket you'd like to link to a Jira
   issue.

   The ticket must be
   an existing ticket. If you are creating a new ticket,
   you'll need to save it
   first.
2. Click **Link Issue** in the Jira
   panel.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/link_issue_in_zd.png)

   **Note**:
   If the Jira app is not displayed on the right side of
   the agent interface, click
   **Apps**.
3. Enter your issue key (XXX-000) or paste a link to the issue.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_select_issue.png)

   If you do not
   know your issue key, you can
   [search Jira
   issues](#topic_brp_wqh_4bb).
4. Click **Link issue**.

The ticket is linked to the existing issue in Jira. In Zendesk
Support, the Jira app in
the sidebar displays the Jira issue name, summary, description,
and comments.

### Tracking a Jira issue from a ticket

The Jira app in the sidebar displays a summary of any issue linked
to the ticket, as well
as any comments associated with it:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/issue_in_zd.png)

Click the **Show More Details** (eye)
icon next to the issue name to view more details
about the issue:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/show_details_in_zd.png)

The details view opens in a new window:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/issue_details_in_zd.png)

You can customize the information displayed in both the summary
and details views. See
[Customizing the summary and details
views](#topic_frt_jyr_zm)
below.

If you're a Jira user too, you can open the issue in Jira by
clicking the issue name in
the summary view. A new browser tab opens and displays the issue.

### Customizing the summary and details views

You can customize the information that's displayed in both the
summary and details views.
For details about the views, see
[Tracking a
Jira issue from a ticket](#topic_jr2_bzc_zm)
above.

**To customize the summary and details views**

1. Click the **Admin icon** in the
   upper-right side of the Jira app next to the
   ticket.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/admin_icon_issue_in_zd.png)
2. Select the information you want to display in the summary
   and details views.

   You
   can add pre-existing or custom Jira fields to these views.
   See
   [Jira custom field type compatibility](https://support.zendesk.com/hc/en-us/articles/4408837969946#topic_jtn_k5c_wxb)
   for a
   list of custom Jira fields that are compatible with the
   Jira app.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/select_summary_details_in_zd.png)
3. Click **Close** to save your choices.

### Adding a label to a Jira issue from a ticket

When creating or linking to a Jira issue from a ticket, a
**jira\_escalated** tag is
added by default to the ticket, and an identical
**jira\_escalated** label is added to
the issue in Jira. You can add more labels to a linked issue
in Jira at any time. Any
ticket tag with a **jira\_** prefix
is added as a matching label to any Jira issue
linked to the ticket.

If the escalating agent has a custom agent role in the Enterprise
plan, the role must
allow the agent to edit tags. See
[Creating custom roles and assigning agents](https://support.zendesk.com/hc/en-us/articles/4408882153882).

**To add a label to a Jira issue**

1. Add a tag with a **jira\_** prefix
   in the **Tags** field in the ticket's
   left
   sidebar:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_tags.png)
2. Update the ticket by clicking **Submit**.

The new label appears in the Details section of the issue in
Jira when the issue is
accessed through a browser, and the Zendesk app is expanded.
The label shows as being
added by the Jira user who opened the issue in the browser.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_labels.png)

### Unlinking a Jira issue from a ticket

- Click the **Unlink** (x) icon in
  the Jira app next to the ticket.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_unlink.png)

### Searching Jira issues

When linking a ticket to a Jira issue, you can search for Jira
issues by keyword, or
using the
[Jira Query Language (JQL)](https://confluence.atlassian.com/jiracorecloud/advanced-searching-765593707.html).
Starting your search
with the project name in capital letters will limit the results
to that project.

**To search Jira issues by keyword**

1. In the **Link Issue** search
   field, enter your search terms. You can limit
   results to a specific project by starting the search
   with the project name in capital
   letters, or you can use
   [JQL](https://confluence.atlassian.com/jiracorecloud/advanced-searching-765593707.html).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira4_search_issues.png)
2. As you're typing, ticket suggestions are made. You can
   select a suggested ticket, or
   continue typing to narrow down the results.

## Using the integration in Jira

As a Jira user, you can view details about tickets linked to your
issues, and add comments
to linked tickets. You can also automatically notify an agent or
a customer when you change
the status of an issue in Jira. See
[Updating a ticket when the status of a Jira issue changes](https://support.zendesk.com/hc/en-us/articles/4408832025114).

This section describes how to view the details of a linked Support
ticket in your Jira
issue. For information on adding comments to linked tickets, see
[Commenting and comment sharing](#topic_cc3_bcz_42b)
below.

**To view the details of a linked Zendesk Support ticket**

1. Navigate to the issue in Jira. In the sidebar under
   **Zendesk Support**, the number
   of linked tickets is displayed. 

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_linked_tickets.png)
2. Double-click on **Linked Tickets**
   to open the linked tickets page.
3. If more than one ticket is linked to the issue, click the
   accordion to expand the
   ticket details.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_linked_ticket_detail.png)
4. To view the ticket in Support, click the linked ticket heading.

## Commenting and comment sharing

When you link Zendesk Support tickets and Jira issues, you can also
share some commenting
functionality between the two platforms.

While the commenting functionality doesn't fully integrate the commenting
systems in
Zendesk Support and Jira, it does allow you to perform the following
tasks, which are
described in this section:

- [Adding a comment to a Jira
  issue from a ticket](#topic_g3z_pcz_42b)
- [Adding a comment to linked
  Zendesk Support tickets from a Jira issue](#topic_mzx_jcz_42b)
- [Notifying Jira issue watchers
  when there are new comments on linked Zendesk tickets](#topic_v2g_kcz_42b)
- [Adding the reporter as a
  watcher when creating a new Jira issue](#topic_pwl_kcz_42b)
- [Adding the current agent as a
  watcher when linking Jira issues](#topic_cvs_kcz_42b)
- [Displaying when the most recent
  comment was added to either account](#topic_in1_lcz_42b)

However, you cannot perform some expected comment-related tasks,
such as:

- Automatically notify Zendesk collaborators when there are new
  comments on
  linked Jira issue, unless they are also watching the Jira issue.
- Mark a comment as having been read by another user.

### Adding a comment to a Jira issue from a ticket

If a Support ticket is linked to a Jira issue, you can add comments
to the Jira
issue from the ticket. This is useful for providing additional
information from customers
to the product team.

Both public and private comments added to a Support ticket are
shared with any
connected Jira issues.

**To add a comment to a Jira issue**

1. Click the **Notify** button in
   the Jira app next to the ticket.
2. Enter the comment you want to add to the issue in Jira.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/notify_issue_in_zd.png)
3. To save typing, you can transfer the last comment made on
   the ticket by clicking
   **Copy the last comment**.
4. Any attachments in ticket comments are shown under
   **Attachments**. Click on the
   attachment to add it to the note.
5. Click **Notify issues**. The note
   is added to the **Activity** section
   in the
   Jira issue.
6. In the **Show** drop-down list,
   select **Comments** to view the
   comment.

### Adding a comment to linked Zendesk Support tickets from a Jira issue

You can notify a Zendesk agent or a customer when you add a comment
to the
linked Jira issue.

When you add a comment to a Jira issue, it adds that comment
to the linked
Support ticket. When the comment is added to the Zendesk ticket,
an email containing your
comment is sent to the agent and any other agent who is copied
on the Support ticket. If
the comment is public, an email is also sent to the customer
who submitted the ticket and
any other end user who is copied on the ticket. Be mindful that
a customer will read your
message when you add a public comment. If in doubt, leave the
comment private.

You can comment on a single linked ticket, or all linked tickets
if you have multiple
tickets linked to an issue. Commenting on all linked tickets
can be performed in the
sidebar or the Activity section of a Jira issue.

**To add a comment to a linked ticket**

1. Navigate to the Jira issue, and in the
   **Activity** drop-down list,
   select **Zendesk Support**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_single_ticket_comment1.png)
2. In the **Ticket** drop-down list,
   select the Support ticket.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_single_ticket_comment2.png)
3. Enter your comment. Select the
   **Make public reply** checkbox
   to make a
   public comment.
4. Click **Add comment**.

**To add a comment to all linked tickets in the Activity section**

1. Navigate to the linked issue in Jira, and in the
   **Activity** drop-down list,
   select **Zendesk Support**.
2. Enter your comment, select the
   **Add for all tickets** checkbox,
   and click
   **Save**.

**To add a comment to all linked tickets in the sidebar**

1. In the sidebar under **Zendesk Support**,
   double-click on **Linked Tickets**.
   The linked ticket page opens.
2. Click **Add comments to linked tickets**,
   which opens a page.
3. Enter your comment and click **Send**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_comment_all_tickets.png)

**To make all comments private**

1. In the Jira top nav bar, select **More**
   >**Apps** > **Manage
   your apps**.
2. Click the **Zendesk Support for Jira** 
   accordion, then click
   **Configure**.
3. In the **Settings** >
   **Other options** section, select
   the
   **Disable all public comments to Zendesk**
   checkbox.
4. Click **Save**.

### Notifying Jira issue watchers when there are new comments on linked Zendesk tickets

Users watching a Jira issue with linked Zendesk tickets can receive
a notification email
from Jira when public comments are added to linked tickets.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_comment_settings.png)

**To enable comment notifications**

1. In the Jira top navigation bar, select
   **More** >
   **Apps** >
   **Manage your apps**.
2. Click the **Zendesk Support for Jira**
   accordion, then click **Configure**.
3. In the **Settings** >
   **Other options** section, select
   the
   **Send
   email notification to issue watchers when comments are added to linked tickets**
   checkbox.
4. Click **Save**.

### Adding the reporter as a watcher when creating a new Jira issue

When creating a new Jira issue from a Support ticket, or when
linking a ticket to an
existing issue, you can add the reporter as a watcher to the
newly-created issue.

Jira also allows you to watch an issue. When you watch an issue,
you receive
email notifications when certain updates are made. Depending
on how your issue
notifications are configured, you may receive an email when:

- The story has been updated (such as the description)
- The status changes (assigned, closed)
- A comment is submitted

**To add a reporter as a watcher**

- When creating a Jira issue from a Zendesk Support ticket,
  select the
  **Add
  reporter as a watcher**
  checkbox.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_reporter_as_watcher_in_zd1.png)

### Adding the current agent as a watcher when linking Jira issues

When linking an existing issue to a ticket in Support, the current
user is added as a
watcher to that issue in Jira. Note that for this to be successful,
the Jira user profile
must contain the Zendesk agent's email or full name.

### Displaying when the most recent comment was added

In the Zendesk Support panel in Jira, you can display how much
time has elapsed since the
last comment was added to the ticket in Zendesk.

**To enable the last comment added display**

1. In the Jira top nav bar, select **More**
   > **Apps** >
   **Manage your apps**.
2. Click the **Zendesk Support for Jira**
   accordion, then click
   **Configure**.
3. In the **Settings** >
   **Zendesk Support ticket fields**
   section, select the
   **Last Commented** checkbox
4. Click **Save**.