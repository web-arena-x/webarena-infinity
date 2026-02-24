# Hiding reviewer identities from agents in Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/9228986629786-Hiding-reviewer-identities-from-agents-in-Zendesk-QA

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

To maintain confidentiality and encourage honest feedback, you can hide reviewer identities from agents. This account-wide setting anonymizes reviewers in areas like Activity, Coaching, and Dashboards. Agents will see "Anonymous user" instead of names, ensuring unbiased reviews and fostering a fair QA process. This feature supports a constructive environment by protecting reviewer identities while allowing agents to dispute feedback with leads or managers.

Location: Zendesk QA > Settings > General

You can anonymize the review process in Zendesk Quality assurance (QA) by preventing agents from seeing who provided their reviews.

Protecting reviewers' identities might be necessary to maintain confidentiality. It can also encourage reviewers to be more honest and open, providing unbiased feedback and fostering a fair and constructive QA process.

This article contains the following topics:

- [About reviewers' identity anonymization](#topic_wsw_cly_ydc)
- [Hiding reviewers' identities](#topic_fsw_lnh_4fc)
- [Using Zendesk QA with hidden reviewer identities](#topic_e4g_mtx_lgc)

## About hiding reviewers' identities

Admins can hide reviewers’ identities from agents This is an account setting, meaning it is turned on and off for the account as a whole. It can't be configured for individual workspaces.

When configured, reviewer identities are hidden in the following areas:

- [Activity](#topic_fcq_cvx_lgc)
 - Reviews
 - Comments
 - Reactions
 - Disputes
- [Coaching](#topic_rf1_fvx_lgc)
- [Dashboards](#topic_nyz_fvx_lgc)

## Hiding reviewers' identities

You must be an admin to configure whether reivewers' identities are hidden.

**To hide reviewers' identities from agents**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click **General**.
4. Click the **Hide reviewer identities from agents** option to turn it on.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_hide_reviewer_identities.png)

## Using Zendesk QA with hidden reviewer identities

When reviewer identities are hidden, the agent’s experience changes in the following locations:

- [Activity page](#topic_fcq_cvx_lgc)
- [Coaching page](#topic_rf1_fvx_lgc)
- [Dashboard page](#topic_nyz_fvx_lgc)

### Using the Activity page with reviewer anonymization

When reviewer anonymization is turned on, agents can’t see the names of reviewers on the Activity page. Instead, each reviewer is identified as Anonymous user.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_anonymization_reviews.png)

Agents can’t see who left comments in the Comments section, or tag anyone in a comment.
Reviewers can still [@mention other users and send them notifications](https://support.zendesk.com/hc/en-us/articles/7043669307418#topic_ezh_syk_32c)
to draw attention to the conversation. However, agents only see that an anonymous user was tagged.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_anonymization_comments.png)

Agents can’t see who left reactions in the Reactions section. Instead, reactions are attributed to Anonymous user.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_anonymization_reactions.png)

Agents can [dispute feedback](https://support.zendesk.com/hc/en-us/articles/7043760048922) only with the reviewer (listed as Original reviewer) or with users who are [leads or managers](https://support.zendesk.com/hc/en-us/articles/7043760141978#topic_dzc_fgq_q2c) in the workspace.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_anonymization_disputes.png)

### Using the Coaching page with reviewer anonymization

When reviewer anonymization is turned on, agents can’t see reviewers’ names in the Feedback pane within [coaching sessions](https://support.zendesk.com/hc/en-us/articles/7043747156506).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_anonymization_coaching.png)

### Using the Dashboard page with reviewer anonymization

When reviewer anonymization is turned on, agents can’t see reviewers’ names in dashboards that display manually submitted review data, such as the [Reviews dashboard](https://support.zendesk.com/hc/en-us/articles/7043724913690). Each reviewer is listed as Anonymous user.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_anonymization_dashboards.png)