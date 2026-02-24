# Working with aggregation-level functions

Source: https://support.zendesk.com/hc/en-us/articles/4408845551258-Working-with-aggregation-level-functions

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

Aggregation-level functions let you specify which attributes slice the metrics
in your report, giving you more control over your Explore reports.

Normally, when you add a metric and multiple attributes to a report, the metric
is sliced by all of those attributes. You can’t prevent the attributes from slicing the
metrics, nor can you add attributes that slice the metric in the background without
being present in the report. With aggregation-level functions, however, you can specify
exactly which attributes will slice your metrics.

This article contains the following topics:

- [Available aggregation-level
  functions](#topic_v1p_gbq_35b)
- [Using the ATTRIBUTE\_FIX
  function](#topic_nz1_g1y_5pb)
- [Using the ATTRIBUTE\_ADD
  function](#topic_pr3_g1y_5pb)

## Available aggregation-level functions

Explore features the following aggregation-level functions.

| Function | Description | Example |
| --- | --- | --- |
| ATTRIBUTE\_FIX(metric, attribute1, attribute2, ...) | Slices the metric by the attributes specified in the function only.  Attributes added to the report (in the **Columns** or **Rows** panel) will not slice the metric, but any filters applied will be taken into account.  Can be used to keep a report’s results from being affected by specific attributes, which is especially useful for calculating percentages. | `ATTRIBUTE_FIX(MED(First Reply Time (min), [Ticket created - Year], [Ticket created - Month])`  In this example, the median first reply time is returned for each month of the year, regardless of the attributes added to the report. |
| ATTRIBUTE\_ADD(metric, attribute1, attribute2, ...) | Extends the metric aggregation to the attributes specified in the function *in addition to* those added to the report.  Attributes added to the report will slice the metric, and any filters applied will be taken into account.  Can be used to calculate metric averages or medians, pre-aggregated, based on attributes not present in the report. | `ATTRIBUTE_ADD(MED(First Reply Time (min), [Ticket created - Year], [Ticket created - Month])`  In this example, the median first reply time is returned for each month of year, before being aggregated by attributes from the report. |

Note: [Calculated attributes](https://support.zendesk.com/hc/en-us/articles/4408831146266#topic_m4c_hc2_zsb) can’t be used
inside of the ATTRIBUTE\_FIX and ATTRIBUTE\_ADD functions.

## Using the ATTRIBUTE\_FIX function

The first example below shows how the ATTRIBUTE\_FIX function works, and the second
and third show potential use cases.

### Find the total number of tickets per group

This example illustrates how the ATTRIBUTE\_FIX function works. You’ll create a
metric that returns the total number of tickets in each group without being
sliced by the attributes from the report.

**To find the total number of tickets per group**

1. [Create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) in the
   **Support - Tickets** dataset.
2. [Create a standard calculated
   metric](https://support.zendesk.com/hc/en-us/articles/4408824243738) named **Tickets fixed to group** with the following
   formula:

   `ATTRIBUTE_FIX(COUNT(Tickets), [Ticket
   group])`
3. In the **Metrics** panel, add the **Tickets** and the **Tickets fixed
   to group** metrics. Use the **SUM** aggregator for the second
   metric.
4. In the **Rows** panel, add the **Ticket group** attribute. At this
   point, both metrics show the number of tickets in each group.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_aggregation_functions_1.png)
5. In the **Rows** panel, add the **Ticket status** attribute. Now, the
   **Tickets** metric is sliced by ticket status and group, but the
   **Tickets fixed to group** metric ignores the ticket status and is
   sliced only by the ticket group.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_aggregation_functions_2.png)

### Find percentage of tickets from the quarterly volume

In this example, you'll create a report that shows the percentage of tickets
created each month from the total number of tickets created each quarter.

**To find percentage of tickets from the quarterly volume**

1. [Create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) in the
   **Support - Tickets** dataset.
2. [Create a standard calculated
   metric](https://support.zendesk.com/hc/en-us/articles/4408824243738) named **% of quarterly volume** with the following
   formula:

   `COUNT(Tickets) / ATTRIBUTE_FIX(COUNT(Tickets), [Ticket
   created - Year], [Ticket created - Quarter])`
3. Open the calculated metric you just created, click **Options** > **Edit
   display format**, and select **%** in the first field.
4. In the **Metrics** panel, add the **Tickets** and **% of quarterly
   volume** metrics. Use the **SUM** aggregator for the second metric.
5. In the **Rows** panel, add the following attributes:
   - **Ticket created - Year**
   - **Ticket created - Quarter**
   - **Ticket created - Month**

Your report should look like the following:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_aggregation_functions_3.png)

### Compare the yearly and overall full resolution time

In this example, you’ll create a chart that shows the average full resolution
time for each year and compares it to the overall average resolution time.

**To compare the yearly and overall full resolution time**

1. [Create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) in the
   **Support - Tickets** dataset.
2. [Create a standard calculated
   metric](https://support.zendesk.com/hc/en-us/articles/4408824243738) named **Full resolution time (fixed)** with the
   following formula:

   `ATTRIBUTE_FIX(AVG(Full resolution time
   (min)))`
3. In the **Metrics** panel, add **Full resolution time (min)** and
   **Full resolution time (fixed)**.
4. In the **Columns** panel, add **Ticket created - Year**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_yearly_full_resolution_time.png)

## Using the ATTRIBUTE\_ADD function

The first example below shows how the ATTRIBUTE\_ADD function works, and the
subsequent examples give you potential use cases.

### Find the average number of tickets per group

This example illustrates how the ATTRIBUTE\_ADD function works. You’ll create a
metric that returns the average number of tickets per group without adding the
groups attribute to the report.

**To find the average number of tickets per group**

1. [Create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) in the
   **Support - Tickets** dataset.
2. [Create a standard calculated
   metric](https://support.zendesk.com/hc/en-us/articles/4408824243738) named **Tickets per group** with the following
   formula:

   `ATTRIBUTE_ADD(COUNT(Tickets), [Ticket
   group])`
3. In the **Metrics** panel, add the **Tickets** metric.
4. In the **Rows** panel, add the **Ticket group** attribute.
5. Open the **Result manipulation** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_manipulation.png)) menu, select **Totals**, and set
   **Grand totals on** to **Rows** with the **AVG**
   aggregator.
6. In the **Metrics** panel, add the **Tickets per group** calculated
   metric you created. Use the **AVG** aggregator. Both metrics in the
   report show the number of tickets in each group, and the average per
   group is shown at the bottom of the table.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_aggregation_functions_4.png)

   However, in this example, you don’t
   want to display groups on the table, only the average number of tickets
   per group.
7. In the **Rows** panel, remove the **Ticket group** attribute, and
   also remove the grand total result manipulation. The **Tickets**
   metric returns the total number of tickets in your account, but the
   **Tickets fixed to group** returns the average number of tickets
   per group.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_aggregation_functions_5.png)
