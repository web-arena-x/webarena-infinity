# Creating standard calculated metrics and attributes: Hands-on tutorial

Source: https://support.zendesk.com/hc/en-us/articles/4408839385754-Creating-standard-calculated-metrics-and-attributes-Hands-on-tutorial

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

In this article, you'll use what you learned in [Creating standard calculated metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4408824243738) to create a standard calculated attribute by working through an example. You can also create a standard calculated metric by following the same process.

Note: Zendesk doesn't provide support for creating or troubleshooting custom metrics or attributes. If you have a problem, ask a question in our [community section](https://support.zendesk.com/hc/en-us/community/topics/6446960561434).

This article contains the following sections:

- [Step 1: Determine what you want to report on](#topic_sql_vrl_bxb)
- [Step 2: Start creating your report](#topic_qyy_wyh_lhb)
- [Step 3: Create a standard calculated attribute](#topic_ybt_qfj_lhb)
- [Step 4: Add your attribute to your report](#topic_ekl_rfj_lhb)
- [Step 5: Edit your attribute's formula](#topic_vyk_5gj_lhb)
- [Next steps](#topic_x4p_byh_nhb)

## Step 1: Determine what you want to report on

In this example, you want to create a report that shows the following information:

- The median first reply time, in minutes, for the Support tickets in your Zendesk account
- Which channel the tickets were created in

After consulting [Metrics and attributes for Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408827693594), you know that you can use the **First reply time (min)** metric and the **Ticket channel** attribute to create your report.

Tip: Zendesk maintains a list of the default metrics and attributes for the datasets in each product. See [Building reports](https://support.zendesk.com/hc/en-us/sections/4405298911258).

## Step 2: Start creating your report

Now that you know what information you're looking for, you can start creating your report.

**To start creating your report**

1. In Explore, click the **Reports** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)).
2. Click the **New report** button.
3. On the **Select a dataset** page, select the **Support - Tickets** dataset and click **Start report**. The report builder opens.
4. In the **Metrics** panel, click **Add** and select **Duration between events - Calendar hours (min)** > **First reply time (min)**.
5. In the **Rows** panel, click **Add** and select **Ticket** >
   **Ticket channel**.

You'll end up with a chart that looks similar to this:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_tutorial_median_reply_by_channel_1.png)

## Step 3: Create a standard calculated attribute

Based on the report you created in [step 2](#topic_qyy_wyh_lhb), you know that some channels have a much faster median first reply time than others. Now you want to know how the first reply time correlates to the ticket volume for each channel. You decide to update your report to answer the following questions:

- How many tickets are being created in each channel?
- For each channel, how many tickets have a fast first reply time, and how many have a slow first reply time?

Because there's no default Explore attribute for "fast first reply time" or "slow first reply time," you'll need to create a standard calculated attribute to define these concepts and reflect them in your report. You want to create a standard calculated attribute with the following logic:

- If a ticket’s first reply time is less than 10 minutes, group it under "Fast response"
- If a ticket’s first reply time is greater than or equal to 10 minutes, group it under "Slow response"

After consulting [Explore functions reference](https://support.zendesk.com/hc/en-us/articles/4408834558746), you determine that the best function to use in your formula is **IF THEN ELSE**. This function allows you to evaluate a condition (the first reply time) and then take an action based on the outcome of that evaluation (labeling the response fast or slow). The following formula is an efficient way to return the results you're looking for:

```
IF VALUE(First reply time (min)) != NULL AND VALUE(First reply time (min)) >= 10 THEN "Slow response"
ELIF VALUE(First reply time (min)) != NULL THEN "Fast response"
ENDIF
```

Tip: The "IF VALUE(First reply time (min)) != NULL" condition means that tickets with no replies won’t be grouped with the fast or slow responses.

Now that you have your formula, it's time to create your standard calculated attribute.

**To create the standard calculated attribute**

1. In your report, click the **Calculations** menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_calculations.png)) and select **Standard calculated attribute**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_tutorial_create_standard_calculated_attribute.png)
2. In the **Name** field, enter a descriptive name such as **Response time fast or slow?** You'll need this name later when you add your calculated attribute to the report.
3. In the **Formula** field, paste in the formula:

   ```
   IF VALUE(First reply time (min)) != NULL AND VALUE(First reply time (min)) >= 10 THEN "Slow response"
   ELIF VALUE(First reply time (min)) != NULL THEN "Fast response"
   ENDIF
   ```
4. In the **Computed from** dropdown, choose **Ticket channel**. This ensures that tickets are counted based on the Ticket channel attribute only.
5. Click **Save** to save the attribute and close the **Standard calculated attribute** panel.

Now that you've created a standard calculated attribute, it acts just like any of the default attributes. It's available to use in any reports within the same dataset, and can be used by anyone who has access to that dataset.

## Step 4: Add your attribute to your report

Next, you'll use your new attribute by adding it to your report. You’ll also add a new metric to count the number of tickets.

**To add a metric and your standard calculated attribute to your report**

1. In the **Metrics** panel, click **Add** and select **Tickets** >
   **Tickets**, and then click **Apply**.
2. Click the **Tickets** metric you just added and change its aggregator to **D\_COUNT**.
3. In the **Rows** panel, click **Add**.
4. From the list of attributes, select **Calculated attributes** > **Response time fast or slow?** (the attribute you created above) and click **Apply**.
5. To filter out tickets with no replies (the blank rows), select the **Result manipulation** menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_manipulation.png)), click **Metric filter**, select **Remove blank values** under **MED(First reply time (min))**, and click **Apply**.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_tutorial_metric_filter.png)

Your report now shows, for each channel, how many tickets had a fast response (first reply within 10 minutes) or a slow response (first reply after 10 minutes).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_tutorial_median_reply_by_channel_2.png)

