# Using result path calculations

Source: https://support.zendesk.com/hc/en-us/articles/4408845886362-Using-result-path-calculations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

*Result path calculations* are a quick way to change how your results are presented without creating any calculations. The calculation processes each metric result (sometimes known as an element) in turn based on a pattern you specify.

The result path calculation replaces your original metric results with the manipulated results. If you want to include both results, you can create a new standard calculated metric with only your metric as the formula. You can then apply the result path calculation to only one metric, so your report contains both the original and manipulated results.

**To create a new result path calculation**

1. In the result manipulation menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_manipulation.png)), select **Result path calculation**.
2. On the **Result path calculation** panel, all metrics currently added to the **Metrics** panel are displayed.
3. From the **Pattern** drop-down list for the metric you want to recalculate, choose a pattern for the calculation.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_pattern.png)

   Choose from the following patterns:

   - **None**: Does not apply any calculation to each result.
   - **% of total**: Calculates the percentage each result contributes to the total.
   - **Difference**: Calculates the change in number against the chosen reference point.
   - **% of difference**: Calculates the change in percentage against the chosen reference element.
   - **%**: Calculates results as the percentage of the chosen reference element. By default, the percentage is a whole number. You can change this on the **Chart configuration** > **Display format** panel.
   - **Running total**: Calculates the cumulative results, by default on SUM. The aggregator can be switched to AVG, MIN, or MAX.
   - **Replace empty cells**: Specifies the result to carry forwards to the next non-empty cell.
   - **Rank**: Displays the results ranked in concurrent (1,2,2,4), dense (1,2,2,3), or single order (1,2,3,4). Concurrent and dense both group values with the same result, but concurrent will skip the next ranking number. Single will assign each value a unique ranking number.
   - **Percentile**: Calculates the percentile of the results across the series. This pattern is useful for tracking changes in results over time.
4. After you select a pattern, you can select your **Path**. Your path indicates how the calculation is computed.
5. Depending on which pattern you chose, you may need to select additional settings:
   - **Reference**: The result from which a calculation is computed.
   - **Ranking method**: Used only with the **Rank** pattern. Lets you choose the distribution of the ranking.
   - **Aggregation**: Used only with the **Running total** pattern. Defines how the data queried by a metric is calculated. For more information, see [Choosing metric aggregators](https://support.zendesk.com/hc/en-us/articles/4408846897178).
   - **Starting point**: Used only with the **Running total** pattern. Defines whether the running total is calculated based on the first element or the last element in the report.

     ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_result_path_calculation_starting_point.png)
6. When you're finished creating your calculation, click **Apply**.

The recalculated results are shown in your report.