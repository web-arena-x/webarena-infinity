# Accessing and viewing the Surveys dashboard

Source: https://support.zendesk.com/hc/en-us/articles/7043759414042-Accessing-and-viewing-the-Surveys-dashboard

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Use the Surveys dashboard to analyze survey results and gain insights into customer support performance. You can filter data by question type, score, language, and more. The dashboard provides metrics like average score, score breakdown, and survey funnel, helping you understand response rates and feedback reasons. It also offers visual tools like word clouds and tracks agent performance over time.

Location: Zendesk QA > Dashboard > Surveys

The Surveys dashboard allows you to view and analyze the results of your [surveys](https://support.zendesk.com/hc/en-us/articles/4408886194202).

This article explains how to access and use the Surveys dashboard to gain valuable insights into your customer support performance.

This article contains the following topics:

- [Accessing and filtering the Surveys dashboard](#topic_hnr_xhv_42c)
- [Understanding the Surveys dashboard](#topic_usg_3nv_sgc)

Related articles:

- [About dashboards in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043701144858)

## Accessing and filtering the Surveys dashboard

Access the Surveys dashboard to analyze specific datasets and gain insights into your surveys performance.

**To access and filter the Surveys dashboard**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Dashboards**
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_dashboard_icon.png) in the sidebar.
2. Click the **Surveys** dashboard.
3. (Optional) Select any [filters](https://support.zendesk.com/hc/en-us/articles/7043701144858#topic_kcp_yv1_cbc) you want to apply.

   The Surveys dashboard offers the following additional filtering options to help you focus on specific data:

   - **Question type**: The type of survey question (for example, CSAT, CES, or custom types), if applicable.
   - **Survey**: Specific survey selection, if applicable.
   - **Score**: The survey score.
   - **Response language**: The language of survey responses.
   - **Source**: Specific [connection](https://support.zendesk.com/hc/en-us/articles/7043712839450), if applicable.
   - **Helpdesk tag**: [Connection](https://support.zendesk.com/hc/en-us/articles/7043712839450) ticket tags, if applicable.
   - **Word cloud word**: Specific words in comments.
   - **Comment size**: Comment length (short, mid-length, long, very long).
   - **Predicted drivers**: AI-generated sentiment or reason filtering is available for comments in English only. This feature helps you categorize customer feedback comments into predefined categories, providing valuable insights into customer sentiment and support performance.

     Comments are tagged under the following content categories:

     - Account
     - Refund
     - Bad support
     - Bad product
     - Bad outcome
     - Good support
     - Feedback for agent
     - Complaint
     - Confusing
     - Crumbs
     - Issue not solved
     - Issue solved
     - Negative sentiment
     - Positive sentiment
     - Praise
     - Good support
     - Support not helpful
     - Fast support
     - Slow support
     - Thanks
   - **Reason for feedback**: Manual categorization of feedback.
   - **Channel**: Communication [channel](https://support.zendesk.com/hc/en-us/articles/4408824097050) filtering.
   - **Helpdesk field**: Custom field filtering for eligible accounts based on [connection](https://support.zendesk.com/hc/en-us/articles/7043712839450).
   - **Helpdesk value**: Custom values filtering for eligible accounts based on [connection](https://support.zendesk.com/hc/en-us/articles/7043712839450).

## Understanding the Surveys dashboard

The following cards are available in the Surveys dashboard to help you understand your survey results:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_dashboards_surveys.png)

1. [Average score](#topic_yhj_dg4_s2c)
2. [Score breakdown](#topic_bnw_phv_sgc)
3. [Survey funnel](#topic_avz_shv_sgc)
4. [Survey responses](#topic_whv_vhv_sgc)
5. [Word cloud](#topic_f3f_zvv_vgc)
6. [Reasons](#topic_wnp_zvv_vgc)
7. [Helpdesk tags](#topic_rr2_1wv_vgc)
8. [Users](#topic_rcn_1wv_vgc)
9. [Quality and survey scores over time](#topic_ggx_1wv_vgc)
10. [Survey and conversation metrics by attribute](#topic_hhf_bwv_vgc)
11. [Survey and conversation metrics over time by attribute](#topic_hlp_bwv_vgc)

### Average score

CSAT is calculated by dividing the sum of all responses by the total possible maximum scores. The average score displays the average Customer Satisfaction Score (CSAT)
normalized to a percentage. It also provides a period-over-period growth calculation in comparison to the previous period.

### Score breakdown

Score breakdown shows the distribution of survey responses by rating score.

### Survey funnel

This card tracks the survey engagement pipeline from conversations to responses.

The survey funnel shows the number of surveys sent versus the number of responses and comments received, allowing you to determine your response rate, including:

- Total conversations
- Surveys sent
- Surveys answered
- Surveys answered with comments

### Survey responses

Displays a detailed table of individual survey responses. Agents can be the original score recipients (default) or those with the most replies in the ticket, based on the dashboard parameter selection.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_survey_responses.png)

Survey responses include the following fields:

- Date
- Agent name
- Response comment
- Rating score
- Predicted drivers (survey response score [insights](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_lmq_fvh_xdc))
- Comment size classification (short, mid-length, long, very long)
- Custom fields (available in the export file for eligible accounts)

### Word cloud

This card provides a visual representation of the top one hundred words mentioned in survey comments.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_surveys_word_cloud.png)

### Reasons

This card shows survey responses by feedback reason tag.

### Helpdesk tags

This card shows survey responses by ticket tags from your [connected Zendesk Support account](https://support.zendesk.com/hc/en-us/articles/7043712839450), if applicable.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_surveys_helpdesk_tag.png)

### Users

This card shows agent performance analytics and comparisons.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_surveys_users.png)

### Quality and survey scores over time

This card shows a high-level trend analysis for key operational metrics for a day, week, month, or quarter.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_quality_survey_scores_overtime.png)

### Survey and conversation metrics by attribute

This card shows a segmented analysis based on key conversation or survey attributes.

The default table attribute used to slice the data is "survey response reason." However, you can modify it to a different survey attribute (such as survey response language or survey response predicted driver) or a conversation attribute (including conversation channel, conversation source, or conversation tag) through dashboard parameters. Use the "Select chart attribute" option under [Display settings](https://support.zendesk.com/hc/en-us/articles/7043701144858#topic_xlj_yjx_vfc).

### Survey and conversation metrics over time by attribute

This card displays your survey scores over different time periods (daily, weekly, monthly, quarterly) and compares them to your targets. It also shows the number of responses.