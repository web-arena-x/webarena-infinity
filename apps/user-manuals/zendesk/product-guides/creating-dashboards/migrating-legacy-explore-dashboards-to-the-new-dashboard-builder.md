# Migrating legacy Explore dashboards to the new dashboard builder

Source: https://support.zendesk.com/hc/en-us/articles/8096478451098-Migrating-legacy-Explore-dashboards-to-the-new-dashboard-builder

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

This article covers the new Explore dashboard builder, released in November 2024. The legacy dashboard builder will remain available until December 31, 2026 (previously February 28, 2026), after which legacy dashboards will become view-only. If you’re using the legacy dashboard builder and need help, see [About the legacy Explore dashboard builder](https://support.zendesk.com/hc/en-us/articles/8210448879002).

The new version of the Explore dashboard builder makes it more straightforward and more intuitive to create dashboards that provide insights into your support and help optimize your service channels.

When you start using the new dashboard builder, you’ll find that most of your legacy dashboards can be migrated to the new dashboard builder with a few clicks. However, some of your dashboards may require additional work before you can work with them in the new dashboard builder.

Important: Zendesk is currently transitioning to a new version of the dashboard builder. There are two types of dashboards, and each one requires a different action from you before you can use them in the new dashboard builder:

- **Prebuilt dashboards:** Ready-to-use dashboards provided with Explore, displaying information in an easy-to-read format. These will be automatically migrated; however, you'll need to recreate any shares or schedules that you previously configured.
- **Custom dashboards:** These are dashboards created or customized by a Zendesk Explore admin or editor. You'll need to migrate these dashboards to the new builder using the importer tool.

In this article, you’ll learn how to discover which dashboards are ready to migrate to the new dashboard builder and how to prepare dashboards that need extra work.

This article contains the following topics:

- [Understanding the migration status of your dashboards](#topic_ul5_m3v_bdc)
- [Migrating legacy dashboards](#topic_zgd_p3v_bdc)

## Understanding the migration status of your dashboards

Explore helps you see which of your dashboards can be used immediately in the new dashboard builder and which need work before you can use them.

**To view the migration status of your dashboards**

- In Explore, click the **Dashboards library** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) on the left sidebar.

  In the list of dashboards, you can see the migration status of each dashboard in the **Migration** column.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_migrat_1.png)

For each dashboard, one of the following migration statuses is displayed:

- **Migrate:** You can click **Migrate** to start migrating your dashboard immediately. You'll receive a notification as soon as your migrated dashboard is ready.
- **Migrate (limited):** You can migrate this dashboard, but some functionality will be different or not available. You can review the limitations before you migrate the dashboard.

If no migration status is shown, the dashboard is ready for you to use in the new dashboard builder.

## Migrating legacy dashboards

Dashboards are migrated from the dashboard library. The Views column in the library can help you decide which legacy dashboards to migrate.

Important: Explore will attempt to replicate the legacy dashboard's layout. However, Zendesk cannot guarantee that the new version will be a replica.

**To migrate a dashboard**

1. In Explore, click the **Dashboards library** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) on the left sidebar.
2. From the list of dashboards, choose a dashboard and click **Migrate**.
3. If there are no issues with the dashboard, the migration will be completed.

   If there are blocking issues or some parts of the dashboard won’t be migrated or will work differently, a page will be displayed showing the issues.
4. The migration creates a copy of the original dashboard. Once you’re ready, you can delete the original dashboard version.

Watch this short video for an overview of the dashboard migration tools:

Using the Explore dashboard importer tool (3:18)