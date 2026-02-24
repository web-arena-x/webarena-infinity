# Chart types using metrics as axes

Source: https://support.zendesk.com/hc/en-us/articles/4408821163290-Chart-types-using-metrics-as-axes

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

While other charts have at least one axis defined by an attribute, the charts in this article use only metrics for axes. This can be helpful for comparing multiple metrics without the scale being altered. If you want to display only one metric, see [Comparing metrics](https://support.zendesk.com/hc/en-us/articles/4408846877082).

The following charts use multi-metric axes:

- [Bubble](#topic_bwv_d3f_z5)
- [Radar](#topic_qp5_d3f_z5)

## Bubble

Bubble charts are constructed similar to a scatter plot. Bubble charts use two metrics to make up the X and Y axis. It can represent only two metrics, but multiple attributes can be placed on columns. The attribute's values make up the points on the bubble chart. When you hover over a point, you can see the value's results.

Below is an example of a bubble chart with the metrics **First reply time in minutes** and **Full resolution time in minutes** added. The points are composed of the **Ticket type** and **Ticket group** attribute values.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_bubble.png)

When you select a bubble chart you can change the following customization options in the chart configuration menu:

- In **Chart**, you can edit the size, opacity, and shape of the circles. Your circles can either be an empty circle, diamond, triangle, or cross.
- You can edit trend line, axes, and legend options. By default a legend will only appear if needed.
- In **Colors**, you can edit the grid and row color.

## Radar charts

While bubble charts only compare two metrics, radar charts can shape results around at least three metrics. Each metric on a radar chart has its own scale, and attribute's values will be represented as colored lines. You can change the arrangement of the axes by reordering the metrics on the frame.

In the image below the metrics **Incidents**, **Problems**, and **Solved tickets** are all added as metrics, and the attribute **Ticket group** is added as a column. The different colors on the radar chart represent the different values of **Ticket group**, as shown in the legend.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_radar.png)

If you add attributes to rows, the row selector will enable viewers to click through a series of results. The radar chart does not permit multi-selection on the row selector, but totals and subtotals can be added.

When you select a radar chart, you can edit the following customization options in the chart configuration menu:

- Axis and legend customization options are the same as for bubble charts.
- In **Chart**, you can edit the stroke width and the radar type. Your radar type can be based on metrics or categories. You can also select to show or hide the levels of comparison and vertices.
- In **Colors**, you can change the line color.