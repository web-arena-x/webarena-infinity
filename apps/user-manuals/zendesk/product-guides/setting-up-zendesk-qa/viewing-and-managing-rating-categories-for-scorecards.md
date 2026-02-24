# Viewing and managing rating categories for scorecards

Source: https://support.zendesk.com/hc/en-us/articles/8992409602842-Viewing-and-managing-rating-categories-for-scorecards

---

Rating categories allow you to effectively assess customer conversations.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Manage rating categories for scorecards to assess customer conversations. You can view, edit, activate, deactivate, or delete categories. While system categories can be tailored for specific keywords, you can also customize manual, exact text-match, and prompt-based categories. Changes apply to future conversations.

Location:  Zendesk QA > Settings > Scorecards

Rating categories allow you to effectively assess customer conversations.

[Internal Quality Score (IQS)](https://support.zendesk.com/hc/en-us/articles/7043701093786#topic_sws_4ww_42c) is calculated based on
these categories, helping you evaluate and improve your customer support.

To help you get started, your account comes with a predefined default scorecard that includes
[autoscoring system categories](https://support.zendesk.com/hc/en-us/articles/7043747123354#understanding_autoscoring_categories) and manual categories.

This article contains the following topics:

- [Accessing your account's rating
  categories](#topic_izk_m2y_m2c)
- [Editing manual, exact text-match,
  and prompt-based categories](#topic_h51_hvk_32c)
- [Activating a category](#topic_wvk_pmf_q2c)
- [Deactivating a category](#topic_ezh_syk_32c)
- [Deleting a category](#topic_fw3_bbl_32c)

Related articles

- [Accessing and managing your scorecards, categories, and
  root causes](https://support.zendesk.com/hc/en-us/articles/7043669430426#topic_fbm_xnf_zdc)
- [Creating rating categories](https://support.zendesk.com/hc/en-us/articles/7043712922522)
- [Customizing AutoQA system categories](https://support.zendesk.com/hc/en-us/articles/9070424158106)

## Accessing your account's rating categories

Admins and account managers can view and manage categories.

**To access your scorecard categories**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right
   corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click
   **Scorecards**.
4. Click **Categories** at the top to display a list of all your
   categories.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_scorecards_categories_list.png)

   From this list, you can do the
   following

   - View each category’s type. Categories that use [autoscoring](https://support.zendesk.com/hc/en-us/articles/7043747123354#understanding_autoscoring_categories) are indicated by a hologram icon
     (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_hologram.png)):
     - [**System**](https://support.zendesk.com/hc/en-us/articles/7043747123354#understanding_autoscoring_categories): Predefined autoscoring
       categories (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_hologram.png)). These categories can't be
       deleted. Admins and account managers can [customize some of these categories](https://support.zendesk.com/hc/en-us/articles/9070424158106)
     - [**Exact text-match**](https://support.zendesk.com/hc/en-us/articles/9302967236890): User-defined
       autoscoring categories (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_hologram.png)) that are assessed based on
       exact text matches.
     - [**Manual**](https://support.zendesk.com/hc/en-us/articles/7043712922522#topic_cch_4xk_32c): User-defined and scored
       categories.
     - [**Prompt-based**](https://support.zendesk.com/hc/en-us/articles/9277382490138): User-defined
       autoscoring categories (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_hologram.png)) that use the latest AI models
       and human-language prompts to provide AI-powered quality scoring and risk
       detection.
   - See how many scorecards use each category.
   - See whether each category is [active](#topic_wvk_pmf_q2c) or [inactive](#topic_ezh_syk_32c).

     Note: If a prompt-based category produces over 95% [N/A (Not applicable) results](https://support.zendesk.com/hc/en-us/articles/7043701093786#topic_y5g_2cj_4fc) for 7
     consecutive days, it’s automatically [marked as inactive](#topic_ezh_syk_32c) and displays an attention icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_prompt_attention.png)). You must update your prompt to gather
     relevant insights before [marking it
     as active](#topic_wvk_pmf_q2c) again.
   - See when each category was last updated.
   - Search for categories by name.
   - Filter the list by categories assigned to a specific scorecard, category type, or
     status.

## Editing rating categories

Admins and account managers can edit manual, text-match, and prompt-based
categories.

System categories can’t be edited. However, admins and account managers can
customize the Spelling and grammar, Greeting, and Closing system categories to identify or
ignore specific keywords or phrases in conversations. See [Customizing AutoQA system categories](https://support.zendesk.com/hc/en-us/articles/9070424158106).

Changes made to categories apply to future conversations only. See [Understanding rating categories for scorecards](https://support.zendesk.com/hc/en-us/articles/7043712922522#topic_izk_m2y_m2c).

Changes made to the name and description of a category do not affect its reporting.

**To edit a category**

1. [Access your account's rating
   categories.](#topic_izk_m2y_m2c)
2. Click the name of the category you want to change.
3. Change the **Name** and **Description** of your category.
4. (Optional) Adjust the filter settings and scores for your [exact text-match categories](https://support.zendesk.com/hc/en-us/articles/7043712922522#topic_gr3_tkb_q2c), or your prompt, in
   [custom-prompt categories](https://support.zendesk.com/hc/en-us/articles/7043712922522#topic_fld_rcr_ffc).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_exact_text_match_category_edit.png)
5. Click **Save changes**.

## Activating a category

Inactive categories aren’t visible in scorecards. To allow it to be used by
reviewers for evaluations in selected scorecards and workspaces, it must be marked as
active.

**To mark a category as active**

1. [Access your account's rating
   categories.](#topic_izk_m2y_m2c)
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_horizontal.png)) next to the category you want to activate and
   select **Mark as active**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_categories_mark_active.png)

## Deactivating a category

A category marked as active is ready to be used for evaluations on scorecards. Marking a
category as inactive means it can't be used for evaluations in scorecards and workspaces.
[Past reviews](https://support.zendesk.com/hc/en-us/articles/7043669307418#topic_fw3_bbl_32c) will not display the removed category.
However, removing a category does not affect historical dashboard metrics or overall scores.
Deactivated categories remain available in reporting and filtering. Your [dashboards](https://support.zendesk.com/hc/en-us/articles/7043701144858) continue to reflect accurate historical data, including
scores and trends, even after categories are removed.

**To mark a category as inactive**

1. [Access your account's rating
   categories.](#topic_izk_m2y_m2c)
2. Next to the category you want to deactivate, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_horizontal.png)) and select **Mark as inactive**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_categories_mark_inactive.png)

## Deleting a category

Deleting categories is permanent. The category is removed from all
scorecards. If it's the only category in a scorecard, the scorecard is automatically deactivated.

Note: Deleting a category erases all category data from reporting. Once deleted, you
can't restore the category or its data.

**To delete a category**

1. [Access your account's rating
   categories.](#topic_izk_m2y_m2c)
2. Next to the category you want to delete from Zendesk QA, click the options
   menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_horizontal.png)) and select **Delete**.