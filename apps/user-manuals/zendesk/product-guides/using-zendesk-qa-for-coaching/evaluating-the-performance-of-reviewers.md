# Evaluating the performance of reviewers

Source: https://support.zendesk.com/hc/en-us/articles/7043661635226-Evaluating-the-performance-of-reviewers

---

Evaluating the reviews completed by your reviewers in Zendesk QA is an important part of a consistent and accurate QA process. By performing spot checks, you can monitor and identify any discrepancies in your reviewers' work. You can think of this as “grading the grader.”

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Evaluate reviewer performance by creating a unique scorecard to conduct spot checks and assign an Internal Quality Score (IQS). Use this scorecard to review and monitor reviewers' work, identifying discrepancies without needing immediate calibration sessions. Leverage dashboards to analyze performance, focusing on areas like comment quality and review accuracy, ensuring consistent and accurate quality assurance processes.

Location: Zendesk QA > Settings > Scorecards

Evaluating the reviews completed by your reviewers in Zendesk QA is an important part of a consistent and accurate QA process. By performing spot checks, you can monitor and identify any discrepancies in your reviewers' work. You can think of this as “grading the grader.”

This article describes how to create and use a unique scorecard to review your reviewers. This method gives your reviewers their own [Internal Quality Score (IQS)](https://support.zendesk.com/hc/en-us/articles/7043724913690#topic_cwx_3qw_42c) that is traceable in the [dashboard](https://support.zendesk.com/hc/en-us/articles/7043724913690), without the need for immediate [calibration sessions](https://support.zendesk.com/hc/en-us/articles/7043724530842).

This article contains the following topics:

- [Creating a grade the grader scorecard](#topic-1__ul_dr2_gl1_t2c)
- [Reviewing your reviewers](#topic_jqy_st2_m2c)
- [Monitoring your reviewers performance](#topic_tlh_ds1_t2c)

Related articles

- [Creating scorecards](https://support.zendesk.com/hc/en-us/articles/7043760215194)

## Creating a grade the grader scorecard

**To create a scorecard to evaluate reviewers**

1. [Create a separate workspace](https://support.zendesk.com/hc/en-us/articles/9202963091866) in your account. For example, you can name it “*Grade the grader*”. This is where the reviews for the reviewers will go.
2. [Create a unique scorecard](https://support.zendesk.com/hc/en-us/articles/7043760215194) for reviewing your reviewers. For example, you can name it “*Spot-check*”.
3. Under **Workspaces**, select the workspace for reviewing reviewers that you created earlier.
4. Under **Workspaces with AutoQA enabled** make sure **No workspaces** is selected.
5. Click **Add a group section**.
6. Add three binary [categories](https://support.zendesk.com/hc/en-us/articles/7043712922522) to the *Spot-check* group. For example:
   - *Comment quality*
   - *Review accuracy*
   - *Review time*![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_grade_the_grader.png)
7. Select **Add root causes to explain rating** and add [**Root causes**](https://support.zendesk.com/hc/en-us/articles/7043759820826) for **Negative ratings** (![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfbkg4jDTU995CHmbn33wTuUaIfzMiqzLomVRwrfHWq9YrusXdCxqKV3n--Ld22_nAiRr0NT-GGk0bxpaBpg04bDjXJG_akvxfrk5VDJC_uge6sQbn-IH_Zq66m_qxyh2WQlGJ-Gg?key=LHgCCuIpUpK86C9IhNIaxhYI)) for each category in the scorecard used by the reviewer to perform reviews:
   - [*Category name*]: Score too high
   - [*Category name*]: Score too low

   Where [*Category name*] is replaced with the name of the respective categories in the scorecard used by the reviewer to perform reviews. For example: *Tone Score too high; Tone Score too low.*
8. Configure any other settings for each category within the scorecard as needed.
9. Click **Apply**.
10. Click **Publish**.

## Reviewing your reviewers

**To review your reviewers**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Conversations**
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_conversations_icon.png) in the sidebar.
2. [Filter](https://support.zendesk.com/hc/en-us/articles/7043759449114) your conversation list for conversations that have been reviewed in the past week.
3. Click **Review**.
4. Select the scorecard you have created for reviewing the reviewers. For example, “*Spot-check*.”
5. Leave a review for the reviewer using the scorecard.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_spot_check_review.png)

## Monitoring your reviewers performance

Use [dashboards](https://support.zendesk.com/hc/en-us/articles/7043724913690) to understand your reviewer's performance.

**To monitor your reviewers using dashboards**

1. [Filter your Reviews dashboard](https://support.zendesk.com/hc/en-us/articles/7043701144858)
   specifically for this scorecard to visualize how your reviewers are performing.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_dashboard_categories_spot-checks.png)
2. Use the [Categories dashboard](https://support.zendesk.com/hc/en-us/articles/9019975345434) to dive deeper into where the reviewer is misaligned (for example, scoring too high or low for a specific category).