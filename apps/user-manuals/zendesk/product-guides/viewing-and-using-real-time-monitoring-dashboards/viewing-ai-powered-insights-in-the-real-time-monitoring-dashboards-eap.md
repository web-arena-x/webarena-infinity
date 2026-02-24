# Viewing AI-powered insights in the real-time monitoring dashboards (EAP)

Source: https://support.zendesk.com/hc/en-us/articles/10009531682842-Viewing-AI-powered-insights-in-the-real-time-monitoring-dashboards-EAP

---

Verified AI summary ◀▼

Enhance your support operations with AI-powered insights in real-time monitoring dashboards. Discover top trending topics and recent anomalies across email, voice, and messaging channels. Access detailed analyses to stay informed about issues like ticket surges or reply time increases. This feature helps you manage support operations effectively by providing actionable insights and historical data on customer interactions.

AI-powered insights enhance the real-time monitoring dashboards by including
important information about your account right where you need it. You’ll find these
insights on the analytics [real-time monitoring home page](https://support.zendesk.com/hc/en-us/articles/9757124462234). AI-powered insights provide
analysis tools to help admins and supervisors stay on top of managing their support
operations.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/rtm-insights-1.png)

The following insights are available in this EAP:

- **Top trending topics:** Displays the top three trending topics.
  Examples of a trending topic include reports of a delivery delay for a product or
  reports of payment failures.
- **Monitoring insights:** Displays the last three anomalies detected for
  the email, voice, and messaging channels. Examples of monitoring insights include
  increases in ticket volume or a surge in first reply times.

This article contains the following topics:

- [Accessing real-time monitoring insights](#topic_h15_x2k_qhc)
- [Viewing top trending topics](#topic_jmj_qyj_qhc)
- [Viewing monitoring highlights](#topic_wqc_tyj_qhc)

## Accessing real-time monitoring insights

You access AI insights from the real-time monitoring home page.

**To access the real-time monitoring insights**

1. Click the **Zendesk products** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/products_icon2.png)) in the top bar, then select Analytics.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/rtm-insights-2.png)

   Analytics opens, on the
   dashboards library page.
2. Click the real-time monitoring home icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/rtm_zra_icon.png)).

   The real-time monitoring home page
   opens displaying the AI-powered insights panel.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/rtm-insights-3.png)

## Viewing top trending topics

The Top trending topics panel displays the three most reported issues with
your support operations. From here, you can open a list of all trending topics.

**To view all trending topics**

1. On the real-time monitoring home page, click **View trending
   topics**. The trending topics page opens, where you can view all trending
   and historical topics.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/rtm-insights-4.png)
2. Click any issue shown in the left-hand panel to see more information
   about it.
3. In the Ticket counts column of the Trending topics list, click a
   ticket count to see all tickets under that topic and an AI-generated summary
   that gives further details of the issues found within the topic.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/rtm-insights-5.png)

You can filter the list of trending topics by brand, queue, group, channel,
or time period. You can select a time period ranging from 60 minutes to 24
hours.

### Trending topics availability and limitations

Trending topics are derived from Zendesk intelligent triage. To see
trending topics, the [Copilot add-on](https://support.zendesk.com/hc/en-us/articles/5524125586330) and [Intelligent triage](https://support.zendesk.com/hc/en-us/articles/4964463770650) must be turned on.

During the closed EAP, trending topics has the following limitations:

- Trending topics uses intelligent triage, available with Zendesk
  Copilot. If intelligent triage is not enabled, you will see "No intents
  detected" in the trending topics view.
- You can only choose trending topics within a fixed time window
  from the last 60 minutes to the last 24 hours.

## Viewing monitoring highlights

The monitoring highlights panel displays the last three anomalies detected
for the email, voice, and messaging channels. When you click the panel, you can see
the last 20 anomalies that were reported.

**To display the anomalies page**

1. On the real-time reporting home page, click **View
   anomalies**.
2. Click any anomaly shown in the left-hand panel to see more information
   about it.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/rtm-insights-6.png)

The anomalies page contains the following sections:

- **Past anomalies:** Displays the last 20 detected anomalies.

- **Anomaly summary:** Displays an AI-generated summary of the
  anomaly, including the metrics that led to the anomaly along with possible
  underlying issues.
- **Monitoring:** This section displays the following two widgets:
  - The key metrics widget displays the value of the metrics and a
    comparison with the historical average.
  - A metrics trend with a benchmark. Anomalies are indicated with
    red dots.
- Trending topics at the time of the anomaly. At the time of anomaly all
  the tickets that were created and updated across the intents and topics. You can
  drill-in further on the intents.

When you click a monitoring widget, a drill-in view opens where you can see
details of tickets.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/rtm-insights-7.png)

### Monitoring highlights availability & limitations

Anomaly detection is available for all real-time monitoring users. During this
EAP, the following limitations apply:

- If no anomaly has occurred in the past, no data will be
  displayed.
- Anomaly detection works on a fixed set of metrics. Zendesk does
  not provide any customizations.
- Anomaly detection alerts are not supported for email or any
  third-party channels such as Slack.
- Supported channel types include Email (API, contact form,
  Support), Messaging (native messaging, social messaging), and Voice (inbound
  phone calls and voicemail).
- Customers can access the last 20 anomalies from the
  dashboard.
- Anomaly detection will start approximately seven days after an
  account is added to the EAP.
- For anomaly detection we currently support email, voice, and
  messaging channels with the following metrics:
  - **Email:** Tickets created
  - **Messaging:** Median first reply time (FRT) and ticket
    created

**Voice:** Tickets created, unassigned tickets, median first assignment time
(FAT)