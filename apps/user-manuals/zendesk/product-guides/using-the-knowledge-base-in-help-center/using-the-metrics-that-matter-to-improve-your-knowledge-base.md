# Using the metrics that matter to improve your knowledge base

Source: https://support.zendesk.com/hc/en-us/articles/4408838548250-Using-the-metrics-that-matter-to-improve-your-knowledge-base

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Support teams know the most about customer issues and the best way to solve
them. That’s why a knowledge base is a crucial part of your customer experience
strategy. It organizes frequently asked questions, product details, policies, and more,
and empowers customers and agents with that information. Integrated seamlessly with your
ticketing system is a smart help center. It’s built to help you and your team
continuously improve your content, keep it up to date, and serve it to customers before
you can say “FAQ”! A great knowledge base means your customers are happy because they
get help faster without having to contact you. This leads to a faster and more efficient
service operation for you and your agents.

However, this leads to the question "How do I know if my knowledge base is
doing its job?"

That question has different answers depending on your business and your
customers. In this article, you'll learn some useful tips to help you measure the
effectiveness of your knowledge base. You'll find that Zendesk includes a bunch of tools
to help you analyze your knowledge base, but you'll also learn about other tools you can
additionally use to get even more information.

Important: Zendesk and third-party products are constantly evolving and
we’ll keep this article up-to-date as things change. Make sure to hit the
**Follow** button at the top of this page to be the first to know when we
make updates.

This article contains the following sections:

