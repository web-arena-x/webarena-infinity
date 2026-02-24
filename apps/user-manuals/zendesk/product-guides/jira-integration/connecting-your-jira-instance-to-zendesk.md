# Connecting your Jira instance to Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/9797104268058-Connecting-your-Jira-instance-to-Zendesk

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Connect your Jira instance to manage and track issues directly from your
support platform. This integration lets agents view, link, and create
Jira issues while handling tickets, and allows product teams to access
customer-reported issues. Ensure you're an admin to set up the connection,
and remember that the integration doesn't support Jira Data Center or
Server. Configure features like ticket view and field sync as needed.

The Jira integration for Zendesk offers a powerful solution that connects
your product
and support teams. To use the integration, first connect your Jira instance
to Zendesk,
as described in this article. Then, configure the integration according
to your desired
usage.

Information will be available soon for customers who have already installed
and configured the legacy integration, including details on migrating
to the new integration.

Note: This integration doesn't support
Jira Data Center and Jira
Server, as Atlassian is planning to discontinue these platforms. See
Atlassian's
announcements for
[Jira Data Center](https://www.atlassian.com/migration)
and
[Jira Server](https://www.atlassian.com/licensing/server-end-of-support#serv-end-of-support).

This article includes the following topics:

- [Understanding the different ways to use the integration](#topic_swl_zkw_q2c)
- [Considerations](#topic_v2v_1lw_q2c)
- [Connecting your Jira instance](#topic_cxr_vlw_q2c)
- [Viewing and editing your connections](#topic_dpq_1wz_t2c)
- [Disconnecting your Jira instance](#topic_rmq_jkt_sjb)

## Understanding the different ways to use the integration

After you’ve connected your Jira instance to Zendesk, the integration
may require
additional configuration, depending on how you plan to use it.

### Allow support agents to view, link, and create Jira issues in Zendesk

Enable your customer service agents to manage Jira issues directly
from Zendesk
while they handle tickets. Consider setting up the following
features:

- **[The Jira app for Zendesk](https://support.zendesk.com/hc/en-us/articles/9810169980058)**
  allows agents to view and interact with linked Jira issues
  from the Zendesk
  ticket sidebar, facilitating direct collaboration with your
  product team.
  For example, if a customer reports a bug through a Zendesk
  ticket, the agent
  can immediately log the bug in Jira. After the issue is resolved,
  a
  developer can comment on the ticket from Jira, notifying
  followers and
  displaying updates in the Zendesk ticket sidebar.
- **[Field sync](https://support.zendesk.com/hc/en-us/articles/9827183512730)**
  allows
  real-time data updates between Zendesk and Jira. For example,
  syncing a
  priority field ensures that both support and product teams
  are informed
  about the current progress and priority of issues.

### Give Jira users visibility to customer-reported issues in Zendesk

Allow product teams to view Zendesk tickets directly in Jira,
enabling them to
investigate customer-reported issues more thoroughly. Consider
setting up the
following features:

- **[Zendesk ticket view for
  Jira](https://support.zendesk.com/hc/en-us/articles/9810155413146)**
  provides product teams with real-time access to Zendesk
  tickets directly within Jira, allowing Jira users to view
  Zendesk ticket
  data in the Jira sidebar for issue context. Additionally,
  ticket view allows
  Jira users to add comments to linked Zendesk tickets in an
  issue's Activity
  tab.
- **[Field sync](https://support.zendesk.com/hc/en-us/articles/9827183512730)**
  ensures that
  both systems have consistent and up-to-date information.

## Considerations

- You must be a Zendesk Support admin and a Jira admin to set up
  your integration.
- If the Zendesk admin who connected the integration has their
  role downgraded,
  the integration will cease to function. It will require the integration
  to be
  disconnected, then reconnected in Admin Center by another Zendesk
  admin.

## Connecting your Jira instance

Set up and configure your integration in Admin Center. You should
test the
integration with your Zendesk and Jira sandbox environments first.

Multiple connections are supported. Repeat these steps for each instance
you’d like
to connect to Zendesk.

**To connect Jira to Zendesk**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Jira**.
3. If you already have connections set up, they display in the
   connections
   list. To add another connection, click
   **Add connection**.
4. Select the type of Jira instance you'd like to connect:
   **Atlassian
   Cloud**
   or **Atlassian Government Cloud (AGC)**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Jira_v2_connect_account_AGC_2.png)
5. Enter your **Jira account URL**
   in the text field.

   You must be an
   administrator of this account to connect the integration.
6. Select the checkbox to agree to the
   **Built by Zendesk Terms of Use**,
   then click **Connect Jira**.

   You are directed to an authorization
   page.
7. In the **Use app on** menu, select
   the Jira account for which you entered
   the URL on the previous page.

   This step grants Zendesk access to data in
   your Atlassian account.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Jira_v2_grant_access.png)
8. Click **Accept**.

   You are directed back to Admin Center. The new
   connection displays in the Jira connections list. The
   [Jira app for Zendesk](https://support.zendesk.com/hc/en-us/articles/9810169980058)
   is now
   connected, but ticket view and field mapping are inactive.

Next, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png))
next to the Jira instance and click
**Configure**
to set up the integration, depending on how you plan to use it. See
[Understanding the different ways to use
the integration](#topic_swl_zkw_q2c).

## Viewing and editing your connections

Use the Integrations page in Admin Center to view and edit your Jira
connections with
Zendesk.

**To view or edit your Jira connections**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Jira**.

   The connections appear in a list.
   Each connection displays which features are active: Support
   app, Ticket
   view, and Field mapping.
3. To edit the connection name or view details, click the name of
   a
   connection.
4. Make changes as needed, then click **Save**.

## Disconnecting your Jira instance

You can disconnect your Jira instance from Zendesk in Admin Center.
After it's
disconnected, your configuration settings are still retained if you
decide to
connect to the same instance.

Each time you connect to a new or previously connected instance,
you must activate
the following features, if applicable to your setup:

- [The Jira app for Zendesk](https://support.zendesk.com/hc/en-us/articles/9810169980058)
- [Zendesk ticket view for Jira](https://support.zendesk.com/hc/en-us/articles/9810155413146)
- [Field sync](https://support.zendesk.com/hc/en-us/articles/9827183512730)

**To disconnect a Jira instance**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Jira**.
3. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png))
   next to the Jira instance you want to
   disconnect, then click **Disconnect**.