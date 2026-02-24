# Best practices for using dashboard filters

Source: https://support.zendesk.com/hc/en-us/articles/4408846768026-Best-practices-for-using-dashboard-filters

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

The information in this article covers the new Explore dashboard builder, released in November 2024. The legacy dashboard builder will remain available until Q4 2025. If you’re using the legacy dashboard builder and need help, see [About the legacy Explore dashboard builder](https://support.zendesk.com/hc/en-us/articles/8210448879002).

This article outlines some of the best practices you can use to help you get the most from dashboard filters. To learn more about filters and how to add them to your dashboard, see [Adding interactive dashboard components](https://support.zendesk.com/hc/en-us/articles/4408828331290).

This article contains the following sections:

- [Use reports from fewer datasets](#h_8102a27a-579b-40c0-adc5-cf492aa879a4)
- [Select time filters you need](#h_a2bcbc01-a036-416b-8108-3b66318bcd83)
- [Link filters](#h_9367d2bd-ec7a-4a30-aea0-42a5def3215c)
- [Exclude filters from reports](#h_9b64cfc6-4559-4ca9-a15d-f740441bc58e)
- [Use time filters](#h_01GX437S69BT27CH5K2K2FJC7R)
- [Save default filter values](#h_bd2ba570-0721-4a5f-8bbb-e631c13caacf)
- [Use filters across multiple tabs](#h_01GFK4KRCCA0F0TESFZ2K27WK9)

## Use reports from fewer datasets

To simplify the dashboard filtering process, don't use reports from too many datasets. Typically, one or two datasets will provide enough data. For example, reports in the most common prebuilt dashboard tabs are based on one dataset.

Sometimes, you'll need to add reports from multiple datasets to a dashboard. In such situations, review the reports in the tab to ensure they can't be created from the same datasets.

For more information about the metrics and attributes contained in each dataset, see [Understanding Explore datasets](https://support.zendesk.com/hc/en-us/articles/4408839218842).

## Select the time filter attributes you need

Each dataset has multiple time attributes. All these attributes are listed in the time filter menu and can be used to filter the dashboard tab. If reports added to the dashboard are from multiple datasets, then time attributes from multiple datasets will be available in the filter menu.

The goal is to select only those time attributes that you actually want to use for filtering the reports in the tab. Typically, you will need one to three time attributes per tab. For example, the Tickets tab of the default Support dashboard uses two attributes for time filtering, **Ticket created** and **Ticket solved**.

![Explore_dash_filter_227.png](https://support.zendesk.com/hc/article_attachments/8364358033690)

## Link filters

If you use more than one dataset in the same dashboard, you must link filter attributes to the equivalent attributes from other datasets.

For example, the **Satisfaction** tab of the default **Support** dashboard uses reports from two datasets: **Tickets** and **Updates history**. The filters are based on the attributes from the Tickets dataset. To ensure that these filters are applied to all reports, they are linked with attributes from the **Updates history** dataset.

## Exclude filters from reports

There are three main reasons for excluding dashboard filters from individual reports:

- You are using more than one attribute in the time filter
- You don't want some of the reports to be affected by a specific filter
- A dashboard filter might override results returned from a filter on the report itself

Dashboard filters can be disabled for each report via the **Exclude filters** setting. See [Excluding reports from dashboard filters](https://support.zendesk.com/hc/en-us/articles/4408828331290#topic_vhc_sx2_nzb).

![Explore_dash_filter_229.png](https://support.zendesk.com/hc/article_attachments/8364358034330)

## Use time filters

When using time filters on dashboards, it’s better to select a specific time limit rather than the **All history** value. Selecting **All history** means that *no* time frame is selected. In other words, it doesn’t filter any report on the dashboard. Additionally, the **All history** value isn't included in the new Explore dashboard builder.

As a result, if some reports on your dashboard have report-level filters, they will still apply even when the reports are viewed from the dashboard because **All history** doesn’t override them.

## Save default filtered views

Values selected from a dashboard filter are not automatically saved. Therefore, the filter selections are reset each time the dashboard is accessed or reloaded. Because of this, it's important to set the default view for each dashboard tab. This is especially important if a time filter is used in the tab or the dashboard will be scheduled for email delivery or shared externally. For help with bookmarks, see [Bookmarking dashboard states with filtered views](https://support.zendesk.com/hc/en-us/articles/7610243884826).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_create_filtered_view_panel.png)

## Use filters across multiple tabs

With the correct configuration, you can make data filters, time filters, and live data filters work across multiple dashboard tabs. To do so, add the same filter to each tab you want it to affect. See [Filtering results across multiple tabs](https://support.zendesk.com/hc/en-us/articles/4408828331290#topic_dj5_3z2_nzb).