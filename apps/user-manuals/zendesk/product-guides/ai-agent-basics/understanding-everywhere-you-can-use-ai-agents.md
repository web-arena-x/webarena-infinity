# Understanding everywhere you can use AI agents

Source: https://support.zendesk.com/hc/en-us/articles/4408821281818-Understanding-everywhere-you-can-use-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

[AI agents](https://support.zendesk.com/hc/en-us/articles/6970583409690) are available in a number of Zendesk
products and integrations. This article is a guide to all the ways you can use AI
agents.

This article contains the following topics:

- [AI agents on messaging, email, API and web form channels](#topic_ewc_cmf_j4b)
- [Advanced AI agents on messaging and email channels](#topic_lrx_41l_f2c)
- [AI agents for messaging in mobile SDKs](#id_ljw_zyb_kxb)
- [Zendesk AI agents for Slack](#topic_ahj_2cm_ygb)
- [Zendesk AI agents for Microsoft Teams](#topic_e55_sxr_pzb)
- [Zendesk AI agents in Web Widget (Classic)](#topic_eyx_2cm_ygb)
- [APIs for AI agents](#topic_ftf_sfq_zgb)

Related article:

- [AI agent resources](https://support.zendesk.com/hc/en-us/articles/4408834322842)

## AI agents on messaging, email, API and web form channels

With [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690#topic_zps_zmk_f2c), you can create AI
agents across messaging, email, API, and web form channels.

Using generative AI, these AI agents can have back-and-forth conversations with your
customers, potentially resolving requests without ever requiring a human agent. In
cases where a human agent is still needed, the AI agent can gather information
during the handoff that helps human agents get up to speed quickly and resolve
customer issues more efficiently.

**More information:**

- [Getting started with AI agents -
  Essential](https://support.zendesk.com/hc/en-us/articles/6478272212506)

## Advanced AI agents on messaging and email channels

With [AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/6970583409690#topic_zps_zmk_f2c), you can create more
advanced AI agents across messaging and email channels.

These advanced AI agents allow you to automate more complex customer queries, create
scripted conversation flows for specific scenarios, integrate with other systems to
fully automate requests, and benefit from in-depth reporting on your AI agent usage
and automation rates.

**More information:**

- [Getting started with AI agents -
  Advanced](https://support.zendesk.com/hc/en-us/articles/8724978128282)

## AI agents for messaging in mobile SDKs

AI agents for messaging can be a part of your mobile support offering. Our **mobile SDKs**
make it easy to integrate into any mobile app, answering customer questions
in-context without them ever having to leave the app or disrupt their experience.
Users can mark the articles as "solving" their issues, or indicate they still need
help and want to escalate their issue to a Support ticket.

**More information:**

- [Unified SDK for iOS](https://developer.zendesk.com/documentation/classic-web-widget-sdks/unified-sdk/ios/getting-started/)
- [Unified SDK for Android](https://developer.zendesk.com/documentation/classic-web-widget-sdks/unified-sdk/android/getting_started/)

## Zendesk AI agents for Slack

Note: The Zendesk AI agents for Slack integration works only for [supported languages](../multiple-language-support/zendesk-language-support-by-product.md#:~:text=supported%20by%20Zendesk-,AI%20agents,-Language).

When enabled in the [Slack for Zendesk Support integration](https://support.zendesk.com/hc/en-us/articles/4408833756698), the AI agent can
"listen in" on questions posed in any Slack channel configured to use the Support
integration and offer relevant article suggestions:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_answer_bot_convo_new.png)

Users can indicate whether the offered article is useful to them by clicking the
**Yes**
or
**No**
buttons. If more than one article is found, they can
click the
**More suggestions**
button to view additional articles.

If their question is not answered by any of the articles offered, they can submit a
Support ticket:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_answer_bot_new_no.png)

**More information:**

- [Using the AI agents for Slack integration](https://support.zendesk.com/hc/en-us/articles/4408827411098)

## Zendesk AI agents for Microsoft Teams

When enabled in the
[Zendesk integration for Microsoft Teams](https://zendeskforteams.com/user-guide), the bot can
provide article suggestions when a user asks a question as a new conversation:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/answerbot_MSTeams.png)

By default, the AI agent is turned off in channels. An admin or agent can use the **answer
bot** command in a channel to turn on the AI agent and manage settings for
that channel, such as filter article recommendations by help center, labels, or user
segments.

If the AI agent doesn't have an answer, it will prompt the user to create a ticket.

**More information:**

- [Zendesk for Microsoft Teams: Getting
  article recommendations](https://zendeskforteams.com/user-guide#article-recommendations-from-AnswerBot)

## Zendesk AI agents in Web Widget (Classic)

If you have the Web Widget (Classic) installed on your help center or website, your
customers can receive article suggestions whenever they need help across your site,
in a conversational way.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/answerbot_widget_ex.png)

Escalation options to a human agent can always be made available, such as requesting
a
**callback**,
**live chat**
or
**leaving a message**.

**More information:**

- [Enabling and using AI agents in Web Widget
  (Classic)](https://support.zendesk.com/hc/en-us/articles/4408843471642)
- [Configuring AI agents for the Widget
  (Classic)](https://support.zendesk.com/hc/en-us/articles/4408831077018)

## APIs for AI agents

The **Answer Bot API** enables businesses to extend AI-powered self-service help to any
channel. Developers can build their own self-service automation experiences wherever
they’d like. When implemented correctly, users can quickly and easily mark their
questions as resolved or not resolved, giving you more data for reporting, and
improving the AI agent model over time.

**More information:**

- [Answer Bot API](https://developer.zendesk.com/rest_api/docs/answer-bot-api/introduction)