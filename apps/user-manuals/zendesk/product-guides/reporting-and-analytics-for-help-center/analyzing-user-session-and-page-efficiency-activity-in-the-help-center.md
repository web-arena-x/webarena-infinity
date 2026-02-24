# Analyzing user session and page efficiency activity in the help center

Source: https://support.zendesk.com/hc/en-us/articles/9118856019098-Analyzing-user-session-and-page-efficiency-activity-in-the-help-center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Verified AI summary ◀▼

Explore the self-service dashboard to analyze user sessions and page efficiency in your help center. Track user interactions, session outcomes, and content performance with metrics like session duration, page views, and ticket deflections. Customize reports to focus on specific scenarios, such as filtering by brand or content type, to gain insights into how your help center content is performing.

Zendesk features a prebuilt self-service dashboard that helps you understand how often your help center articles and community posts are being viewed and who is viewing them.

Important: Self-service data is available from January 15, 2025 onwards.

The dashboard can help you:

- See user session outcomes for specific users.
- Look at trends across the different roles.
- Understand content performance, including which articles are most helpful and which are responsible for the most tickets submitted.

You can edit and customize the self-service dashboard by cloning it (see [Cloning dashboards](https://support.zendesk.com/hc/en-us/articles/4408821374362-Duplicating-pre-built-and-shared-dashboards)).

Tip: If you need something more complex, you can write your own reports using a wide range of metrics and attributes. For details, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530).

The information in Explore dashboards is updated on a schedule. The schedule depends on which Explore plan you are using. For details, see [Data refresh intervals for Explore plans](https://support.zendesk.com/hc/en-us/articles/4408823242778).

Important: All ticket deflection reports, such as confirmed and assumed deflections, only track tickets submitted using the help center request form.

This article contains the following topics:

- [Accessing the self-service dashboard](#topic_p1h_fqt_cnb)
- [Understanding the self-service dashboard reports](#topic_j14_fqt_cnb)
- [Filtering the reports for specific scenarios](#topic_bz4_cvm_dfc)

Related articles:

- [Metrics and attributes for Zendesk Knowledge](https://support.zendesk.com/hc/en-us/articles/4409155064090)
- [Enabling anonymous user tracking for your help center](https://support.zendesk.com/hc/en-us/articles/6297027870618)

## Accessing the self-service dashboard

Use the following procedure to access the self-service dashboard.

**To access the self-service dashboard**

1. Click the **Zendesk Products** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/products_icon2.png)) in the top bar, then select **Analytics**.
2. From the list of dashboards, select the **Zendesk Knowledge** dashboard.
3. Click the **Self-service** tab.

## Understanding the self-service dashboard reports

The Self-service dashboard shows information about page views and user sessions. You can filter the reports on the dashboard by **Time**, **Brand**, **Visitor role**, **Language**, and **Sessions with search**.

As of April 4, 2025, the self-service datasets have been filtered to show only events that originate from the help center. Prior to this date, there were some events from other sources, such as Agent Workspace that were included in the following data:

- Page views (articles and community posts)
- Searches
- Quick answers

Depending on your usage of other channels, the inclusion of these additional events might impact session duration, page view duration, and number of sessions and visitors.

Data for end users and anonymous users were impacted less by this exception, so filtering for end-user and anonymous user traffic prior to the date above will give you more accurate data.

Important: By default, these datasets track only authenticated users, meaning users who are signed into their Zendesk account. If you want to track anonymous user activity, see [Enabling anonymous user tracking for your help center](https://support.zendesk.com/hc/en-us/articles/6297027870618).

### Self-service dashboard headline metrics

This tab displays the following headline metrics (KPIs) for the time range you specify:

- **Self-service ratio:** The number of sessions per ticket created in the help center.
- **Confirmed deflections:** The number of tickets that were deflected based on an article suggested on the help center request form.
- **Assumed deflections:** The number of times a visitor visits your help center and does not submit a ticket.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_users_sessions_1.png)

- **Sessions:** The total number of visits during the date range you specified. A session is defined as a period in which a user interacts with your help center. This might include multiple page views, events, and other interactions that occur in a single visit. Think of it as the time between when they open your help center page until they close it. A session consists of one or more of the following events:
 - Page views:
    - Article views
    - Community post views
 - Searches
 - Suggested article clicked from the request form
 - Tickets submitted by the user
 - A [quick answer search](https://support.zendesk.com/hc/en-us/articles/8888178335898) result shown

 A user session is limited to 100 of these events or a 30 minute timeout, whichever happens first. For sessions that reach the event limit, a new session will only start after the user has gone inactive for 30 minutes.

 Tip: The visitors metric is a count of unique visitors across the filtered parameters in a report. The session metrics are a count of the number of sessions attributed to those visitors. To get an idea of overall user traffic, the session metrics should be used. The visitors metric is intended to count the unique users who have visited your help center.
- **Page views:** The total number of page views. A page view is defined as an instance of an article or community post being loaded or reloaded in the visitor's web browser. Each time the visitor revisits or reloads the page, it's counted as an additional page view.
- **Avg session duration:** The average length of each session.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_users_sessions_4.png)

- **Visitors:** The number of unique visitors to your help center.
- **Sessions per visitor:** The average number of sessions per unique visitor.
- **Bounce rate:** The percentage of sessions where the user did not view any pages (articles or community posts).
- **Search exits:** The number of sessions that ended on the search results page.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_users_sessions_3.png)

The results from the self-service datasets and the other Knowledge datasets might differ due to the nature of how a session is defined as well as the ability for users to control if and how they’re tracked. This includes factors such as:

- Anonymous users will not be tracked if [anonymous user tracking](../setting-up-your-help-center/enabling-anonymous-user-tracking-for-your-help-center.md) is not implemented or has been opted out of by the user.
- Session events are not registered after a session has reached the 100 event limit. That visitor will only register new events when their next session begins.

This dataset is meant to provide insights into users session outcomes and overall content performance while not being a complete audit of all user interactions.

### Self-service dashboard reports

This tab displays the following reports for the time range and filters you specify:

- **Ticket deflections:** Displays the number of confirmed and assumed ticket deflections over the date range you specify.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_users_sessions_2.png)
- **Self-service ratio over time:** Displays the ratio of tickets to help center sessions, allowing you to measure the efficacy of your available help center content. This report displays your self-service ratio over the date range you specify.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_users_sessions_5.png)
- **Page views over time:** Displays page views and community post views over the date range you specify. Additionally, a line graph shows the average page views per session.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_users_sessions_6.png)
- **Sessions, visitors, and page views:** A combined report showing the number of sessions, visitors, and page views over the date range you specify.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_users_sessions_7.png)
- **Sessions with search:** Displays the percentage of sessions in which the visitor performed no search, a standard search, or a quick answer session.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_users_sessions_8.png)
- **Sessions by role:** Displays a pie chart showing the percentage of sessions for each user role over the date range you specify.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_users_sessions_9.png)
- **Sessions by language:** Displays a bar chart showing the number of sessions in each language over the date range you specify.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_users_sessions_10.png)
- **Deflection drill-down:** Displays a detailed report showing each article that was viewed together with the article author, the average time that visitors spent on the page, and deflections.

 You can filter this report by article section, article category, or community topic title.
 In addition, the brand, visitor role, and language filters at the top of the dashboard also apply to the deflection drill-down report.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_users_sessions_11.png)

## Filtering the reports for specific scenarios

The following topics provide useful information about how you can filter the reports to get the information you need.

### Filtering reports by brand

If a user visits multiple help centers under a given account, this will be tracked across separate sessions. This allows for the analysis of a specific help center’s performance, but you can filter for multiple, related brands on the dashboard if you want to get an overall picture of help centers which you are cross-referencing in your documentation.

### Filtering by article and community posts

To optimize the display of combined article and community post results in Explore, the titles and ids of both community posts and articles have been combined to provide combined page attributes such as title. In reports where you are exposing a community post and article id in a combined report, the community post id will be NULL or blank if the item is an article, and the article id will be NULL or blank when the item is a community post. To filter for only community posts or articles, use the Page type attribute.