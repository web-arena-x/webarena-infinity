# Using the Jira integration for Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/9827173048858-Using-the-Jira-integration-for-Zendesk

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

The Jira integration lets you create, link, and manage Jira issues directly from tickets, fostering collaboration between support and product teams. You can add labels, search issues, and share comments between platforms. If you encounter issues with Firefox, try another browser like Chrome for optimal performance. This integration streamlines communication and enhances issue tracking across both platforms.

The Jira integration for Zendesk encourages collaboration between product and support
teams. For example, after a customer reports a bug in a ticket, the agent can file a bug
in Jira directly from Zendesk. After fixing the bug, a developer can add a comment to
the ticket directly from Jira.

Note: Jira uses [security headers](https://confluence.atlassian.com/jirakb/security-headers-in-jira-939919914.html) that affect the behavior of
the Jira app within Firefox web browsers and may cause problems loading content. If your
team uses the Jira integration and experiences problems, use another web browser, such
as Google Chrome, to ensure the Jira app functions as intended.

This article covers the following topics:

- [Using the integration in Zendesk
  Support](#topic_qx5_2gl_xm)
  - [Creating a Jira issue from a ticket](#topic_fwb_hwc_zm)
  - [Linking or unlinking an existing Jira issue from a ticket](#topic_thj_3wc_zm)
  - [Adding a label to a Jira issue from a ticket](#topic_okj_r5d_zm)
  - [Searching Jira issues](#topic_brp_wqh_4bb)
- [Using the integration in Jira](#topic_wgy_wwc_zm)
- [Commenting and comment
  sharing](#topic_cc3_bcz_42b)

Related articles:

- [Configuring the Jira app for Zendesk
  Support](https://support.zendesk.com/hc/en-us/articles/9810169980058)
- [Setting up ticket view for Jira](https://support.zendesk.com/hc/en-us/articles/9810155413146)

## Using the integration in Zendesk Support

As an agent, you can create a new Jira issue from a ticket, or link to an existing
Jira issue from a ticket. You can then use the link to track the progress made by
the product team on addressing the issue. For example, within Zendesk Support, you
can view details about a bug you filed in Jira to see if the engineering team fixed
it.

This topic includes the following sections:

- [Creating a Jira issue from a
  ticket](#topic_fwb_hwc_zm)
- [Creating a link to an existing
  Jira issue from a ticket](#topic_thj_3wc_zm)
- [Adding a label to a Jira issue
  from a ticket](#topic_okj_r5d_zm)
- [Searching Jira
  issues](#topic_brp_wqh_4bb)

### Creating a Jira issue from a ticket

You can create a Jira issue from a ticket in Support, for example, when the
ticket is a feature request or a bug report from a customer.

**To create a Jira issue from a ticket**

1. In Zendesk Support, go to the ticket you want to use as a basis for a new
   Jira issue.
2. In the Jira sidebar app, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)), then click **Create issue**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_app_create_issue.png)

   If the Jira app isn't displayed on the right side of the Agent
   Workspace, click the Apps icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_apps.png)) in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362) to open
   it.
3. Click the **Project** menu to display available Jira projects. If you
   start typing the name of the Jira project for the issue, the list of
   suggested projects is filtered to match.
4. Enter the details about the issue.

   1. Select the **Work type**, which is custom to your company.
      For example, work types could include Bug, Feature, Task, or
      Improvement. After you select the work type, additional fields
      related to that work type may appear.
   2. In the **Reporter** field, leave the default reporter for the
      issue, or select a different reporter. If the assignee or
      reporter you're looking for doesn't appear in the suggested user
      list, enter the exact Jira user name.

      By default, the Reporter
      field displays the user whose email address matches the
      ticket requester's. If no match is found, it displays the
      signed-in agent.
   3. Click **Copy fields from this ticket** to populate the issue
      fields using the values from the ticket. This option only copies
      the subject and most recent comment. It doesn't copy any
      additional custom fields.

   Below is an example form, but your admin can [customize the form](https://support.zendesk.com/hc/en-us/articles/9810169980058#topic_mgd_rj4_qz) based on
   work type.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_app_create_issue2.png)
5. Click **Create issue**.

A new issue is created in Jira, and the ticket is linked to it.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_app_linked_issue.png)

### Linking or unlinking an existing Jira issue from a ticket

If you know that an issue is tracked in Jira and you receive a support request
that's related to it, you can link the ticket to the issue. You can also link
the same ticket to other issues in Jira.

When linking an existing issue to a ticket in Support, the current user is added
as a watcher to that issue in Jira. The Jira user profile must contain the
Zendesk agent's email or full name.

You can remove the link if it's no longer needed.

Tip: For best results, it's recommended to link
one Jira issue to one Zendesk ticket and use [problem and incident tickets](https://support.zendesk.com/hc/en-us/articles/4408835103898) to manage
related incidents.

**To link to an existing Jira issue**

1. In Zendesk, go to the ticket you'd like to link to a Jira issue.

   The
   ticket must be an existing ticket. If you're creating a new ticket,
   you'll need to save it first.
2. In the Jira sidebar app, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)), then click **Link issue**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_app_create_issue.png)

   If the Jira app is not displayed on the right side of the Agent
   Workspace, click the Apps icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_apps.png)) in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362) to open
   it.
3. In the Link issue field, enter your issue key (XXX-000) or paste a link to
   the issue.

   If you don't know your issue key, you can [search Jira issues](#topic_brp_wqh_4bb) by
   typing keywords.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_app_search_link.png)
4. Click **Link issue**.

After the Jira issue is linked, it appears in the Jira app in the Zendesk Support
sidebar as a linked issue.

**To unlink an existing Jira issue**

1. In the sidebar app, click the unlink icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_unlink.png))
   next to the issue.
