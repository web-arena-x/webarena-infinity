# Creating AI prompt-based spotlight insights

Source: https://support.zendesk.com/hc/en-us/articles/9327313916570-Creating-AI-prompt-based-spotlight-insights

---

Zendesk QA prompt-based AI insights leverage the latest AI models, allowing you to customize AI-powered prompts using natural language for qualityautoscoringand risk detection.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Leverage AI prompt-based spotlight insights to enhance quality autoscoring and risk detection in customer conversations. Customize AI prompts to identify key phrases or behaviors, and create new insights for manual review. Manage up to 10 active insights per account, focusing on text-based interactions. Use the AI prompt library and follow best practices for accurate, actionable insights.

Location:  Zendesk QA > Settings > AI

Zendesk QA prompt-based AI insights leverage the latest AI models, allowing you to
customize AI-powered prompts using natural language for quality [autoscoring](https://support.zendesk.com/hc/en-us/articles/7043747123354#understanding_autoscoring_categories) and risk detection.

In Zendesk QA, [rating categories](https://support.zendesk.com/hc/en-us/articles/7043712922522) are great at assessing customer conversations and
scoring agents, while [spotlight insights](https://support.zendesk.com/hc/en-us/articles/7043759586074) are best at providing insights into
the quality of your conversations and helping you handpick critical conversations for manual
review.

Spotlight insights work with both text-based conversations and voice transcripts.
Various [out-of-the-box insights](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_lmq_fvh_xdc) help you identify specific
keywords or phrases in newly closed and synced conversations that indicate the need for
further analysis.

In addition to [customizing some of these out-of-the-box spotlight
insights](https://support.zendesk.com/hc/en-us/articles/9483275885466#topic_hvj_hvh_xdc), you can create new ones. You can create both [text-match AI spotlights](https://support.zendesk.com/hc/en-us/articles/9486586566170) that find exact phrases or keywords, and
prompt-based AI spotlights that ask specific questions about a conversation.

For example, if you want to highlight cases where either the agent or the customer
mentions a direct competitor, you could create a spotlight insight named 'Competitor' and
provide a list of competitor names, product names, and features.

Related articles

- [About AI insights in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/9224552305946)
- [Managing AI spotlight insights](https://support.zendesk.com/hc/en-us/articles/9483275885466)

Admins and account managers can have up to 10 active AI prompt-based rating
categories and AI prompt-based spotlight insights per account. When you reach this limit, you
must either mark one as inactive or delete it before you can create or activate more.

**To create a custom AI prompt-based spotlight insight**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_ai_prompt_spotlight.png)

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right
   corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click **AI**.
4. Click **Create AI insight**.
5. Select the **Prompt based** AI insight type.
6. Enter an **AI insight name**.
7. Under **AI insight description**, click **Prompt library** to select a prompt from
   our ready-to-use [AI prompt library](https://support.zendesk.com/hc/en-us/articles/9250434748058). Click **Use prompt**.

   You can also customize any prompt to fit your specific needs or create a new
   prompt from scratch:

   1. In **What do you want to detect?**, clearly describe what this insight
      should identify and accomplish.

      Specify whether the focus is on the behavior of
      agents or customers, and use objective, measurable language. You can enter up to
      2,000 characters.

      Be sure to follow our best practices for [writing prompts for AI insights](https://support.zendesk.com/hc/en-us/articles/9464975500954#topic_jqy_st2_m2c) to ensure
      your insights are accurate and actionable.
   2. In **Detection conditions**, enter an additional scoring prompt, up to 128
      characters, so the [Spotlight gets flagged positively](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_edt_gbn_q2c). Be sure to
      follow our [scoring prompt-based AI insights best
      practices](https://support.zendesk.com/hc/en-us/articles/9464975500954#topic_zgc_kbr_ffc) to ensure accurate evaluations.
   3. In **Absence conditions**, enter an additional scoring prompt of up to 128
      characters so the [Spotlight gets flagged negatively](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_edt_gbn_q2c).
8. Click **Validate** to receive feedback and tips on how to improve your prompt.
9. Under **Suggested usage**, select **Use as a spotlight**.
10. (Optional) Click **Test prompt** to confirm that your prompt works correctly and meets
    the specified criteria.

    [A conversation filter view](https://support.zendesk.com/hc/en-us/articles/7043759449114) shows the total number of
    conversations found based on the prompted insight.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_prompt_select_for_testing.png)

    To keep the pool of conversations for
    testing specific, the filter displays a list of closed conversations created in the last
    seven days that have more than four replies, by default, with a limit of 100
    conversations.
11. (Optional) Click **Select for testing**. The conversations found using this prompt
    are listed in the right-side panel, displayed 10 at a time.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_ai_prompt_spotlight_test_review.png)
12. (Optional) If you’ve validated and tested this prompt, then edited it and are testing it
    again, a prompt history is displayed. This lets you view earlier versions of the prompt
    and the match rate, which indicates the results evaluated based on that version. Check how
    often auto review and manual review scores align to get a clearer overview of your prompt
    performance. You can use this history to select the most suitable prompt version before
    moving on to its final creation.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_prompt_history_spotlight.png)
13. (Optional) Test your results:
    1. (Optional) Click **Review** next to each conversation and manually score them
       based on the prompt you are creating, so you can compare the results and see how often
       auto review and manual review scores align.
    2. Click **Run auto review** to see the results of your prompt conditions
       automatically applied to all listed conversations under **Auto**.

       If
       you see many conversations highlighted in yellow, this likely indicates a
       misalignment between how you want to score conversations and how AI is scoring them.
       You should consider rephrasing your prompt.

       When
       rephrasing what you want to detect with your prompt, if your changes are minor, you
       can click **Run auto review** again. However, if your changes are more
       significant, such as modifying it to evaluate the agent instead of the customer, the
       prompt type might change from spotlight to category. In this case, you'll need to
       return to step 10 and click **Test prompt** again.
14. Click **Create Spotlight**.