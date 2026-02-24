# Chart types for comparing metrics

Source: https://support.zendesk.com/hc/en-us/articles/4408846877082-Chart-types-for-comparing-metrics

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

While you can compare metrics with all of the chart types, sometimes you might want to view results for only one metric or compare multiple metrics without adding attributes. With the exception of the waterfall chart, these charts work best when comparing one or two metrics.
For information on comparing multiple metrics, see [Using metrics as axes.](https://support.zendesk.com/hc/en-us/articles/4408821163290)

The following charts are the best-suited for comparing metrics:

- [KPI](#topic_rn4_bdf_z5)
- [Bullet and gauge](#topic_unn_bdf_z5)
- [Waterfall](#topic_vdl_bdf_z5)

## KPI

The KPI (or *Key Performance Indicator*) chart displays your metric's results as a headline number to place on your dashboard. You can use the KPI chart to display a single metric or add a second metric as a reference number. If your headline number is higher than the reference number, a green triangle will appear. If it is lower, a red triangle will appear.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_KPI.png)

In the image above, the red triangle indicates that **Solved tickets** is lower than **Tickets**. If you want to display the percentage or difference, select **Show variation** in **Chart configuration** > **Chart**.

If you place an attribute on the frame, the headline number will reflect the results of the value last in the attribute order. If you enable **Show chart** in **Chart configuration** > **Chart**, a chart will appear below your headline number. If you are using a reference number, the chart will not be displayed.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_KPI_attribute.png)

In the image above, 2016 is the latest year, so it's value is displayed as the headline number.

When you select a KPI chart, you can change the following options in the chart configuration menu:

- In **Colors**, you can edit the variation, background, and min/max colors.
- In **Chart**, you can add a small chart to your KPI. You can add a column, line, or area chart in **Show chart**. This option is only available if you have added an attribute.
- If you add an attribute, you can change the results your headline number represents.
 Your headline number can be either the last value of the attribute, the total, the average, or the number of values in the attribute. In **Chart**, you can select a new value from the **Value type** drop-down list.

## Bullet and gauge

The bullet and gauge charts are used to compare a metric to either a target or an overall total. The bullet chart provides a compact way of displaying *actual* and *target* results for multiple values of an attribute. The first metric added will represent the actual results, and the second will represent the target results. In a bullet chart, the vertical line represents the target results, and the black bar represents the actual results.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_bullet_gauge.png)

The gauge chart is a simple way to view how your results compare to a target. If you're using more than one metric, your first result will be the value and your second metric will be the target. The gauge needle will point to the area near the value's results, and the result number will be listed underneath the chart. The target results will appear as a black dot.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_gauge.png)

When you select a bullet or gauge chart, you can customize the following options in the chart configuration menu.

- In **Colors**, you can edit the range colors. Colors will automatically appear in a traffic light series.

- In **Chart**, you can edit whether your results are measured against a percentage of the maximum number or the target number. You can also configure the minimum and maximum values and percentages for your report.
- For a gauge chart, you can select the range color to be a color series or only colored according to the needle position. You can edit this setting in **Chart** >
 **Range color indicated by the needle**.

## Waterfall

A waterfall chart can help you understand the components of a result or the cumulative effect of a series. You can use waterfall charts to focus on how results change from point A to point B. A waterfall chart can be set up in two ways.

First, you can use a series of metrics with positive and negative factors to build a picture of the overall result. For example, in the image below each metric is a factor in calculating the total number of tickets.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_waterfall.png)

If you do not have a series of positive and negative metrics, you can break one metric down by elements of an attribute, such as time periods. The waterfall chart is best for comparing time period on time period results rather than trends over time. For more information, see [Comparing trends over time](https://support.zendesk.com/hc/en-us/articles/4408838807194).

The waterfall chart below compares month-on-month results for the **Solved tickets** metric. This report incorporates a result path calculation to display difference.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_waterfall_different.png)

When you select a waterfall chart, you can edit the following options in the chart configuration menu:

- In **Chart**, you can choose to have connecting bars between your columns by checking the **Connecting bars** box. If you deselect the option, the dashed lines between your bars will be removed.
- In **X axis** and **Y axis** you can edit axes title, style, and visibility.