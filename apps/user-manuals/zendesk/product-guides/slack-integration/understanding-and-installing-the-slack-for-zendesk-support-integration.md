# Understanding and installing the Slack for Zendesk Support integration

Source: https://support.zendesk.com/hc/en-us/articles/4408833756698-Understanding-and-installing-the-Slack-for-Zendesk-Support-integration

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

The Slack integration lets you manage support tickets directly in Slack channels. You can receive ticket notifications, create new tickets, and use side conversations. It supports multiple Slack workspaces and accounts, and includes the Answer Bot for article suggestions. Easily install or remove connections as needed, but note that shared Slack workspaces aren't supported.

Slack for Zendesk Support is a Built-by-Zendesk integration that can connect one or more
Zendesk subdomains to multiple Slack workspaces. It allows you to interact with Zendesk
Support tickets in your Slack channels.

This article covers the following topics:

- [About the Slack for Zendesk Support integration](#topic_fkh_s2d_pvb)
- [Considerations when connecting multiple accounts](#topic_rhb_dxc_r1c)
- [Installing the integration to add a connection between Slack and Zendesk](#topic_vrx_4x4_ldb)
- [Removing a connection between Zendesk and Slack](#topic_ryg_qmx_dvb)

Related articles:

- [Creating and managing triggers for Slack](https://support.zendesk.com/hc/en-us/articles/4963959597594)
- [Using the Slack for Zendesk Support integration](https://support.zendesk.com/hc/en-us/articles/4408843621530)
- [Using the Answer Bot for Slack integration](https://support.zendesk.com/hc/en-us/articles/4408827411098)

## About the Slack for Zendesk Support integration

Note: The Slack for Zendesk Support integration is not part of the [Slack Direct Messages channel](https://support.zendesk.com/hc/en-us/articles/4629038081306#topic_wd1_zjm_25b), which allows end
users to create tickets by sending a direct message to a handle within Slack.

The Slack for Zendesk Support integration includes the following features:

- **Ticket event notifications in Slack**: Slack users can see information
  about Zendesk Support ticket events in specified Slack channels. Using [triggers](https://support.zendesk.com/hc/en-us/articles/4963959597594), Zendesk administrators can configure which conditions
  will send notifications, the Slack channels to send them to, and the information included
  in the notification message.
- **Create new tickets directly from Slack**: This feature is designed to cater to an
  internal use case where Slack users want to raise a new Support ticket directly from
  Slack. See [Creating tickets in Slack](https://support.zendesk.com/hc/en-us/articles/4408843621530#topic_xgp_1z4_ldb).
- **Side conversations**: Agents can use [side conversations](https://support.zendesk.com/hc/en-us/articles/4408844202778) in a ticket to initiate and participate in
  Slack threads.
- **Answer Bot for Slack**: The [Answer Bot for Slack integration](https://support.zendesk.com/hc/en-us/articles/4408827411098) is included in the Slack for
  Zendesk Support integration and utilizes Answer Bot to listen on selected Slack channels.
  It resolves questions by providing article suggestions from your Guide knowledge
  base.
- **Support for multiple connections**: You can [connect](#topic_rhb_dxc_r1c) multiple Zendesk accounts to one or more Slack
  workspaces.

## Considerations when connecting multiple accounts

It's common for organizations to have internal teams with their own Zendesk accounts but
share a single Slack workspace. Similarly, a company can have just one Zendesk account and
collaborate in several Slack workspaces.

The good news is that the integration is flexible and allows you to use one or more Slack
workspaces to respond to customer inquiries sourced from multiple Zendesk accounts.

Things to consider when adding multiple connections:

- When [installing the integration](#topic_vrx_4x4_ldb),
  you add one Slack-to-Zendesk connection at a time.
- When adding new connections between Zendesk and Slack, [create triggers](https://support.zendesk.com/hc/en-us/articles/4963959597594) for the Slack ticket notifications you want to
  send.
- If you're using Answer Bot for Slack and a question is posted in a channel, users will
  receive article suggestions from all your help centers. Article suggestions aren't
  combined into a single response from Answer Bot—users will see multiple Answer Bots
  responding.
- If you plan to use Slack in side conversations, you must [turn on side conversations](https://support.zendesk.com/hc/en-us/articles/6894206691866#topic_fhm_sgl_r1c) for each Slack
  workspace.
- The integration supports [multi-workspace channels](https://slack.com/help/articles/115001399587), which are shared among
  multiple workspaces in an Enterprise Grid organization. However, it does not support
  organization-shared channels, which are configured to be shared among *all*
  workspaces in an Enterprise Grid organization (applies to Slack Enterprise Grid plans
  only).

## Installing the integration to add a connection between Slack and Zendesk

To install the integration, you must have administrative privileges in Zendesk Support and
have permission to install apps in the Slack workspace. Additionally, the integration cannot
be installed on a shared Slack workspace (a workspace you don't own but have been invited to
as an external user).

The installation adds a connection between one Zendesk account and one Slack workspace. To
add multiple connections, run the installation for each connection. For example, if your
company uses one Slack workspace with three Zendesk accounts, run the installation three
times to make these connections.

After the integration is installed, tickets can be created from any Slack channel, but the
app needs to be [added to each channel](https://support.zendesk.com/hc/en-us/articles/6894206691866#topic_tjj_vjx_dvb) that requires notifications
and Answer Bot.

**To connect Slack and Zendesk**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to Slack, then click **View**.
3. Click **Connect workspace**.
4. If your company uses multiple Slack workspaces, make sure the drop-down list in the
   upper right corner displays the name of the workspace you'd like to connect to Zendesk,
   then click **Allow**.
5. Click **Set up in Zendesk Admin Center** to [configure this connection](https://support.zendesk.com/hc/en-us/articles/6894206691866), or repeat this procedure to add more
   connections.

Note: If your Slack **Approve apps** permission setting is off, you can potentially break
the integration when another instance is installed. We recommend turning on the **Approve
apps** setting in Slack or advising your Slack users not to reinstall the
integration.

## Removing a connection between Zendesk and Slack

If you no longer want to use the Zendesk app in a Slack workspace, disconnect the
integration for that workspace. You can disconnect from Admin Center or Slack; the result is
the same. It's important to note that you won’t receive ticket notifications in your
channels for that workspace or be able to create tickets from Slack.

Your configuration settings will not be lost even if you reinstall the app. However, you
will have to [re-add the app](https://support.zendesk.com/hc/en-us/articles/6894206691866#topic_tjj_vjx_dvb) to Slack channels.

**To disconnect using Admin Center**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to Slack, then click **View**.
3. Click **Configure** under the name of the Slack workspace to disconnect.
4. Click **Actions**, then click **Disconnect** from the drop-down menu.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_disconnect.png)
5. Click **Disconnect** in the confirmation message.

**To disconnect using Slack**

1. Sign in to your Slack workspace.
2. Under **Apps**, click **Zendesk**.
3. Under **Connected Zendesk accounts**, click **Disconnect** for the account you'd
   like to disconnect.