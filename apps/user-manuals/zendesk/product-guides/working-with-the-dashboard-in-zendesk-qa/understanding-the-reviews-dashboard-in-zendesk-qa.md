# Understanding the Reviews dashboard in Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/7043724913690-Understanding-the-Reviews-dashboard-in-Zendesk-QA

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

The Reviews dashboard helps you analyze your support team's performance by providing insights into quality scores, review times, and conversation metrics. Use it to track key performance indicators, understand category performance, and identify areas for improvement. The dashboard's detailed quality indicators allow you to monitor trends, assess reviewer and agent performance, and explore root causes, enhancing your quality assurance process.

Location:  Zendesk QA > Dashboard > Reviews

The Reviews dashboard in Zendesk Quality assurance (QA) includes all the data of
your manually submitted reviews and allows you to view a breakdown of your quality
results.

By accessing conversation data directly from the Reviews dashboard, you can gain
insights into your support team's performance. This article describes how to access, view, and
use the information on your Reviews dashboard. Its various quality indicators allow you to
monitor quality scores across categories, track metrics like average review times, and analyze
the quality of your customer interactions.

This article contains the following topics:

- [Overview of the Reviews dashboard
  (video)](#topic_n21_wsv_42c)
- [Understanding the quality indicators on the
  Reviews dashboard cards](#topic_cwx_3qw_42c)
- [Accessing the Reviews dashboard](#topic_qsl_bv5_s2c)

Related articles:

- [About dashboards in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043701144858)
- [About the Zendesk QA Reviews dashboard calculations](https://support.zendesk.com/hc/en-us/articles/7043701093786)

## Overview of the Reviews dashboard (video)

In addition to the details in this article, this video provides a helpful visual
overview of the Reviews dashboard.

## Understanding the quality indicators on the Reviews dashboard cards

The Reviews dashboard is separated into several cards that represent your main
key performance indicator (KPI) metrics.

You may want to use this information to determine your current quality score and how it's
changing over time. It can also help you understand if your review process is efficient and
reviews are being seen, how active your reviewers are, and more.

### Main Reviews dashboard cards

The following quality indicators represent your main KPI metrics displayed on
these cards:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_dashboards_reviews.png)

- [**Internal quality score (IQS)**](https://support.zendesk.com/hc/en-us/articles/7043701093786#topic_sws_4ww_42c): The average
  of all [review scores](https://support.zendesk.com/hc/en-us/articles/7043701093786#understanding_individual_review_scores) received or given over a period of
  time expressed as a percentage.
- **Reviews**: The number of [manually submitted reviews](https://support.zendesk.com/hc/en-us/articles/7043669307418).
- **[Pass rate](https://support.zendesk.com/hc/en-us/articles/7043668650266)**: The outcome of your
  conversation reviews, determined by a predefined baseline, for example, pass or fail.
- **Reviewed conversations**: The number of conversations that received one or more
  manual review.
- **Average review time**: The average time spent on a conversation before it was
  submitted for review.
- **Reviewed agents**: Number of users who received a manual review.
- **Disputed reviews**: Percentage of manual reviews that have a dispute.
- **Reviews with comments**: Percentage of manual reviews that have at least one
  comment.
- **Unseen reviews**: Percentage of manual reviews that have not yet been seen by
  reviewees. Bots are not included in the unseen reviews metric.

### Additional detailed quality indicators

Your Reviews page includes the following additional quality indicators
displayed in graphs and charts:

- [Quality scores over
  time](#topic_msk_dbv_s2c)
- [Category scores over
  time](#topic_osk_dbv_s2c)
- [Average category
  scores](#topic_qsk_dbv_s2c)
- [Category group performance and
  category insights](#topic_ssk_dbv_s2c)
- [Root causes and workspaces](#topic_usk_dbv_s2c)
- [Reviewer and reviewee
  performance](#topic_wsk_dbv_s2c)
- [Scores by category](#topic_ysk_dbv_s2c)
- [Review scores](#topic_atk_dbv_s2c)
- [Ratings and root causes by
  reviews](#topic_ctk_dbv_s2c)

#### Quality scores over time

Use the Quality scores over time card to understand the evolution of your quality
scores on a weekly basis. You can also view the number of reviews created to understand
trend reliability.

Click an aggregated score to drill down into the individual score.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_reviews_dashboard_quality_scores.png)

You may want to use this information to understand how strict reviewers are with their
ratings, how agents are performing, if there are any outliers that require calibration
sessions, and if any agents might require specific training.

#### Category scores over time

The [Category scores over time](https://support.zendesk.com/hc/en-us/articles/7043701093786#understanding_rating_categories) card displays the
evolution of quality ratings over time (in weeks), by categories. This card compares
categories to each other and does not reflect on your agents.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_reviews_dashboard_category_scores.png)

This information can help you understand how your categories are developing over time,
how many ratings are being given per category, and what specific dates did a category
dip or improve. Additionally, you can filter for a specific agent to view their
individual data.

#### Average category scores

The category chart display which categories have scores above 80% and which have 0%
scores.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_reviews_dashboard_average_category_scores.png)

Category score cards provide an overview of which categories are above an 80% score and
which are below.

Use these cards to understand how your categories are performing. You can view this
information to understand the distribution of scores across categories and which
consistently fall short with 0% scores.

#### Category group performance

If your categories are grouped, you can quickly compare the score per category group
with this card. It can help you understand your highest and lowest performing category
group and compare category group scores to the previous period.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_reviews_dashboard_category_performance_scores.png)

The Category insights card displays the combined average of all category
scores that are given or received. These insights can help you analyze which category
receives the highest and lowest quality scores and determine if training sessions are
needed for specific categories.

You can drill into all the numbers in the scorecard for a more granular view
and understand, for example, which agents are struggling the most with some category
performances, or which tickets contributed the most to those results.

You can also check how frequently a category has been disputed. This can help
ensure that agents and reviewers have a consistent understanding of what those
categories mean.

#### Root causes and workspaces

Here, you can view the number of times a root cause has been selected. You can also
click into it to see the list of conversations and agents that contributed to those root
causes.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_reviews_dashboard_rootcauses.png)

If you operate multiple workspaces, you can also compare their quality results.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_reviews_dashboard_workspaces.png)

#### Reviewer and reviewee performance

The Reviewer and Reviewee performance cards show a full overview of all your Zendesk QA
users and their individual KPIs.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_reviews_dashboard_reviewer_performance.png)

Use these cards to understand the number of reviews each user is receiving, who is
giving and receiving higher or lower scores in comparison to their peers, and how many
reviews are given per user.

This helps you measure trends over time.

You can also view the average review time for each reviewer. This can help you ensure
reviewers aren't simply rushing to complete reviews.

#### Scores by category

The scores by category card displays all your support agents along with their total
category scores and [scores for each scorecard category](https://support.zendesk.com/hc/en-us/articles/7043701093786).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_reviews_dashboard_scores_category.png)

The average per category highlights opportunities for improvement more explicitly than
the average per conversation.

You can sort the table to quickly understand which agents are struggling the most, or
where additional training or improving your knowledge management processes may be
required, without the need to manually review individual tickets.

#### Scores by reviews

The Scores by Reviews card displays conversation scores for each agent,
including the review ID, a link to the conversation in the help desk, comments provided,
and the review scores. You can filter these scores by reviewer or reviewee and sort the
table by date, review scores, pass rate, review time, visibility status (seen or unseen
by reviewees), number of disputes, assignment name, or comments.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_reviews_dashboard_scores_reviews.png)

When filtering for a specific agent, you can determine which conversations they
excelled at and where they can improve. This card can help you spot if there are any
outliers in conversations and how reviewers are rating specific conversations.

#### Ratings and root causes by reviews

Similar to the Scores by reviews card, the Ratings and root causes by reviews
card provides a breakdown of scores for each conversation. It offers an additional level
of detail by breaking down scores for each category and root cause.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_Ratings_and_root_causes_by_reviews.png)

## Accessing the Reviews dashboard

**To access the Reviews dashboard**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Dashboards**
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_dashboard_icon.png) in the sidebar.
2. From the list of dashboards, select **Reviews**.
3. (Optional) Use filters to narrow down the data based on specific criteria. See [Filtering the Reviews dashboard](https://support.zendesk.com/hc/en-us/articles/7043701144858).
4. (Optional) Use the [Display menu](https://support.zendesk.com/hc/en-us/articles/7043701144858#topic_xlj_yjx_vfc) (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_view_icon.png)) in the top right corner to select
   which cards to display or hide on your dashboard.
5. (Optional) You can drill down into the following additional data points:

- Rating scores
- Reviews
- Conversations
- Categories
- Root causes

If a conversation has more than one review, you can have more rows in the drill-down than
the number of unique conversations. For example, the Reviewed conversations card displays
how many conversations were reviewed. However, in the drill-down, you can access all reviews
completed for each agent in that conversation.

See [Accessing additional data points](https://support.zendesk.com/hc/en-us/articles/7043701144858#topic_hng_tlx_vfc).