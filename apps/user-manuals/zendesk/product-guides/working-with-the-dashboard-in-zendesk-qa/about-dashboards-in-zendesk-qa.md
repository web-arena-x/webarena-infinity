# About dashboards in Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/7043701144858-About-dashboards-in-Zendesk-QA

---

Dashboards in Zendesk QA offer valuable insights into the quality of your customer service. They allow you to view, customize, and download reports that give you an overview of your Zendesk QA data.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Dashboards in QA provide insights into your customer service quality. You can filter data to assess team performance, customize display settings, and download reports in CSV or PDF formats. Access additional data points by drilling down into specific metrics, and check the last data update time to ensure you're viewing the latest information. This helps you manage and improve your support operations effectively.

Location: Zendesk QA > Dashboards

Dashboards in Zendesk QA offer valuable insights into the quality of your customer service. They allow you to view, customize, and download reports that give you an overview of your Zendesk QA data.

Use dashboard filters to efficiently locate the data necessary for assessing and enhancing your team's performance.

You must allow third-party cookies in your browser to view Zendesk QA dashboards properly.

This article contains the following topics:

- [Using dashboard filters](#topic_kcp_yv1_cbc)
- [Understanding the Display settings menu](#topic_xlj_yjx_vfc)
- [Understanding dashboard filters](#topic_dmj_yjx_vfc)
- [Time period selection](#topic_fmj_yjx_vfc)
- [Accessing additional data points](#topic_rnw_zjx_vfc)
- [Downloading dashboard data](#topic_hng_tlx_vfc)
- [Accessing the dashboard’s last data update time](#topic_wk1_gsx_vfc)

## Using dashboard filters

Dashboards display a list of filters that help you analyze the data in your workspaces and quickly find the information you need. You can apply one or more filters to your workspaces.

Note: Workspace members with the [agent role](https://support.zendesk.com/hc/en-us/articles/7043760141978#workspace-users) can see only their own data.

**To apply dashboard filters**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Dashboards**
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_dashboard_icon.png) in the sidebar.
2. The following dashboards are available in Zendesk QA, depending on your permissions:
   - [Reviews](https://support.zendesk.com/hc/en-us/articles/7043724913690)
   - [AutoQA](https://support.zendesk.com/hc/en-us/articles/9019507481242)
   - [BotQA](https://support.zendesk.com/hc/en-us/articles/7418648572826)
   - [Assignments](https://support.zendesk.com/hc/en-us/articles/8207770590490)
   - [Surveys](https://support.zendesk.com/hc/en-us/articles/7043759414042)
   - [Disputes](https://support.zendesk.com/hc/en-us/articles/7043760048922#dispute-dashboard)
   - [Categories](https://support.zendesk.com/hc/en-us/articles/9019975345434)
   - [Calibration](https://support.zendesk.com/hc/en-us/articles/7043724530842#viewing-results)
3. Select the filters you want to apply from the filter row on the top. The default filter applied is Last 30 days.

   Click the plus sign (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_plus_sign.png)) to access additional filters.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_dashboards_filters.png)

   See [Understanding dashboard filters](#topic_dmj_yjx_vfc).

   Tip: The system reverts to the default filter and resets all applied filters every time you visit a different page in Zendesk QA. To save your dashboard filters for your next visit, you can use browser bookmarks, such as [Google Chrome bookmarks](https://support.google.com/chrome/answer/188842).
4. (Optional) Click the display menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_view_icon.png)) in the top right to choose how to display your data and which cards to show or hide on your dashboard. See [Understanding the Display settings menu](#topic_xlj_yjx_vfc).
5. (Optional) Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_options_menu_vertical.png)) to download your filtered data.
6. (Optional) Click **Reset** to clear all applied filters.

## Understanding the Display settings menu

Use the display settings menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_view_icon.png)) in the top right corner to select how to display your data and which cards and charts to display or hide on your dashboard.

Hiding display data affects only the dashboard visualization. The data remains visible in CSV and PDF downloads.

The data varies by dashboard but can include:

- Conversation created date
- Review created date

Self-reviews:

- Exclude self-reviews
- Include self-reviews
- Show only self-reviews

Date granularity:

- Day
- Week
- Month
- Quarter

Assign CSAT score to:

- Owner of the ticket
- Agent with most replies

Display data based on:

- CSAT survey reply date
- Conversation creation date
- CSAT survey sent date

Survey chart attribute:

- Survey response reason
- Survey response language
- Survey response predicted driver
- Conversation channel
- Conversation source
- Conversation tag

## Understanding dashboard filters

Depending on the dashboard you select, you can apply the following filters:

| | |
| --- | --- |
| **Filter name** | **Description** |
| Date filter | Select a time period. By default, the dashboard returns data for the last month. See [Time period selection](#topic_fmj_yjx_vfc). Dates are also determined based on the [Display settings](#topic_xlj_yjx_vfc)selection. |
| Workspaces | Choose your [workspaces](https://support.zendesk.com/hc/en-us/articles/9203020826266). This filter displays results based on selected workspaces. You'll see data only for workspaces that you are a member of. |
| Reviewer | The user [giving the review](https://support.zendesk.com/hc/en-us/articles/7043669307418). |
| Reviewee | The user [receiving the review](https://support.zendesk.com/hc/en-us/articles/7043760283546). |
| Group | Allows you to select a [group](https://support.zendesk.com/hc/en-us/articles/7043747142938). Using groups helps you avoid selecting multiple agents each time you want to see a group's performance. This filter limits the options to conversations in which reviewees and reviewers from those groups participated. |
| Scorecard | Allows filtering by [scorecard](https://support.zendesk.com/hc/en-us/articles/7043760215194) if multiple scorecards are available. |
| Category | Display results based on selected [categories](https://support.zendesk.com/hc/en-us/articles/8992409602842). |
| Connection name | Choose your connection (for example, if you're using [multibrand](https://support.zendesk.com/hc/en-us/articles/4408829476378#topic_hyq_l1v_cr) Zendesk instances). |
| Hashtag | Report on the [hashtags left in the Zendesk QA comment section](https://support.zendesk.com/hc/en-us/articles/7043700996762). |
| Helpdesk tag | Filter by [connection](https://support.zendesk.com/hc/en-us/articles/4408888664474) ticket tag. |
| Conversation channel | Display results based on the [conversation channel](https://support.zendesk.com/hc/en-us/articles/4408824097050). For example, only email reviews. |
| Assignment name | Access manual review data based on active [assignments](https://support.zendesk.com/hc/en-us/articles/7043747327770) that are accessible to you. |
| Helpdesk field and value | Filter by ticket [fields](https://support.zendesk.com/hc/en-us/articles/4408883152794). |
| Root cause | Select one or more root causes. |
| Language | Display results based on selected [conversation languages](https://support.zendesk.com/hc/en-us/articles/4408821324826#01J2KMA3YJ45DGA1GEZZVHEWQ9). |
| Rating category | Display results based on selected [autoscoring categories](https://support.zendesk.com/hc/en-us/articles/7043747123354). |
| Participant type | [Bot](https://support.zendesk.com/hc/en-us/articles/7418648293018) or user. |
| Connection | Display results based on [connections](https://support.zendesk.com/hc/en-us/articles/7043669282714). |
| Rating score | Display results based on selected [rating score](https://support.zendesk.com/hc/en-us/articles/7043701093786#understanding_rating_categories) values. |
| Low bot communication efficiency | Show results based on if the [low bot communication efficiency insight](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_lmq_fvh_xdc) is detected or not. |
| Bot repetition | Display results based on whether [bot repetition insights](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_lmq_fvh_xdc) are detected. |
| Churn risk | Display results based on whether [churn risk insights](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_lmq_fvh_xdc) are detected. |
| Escalation | Display results based on whether [escalation insights](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_lmq_fvh_xdc) are detected. |
| Exceptional service | Display results based on whether [exceptional service insights](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_lmq_fvh_xdc) are detected. |
| Follow-up | Display results based on whether [follow up insights](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_lmq_fvh_xdc) are detected. |
| Outlier | Display results based on whether [outlier insights](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_lmq_fvh_xdc) are detected. |
| Dead air | Display results based on whether [dead air](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_lmq_fvh_xdc__dead_air) lasting longer than the set threshold was detected in voice conversations. |
| Recording disclosure missing | Display results based on whether the [speaker disclosed that the voice conversation was being recorded](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_lmq_fvh_xdc__recording_missing). |
| Sentiment | Display results based on whether [sentiment insights](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_lmq_fvh_xdc) are positive or negative. |
| Helpdesk tag | Display results based on [ticket tags](https://support.zendesk.com/hc/en-us/articles/4408881573658) . |
| Call | Display results for [voice calls](https://support.zendesk.com/hc/en-us/articles/8536308081178) only, text-based interactions (chats and emails) only, or both. |

## Time period selection

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_dashboards_date.png)

- **"This" date range selections**: Include today as one of the days counted for this week, month, or year.
- **"Last" date range selections**: Include the current day, week, month, quarter, or year. For example, defining the custom period "Last 3 days" returns data for the day before yesterday, yesterday, and through the end of today. It includes today as one of the three days. Similarly, "Last 2 months" returns data for the current and previous months.
- **Custom period**: The date range picker provides a calendar that allows you to select both a start date and an end date. The selected date range includes both the start and end dates. Double-click on a date to select only that day.

## Accessing additional data points

Access additional data points by drilling down into specific metrics.

Note: If a conversation has more than one review, you can have more rows in the drill-down than the number of unique conversations. For example, you can observe this in the [AutoQA dashboard drill-down](https://support.zendesk.com/hc/en-us/articles/9019507481242#topic_fvl_1xq_42c) and the [Reviews dashboard drill-down](https://support.zendesk.com/hc/en-us/articles/7043724913690#topic_qsl_bv5_s2c).

**To access additional data points on your dashboard**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Dashboards**
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_dashboard_icon.png) in the sidebar.
2. Click to open a dashboard.
3. Click on any score, review, category, root cause, or conversation value to access the list of associated reviewed conversations.

   For example, click the percentage value displayed on the Reviews dashboard IQS card or the goal completion percentages in the Assignments dashboard to drill down into the data for each conversation.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_dashboards_assignments_goal.png)

   You can also click a line on a score graph and use the dropdown menu to select a drill-down option:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_drill_down_rating_scores.png)
4. Explore the additional data points or click any conversation link to open it. Both the review and conversation IDs are hyperlinked for easy navigation to specific review conversations.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_dashboards_assignments_goal_drill_down.png)

## Downloading dashboard data

You can download data from your dashboards either as a whole or for individual cards. The data is available in CSV or PDF file formats.

### Downloading all dashboard data

You can download the data from all your dashboard cards.

If the dashboard data is filtered, the download reflects the [applied filters](#topic_kcp_yv1_cbc). However, [hiding display data](#topic_xlj_yjx_vfc) affects only the dashboard visualization; the data remains visible in CSV and PDF downloads.

**To download the dashboard data**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Dashboards**
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_dashboard_icon.png) in the sidebar.
2. Click a dashboard to open it.
3. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_options_menu_vertical.png)) in the top-right corner of the dashboard to download your data.
4. Select **Download**.
5. Set the **Format** to either **CSV** or **PDF**.

   If you select PDF, specify whether you want to expand tables to show all rows. Note that large tables may render as plain text or limit the number of displayed rows. Additionally, indicate if you want to arrange dashboard tiles in a single column.

   If you select CSV, all dashboard cards will be downloaded as individual CSV files in a zip folder.
6. Click **Download**.

### Downloading dashboard data for a single card

You can download data individually for specific dashboard cards.

**To download dashboard data for a specific card**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Dashboards**
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_dashboard_icon.png) in the sidebar.
2. Click a dashboard to open it.
3. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_options_menu_vertical.png)) next to a card and select **Download data**.
4. Select **Download data**.
5. Select a **Format**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_reviews_dashboard_download_formats.png)
6. By expanding the **Advanced data options** menu, you can choose whether to download your results with visualization options applied or as displayed in the data table.
   - **With visualizations options applied**: The download attempts to reflect any customizations made in the visualization, although it may not match exactly. This includes options such as re-labeling columns, hiding totals, or adding conditional formatting.
   - **As displayed in the data table:** Includes more fields than those currently visible in your dashboard card.
   - **Data values:** You can also choose whether to download your results with data values formatted (for example, rounding, special characters) or not.
   - **Number of rows to include**: You can specify the number of rows to include.
     Options include selecting the current result table, all results, or a custom number of rows.

     The custom number of rows is limited to 5,000. This number can be increased by selecting All results.
7. Click **Download**.

## Accessing the dashboard’s last data update time

The **Last data update time** card of each dashboard allows you to see when the dashboard was last updated. Time is in UTC:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_last_updated.png)

To find the last data update time for a dashboard, [navigate to the dashboard](#topic_kcp_yv1_cbc). The last updated timestamp card is typically displayed at the top or bottom of the dashboard, or it can be enabled in the [Display settings menu](#topic_xlj_yjx_vfc).
Make sure to refresh the dashboard to view the most current update:

- Dashboard data is updated approximately every 60 to 90 minutes for hashtags, ticket tags, ticket fields, conversations, groups, conversation channels, survey data, and assignment name fields.
- Reviews, ratings, rating categories, comments, disputes, feedback, scorecards and root causes are updated every 30 to 35 minutes.
- Assignments, assignment cycles, assignment tickets, and assignment reviews are updated at least every 15 minutes.
- Dashboard data for workspaces and users is updated approximately every 90 minutes.