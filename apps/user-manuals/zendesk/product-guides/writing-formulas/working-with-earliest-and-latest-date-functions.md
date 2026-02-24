# Working with earliest and latest date functions

Source: https://support.zendesk.com/hc/en-us/articles/4408833381402-Working-with-earliest-and-latest-date-functions

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

In this article, you'll learn about using Explore date functions that help you to focus your calculations on the first or the last event in a series.

Typically, when you report on specific events or the time between them, some of the events are not unique. For example, one ticket can have multiple resolution events. The Explore earliest and latest date functions help you find unique first and last events.

Explore features the following four earliest and latest date functions:

- DATE\_FIRST(*time attribute*)

  Returns the earliest date or timestamp according to attributes added to the report and is affected by all applied filters.

  **Example:** DATE\_FIRST([Update - Timestamp])

  Returns the earliest update timestamp taking into account all attributes you added to the report.
- DATE\_LAST(*time attribute*)

  Returns the latest date or timestamp according to attributes added to the report and is affected by all applied filters.

  **Example:** DATE\_LAST([Update - Timestamp])

  Returns the latest update timestamp taking into account all attributes you added to the report.
- DATE\_FIRST\_FIX(*time attribute, attribute1, attribute2, ...*)

  Returns the earliest date or timestamp according to the attributes specified in the function. Attributes added to the report will not affect the calculation but any filters applied will be taken into account.

  **Example:** DATE\_FIRST\_FIX([Update - Timestamp], [Update ticket ID])

  Returns the earliest update timestamp per ticket, regardless of the attributes from the report.
- DATE\_LAST\_FIX(*time attribute, attribute1, attribute2, ...*)

  Returns the latest date or timestamp according to the attributes specified in the function. Attributes added to the report will not affect the calculation but any filters applied will be taken into account.

  **Example:** DATE\_LAST\_FIX([Update - Timestamp], [Update ticket ID])

  Returns the latest update timestamp per ticket, regardless of the attributes from the report.

Note: DATE\_FIRST\_FIX and DATE\_LAST\_FIX are affected by report and dashboard filters. To ensure that no events are incorrectly left out by report or dashboard filters, use ticket-based time filters instead of update-based time filters. For example, use **Ticket created - Date** or **Ticket solved - Date** instead of **Update - Date**.

## Examples for using earliest and latest date functions

This section contains the following examples:

