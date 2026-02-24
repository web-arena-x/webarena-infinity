# Creating AI prompt-based rating categories

Source: https://support.zendesk.com/hc/en-us/articles/9277382490138-Creating-AI-prompt-based-rating-categories

---

Zendesk QA prompt-based AI insights leverage the latest AI models, allowing you to customize AI-powered prompts for quality autoscoring and risk detection.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

With AI prompt-based rating categories, you can create custom prompts to automatically score customer conversations and detect risks. Use the AI prompt library or craft your own prompts to focus on specific behaviors. Ensure both AutoQA settings are enabled, and manage up to 10 active categories. Add categories to scorecards to start evaluating conversations based on your criteria.

Location: Zendesk QA > Settings > AI

Zendesk QA prompt-based AI insights leverage the latest AI models, allowing you to customize AI-powered prompts for quality autoscoring and risk detection.

In addition to the [system categories](https://support.zendesk.com/hc/en-us/articles/7043747123354#understanding_autoscoring_categories), [manual categories](https://support.zendesk.com/hc/en-us/articles/10301342601626), and [exact text-match categories](https://support.zendesk.com/hc/en-us/articles/9302967236890), admins and account managers can create AI prompt-based rating categories.

All [rating categories](https://support.zendesk.com/hc/en-us/articles/7043712922522) allow you to effectively assess customer conversations. However, by using AI prompt-based categories, you can ask targeted questions about conversations using natural language and automatically score them based on your criteria.

This article describes how to use AI prompt-based rating categories from our ready-to-use [AI prompt library](https://support.zendesk.com/hc/en-us/articles/9250434748058) and how to create your own custom AI prompt-based categories.

Tip: To ensure proper functionality, both the *Automatic scoring with AutoQA* and the *LLM-based AutoQA* [account settings](https://support.zendesk.com/hc/en-us/articles/7043669430426#topic_wsw_cly_ydc) must be turned on.

Related articles

- [About AI insights in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/9224552305946)
- [Best practices for creating AI insights prompts in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/9464975500954)
- [Creating AI prompt-based spotlight insights](https://support.zendesk.com/hc/en-us/articles/9327313916570)

Admins and account managers can have up to 10 active AI prompt-based rating categories and AI prompt-based spotlight insights per account. When you reach this limit, you must either mark one as inactive or delete it before you can create or activate more.

**To create a custom AI prompt-based rating category**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_ai_prompt_category.png)

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click **AI**.
4. Click **Create AI insight**.
5. Select the **Prompt-based** AI insight type.
6. Enter an **AI insight name**.
7. Under **AI insight description** click **Prompt library** to select a prompt from our ready-to-use [AI prompt library](https://support.zendesk.com/hc/en-us/articles/9250434748058). Click **Use prompt**.

   You can also customize any prompt to fit your specific needs or create a new prompt from scratch:

   1. In **What do you want to detect?**, clearly describe what this insight should identify and accomplish.

      Specify whether the focus is on the behavior of agents or customers, and use objective, measurable language. You can enter up to 2,000 characters.

      Be sure to follow our best practices for [writing prompts for AI insights](https://support.zendesk.com/hc/en-us/articles/9464975500954#topic_jqy_st2_m2c) to ensure your insights are accurate and actionable.
   2. In **Detection conditions**, enter an additional scoring prompt, up to 128 characters, that describes what the agent must do to receive a thumbs-up (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_thumbs_up.png)) rating in a category. Be sure to follow our [scoring prompt-based AI insights best practices](https://support.zendesk.com/hc/en-us/articles/9464975500954#topic_zgc_kbr_ffc) to ensure accurate evaluations.
   3. In **Absence conditions**, enter an additional scoring prompt, up to 128 characters, that describes things that should cause the agent to receive a thumbs-down (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_thumbs_dowm.png)) negative rating score for this category. For example, if the agent did not offer a demo, and the text does not include “let’s schedule a demo”, the agent receives a negative rating score for this category.

      Note: If AI can't find a clear answer based on the prompts, the category is automatically [rated as N/A](https://support.zendesk.com/hc/en-us/articles/7043701093786#topic_y5g_2cj_4fc).
8. Click **Validate** to receive feedback and tips on how to improve your prompt.
9. Under **Suggested usage**, select **Use as a category on a scorecard**.
10. (Optional) Click **Test prompt** to confirm that your prompt works correctly and meets the specified criteria.

    [A conversation filter view](https://support.zendesk.com/hc/en-us/articles/7043759449114) shows the total number of conversations found based on the prompted insights.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_prompt_select_for_testing.png)

    To keep the pool of conversations for testing specific, the filter displays a list of closed conversations created in the last seven days that have more than four replies, by default, with a limit of 100 conversations.
11. (Optional) Click **Select for testing**. The conversations found using this prompt are listed in the right-side panel, displayed 10 at a time.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_Manual+vs+Auto+Review_category_prompt.png)
12. (Optional) If you’ve validated and tested this prompt, then edited it and are testing it again, a prompt history is displayed. This lets you view earlier versions of the prompt and the match rate, which indicates the results evaluated based on that version. Check how often auto review and manual review scores align to get a clearer overview of your prompt performance. You can use this history to select the most suitable prompt version before moving on to its final creation.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_prompt_history_category.png)
13. (Optional) Test your results:
    1. (Optional) Click **Review** next to each conversation and manually score them based on the prompt you are creating so you can compare the results and see how often auto review and manual review scores align.
    2. Click **Run auto review** to see the results of your prompt conditions automatically applied to all listed conversations under **Auto**.

       If you see many conversations highlighted in yellow, this likely indicates a misalignment between how you want to score conversations and how AI is scoring them.
       You should consider rephrasing your prompt.

       When rephrasing what you want to detect with your prompt, if your changes are minor, you can click **Run auto review** again. However, if your changes are more significant, such as modifying it to evaluate the customer instead of the agent, the prompt type might change from category to spotlight. In this case, you'll need to return to step 10 and click **Test prompt** again.
14. Click **Create category**.
15. After creating it, you must [add the category to your scorecards](https://support.zendesk.com/hc/en-us/articles/7043760215194) to start using it.