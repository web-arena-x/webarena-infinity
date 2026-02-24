# Understanding autoscoring categories

Source: https://support.zendesk.com/hc/en-us/articles/7043747123354-Understanding-autoscoring-categories

---

Autoscoring supports your manual review efforts by automatically evaluating and scoring customer interactions for 100% of your ticket volume based on predefinedcategories. This ensures consistent quality assessments, reduces subjectivity, and saves reviewers time, allowing them to focus on categories that need more attention.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Autoscoring evaluates and scores all customer interactions automatically, helping you maintain consistent quality assessments and save time. By activating autoscoring categories, you can focus on areas needing attention. Customize or create new categories to suit your needs. Use the AutoQA dashboard to track performance trends and identify training needs across categories like empathy, tone, and comprehension.

Location:  Zendesk QA > Settings > Scorecards

Autoscoring supports your manual review efforts by automatically evaluating and
scoring customer interactions for 100% of your ticket volume based on predefined [categories](https://support.zendesk.com/hc/en-us/articles/7043712922522). This ensures consistent quality assessments, reduces
subjectivity, and saves reviewers time, allowing them to focus on categories that need more
attention.

This article contains the following topics:

- [Overview of autoscoring
  (video)](#topic_epd_qvb_42c)
- [About
  autoscoring categories](#understanding_autoscoring_categories)
- [Viewing
  autoscoring in conversations](#creating_custom_autoqa_categories)

Related articles

- [About rating categories for scorecards](https://support.zendesk.com/hc/en-us/articles/7043712922522)
- [Viewing and managing rating categories for
  scorecards](https://support.zendesk.com/hc/en-us/articles/8992409602842)
- [Changing an agent’s autoscore](https://support.zendesk.com/hc/en-us/articles/9046364914842)

## Overview of autoscoring (video)

In addition to the details in this article, this video provides a helpful visual
overview of autoscoring.

## About autoscoring categories

Autoscoring categories are indicated by a hologram icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_hologram.png)). To use automatic scoring with AutoQA,
you must first activate this feature in your [account settings](https://support.zendesk.com/hc/en-us/articles/7043669430426#topic_wsw_cly_ydc). Additionally, categories must be
marked as [active](https://support.zendesk.com/hc/en-us/articles/8992409602842#topic_wvk_pmf_q2c) and [assigned to at least one workspace and one active
scorecard](https://support.zendesk.com/hc/en-us/articles/8875998154906#topic_wsw_cly_ydc) to automatically evaluate and score those agents.

Zendesk Quality assurance (QA) includes several system categories that are
automatically scored when active. Admins can [customize some of these categories](https://support.zendesk.com/hc/en-us/articles/9070424158106) and [create new custom autoscoring categories](https://support.zendesk.com/hc/en-us/articles/7043712922522).

Text-based interactions (chats and emails) are reviewed by AutoQA separately from
[voice calls](https://support.zendesk.com/hc/en-us/articles/7043759312154).

The languages supported for each category depend on whether LLM-based AutoQA is
activated in the [Account settings](https://support.zendesk.com/hc/en-us/articles/7043669430426#topic_wsw_cly_ydc).

The following system categories receive automatic scoring in Zendesk QA:

- [Greeting](#understanding_autoscoring_categories__greeting)
- [Empathy](#understanding_autoscoring_categories__empathy)
- [Spelling and grammar](#understanding_autoscoring_categories__spelling)
- [Closing](#understanding_autoscoring_categories__closing)
- [Solution offered](#understanding_autoscoring_categories__solution)
- [Tone](#understanding_autoscoring_categories__tone)
- [Readability](#understanding_autoscoring_categories__readability)
- [Comprehension](#understanding_autoscoring_categories__comprehension)

The Greeting, Spelling and grammar, Readability, and Closing categories are scored each
time a ticket syncs with Zendesk QA, regardless of whether the ticket is in a closed or
solved status. In contrast, the Empathy, Solution offered, Tone, and Comprehension
categories are evaluated only once the ticket is set to a solved or closed status.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Category** | **Description** | **Score** | **Languages/OpenAI-enabled** | **Languages/OpenAI-disabled** |
| Greeting | Answers the question “Did the agent greet the customer?”. Greeting phrases in different languages are searched in agent messages.  Each agent receives their own greeting score, which is [accessible in the conversation](#creating_custom_autoqa_categories) and in the [AutoQA dashboard](https://support.zendesk.com/hc/en-us/articles/9019507481242#topic_b4n_tpv_q2c). Agents who use a greeting receive a positive score. Agents who don't use a greeting are scored as [N/A](https://support.zendesk.com/hc/en-us/articles/7043701093786#topic_y5g_2cj_4fc), unless they're the first agent in the conversation. If the first agent in the conversation does not use a greeting, that agent receives a negative score.  The [conversation greeting category](https://support.zendesk.com/hc/en-us/articles/7043759449114#topic_vkp_t3k_dgc) receives an upvote only if all agents use a greeting.  The Greeting AutoQA category is available for both text and voice interactions. | Binary: ( , ) | All | English, German, Spanish, French, Italian, Dutch, Polish, Portuguese |
| Empathy | Assesses whether the agent was empathetic towards the customer and their problems.  Each agent receives their own empathy score. However, the conversation empathy category is evaluated positively only if all agents demonstrate empathy. AI agents (bots) results don’t impact agent scores.  Empathy is evaluated negatively if at least one agent doesn’t show empathy.  If the system fails to evaluate empathy, all agents receive a score of [N/A](https://support.zendesk.com/hc/en-us/articles/7043701093786#topic_y5g_2cj_4fc). For example, this can occur if the ticket is too short.  The Empathy AutoQA category is available for both text and voice interactions. | Binary: ( , ) | All | Not available without OpenAI |
| Spelling and grammar | Detects and highlights grammar mistakes, misspellings, and style errors. Error highlighting can be toggled on or off.  The number of grammar mistakes, misspellings, and style errors found for all agents is displayed. Hovering over the highlight shows specific information about the error.  Each agent receives their own spelling and grammar score. | Customizable | English (US),English (UK), German, French, Polish, Spanish, Portuguese (Brazil), Portuguese (Portugal), Dutch | English (US),English (UK), German, French, Polish, Spanish, Portuguese (Brazil), Portuguese (Portugal), Dutch |
| Closing | Evaluates whether the agent closed the conversation properly, including offering further help and thanking the customer. Each agent receives their own closing score, which is [accessible in the conversation](#creating_custom_autoqa_categories) and in the [AutoQA dashboard](https://support.zendesk.com/hc/en-us/articles/9019507481242#topic_b4n_tpv_q2c). Agents who use a closing receive a positive score. Agents who don't use a closing are scored as [N/A](https://support.zendesk.com/hc/en-us/articles/7043701093786#topic_y5g_2cj_4fc), unless they're the last agent in the conversation. If the last agent in the conversation does not use a closing, that agent receives a negative score.  The [conversation closing category](https://support.zendesk.com/hc/en-us/articles/7043759449114#topic_vkp_t3k_dgc) receives an upvote only if all agents use a closing.  The Closing AutoQA category is available for both text and voice interactions. | Binary: ( , ) | All | English, German, Spanish, French, Italian, Dutch, Polish, Portuguese |
| Solution offered | Identifies whether a solution was proposed in the conversation.  Each agent receives their own solution offered score, which is [accessible in the conversation](#creating_custom_autoqa_categories) and in the [AutoQA dashboard](https://support.zendesk.com/hc/en-us/articles/9019507481242#topic_b4n_tpv_q2c). Agents who offer a solution receive a positive score. Agents who don't offer a solution are scored negatively.  The [conversation solution offered category](https://support.zendesk.com/hc/en-us/articles/7043759449114#topic_vkp_t3k_dgc) receives an upvote only if all agents offered a solution.  The Solution AutoQA category is available for both text and voice interactions. | ( , ), or "[N/A](https://support.zendesk.com/hc/en-us/articles/7043701093786#topic_y5g_2cj_4fc)" if not sure | All | Not available without OpenAI |
| Tone | Recognizes tones and calculates a score based on their positive or negative weights.  The conversation tone category is evaluated positively if at least one agent uses a positive tone.  There are seven root categories in total, tied to tones or emotions:   - Cheerful: joyful, fun, excited, friendly, informal  - Supportive: encouraging, supportive, empathetic, appreciative,   optimistic, reassuring, accessible, helpful, informative  - Professional: professional, diplomatic, confident, polite,   formal  - Calm: calm, patient  - Inquisitive: curious, surprised  - Sorry: apologetic, regretful, concerned, worried  - Negative: angry, sad, frustrated, accusatory | Customizable | All | Not available without OpenAI |
| Readability | Analyzes how easily a text can be understood, considering word complexity and sentence length. Complex words and long sentences highlighting can be toggled on or off.  Each agent receives their own spelling and grammar score. | Fixed 3-point scale | English, Spanish | English, Spanish |
| Comprehension | Checks whether the agent understood the customer's issue, possibly requiring clarifying questions or summarizing the problem. The conversation comprehension category is evaluated positively if at least one agent is assessed as having understood the customer’s issue.  The Comprehension AutoQA category is available for both text and voice interactions. | Binary: ( , ) | All | Not available without OpenAI |

## Viewing autoscoring in conversations

Conversations with autoscoring categories are indicated by a hologram icon (
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_hologram.png)) in the Conversations view.

**To access AutoQA in conversations**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Conversations**
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_conversations_icon.png) in the sidebar.
2. Select a conversation.

   You can [use custom filters to find conversations](https://support.zendesk.com/hc/en-us/articles/7043759449114) using AutoQA
   categories to review.
3. In the sidebar on the right, click the **Feedback**
   icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_feedback.png)).
4. View the AutoQA autoscores under Reviews.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_feedback_reviews_autoqa.png)

The [AutoQA dashboard](https://support.zendesk.com/hc/en-us/articles/9019507481242) tracks your teams’ performance across all
AutoQA categories. It’s the best place to track trends over time and identify the training
needs of your teams and individual agents.