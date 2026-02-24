# Using the IF THEN ELSE function

Source: https://support.zendesk.com/hc/en-us/articles/4408838560922-Using-the-IF-THEN-ELSE-function

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

The **IF THEN ELSE** function is used in calculations in several different ways, including
filtering, grouping, bucketing, and relabeling results. The IF THEN ELSE function tests a
condition, then returns a value based on the result of that condition.

The IF THEN ELSE expression can be defined in two ways:

- **IF (boolean condition) THEN (true value) ELSE (false value) ENDIF**: The returned
  result will depend on whether the condition passes or fails.
- **IF (boolean condition) THEN (true value) ENDIF**: The returned result will always
  be the true result. If the conditional expression fails, results will be empty.

Additionally, you can nest multiple IF THEN ELSE statements. For more information, see [Nesting multiple IF THEN ELSE functions](#topic_xwz_smg_lx) below.

For information about all of the available functions in Explore, see [Explore functions reference](https://support.zendesk.com/hc/en-us/articles/4408834558746).

This article contains the following topics:

- [Grouping your results](#topic_dnb_tmg_lx)
- [Filtering your results](#topic_fs1_tmg_lx)
- [Nesting multiple IF THEN ELSE
  functions](#topic_xwz_smg_lx)

## Grouping your results

You can use the IF THEN ELSE function to group or bucket your results. This enables you to
relabel, exclude, or segment results to indicate higher or lower values. When you combine
grouping and filtering together, you can highlight results by individual values.

This section shows how to relabel your results based on the conditional expression's
outcome.

### Labeling your grouped results

You can use the IF THEN ELSE function to apply different labels to your results,
depending on the outcome of your conditional expression. For example, you can use IF THEN
ELSE to label whether results are above or below a metric's target. This can be useful for
quickly identifying if your headline number surpassed a goal.

This example uses the IF THEN ELSE function to indicate whether an agent was above or
below the targeted first reply time. You can duplicate this example using any attribute,
metric, and target.

**To label results based on first reply time**

1. In the **Calculations** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_calculations.png)) menu, click **Standard calculated attribute**.
2. Under **Functions**, click **Add**.
3. Give your calculated attribute a name like **First reply time test**.
4. From the list of functions, choose **IF THEN ELSE**.
5. Double-click **\_boolean\_condition** to highlight it.
6. Select a metric from the **Select a field** drop-down list or type in the metric
   name. This example uses **SUM(First reply time (min))**.
7. Type in the greater than symbol (>) and your target amount.
8. For **\_value\_if\_true** enter **"Over"** in double quotes.

   Note: You can also
   substitute in elements or other labels. For example, you could select your Invoice
   Number attribute for your **\_value\_if\_true**, to view the invoice numbers for the
   values with revenue above 100,000.
9. For your **\_value\_if\_false** enter **"Under"** in double quotes.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_IFTE_label.png)
10. In **Computed from**, select the attribute you are using in your report. If you do
    not select an attribute, the calculation will be measured against the total.
11. Click **Save**.
12. Click **Add** in any attribute panel.
13. Choose your attribute from the attributes drop-down list.

## Filtering your results

You can filter your results with IF THEN ELSE by removing the ELSE statement. When you
remove the false parameter, your report will only list the true results. In most cases, it
is easier to add attributes to the **Filters** section of the report, but if you want to
calculate results before processing or perform unique calculations, you can use this method.

This section includes the following examples:

- [Filtering results by metric](#topic_cb2_y1m_lx)
- [Filtering results by
  attribute](#topic_rbd_y1m_lx)

### Filtering results by metric

You can filter your report to only show results that are higher or lower than a specified
metric value. For example, you can limit your results to only display assignee names with
a first reply time over 10 minutes. Follow the same steps as the labeling example above,
but with this formula:

```
IF (SUM(First reply time (min))>10 THEN [Assignee name] ENDIF
```

When you add the attribute to your report, only the assignees with a first reply time
over 10 will be displayed.

### Filtering calculations by attribute

Along with filtering results based on a metric, you can also filter calculations to a
specific attribute value. This formula is useful if you want to perform calculations on
one attribute value and show the original metric results, or perform different
calculations on the other values.

The example below calculates the number of replies per ticket for the support ticket tag,
but you can duplicate this example using any attribute value and calculation.

**To limit calculations to an attribute value**

1. In the **Calculations** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_calculations.png)) menu, click **Standard calculated metric**.
2. Name your calculated metric.
3. Under **Functions**, click **Add**.
4. From the list of functions, choose **IF THEN ELSE**.
5. Double-click **\_boolean\_condition** to highlight it.
6. Select the attribute containing the restricting value from the **Select a field**
   drop-down list or type in the attribute name. This example uses **Ticket tags** .
7. Type in an equal sign (**=**) and the attribute value in "double quotes". This
   example uses =**"support"**.

   This conditional expression will restrict your
   calculation to the entered attribute value.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_filter_attribute.png)
8. In **\_value\_if\_true** enter your calculation.
9. Delete **ELSE** and **value\_if\_false**. You can use **value\_if\_false** to
   provide an alternative formula for results when your expression fails. This example
   does not use a false option, so the ELSE statement is deleted.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_IFTE_function_complete.png)
10. Click **Save**.
11. In the **Metrics** panel, click **Add**, then choose the calculated metric to
    add to your report.

## Nesting multiple IF THEN ELSE functions

If you are using more than one ELSE IF statement in your formula, you can use ELIF to
simplify your expression. For example, if you are trying to show different numbers when your
first reply time is greater than 10, equal to 10, or less than 10, you could use the ELIF
expression to avoid writing multiple ELSE IF statements.

The conditional expression for this example would look like the formula below:

```
IF (SUM(First reply time (min))>10) THEN 1
ELIF (SUM(First reply time (min))=10) THEN 2
ELIF (SUM(First reply time (min))<10) THEN 3
ENDIF
```

Additionally, you can add an ELSE statement after the conditions. The ELSE value will be
used if none of the conditions are true.

Nesting multiple conditional IF THEN ELSE statements can be useful for creating several
different groups or filtering by different conditional expressions.

For another method you can use to evaluate multiple conditional expressions, see [Adding multiple conditional expressions with
SWITCH](adding-multiple-conditional-expressions-with-switch.md).