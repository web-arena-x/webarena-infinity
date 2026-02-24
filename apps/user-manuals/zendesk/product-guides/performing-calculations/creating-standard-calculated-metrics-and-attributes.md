# Creating standard calculated metrics and attributes

Source: https://support.zendesk.com/hc/en-us/articles/4408824243738-Creating-standard-calculated-metrics-and-attributes

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

Explore's built-in metrics and attributes give you great flexibility to create reports.
However, every business is different, and eventually you might want to create reports using metrics and attributes that aren't included in Explore by default. To bridge this gap, you can create standard calculated metrics and standard calculated attributes.

This article contains the following sections:

- [Understanding standard calculated metrics and attributes](#topic_qsx_qhl_bxb)
- [Creating a standard calculated metric](#topic_g2g_hdb_hv)
- [Creating a standard calculated attribute](#topic_hjf_hdb_hv)
- [Next steps](#topic_wxs_h4l_bxb)

Related articles:

- [Writing Explore formulas](https://support.zendesk.com/hc/en-us/articles/4408836190362)
- [Explore functions reference](https://support.zendesk.com/hc/en-us/articles/4408834558746)
- [Using result manipulations and calculations](https://support.zendesk.com/hc/en-us/articles/4408831146266)

## Understanding standard calculated metrics and attributes

Standard calculated metrics and attributes allow you to create new metrics and attributes by combining default metrics and attributes with a variety of formulas, mathematical functions, and more. For example, you could create a standard calculated metric to return a per-hour cost, or create a standard calculated attribute to return a value based on a certain condition.

Standard calculated metrics and attributes are located in the Calculations menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_calculations.png)) in the right sidebar of the Explore report builder.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_calculations_menu_standard_calculated_metric.png)

As with default metrics and attributes, you need to add standard calculated metrics and attributes to your report after creating them (see [Using metrics and attributes in reports](https://support.zendesk.com/hc/en-us/articles/4408846733722)).

Tip: Adding a standard calculated metric or attribute to your report first filters your results before they’re processed. As a result, standard calculated metrics and attributes can help speed up loading times for large datasets.

## Creating a standard calculated metric

Standard calculated metrics allow you to create new, custom metrics to add to your reports.
For example, you could create a standard calculated metric that uses the following formula to return only tickets received through the email channel:

```
IF ([Ticket channel]="Email") THEN [Ticket ID] ENDIF
```

**To create a standard calculated metric**

1. In Explore, [create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) or [open an existing one](https://support.zendesk.com/hc/en-us/articles/4408823403546).
2. Click the **Calculations** menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_calculations.png)) and select **Standard calculated metric**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_standard_calculated_metric_panel.png)
3. In the **Name** field, enter a descriptive name for your new metric.

   Note: Don’t include quotation marks, parentheses, or square brackets in the name. Doing so will cause errors if the metric is referenced in another calculated metric or attribute, or in a [result metric calculation](https://support.zendesk.com/hc/en-us/articles/4408831485466).
4. In the **Formula** field, type or paste the formula that the metric should use. If you type your formula, you can click the auto-complete suggestions as they appear.

   Alternatively, you can click the following fields to select elements to add to your formula:

   - **Fields** > **Select a field**: Shows a list of existing metrics and attributes, including default and custom.
   - **Functions** > **Add**: Shows a list of available functions. For more information about each one, see [Explore functions reference](https://support.zendesk.com/hc/en-us/articles/4408834558746).
5. If your formula uses existing calculated metrics and attributes and you don't want to affect their original calculations, select **Compute separately** .
6. Click **Save**. The metric is saved to the dataset you selected when you started the report.

You can now add this calculated metric to your report. When you click **Add** in the **Metrics** panel, you'll find your metric in the **Calculated metrics** folder.

Note: When you add a calculated metric to your report, the report shows all results by default, including null and zero results. To see only the results that apply to your calculated metric, [add a metric filter](https://support.zendesk.com/hc/en-us/articles/4408821978266) to remove zero and null results.

## Creating a standard calculated attribute

Standard calculated attributes allow you to create new, custom attributes to add to your reports. For example, you could create a standard calculated attribute that groups results based on defined values. See [Creating standard calculated metrics and attributes: Hands-on tutorial](https://support.zendesk.com/hc/en-us/articles/4408839385754).

**To create a standard calculated attribute**

1. In Explore, [create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) or [open an existing one](https://support.zendesk.com/hc/en-us/articles/4408823403546).
2. Click the **Calculations** menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_calculations.png)) and select **Standard calculated attribute**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_standard_calculated_attribute_panel.png)
3. In the **Name** field, enter a descriptive name for your new attribute.

   Note: Don’t include quotation marks in the name. Doing so will cause errors if the attribute is referenced in another calculated metric or attribute.
4. In the **Formula** field, type or paste the formula that the metric should use. If you type your formula, you can click the auto-complete suggestions as they appear.

   Alternatively, you can click the following fields to select elements to add to your formula:

   - **Fields** > **Select a field**: Lists the existing metrics and attributes, including default and custom.
   - **Functions** > **Add**: Lists the available functions. For more information about each one, see [Explore functions reference](https://support.zendesk.com/hc/en-us/articles/4408834558746).
5. Configure the additional settings as needed:
   - **Computed from**: Lists the metrics and attributes you can use in your standard calculated attribute.

     Important: Although you can select standard calculated metrics from the list, doing so can lead to inaccurate results and is not supported. Use only default metrics in your standard calculated attributes.
   - **Sort like time attribute**: If your calculated attribute represents a date, this option places your date values in the correct order.

     Note: This option applies only to single attributes.
     Combining attributes, such as adding a year to the end of a month, results in alphabetical sorting instead of chronological.
6. Click **Save**. The attribute is saved to the dataset you selected when you started the report.

You can now add this calculated attribute to your report. When you click **Add** in the **Columns**, **Rows**, **Explosions**, or **Filters** panels, you'll find your attribute in the **Calculated attributes** folder.

## Next steps

Now that you understand the basics of creating standard calculated metrics and attributes, you're ready to put this knowledge into practice. See [Creating standard calculated metrics and attributes: Hands-on tutorial](https://support.zendesk.com/hc/en-us/articles/4408839385754) to practice creating a calculated attribute by working through an example.