# Creating a top/bottom filter

Source: https://support.zendesk.com/hc/en-us/articles/4408834483994-Creating-a-top-bottom-filter

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

A *top/bottom* filter restricts your report results to a range you choose. For example, you can create reports such as the ticket type with the shortest resolution time or the five agents with the most solved tickets.

The top/bottom result manipulation is a simple way to break down a report into the highest and lowest results. Watch the following video for a demonstration:

How to create a top/bottom filter for reports (1:46)

**To apply this filter**

1. In the report builder, click the result manipulation icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_manipulation.png)).
2. In the **Result Manipulation** panel, click **Top/bottom**.
3. Enter the number of top and bottom results you would like to see.
4. Select the metric to use.
5. Select a strategy.

   If you have attributes on both rows and columns, you can select the appropriate section. If you have multiple attributes and would like to see the top/bottom for each individually, select the **per block** strategy. If you select **Auto**, Explore will automatically choose a location.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_bottom_top.png)
6. Optionally, select a calculation option:
   - **Aggregate values**: Useful if you have attributes in both the **Rows** and **Columns** panels, or a chart displaying results over time. Aggregate values calculate the total of the metric's results, instead of on the first concurrence of the metric.
   - **Aggregate filtered elements**: All results outside your specified top/bottom range will be combined into another category. This is useful when you don't want to view the details of the smaller results, but still want the overall totals and percentage shares to be accurate. Works only with the COUNT, SUM, MIN, and MAX aggregators.
7. Click **Apply**.

The top/bottom result manipulation is added to the **Filters** panel.