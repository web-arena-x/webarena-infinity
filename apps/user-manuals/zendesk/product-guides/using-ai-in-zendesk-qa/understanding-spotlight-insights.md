# Understanding spotlight insights

Source: https://support.zendesk.com/hc/en-us/articles/7043759586074-Understanding-spotlight-insights

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Spotlight insights enhance your QA process by automatically highlighting key interactions for review, using predefined insights like outliers, churn risk, and exceptional service. This tool helps you identify improvement opportunities by analyzing conversations and tagging them with performance indicators. Access insights through the Feedback section to quickly assess and address customer interactions, improving your team's response and service quality.

Location: Zendesk QA > Settings > Spotlight

In addition to [automatically scoring specific categories](https://support.zendesk.com/hc/en-us/articles/7043747123354) within scorecards, you can use spotlight insights to further streamline your Quality assurance (QA) process.

This article contains the following topics:

- [About spotlight insights](#topic_u4j_rth_xdc)
- [About the standard spotlight insights](#topic_lmq_fvh_xdc)
- [About the spotlight insight tag types](#topic_edt_gbn_q2c)

**Related articles**

- [Editing spotlight insights](https://support.zendesk.com/hc/en-us/articles/8992300083226)
- [Creating custom spotlight insights](https://support.zendesk.com/hc/en-us/articles/8992282733850)

## About spotlight insights

Spotlight is a discovery tool in Zendesk QA that enhances and accelerates your evaluation process by highlighting valuable opportunities for improvement and learning. It analyzes all team interactions, automatically surfacing newly synced closed conversations by identifying and labeling specific keywords or phrases. Spotlight also offers various out-of-the-box insights to help you identify specific events or signals for further analysis.

In addition to the details in this article, this video provides a helpful visual overview of spotlight.

## About the standard spotlight insights

Spotlight offers predefined insights to help you identify specific events or signals for further analysis. Some require [LLM-based AutoQA](https://support.zendesk.com/hc/en-us/articles/7043669430426#topic_wsw_cly_ydc) to be enabled for functioning.

The following predefined spotlight insights automatically surface newly synced closed conversations in Zendesk QA:

- [Outliers](#topic_lmq_fvh_xdc__outliers)
- [Churn risk](#topic_lmq_fvh_xdc__churn_risk)
- [Escalation](#topic_lmq_fvh_xdc__escalation)
- [Follow up](#topic_lmq_fvh_xdc__follow_up)
- [Exceptional service](#topic_lmq_fvh_xdc__exceptional_service)
- [Sentiment](#topic_lmq_fvh_xdc__sentiment)
- [SLA](#topic_lmq_fvh_xdc__sla)
- [Bot communication efficiency](#topic_lmq_fvh_xdc__bot_communication)
- [Bot repetition](#topic_lmq_fvh_xdc__bot_repetition)
- [Dead air (voice)](#topic_lmq_fvh_xdc__dead_air)
- [Recording disclosure missing (voice)](#topic_lmq_fvh_xdc__recording_missing)

| | | |
| --- | --- | --- |
| **Spotlight insight name** | **Description** | [**LLM-based AutoQA**](https://support.zendesk.com/hc/en-us/articles/7043669430426#topic_wsw_cly_ydc)**required?** |
| Outliers | Offers the highest learning potential by allowing you to find critical conversations for review with a single click. It automatically identifies must-review interactions that are atypical or unusual for the team. It’s available in over 100 languages. Flags conversations where:   - The customer's problem could not be explained in one message. - The agent needed to ask for further information to understand the   request. - There were more replies than average from both the customer and   agent. - The length of replies was longer than average | No |
| Churn risk | Highlights conversations where customers express a potential risk of attrition. It identifies instances where customers explicitly mention canceling their subscription or switching to a competitor. The Churn risk insight is available in the 100+ languages supported by OpenAI. | Yes |
| Escalation | Flags conversations where the customer requests to speak with a higher-level representative, such as a manager. It does not detect internal escalation processes that occur outside the conversation. It’s available in the 100+ languages supported by OpenAI. | Yes |
| Follow up | Flags instances where a support representative has promised to take a future course of action. It does not assess the validity of the action, only whether it was completed. It’s available in the 100+ languages supported by OpenAI. | Yes |
| Exceptional service | Identifies instances where a support representative provided exceptional service and the customer expressed gratitude. It’s available in the 100+ languages supported by OpenAI. | Yes |
| Sentiment | Detects both negative and positive sentiments in conversations, enabling you to identify dissatisfaction or delight and address critical issues. Understanding how customers feel when interacting with your support team through sentiment analysis helps you assess your agents' empathy skills and tone when handling difficult situations. It's currently available in English, Spanish, French, German, Polish, Italian, Dutch, Portuguese, Turkish, Japanese, and Swedish. | No |
| SLA | Detects whether the [service level agreement (SLA)](https://support.zendesk.com/hc/en-us/articles/5600997516058), which specifies and measures the response and resolution times that your support team provides to customers, has been breached. | No |
| Bot communication efficiency | Compares your bot’s conversation handling to that of average agents. It returns an efficiency percentage that indicates whether interacting with the bot resolved the issue faster and with fewer questions than speaking with a human. Efficiency percentages under 20% are not returned. | No |
| Bot repetition | Reports when the bot is stuck in a loop and repeating the same message to the customer. Filter values include "detected" and "not detected". | No |
| Dead air (voice) | Highlights calls where the gap between consecutive messages exceeds the set threshold. The default industry threshold is 30 seconds, but [it can be adjusted to any duration](https://support.zendesk.com/hc/en-us/articles/8992300083226#topic_hvj_hvh_xdc). | No |
| Recording disclosure missing (voice) | Detects whether the speaker discloses that the conversation is being recorded. It can be customized to [specify which conversations it applies to](https://support.zendesk.com/hc/en-us/articles/8992300083226#topic_hvj_hvh_xdc). | Yes |

## About the spotlight insight tag types

Spotlight insights are available by accessing the “Feedback” section of a conversation, regardless of whether you access that conversation via a [dashboard](https://support.zendesk.com/hc/en-us/articles/7043701144858#topic_rnw_zjx_vfc), the [Conversations view](https://support.zendesk.com/hc/en-us/articles/7043661945370#topic_wsw_cly_ydc), the [Assignments view](https://support.zendesk.com/hc/en-us/articles/7043747327770#topic_g5y_dw1_cbc__section_xx1_nsc_tcc), or the [Reviews view](https://support.zendesk.com/hc/en-us/articles/7043760283546#topic_wsw_cly_ydc).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_feedback_spotlight.png)

The following icons serve as visual indicators of performance for each spotlight:

- A yellow exclamation mark icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_negative_spotlight.png)) indicates negative feedback.
- A gray eye icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_neutral_spotlight.png)) indicates neutral feedback.
- A green happy face icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_positive_spotlight.png)) indicates positive feedback.