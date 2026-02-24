# Migrating the Zendesk Jira integration when moving Jira instances (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4408830699546-Migrating-the-Zendesk-Jira-integration-when-moving-Jira-instances-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

To migrate your Jira integration when moving Jira instances, first create
a new Jira instance and transfer your data, ensuring issue key data is
maintained. Disconnect the current integration, then install and configure
it on the new instance. Use the migration tool to update links from the
old to the new instance. Track progress, which may take up to an hour,
without disrupting other features.

This article describes the process for migrating the Zendesk Support
for Jira integration
when moving Jira instances, such as migrating from Jira Server to a Jira
Cloud
instance.

This article covers the following topics:

- [Requirements](#topic_gcw_ywx_ypb)
- [Migrating the Zendesk Support for Jira integration](#topic_k3w_bxx_ypb)

## Requirements

You must maintain Jira issue key data when transferring Jira issues
between Jira
accounts. Additionally, your Jira instance must be public (not behind
a firewall)
for Zendesk to migrate your links between Jira instances.

## Migrating the Zendesk Support for Jira integration

Migrating the integration consists of installing and configuring
the Zendesk
integration in the new Jira instance, then using the migration tool
in Jira to
update links from the old instance to the new one.

**To migrate the Zendesk Support for Jira integration**

1. Following Atlassian's recommendations, create a new Jira
   instance and
   migrate your data from the old Jira instance. For more information,
   see
   [Migrate your Atlassian Server to
   Cloud](https://support.atlassian.com/migration/resources/).

   Important: Ensure
   that you maintain
   the Jira issue ID and issue key data during the migration.
2. In Jira administration, disconnect the current Zendesk Support
   for Jira
   integration.
   1. Click the **Settings**
      cog, then select **Apps**
      >
      **Manage apps** >
      **Zendesk Support for JIRA**
      >
      **Configure** >
      **Settings**.
   2. On the Settings page, click
      **Disconnect** at
      **Zendesk Support
      URL**.
   3. Click **Save**.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_zendesksupport_settings_disconnect.png)
3. Install and configure the Zendesk Support for Jira integration
   on the new
   instance. See
   [Setting up the Zendesk Support for Jira
   integration](https://support.zendesk.com/hc/en-us/articles/4408837969946).
4. After installing the integration on the new Jira instance,
   migrate links
   from the disconnected Jira instance to the new instance.
   1. In Jira administration, navigate to
      **Apps** >
      **Manage
      apps**
      > **Zendesk Support for JIRA**
      >
      **Configure** >
      **Link Migration**. The
      previously
      connected Jira instances display in a list.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_migrate_links.png)
   2. Click **Migrate links**
      for each previously connected Jira
      instance. The link transfer processes and restores
      the ticket
      links.

You can track the migration process here. It may take up to an hour,
depending on the
number of links. You can continue using all other integration features
while the
migration progresses. When the migration is complete, the previously
connected Jira
instance displays **100% complete**.