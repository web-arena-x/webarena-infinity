# Setting reminders to review and verify articles

Source: https://support.zendesk.com/hc/en-us/articles/4408828628634-Setting-reminders-to-review-and-verify-articles

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Enterprise |

Location:  Knowledge admin > Settings (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) > Article verification

Verification is an article setting that lets you indicate whether an article is accurate and
current, or whether it needs review and possible revision. You can use [article verification](https://support.zendesk.com/hc/en-us/articles/5588297664666) to either:

- Manually unverify articles, prompting an immediate review and verification by
  article owners.
- Automatically unverify articles by configuring article verification rules based
  on predefined filter and interval criteria.

When articles are unverified, article owners receive email reminders to review and verify
their articles. You cannot change or add recipients to the notifications. The owner is the
author by default, but you can [change the article owner](https://support.zendesk.com/hc/en-us/articles/4408832308506) to another user or a group.

Important: When you downgrade article owners from agents to
end users, you must also reassign their article ownership. Unless you reassign article
ownership, agents who are downgraded to end users will still receive article verification
emails for the articles that they own. For more information, see [Changing the article owner](https://support.zendesk.com/hc/en-us/articles/4408832308506).

This article contains the following sections:

- [Manually unverify articles](#topic_flt_ggb_dxb)
- [Create article verification
  rules](#topic_o1t_3gb_dxb)

## Manually unverify articles

You can use article verification to initiate a one-time review of your knowledge base
content. For example, you might be moving to a new brand name, in which case you would want
to review and revise your articles to reflect the new brand.

To perform a one-time review, you can either unverify individual articles, or unverify
articles in bulk.

****To unverify individual articles****

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Manage articles**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_manage_articles.png)) in the sidebar.
2. Select one or more articles to update.

   You can select a maximum of 30 articles at a
   time. To select 30 items at once, select the check box beside **Title** at the top
   of the list.

   ![Bulk article update select all.](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bulk_update_select_all.png)
3. Click the **Article settings** bulk actions menu at the bottom, then select
   **Unverify**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_articles_Bulk_verify.png)
4. Click **Unverify** to confirm that you want to verify the selected articles.

## Create article verification rules

You can create [article verification rules](https://support.zendesk.com/hc/en-us/articles/5588297664666) to send reminders when
articles need to be reviewed and verified, based on the criteria and interval you set. This
helps ensure that your content doesn't become stale or out of date. For example, every three
months you might want to review articles that have a specific label, appear in a certain
category, or haven't been updated in a while.

You can create as many as 20 verification rules. You must be a Knowledge admin to create
article verification rules.

You can [duplicate an existing rule](managing-article-verification-rules.md#topic_q4h_5zs_hhb) if you'd like your rule
to be based on another rule.

**To create an article verification rule**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) in the sidebar.
2. Click **Article verification**, then click **Add**.

   If the Add button is not
   available, then you have already created the maximum number of 20 rules. You can delete
   a rule if you want to add a new rule.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/article_verification_rule_add.png)
3. Enter a **Rule name**.
4. Select a **Frequency** for the reminder.

   After the specified interval, an email
   notification is sent to the article owner and the articles appear in the Article
   Verification list.
5. Select **Filters** to determine the group of articles for this rule.

   As you select
   filter options, a list of affected articles appears below. See [product limits](https://support.zendesk.com/hc/en-us/articles/4408831783962-Guide-product-limits-for-your-help-center) for filter limits.
6. Click **Create**.