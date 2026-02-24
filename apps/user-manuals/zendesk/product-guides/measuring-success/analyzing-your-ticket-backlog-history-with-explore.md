# Analyzing your ticket backlog history with Explore

Source: https://support.zendesk.com/hc/en-us/articles/4408819760666-Analyzing-your-ticket-backlog-history-with-Explore

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

Your ticket backlog is a snapshot of your unsolved tickets at the end of any given date and can be a useful indication of how your support organization is doing. To help you report on your backlog, Zendesk Explore includes the *Support: Backlog history* dataset. This dataset functions a little differently than other Explore datasets. For example, the *Support: Tickets* dataset shows you the current state of the tickets in your Support account, and the *Support: Updates history* dataset can show past events and changes to tickets.

The backlog history dataset is different in that it shows a snapshot of unsolved tickets at the end of any given date. Unlike the other datasets, this information cannot be found anywhere else in your Zendesk account. Explore collects backlog information every time your [data synchronizes](https://support.zendesk.com/hc/en-us/articles/4408820703386) with Explore.

If you're used to other Explore datasets, you'll find that the backlog dataset contains fewer metrics and attributes than other Explore datasets. This is because of the large amount of historical ticket information it stores. However, this does mean that backlog history reports can be a little easier to create.

Use this article to learn more about how to examine your ticket backlog using Explore.

This article contains the following sections:

- [Using the pre-built backlog history reports](#topic_hrm_c2g_4nb)
- [Creating a backlog history report (Explore Professional and Enterprise)](#topic_sbd_kwf_mnb)

## Using the pre-built backlog history reports

To make things easier for you, Explore contains a selection of pre-built backlog history reports.

**To view the pre-built backlog history reports**

1. In Zendesk Support, open the [product tray](https://support.zendesk.com/hc/en-us/articles/4408838272410).
2. From the list of products, click **Analytics**. Explore opens and displays the dashboard library.
3. From the list of dashboards, select the **Zendesk Support** dashboard.
4. In the **Support** dashboard, click the **Backlog** tab.

On the **Backlog** tab, you can view the following reports:

- **Daily historical backlog by status (30 days):** A list of your open ticket backlog over the last 30 days to help you identify trends.
- **Weekly historical backlog by status (12 weeks):** A list of your open ticket backlog over the last 12 weeks to help you identify trends.
- **Weekly historical backlog by selected attribute (top 10/12 weeks):** The number of unsolved tickets at the end of each week for the last 12 weeks. Choose a tab to display results by ticket brand, group, channel, priority, or type.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore-prebuilt-dash-81.png)

For more information about the **Backlog** tab and the other tabs on the Support dashboard, see [Analyzing your Support ticket activity and agent performance](https://support.zendesk.com/hc/en-us/articles/4408835846810).

## Creating a backlog history report (Explore Professional and Enterprise)

If you can't find what you need in the pre-built reports and you're using Explore Professional or Enterprise, you can use the supplied metrics and attributes in the backlog history dataset to build your own reports.

Here's an example report that displays the number of tickets that were unsolved in your account at the end of each month. If you need help building Explore reports, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530).

**To create the report**

1. In Explore, click the reports (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)) icon.
2. In the Reports library, click **New report**.
3. On the **Choose a dataset** page, click **Support** > **Backlog history** > **Support: Backlog history**, then click **Start report**. The report builder opens.
4. In the **Metrics** panel, click **Add**.
5. From the list of metrics, choose **Backlog tickets (unsolved)** >
   **Tickets****,** then click **Apply**.
6. In the **Rows** panel, click **Add**.
7. From the list of attributes, choose **Time - Backlog recorded** > **Backlog recorded - Year** and**Time - Backlog end of period** > **End of month****,** then click **Apply**.

   For this example, the finished report is displayed with the **Table** visualization, but you can use any chart type you want.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_backlog_sample_1.png)

Tip: If you're report takes too long to generate or if you see a timeout error, add a filter to your report to restrict the results. For example, you could add the **Time - Backlog recorded** > **Backlog recorded - Date** attribute to the **Filters** panel in the report builder to restrict your results to specific dates.

For a list of all the metrics and attributes you can use to build backlog reports in Explore, see [Metrics and attributes for Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408827693594).