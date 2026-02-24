# Using real-time AI suggestions in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/10143999626394-Using-real-time-AI-suggestions-in-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

|  |  |
| --- | --- |
| **Add-on** | Copilot |

Real-time AI suggestions for calls in Zendesk Contact Center gives your agents
immediate, context-aware suggestions about how to assist the customer they’re talking
to. These suggestions are pulled from your organization’s Zendesk help center including
any support articles, policies, troubleshooting guides, and internal FAQs you may
have.

This feature gives agents the support they need to resolve customer issues efficiently
and confidently on calls. Using this feature, agents can resolve calls faster and
provide a better support experience.

If you're using Zendesk Voice, see [Using real-time AI suggestions for voice calls](https://support.zendesk.com/hc/en-us/articles/9752130101914).

This article contains the following topics:

- [About real-time AI suggestions for calls](#topic_hzk_wmx_5gc)
- [Generating real-time AI suggestions during a call](#topic_x4j_bxl_tgc)

## About real-time AI suggestions for calls

When you turn on [live voice transcripts](https://support.zendesk.com/hc/en-us/articles/9696174623770) in Contact Center
and you have [Zendesk Copilot](https://support.zendesk.com/hc/en-us/articles/5524125586330), calls are transcribed into text in real
time and agents can request suggestions to advance the ticket while on the call.
Generative AI analyzes the live transcript to determine the reason for the
customer’s call. Then it automatically searches the help center for relevant
articles to help resolve the issue.

The AI provides a natural language answer, supported by information from one or more
articles. When agents request suggestions, these appear in the **Knowledge** tab
in the ticket as digestible, bite-sized pieces of information, helping agents stay
focused during the call.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_call_suggestion_realtime.png)

**Note:** In Admin Center, **Generate live suggestions during phone calls** is
always on, regardless if you turn it on or off. To opt out, submit a request to
[Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).

### Considerations for using real-time AI suggestions for calls

Before you start generating real-time suggestions, to get the best results, it's
important that your help center articles cover the most common topics for which you
provide support. Otherwise, generative AI models might not be able to provide useful
suggestions to agents.

## Generating real-time AI suggestions during a call

Now that you've set up live suggestions in Contact Center, you can start generating
suggestions during phone calls.

**To generate live suggestions during a phone call**

1. In Agent Workspace, during an active phone conversation, click **View
   knowledge suggestions** in the ticket.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_call_ongoing_suggestions_view.png)

   The live suggestions open in the Knowledge panel.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_call_suggestion_realtime_knowledge.png)
2. (Optional) Review the suggestions and upvote (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cp-t-icon-3.png)) or downvote (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cp-t-icon-2.png)), the suggestions by clicking the appropriate
   icon below the suggestions.

   Upvote when the suggestion is accurate and helpful and downvote when it’s
   off‑topic, incorrect, or outdated. If the conversation has shifted, click
   refresh (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cp-t-icon-1.png)) first. Your votes
   improve future suggestions.
3. Click refresh (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cp-t-icon-1.png)) to regenerate suggestions

   **Tip:** Regenerating a suggestion can be useful if the conversation has
   evolved or pivoted to a new topic, and agents require additional help.