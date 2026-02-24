# Analyzing your bot builder activity (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4408829761690-Analyzing-your-bot-builder-activity-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Light, Professional, or Enterprise |

Note: This article describes functionality available only to customers who had a drafted or published AI agent as of February 2, 2025. For information about equivalent functionality in the [AI agents - Advanced add-on](https://support.zendesk.com/hc/en-us/articles/6970583409690), see [Analyzing AI agents - Advanced](https://support.zendesk.com/hc/en-us/sections/8264324722970).

Zendesk Explore features a prebuilt Answer Bot dashboard that includes tabs that help you monitor your bot's performance. These dashboard tabs can help you identify how many users received a message from the bot, how many users actively engaged with the bot, and how many users’ conversations were transferred from the bot to an agent.

You can edit and customize the dashboard by [cloning it](https://support.zendesk.com/hc/en-us/articles/4408821374362). If you need something more complex, you can [create your own reports](https://support.zendesk.com/hc/en-us/articles/4408821589530)
using a wide range of [metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4408824748698#topic_mxt_wqs_crb).

The information in Explore dashboards is updated on a schedule. The schedule depends on which Explore plan you are using. See [Data refresh intervals for Explore reporting](https://support.zendesk.com/hc/en-us/articles/4408823242778).

This article contains the following topics:

- [Accessing the Answer Bot dashboard](#topic_ccc_vzs_crb)
- [Understanding the Flow Builder Overview tab](#topic_wpl_tzs_crb)
- [Understanding the Flow Builder Performance tab](#topic_fwz_g4x_tvb)

For information about the Article Recommendations tab, see [Analyzing article recommendations](https://support.zendesk.com/hc/en-us/articles/4409155069466).

## Accessing the Answer Bot dashboard

Use this procedure to open the Answer Bot dashboard.

**To access the Answer Bot dashboard**

1. In Explore, click the **Dashboard** icon (
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select the **Zendesk Answer Bot** dashboard.

## Understanding the Flow Builder Overview tab

The Flow Builder Overview tab shows information about your users’ engagement with the bot you've built with Flow Builder (also known as bot builder) and deployed across messaging channels. You can filter the reports on the dashboard by **Time**, **Brand**, **Channel**, and **Language**.

**To open the Flow Builder Overview tab**

1. In Explore, click the **Dashboard** icon (
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select the **Zendesk Answer Bot** dashboard.
3. Click the **Flow Builder Overview** tab.

### Flow Builder Overview tab headline metrics

The dashboard displays the following headline metrics (KPIs):

- **Total users**: The number of unique users who received a message from the bot.
- **Engaged with bot**: The number of total users who actively participated in the conversation (for example, sent messages or selected options presented by the bot).
- **Transferred to agent**: The number of engaged users whose conversation was transferred from the bot to an agent. Also represents the number of tickets created.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_fb_dashboard_KPIs.png)

### Flow Builder Overview tab reports

The dashboard displays the following reports:

- **Users by month**: Shows the total users, engaged users, and transferred users each month.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_fb_dashboard_users_by_month.png)
- **Top answers**: Shows the answers that users engaged with, ranked in descending order of count by default, along with the percentage of those engaged users who then asked to be transferred to an agent.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_ab_dashboard_overview_tab_top_answers.png)
- **Top selected options**: Shows how many times each quick reply of each answer has been selected by an end user, ranked in descending order of count by default. If an answer or quick reply option is available in multiple languages, or has had its wording updated since originally released, those will show up as separate rows in this report.

 Use this report to understand your customers’ most common inquiries or problem topics, and how they’re typically interacting with the bot.
 A limited number of rows are visible by default. To see more, you can scroll down in the table, expand the table to see more at once, or [export the data](https://support.zendesk.com/hc/en-us/articles/4483481898266)
 into a CSV or Excel file to view it there.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_ab_dashboard_overview_tab_top_selected_options.png)
- **Users by day of week or hour**: Shows the total users, engaged users, and transferred users each day. Clicking **Hour** toggles the graph to show the same data for each hour of the day.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_fb_dashboard_users_by_day_or_hour.png)
- **Users by brand or channel**: Shows the total users, engaged users, and transferred users by brand. Clicking **Channel** toggles the graph to show the same data for each [messaging channel](../suite-basics/about-zendesk-channels.md#topic_ik1_ppb_j4b).

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_fb_dashboard_users_brand_channel.png)

## Understanding the Flow Builder Performance tab

The **Flow Builder Performance** tab shows information about bot and answer performance. This information gives admins the tools they need to measure and improve their bot automation performance. You can filter the reports by time, brand, channel, and language.

**To open the Flow Builder Performance tab**

1. In Explore, click the **Dashboard** icon (
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. From the list of dashboards, select the **Zendesk Answer Bot** dashboard.
3. Click the **Flow Builder Performance** tab.

### Flow Builder Performance tab reports

This tab displays the following reports:

- **Containment rate**: The percentage of conversations with engaged users where the user was not transferred from the bot to an agent.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_ab_dashboard_fbperf_containment.png)
- **Responses received**: The total number of times that a user responded when asked for feedback by the bot, the total number of times that a bot asked a user for feedback, and the percentage of instances where users responded to a bot’s feedback request.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_ab_dashboard_fbperf_responses_received.png)
- **Resolved**: The total number and the percentage of instances where users who responded indicated that their issue was resolved.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_ab_dashboard_fbperf_resolved.png)
- **Unresolved**: The total number and the percentage of instances where users who responded indicated that their issue was not resolved.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_ab_dashboard_fbperf_unresolved.png)
- **Top resolved answers**: The answers with the highest proportion of resolved responses from users.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_ab_dashboard_fbperf_top_resolved_answers.png)
- **Top unresolved answers**: The answers with the highest proportion of unresolved responses from users.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_ab_dashboard_fbperf_top_unresolved_answers.png)
- **Resolution rate by month**: The percentage of conversations with the bot when a user’s issue was successfully resolved by the bot.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_ab_dashboard_fbperf_resolution_rate_month.png)