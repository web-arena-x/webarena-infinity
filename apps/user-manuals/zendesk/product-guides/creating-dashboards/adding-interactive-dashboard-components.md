# Adding interactive dashboard components

Source: https://support.zendesk.com/hc/en-us/articles/4408828331290-Adding-interactive-dashboard-components

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

Important: This article covers the new Explore dashboard builder, released in
November 2024. The legacy dashboard builder will remain available until December 31, 2026
(previously February 28, 2026), after which legacy dashboards will become view-only. If
you’re using the legacy dashboard builder and need help, see [About the legacy Explore dashboard builder](https://support.zendesk.com/hc/en-us/articles/8210448879002).

You can add interactive components to a dashboard so your viewers can interact with and
customize their results. Only editors can add interactive components, but anyone with
permission to view a dashboard can use them.

For help using interactive components, see [Interacting with dashboards](../viewing-and-using-dashboards/interacting-with-dashboards.md).

This article contains the following sections:

- [Filtering results](#topic_efy_2rg_2v)
- [Selecting new attributes](#topic_y1x_2rg_2v)
- [Excluding reports from dashboard filters](#topic_vhc_sx2_nzb)

Related articles:

- [Best practices for using Explore dashboard filters](https://support.zendesk.com/hc/en-us/articles/4408846768026)

## Filtering results

Viewers can use interactive filter components to restrict results to specific attribute
values, date and number ranges, or the highest and lowest results. You can configure filters
to work across multiple tabs, and prevent filters from applying to individual reports.

This section contains the following topics:

- [Filtering dashboards by time or attributes](#topic_t3t_4z2_nzb)

### Filtering dashboards by time or attributes

The following are the available types of filters:

- [Time filter](#topic_qht_srg_2v)
- [Data filter](#topic_jj5_srg_2v)

Note: Dashboard-level filters overwrite any filters configured in
individual reports. If necessary, you can [exclude a report from dashboard filters](#topic_vhc_sx2_nzb) so its filters aren't
overwritten.

#### Adding a time filter component

A *time filter* enables users to edit the displayed period for a dashboard.

**To add a time filter**

1. In the **Dashboard** menu, click **+** > **Time filter**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dash_filter_1.png)
2. In the **Time filters** panel, select a date attribute to use in the filter.

The time filter component is added and will resemble the image below.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dash_filter_2.png)

#### Using the time filter

Now that you've added a time filter, dashboard viewers can use it to configure the
period displayed on the dashboard reports.

**To change the displayed period**

1. In your dashboard, click your time filter.
2. From the dropdown list, select the period for which you want to display
   results, for example, **Last 12 months**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dash_filter_3.png)

Your dashboard reports refresh to display only data for the period you
selected.

Note: Time filters default to the Last 30 days setting and will revert to this setting each time the
dashboard is reloaded.

#### Adding a data (attribute) filter

A *data filter* enables viewers to filter results by an attribute's values.
Viewers can divide data by an additional attribute without the results appearing on each
report.

**To add a data filter**

1. In the **Dashboard** menu, click **+** > **Data filter**.
2. On the **Choose data filter dataset** panel, select the attribute by which you
   want to filter.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dash_filter_4.png)

   You can either browse the available
   attributes in the list or refer to [Understanding Explore datasets](https://support.zendesk.com/hc/en-us/articles/4408839218842-Metric-and-attribute-reference) for a
   complete list of available values for your dataset.

   Tip: If you choose a date attribute, think about
   how you want your viewers to be able to filter the dashboard. For example, a
   common filter might be the date the ticket was created, so you'd choose the
   **Ticket created - Date** attribute. The attribute you select must be part
   of the dataset used to generate the report you’ve added to the dashboard.

Your new filter is displayed. In this example, you've added a data filter to only show
results for tickets that contain one or more selected tags.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dash_filter_5.png)

## Selecting new attributes

When you select these interactive widgets, your viewers can edit the initial attributes to
view other possible outcomes.

The following interactive widgets that enable your viewers to edit existing metrics or
attributes:

- [Change attribute](#topic_rcq_jvg_2v)

### Selecting a different attribute

The change attribute interactive component lets viewers select a new attribute for a
report from a list you configure.

**To add a change attribute interactive component**

1. In the **Dashboard** menu, click **+** > **Change attribute**.
2. In the **Add change attribute** panel, select the dataset containing the
   attribute you want to become a change attribute.
3. Select the attribute that will become a change attribute.
4. After you select an attribute, you can edit the display format and restrict the list
   of available attributes.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/display_as.png)
5. When you are finished, click **Add**.

   Your change attribute component is
   displayed and will resemble the image below.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dash_filter_7.png)

## Excluding reports from dashboard filters

You can prevent dashboard filters from applying to individual reports within the dashboard.
This is helpful if you don't want dashboard-level filters to overwrite the filters
configured in the report itself.

**To turn off dashboard filters for a report**

1. Select a report in the dashboard. The filter options menu displays.
2. From the Exclude from filters dropdown list, select the filters you want to exclude from
   your report.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dash_filter_6.png)

Your dashboard updates with the new filter configuration.