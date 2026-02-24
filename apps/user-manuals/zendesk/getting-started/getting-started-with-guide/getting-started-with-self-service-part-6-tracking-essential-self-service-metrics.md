# Getting started with self-service - Part 6: Tracking essential self-service metrics

Source: https://support.zendesk.com/hc/en-us/articles/4408894139930-Getting-started-with-self-service-Part-6-Tracking-essential-self-service-metrics

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Articles in the series

- [Introduction: Elements of a self-service channel](https://support.zendesk.com/hc/en-us/articles/4408885576346)
- [Part 1: Planning your self-service content project](https://support.zendesk.com/hc/en-us/articles/4408886455578)
- [Part 2: Planning your self-service content structure](https://support.zendesk.com/hc/en-us/articles/4408883389338)
- [Part 3: Determining what articles you need to create](https://support.zendesk.com/hc/en-us/articles/4408894140826)
- [Part 4: Writing your knowledge base articles](https://support.zendesk.com/hc/en-us/articles/4408887322522)
- [Part 5: Launching your help center](https://support.zendesk.com/hc/en-us/articles/4408885574298)
- [Part 6: Tracking essential self-service metrics](https://support.zendesk.com/hc/en-us/articles/4408894139930)
- [Part 7: Maintaining and improving your knowledge base](https://support.zendesk.com/hc/en-us/articles/4408882663194)

With your help center live (see [Getting started with self-service - Part 6: Launching your help center](https://support.zendesk.com/hc/en-us/articles/4408885574298)), you should now start tracking the key self-service metrics that will help you determine how your help center is being used, how useful your articles are, and how you’re doing delivering self-service.

This article covers the following topics:

- [Calculating your self-service score](#topic_hz2_nhd_jmb)
- [Connecting Google Analytics to your help center](#topic_gfb_tsj_x4b)
- [Using the help center activity dashboards](#topic_lff_zsj_x4b)

## Calculating your self-service score

The success of your help center can be measured in a number of ways. You of course want to monitor the uptake in the use of your help center; how many views and users you’re getting per month. You should see an increase based on your efforts to promote your new self-service channel.

You can also compare your number of help center users to the number of tickets that were created in the same period of time. This is referred to as the *self-service score* (it’s also known as the *self-service ratio* and the *ticket deflection ratio*).

Self-service score = Total user sessions of your help center(s) / Total users in tickets

This formula gives you a ratio such as 4:1, meaning that for every four customers who attempt to solve their own issues using self-service, one customer submits a support request. Success here is demonstrated by an increasingly large ratio (for example, for every 40 users only one of them submits a ticket - 40:1 ratio).

**To calculate your self-service score**

1. Set up Google Analytics for your help center as described in [Enabling Google Analytics for your help center](https://support.zendesk.com/hc/en-us/articles/4408828643098).
2. When you have several months of user activity available in Google Analytics, take a 30-day snapshot (for example) of the number of visitor sessions in your help center.
3. Divide that number by the total number of users who have submitted tickets in that same time period. See [Explore recipe: Finding how many users submit tickets each month](https://support.zendesk.com/hc/en-us/articles/4408819207706).

## Connecting Google Analytics to your help center

Your help center is like any other website in that you want to measure, in as much detail as possible, how it’s being used and where it needs to be improved. After you’ve [enabled Google Analytics for your help center](https://support.zendesk.com/hc/en-us/articles/4408828643098), you can begin to analyze traffic, user engagement, and other typical website metrics. Google Analytics is a third-party, non-Zendesk service.

Some of the metrics that you can consider tracking in Google Analytics include the following:

- **Users** - Aside from helping you calculate your self-service score, the users metric also shows you the pages your visitors are accessing during their sessions, which gives you a fuller picture of how they’re engaging with your content.
- **Avg. Session Duration** - A low average session duration may indicate that your visitors are not engaging with your content.
- **% New Sessions** - This metric gives you insight into how many of your visitors are returning or new, which can help you determine the type of content you need to focus on (for example, providing more getting started content for new users).
- **Bounce Rate** - A high bounce rate on your landing pages (category and section pages with the listings of your articles) could indicate that you either aren’t providing the content they need or that your article titles need to be improved.

## Using the help center activity dashboards

Help center activity is tracked and available in prebuilt dashboards. Activity is tracked for your knowledge base articles, search, Knowledge activity, and your community (if enabled).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_guide_db_tabs.png)

The data you’ll find in these three dashboards help you to analyze and improve how your help center and your content is performing. While all the data is interesting and important, several of them are good indicators that you need to make changes to your knowledge base content.

### Knowledge Base activity

Statistics on this dashboard include the number of articles created, article views, and the total number of votes, subscriptions, and comments. Of these, article views, votes, and comments are of particular importance.

- **Views** is the total number of views for articles in the knowledge base. You want to track this over time and see an increase in views. This can indicate how well you’re doing promoting and driving the use of your help center and knowledge base articles.
- **Net article votes** is the difference of all the positive and negative votes on all articles. If you’re getting a high number of negative votes on your articles, that could indicate that they need to be updated and improved. On the other hand, a high number of positive votes indicates that an article is useful and is helping to deflect tickets.

- **Comments** is the total number of comments on articles in the knowledge base. An article with many comments can indicate that the content is confusing or incomplete and requires your customers to ask follow-up questions.

For more information about this dashboard, see [Analyzing knowledge base activity](https://support.zendesk.com/hc/en-us/articles/4408830631962).

### Search activity

Statistics on this dashboard include the total number of searches, searches with no results, searches with no clicks, and tickets created. The last three are particularly interesting because they indicate where you may have content gaps and that some articles are not getting the job done.

- **With no result** is the number of searches that returned 0 results. What this tells you is that your customers are searching for something that is not included in your knowledge base. The search strings that are being used could be nonsense, therefore no results, or you need a new knowledge base article to provide the information they are looking for.
- **With no clicks** is the number of searches where no result was selected. This might indicate a content gap (they searched for something, but nothing was available)
 or that you need to update the titles of your knowledge base articles (the article is there, but the title doesn’t contain the search term they’re using).
- **Tickets created** is the number of searches that led to a ticket being created.
 Drilling down into the detail for this statistic, you can see each search term used that resulted in a ticket being created. Two things could likely be happening here.
 First, they searched for a term that had to result, so the customer immediately created a ticket to get the answer they needed. Second, they clicked into an article and for some reason needed more help from an agent, which might mean the article needs to add more information.

For each of these statistics, you can see the search strings that are being used. You might find that customers are using alternate terms (an old product name, the term one of your competitor’s uses for something you have a different name for) and common misspelled words. This is where using labels comes in very handy. You can add these alternate terms and misspellings as labels in your articles to improve the search results for your customers.

For more information about this dashboard, see [Analyzing help center search results](https://support.zendesk.com/hc/en-us/articles/4408818465562)

### Knowledge activity

If you’re using Knowledge in the Context panel to create articles and enable your agents to link straight to your knowledge base content, reporting about its use is also available.

For more information about this dashboard, see [Analyzing your Knowledge activity](https://support.zendesk.com/hc/en-us/articles/4408887529370).

### Community activity

Statistics on this dashboard include the number of posts created, how many users have viewed posts, and the total number of votes, subscriptions, and comments.

Because your community is there to also provide you with feedback, a community post could be telling you that you need to create a knowledge base article to address the subject.

For more information about this dashboard, see [Analyzing community activity](https://support.zendesk.com/hc/en-us/articles/4604030850842).