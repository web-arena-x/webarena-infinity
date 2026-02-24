# Understanding conversation filter types in Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/7043759449114-Understanding-conversation-filter-types-in-Zendesk-QA

---

Conversation filters in Zendesk QA allow you to quickly locate specific conversations for review based on your chosen criteria. Bysetting up custom filters, you streamline your review process and ensure that you focus on the conversations that matter most. This article describes the filters that are available when you set up a custom filter.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Conversation filters help you find specific conversations for review based on criteria like date, attributes, and help desk metrics. By setting up custom filters, you can streamline your review process, focusing on the most relevant conversations. Filters include options for date ranges, conversation status, participants, and more, allowing you to tailor your search to your needs.

Location:  Zendesk QA > Conversations

Conversation filters in Zendesk QA allow you to quickly locate specific
conversations for review based on your chosen criteria. By [setting up custom filters](https://support.zendesk.com/hc/en-us/articles/7043669455130), you streamline your review process and
ensure that you focus on the conversations that matter most. This article describes the
filters that are available when you set up a custom filter.

This article contains the following topics:

- [Filters based on date](#topic_vgp_mw2_dgc)
- [Filters based on conversation
  attributes](#topic_ccj_hhk_dgc)
- [Filters based on help desk
  metrics](#topic_as3_tyk_dgc)

## Filters based on date

This section includes filters for specific time frames, such as when a conversation was
created, updated, or resolved.

The following date-based filters are available:

|  |  |  |
| --- | --- | --- |
| **Date filter name** | **Description** | **Time frame** |
| Closed date | Find conversations based on when they were closed in your help desk. | For each conversation action you can select the following time frames:  - last 24h - today - yesterday - last 7 days - last 14 days - this week - last week - last 30 days - this month - last month - from - until |
| Commented date | Find conversations based on when a comment was left on a conversation in Zendesk QA, either as a part of the review or a standalone comment. |
| Created date | Find conversations that were started by customers in a certain period of time. |
| CSAT survey reply date | Find conversations based on the date when the survey reply was sent. |
| CSAT survey sent date | Find conversations based on the date when the survey was sent out. |
| Last reply date | Find conversations based on the last time a reply was sent to your customer. |
| Reviewed date | Find conversations that have already been reviewed. You may want to revisit conversations that have already been reviewed to enhance the quality of your evaluations or to use them for [calibration](https://support.zendesk.com/hc/en-us/articles/7043724530842) purposes, ensuring consistency in your assessment process. |
| Updated date | The updated date filter rule displays all conversations that have had actions performed on them, such as being closed, new replies being received, or new internal notes being added. |

## Filters based on conversation attributes

This section includes filters based on conversation attributes, including status,
assignee, tags, and other relevant details. Conversation filters are grouped by the
following types:

- [Intelligent filters](#topic_zl3_5bg_nhc)
- [Categories (AutoQA)](#topic_vkp_t3k_dgc)
- [Custom categories](#topic_yw3_qyk_dgc)
- [Information](#topic_rr1_l1l_dgc)
- [Metrics](#topic_h1f_ryk_dgc)
- [Participants](#topic_b4m_ryk_dgc)
- [Review and feedback](#topic_nkv_ryk_dgc)
- [Spotlight](#topic_cnd_syk_dgc)
- [Custom spotlight](#topic_bk5_syk_dgc)

The following conversation based filters are available:

### Intelligent filters

AI-powered filters that automatically detect a set of predefined
conditions.

|  |  |  |
| --- | --- | --- |
| **Conversation filter name** | **Description** | **Condition** |
| Agent escalations | Conversations in which tickets were escalated only by human agents | Select the condition score using the following options:   - detected - not detected |
| AI agent conversations | Conversations handled only by AI agents |
| AI agent escalations | Conversations in which tickets handled by AI agents were escalated to human agents for further assistance |
| AI evaluated | Conversations in which AI evaluation is completed |
| Frustrated AI agent conversations | Conversations where customers were frustrated while interacting with an AI agent |
| Low scoring categories | Conversations with at least one category scoring below 50% |

### Categories (AutoQA) conversation filters

Autoscoring automatically evaluates and scores customer interactions for 100% of your
ticket volume based on predefined [categories](https://support.zendesk.com/hc/en-us/articles/7043712922522).

|  |  |  |
| --- | --- | --- |
| **Conversation filter name** | **Description** | **Condition** |
| Closing | Analyzes if the agent wrapped up the conversation politely | Select the condition score using the following options:  - is - is not |
| Comprehension | Analyzes whether the agent understands the customer's query or concern |
| Empathy | Analyzes whether the agent understands and acknowledges the customers' feelings |
| Greeting | Analyzes the entire conversation for typical greeting phrases |
| Rating category | Categories used to rate or evaluate the conversation | Select the condition name using the following options:  - is - is not |
| Readability | Analyzes how easily a text can be understood,considering word complexity and sentence length | Select the condition score using the following options:  - is - is not |
| Solution offered | Analyzes the entire conversation for an offered solution |
| Spelling and grammar | Analyzes agent's grammar, spelling and style mistakes |
| Tone | Analyzes agent's tone throughout the conversation |

### Custom categories conversation filters

These are filters based on the [custom rating categories](https://support.zendesk.com/hc/en-us/articles/7043712922522) you have created. You can select their
condition scores by ‘is’ or is ‘not’.

### Information conversation filters

These are filters based on the information contained in the conversations.

|  |  |  |
| --- | --- | --- |
| **Conversation filter name** | **Description** | **Condition** |
| Call | Whether conversation contains phone call(s) | Select the condition using the following options:  - exists - does not exist |
| Call transcript content | The content of a transcription in a conversation | Select the condition using the following options:  - is - is not |
| Conversation brand | The brand or specific product/service associated with the conversation |
| Conversation channel | Find conversations based on the communication channel such as email, chat, voice, or api. |
| Conversation content | Find conversations containing a specific key word or phrase in the textual conversations (does not work for call transcripts). | Select the condition using the following options:  - is - is not - contains - does not contain |
| Conversation description | Find conversations based on the first message in the conversation. |
| Conversation form | The form or template used for structuring the conversation | Select the condition using the following options:  - is - is not |
| Conversation group | Find conversations based on the group they belong to in your help desk. |
| Conversation priority | The priority level assigned to the conversation |
| Conversation status | Find conversations based on the current status (e.g. open, pending, closed, solved). |
| Conversation subject | Find conversations based on the subject or the topic of the conversation. | Select the condition using the following options:  - is - is not - contains - does not contain |
| Conversation type | Find conversations based on the type or category that describes the nature of the conversation (e.g. inbound, outbound). | Select the condition using the following options:  - is - is not |
| Help desk tag | Find conversations based on the tags from your help desk. |
| Language (AI) | Find conversations based on their language. |
| Message channel | The communication channel used for the conversation (e.g. email, chat) |
| Starred | Find conversations that were starred either by you or other team members. | Select the condition using the following options:  - starred by me - not starred by me |
| Transcript | Find conversations with a transcript of the call recording. | Select the condition using the following options:  - exists - does not exist |
| Viewed status | Find conversations which were or weren't viewed by the currently logged in user. | Select the condition using the following options:  - viewed - not viewed |

### Metrics conversation filters

|  |  |  |
| --- | --- | --- |
| **Conversation filter name** | **Description** | **Condition** |
| Agent reply count (AI) | Find conversations based on a specific number of messages sent by the agent(s). | Select the condition using the following options:  - less than - more than - is - up until - starting from |
| Average character count (AI) | Find conversations with a specific character number. |
| Average word count (AI) | Find conversations of a certain length. |
| AI agent reply count | Number of AI agent replies in conversations |
| Call duration (in seconds) | Find only phone call recordings of a certain duration. That way you can focus on giving reviews to calls of a certain length. |
| Conversation private note count (AI) | Find conversations that contain internal notes. |
| Conversation reply count | Find conversations based on the replies sent by both the agent and the customer (including internal notes). |
| CSAT per message | Find conversations with satisfaction scores per individual message. | Select the condition using the following options:  - less than - more than - is - is not - up until - starting from |
| Customer reply count (AI) | Find conversations based on the number of replies sent by your customer. | Select the condition using the following options:  - less than - more than - is - up until - starting from |
| Most active agent (AI) | Find conversations based on the name of the most active agent in conversations handled by multiple support reps. | Select the condition using the following options:  - is - is not |
| Number of participating agents (AI) | Find conversations based on the number of agents who were participating in a conversation (including the ones who left an internal note). | Select the condition using the following options:  - less than - more than - is - up until - starting from |
| Public reply count (AI) | Find conversations based on the number of messages by the agent (internal notes not included) and the customer. |
| Satisfaction score (CSAT) | Find conversations based on the feedback result. | Select the condition using the following options:  - is - is not |

### Participants conversation filters

|  |  |  |
| --- | --- | --- |
| **Conversation filter name** | **Description** | **Condition** |
| Assignee | Assignee filter rules will help you focus on a particular user or the entire group. You can select just one or multiple users as Assignees or exclude some of them from your filter. | Select the condition using the following options:   - is - is not |
| AI agent | Find conversations based on which AI agent was involved in the conversation. |
| AI agent type | Find conversations based on which type of AI agent (workflow or generative) was involved in the conversation. |
| External ID | Find conversations based on the external reference ID linked to the conversation. |
| Participant | Find conversations based on who participated in it (including users who have left internal notes). |
| Phone number | Find conversations based on the phone number (e.g. your customer's phone number). |
| Public participant | Find conversations based on the agents who sent messages to your customers. |
| Related email | Find conversations based on an email address that was included in the conversation. | Select the condition using the following options:  - is - is not - contains - does not contain |
| Reviewed by | Find conversations based on who the reviewer was (or wasn't). | Select the condition using the following options:  - is - is not |
| Reviewee | Find conversations based on who the recipient of the review was (or wasn't). |

### Review and feedback conversation filters

|  |  |  |
| --- | --- | --- |
| **Conversation filter name** | **Description** | **Condition** |
| Comment | Find conversations which contain (or don't) a review with a comment or a standalone comment. | Select the condition using the following options:  - commented - has not commented - commented by me - not commented by me - my comment has replies |
| Comment hashtag | Find conversations based on a hashtag in a review. | Select the condition using the following options:  - is - is not |
| Comment tag | Find conversations based on a tag in a review. |
| Dispute | Find conversations which were disputed. | Select the condition using the following options:  - exists - does not exist |
| Review status | Find conversations which were or weren't reviewed. | Select the condition using the following options:  - reviewed - not reviewed - reviewed by me - not reviewed by me |
| Review viewed | Find conversations which were reviewed and check if the reviewee has seen it or not. | Select the condition using the following options:  - viewed - not viewed |
| Reviewed scorecard | Find conversations based on the scorecard that was used to leave the review. | Select the condition using the following options:  - is - is not |
| Source type | Find conversations based on the source type. |

### Spotlight conversation filters

These are filters based on [spotlight insights](https://support.zendesk.com/hc/en-us/articles/7043759586074).

|  |  |  |
| --- | --- | --- |
| **Conversation filter name** | **Description** | **Condition** |
| AI agent communication efficiency | Compares your AI agent's conversation handling against average agents | Select the condition using the following options:  - better than agents - worse than agents |
| AI agent repetition | AI agent is stuck in a loop, repeating the same message in consecutive turns | Select the condition using the following options:  - detected - not detected |
| Churn risk | Signs of customer attrition. Customer was considering a switch or promise to part ways | - detected |
| Dead air | Silence between the agent and the customer exceeded the threshold |
| Escalation | Customer sought higher-level assistance |
| Exceptional service | The customer expressed extreme gratitude or was very satisfied with the support received. |
| Follow up | Either the customer or agent explicitly requested a follow-up | Select the condition using the following options:  - detected - not detected |
| Ineligible for review | Conversations that are ineligible for review through Al analysis | Select the condition using the following options:  - yes - no |
| Outlier | Conversation was unusual or atypical and there was more back-and-forth to reach resolution | - detected |
| Recording disclosure missing | Automatically identify calls lacking the mandatory disclosure statement, like 'This call will be recorded' and similar. |
| Sentiment | Positive and negative sentiment detected in the conversation | Select the condition using the following options:  - positive - negative |
| SLA | A [service level agreement (SLA)](https://support.zendesk.com/hc/en-us/articles/5600997516058), is a policy you define that specifies and measures the response and resolution times that your support team delivers to your customers. | Select the condition using the following options:  - breached - not breached |

### Custom spotlight conversation filters

These are filters based on the [custom spotlight insights](https://support.zendesk.com/hc/en-us/articles/8992282733850) you have created. You can select their
condition scores by ‘is’ or is ‘not’.

## Filters based on help desk

Depending on the data that is available from your [help desk connection](https://support.zendesk.com/hc/en-us/articles/7043712839450), you might see custom filters that reflect
your help desk setup.