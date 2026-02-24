# Using stacked charts to display results

Source: https://support.zendesk.com/hc/en-us/articles/4408833603482-Using-stacked-charts-to-display-results

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

A *stacked* chart breaks down each bar or column in a chart into subsections of the total. For example, if you've created a column chart displaying tickets by the year in which they were solved, you could further break each column down by the ticket satisfaction rating. This can be particularly useful when you want to see a visual representation of which items are having the most influence on a category total.

![Explore column chart demonstrating stacked columns](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_recipe_stacked_2.png)

The following chart types support using stacked values:

- Area
- Bar
- Column

In this article, you'll work through an example of creating a column chart showing ticket satisfaction ratings on a year-by-year basis. You'll then use stacking to make the chart easier to read. Finally, you'll be introduced to some of the options you can use to refine stacked charts.

This article contains the following topics:

- [Creating a stacked chart](#topic_rnh_vnc_jjb)
- [Advanced settings for stacked charts](#topic_i54_c4c_jjb)

## Creating a stacked chart

In this example, you'll create a column chart that shows ticket satisfaction ratings on a year-by-year basis. You'll then use stacking to enhance the readability of the chart.

**To create the stacked chart**

1. In Explore, click the **Queries** ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)) icon.
2. In the Reports library, click **New report**.
3. On the **Select a dataset** page, choose the dataset containing the ticket data you'll need to build the report; in this case **Support - Tickets**, then click **Start report**.
4. Next, in the report builder, add your metrics, the things you want to measure; in this case, the number of tickets created. In the **Metrics** panel, click **Add**.
5. From the list of metrics, choose **Tickets** > **Tickets**, then click **Apply**.

   Explore displays the number of tickets in your Zendesk Support instance.
6. In the **Columns** panel, click **Add**.
7. From the list of attributes, choose **Time - Ticket solved** > **Ticket solved - Year**, then click **Apply**.

   Explore displays the number of tickets broken down by the year in which they were solved. If the chart is not displayed as a column chart, you can change this from the visualization type menu ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_visualization_type.png)).
8. In the **Rows** panel, click **Add**.
9. From the list of attributes, choose **Customer satisfaction** > **Ticket satisfaction rating**, then click **Apply**.

   Explore displays the number of tickets broken down by year. Using the row selector, you can select which ticket satisfaction rating to display though often, you'll click the row selector heading to select all rows. Each rating type displays as a separate column on the chart. Next, group these rating columns together to create a cleaner looking stacked column chart.

   ![Unstacked column chart example](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_stacking_30.png)
10. From the Chart configuration menu ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)) , click **Chart**.
11. From the **Chart** panel, select **Stacked**. Make sure the other options on this panel are not selected.

    Note: To find out more about the other stacking options, see [Advanced settings for stacked charts](#topic_i54_c4c_jjb) in this article.
12. In the row selector, select the ratings you want to appear in the stacked chart or click the heading, in this case **Ticket satisfaction rating**, to select all the ratings.

    ![Explore row selector](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_row_selecter.png)

Explore redisplays the column chart with the satisfaction ratings stacked together for the selected rows.

![Example stacked column chart](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_stacking_31.png)

Tip: If you want the report to open with all rows selected, in the Chart configuration menu ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)) click **Row selector**, then from the **Selected position** dropdown list, choose **Select all**.

## Advanced settings for stacked charts

Use the chart panel in the Chart configuration menu ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)) to access stacking options for area, column, and bar charts.

![Explore chart stacking menu](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_stacking_32.png)

This menu contains the following options for stacking your chart:

- **Stacked:** Turns stacking on or off. Hover over one of the bars in the stack to see the total number for that bar.
- **Stacked: Aggregate values:** Starting from the first bar, the values of subsequent bars are cumulatively added together. The final bar displays the total of all bars.
- **Stacked: Percentage:** Displays the percentage of the total for each stacked bar. In addition to selecting this option, you must configure the **Show value** option on the **Displayed values** panel of the Chart configuration menu to **Show**.
- **Stacked: Show total values:** Displays the total from each bar at the top of the stack.