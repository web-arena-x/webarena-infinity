# About rating categories for scorecards 

Source: https://support.zendesk.com/hc/en-us/articles/7043712922522-About-rating-categories-for-scorecards

---

Rating categories are used to evaluate customer conversations. Well-defined rating categories streamline the review process and ensure consistent quality assessments in Zendesk Quality assurance (QA). From the rating categories, you can derive theInternal Quality Score (IQS), which provides valuable insights you can use to assess and improve your customer support.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Rating categories for scorecards help you evaluate customer conversations by focusing on key areas like spelling, comprehension, and tone. You can create custom categories tailored to your needs, including manual and AI-based options. Automatic scoring analyzes new conversations, providing insights to improve support quality. Manual categories are scored by human reviewers, offering flexibility in assessing interactions.

Location:  Zendesk QA > Settings > Scorecards

Rating categories are used to evaluate customer conversations. Well-defined rating
categories streamline the review process and ensure consistent quality assessments in Zendesk
Quality assurance (QA). From the rating categories, you can derive the [Internal Quality Score (IQS)](https://support.zendesk.com/hc/en-us/articles/7043701093786#topic_sws_4ww_42c), which provides valuable
insights you can use to assess and improve your customer support.

There are countless ways to [combine rating categories](https://support.zendesk.com/hc/en-us/articles/8992409602842) to build your [scorecard rating system](https://support.zendesk.com/hc/en-us/articles/8875998154906). It may take some trial and error to
identify the right factors to rate in order to accurately assess and improve your customer
support. Zendesk QA includes several [system categories](https://support.zendesk.com/hc/en-us/articles/7043747123354#understanding_autoscoring_categories) that are automatically scored when
active. The following rating categories are among the most commonly used in Zendesk QA and
provide a good starting point:

- **Spelling and grammar**: Did the agent use correct spelling, grammar, and
  punctuation?
- **Comprehension**: Did the agent understand the issue and its root
  cause?
- **Solution offered**: Did the agent follow the correct process and provide an
  appropriate solution according to internal guidelines?
- **Tone of voice**: Was the response personal and aligned with the brand’s
  voice?
- **Closing**: Did the agent anticipate potential issues and go the extra mile
  to resolve them before closing the ticket?

You can [customize some of these categories](https://support.zendesk.com/hc/en-us/articles/9070424158106) and create custom
rating categories tailored to your organization’s specific needs. Specifically, you can
also:

- [Create AI prompt-based categories](https://support.zendesk.com/hc/en-us/articles/9277382490138)
- [Create exact text-match custom rating
  categories](https://support.zendesk.com/hc/en-us/articles/9302967236890)
- [Create manual custom rating categories](https://support.zendesk.com/hc/en-us/articles/10301342601626)

Before creating categories, it’s important to understand the following information
about categories and how they’re used in Zendesk QA:

- [Enabling automatic scoring with AutoQA](https://support.zendesk.com/hc/en-us/articles/7043669430426#topic_wsw_cly_ydc) allows
  Zendesk QA to automatically evaluate and score agents.
- System autoscoring and AI prompt-based categories are indicated by a hologram
  icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_hologram.png)). See [Viewing and managing rating categories for scorecards](https://support.zendesk.com/hc/en-us/articles/8992409602842).
- To ensure proper functionality for prompt-based AI insights, both the *Automatic scoring
  with AutoQA* and the *LLM-based AutoQA* [account settings](https://support.zendesk.com/hc/en-us/articles/7043669430426#topic_wsw_cly_ydc) must be turned on.
- When a new category is created, only new incoming conversations are automatically analyzed
  and rated based on the category conditions. It may take some time for the scores to load due
  to necessary calculations.
- To qualify for analysis, conversations must include at least one message from both the
  customer and the agent, with a minimum word count of 10.
- AutoQA does not evaluate existing conversations, spam conversations, or historical data.
  However, existing conversations with a status of Solved or [Closed](https://support.zendesk.com/hc/en-us/articles/7335734335258) that are updated after the category is added are also
  automatically analyzed and rated. As a result, you may notice a conversation that has
  already been analyzed and rated being analyzed and rated again in a new workspace.
- If no matches are found, "[N/A](https://support.zendesk.com/hc/en-us/articles/7043701093786#topic_y5g_2cj_4fc)" is assigned. AutoQA may also return "N/A" for
  certain categories when there is insufficient information to provide an accurate
  rating.