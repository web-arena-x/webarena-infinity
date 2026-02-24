# Analyzing your autoreplies with articles (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4409155069466-Analyzing-your-autoreplies-with-articles-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

As of July 31, 2025, the autoreplies with articles feature is considered legacy functionality. Instead, [use AI agents](https://support.zendesk.com/hc/en-us/articles/6478272212506) to deliver generative AI-powered responses on messaging, email, and web form channels.

Zendesk Explore includes the Article recommendations prebuilt dashboard, which helps you monitor the acitivity and effectiveness of your autoreplies with articles in [email notifications](https://support.zendesk.com/hc/en-us/articles/4408833721498) and [web forms](https://support.zendesk.com/hc/en-us/articles/4408820951450). The dashboard can help you identify whether autoreplies with articles are solving your support requests, how quickly users are opening suggested articles, and how your individual articles are performing.

To edit and customize the dashboard, you'll first need to [clone it](https://support.zendesk.com/hc/en-us/articles/4408821374362).

Tip: If you need more complex reports, you can write your own using a wide range of metrics and attributes. For details, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530).

The information in Explore dashboards is updated on a schedule. The schedule depends on which Explore plan you are using. For details, see [Data refresh intervals for Explore plans](https://support.zendesk.com/hc/en-us/articles/4408823242778).

This article contains the following sections:

- [Accessing the Article recommendations dashboard](#topic_esj_ggj_nlb)
- [Understanding the Article recommendations dashboard reports](#topic_hsj_ggj_nlb)

Related article:

- [Improving autoreply metrics for article recommendations](https://support.zendesk.com/hc/en-us/articles/4408889123610)

## Accessing the Article recommendations dashboard

The Article recommendations dashboard provides information about your use of autoreplies with articles.

**To access the Article recommendations dashboard**

1. In Zendesk Support, open the [product tray](https://support.zendesk.com/hc/en-us/articles/4408838272410).
2. From the list of products, click **Analytics**.
   Explore opens and displays the dashboard library.
3. From the list of dashboards, click the **Zendesk Answer Bot** dashboard.
4. In the Zendesk Answer Bot dashboard, click the **Article recommendations** tab.

   Note: If you have not set up autoreplies with articles, then this tab won't be displayed.

## Understanding the Article recommendations dashboard reports

The Article recommendations dashboard shows information about autoreply activity, ticket resolutions, and activity by articles. You can filter the reports on the dashboard by **Time**, **Answer channel**, **Answer brand**, **Article language**, **Ticket group**, and **Ticket form**.

Note: The Article recommendations reports do not include data from the messaging channel.

### Article recommendations dashboard headline metrics

The dashboard displays the following headline metrics (KPIs):

- **Suggestion rate:** Displays the percentage of customer inquiries where an autoreply with articles was sent. The KPI also displays the number of answers, attempts made, and unsuccessful attempts. For tips on improving the suggestion rate, click **Improve**.
- **Click-through rate:** Displays the percentage of responses clicked by end users from the total responses offered. The KPI also displays the number of clicks, clicked articles, and the median click time. Click the **Improve** link to get tips about how to improve the click-through rate.
- **Resolution rate:** Displays the percentage of inquiries that are resolved with no agent involvement. The KPI also displays the number of resolutions, indirect resolution answers, and the median resolution time.
 Click the **Improve** link to get tips about how to improve the resolution rate.
- **Rejection rate:** Displays the percentage of suggested articles marked as unhelpful by end users from the total number of suggestions offered. The KPI also displays the number of articles marked unhelpful. Click the **Decrease** link to get tips about how to improve the rejection rate.

![Explore Guide KPIs](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ab_120.png)

### Article recommendations dashboard reports

The dashboard displays the following reports:

- **Answer Bot activity volumes by date:** Shows the number of offered, clicked, and resolved bot answers and resolutions over the chosen time period.

 ![Answer Bot activity volumes by date report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ab_121.png)
- **Answer Bot activity rates by date:** The percentage of answers clicked, rejected, or resolved over the selected time period.

 ![Answer Bot activity rates by date report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ab_122.png)
- **Resolutions by month (12 month):** The number of resolutions and the percentage resolution rate over a 12 month period.

 ![Resolutions by month report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ab_123.png)
- The following reports can be filtered by clicking the tabs at the top of the section: Answer channel, Answer brand, or Suggested article language.

 ![Answer Bot report filters](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ab_124.png)
 - **Answers by selected attribute (top 10):** Displays the top ten offered answers by channel, brand, or language.

    ![Answers by selected attributes report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ab_125.png)
- **Clicks and resolutions by selected attribute (top 10):** Displays the top ten resolutions and clicks by channel, brand, or language.

 ![Clicks and resolutions by selected attributes report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ab_126.png)
- **Resolutions by selected attribute (12 months):** Displays the resolutions over the last 12 months sorted by language, brand, or channel.

 ![Resolutions by selected attribute report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ab_127.png)
- **Answer Bot activity by article:** A detailed report about activity for all of your Guide articles. You can restrict the range of results shown by using the **Top** and **Bottom** filters. The table contains the following information for each article that is offered:
 - **Article author:** The author of each article
 - **Suggested articles:** The number of times each article was suggested
 - **Clicked articles:** The number of times each article suggested was clicked
 - **Resolution articles:** The number of tickets for each article that were solved by a suggestion
 - **Rejected articles:** The number of times a suggestion for each article was rejected by an end user
 - **Resolutions/Clicks:** The percentage of resolutions from clicked answers for each article.
    It is possible for this number to be over 100% as you can resolve an answer from the initial suggestion without clicking into it.

 ![Answer Bot activity by article report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ab_128.png)