# Filtering Explore reports

Source: https://support.zendesk.com/hc/en-us/articles/4408825475354-Filtering-Explore-reports

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

*Filters* are used to control the results returned from an Explore report. Examples of when you might use filters include:

- You want to display results only between certain dates.
- You want to restrict results to a certain group.
- You want to make a large report more manageable by restricting the results.

You can filter a report in two ways:

- **Filtering by an attribute in the Filters panel** lets you filter your report results without adding the attribute itself to your report visualization.
- **Filtering by an attribute in the Columns or Rows panel** lets you filter by selected values for attributes that do appear in your report visualization.

This article contains the following sections:

- [Filtering by an attribute in the Filters panel](#topic_enj_1pk_zwb)
- [Filtering by an attribute in the Columns or Rows panel](#topic_wfq_zpk_zwb)
- [Other filter types](#topic_cyt_wxr_cmb)

## Filtering by an attribute in the Filters panel

When you add an attribute in the **Filters** panel, you can control which report results are returned without adding the attribute itself to your report. Filtering this way is helpful if you want to narrow down your results, but you don't want to clutter the report with an unnecessary column or other data visualization.

Tip: When you create a report in the **Support - Tickets** dataset, the **Ticket created - Date** attribute is automatically added to the **Filters** panel and set to 30 days in the past.

**To filter by an attribute in the Filters panel**

1. In Explore, [create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) or [open an existing one](https://support.zendesk.com/hc/en-us/articles/4408823403546).
2. If necessary, add at least one metric.
3. In the **Filters** panel, click **Add**.
4. From the list of attributes, select the one you want to filter your report by and click **Apply**.
5. Click the attribute you just added. The filter panel opens, showing you a list of all possible values for that attribute.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_filtering_a_report_in_filters_panel.png)
6. Select the values you want to include in the report results. Only the first 100 values are shown in the list. To show more values if necessary, click the arrow next to the **Apply** button or search for a specific value.

   Alternatively, if you're filtering by a date attribute, you can click **Edit date ranges** to configure simple date ranges like **Today** or **Last month**, or more advanced date ranges like **20 days in the past**. With advanced date ranges, you can even add repeating patterns to return specific data based on your business reporting needs.

   | | |
7. Click **Apply**.

The report is filtered by the attribute values you selected in your filter. However, the attribute itself does not appear in your report visualization.

### Example: Filtering tickets by creation date in the Filters panel

In this example, you'll add a count of all tickets and solved tickets, and then filter the results to show only tickets created last week. But the creation date attribute won't appear in your report visualization.

**To create and filter the report**

1. [Create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) using the **Support - Tickets** dataset.
2. In the **Metrics** panel, click **Add**.
3. From the list of metrics, select **Tickets** > **Tickets** and **Tickets** > **Solved tickets**.
4. Click **Apply**. Explore displays the total number of tickets and the total number of solved tickets in your Support instance.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_filtering_11.png)

   Now you'll add a filter to restrict the results to only show tickets created last week.
5. In the **Filters** panel, click **Add**.
6. From the list of filters, select **Time - Ticket created** > **Ticket created - Date**.
7. Click **Apply**. You'll notice that the report results haven't changed.
   This is because you need to configure the filter to display only the values you want.
8. In the **Filters** panel, click the **Ticket created - Date** filter you just added.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_filtering_12.png)
9. Click **Edit date ranges**.
10. Select **Last week** and then click **Apply**.

The report results update to show only tickets and solved tickets created last week. Notice that the **Ticket created - Date** attribute doesn't appear in the report visualization because you added it in the **Filters** panel.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_filtering_14.png)

## Filtering by an attribute in the Columns or Rows panel

When you add an attribute in the **Columns** or **Rows** panel, you can also filter the report results by specific values for that attribute. Filtering this way is helpful if you want to narrow down your results by an attribute that already appears in your report visualization.

**To filter by an attribute in the Columns or Rows panel**

1. In Explore, [create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) or [open an existing one](https://support.zendesk.com/hc/en-us/articles/4408823403546).
2. If necessary, add at least one metric and at least one attribute in either the **Columns** or **Rows** panel.
3. Click the attribute you just added. The filter panel opens, showing you a list of all possible values for that attribute.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_filtering_a_report_in_rows_panel.png)
4. Select the values you want to include in the report results. Only the first 100 values are shown in the list. To show more values if necessary, click the arrow next to the **Apply** button or search for a specific value.

   Alternatively, if you're filtering by a date attribute, you can click **Edit date ranges** to configure simple date ranges like **Today** or **Last month**, or more advanced date ranges like **20 days in the past**. With advanced date ranges, you can even add repeating patterns to return specific data based on your business reporting needs.

   | | |
5. Click **Apply**.

The report is filtered by the attribute values you selected in your filter, and the attribute itself appears in your report visualization.

### Example: Filtering tickets by assignee in the Rows panel

In this example, you'll create a report that displays the assignee name and ticket status for all tickets in your Support instance. You'll then filter this report to show only tickets assigned to a specific team member.

**To create and filter the report**

1. [Create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) using the **Support - Tickets** dataset.
2. In the **Metrics** panel, click **Add**.
3. From the list of metrics, select **Tickets** > **Tickets** and then click **Apply**.
4. In the **Rows** panel, click **Add**.
5. From the list of attributes, select **Assignee** > **Assignee name** and **Tickets** > **Ticket status**.
6. Click **Apply**. Explore displays a table showing each assignee name and the number of tickets they have in each ticket status.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_filtering_15.png)

   Now you'll filter on the **Assignee name** attribute to include only a single team member in the results.
7. In the **Rows** panel, click the **Assignee name** attribute.
8. In the filter panel, select the checkbox next to a team member's name. If the list of names is long, you can type the first few characters to narrow down the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_filtering_16.png)
9. Click **Apply**.

Explore displays only tickets assigned to the team member you selected and the number of tickets in each status. Notice that the **Assignee name** attribute does appear in the report visualization because you added it in the **Rows** panel.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_filtering_17.png)

## Other filter types

Another type of filter, the *metric filter*, enables you to set minimum and maximum values for your results. For more information, see [Selecting the metric result range](https://support.zendesk.com/hc/en-us/articles/4408821978266).

You can also apply filters to your dashboards. When you do this, dashboard viewers can directly control the filters to modify the report. For more information, see the following two articles:

- [Adding interactive dashboard components](https://support.zendesk.com/hc/en-us/articles/4408828331290)
- [Best practices for using dashboard filters](https://support.zendesk.com/hc/en-us/articles/4408846768026)

Note: Any filters set inside of an individual report are overwritten by dashboard-level filters. For more information, see [Should I apply filters at the report or dashboard level?](https://support.zendesk.com/hc/en-us/articles/4408846716570)