8. (Optional) In the **Rows** panel, add any additional attributes you
   want to slice the metrics. For example, add the **Ticket status**
   attribute. Now, the **Tickets** metric returns the total number of
   tickets in each status, but the **Tickets per group** returns the
   average number of tickets per group in each status.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_aggregation_functions_6.png)

### Find the average and median tickets per month for each quarter or year

In this example, you'll create a report that shows the average and median tickets
created per month.

**To find the average and median tickets per month for each quarter or
year**

1. [Create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) in the
   **Support - Tickets** dataset.
2. [Create a standard calculated
   metric](https://support.zendesk.com/hc/en-us/articles/4408824243738) named **Tickets per month** with the following formula:

   `ATTRIBUTE_ADD(COUNT(Tickets), [Ticket created - Year],
   [Ticket created - Month])`
3. In the **Metrics** panel, add the **Tickets** and **Tickets per
   month** metrics. Use **AVG** and **MED** aggregators for the
   second metric. (To select multiple aggregators, expand the metric and select
   each aggregator you want to add.)

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_aggregation_functions_7.png)
4. In the **Rows** panel, add the **Ticket created - Year** and **Ticket
   created - Quarter** attributes. As a result, your report shows the
   average and median tickets per month for each quarter:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_aggregation_functions_8.png)
5. (Optional) Remove the **Tickets created - Quarter** attribute to see the
   average and median tickets per month for each year.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_aggregation_functions_9.png)

### Find the highest average resolution time per assignee

In this example, you'll create a KPI that shows the highest average resolution
time across all assignees.

**To find the highest average resolution time per assignee**

1. [Create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) in the
   **Support - Tickets** dataset.
2. [Create a standard calculated
   metric](https://support.zendesk.com/hc/en-us/articles/4408824243738) named **Resolution time per assignee** with the
   following formula:

   `ATTRIBUTE_ADD(AVG(Full resolution time
   (days)), [Assignee ID])`
3. Open the calculated metric you just created, click **Options** >
   **Edit display format**.
4. In the first field, select **Custom**, and then set **Decimal
   place** to **1** and **Suffix** to **days** (with a space
   before the word).
5. In the **Metrics** panel, add the **Resolution time per assignee**
   metric. Use the **MAX** aggregator.
6. In the **Filters** panel, add the **Ticket solved - Date**
   attribute and configure this to show tickets solved in the last 30 days.

Your report shows the highest average resolution time across all assignees over
the past 30 days.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_aggregation_functions_10.png)

### Find the average number of ticket comments per agent

In this example, you'll create a bar chart that shows the average number of
comments submitted by agents per ticket.

**To find the average number of ticket comments per agent**

1. [Create a new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) in the
   **Support - Tickets** dataset.
2. [Create a standard calculated
   metric](https://support.zendesk.com/hc/en-us/articles/4408824243738) named **Comments per ticket** with the following
   formula:

   `ATTRIBUTE_ADD(COUNT(Comments), [Update ticket
   ID])`
3. Open the calculated metric you just created, click **Options** >
   **Edit display format**.
4. In the first field, select **Custom**, and then set **Decimal
   place** to **1**.
5. In the **Metrics** panel, add the **Comments per ticket** metric.
   Use the **AVG** aggregator.
6. In the **Filters** panel, add the following attributes:
   - **Update - Date**: Set this to show updates from the last
     week.
   - **Updater role**: Set this to exclude end users.
7. In the **Visualization type** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_visualization_type.png)) menu, select **Bar**.

The report shows the average number of ticket comments for each agent.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_aggregation_functions_11.png)