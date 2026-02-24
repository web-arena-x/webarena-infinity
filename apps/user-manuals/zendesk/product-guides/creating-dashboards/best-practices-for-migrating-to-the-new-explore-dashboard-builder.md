# Best practices for migrating to the new Explore dashboard builder

Source: https://support.zendesk.com/hc/en-us/articles/8002974915482-Best-practices-for-migrating-to-the-new-Explore-dashboard-builder

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

This article covers the new Explore dashboard builder, released in November 2024. The legacy dashboard builder will remain available until December 31, 2026 (previously February 28, 2026), after which legacy dashboards will become view-only. If you’re using the legacy dashboard builder and need help, see [About the legacy Explore dashboard builder](https://support.zendesk.com/hc/en-us/articles/8210448879002).

Explore’s new dashboard builder is designed to streamline the creation, customization, and sharing of dashboards to help you make smarter business decisions.

Over the next year, we’re transitioning from the legacy dashboard builder to the new dashboard builder. This transition period presents you with a great opportunity to optimize your Explore instance. In this article, we've compiled some best practices and resources to guide you through this process.

Important: There are two types of dashboard, and each one requires a different action from you before you can use them in the new dashboard builder:

- **Prebuilt dashboards:** Ready to use dashboards provided with Explore displaying information in a easy-to-read format. These will be automatically migrated, but you'll need to recreate any shares or schedules you previously configured.
- **Custom dashboards:** These are dashboards created or customized by a Zendesk Explore admin or editor. You'll need to migrate these dashboards to the new builder using the importer tool.

See [Migrating legacy Explore dashboards to the new dashboard builder](https://support.zendesk.com/hc/en-us/articles/8096478451098).

This article contains the following topics:

- [Understanding changes in the new dashboard builder](#topic_awd_w14_bdc)
- [Decide which dashboards to migrate](#topic_yks_w14_bdc)
- [Consolidate dashboards using dashboard restrictions](#topic_n2t_w14_bdc)
- [Embrace the new dashboard builder](#topic_v5t_w14_bdc)
- [Make the most of the dashboard migration tools](#topic_sk5_w14_bdc)
- [Additional resources](#topic_jw5_w14_bdc)

## Understanding changes in the new dashboard builder

The Explore documentation primarily reflects the new dashboard builder. If you’re looking for a refresher on the legacy dashboard builder, see [About the Explore legacy dashboard builder](https://support.zendesk.com/hc/en-us/articles/8210448879002).

## Decide which dashboards to migrate

[Explore’s dashboard library](https://support.zendesk.com/hc/en-us/articles/4408831595418) contains the following information to help you decide which dashboards you want to migrate to the new dashboard builder:

- **Migration recommendation:** Start here to see the current migration status of each dashboard. Possible values include:
  - **Start migration:** This will initiate the dashboard’s migration to the new dashboard builder. A copy of the original dashboard is added to the new dashboard builder.
  - **Share:** After the dashboard is migrated, you’ll need to replicate your sharing settings on the new version. When you click **Share**, you can either select each recipient again or import the recipients from the legacy dashboard.
  - **Delete:** When you migrate a dashboard to the new builder, the legacy version is not automatically deleted. Once you've migrated a dashboard, this option will appear for the legacy dashboard.
- **Views:** Displays dashboard views from the past six months. This helps you discover which dashboards are not being used and might not need to be migrated.
- **Schedules:** Displays how many scheduled deliveries of the dashboard have been set up.

Tip: We’ve found that most dashboards are no longer edited after 10 days following their creation. The last updated date provides an indication of whether the dashboard is still up to date, or whether it could be archived.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_newdashboard_migrating.png)

## Consolidate dashboards using dashboard restrictions

You can use [Dashboard Restrictions](../publishing-and-sharing-dashboards/dynamically-adapting-dashboard-data-based-on-viewer.md#:~:text=A%20dashboard%20restriction%20is%20a,maximum%20of%2010%20dashboard%20restrictions.) to consolidate similar dashboards. By dynamically or statically restricting the data a viewer can see, you can create tailored experiences for different audiences without duplicating dashboards.

For example:

- **Dynamic restrictions:** Adapt data based on the logged-in user (for example, showing an agent only their own metrics).
- **Static restrictions:** Limit data based on unchanging attributes (for example, team or location).

Unlike the legacy dashboard builder, you can create a single dashboard that adapts to different audiences, reducing maintenance and complexity.

When planning your migration, consider using dashboard restrictions to combine redundant dashboards. This is especially useful for creating agent-specific productivity dashboards, allowing agents to focus on their own performance while safeguarding sensitive data.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dashboard_restrictions_share.png)

## Embrace the new dashboard builder

Even though both the new and legacy dashboard builders are available, we recommend creating all dashboards with the new builder going forward. This will simplify your transition and let you explore [its enhanced features](https://www.youtube.com/watch?v=rPQScdHxj04).

![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/Explore_newDB_alert.png)

## Make the most of the dashboard migration tools

Our [importer tool](https://support.zendesk.com/hc/en-us/articles/8096478451098) makes it easy to migrate legacy dashboards to the new builder with just a few clicks. In early 2025, we'll introduce a bulk migration tool so you can migrate multiple dashboards at once for even faster, more efficient transfers.

Watch this short video for an overview of the dashboard migration tools:

Using the Explore dashboard importer tool (3:18)

## Additional resources

Need more help with the transition? Check out our [migration guide](https://support.zendesk.com/hc/en-us/articles/8096478451098).