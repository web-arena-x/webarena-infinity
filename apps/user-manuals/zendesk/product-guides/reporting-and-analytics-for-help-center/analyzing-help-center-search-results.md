# Analyzing help center search results

Source: https://support.zendesk.com/hc/en-us/articles/4408818465562-Analyzing-help-center-search-results

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Zendesk features a prebuilt Search dashboard that helps you understand how your customers interact with your help center, including what they’re searching for and how successfully they find answers. It helps you identify topics that interest customers most, and also helps you detect gaps in your knowledge base that need to be addressed.

In the following topics, you'll learn how to access the search analytics dashboard and see the available reports:

- [Accessing the Search dashboard](#topic_px1_qns_dcc)
- [Understanding the Search dashboard reports](#topic_rcq_5ns_dcc)

Tip: You can edit and customise the Search dashboard by cloning it (see [Cloning dashboards](https://support.zendesk.com/hc/en-us/articles/4408821374362)). If you need something more complex, you can write your own reports using a wide range of metrics and attributes. For details, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530).

The information in the Search dashboard is updated on a schedule. The schedule depends on which plan you are on. For details, see [Data refresh intervals for analytics](https://support.zendesk.com/hc/en-us/articles/4408823242778).

## Accessing the Search dashboard

Use the following procedure to access the Search dashboard.

**To access the Search dashboard**

1. Click the **Zendesk Products** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/products_icon2.png)) in the top bar, then select **Analytics**.
2. From the list of dashboards, select the **Zendesk Knowledge** dashboard.
3. Click the **Search** tab.

## Understanding the Search dashboard reports

The Search dashboard shows information about searches, click-through rate, tickets created, and more. You can filter the reports on the dashboard by **Time**, **Brand**, **Search channel**, **User role**, and **Locale**.

Note: The dashboard excludes any click or search events that have a blank **Search query** attribute value. This prevents [content tag](https://support.zendesk.com/hc/en-us/articles/4848925672730) data from appearing on this dashboard.

Using the dashboard, you can slice and filter the search metrics to get a detailed picture of your help center’s performance, including:

- **The most common queries your customers search for**: Track search queries by brands, user types, and locales.
- **Where users perform their searches**: Track whether searches are performed directly in the help center or via the Mobile SDK or Web Widget.
- **Where you can improve your self-service performance**: Track the number of results and click-through rate by searches to identify whether customers find what they’re looking for.
- **How search volume affects ticket creation**: Track the number of searches and the number of tickets created and detect possible correlations.

Note: The dashboard shows data for up to 390 days in the past due to the retention period of the [Search dataset](https://support.zendesk.com/hc/en-us/articles/4409155064090#topic_anj_4gj_nrb).

### Search dashboard headline metrics

This tab displays the following headline metrics (KPIs) for the time range you specify:

- **Total searches**: The total number of searches that users performed in your knowledge base.
- **Searches with no results**: The total number of searches that users performed that returned no results.
- **Avg click-through rate**: The number of results clicked on divided by the number of searches performed.
- **Tickets created**: The total number of tickets created in the help center.

![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_search_dashboard_KPIs.png)

### Search dashboard reports

This tab displays the following reports for the time range and data filters you specify:

- **Searches by results and clicks (last 7 days):** Displays a pie chart with the total number of searches performed, broken down by searches with clicks, searches with no results, and searches with no clicks.

 ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_search_by_results_and_clicks.png)

- **Searches by user role:** Displays a pie chart with the total number of searches, broken down by the role of the user who performed the search.

 ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_search_by_user_role.png)
- **Searches with no results (top 5):** Displays a bar chart with the top 5 most searched-for strings that returned no results. ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_search_no_results.png)
- **Search effectiveness:** Displays a column chart with the total searches performed, broken down to searches with results and searches without results. On top of the bars, the line chart shows the average click-through rate over time.

 ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_search_effectiveness.png)
- **Ticket to search ratio:** Displays a column chart with the number of tickets created after search. The line chart shows the tickets created per search ratio over time.

 ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_search_ticket_search_ratio.png)
- **Search queries overview (last 30 days):** Displays a table with the strings that users searched for, including how many times a string was searched for, the average number of results it returned, the average click-through rate, and the number of tickets created after searching for that string.

 ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_search_queries_overview.png)

- **Search queries and top clicked articles:** Displays a table with the articles that were clicked on most often, including the string that users searched for to find the article, and the number of times the article was clicked.

 ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_search_queries_and_top_clicked_articles.png)