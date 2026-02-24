# Using metrics and attributes in reports

Source: https://support.zendesk.com/hc/en-us/articles/4408846733722-Using-metrics-and-attributes-in-reports

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

When you [create a report](https://support.zendesk.com/hc/en-us/articles/4408821589530), you must add at least one metric and optional attributes. Metrics are quantifiable values, such as the number of tickets, replies to tickets, and agent or customer wait times. Attributes are non-quantifiable values, such as ticket ID, ticket tags, and assignee names.

There are many metrics and attributes that you can use for each Zendesk product. To learn what's available, see [Understanding Explore datasets](https://support.zendesk.com/hc/en-us/articles/4408839218842-Metric-and-attribute-reference).

This article contains the following topics:

- [Using metrics in reports](#topic_ghz_hmb_y5)
- [Using attributes in reports](#topic_mwx_hmb_y5)

## Using metrics in reports

You can [add metrics](https://support.zendesk.com/hc/en-us/articles/4408821589530#topic_zt4_3xc_zsb) in different sizes, colors, on a dual axis, to a trend line, or include them in datatips (also known as tooltips).

You can calculate your metric results in different ways, such as summation (SUM) or count (COUNT). The aggregator in front of the metric name tells you which calculation is currently applied. Explore automatically applies a default aggregator, but you can select a new one.
See [Changing metric aggregators](https://support.zendesk.com/hc/en-us/articles/4408846897178).

This section contains the following topics:

- [Measuring results by color and size](#topic_esg_kmb_y5)
- [Adding a metric as a secondary axis](#topic_n3f_kmb_y5)
- [Displaying a metric's results as a trendline](#topic_tg5_hw3_y5)
- [Restricting metric results to datatips](#topic_wd2_kmb_y5)
- [Using comparison lines to highlight metric results](#topic_ehf_j4r_nv)
- [Removing metric settings](#topic_z2g_vkl_23c)

### Measuring results by color and size

You can measure a metric's results in a color gradient or with different display sizes.

In the image below, **Agent replies** has been added as a color-encoded metric. At the upper-right of the chart, you can see how results are distributed in the color gradient.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_color_encoded_metric.png)

In the image below, **Agent replies** has been added as a size-encoded metric. At the upper-right of the chart you can see how results are distributed in the different sizes.
Size-encoding options cannot be edited.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_size_encoded_metric.png)

**To add a color or size-encoded metric**

1. In the **Metrics** panel, click the **Color-encoding** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_add_color_icon.png)) or the **Size-encoding** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_add_size_icon.png)).
2. Select the metric you want to color-encode, or size-encode..

**To change the color style**

1. Click the chart configuration icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)).
2. Click **Colors**.
3. From the **Color encoding** drop-down list, choose a new color style.

### Adding a metric as a secondary axis

On some chart types, you can add a metric as a *dual axis*, or secondary axis. This is an easy way to compare metrics with different scales and separate results that would be difficult to analyze.

In the image, the **Unresolved unreplied tickets** metric uses a much smaller scale than the **Agent replies** and **Tickets** metrics. As the image below shows, the results from this metric are difficult to view.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dual_axis_metric_normal.png)

To make data easier to view, you can add **Unresolved unreplied tickets** as a dual axis. This displays the metric by its own scale and visualization as displayed below:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_on_dual_axis_metric.png)

**To add a dual axis metric**

1. In the **Metrics** panel, click the dual axis icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dual_axis_icon.png)).
2. Select the metric you want to use for the dual axis.

You can edit the dual axis in **Chart configuration** > **Secondary axes**.

### Displaying a metric's result as a trend line

Similar to a dual axis, you can add a metric as a trend line to separate results. You can also display the trend for each metric by adding trend lines in **Chart configuration**> **Trend line**.

Note: If one of your metrics is added as a trend line and you add a trend line in **Chart configuration**, an additional line will not appear for that metric.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_trendline_metric.png)

**To add a metric as a trend line**

1. In the **Metrics** panel, click the trend line icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trendline_icon.png)).
2. Select the metric you want to add as a trend line.

You can edit trend line options, including hiding and displaying values in **Chart configuration**>**Trend line**.

### Restricting metric results to datatips (or tooltips)

If you do not want a particular metric to display on the report, but still want users to be able to see the data, you can add the metric as a datatip. Any results from the metric added as a datatip will appear when a user hovers over a data point. For more information on adding and customizing datatips, see [Working with datatips](https://support.zendesk.com/hc/en-us/articles/4408838176538).

In the image below, only the replies metric is visible on the report, but when a viewer hovers over a data point, they can see the corresponding number of tickets results.

![Datatips](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_datatip_metric.png)

**To add a metric as a datatip**

1. In the **Metrics** panel, click the datatips icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_datatip_icon.png)).
2. Select the metric you want to display as a datatip.

### Using comparison lines to highlight metric results

Comparison lines can highlight multiple metric results for one value. When you add a comparison line, you can hover over any data point to view all results for the same X axis location. Comparison lines are useful when your attribute has several values, but your screen size cannot display each label.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_comparison_line_metric.png)

**To add comparison lines**:

1. In the chart configuration menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)), select **Datatips**.
2. Select **Comparison line** from the **Mode** drop-down list.

### Removing metric settings

You can remove any of the metric settings described in this article.

**To remove metric settings**:

1. Click the metric for which you want to remove the settings.
2. In the metric's settings, click **None**.

## Using attributes in reports

Within a report, you can [add attributes](https://support.zendesk.com/hc/en-us/articles/4408821589530#topic_m34_jxc_zsb) to the **Columns**, **Rows**, **Filters**, and **Explosions** panels.

This section contains the following topics:

- [Adding attributes to columns](#topic_uws_xnb_y5)
- [Adding attributes to rows](#topic_egq_xnb_y5)
- [Adding attributes to explosions](#topic_b2v_11k_y5)
- [Adding attributes as filters](#topic_s2p_xnb_y5)

### Adding attributes to columns

Columns slice your results by the attribute's values in one chart. To add an attribute to the **Columns** panel, click **Add**, then select an attribute.

Note: You can switch attributes in the **Columns** and **Rows** panels by clicking pivot table (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Pivot_Table_Icon.png)) in the **Columns** panel. The pivot table feature saves you time by automatically moving your attributes, so you don't have to drag and drop.

Below is an example with the attribute **Ticket created - Month** added as a column.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_columns_attribute.png)

### Adding attributes to rows

If you add an attribute to the **Rows** panel, you can see individual charts for each of your attribute's values without selecting or excluding results. You can view a value using the *Row Selector* to the left your chart.

Below is an example of a report with the **Ticket status** attribute added as a row.
The value **Closed** is selected in the row selector.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_Rows_attribute.png)

### Adding attributes to explosions

Similar to rows, attributes added to the **Explosions** panel break your report into individual charts based on the attribute's values. Unlike rows, explosions show all charts side-by-side. This provides a simple way to compare results, but if your attribute has several values, you should consider selecting values to display or using rows.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_explosions_attributes.png)

You can display a maximum number of 30 charts using an Explosion. If the attribute you add to the **Explosions** panel returns more than 30 values, apply a filter to restrict the number of values returned.

### Adding attributes as filters

Attributes added as filters enable you to select or exclude values to include in the report results. Results are filtered to the values you select, but the attribute names do not appear in your report. Instead, all your applied filters are listed underneath your report. This list includes any result manipulations you create.

For example, the results below are filtered by the **Open** ticket status, but the attribute name is not displayed on the report.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_filter_attributes.png)

To limit performance issues, Explore currently returns only the first 50,000 rows from a report. To successfully run the report, consider using a filter to limit the results returned.