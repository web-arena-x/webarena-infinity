# Adding totals to results

Source: https://support.zendesk.com/hc/en-us/articles/4408846476698-Adding-totals-to-results

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

In Explore, you can find the total of your overall results or subtotals for individual categories in a report. Each total can be calculated with a unique aggregator (see [Changing metric aggregators](https://support.zendesk.com/hc/en-us/articles/4408846897178-Changing-metric-aggregators)).

You can configure totals in two different ways in Explore:

- **Simple totals** let you add a row of grand totals and a row of subtotals, using any of Explore's aggregators. Grand totals will calculate the overall total of your results, using your chosen aggregator. Subtotals can be used if you have more than one attribute added to your report.
- **Advanced totals**, usable only with the Table visualization option, let you to add multiple rows of totals, each with a different aggregator. Grand totals will be applied only to the first attribute on the selected location. Subtotals are available only for the first attribute on rows. If you have attributes on columns, subtotals will not be an available action.

Note: [Applying a metric filter](https://support.zendesk.com/hc/en-us/articles/4408821978266) to remove a value from being displayed in the report doesn't exclude those values from the calculated total.

**To add simple totals to your report**

1. In the report builder, click the result manipulation icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_manipulation.png)).
2. Select the **Totals** option.
3. Underneath **Grand totals on**, check the location of the attributes for which you want to apply grand totals. You can select **Columns**, **Rows**, or both.
4. Select an aggregator.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_simple_totals_select_aggregator.png)
5. Underneath **Subtotals on**, check the location of the attributes where you would like to apply subtotals. You can select **Columns**, **Rows**, or both.
6. Select an aggregator.
7. When you are finished, click **Apply**.

Below is an example of a report displaying the tickets solved each month and the total number of tickets solved for the previous 12 months..

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_simple_totals_final_report.png)

**To add advanced totals to your report**

1. In the report builder, click the result manipulation icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_manipulation.png)).
2. Select the **Totals** option.
3. Click the **Advanced** tab (this is only visible if your visualization type is **Table**).
4. Click **+ Add a new total**.
5. Underneath **Attribute** select the location of the attribute you want to apply your total to. You can calculate grand totals on either **Columns** or **Rows**, and subtotals on an individual attribute.

   Note: You can only calculate subtotals on the first attribute listed in **Rows**. If you have an attribute in **Columns** instead, subtotals will not be an available option.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_advanced_totals_select%20attribute.png)
6. Select an aggregator underneath **Aggregators**.
7. Click **+ Add a new total** to add any additional totals. If you want to delete a total, you can click the trash can icon next to the total.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_advanced_totals_multiple_totals.png)
8. Click **Apply**.

Below is an example of a report calculating the total average number of tickets and total summation number of tickets by month

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_advanced_totals_final_report.png)