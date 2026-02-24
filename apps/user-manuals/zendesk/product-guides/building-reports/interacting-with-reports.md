# Interacting with reports

Source: https://support.zendesk.com/hc/en-us/articles/4408829009818-Interacting-with-reports

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

After you create a report, Explore includes options that help you dig deeper into your results to find exactly the information you need. You can use these interaction options in the report builder, and if you've added the report to a dashboard then viewers can also use the options. The main options are:

- **Drill in**: Enables the report viewer to break a data point down by additional attributes.
- **Decompose**: Enables the report viewer to slice the report results with another attribute they choose.

You perform these interactions by selecting a data point on a table or chart or by clicking and dragging across multiple data points. After you click, a drop-down list appears displaying the available interaction options.

![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/Explore_drill_in_decompose_dropdown.png)

Note: Interaction options are disabled when you [share dashboards externally](https://support.zendesk.com/hc/en-us/articles/4408826905626).

This article contains the following topics:

- [Drill in](#topic_kdx_msp_kqb)
- [Decompose](#topic_uw1_4mz_nv)
- [Copy (tables only)](#topic_xgn_fkp_3kb)
- [Reverting interaction options](#topic_klf_jmh_nkb)

## Drill in

The drill in interaction breaks down the data points by additional attributes. For more on drill in, see [Using drill in to refine your reports](https://support.zendesk.com/hc/en-us/articles/4408826499482).

## Decompose

The decompose interaction slices the data points you selected by additional attributes.

**To decompose a report**

1. In your report, select one or more data points and then click **Decompose**.
2. On the next page, choose one or more attributes to slice the selected data points.

   By default, decompose allows viewers to select any attribute in your dataset. You can restrict the available attributes or set a **Decompose path** in **Chart configuration** > **Decompose type**.
3. If you want the new attributes to be placed in the **Columns** panel, click **On columns** or if you want them in the **Rows** panel, click **On rows**.
4. If you want to keep your original attribute in the report, select **Keep original element on the axis**.
5. When you are finished, click **Ok**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_interact_1.png)

The selected data points will be sliced by the new attributes you have selected. If you have chosen not to keep the original elements those attributes are added to the **Filters** panel.

**Example 1**

You’re measuring the number of Tickets by **Ticket solved - Year**, and you decompose the 2018 year data point by **Ticket solved - Month** on columns. Your results would resemble the image below.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_interact_2.png)

**Example 2**

The example below uses decompose to examine the number of tickets created by channel each quarter. You can replicate these steps using any metrics and attributes.![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_interact_4.gif)

**To examine quarterly results**

1. Click the bar of the quarter you want to view.
2. Click **Decompose**.
3. Choose the **Ticket channel** attribute.
4. Click **On columns**.
5. Click **Ok**.

   The bar for Q1 is decomposed to show the ticket channels used in the Q1 period.

**To disable decompose**

1. Click the chart configuration icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)).
2. In the chart configuration menu, select **Interactions**.![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/Explore_disable_decompose.png)
3. Clear the **Allow decompose** option.
4. Save the report.

## Copy (tables only)

In tables only, you can select one or more data points and then click **Copy** to add the data to your computer clipboard. You can only copy the result data points, not the attribute names.

## Reverting interaction options

After you've used a drill in or decompose operation to dig into your data, you can use this procedure to revert to your initial report results.

**To revert an interaction option**

- In the report builder, click the undo button.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_undo_command.png)

The report results revert to their previous state. Depending on how many report interactions you performed, you might need to click undo more than once.