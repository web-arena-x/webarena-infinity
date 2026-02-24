# Analyzing omnichannel routing queues

Source: https://support.zendesk.com/hc/en-us/articles/9046706751002-Analyzing-omnichannel-routing-queues

---

All Suites | Professional, Enterprise, or Enterprise Plus

Support with | Explore Professional or Enterprise

Important: You must be using [omnichannel routing queues](https://support.zendesk.com/hc/en-us/articles/6716530152858) to use the
dashboard described in this article.

Explore features a prebuilt dashboard to help you monitor how well omnichannel
routing queues are distributing work to agents. Supervisors can use this dashboard to
understand the inbound and outbound volume of queues, average and longest wait times for
any given queue, and drill down to tickets within the queue to understand why the ticket
entered or exited the queue.

Tip: You can [clone this dashboard](https://support.zendesk.com/hc/en-us/articles/4408821374362) and [customize it](https://support.zendesk.com/hc/en-us/articles/4408819770906) to meet more specific requirements. If you
need something more complex, you can [create your own reports](https://support.zendesk.com/hc/en-us/articles/4408821589530) using metrics and attributes for
omnichannel routing queues. See [Metrics and attributes for omnichannel custom
queues](https://support.zendesk.com/hc/en-us/articles/9046662025498).

This article contains the following topics:

- [Current limitations](#topic_qr3_nhd_t2c)
- [Opening the dashboard](#topic_hfs_xhd_t2c)
- [Understanding the reports](#topic_dyw_xhd_t2c)

## Current limitations

- Call tickets are not captured by the omnichannel routing queues dataset. This is
  planned for a future release.

## Opening the dashboard

Use the following procedure to access the queues dashboard.

**To access the dashboard**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png))
2. From the list of dashboards, click the **Queues** dashboard.

## Understanding the reports

The queues dashboard contains the following tabs:

- [Activity
  tab](#topic_dyw_xhd_t2c__ul_el2_3jd_t2c)
- [Wait times
  tab](#topic_dyw_xhd_t2c__section_uld_1gd_t2c)

### Activity tab

The Activity tab shows information about the tickets that have entered
and exited any given queue. In this report, you can also drill into queues to
see which exact tickets have entered or exited the queue, with specific inbound
or outbound reasons. You can filter the reports by Date, Channel, Queue and
Queue Groups.

### Activity tab headline metrics

This tab displays the following headline metrics (KPIs):

- **Tickets entered queue:** The total number of tickets that
  entered queues within the specified filter conditions.
- **Tickets exited queue:** The total number of tickets that
  exited queues within the specified filter conditions.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocr_queue_dash_1.png)

### Activity tab reports

This tab displays the following reports:

- **Tickets Entered vs. Exited**: The total number of tickets
  that entered and exited queues daily within the specified filter
  conditions.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocr_queue_dash_2.png)

- **Volume details:** A table that shows, for each queue and each
  day, how many tickets have entered and exited the queue for each
  channel.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocr_queue_dash_3.png)

You can drill into this report to see more details such as ticket IDs
that have been counted towards the calculated metric and inbound or outbound
reasons to describe why the ticket had entered or exited the queue.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocr_queue_dash_4.png)

**Drill in to view tickets:** View the ticket, and whether it had
entered or exited the queue within the corresponding day of the chosen data
point. You can drill in further to view more details around when and why the
ticket entered or exited the queue at that time.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocr_queue_dash_5.png)

**Drill in to view ticket inbound or outbound details:** View when and why the selected ticket entered or exited the queue at
that time.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocr_queue_dash_6.png)

### Wait times tab

The Wait times tab shows information about how long tickets have waited
in the queue. You can filter the reports by date, channel, queue and queue
groups.

### Wait times tab reports

This tab displays the following reports:

- **Average wait time by channel:** The average wait time by
  channel daily within the specified filter conditions.
- **Longest wait time by channel:** The longest wait time by
  channel daily within the specified filter conditions.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocr_queue_dash_7.png)

- **Wait times by queue:** A table of the average and longest time a ticket spent in the queue for each
  channel, per queue and day.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocr_queue_dash_8.png)