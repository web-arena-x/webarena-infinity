# Understanding the AutoQA dashboard in Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/9019507481242-Understanding-the-AutoQA-dashboard-in-Zendesk-QA

---

The AutoQA dashboard tracks team performance across all AutoQA categories. It monitors quality performance and agent scores over time, providing breakdowns by agent and category. This dashboard is ideal for monitoring trends and identifying the training needs of your teams.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

The AutoQA dashboard helps you monitor team performance and identify training needs by tracking quality performance and agent scores over time. It provides insights into metrics like auto-reviewed conversations, efficiency gain, and accuracy scores. You can also explore additional data points, such as category insights and root causes of errors, to enhance your team's support capabilities.

Location: Zendesk QA > Dashboard > AutoQA

The AutoQA dashboard tracks team performance across all AutoQA categories. It monitors quality performance and agent scores over time, providing breakdowns by agent and category. This dashboard is ideal for monitoring trends and identifying the training needs of your teams.

While manually submitted grades contribute to the agents’ [Internal Quality Score (IQS)](https://support.zendesk.com/hc/en-us/articles/7043724913690-Accessing-and-viewing-the-Reviews-dashboard#ariaid-title3), automated reviews are tracked using the Auto Quality Score (AQS).

This article contains the following topics:

- [Accessing the AutoQA dashboard](#topic_ezq_nmn_s2c)
- [Understanding the main AutoQA dashboard cards (with examples)](#topic_bwl_kpq_42c)
- [Understanding additional AutoQA dashboard cards](#topic_b4n_tpv_q2c)
- [Drilling down into AutoQA dashboard data](#topic_fvl_1xq_42c)

Related articles:

- [About dashboards in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043701144858)

## Accessing the AutoQA dashboard

The AutoQA dashboard tracks your teams’ performance across all [AutoQA categories](https://support.zendesk.com/hc/en-us/articles/7043747123354-Setting-up-autoscoring-in-Zendesk-QA-using-AutoQA#understanding-autoscoring-categories).

**To access the AutoQA dashboard**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Dashboards**
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_dashboard_icon.png) in the sidebar.
2. From the list of dashboards, select **AutoQA**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_dashboard_autoqa.png)

## Understanding the main AutoQA dashboard cards with examples

The following quality indicators represent the standard cards displayed on the AutoQA dashboard:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_autoqa_dashboard_main_cards.png)

Use the table below to understand the metrics for your main dashboard cards, using the values in the screenshot above as an example:

| | | |
| --- | --- | --- |
| **Metric** | **Description** | **Example (using the screenshot above)** |
| **Auto-reviewed conversations** | The number of conversations that had at least one category automatically scored without human intervention. If the category is automatically scored more than once, only the latest AutoQA is taken into account. Since auto-reviewed conversations count distinct conversations, not reviews, the same conversation is counted only once per [group](https://support.zendesk.com/hc/en-us/articles/7043701144858#topic_dmj_yjx_vfc), even if it's reviewed for different users in different groups. | Using the above screenshot as an example, there are 404 conversations that received at least one auto-review but haven't received any manual reviews. |
| **Manually reviewed conversations** | The number of automatically scored conversations that were also manually reviewed by humans. It counts all conversations with at least one manual review based on the conversation creation date. If the category is automatically scored more than once, only the latest AutoQA is taken into account. As this value is based on the conversation creation date filter, it may differ from the review date reported in the [Reviews dashboard](https://support.zendesk.com/hc/en-us/articles/7043724913690). | In the screenshot above, 173 conversations were manually reviewed. There may be overlap between conversations that were auto-reviewed and those that received manual reviews, as the conversations counted in this card include at least one manual review. |
| **Efficiency gain** | The ratio of how many tickets AutoQA can cover compared to manual reviews, calculated as follows: `Efficiency Gain = Auto-reviewed conversations / Manually reviewed conversations` | In the example above, the efficiency gain is calculated as follows: `2.34 Efficiency gain = 404 Auto-reviewed conversations / 173 Manually reviewed conversations` This indicates that for every manual review, you gain the equivalent of 2.34 conversations through auto-review. |
| **Auto-reviewed per reviewee** | The average number of reviews conducted for each reviewee by AutoQA, illustrating how AutoQA aids in providing feedback. | In the screenshot above: `7.8 Auto-reviewed conversations per reviewee = Number of conversations with at least one auto-review / Number of reviewees in these auto-reviews` This figure reflects the number of users who received an auto-review, not the total number of users in a workspace. The numerator for this metric includes conversations with both auto and manual reviews. This metric assesses auto-review coverage per reviewee, which is why all conversations that have received an auto-review are considered. |
| **Manually reviewed per reviewee** | The average number of manual reviews given to each reviewee. | Using the above screenshot as an example, the calculation is as follows: `3.04 Manually reviewed conversations per reviewee = 173 Manually reviewed conversations / Number of reviewees in these manual reviews` This figure refers to the number of users who received a manual review, not the total number of users in a workspace. |
| **Accuracy score** | The accuracy score measures the consistency and level of agreement between ratings generated by AutoQA and those provided by human reviewers. The gauge chart displays the average accuracy score for the selected period and filter options. A score above 75% indicates a high level of agreement, demonstrating the effectiveness of AutoQA. | |
| **Ratings by accuracy level** | The Ratings by accuracy level bar chart displays the relative proportions of AutoQA ratings grouped by accuracy level for the selected period and filter options. The accuracy metric generates a score between 0% and 100%, where 0% indicates total disagreement and 100% indicates total agreement between AutoQA and human reviewers:   - High accuracy: Scores between 75% and 100% - Medium accuracy: Scores between 25% and 74% - Low accuracy: Scores between 0% and 24% | |
| **Modified AutoQA conversations** | Number of conversations where a human has changed the AutoQA score in at least one category. | Because there was disagreement in several categories with AutoQA, these categories would be included in the 79 Modified AutoQA conversations shown in the dashboard screenshot above. |
| **AQS** | Average auto quality score of all conversations evaluated by AutoQA. | |

## Understanding additional AutoQA dashboard cards

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_autoqa_dashboard_aqs_top_languages.png)

Use the table below to understand the metrics for the additional AutoQA cards:

| | |
| --- | --- |
| **Metric** | **Description** |
| **AQS over time** | Difference in auto quality score over a selected period. This metric helps quickly identify drops in performance, allowing you to address issues promptly. |
| **Breakdown for top languages** | This metric provides the ratio and count of conversation languages, helping you identify where to invest your support efforts. For example, if you notice an increase in volume for a specific language, it may be beneficial to include that language in your knowledge base. |
| **Category insights** | Breakdown of AutoQA scores per category. If the category is automatically scored more than once, only the latest AutoQA is taken into account. |
| **Custom category insights** | Breakdown of AutoQA scores per [custom AutoQA category](https://support.zendesk.com/hc/en-us/articles/7043712922522). If the category is automatically scored more than once, only the latest AutoQA is taken into account. |
| **Category scores over time** | Line graph showing changes in category scores over a selected period. |
| **AutoQA conversations by category** | This metric represents the number of conversations that received an AutoQA rating. When a new category is added, only new incoming conversations with a Closed or Solved status are automatically analyzed and rated based on the category conditions. These are conversations that were closed with at least one public reply from both the agent and the customer. Existing conversations with a Closed or Solved status that receive an update after the category is added are also automatically analyzed and rated. Consequently, you may notice a conversation that has already been analyzed and rated being assessed again in a new workspace. |
| **Category scores per reviewee** | This metric provides information on reviewees and their automatically calculated average scores for specific auto categories over a selected time period, including archived and deleted categories. It helps quickly identify which agents are underperforming in those areas, allowing you to determine who needs training. Additionally, it provides a reference for relevant conversations to review for each agent. |
| **Root causes of spelling and grammar mistakes per reviewee** | Information about reviewees and the AutoQA-assessed [root causes](https://support.zendesk.com/hc/en-us/articles/7043759820826) identified by AutoQA's Spelling and Grammar categories. |
| **Root causes of tone mistakes per reviewee** | This metric provides information about reviewees and the [root causes](https://support.zendesk.com/hc/en-us/articles/7043759820826) of tone mistakes identified by AutoQA's tone category. |
| **Repeated spelling and grammar mistakes per reviewee** | This metric lists repeated errors, broken down by reviewee and their frequency. |
| **Last data update time (UTC)** | The date and timestamp of the last dashboard update. The AutoQA dashboard updates automatically every hour. |

## Drilling down into AutoQA dashboard data

You can drill down into the following data points:

- Conversations
- Categories
- Root causes

If a conversation has more than one review, you can have more rows in the drill-down than the number of unique conversations. For example, the Auto-reviewed conversations card displays how many conversations were reviewed. However, in the drill-down, you can access all reviews completed for each agent in that conversation.

See [Accessing additional data points](https://support.zendesk.com/hc/en-us/articles/7043701144858#topic_rnw_zjx_vfc).