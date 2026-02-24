# Best practices for creating AI insights prompts in Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/9464975500954-Best-practices-for-creating-AI-insights-prompts-in-Zendesk-QA

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Explore AI insights prompts to enhance agent performance evaluation by creating custom prompts for quality autoscoring and risk detection. Focus on clarity and objectivity in your prompts, avoiding subjective language. Use metadata criteria like time, tags, and channels to refine assessments. Define clear evaluation outcomes to ensure consistent scoring, aligning with your established criteria.

Location:  Zendesk QA > Settings > AI

Zendesk QA prompt-based AI insights leverage the latest AI models, allowing you
to customize AI-powered prompts using natural language for quality [autoscoring](https://support.zendesk.com/hc/en-us/articles/7043747123354#understanding_autoscoring_categories) and risk detection.

In addition to using or editing prompts from the [AI insights prompt library](https://support.zendesk.com/hc/en-us/articles/9250434748058), you can [create your own AI custom prompt categories](https://support.zendesk.com/hc/en-us/articles/9277382490138) and [spotlights](https://support.zendesk.com/hc/en-us/articles/9327313916570).

By following these guidelines, evaluators can effectively leverage generative
AI to assess customer support agent performance, ensuring clarity, consistency, and a
strong focus on service quality.

This article contains the following topics:

- [Compliance suggestions for
  using Zendesk QA AI prompts](#topic_ylj_4tk_nfc)
- [Writing prompts for AI
  insights](#topic_jqy_st2_m2c)
- [Scoring prompt-based AI
  insights](#topic_zgc_kbr_ffc)

Related articles

- [About AI insights in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/9224552305946)

## Compliance suggestions for using Zendesk QA AI prompts

Zendesk AI is built on our foundational principles of privacy, security,
accuracy, transparency and customer control. See [AI Trust at Zendesk](https://support.zendesk.com/hc/en-us/articles/9196781863578).

Zendesk’s compliance and configuration suggestions are not legal advice.
You, as the user, remain solely responsible for ensuring that your interactions with
the system are fair, respectful, free from discriminatory or derogatory language,
and appropriate for your purposes — including when using prompts from Zendesk’s
prompts library.

We encourage you to maintain a polite tone in all communications, consider
fair usage when creating prompts and implementing outputs, and always verify that
the prompt is suitable for your specific use case.

Custom prompts and any other Zendesk QA AI prompts should not be used to
make automated decisions, especially those related to employment or other high-risk
situations as defined by the EU AI Act. Please be aware that Zendesk does not assume
any responsibility for the consequences of misuse of the system.

## Writing prompts for AI insights

We recommend keeping your prompts simple and focused on a single category
and spotlight at a time. For example, avoid combining topics such as empathy and
grammar in the same prompt. Instead, create separate prompts for each category. This
approach helps the model evaluate each prompt more accurately, as it can be
challenging to determine whether a rating applies to empathy, grammar, or both.

The goal of these prompts is to evaluate the performance of customer
support agents based on service quality using generative AI. Therefore, ensure that
responses can be generated without requiring validation from third-party
applications or internal documentation, as these sources are not accessible to the
AI model.

Write category and spotlight descriptions objectively, avoiding subjective
language and phrasing. Subjective descriptions can result in inconsistent and
non-measurable evaluations.

Be specific when [writing prompts with
criteria that include metadata](#topic_sbq_lw4_jhc), such as time related to tickets, ticket
tags, channel, internal notes, and more.

Below are examples of subjective expressions alongside their objective
alternatives that you should use:

|  |  |
| --- | --- |
| **Instead of** | **Use** |
| *friendly* | “*demonstrated courtesy*" or "*used polite language*" |
| *attentive* | *responded to customer inquiries*" or "*addressed customer needs*" |
| *helpful* | "*provided relevant information*” or "*resolved the issue presented*" |
| *professional* | "*maintained a formal tone*" |
| *confident* | “*provided clear explanations*" |
| *polite* | "*used polite language*" or "*acknowledged the customer appropriately*" |
| Vague adverbs and adjectives (i.e., *very*, *really*, *absolutely*, *a bit*) | Adverbs and adjectives can often be omitted, but when used should be objective and measurable. |

In addition to using objective descriptions, evaluations should also be
based solely on the conversation text. Ensure that you clearly define the rating
criteria for each evaluation. For example:

- **Use specific criteria**. Focus on specific behaviors or actions
  taken by the agent rather than general feelings or impressions.
  - **Instead of**: *Was the agent friendly?*
  - **Use**: *Did the agent use polite language, maintain a
    formal tone and acknowledge the customer appropriately?*

- **Define expectations clearly**. Outline what constitutes
  satisfactory performance for each criterion to minimize subjectivity.
  - **Instead of**: *Did the agent communicate well?*
  - **Use**: *Did the agent use polite language, avoid
    derogatory words and slang? Evaluate the agent negatively, if they
    failed all three criteria. Rate positively if they avoided
    derogatory words and slang, but used polite language
    otherwise.*

- **Use consistent terminology**. Maintain uniform language
  throughout all rating descriptions. Use a single term consistently.
  - **Instead of**: Using a variety of terms, such as
    "*colleague*," "*employee*," "*representative*,"
    "*advocate*," and "*associate*"
  - **Use**: “*agent*”
  - - **Instead of**: "*member*," "*caller*,"
      "*guest*," and "*subscriber*"

      **Use**:
      “*customer*”

- **Do not use acronyms and abbreviations.**
  - **Instead of**: *Did the agent confirm the customer’s
    DOB?*
  - **Use**: *Did the agent confirm the customer’s date of
    birth?*

- **Don’t use double quotes unless necessary.** Use double quotes
  only when referencing exact words spoken by the agent or customer. This approach
  allows for a broader evaluation of intent or sentiment without restricting
  assessments to specific phrasing.
- - **Instead of**: "*Did the agent say “Have a nice
    day?”*"
  - **Use**: *The agent wished the customer a nice day.*

- **Provide examples** of acceptable and unacceptable responses to
  guide evaluators in their assessments. When questions require knowledge of
  specific business terminology, explicitly define those terms in the
  instructions.
  - **Instead of**: “*The agent must mention the department
    name in their greeting.*”
  - **Use**: “*The agent must mention one of the department
    names from the list below in their greeting.*” (Provide a list of
    acceptable department names.)

- **Be clear about your rating conditions**. Explicitly state whether
  all conditions described must be met or if meeting only some is sufficient for a
  good rating. This clarity improves consistency and reliability in scoring.
  - **Instead of**: *Did the agent confirm the customer’s
    booking number and name?*
  - **Use**: *Did the agent confirm either the customer’s
    booking number or name?*
  - **Use**: *Did the agent confirm the customer’s booking
    number and name? Both have to be confirmed.*

- **Write your rating criteria in affirmative language rather than
  negative**. This positive framing can lead to clearer and more effective
  evaluations.
  - **Instead of**: *The agent didn’t use derogatory
    words.*
  - **Use**: *The agent used polite and respectful
    language.*

### Writing prompts with metadata

When writing prompts with criteria that include metadata, such as time
related to tickets, ticket tags, channels, internal notes, and more, follow
these guidelines:

- Describe specifically what time interests you.
  - **Instead of**: Using generic terms like “*correct
    time*” or “*timely manner.*”
  - **Use**: *Did the agent respond to the customer's
    initial message within 2 minutes?*

- Do not use complex time formulas.
  - **Instead of**: *The sum of all times between
    messages should be less than 10 minutes.*
  - **Use**: *Did the conversation last longer than 10
    minutes from start to resolution?*

- Do not rely on timezone information.
  - **Instead of:**
    *Responded in 30 minutes if the customer is in the same time
    zone.*
  - **Use**: *Did the agent respond to each customer
    message within 30 seconds throughout the conversation?*

- Be specific about the channel you’re interested in.
  - **Instead of**: Using generic terms like “*correct
    channel*” or “*most popular channel.*”
  - **Use**: *If the channel is email, did the agent
    request additional verification before processing the account
    change?*
  - **Use**: *If the channel is chat, did the agent offer
    to escalate to a phone call for complex technical
    issues?*
  - **Use**: *If the channel is phone, did the agent
    verbally confirm the customer's email address before sending
    documentation?*

- Be specific about the notes you’re interested in. Use words like
  “*internal notes*”, “*non-public messages*”, etc. Notes
  outside of the conversation are not accessible to the model by default. If
  your procedure requires accessing notes outside of the help desk, we cannot
  analyze that information.
  - **Instead of**: Asking about notes outside of the
    conversation, such as “*Did the agent create a Jira
    ticket?*”
  - **Use**: *If there was an escalation, did the agent
    note it down in the internal notes?*
  - **Use**: *Did the agent record the customer's
    preferred callback time in the internal notes?*
  - **Use**: *Did the agent document the resolution
    method used in the non-public messages for future
    reference?*

- Be specific about the tags you’re interested in. Ideally, provide
  a list of all the tags if it's not too long, for example, "*We use tags
  "abc", "def", and "ghi". Did the agent use any of those tags?*”
  - **Instead of**: Using generic terms like “*correct
    tag*”.
  - **Use**: *Did the agent use the "escalated\_to\_ticket"
    tag when escalating the customer issue?*
  - **Use**: *Did the agent apply the "billing\_dispute"
    tag when the customer complained about incorrect
    charges?*
  - **Use**: *We use tags "product\_a", "product\_b" and
    "product\_c". Did the agent use any of those tags when discussing
    product features?*

## Scoring prompt-based AI insights

After establishing your prompt, the next step is to define how evaluations
are applied. This involves specifying what constitutes a positive or negative
outcome and selecting clear terms or phrases to represent these outcomes. Examples
include yes/no, helpful/unhelpful, or polite/impolite.

Assigning the correct outcomes based on your rating criteria is essential
to ensure accurate evaluations.

Below are examples illustrating how to structure these evaluations:

- **Politeness of language**:
  - Question: *Did the agent use polite language?*
    - Positive outcome: *Yes*
    - Negative outcome: *No*

- **Use of derogatory words**:
  - Question: *Did the agent use derogatory words?*
    - Positive outcome: *No*
    - Negative outcome: *Yes*

By clearly defining these parameters, you ensure that evaluations are
consistent, aligned with your established rating criteria, and accurately reflected
in your [AQS scores](https://support.zendesk.com/hc/en-us/articles/9019507481242#topic_b4n_tpv_q2c).