# Using real-time AI suggestions for voice calls

Source: https://support.zendesk.com/hc/en-us/articles/9752130101914-Using-real-time-AI-suggestions-for-voice-calls

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Real-time AI suggestions for voice calls provide agents with immediate, context-aware help from your help center during calls. This feature transcribes calls, analyzes them, and offers relevant article-based suggestions, enhancing issue resolution. Considerations include transcription costs, language settings, and data processing regions. Admins must enable this feature, and agents can interact with suggestions during calls for improved customer support.

Important: There are additional costs involved in transcribing calls in real-time. See
[Zendesk number availability and pricing](https://support.zendesk.com/hc/en-us/articles/4408846483482)
for real-time transcription costs.

Real-time AI suggestions for voice calls gives your call center agents immediate,
context-aware suggestions about how to assist the customer they’re talking to. These
suggestions are pulled from your organization’s Zendesk help center including any
support articles, policies, troubleshooting guides, and internal FAQs you may have.

This feature gives agents the support they need to resolve customer issues efficiently
and confidently on calls. By using this feature, agents can resolve calls faster and
provide a better support experience.

This article contains the following topics:

- [About real-time AI suggestions for voice calls](#topic_hzk_wmx_5gc)
- [Considerations for using real-time AI suggestions for voice calls](#topic_isj_mbm_tgc)
- [Turning on real-time AI suggestions for voice calls](#topic_ejj_1xl_tgc)
- [Generating real-time AI suggestions during a call](#topic_x4j_bxl_tgc)

## About real-time AI suggestions for voice calls

When you turn on this feature, calls are transcribed into text in real
time. When an agent requests a suggestion, generative AI analyzes the live
transcript to determine the reason for the customer’s call. Then it automatically
searches the help center for relevant articles to help resolve the issue.

The AI provides a natural language answer, supported by information from
one or more articles. These suggestions appear in the Knowledge tab in the ticket as
digestible, bite-sized pieces of information, helping agents stay focused during the
call.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_t2.png)

### Considerations for using real-time AI suggestions for voice calls

Before you start generating real-time suggestions, it’s important to
understand the following considerations:.

- To get the best results, it is important that your help center articles
  cover the most common topics for which you provide support. Otherwise,
  generative AI models might not be able to provide useful suggestions to
  agents.
- When you turn on this feature for a group of agents, calls to the
  agent group will be transcribed in real-time, even if agents in the assigned
  groups do not request AI suggestions. There are additional fees for
  real-time transcription (see note at the beginning of this article).
- When a call is completed, the transcript and summary can be added
  to the ticket if the call summary feature is enabled on that particular
  phone line. See [Using generative AI to create call
  summaries and transcripts on tickets](https://support.zendesk.com/hc/en-us/articles/6170157307162).
- The real-time transcript will be created based on the agent's
  Zendesk profile language. If agents have conversations in languages other
  than their Zendesk profile language, then the feature will not work. For
  example, if a phone conversation happens in English and the agent's Zendesk
  profile language is set to Spanish, then a transcript will not be generated.
- Real-time transcription data will be processed in the US region
  and cannot be processed in other regions at this time.
- It is not possible to redact PII (Personally Identifiable
  Information) such as names, emails, and addresses from real-time transcripts
  at this time.
- For detailed information on transcription language support and
  other transcription related questions, see [Call transcription and Summarization FAQs](call-transcription-and-summarization-faq.md)

## Turning on real-time AI suggestions for voice calls

Before agents can start receiving real-time suggestions, an admin needs to turn it on
in Admin Center.

Note: Call recording is a prerequisite for transcription, as calls
need to be recorded in order for them to be transcribed. [See managing call recording
options](managing-call-recording-options.md).

**To turn on live suggestions**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Agent copilot > Suggestions**.
2. On the Suggestions page, click **Generate live suggestions during phone
   calls**.
3. Under **Who has access,** select the groups for which you want to turn AI
   suggestions on for.
4. Click **Save**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_t0.png)

## Generating real-time AI suggestions during a call

Now that you've turned live suggestions on, you can start generating suggestions
during phone calls.

**How to generate live suggestions during a phone call**

1. During an active phone conversation, click **View Knowledge suggestions** in
   the ticket.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_pilot_2.png)

   The live suggestions open in the
   Knowledge panel.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_pilot_1.png)
2. Review the suggestions and upvote (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cp-t-icon-3.png)), downvote (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cp-t-icon-2.png)), or regenerate (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cp-t-icon-1.png)) them by clicking the appropriate icon below the suggestions.

   Tip: Regenerating a suggestion can be useful if the conversation
   has evolved or pivoted to a new topic, and agents require additional
   help.