# Setting up Zendesk ticket view for Jira

Source: https://support.zendesk.com/hc/en-us/articles/9810155413146-Setting-up-Zendesk-ticket-view-for-Jira

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Admins can set up a ticket view for Jira to enhance collaboration between support and product teams. This integration allows you to access ticket data directly in Jira, helping prioritize and address issues. You can configure ticket fields, comment types, and email notifications. Note that this integration isn't supported for Jira Data Center and Jira Server.

Admins can set up Zendesk ticket view for Jira to help improve collaboration between
support and product teams. This app provides users working in Jira with real-time access
to Zendesk ticket data, allowing teams to prioritize and address issues more
effectively.

Note: This integration doesn't support Jira Data Center and Jira
Server, as Atlassian is planning to discontinue these platforms. See Atlassian's
announcements for [Jira Data Center](https://www.atlassian.com/migration) and [Jira Server](https://www.atlassian.com/licensing/server-end-of-support#serv-end-of-support).

This article includes the following topics:

- [Understanding where Zendesk ticket data appears in Jira](#topic_swl_zkw_q2c)
- [Installation requirements](#topic_v2v_1lw_q2c)
- [Installing and turning on Zendesk ticket view](#topic_axj_2c2_sjb)
- [Configuring Zendesk ticket view](#topic_kmb_ks5_wgc)

Related topics:

- [Configuring the Jira app for Zendesk
  Support](https://support.zendesk.com/hc/en-us/articles/9810169980058)
- [Using the Zendesk Support for Jira
  integration](https://support.zendesk.com/hc/en-us/articles/9827173048858)

## Understanding where Zendesk ticket data appears in Jira

After ticket view is installed and turned on, users working in Jira can access
Zendesk ticket data in the Jira sidebar and activity bar.

The Zendesk Support app in the Jira sidebar shows ticket data when you view a Jira
issue. You can see all Zendesk tickets linked to the issue, unlink tickets, and view
ticket fields based on your [configuration](#topic_kmb_ks5_wgc). If there are multiple linked tickets, you can find the
right one using search or sort features. You can also switch between different
Zendesk accounts if needed.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_jira_sidebar_4.png)

The activity bar at the bottom of a Jira issue includes a Zendesk Support tab, which
displays comments from the linked Zendesk tickets. Depending on your [configuration](#topic_kmb_ks5_wgc), you can add
internal or public comments, which are also added to the Zendesk ticket. If you've
configured the integration to send notifications, issue followers are sent an email
notification when comments are added to linked tickets.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_jira_activity_2.png)

## Installation requirements

The user installing Zendesk ticket view must have admin permissions in both Jira and
Zendesk Support. Additionally, the user must be a member of the
**jira-administrators** and **jira-software-users** groups in Jira.

## Installing and turning on Zendesk ticket view

Follow the procedures outlined in this section if you're installing the Zendesk app
in Jira for the first time or re-installing it.

There are three steps to installing and turning on the app:

1. [Connecting your Zendesk Support instance to Jira](#topic_tsg_gm3_xcc)
2. [Installing the Zendesk app](#topic_u5g_gq5_wgc)
3. [Turning on Zendesk ticket view](#topic_ncf_1m3_xcc)

### Connecting your Zendesk Support instance to Jira

Before installing the Zendesk app in Jira, you must first connect your Zendesk
and Jira accounts. You must be an admin in both Zendesk and Jira to complete
this task.

For details, see [Connecting your Jira instance to
Zendesk](https://support.zendesk.com/hc/en-us/articles/9797104268058).

### Installing the Zendesk app

After connecting your Zendesk and Jira accounts, install the Zendesk Support app
in Jira.

**To install and configure the Zendesk app**

1. In Jira, click **Apps** in the top navigation bar, then select **Explore
   more apps**.
2. On the Marketplace apps page, search for **Zendesk**.
3. Locate and click the **Zendesk Support for Jira v2.0** entry in the
   search results.
4. Click **Get app**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_ticket_view_app_v2.png)
5. Click **Get it now**.

### Turning on Zendesk ticket view

Turning on Zendesk ticket view makes Zendesk ticket data visible to Jira users.
If you haven't yet [configured](#topic_kmb_ks5_wgc) the app, return to this step when you're ready. You can
also turn off the app if you need to hide it temporarily.

**To turn on Zendesk ticket view**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Jira** link.
3. If you have multiple connections, click the name of the connection you are
   setting up.
4. Click the **Ticket view** tab.
5. Select **Turn on Zendesk ticket view for Jira** to make it visible to
   agents. Deselect this option to hide the app from agents.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_ticket_view_enable.png)
6. Click **Save**.

## Configuring Zendesk ticket view

You can configure Zendesk ticket view to update the list of Zendesk ticket fields
that appear in Jira, change the type of comments users can view or add (internal or
public), and turn on or off email notifications for comments.

**To configure Zendesk ticket view**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Jira** link.
3. If you have multiple connections, click the name of the connection you are
   setting up.
4. Click the **Ticket view** tab.

   Configuration options appear in the center
   of the Ticket view tab.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_ticket_view_config_options.png)
5. The Zendesk Support ticket fields section displays the preselected default
   Zendesk fields to display in the Jira sidebar. To add fields, begin typing in
   the field to open a drop-down list of available fields to select, or click "x"
   next to a field to remove it.
6. In the Comments section, select whether to allow users to view or add comments
   from the Activity tab of a Jira issue.
   - Select **View** to display comments with that type (internal or
     public) within the Activity tab of a Jira issue.
   - Select **Add** to allow users to add comments with that type
     (internal or public) within the Activity tab of a Jira issue.
7. Select **Send an email notification to issue watchers when comments are added
   to linked tickets** to turn on this email notification.
8. Click **Save**.