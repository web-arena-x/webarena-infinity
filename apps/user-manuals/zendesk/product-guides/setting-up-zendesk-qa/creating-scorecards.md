# Creating scorecards

Source: https://support.zendesk.com/hc/en-us/articles/7043760215194-Creating-scorecards

---

Scorecardsin Zendesk QA provide a powerful tool for evaluating agent performance, identifying areas for improvement, and ensuring that your team meets organizational goals.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Create scorecards to evaluate agent performance and identify improvement areas. You can add categories, set rating scales, and define weights to highlight important aspects of customer interactions. Use conditional scorecards to streamline reviews based on specific criteria, and add root causes for detailed feedback. Once set up, publish your scorecard to start enhancing your team's quality assurance process.

Location:  Zendesk QA > Settings > Scorecards

[Scorecards](https://support.zendesk.com/hc/en-us/articles/8875998154906) in Zendesk QA provide a powerful tool for
evaluating agent performance, identifying areas for improvement, and ensuring that your team
meets organizational goals.

Admins can create new scorecards.

**To create a new scorecard**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right
   corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click
   **Scorecards**.
4. Click **Create** and select **Scorecard**.
5. Enter a **Name** for the scorecard.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_create_scorecard.png)
6. Under **Workspaces**, select the workspaces you want to review manually with
   this scorecard.
7. Under **Workspaces with AutoQA enabled**, select the workspaces you want to
   [autoscore](https://support.zendesk.com/hc/en-us/articles/7043747123354) with this scorecard.
8. (Optional) Click **Add group section** to organize your scorecard’s
   categories.
9. Click **Add category** to select the categories to include in the scorecard.

   You can create a new category by typing a name and selecting **[Create category](https://support.zendesk.com/hc/en-us/articles/7043712922522)**.
10. Select a **Rating scale**.

    Smaller scales work best for quick,
    consistent reviews across a large volume of tickets, while larger scales provide nuance
    and are better suited for coaching and improving quality. See [Understanding how category scores are
    calculated](https://support.zendesk.com/hc/en-us/articles/7043701093786#category_scores).

    The following rating scales are available:

    - **Binary**: A binary scale is the fastest and most consistent scale
      because it has only two options: *good* and *bad*. It is ideal for large
      volumes where speed is important.
    - **3-point**: A 3-point scale can still be graded quickly but adds a
      little more nuance by including a middle option of *satisfactory* in addition to
      *good* and *bad*.
    - **4-point**: A 4-point scale encourages critical thinking by requiring a
      decisive assessment of *good*, *slightly good*, *slightly bad*, or
      *bad* without a neutral option.
    - **5-point**: A 5-point scale offers more detailed feedback and resembles
      the academic grading system (A = 5, B = 4, and so on). The drawback of this type of
      scale is that grading can often take longer, since there is more for your reviewers to
      consider.

      Clicking Settings in the top-right corner allows you to [use emojis instead of numbers and allow users to
      skip categories, by including N/A as an option](https://support.zendesk.com/hc/en-us/articles/8875998154906#topic_ufd_t3n_zfc).
11. Specify a **Weight** for the category to define its importance relative to other
    categories. This value must be an integer between 0 and 100. The default weight for a new
    category is 10.

    Adjusting the weight of different categories can highlight what
    is most important to your company when responding to customer requests. For example, you
    might give the root cause a higher weight than documentation if you think understanding
    the root cause is more important.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_category_weight.png)

    When you hover over the category
    weight, it displays how it translates to the overall quality score as a
    percentage.
12. (Optional) Select **Critical category** if this category is important enough to fail
    the review. Critical rating categories are those where a rating below 50% results in an
    automatic failure for all categories, leading to a score of 0%. This is useful for tracking
    regulatory compliance, for example.

    If the category is part of a group, select whether the
    failure of this category:

    - **Fails the whole review**: All categories in the review are failed and
      the review score is 0%.
    - **Fails the group only**: Only other categories in the group fail.
13. (Optional) Select **Only show on the scorecard under certain conditions** to narrow the
    scope of what this scorecard is used for. For example, if you are reviewing a conversation
    with a *Satisfaction Score of 3*, your *Product Knowledge* Rating Category will be
    available for grading. Setting up conditional scorecards saves time as you don't need to
    manually select the scorecard each time you review a conversation.

    You can
    create conditions that the conversation must meet for the scorecard to be automatically
    selected based on the following criteria:

    - [Source type](https://support.zendesk.com/hc/en-us/articles/7043759449114#h_4e27ce74b3)
    - [Conversation channel](https://support.zendesk.com/hc/en-us/articles/4408824097050)
    - [Help desk tag](https://support.zendesk.com/hc/en-us/articles/4408881573658)
    - [Satisfaction score (CSAT)](https://support.zendesk.com/hc/en-us/articles/7689997846554)

    If no condition is selected the scorecard needs to be manually selected
    when you are reviewing conversations.
14. (Optional) Select **Add root causes to explain rating** to prompt reviewers to provide
    more details on their feedback for the category. This is particularly helpful for negative
    feedback.

    When selected, you can:

    - Specify separate lists of predefined **Root causes** that are available for
      negative ratings (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_thumbs_dowm.png)) and positive ratings (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_thumbs_up.png)).

      Select from the list or create a new root cause by typing a
      name and selecting [Create](https://support.zendesk.com/hc/en-us/articles/7043759820826).
    - Select whether you want to provide reviewers with an **‘Other’ option** and comment
      field where they can provide their own, non-standard root cause.
    - Select whether you want to allow reviewers to add **Allow selecting ultiple root
      causes** for this category.
15. Click **Apply**.
16. Click **Publish** to make your new scorecard available for use or click **Save as draft** if you aren't ready to publish it.