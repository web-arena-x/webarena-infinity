# Using drill in to refine your reports

Source: https://support.zendesk.com/hc/en-us/articles/4408826499482-Using-drill-in-to-refine-your-reports

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

Drill in enables you to refine the results of your Explore report by slicing metrics using extra attributes you choose or by allowing the report viewer to choose from a range of attributes. For example, you create a report showing all of your tickets by assignee name. You could configure drill in to additionally display the status for each ticket or add an optional attribute for the ticket channel.

This article contains the following sections:

- [Configuring drill in](#topic_bwr_sbd_zpb)
- [Using drill in](#topic_sgl_5cd_zpb)
- [Drill in example](#topic_y25_cfd_zpb)
- [Exporting your drill in results](#topic_o42_y3l_cqb)
- [Turn on drill in on a dashboard](#topic_x3z_l42_lqb)

## Configuring drill in

You configure drill in options for each report you create.

**To configure drill in**

1. In your report, from the Chart configuration menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)), click **Drill in**.
2. In the **Drill in** panel, click **Enable drill in**.
3. In the drop-down list under **Enable drill in**, choose up to 20 attributes that will be displayed when the report viewer drills in to a metric in your report.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_drill_in_8.png)
4. You can add more levels to your drill in to dig deeper into your data. For example, if you added the Ticket status attribute to your drill in, you could then click the associated metric and drill in by further attributes. If you want to add more levels to your drill in, click **Add more levels**.

   Tip: While there is no limit to the number of levels you can add, Zendesk doesn't recommend using more than 10 levels for performance and administration purposes.
5. If you want the report viewer to be able to optionally add other attributes, click **Enable adding attributes**, then, from the drop-down list select up to 20 attributes they can add or remove to the report.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_drill_in_2.png)

Note: [Metric filters](https://support.zendesk.com/hc/en-us/articles/4408821978266) don't apply to drill in reports. To set a floor or ceiling for drill in results, [use a report-level filter](https://support.zendesk.com/hc/en-us/articles/4408825475354)
instead.

## Using drill in

After you've [configured drill in on a report](#topic_bwr_sbd_zpb), you can drill into a metric to see attributes (information and context) associated with that metric. You can't drill in to an attribute itself.

**To use drill in**

1. In your report, select the data point you want to drill into. In area charts, click and drag to select the data area you want to drill into.
2. From the menu, click **Drill in**. Explore displays the **Drill in** panel showing all metrics sliced by the drill in attributes you chose.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_drill_in_3.png)

   For example, if your report contains the Tickets metric and the Ticket status attribute, you can click any "Tickets" value to drill in and show the tickets with that status.
3. If you configured more drill in levels, you can click any metric result to show more information.

Note: Drill in displays results using the default metric format. To display a different format in the drill in results, change the default metric format to the required value.

## Drill in example

In this example, you've created a report using the Support: Tickets dataset. It produces a simple table that shows each assignee name and the number of tickets assigned to that person.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_drill_in_1.png)

You want to allow users to drill into this data by showing the status of each ticket and, optionally, the channel from which each ticket came. Use the following procedure to accomplish this.

**To configure the example**

1. In your report, from the Chart configuration menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)), click **Drill in**.
2. In the **Drill in** panel, click **Enable drill in**.
3. First, you'll configure drill in to show the status of the ticket. In the **Select attributes** drop-down, choose **Ticket status**.
4. Next, choose the ticket channel attribute which report viewers can optionally display. Click **Enable adding attributes**.
5. In the **Select attributes** drop-down, choose **Ticket channel**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_drill_in_2.png)
6. You can now test your new drill in configuration. In your report, click one of the **Tickets** results, then click **Drill in**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_drill_in_3.png)
7. The **Drill in** panel opens displaying the tickets you selected broken down by status.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_drill_in_4.png)
8. If you want to add the optional ticket channel attribute you configured to the drill in, click the **Select information to show** drop-down list and add **Ticket channel**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_drill_in_7.png)
9. If you want to return to your original report, click **Cancel**.

## Exporting your drill in results

You can export your drill in results in comma-seperated values (CSV) or Excel format.

**To export your drill in results**

1. In the drill in panel, click **Export** > **CSV** or **Excel**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_drill_in_5.png)
2. Explore prepares the file and adds it to your computer's downloads folder.

## Turn on drill in on a dashboard

You might need to proactively turn on the drill in feature on certain dashboards.
This applies only to dashboards where you’ve previously [turned off other report interactions](https://support.zendesk.com/hc/en-us/articles/4408834479258#topic_n3r_zk2_gv).

Before turning on drill in on a dashboard, make sure that drill in is also turned on for at least one of the reports on the dashboard. Otherwise, the dashboard-level setting won't be saved.

Drill in isn't available on [dashboards shared externally](https://support.zendesk.com/hc/en-us/articles/4408826905626), including dashboards shared to Zendesk end users.

**To turn on drill in on a dashboard**

1. Open your dashboard for editing.
2. Click the settings icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dash_setings.png)) to open the general dashboard settings.
3. Select **Allow drill-in on historical data**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dash_drill_1.png)

Note: When drill in is enabled for a [legacy dashboard](https://support.zendesk.com/hc/en-us/articles/8096478451098), only one filter will be applied at a time. Legacy dashboards don't support multiple filters for drill in; only the newest configured filter is applied. You can click the filter button to switch between filters.