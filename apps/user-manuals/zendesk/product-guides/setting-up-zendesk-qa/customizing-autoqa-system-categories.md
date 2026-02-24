# Customizing AutoQA system categories

Source: https://support.zendesk.com/hc/en-us/articles/9070424158106-Customizing-AutoQA-system-categories

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Customize AutoQA system categories to enhance your quality assurance process. You can modify spelling and grammar, greeting, and closing categories by adding, editing, or deleting exemptions and approved phrases. This allows you to tailor the system to your brand's standards and improve interaction analysis. Bulk editing options are available for managing multiple entries efficiently.

Location:  Zendesk QA > Settings > Scorecards

To help you get started, your account comes with a [predefined default scorecard](https://support.zendesk.com/hc/en-us/articles/8875998154906#topic_h51_hvk_32c) that includes [autoscoring system categories](https://support.zendesk.com/hc/en-us/articles/8640083599514#understanding_autoscoring_categories) and [manual categories](https://support.zendesk.com/hc/en-us/articles/8992409602842#topic_h51_hvk_32c).

You can customize the following AutoQA system categories to identify or ignore
specific keywords or phrases in conversations: Spelling and grammar, Greeting, and
Closing.

This article contains the following topics:

- [Customizing the Spelling and
  grammar category](#topic_abs_vsz_m2c)
- [Customizing the Greeting
  category](#topic_h2l_z3c_r2c)
- [Customizing the Closing
  category](#topic_tpy_z3c_r2c)

Related articles

- [Viewing and managing categories](https://support.zendesk.com/hc/en-us/articles/7043712922522)
- [Understanding autoscoring categories](https://support.zendesk.com/hc/en-us/articles/7043747123354)

## Customizing the Spelling and grammar category

In this category, AutoQA analyzes grammar, spelling, and style mistakes in both
agent and bot interactions.

You can add and manage a list of words and phrases you’d like AutoQA to ignore as
spelling and grammar mistakes. Specifically, you can make the following changes to the Spelling and grammar system
category:

- [Add
  an exemption](#topic_abs_vsz_m2c__ol_ngm_3mz_p2c)
- [Edit
  an exemption](#topic_abs_vsz_m2c__ol_v5z_lhm_52c)
- [Delete
  an exemption](#topic_abs_vsz_m2c__ol_ccl_2sb_v2c)

Changes made apply to future conversations.

If you need to delete or change the language of multiple exemptions at
once, see [Bulk editing and deleting exemptions, greetings, and closings](#topic_qkd_ljc_w2c).

**To add an exemption**

Admins and Account Managers can add up to 300 exemptions for spelling and grammar.

1. [Access your account's rating categories.](https://support.zendesk.com/hc/en-us/articles/8992409602842#topic_izk_m2y_m2c)
2. Click the name of the **Spelling and grammar** category.
3. Click **Add exemption**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_add_exemption.png)
4. Select the applicable languages from the dropdown menu.
5. Enter the words and phrases you’d like AutoQA to ignore as spelling or grammar mistakes,
   separated by a line break.
6. Click **Add exemptions**.

**To edit an exemption**

1. [Access your account's rating categories.](https://support.zendesk.com/hc/en-us/articles/8992409602842#topic_izk_m2y_m2c)
2. Click the name of the **Spelling and grammar** category.
3. Next to the exemption word or phrase you want to edit, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_horizontal.png)) and select **Edit**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_edit_spelling_and_grammar_category.png)
4. Change the exemption and its applicable languages, then click **Save changes**.

**To delete an exemption**

1. [Access your account's rating categories.](https://support.zendesk.com/hc/en-us/articles/8992409602842#topic_izk_m2y_m2c)
2. Click the name of the **Spelling and grammar** category.
3. Next to the exemption word or phrase you want to remove, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_horizontal.png)) and select **Delete**.
4. Click **Delete exemption**.

## Customizing the Greeting category

In this category, you can add approved greetings that align with your brand and
service standards.

Note that once you add an approved greeting or a list of approved greetings for a
specific language or for all languages, AutoQA only looks for these approved greetings for
positive evaluations. Greetings are not translated. If necessary, you must manually add the
expected greeting for each language. Selecting All languages means you expect that exact
greeting to be used for all detected languages. For example, if you add the approved
greeting "Bom dia" for All languages and the first agent in the conversation greets the
customer with "Buenos días," the detected language is Spanish, and the agent receives a
downvote for not using "Bom dia" in Portuguese.

When you don’t add any approved greetings for All languages, agents are evaluated
only for the specific languages where you add greetings.

The Greeting AutoQA category is available for both text and voice interactions. Specifically, you can do the following in the Greeting system category:

- [Add a greeting](#topic_h2l_z3c_r2c__ol_i2l_z3c_r2c)
- [Edit an approved
  greeting](#topic_h2l_z3c_r2c__ol_nvx_4dn_52c)
- [Delete an approved
  greeting](#topic_h2l_z3c_r2c__ol_lqj_ftb_v2c)

Changes made apply to future conversations.

If you need to delete or change the language of multiple greetings at
once, see [Bulk editing and deleting exemptions, greetings, and closings](#topic_qkd_ljc_w2c).

**To add an approved greeting**

Admins and Account Managers can add up to 200 approved greetings.

1. [Access your account's rating categories.](https://support.zendesk.com/hc/en-us/articles/8992409602842#topic_izk_m2y_m2c)
2. Click the name of the **Greeting** category.
3. Click **Add greeting**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_add_greeting.png)
4. Select the applicable languages from the dropdown menu.
5. Enter a greeting of up to 300 characters.

   To add a variable,
   enter a forward slash (/) and then add the variable `{..}`. This
   variable is a dynamic content placeholder that can be used to represent any name. For
   example, `Hello {··}!`
6. Click **Add greeting**.

**To edit an approved greeting**

1. [Access your account's rating categories.](https://support.zendesk.com/hc/en-us/articles/8992409602842#topic_izk_m2y_m2c)
2. Click the name of the **Greeting** category.
3. Next to the approved greeting you want to edit, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_horizontal.png)) and select **Edit**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_edit_greeting.png)
4. Change the greeting and its applicable languages, then click **Save changes**.

**To delete an approved greeting**

1. [Access your account's rating categories.](https://support.zendesk.com/hc/en-us/articles/8992409602842#topic_izk_m2y_m2c)
2. Click the name of the **Greeting** category.
3. Next to the approved greeting you want to remove, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_horizontal.png)) and select **Delete**.
4. Click **Delete greeting**.

## Customizing the Closing category

AutoQA analyzes if the agent or bot wrapped up the conversation.

You can define your own sign-offs that align with your brand and service
standards. Once added, AutoQA will only detect approved closings.

The Closing AutoQA category is available for both text and voice interactions. Specifically, you can do the following in the Closing category:

- [Add a closing](#topic_tpy_z3c_r2c__ol_upy_z3c_r2c)
- [Edit an approved
  closing](#topic_tpy_z3c_r2c__ol_p3s_t3n_52c)
- [Delete an approved
  closing](#topic_tpy_z3c_r2c__ol_hrt_qxb_v2c)

Changes made apply to future conversations.

If you need to delete or change the language of multiple closings at
once, see [Bulk editing and deleting exemptions, greetings, and closings](#topic_qkd_ljc_w2c).

**To add a new approved closing**

Admins and Account Managers can add up to 200 approved closings.

1. [Access your account's rating categories.](https://support.zendesk.com/hc/en-us/articles/8992409602842#topic_izk_m2y_m2c)
2. Click the name of the **Closing** category.
3. Click **Add closing**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_add_closing.png)
4. Select the applicable languages from the dropdown menu.
5. Enter an approved closing of up to 300 characters.

   To add a
   variable, enter a forward slash (/) and then add the variable
   `{..}`. This variable is a dynamic content placeholder that can
   be used to represent any name. For example, `Take care, {··}!`
6. Click **Add closing**.

**To edit an approved closing**

1. [Access your account's rating categories.](https://support.zendesk.com/hc/en-us/articles/8992409602842#topic_izk_m2y_m2c)
2. Click the name of the **Closing** category.
3. Next to the approved closing you want to edit, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_horizontal.png)) and select **Edit**.![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_edit_closing.png)
4. Change the closing and its applicable languages, then click **Save changes**.

**To delete an approved closing**

1. [Access your account's rating categories.](https://support.zendesk.com/hc/en-us/articles/8992409602842#topic_izk_m2y_m2c)
2. Click the name of the **Closing** category.
3. Next to the approved closing you want to remove, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_horizontal.png)) and select **Delete**.
4. Click **Delete closing**.

## Bulk editing and deleting exemptions, greetings, and closings

There are some changes you can make in bulk to exemptions, greetings, and closings. Specifically, you can:

- [Change the language of multiple exemptions, greetings, or closings](#topic_qkd_ljc_w2c__ol_amg_4jc_w2c)
- [Delete multiple exemptions, greetings, or closings](#topic_qkd_ljc_w2c__ol_m22_j4c_w2c)

**To change the language for multiple exemptions, greetings, and closings in
bulk**

1. [Access your account's rating categories.](https://support.zendesk.com/hc/en-us/articles/8992409602842#topic_izk_m2y_m2c)
2. Click the name of the **Spelling and grammar**, the **Greeting**, or
   the **Closing** category.
3. Select the exemptions, greetings, or closings for which you want to change the
   language, or select the entire list by clicking the checkbox in the top left
   corner.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_edit_closing_bulk.png)
4. A toolbar appears at the bottom of the list. Click **Languages**.
5. Select or deselect the languages to apply for your selected exemptions, greetings or
   closings. Your changes are automatically applied.
6. To close the **Languages** selection box, click outside of it.

**To delete multiple exemptions, greetings, and closings in bulk**

1. [Access your account's rating categories.](https://support.zendesk.com/hc/en-us/articles/8992409602842#topic_izk_m2y_m2c)
2. Click the name of the **Spelling and grammar**, the **Greeting**, or
   the **Closing** category.
3. Select the exemptions, greetings, or closings you want to delete, or select the entire
   list by clicking the checkbox in the top left corner.
4. A toolbar appears at the bottom of the list. Click **Delete**.
5. Click **Delete exemptions** to permanently delete your selected exemptions,
   greetings, or closings.