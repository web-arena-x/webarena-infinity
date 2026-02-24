# Monitoring chat activity with Analytics

Source: https://support.zendesk.com/hc/en-us/articles/4408828193562-Monitoring-chat-activity-with-Analytics

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Professional or Enterprise |

If your plan includes Zendesk Explore, you can also analyze Chat activity using a prebuilt dashboard. See [Analyzing your Chat activity](https://support.zendesk.com/hc/en-us/articles/4408837869850).

Analytics displays a series of reports, giving you an overview of your chat and agent activity. With this data you can optimize your customer support strategy and improve its efficiency.

Chat analytics are updated once an hour, and display the data for the previous hour. For example, if you look at a report at 9:15 a.m., you'll see data from 8 a.m. and earlier.

Note: Chats deleted from the Chat History will still be included in the Analytics

This article contains the following sections:

- [Using Analytics: Chat reports](#topic_qyc_xqq_5mb)
- [Using Analytics: Agent reports](#topic_lsh_xqq_5mb)
- [Filtering Analytics reports](#topic_xbm_xqq_5mb)
- [Exporting Analytics data as a CSV file](#topic_ojd_brq_5mb)
- [Receiving email reports of Analytics data](#topic_gdm_brq_5mb)
- [Monitoring chat capacity](#topic_orv_brq_5mb)

## Using Analytics: Chat reports

The Chat reports tab displays information on all the chats in your account, including:

- [Chat stats](#topic_vd4_drq_5mb)
- [Satisfaction ratings](#topic_djs_drq_5mb)
- [Chat timings](#topic_jhw_drq_5mb)

### Chat stats

The Chat Stats graph lets you compare the volume of chats with their timing trends, on an hourly, daily, or weekly basis.

![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_analytics_chatreportsfinal2.png)

Determine your busiest periods by observing visitor wait times, response times, satisfaction ratings, and acceptance rate, and the number of chats served and missed by your agents at any given time. The graph includes a stacked bar chart with all served and missed chats, giving you an overview of your agents chat load in any given time period.

Note: If [auto-accept](https://support.zendesk.com/hc/en-us/articles/6009407849754) is turned on, acceptance rate is not displayed in Chat stats.

Note: Wait Time (Served) shows the same results as First Response Time in the CSV. This means you will see the time it takes for agents to respond to initial chat requests.

Next to each metric is an up/down arrow comparing the currently selected period with the previous one. For example, if your currently selected period is Last 7 Days, then it will compare the number of served chats, missed chats, and your chat timings with the previous seven day period.

### **Satisfaction ratings**

The Satisfaction Ratings section shows the percentage of chats rated Good and Bad for the given time period.

![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/satisfaction_rating2.png)

Click on either portion of the graph to see chat history details for chats with that rating.

### **Chat timings**

The Chat Timings section shows you chat response times, chat lengths, how long visitors waited before first receiving a response, and the time between a visitor's last reply and when they ended the chat (without an agent response).
This graph can help you see if your efforts in improving visitor wait times have had an effect.

![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/analytics_chattimings2.png)

## Using Analytics: Agent reports

The Agent Reports tab shows graphs of overall and individual agent activity on your account, including:

- [Viewing activity for all agents](#topic_nbg_wrq_5mb)
- [Viewing activity for individual agents](#topic_k1k_wrq_5mb)

### Viewing activity for all agents

On the **All Agents** tab, you can see the number of agents logged in versus various chat metrics.

![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_analytics_allagents2.png)

Under the graph, you can also view an Activity Breakdown of all your agents and their chats.

- Click the **Leaderboard** tab to see a list of agents sorted by who has served the most chats.
- Click any of the other column headings to sort by that column.

 ![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_analytics_activitybreakdown.png)
- Select the **Leaderboard** dropdown menu in the upper right and choose **Agents Logged In**, **Agents Online**, or **Agents Serving** to see a schedule for each group of agents for the given time period. Note that this feature only shows logged in times to the nearest hour.

 ![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/activitybreakdown_agentsloggedin2.png)

### Viewing activity for individual agents

Click the **Individual Profile** tab at the top of the page to see a specific agent's activity, including total time serving and logged in, when the agent was last seen, total number of served chats, acceptance rate, and satisfaction ratings. You can also view the agent's individual activity by clicking the magnifying glass next to their name from the Leaderboard.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Agent-Reports_IndividualProfile.png)

Under the graph, see an Activity Breakdown for the specific agent selected above.
Click the **Performance** tab to see details on the agent's performance compared with the average for your account, as well as their Logged In, Online, and Serving schedules for the given time period. You can also hover over a section of the schedule to view a breakdown of their time in each status (Online, Away, or Invisible).

Note: If [auto-accept](https://support.zendesk.com/hc/en-us/articles/6009407849754) is turned on, acceptance rate is not displayed in the Individual Profile.

![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/activity_breakdown.png)

- **Response Time** refers to the average time it takes for this agent to respond to the last visitor message in that chat.
- **Average Response Time** refers to the average value of the average response time across all the agents chats.

Click the **Satisfaction** tab to see an overview of the agent's satisfaction ratings and related comments.

![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/activitybreakdown_satisfaction2.png)

## Filtering Analytics reports

You can filter your analytics reports by the certain criteria, including:

- [Filtering by time range](#topic_egv_tsq_5mb)
- [Filtering by department](#topic_ky1_5sq_5mb)

### Filtering by time range

You can view Chat and Agent Reports data for any of the following preset time ranges:

- Last 1 day (24 hours)
- Last 7 days
- Last 14 days
- Last 30 days

You can also select a custom time range.

![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/analytics_daterange2.png)

Data in the Chat Stats graph can be viewed on an hourly, daily, or weekly basis. Hourly data is limited to a 24 hour period, daily data is limited to 31 days and weekly data is limited to 90 days.

The data in all graphs includes the last full day that has passed. For example, the “Last 1 day” hourly data includes the last 24 hours from the the previous midnight.

### Filtering by department

Note: Departments are only available on accounts with the Enterprise plan.

You can group chat and agent activity data by department by selecting a department from the **Filter Department** dropdown menu:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/department_filter2.png)

Deleted departments are not displayed in the filter department dropdown list, and any historical Chat data linked to any deleted Chat departments is not included in the analytics dashboard.

## Exporting Analytics data as a CSV file

You can export your Chat and Agent Reports into a CSV file. In the exported CSV file, the first row of data will always start from 00:00 of the selected timezone.

For details about the metrics that are exported to the CSV file, see the [Analytics CSV glossary.](https://support.zendesk.com/hc/en-us/articles/4408893283098)

**To export data into a CSV file**

1. Click **Download CSV** in the upper right-hand corner.
2. Select the reports, date range, interval, and recipients in the window that appears. Emails must already be registered in your Zendesk Chat account. You can enter multiple emails separated by commas. Enterprise accounts can choose to export data by department.

   ![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_analytics_csv_export.png)
3. Click **Send**.

Tip: The CSV file is sent from chat@zendesk.com. To make sure you receive the file, [add this address to your allowlist](https://support.zendesk.com/hc/en-us/articles/4408886840986#topic_jqt_4b4_xz) or verify that it isn't in your blocklist.

## Receiving email reports of Analytics data

You can receive Analytics email reports weekly, monthly, or (for Enterprise accounts) daily.

**To enable Analytics email reports**

1. From the dashboard, go to **Settings** > **Personal**.
2. Click the **Email Reports** tab.
3. Select the **Enable email reports** check box.![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/analytics_enablereports.png)
4. Select the frequency of reports you want to receive.

   Note: Only Enterprise accounts have the option of daily email reports.

   ![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/analytics_reportfrequency.png)
5. Click **Save Changes**.

Tip: The email reports are sent from noreply@zopim.com. To make sure you receive the file, [add this address to your allowlist](https://support.zendesk.com/hc/en-us/articles/4408886840986#topic_jqt_4b4_xz) or verify that it isn't in your blocklist.

## **Monitoring chat capacity**

Capacity is the estimated amount of chats that can be served by the account in a given period of time. The capacity is a function of the number of agents logged in, the average chat duration of an account, and the chat limit set by the agent. Under **Agent Reports** > **All Agents**, you can compare capacity with total chat volume to get a sense of how over- or underutilized your agents are based on your current chat routing settings.
For details about chat routing, see [Setting up Chat Routing](https://support.zendesk.com/hc/en-us/articles/4408836490138).

![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_analytics_capacity.png)

**To enable chat capacity**

1. From the dashboard, select **Analytics**.
2. Click the **...** menu in the upper right corner.
3. Select **Enable Capacity**.

   ![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_analytics_enable_capacity.png)