Note that the **First reply time (min)** column values have changed from the first version of your report. Because you added your calculated attribute to the report, the **First reply time (min)** metric is now being sliced by that attribute in addition to the **Ticket channel** attribute. In other words, instead of showing the median first reply time for all tickets in a given channel, the metric now shows the median first reply time for tickets in the “Fast response” and “Slow response” groups for each channel.

## Step 5: Edit your attribute's formula

In this section, you'll continue to work with the standard calculated attribute you created previously, but you'll edit it to return slightly different results. In this example, you want to change the attribute's logic so that the following conditions apply:

- If a ticket’s first reply time is less than 10 minutes, group it under "Fast response” (same as before)
- If a ticket’s median first reply time is greater than or equal to 10 minutes but less than 30 minutes, group it under "Slow response"
- If a ticket’s first reply time is greater than or equal to 30 minutes, group it under "Very slow response"

To update your attribute, you'll nest multiple **IF THEN ELSE** functions to evalute the extra condition. However, the basic structure of the formula is similar to what you've already created.

**To edit the formula**

1. In the **Rows** panel, click the **Response time fast or slow?** attribute.
2. Click the pencil icon below the attribute's name.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_creating_custom_tutorial_4.png)

   The **Standard calculated attribute** panel opens, showing your standard calculated attribute.
3. Replace the formula with the following:

   ```
   IF VALUE(First reply time (min)) != NULL AND VALUE(First reply time (min)) >= 30 THEN "Very slow response"
   ELIF VALUE(First reply time (min)) != NULL AND VALUE(First reply time (min)) >= 10 AND VALUE(First reply time (min)) < 30 THEN "Slow response"
   ELIF VALUE(First reply time (min)) != NULL AND VALUE(First reply time (min)) < 10 THEN "Fast response"
   ENDIF
   ```

   This is a useful way to avoid having to write multiple **IF THEN ELSE** functions. You could also use the [SWITCH function](../writing-formulas/adding-multiple-conditional-expressions-with-switch.md) to achieve a similar result.
4. Click **Save**.

Explore automatically recalculates your report and displays the results, which now include the "Very slow response" group.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_tutorial_median_reply_by_channel_3.png)

## Next steps

Explore has hundreds of default metrics and attributes and a wide range of functions you can use in your formulas. Experiment with creating your own calculated metrics and attributes. The following articles are a great reference to help you:

- [Formula writing resources](https://support.zendesk.com/hc/en-us/articles/4408845804314)
- [Using result manipulations and calculations](https://support.zendesk.com/hc/en-us/articles/4408831146266)