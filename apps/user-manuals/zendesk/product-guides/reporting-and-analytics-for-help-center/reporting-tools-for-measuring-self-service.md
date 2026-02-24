# Reporting tools for measuring self-service

Source: https://support.zendesk.com/hc/en-us/articles/4408832867226-Reporting-tools-for-measuring-self-service

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

When you create a help center for your customers, you’re providing them with a self-service
channel to solve their own problems instead of opening tickets. This helps you scale your
customer support organization because self-service can result in fewer requests for agents to
handle, known as *ticket deflection*.

This article introduces the tools and metrics that work together to measure the effectiveness
of your self-service channel.

This article contains the following topics:

- [Analyzing knowledge base engagement metrics](#topic_v3b_zfd_v3)
- [Analyzing search engagement metrics](#topic_uft_zrw_plb)
- [Monitoring help center traffic and activity with Google Analytics](#topic_uv2_331_53)
- [Calculating your self-service score](#topic_p22_sw2_2db)
- [Analyzing Knowledge activity for knowledge base content and solved tickets](#topic_5t2_k1n_ldb)
- [Analyzing automated ticket resolution via autoreplies with articles](#topic_hpx_51n_ldb)
- [A summary of your self-service channel reporting options](#topic_czm_dbn_ldb)

## Analyzing knowledge base engagement metrics

Analyzing knowledge base activity begins in the Knowledge Base dashboard in Explore. In
this dashboard, administrators can measure essential engagement metrics for the knowledge
base.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_guide_kb_dashboard_overall_updated.png)

For more information, see [Analyzing knowledge base activity with Explore](https://support.zendesk.com/hc/en-us/articles/4408830631962).

## Analyzing search engagement metrics

If your customers can’t find the information they’re looking for in your help center, your
self-service channel will be of little help to them. The Search dashboard in Explore is
where you’ll find metrics that help you track what your customers are searching for and what
actions they take after searching.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_guide_dashboard_search_tab_overview.png)

For more information, see [Analyzing help center search results with Explore](https://support.zendesk.com/hc/en-us/articles/4408818465562).

## Monitoring help center traffic and activity with Google Analytics

Just as with any other website, you can monitor and analyze the traffic and activity in
your help center using Google Analytics. Google Analytics provides industry-standard metrics
for website traffic, user activity, and user engagement. When used with the Knowledge Base
dashboard in Explore, which gives you a snapshot of essential activity data, Google
Analytics helps you to dig much deeper into important user activity and engagement
metrics.

Although these metrics can’t tell you how many tickets have been deflected by using your
help center, they do provide you with a comprehensive understanding of the use and
effectiveness of the content in your help center.

To get started, [set up Google Analytics for help center](https://support.zendesk.com/hc/en-us/articles/4408828643098). Then you
can track your help center activity in your Google Analytics account.

After you set up Google Analytics and have some data to work with (gathered over several
months, for example), begin looking at the key metrics, including:

- **Page views**: This is the number of page views in your help center. You can track
  views in both Google Analytics and the Knowledge Base dashboard in Explore.
- **Unique page views**: This is the number of unique visitors to your help center.
  Each visit to your help center counts as a session, and each session (usually) results
  in multiple page views. Tracking the number of users visiting your help center gives you
  some perspective about its use compared to the total number of views in a specified
  period. A monthly views total of 10,000 compared to 1000 unique users within that same
  period tells you that those users are viewing, on average, 10 pages per session. This
  helps you understand how many of your customers use your self-service content.
- **% New Sessions**: Understanding how many new versus returning users visit your
  help center helps you focus on the content that addresses the needs of those users. For
  example, rolling out a new product may result in a spike of new users, which you can
  address by providing the information needed to use the new product.
- **Average session duration**: The average duration of a user session in your help
  center tells you how much time they spend in your help center and, if you drill down
  deeper, how much time they spend reading specific articles and FAQs. Ideally, they spend
  enough time to read through the information you provided them. If they don’t, that tells
  you something as well—that perhaps your content isn't engaging or isn't the information
  they need.
- **Pages per session**: This is the average number of pages viewed during a session
  on your help center. Once again, this tells you how much of your self-service content is
  being used.
- **Bounce rate**: This is the percentage of single-page sessions in your help
  center. A bounce means that the customer left your help center after viewing the first
  page they landed on. A user may have visited the help center unintentionally, or didn’t
  like what they saw when they got there.

With Google Analytics, you can also analyze what users are searching for and what actions
they take after those
searches.

## Calculating your self-service score

To begin more directly quantifying the effectiveness of your help center as a self-service
channel, and its impact on ticket deflection, you may want to determine what your
*self-service score* is. This metric, also known as the self-service ratio, is a
manual calculation you can make using this formula:

*Self-service score = Total user sessions of your help center(s) / Total users in
tickets*

This gives you a ratio such as 4:1, meaning that for every four customers who attempt to
solve their own issues using self-service, one customer submits a support request.

Note: To
calculate your self service score, you need a Google Analytics account plus the
Professional or Enterprise versions of Zendesk Support with Zendesk Explore Professional
enabled (you can run limited reports using the prebuilt dashboards in Explore Lite, see
[Activating Zendesk Explore](https://support.zendesk.com/hc/en-us/articles/4799941569690).

**To calculate your self-service score**

1. Set up a Google Analytics account and connect it to help center as described in [Enabling Google Analytics for your help center](https://support.zendesk.com/hc/en-us/articles/4408828643098).
2. When you have several months of user activity available in Google Analytics, take a
   30-day snapshot (for example) of the number of visitor sessions in your help
   center.
3. Divide that number by the total number of users who have submitted tickets in that
   same time period. See [Explore recipe: Finding how many users submit tickets each
   month](https://support.zendesk.com/hc/en-us/articles/4408819207706).

When making this calculation, you may also want to define what you consider to be active
use of your help center in an attempt to self-serve. In [6 steps for measuring self-service success](https://www.zendesk.com/blog/measuring-self-service-success/), Erin Cochran of
RJMetrics says, “We defined ‘content interaction’ as someone who did more than just visit
the help center landing page or navigate straight to a new ticket form. This allowed us to
get a better idea of how many visitors were actually trying to self-serve before submitting
a ticket.” Erin shares other useful tips for evaluating self-service in her article—give it
a look.

## Analyzing Knowledge activity for knowledge base content and solved tickets

Knowledge in the context panel enables agents to easily share and direct customers to
knowledge base content to help customers solve their support issues themselves.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/knowledge_panel_search.png)

There’s manual intervention needed here because agents add the links to knowledge base
content into their replies to customers, but you can then track whether the linked content
helped the user solve their own ticket. Tickets aren’t deflected in this case, but their
resolution may be the result of the use of your self-service channel.

For more information, see [Analyzing your Knowledge or Knowledge Capture app activity](https://support.zendesk.com/hc/en-us/articles/4408887529370).

## Analyzing automated ticket resolution via autoreplies with articles

The autoreplies with articles feature uses machine learning to scan the text of incoming
support requests and then automatically responds to tickets with a list of relevant
knowledge base articles that may help your customers resolve their issues without having to
interact with an agent.

Like Knowledge in the context panel, you can view analytics for autoreplies with articles
activity in Explore. Most importantly, you can see how many tickets were solved using your
knowledge base articles.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ab_120.png)

This includes overall performance (how many times the links resolve tickets), and also the
performance of individual articles (which articles are the best and worst at helping
customers solve their problems).

For more information, see [Analyzing article recommendations](https://support.zendesk.com/hc/en-us/articles/4409155069466).

## A summary of your self-service channel reporting options

Here’s a quick overview of the metrics we just described and what products and tools you
need to report on them.

| Reporting tool | Location of reports |
| --- | --- |
| Knowledge Base dashboard | [Knowledge Base dashboard in Explore](https://support.zendesk.com/hc/en-us/articles/4408830631962) |
| Search dashboard | [Search dashboard in Explore](https://support.zendesk.com/hc/en-us/articles/4408818465562) |
| Google Analytics | Google Analytics dashboard |
| Knowledge Capture dashboard | [Knowledge Capture dashboard in Explore](https://support.zendesk.com/hc/en-us/articles/4408887529370) |
| Article Recommendations dashboard | [Article Recommendations dashboard in Explore](https://support.zendesk.com/hc/en-us/articles/4408887529370) |