2. Click **Unlink**.

### Adding a label to a Jira issue from a ticket

When creating or linking to a Jira issue from a ticket, a **jira\_escalated**
tag is added by default to the ticket, and an identical **jira\_escalated**
label is added to the issue in Jira. You can add more labels to a linked issue
in Jira at any time. Any ticket tag with a **jira\_** prefix is added as a
matching label to any Jira issue linked to the ticket.

If the escalating agent has a [custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882), the role must allow the
agent to edit tags.

**To add a label to a Jira issue**

1. [Add a tag](https://support.zendesk.com/hc/en-us/articles/4408835059482#topic_vwg_ola_vb) with a **jira\_**
   prefix in the **Tags** field in the ticket's left sidebar.
2. Update the ticket by clicking **Submit**.

The new label appears in the Details section of the issue in Jira when accessed
through a browser, and the Zendesk app is expanded. The label shows as being
added by the Jira user who opened the issue in the browser.

### Searching Jira issues

When linking a ticket to a Jira issue, you can search for Jira issues by
keyword.

**To search Jira issues by keyword**

1. In the **Link Issue** search field in the sidebar app, enter your
   search terms. You can limit results to a specific project by starting
   the search with the project name in capital letters.
2. As you're typing, ticket suggestions are made. You can select a
   suggested ticket or continue typing to narrow the results.

## Using the integration in Jira

If your admin turned on [Zendesk ticket view](https://support.zendesk.com/hc/en-us/articles/9810155413146), you can view details about tickets
linked to your Jira issues and add comments to linked tickets.

This section describes how to view the details of a linked Support ticket in your
Jira issue. For information on adding comments to linked tickets, see [Commenting and comment
sharing](#topic_cc3_bcz_42b).

**To view the details of a linked Zendesk Support ticket**

1. Navigate to the issue in Jira.

   Linked tickets display in the Zendesk
   Support app in the Jira sidebar.
2. If multiple tickets are linked to the issue, expand a ticket header to view
   details.

   If you have multiple Zendesk accounts connected, select a
   Zendesk subdomain in the drop-down menu to view linked tickets by
   account.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_jira_sidebar_2.png)
3. To view the ticket in Zendesk Support, click the linked ticket heading.

## Commenting and comment sharing

When you link Zendesk Support tickets and Jira issues, you can also share some
commenting functionality between the two platforms.

While the commenting functionality doesn't fully integrate the commenting systems in
Zendesk Support and Jira, it does allow you to perform the following tasks, which
are described in this section:

- [Adding a comment to linked Jira issues from a Zendesk ticket](#topic_g3z_pcz_42b)
- [Adding a comment to linked Zendesk tickets from a Jira issue](#topic_mzx_jcz_42b)

You can't perform some comment-related tasks, such as:

- Automatically notify Zendesk collaborators when there are new comments
  on a linked Jira issue, unless they are also watching the Jira issue.
- Mark a comment as having been read by another user.

### Adding a comment to linked Jira issues from a Zendesk ticket

If a Support ticket is linked to a Jira issue, you can add comments to
the Jira issue from the ticket. This is useful for providing additional
information from customers to the product team.

Both public and private comments added to a Support ticket are shared
with all linked Jira issues. See [Configuring Zendesk ticket view](https://support.zendesk.com/hc/en-us/articles/9810155413146#topic_kmb_ks5_wgc) to
configure integration settings for internal and public comments.

**To add a comment to a Jira issue**

1. In the Jira sidebar app, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)), then click **Notify issue**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_app_create_issue.png)

   If the Jira app isn't displayed on the right side of the agent
   interface, click the Apps icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_apps.png)) in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362) to open
   it.
2. Enter the comment you want to add to the issue in Jira.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_notify_linked.png)
3. To save typing, you can transfer the last comment made on the ticket by
   clicking **Copy the last comment** or **Append the last
   comment**.
4. Click **Notify issue**.

   The note is added to the ticket and the
   Comments section in the Jira issue.

### Adding a comment to linked Zendesk tickets from a Jira issue

You can notify a Zendesk agent or a customer when you add a comment to
the linked Jira issue.

When the comment is added to the Zendesk ticket using the Zendesk
Support app in the Activity tab, an email containing your comment is sent to the
agent and any other agent who is copied on the Support ticket. If the comment is
public, an email is also sent to the customer who submitted the ticket and any
other end user who is copied on the ticket. Be mindful that a customer will read
your message when you add a public comment. If in doubt, leave the comment
private.

You can comment on a single linked ticket, or all linked tickets if you have
multiple tickets linked to an issue. Commenting on all linked tickets can be
performed in the sidebar or the Activity section of a Jira issue.

**To add a comment to a linked ticket**

1. Navigate to the Jira issue, and in the Activity section, click the
   **Zendesk Support** tab.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_jira_activity_2.png)
2. In the Select Zendesk ticket menu, select the ticket you'd like to
   add the comment to.
3. Select **Add internal note** to add a private comment, or click **Add
   public reply** to add a public comment.
4. Enter your comment.
5. Click **Add** to add the note to the current ticket only, or
   click **Add to all tickets** to add the comment to all linked
   tickets.