- [Is anyone looking at your articles?](#topic_bqr_qgh_knb)
- [What are your readers searching for?](#topic_hm5_vct_vnb)
- [Calculating your self-service score](#topic_vjq_3hh_knb)
- [Understanding article votes](#topic_x2v_nhh_knb)
- [Using autoreplies to analyze article performance](#topic_rqf_mnt_v4b)
- [More tools and resources to help you monitor your knowledge base](#topic_g4z_1xp_b4b)
- [Join the conversation](#topic_cws_nb2_snb)

## Is anyone looking at your articles?

A *pageview* is a count of how many times your page has been viewed in
a web browser. Page views are a useful indicator that people are using your
knowledge base. You can use them to show which articles your users are most
interested in, help find out if your pages are optimized for search engines, and to
help you understand user behaviors.

**Advantages of monitoring pageviews**

- Shows that people are actually using your knowledge base.
- Gives an indication about which of your articles are the most
  popular.
- Collecting pageviews over time can give you a good trend as to how
  your articles are performing over time.

**Disadvantages of monitoring pageviews**

- A pageview doesn't indicate whether the reader found what they needed
  in your article.

Always monitor page views in conjunction with other monitoring methods to
ensure you have a complete picture of your team's success and areas where you could
improve.

### Examining page views with Explore

Explore currently tracks all pageviews to your articles including
repeat visits. If you want to track only unique visitors, you'll need to use
Google Analytics.

In this section, you'll learn how to create a quick count of all of
your pageviews using Explore.

**To create a pageview report using Explore**

1. In Explore, click the reports ( ![](https://lh6.googleusercontent.com/PmrDL9Y9-HVxU17Vtrv09G56M9sktLv2_0P74J570wGbXTyTKIcBloeC8shf1uBKEAB3m5cjnwKHzKg__B5yCw9w4eOdkBDDCM7ggnMlHItTd7onQGtt4K2PR7VrLC1E9_LhX2zw)) icon.
2. In the Reports library, click **New report**.
3. On the **Select a dataset** page, click **Knowledge** >
   **Knowledge - Knowledge Base**, then click **Start report**. The
   report builder opens.
4. In the **Metrics** panel, click **Add**.
5. From the list of metrics, choose **Article views** >
   **Views**, then click **Apply**. Explore displays the total number
   of article views in your knowledge base.
6. In the **Rows** panel, click **Add**.
7. From the list of attributes, choose **Article** > **Article
   translation title**, then click **Apply**. Explore displays a table
   showing the number of page views for each article in your knowledge base.
   Click the **Views** column header to sort the table into order by number
   of views.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_mm_2.png)

Tip: Usually, you'll want to look at page views over a period, like "Last month" rather
than over the whole life of the article. To do this, add a filter for
**Time - Article views recorded**. For help with Explore filters, see
[Filtering a report](https://support.zendesk.com/hc/en-us/articles/4408825475354).

### Examining page views with Google Analytics

[Google Analytics](https://support.zendesk.com/hc/en-us/articles/4408828643098) tracks both total
page views, and unique page views only. It also gives you an indication of how
long the visitor spent on your page. This can help you understand the level of
engagement visitors have with your content. Additionally, Google Analytics can
help you to understand some information from Zendesk Gather (though this
capability is on the roadmap for Explore).

## What are your readers searching for?

By understanding the terms that your customers search for on your site, you
can ensure that relevant content is returned when they search.

You use the search analytics dashboard to review the search words that
customers have entered in the help center search field. For each search term that's
been used, you can see the number of searches for that term, number and type of
search results returned (if any), click-through, and the next action taken.

**To open the search analytics dashboard**

- In Support, click the **Reporting** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/report_icon.png)) in the sidebar, then click
  the **Search** tab.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_reporting_with_channel.png)

For more information, see [Analyzing help center search results with Explore](https://support.zendesk.com/hc/en-us/articles/4408818465562).

### How to improve search results

End users generally search your knowledge base in one of two ways:

- From the search bar in your help center.
- From an internet search engine like Google or Bing.

The methods for optimizing content for search are similar both for your
help center search and search from a search engine like Google or Bing. You can
improve end-user search results by updating content in the following ways:

- Add labels to content (not available on Suite Team). You can add
  labels to content so that the appropriate content appears in search results.
  For example, if you see that end users are searching for "e-mail" but you
  use "email" without a dash in your content, add a label with the similar
  term to the content.

  You can test how well this works in your own help
  center. To get started and find information about optimizing your search
  results, see [About Help Center end user
  search](https://support.zendesk.com/hc/en-us/articles/4408894061338).
- Update content titles. You can rewrite titles to more closely
  match end-user searches. For example, if your article is titled "Deleting an
  email account" and end-users are searching for "removing a user from email,"
  consider updating the title.
- Break content into smaller articles. You can divide large articles
  into smaller articles to help customers find what they are looking for. For
  example, instead of "Managing email" consider smaller articles about
  "Setting up email", "Adding email accounts", and "Deleting email
  accounts".
- Update content body text. You can add common end-user search terms
  to the body of appropriate articles so that the article appears higher in
  search results.
- Remove old content so that it does not clutter search results and
  confuse your customers.
- Ensure content is available. If people are searching for an
  article in your knowledge base that doesn't exist, or if you see a high
  volume of tickets for a topic that’s not covered, write an article about
  it!

## Calculating your self-service score

One useful indicator of how well your knowledge base is doing is your
self-service score. This measures the number of unique visitors to your knowledge
base against the total number of users who've submitted support tickets.

Currently, Explore can't calculate your self-service score directly as you
can’t combine data from tickets and pageviews in the same report. In this example,
you'll calculate your self-service score over the last month.

**To calculate your self-service score**

1. In Explore, create a report using the Knowledge - Knowledge Base
   dataset. Add the **SUM(Views)** metric and a filter containing the attribute
   **Time - Article views recorded**. Ensure that the date range on your
   filter is configured for the past month.
2. Next, create a report using the Support - Tickets dataset. Add the
   **COUNT(Tickets)** metric and a filter containing the attribute **Ticket
   created - date**. Ensure that the date range on your filter matches the
   date range in your knowledge base report.
3. Divide the number of pageviews by the number of tickets created over
   the same time period to obtain your self-service score.

Continue to monitor your score over time to track improvements, or areas in
which you need to improve. For example, after you created a number of new articles,
did your self-service score improve?

## Understanding article votes

At the bottom of each of your articles, you'll find two voting buttons that let you
vote an article up or down. A number representing the difference between positive
and negative votes is displayed.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_mm_5.png)

If an article has more negative votes than positive votes, the number of
votes is shown as a negative value. Here are some things you can consider when an
article has negative votes:

- Read the article. Is it up to date? Check if any procedures still
  work.
- If you have commenting turned on, read the comments to see if there
  are any clues to what your readers don't like.
- If you wrote the article, consider asking another team member or even
  a customer to peer review the article.
- Try to discover what people don't like about the article. Maybe
  organize some customer meetings. Sometimes, you'll find that the article is
  fine, but customers have an issue with the product itself. In those cases, you
  can pass along that feedback to the relevant teams at your company.

### Reporting article votes with Explore

In this simple Explore example, you'll learn how to report the top ten articles
by the most votes.

Note: Explore only reports the current article votes. You can't report on the history of votes over
time.

**To create a report by votes**

1. In Explore, click the reports ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)) icon.
2. In the Reports library, click **New report**.
3. On the **Select a dataset** page, click **Knowledge** >
   **Knowledge - Knowledge Base**, then click **Start report**. The
   report builder opens.
4. In the **Metrics** panel, click **Add**.
5. From the list of metrics, choose **Article views** > **Article
   votes**, then click **Apply**. Explore displays the total number of
   votes across all of your articles.
6. In the **Rows** column, click **Add**.
7. From the list of attributes, choose **Article** > **Article title**,
   then click **Apply**. Explore displays a list of all of your articles
   together with the vote for each one.
8. Now, you'll restrict the results to only the ten most voted for articles. In
   the result manipulation menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_manipulation.png)), click **Top/bottom**.
9. In the **Top/bottom** panel, select **Top**, and set the value to
   **10**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_mm_6.png)
10. When you are finished, click **Apply**. Explore displays a table of your
    ten highest voted articles.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_mm_7.png)

## Using autoreplies to analyze article performance

Autoreplies suggest articles from your knowledge base to answer
customer questions without an agent ever becoming involved.

To get things up and running and learn how to optimize your content, see
[Quickstart guide:
Autoreplies](https://support.zendesk.com/hc/en-us/articles/4408820349850).

When you’re ready, Explore offers a prebuild
dashboard to help you understand how your articles are
performing.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ab_120.png)

See
[Analyzing your autoreplies for article
recommendations](https://support.zendesk.com/hc/en-us/articles/4409155069466).

## More tools and resources to help you monitor your knowledge base

In this section, you'll learn about other useful tools that will help you
measure the effectiveness of your knowledge base and the articles it contains. Some
of these are third-party tools so contact each company if you want more details:

- [Pendo](https://www.pendo.io/about/) gives you powerful usage analytics about your
  product and web pages. You can use Pendo to help understand the user's journey
  through your project which can help you to understand where you might need to
  write further usage assistance. It can also help you understand where your
  knowledge base visitors came from. Pendo has [an app](https://www.zendesk.com/apps/support/pendo/) that works with Zendesk to give you
  information right inside your Zendesk tickets.
- [Crazy Egg](https://www.crazyegg.com/): takes article analytics a step further by allowing you to
  see how readers interact with your page. For example, you can generate heat maps
  that show where readers spend the most time on your page, or click maps that
  show you where they click. A similar product to Crazy Egg is [Hotjar](https://www.hotjar.com/).
- We have a bunch of recipes to help you get started monitoring and
  improving both your knowledge base and your support operation in general. To get
  started, see [Explore recipes reference](https://support.zendesk.com/hc/en-us/articles/4409149172890).

## Join the conversation

What metrics do you use to help measure the success of your knowledge base? How have
you managed to improve them? Let us know in the comments below!