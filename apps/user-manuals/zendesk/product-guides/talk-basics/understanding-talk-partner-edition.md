# Understanding Talk Partner Edition

Source: https://support.zendesk.com/hc/en-us/articles/4408819751194-Understanding-Talk-Partner-Edition

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

For businesses with an existing phone support solution or sophisticated
telephony needs, Talk Partner Edition enables you to choose your own call center
software and integrate it with Zendesk’s omnichannel solution.

To get started right away, we have over 130 pre-built telephony integrations
that plug right into Zendesk. Otherwise, you can use our CTI toolkit to build your own
integration with your preferred call center solution.

Note: If you have a legacy plan and are using the Support Productivity Pack, the Talk Partner edition is included by default for the number of agents you have. Otherwise, legacy plans require Talk Partner Licenses for all agents using the third-party Voice app inside Zendesk.

This article contains the following sections:

- [Why use Talk Partner
  Edition?](#topic_hwl_ghb_nlb)
- [How to use Talk Partner
  Edition?](#topic_jl3_khb_nlb)
- [What telephony integrations are available?](#topic_zgp_lhb_nlb)
- [What are the features of Talk Partner
  Edition?](#topic_m3f_4y1_yyb)
- [Further reading](#topic_ep3_mhb_nlb)

## Why use Talk Partner Edition?

Although you use Zendesk Support, we realize that you might use a call center
solution other than Zendesk Talk that you want to connect to Zendesk’s omnichannel
experience. With Talk Partner Edition, you can use [130+ pre-built telephony integrations](https://www.zendesk.com/apps/directory/?q=&idx=appsIndex&p=0&dFR%5Bcategories.name%5D%5B0%5D=CTI%20Providers) that
plug directly into Support, or use the [Talk Partner Edition API](https://developer.zendesk.com/rest_api/docs/talk-partner-edition-api/introduction) to write your own
integrations.

## How to use Talk Partner Edition?

If you don’t want to use the pre-built integrations, the [Talk Partner Edition developer guide](https://developer.zendesk.com/documentation/voice/talk-partner-edition/integrating-telephony-systems-with-talk-partner-edition/) contains a wealth
of information to help you integrate your existing call center solution with Zendesk
products.

With the [Talk Partner Edition API](https://developer.zendesk.com/api-reference/voice/talk-partner-edition-api/introduction/) you can configure
telephony requests to trigger actions in Zendesk Support, for example:

- Identifying an agent based on the phone device
- Creating a ticket and displaying it to an agent
- Opening an existing ticket for an agent
- Displaying a user’s profile to an agent
- Adding a recording or transcription to a ticket
- Creating a voicemail ticket

You can try out Talk Partner Edition when you are on a trial or paid subscription of
Zendesk Suite. For more details and examples, see the [Talk Partner Edition developer guide](https://developer.zendesk.com/documentation/voice/talk-partner-edition/integrating-telephony-systems-with-talk-partner-edition/).

## What telephony integrations are available?

Currently, there are over 90 apps designed to help you integrate your call center
software with Support. Examples include:

- [Five9](https://www.zendesk.com/marketplace/apps/support/91303/five9-plus-adapter-for-zendesk/)
- [Aircall](https://www.zendesk.com/marketplace/apps/support/65522/aircall-for-support/)
- [55PBX](https://www.zendesk.com/marketplace/apps/support/93858/55pbx-softphone-pabx-virtual/)
- [Babelforce](https://www.zendesk.com/marketplace/apps/support/914359/babelconnect/)

For a full list, see the [Zendesk Apps Marketplace](https://www.zendesk.com/apps/directory/#CTI_Providers).

Note: When you create reports with Explore, only information associated with Zendesk
tickets is available. If you want to report on information from a third-party
app, use the reporting solution associated with that app.

## What are the features of Talk Partner Edition?

[Talk Partner Edition (TPE) APIs](https://www.zendesk.com/service/voice/talk-partner-edition/) has two
features to help with Computer Telephony Integrations (CTI): Standard Call
Object and Voice Comment. You can use Standard Call Object to store
third-party, industry-standard call data in Zendesk. Voice comment is for Talk
Partner Edition-based apps and is ideal for voicemails. For example, to display
information such as the end-user number, the name of the agent that took the call,
or the call duration.

### Standard Call Object

The [Standard Call Object](https://developer.zendesk.com/documentation/voice/talk-partner-edition/creating-a-call-record-in-zendesk/) is a foundational feature that works well with
**third-party call integration with Explore**, and can store
third-party, industry-standard call data in Zendesk. CTI integrations must
save only their call data in the standard call object. Zendesk manages the object's storage and
visualization.

Previously, CTI integrations could either store their call data in custom ticket fields or tags, which made the data visible in Explore, or use ticket comments to display the call data within the ticket.
However, each of these options had downsides.

Storing call data in custom ticket fields meant that if a ticket involved
multiple calls, and the CTI integration updated the ticket with data from the
latest call, the information from the previous call would be lost. Similarly, tags aren't
intended for structured data and ticket comments aren't suited to
presenting long lists of tabular data. Additionally, all of these options add clutter to tickets.

### Voice Comment

A Voice Comment is a special type of comment currently used by both Talk Partner
Edition-based apps and Zendesk Talk to display information from calls. This
includes:

- End-user number
- Name of the agent that answered the call,
- The duration of the call
- Display of the controls to play call recordings directly in the
  ticket

Voice comments are perfect for voicemails as they are short and always come with
an audio recording. However, sometimes they are too limited to meet all the needs of CTI integrations.

The enhanced [TPE Voice Comment](https://developer.zendesk.com/documentation/voice/talk-partner-edition/creating-a-voice-comment-in-ticket/) architecture,
developed exclusively for TPE, works in conjunction with the standard call
object. After the data is stored in the call object, partners tell Zendesk which
call record they want to pull data from, and which fields they want to display
in the comment. Zendesk Talk then presents the data in the ticket.

## Further reading

See the following resources for more help with Talk Partner Edition:

- [Talk Partner Edition website](https://www.zendesk.com/talk/talk-partner-edition/)
- [Talk Partner Edition developer
  guide](https://developer.zendesk.com/documentation/voice/talk-partner-edition/integrating-telephony-systems-with-talk-partner-edition/)