- [Using the DATE\_LAST function to find tickets solved on the last day of the month for a group](#topic_jgp_sdy_5pb)
- [Using the DATE\_FIRST function to find the earliest daily ticket assignment](#topic_hvz_vdy_5pb)
- [Using the DATE\_LAST\_FIX function to find the final ticket resolution date](#topic_rn1_wdy_5pb)
- [Using the DATE\_LAST\_FIX function to find the latest agent comment time](#topic_mcb_wdy_5pb)
- [Using the DATE\_FIRST\_FIX function to find the first internal comment time](#topic_hrb_wdy_5pb)

### Using the DATE\_LAST function to find tickets solved on the last day of the month for a group

In this example you'll use the DATE\_LAST function to create a report that returns tickets solved on the last date, then by adding year, month and group attributes to the report you will get resolutions for the last date of the month for each group.

**To create the report**

1. Create a new report using the **Support: Tickets** dataset.
2. Create a standard calculated metric named **Tickets solved on last date** with the following formula:

   ```
   IF DATE_LAST([Ticket solved - Date])=[Ticket solved - Date] THEN [Ticket ID] ENDIF
   ```
3. Edit the metric you just created and set its default aggregator to **COUNT**. Remove any other aggregators.
4. Add the **Tickets** and **Tickets solved on last date** metric to the **Metrics** panel of the report builder.
5. In the **Rows** panel, add the **Ticket solved - Year** and **Ticket solved - Month** attributes. You’ll see total number of solved tickets and tickets solved on the last day of the month, for example:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_date_early_late_1.png)
6. In the **Rows** panel, add the **Ticket group** attribute. You’ll see that the tickets solved on the last date are determined per group in addition to year and month:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_date_early_late_2.png)

### Using the DATE\_FIRST function to find the earliest daily ticket assignment

In this example you'll use the DATE\_FIRST function to create a report that returns the earliest ticket assignment timestamp. Then, you'll add the assignee and date attributes to get the earliest timestamp per date and assignee.

**To create the report**

1. Create a new report using the **Support: Tickets** dataset.
2. Create a standard calculated attribute named **Earliest assignment - timestamp** with the following formula:

   ```
   IF DATE_FIRST([Ticket first assigned - Timestamp])=[Ticket first assigned - Timestamp] 
   THEN [Ticket first assigned - Timestamp] 
   ENDIF
   ```
3. Add the **Tickets** metric to the **Metrics** panel of the report builder.
4. In the **Rows** panel, add the **Assignee name** and **Ticket assigned - Date** attributes. Configure the second attribute to show tickets created this week.
5. In the **Rows** panel, add the **Earliest assignment - timestamp** attribute, then filter it by excluding NULL values. You’ll see the earliest daily ticket assignments by assignee and date, for example:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_date_early_late_3.png)

### Using the DATE\_LAST\_FIX function to find the final ticket resolution date

Tickets can be resolved and reopened multiple times. In some cases, you only want to see the latest resolution. In this example you'll use the DATE\_LAST\_FIX function to produce a metric that will return the number of final ticket resolutions.

**To create the report**

1. Create a new report using the **Support: Updates history**dataset.
2. Create a standard calculated metric named **Final resolutions** with the following formula:

   ```
   IF ([Changes - Field name]="status"    
          AND [Changes - Previous value]!="solved"
         AND ([Changes - New value]="solved" OR [Changes - New value]="closed")  
         AND  DATE_LAST_FIX([Update - Timestamp], [Update ticket ID], [Changes - Field name], [Changes - New value])=[Update - Timestamp]) 
   THEN [Update ID] 
   ENDIF
   ```
3. Edit the metric you just have created and set its default aggregator to **COUNT**. You can also remove other aggregators.
4. Add the **Resolutions** and **Final resolutions** metrics to the **Metrics** panel of the report builder.
5. In the **Filters** panel, add the **Update - Date** attribute and configure this to show updates in the last 30 days. Your report will return the total number of resolutions and number of final resolutions. You can slice these metrics using any attributes, for example **Update ticket group**.

### Using the DATE\_LAST\_FIX function to find the latest agent comment time

In this example you'll use the DATE\_LAST\_FIX function to create an attribute that will return the latest agent comment timestamps that will not be sliced by the attributes from the report. This report can help you detect agent seats that were not used for a long time.

**To create the report**

1. Create a new report using the **Support: Updates history**dataset.
2. Create a standard calculated attribute named **Latest agent comment - timestamp** with the following formula and enable the **Sort like time attribute** setting:

   ```
   IF ([Comment present]=TRUE 
   AND [Comment public]=TRUE 
   AND DATE_LAST_FIX([Update - Timestamp],[Comment present],[Comment public],[Updater name])=[Update - Timestamp]) 
   THEN [Update - Timestamp] ENDIF
   ```
3. Add the **Comments** metric to the **Metrics** panel of the report builder.
4. In the **Filters** panel, add the **Ticket created - Date** attribute and configure this to show updates in the last week or month.
5. In the **Filters** panel, add the **Updater role** attribute and configure this to show **Agents** and **Admins**.
6. In the **Rows** panel, add the **Updater name** attribute.
7. Finally, in the **Rows** panel, add the **Latest agent comment - timestamp** attribute, then filter it to exclude NULL values. You’ll see the list of agents and their latest comment timestamps:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_latest_agent_comment_timestamp_updated.png)

### Using the DATE\_FIRST\_FIX function to find the first internal comment time

One of the default metrics available in the Tickets dataset is First reply time. It gives you insight on how long it took for an agent to respond to the end user. Some customers have internal processes where an internal comment is added to the ticket before a public reply.

In this example, you'll use the DATE\_FIRST\_FIX function to create a report that returns the average first internal comment time by month.

**To create the report**

1. Create a new report using the **Support: Updates history** dataset.
2. Create a standard calculated attribute named **First internal comment - Timestamp** with the following formula and enable the **Sort like time attribute** setting:

   ```
   IF ([Comment present]=TRUE
   AND [Comment public]=FALSE
   AND DATE_FIRST_FIX([Update - Timestamp],[Update ticket ID],[Comment present],[Comment public])=[Update - Timestamp])
   THEN [Update - Timestamp] ENDIF
   ```
3. Create a standard calculated metric named **First internal comment time (hrs)** with the following formula:

   ```
   DATE_DIFF([First internal comment - Timestamp], [Ticket created - Timestamp], "nb_of_hours")
   ```
4. Edit the metric you just created, set it's default aggregator to **AVG**, display format to **Custom**, and set **Decimal points** to **1** and **Suffix** to **hrs**
5. In the **Filters** panel, add the **Ticket created - Date** attribute and configure this to show updates in the last three months.
6. Add the **First internal comment time (hrs)** metric to the **Metrics** panel of the report builder.
7. In the **Columns** panel, add the **Ticket created - Month** attribute and configure this to show updates in the last 6 months.
8. Finally, in the **Visualization types** menu, select the **Column** chart. You’ll see the first internal comment time by month:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_median_first_internal_comment_updated.png)