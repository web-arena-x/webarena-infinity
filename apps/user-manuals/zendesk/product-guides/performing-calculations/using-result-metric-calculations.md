# Using result metric calculations

Source: https://support.zendesk.com/hc/en-us/articles/4408831485466-Using-result-metric-calculations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

*Result metric calculations* enable you to add a further calculation to a report you
have already taken. For example, if you've created a report to calculate a cost of service for
your tickets (see [Calculating estimated cost of service](https://support.zendesk.com/hc/en-us/articles/4408846694170-Explore-recipe-Calculating-estimated-cost-of-service) for an example),
and you want to add a ten percent margin to this, you could use a result metric calculation.

This article contains the following topics:

- [Creating a result metric calculation](#topic_ehk_b4c_v3b)
- [Example: Calculating the percentage of On-hold tickets](#topic_r3t_b4c_v3b)

## Creating a result metric calculation

**To create a result metric calculation**

1. With an Explore report open, click the result manipulation menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_manipulation.png)), then select **Result metric calculation**.
2. Click **Add a new metric**.
3. On the **Result metric calculation** panel, enter the name of your metric.
4. Enter your formula. For help writing formulas, see [Writing Explore formulas](../writing-formulas/writing-explore-formulas.md).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_formula.png)
5. Select **Clear used metrics** to hide other metrics from the report results and
   only show the result metric calculation. The metrics are still used in the result metric
   calculation, but the results will not appear in your chart.
6. Click **Add**, then close the **Result metric calculation** panel. The new
   result metric calculation is added to the report.
7. Your calculation is automatically added to the open report.
8. In your report, click **Save**.

Note: The result metric calculation is always the last action taken. All other report
calculations are performed first.

## Example: Calculating the percentage of On-hold tickets

In this example, you'll create a report that shows the total number of tickets, and the
number of On-hold tickets for any given year. Then, you'll add a result metric calculation
that displays the percentage of On-hold tickets.

## Creating the report

**To create the report**

1. In Explore, create a new report using the **Support: Tickets** dataset.
2. In the **Metrics** panel, add the following metrics:
   - **COUNT(Tickets)**
   - **COUNT(On-hold tickets)**
3. In the **Filters** panel, add the following attribute:
   - **Ticket created - Year**
4. From the visualization type menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_visualization_type.png)), choose **Table**.

   Explore displays a table showing the
   total number of tickets and the number of On-hold tickets. You can click the **Ticket
   created - Year** filter to filter your results to specific years.

   ![Explore result metric example](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_metric_1.png)
5. Enter a name for the report, then click **Save**.

## Adding the result metric calculation

**To add the result metric calculation**

1. With an Explore report open, click the result manipulation menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_manipulation.png)), then select **Result metric calculation**.
2. Click **Add a new metric**.
3. On the **Result metric calculation** panel, enter the name of your metric,
   **Percentage of On-hold tickets**.
4. Enter the following
   formula:

   ```
   COUNT(On-hold tickets)/COUNT(Tickets)
   ```

   The **Result
   metric calculation** panel will look like the following example:

   ![Result metric calculation page](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_metric_2.png)
5. Click **Add**, then close the **Result metric calculation** panel. The new result
   metric calculation is added to the report.
6. Next, you need to display the new calculation as a percentage. In the chart
   configuration menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)), click **Display format**.
7. On the **Display format** panel, click the drop-down list next to your metric,
   **SUM(Percentage of On-hold tickets)**.
8. From the list of display formats, choose percentage, (**%**). The result metric
   calculation in your report now displays a percentage.

   ![Explore result metric calculation example](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_metric_3.png)
9. In your report, click **Save**.