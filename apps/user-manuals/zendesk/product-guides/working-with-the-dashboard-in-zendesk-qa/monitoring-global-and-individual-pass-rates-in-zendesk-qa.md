# Monitoring global and individual pass rates in Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/7043668650266-Monitoring-global-and-individual-pass-rates-in-Zendesk-QA

---

The pass rate is a key metric for evaluating the quality of customer interactions in Zendesk Quality assurance (QA). It measures the percentage of reviews that meet a predefined baseline quality score. You can monitor the pass rate on the Reviews dashboard to track performance and ensure quality standards are met.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Monitor your team's pass rate using the Reviews dashboard to ensure quality customer interactions. The pass rate reflects the percentage of reviews meeting a baseline quality score, typically 80%. You can view overall and individual pass rates, track performance changes, and analyze scores to maintain high standards. Adjust the baseline score by contacting customer support if needed.

Location:  Zendesk QA > Dashboards > Reviews

The pass rate is a key metric for evaluating the quality of customer interactions in
Zendesk Quality assurance (QA). It measures the percentage of reviews that meet a predefined
baseline quality score. You can monitor the pass rate on the Reviews dashboard to track
performance and ensure quality standards are met.

This article includes the following topics:

- [About the pass rate](#about_pass_rate)
- [Viewing pass rate data in the
  Reviews dashboard](#viewing_pass_rate)

**Related articles**

- [About dashboards in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043701144858)
- [Setting a performance reporting threshold in Zendesk
  QA](https://support.zendesk.com/hc/en-us/articles/7043700991514)

## About the pass rate

Each review is measured against a baseline set for the Internal Quality Score
(IQS) to determine whether it passes or fails. By default, Zendesk QA uses a baseline score
of 80%. Reviews scoring 80% or higher pass, while those scoring 79.9% or lower fail.

The pass rate is the percentage of the total reviews that meet and exceed the baseline score. This is calculated by dividing the number of reviews that pass by the total number of reviews.

Note: The pass rate for Zendesk QA is a global setting that applies to your entire account
and all workspaces. To change the baseline score, [contact Zendesk customer support](https://support.zendesk.com/hc/en-us/articles/4408843597850). Once changed, scores update
across both historical data and new reviews.

## Viewing pass rate data in the Reviews dashboard

The [Reviews dashboard](https://support.zendesk.com/hc/en-us/articles/7043724913690) is comprised of many cards that together provide a quick overview of reviews, including overall and individual pass rates.

**To view the pass rate data in the Reviews dashboard**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Dashboards**
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_dashboard_icon.png) in the sidebar.
2. On the **Reviews** dashboard, open the following cards to see scores and pass rate
   information:
   - **Pass rate**: Provides a quick overview of the overall pass rate for your
     team.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_dashboards_reviews.png)
   - **Reviewer performance**: Provides detailed information about individual
     reviewer performance, including the pass rate for each user, percentage change in
     their pass rates over time, and the number of passed reviews.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_reviews_reviewer_performance.png)
   - **Reviewee performance**: Provides detailed information about individual
     reviewee performance, including the pass rate for each user, percentage change in
     their pass rates over time, and the number of passed reviews.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_reviews_reviewee_performance.png)
   - **Scores by review**: Provides detailed information about each review,
     including the score and the pass/fail status. You may notice a difference in colors
     between the Score and Pass/Fail columns because they are color-coded based on
     different metrics. The colors in the Pass/Fail column are based on the pass rate
     baseline score, while the colors in the Score column reflect the workspace's
     [performance reporting threshold](https://support.zendesk.com/hc/en-us/articles/7043700991514).

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_reviews_dashboard_scores_reviews.png)