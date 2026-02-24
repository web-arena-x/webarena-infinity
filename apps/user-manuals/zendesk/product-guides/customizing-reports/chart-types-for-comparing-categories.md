# Chart types for comparing categories

Source: https://support.zendesk.com/hc/en-us/articles/4408839361946-Chart-types-for-comparing-categories

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

Explore includes chart types that help you to understand reports that compare team, or
category results. These chart types are recommended for reporting on metrics in relation to
attributes (categories).

The following are the best chart types for comparing categories:

- [Bar](#topic_shm_yr2_z5)
- [Dot chart](#topic_lb1_cqz_yfb)
- [Treemap](#topic_em4_yr2_z5)
- [Bubble pack](#topic_kp5_cwh_jx)
- [Picto chart](#topic_tsn_wyh_jx)

## Bar chart

A bar chart is similar to a column chart, but displays results from left to right.
Attributes on a bar chart are displayed on the Y axis, while metrics are displayed on the X
axis.

If you are building reports with sorting or benchmarking, viewers can compare results
against each other easily. Bar charts display results on a grid, so you can add trend lines
to track increases or decreases.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_bar_chart.png)

When you select a bar chart, you can change the following options in the chart
configuration (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)) menu:

- In **Colors**, you can edit the grid, background, and individual metric
  colors.
- In **X axis** and **Y axis**, you can edit text style, alignment, label format,
  minimum and maximum values, and visibility.
- In **Trend line**, you can add and edit your trend lines. Adding a trend line in
  the chart configuration menu will show trend lines for each metric. To show a trend line
  for only one metric, see [Adding metrics as a trend line](https://support.zendesk.com/hc/en-us/articles/4408846733722#topic_tg5_hw3_y5).
- In **Chart**, you can create stacked results, so multiple metrics will be combined
  into one column.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_bar_stacked.png)

## Dot chart

A dot chart is similar to a bar chart, but displays results as a dot showing the value of
the metric. Attributes on a dot chart are displayed on the Y axis, while metrics are
displayed on the X axis.

If you are building reports with sorting or benchmarking, viewers can compare results
against each other easily. Dot charts display results on a grid, so you can add trend lines
to track increases or decreases.

![Explore dot chart](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dot_chart.png)

When you select a dot chart, you can change the following options in the chart
configuration (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)) menu:

- In **Colors**, you can edit the grid, background, and individual metric colors.
- In **X axis** and **Y axis**, you can edit text style, alignment, label format,
  minimum and maximum values, and visibility.
- In **Trend line**, you can add and edit your trend lines. Adding a trend line in the
  chart configuration menu will show trend lines for each metric. To show a trend line for
  only one metric, see [Displaying a
  metric's result as a trend
  line](https://support.zendesk.com/hc/en-us/articles/4408846733722#topic_tg5_hw3_y5).

## Treemap

A treemap is a
visualization of hierarchical data such as a user name or ticket channel. The treemap
consists of a series of nested rectangles whose size is proportional to the attribute value.
For instance, in the screenshot below you can see at a glance that Ruth Perkins and Rachel
Cook have the most problems and incidents in the Documentation group. A
treemap is useful for comparing several results at the same time. If you add more than one
attribute to the **Columns** panel, a treemap will show results in a hierarchy. The first
attribute's values will group the second attribute's values, the second will group the
third, and so on. The last attribute's values will be the tiles. You can rearrange the
hierarchy by dragging and dropping to re-order the attribute order in the **Columns**
panel.

The values for each group will appear as a title bar over the tiles. If you hover over a
title bar, the treemap will show you overall results for the attribute.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_treemap_value.png)

If you only want to view results for a select group, you can click the **+** icon on the
title bar to zoom in. You can click the **-** icon to view all results again.

When you select a treemap, you can change the following options in the chart configuration
menu:

- In **Colors**, you can edit your treemap header, text, and background colors.
- In **Chart**, you can change to the classic view by selecting
  **Classic**
  from the **Treemap version** drop-down list.

  Below is an example of the classic
  view:

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_classic_treemap.png)

## Bubble pack

If your attribute contains several different values, you can use a bubble pack to easily
identify the largest and smallest results. Bubbles will vary in size, depending on the
number of results a value contains. Bubble packs work better when there is a limited number
of attributes and metrics on your report frame.

If you add multiple metrics to your report, only the first two will appear. The first
metric will represent the size of the bubbles, and the second metric will be color-encoded
to show the difference in results based on a color gradient. The second metric is
color-encoded by default. Any subsequent metrics you add will not be visible on your report.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_bubble_pack.png)

If you add multiple attributes to your category, more bubbles will appear, so results are
sliced by every possible combination of the added attribute values. The bubbles will only
show the value names for the attribute that was last added. You can hover over a bubble to
see what other values are slicing the result in a datatip. If you do not see a datatip,
ensure that the **Show datatips** box is checked in **Chart configuration** >
**Datatips**.

When you select a bubble pack, you can change the following options in the chart
configuration menu:

- In **Chart**, you can check **Flatten hierarchy** to show all of your results
  together, rather than grouped into circles. You can also arrange your options in either
  ascending, descending, or no order in the **Ordering** drop-down list.
- In **Colors**, you can select a background color and color encoding options. If you
  unchecked **Flatten hierarchy**, you can select the colors for the circles grouping
  your results in **Node color**.

## Picto chart

A picto chart enables you to visualize differences in each value using images or symbols.
Picto charts function best using one metric and one attribute with a small number of values.
In your chart legend, you can see what colors correspond to what values and the approximate
number each image represents. You can change where your legend is located and the legend
style in **Chart configuration** > **Legend**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_picto_chart.png)

When you select a picto chart, you can change the following options in the chart
configuration menu:

- In **Chart**, you can select a new image to represent your results. Images are
  divided into different categories. You can select a new category from the **Icon**
  drop-down list. You can also edit the amount of space between each icon by dragging the
  circle on the **Icon margin** bar. Each image is automatically assigned a value, but
  you can uncheck **Automatic scale**  to enter a new number to represent each image.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/pictochart_2.png)
- In **Colors**, you can change the background color and the image color. If you
  check **Automatic color**, your values will be assigned colors.