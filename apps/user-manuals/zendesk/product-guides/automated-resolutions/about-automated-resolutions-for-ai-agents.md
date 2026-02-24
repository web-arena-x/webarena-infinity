# About automated resolutions for AI agents

Source: https://support.zendesk.com/hc/en-us/articles/5352026794010-About-automated-resolutions-for-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Automated resolutions are the unit of measurement used for calculating and billing your
account for [AI agent](https://support.zendesk.com/hc/en-us/articles/6970583409690) usage.

Paying per automated resolution means that you pay only for customer requests that were
successfully resolved by the AI agent, without any escalation to a human agent.
Conversations flagged as resolved are also verified by a large language model (LLM),
ensuring its accuracy and delivering a true automation rate.

Zendesk provides tools for [monitoring](https://support.zendesk.com/hc/en-us/articles/8922391373978) and [managing](https://support.zendesk.com/hc/en-us/articles/6958358659226) your automated resolution usage.

This article contains the following topics:

- [Understanding how
  automated resolutions are measured](#topic_m1n_sq4_jwb)
- [Understanding the
  default allocation of automated resolutions per plan and adding
  more](#topic_fcr_sq4_jwb)
- [Finding more information](#topic_kqn_rp1_ccc)

Related articles:

- [Managing your automated
  resolutions](https://support.zendesk.com/hc/en-us/articles/6958358659226)
- [Monitoring your automated resolution
  usage](https://support.zendesk.com/hc/en-us/articles/8922391373978)
- [Turning off automated
  resolution features](https://support.zendesk.com/hc/en-us/articles/7460877856026)

## Understanding how automated resolutions are measured

An automated resolution is counted when a customer’s issue is successfully resolved
without live-agent intervention. Automated resolutions are counted per conversation
rather than per user. A single user’s visits over multiple channels, browsers, or
devices will be considered separate interactions.

There are differences in how and when an issue is deemed resolved, depending on the
channel used. This section explains these differences so you can better understand
your usage.

This section includes the following topics:

- [Automated resolutions in essential AI agents](#topic_dcn_13x_4wb)
- [Automated resolutions in advanced AI agents](#topic_t1f_bqb_g2c)
- [Automated resolutions in autoreplies with articles](#topic_o2r_13x_4wb)
- [Automated resolutions in autoreplies based on intelligent triage](#topic_gww_13x_4wb)
- [Automated resolutions in Web Widget (Classic)](#topic_p4p_zqr_y1c)
- [Actions that don’t contribute to automated resolution calculations](#topic_v2v_yqr_y1c)

### Automated resolutions in essential AI agents

Note: This section applies to all AI
agents available on Suite and Support plans,
including those with legacy functionality. For AI
agents - Advanced, see the [next
section](#topic_t1f_bqb_g2c).

For [AI agents -
Essential](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Essential%20and%20Advanced.-,AI%20agents%20%2D%20Essential,-Included%20in%20all) and [legacy AI agent
functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=AI%20agents%20%2D%20Advanced-,Legacy%20AI%20agent%20functionality,-Customers%20who%20had), automated resolutions are
calculated for AI agents on the following channel types:

- Messaging (including Web Widget, mobile SDK, and
  third-party messaging channels such as Facebook
  Messenger, X Direct Message, Instagram Direct, LINE,
  or WhatsApp)
- Email
- Web form

Note: No automated resolutions are
counted when you test your AI agent using the [testing features in
Admin Center](https://support.zendesk.com/hc/en-us/articles/9462994470810).

#### Automated resolutions for AI agents on messaging channels

An automated resolution is counted after 72 hours of
inactivity if AI evaluation has confirmed that the
AI agent’s response was relevant *and* the last
interaction was one of the following:

- The end user provided positive feedback (“Yes, problem solved”)
  - If no feedback is provided, the conversation will be evaluated using
    AI
- The AI agent shared help center articles in response to the end user’s
  request:
  - If articles were shared using Article Recommendation or an
    article step in an answer flow, the end user must have clicked on at
    least one article link.
  - If articles were shared in a generative reply, the end user
    doesn’t have to click on an article for an automated resolution to be
    counted.
- The end user reached the final step in an answer flow.

The *end user* is anyone who makes a request and
interacts with the AI agent (referred to as a "bot"
in the flowchart below).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/AR_for_conversation_bot.png)

#### Automated resolutions for AI agents on email and web form channels

An automated resolution is counted after 72 hours of
inactivity if all of the following are true:

- The AI agent provided a generative reply based
  on the end user’s question.
- No human agent responded to the ticket created
  by the end user’s request.
- The AI evaluation process confirmed that the AI
  agent’s response was relevant.

### Automated resolutions in advanced AI agents

If you have the [AI agents - Advanced
add-on](https://support.zendesk.com/hc/en-us/articles/8725042447002), automated resolutions apply to both
messaging and email AI agents, and are calculated using the
following logic:

- **For messaging AI agents**: An automated resolution is consumed for
  any conversation that is considered [AI
  agent-handled](https://support.zendesk.com/hc/en-us/articles/9510024609178#:~:text=reply%20was%20sent.-,Handled%20conversations,-%3A%20Conversations%20fully%20handled) and passes the verification
  performed by our LLM.
- **For email AI agents**: An automated resolution is consumed for any
  conversation that is considered Answered (because
  a reply was sent or a public comment was added)
  and passes verification performed by our LLM.
  Adding actions or internal notes only does not
  consume an automated resolution.

The verification process performed by the LLM evaluates the text of the
conversation to ensure that the customer’s request was actually satisfactorily
resolved without human-agent intervention. Conversations that don’t pass this
verification are not considered automated and do not consume an automated
resolution.

Automated resolutions are evaluated at the end of the conversation session
duration, which is determined based on the following
logic:

- **For messaging AI agents**: 2 hours after the first
  message (by default, with a maximum configurable
  duration of 72 hours)
- **For email AI agents**: 72 hours after the first
  message

Only conversations with the handled or answered status are evaluated for
automated resolutions. All escalations change the status of
a conversation to something other than handled or answered.
This means that as soon as a conversation is escalated to a
human agent, it can no longer be counted as an automated
resolution.

Note: For email AI agents, make sure
you've [created the
automation trigger](https://support.zendesk.com/hc/en-us/articles/8357750858010#topic_j5r_psk_m2c). If you don’t, any
replies made by human agents during conversations in
which the email AI agent also participated don't
appear in the [conversation
logs](https://support.zendesk.com/hc/en-us/articles/8357749580186). As a result, automated resolutions
might be consumed for conversations they shouldn't
be.

### Automated resolutions in autoreplies with articles

If you’re using autoreplies with articles, an automated resolution is counted in *either* of
the following situations:

- An article is suggested to the user, and the user clicks “Yes, close my request” in:
  - A feedback prompt on the article page opened
    via the email notification or web form.
  - A feedback prompt embedded in the email
    notification or web form.
- An article is suggested to the user, and within 72 hours, the user clicks on the suggested
  article link *and*
  - The ticket status is marked solved before any
    user or public agent reply *or*
  - No user or public agent reply has been added
    to the ticket.

When either of the conditions above is satisfied, and the
conversation has been evaluated as resolved by the LLM
verification process, then the [ai\_agent\_automated\_resolution](https://support.zendesk.com/hc/en-us/articles/4408894189082#h0sj62mlybt1v22j6318w7tje224ap8) tag is added
to the ticket 72 hours after the last user interaction as
long as the ticket is not yet closed.

### Automated resolutions in autoreplies based on intelligent triage

If you’re using [autoreplies based on intelligent
triage](https://support.zendesk.com/hc/en-us/articles/6191477770906) in email notifications, an automated
resolution is counted when *all* of the following
criteria are met:

- A trigger with a sentiment, language, or intent
  condition fired on the ticket. (This can be, but
  doesn't have to be, the same as the trigger
  below.)
- A trigger with an autoreply action fired on the
  ticket. (This can be, but doesn't have to be, the
  same as the trigger above.)
- No user or public agent reply has been added to
  the ticket in 72 hours.

When the conditions above are satisfied, and the conversation has
been evaluated as resolved by the LLM verification process,
then the [ai\_agent\_automated\_resolution](https://support.zendesk.com/hc/en-us/articles/4408894189082#h0sj62mlybt1v22j6318w7tje224ap8) tag is added
to the ticket 72 hours after the last user interaction as
long as the ticket is not yet closed.

### Automated resolutions in Web Widget (Classic)

If you’re using [Web Widget (Classic) to deliver article
recommendations](https://support.zendesk.com/hc/en-us/articles/4408843471642) to your end users, an automated resolution is counted
when the AI agent has suggested at least one article via Article Recommendations
and the end user has clicked on at least one article preview link or provided
positive feedback “Yes, problem solved”.

When this happens, a ticket is created for tracking purposes with
a requester called *End user*, no assignee, and the
[ai\_agent\_automated\_resolution](https://support.zendesk.com/hc/en-us/articles/4408894189082#h0sj62mlybt1v22j6318w7tje224ap8) tag. The
*End user* profile cannot be edited or
deleted.

The conversation is considered unresolved if:

- The user initiated a live chat
- The user submitted a contact form
- The user requested a callback
- The user provided negative feedback (“No, I still need
  help”)
- The AI agent (referred to as a “bot” in the flowchart
  below) didn’t understand the request

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/AR_for_web_widget_classic.png)

In the Web Widget (Classic), a session ends after 72
hours of inactivity or when the end user closes the browser
or tab.

### Actions that don’t contribute to automated resolution calculations

In some cases, the AI agent response used in calculating automated resolution is an article
recommendation. However, the following actions are not
considered when calculating automated resolutions, even
though an article may be suggested:

- [Answer Bot for Slack](https://support.zendesk.com/hc/en-us/articles/4408827411098)
  (Article recommendation)
- [Article Recommendation
  API](https://support.zendesk.com/hc/en-us/articles/4408831077018)
- [Article Recommendation for Mobile
  SDK Classic](https://support.zendesk.com/hc/en-us/articles/4408843471642)
- [Article Recommendation for
  Agents](https://support.zendesk.com/hc/en-us/articles/5581313653530)
- [Zendesk AI agents
  for Microsoft Teams](https://support.zendesk.com/hc/en-us/articles/4408821281818#topic_e55_sxr_pzb)

Actions that link to another flow do not increase the automated
resolution count.

Automated resolutions in [sandbox
environments](https://support.zendesk.com/hc/en-us/articles/6150628316058) do not count against your
default allocation of automated resolutions for your
account.

## Understanding the default allocation of automated resolutions per plan

All Zendesk Suite and Support plans include a baseline number of automated resolutions based on
your plan type. You can increase the number of automated resolutions
to avoid exceeding your allotted amount, or [pause the AI agent
functionality](https://support.zendesk.com/hc/en-us/articles/7460877856026) when you reach your limit in order to
prevent overage.

If you want to ensure your account isn't consuming any automated
resolutions, you can [turn off all capabilities related to AI agents](https://support.zendesk.com/hc/en-us/articles/7460877856026).

This section includes the following topics:

- [Default automated resolution allocation per plan](#topic_hn3_q3x_4wb)
- [Adding automated resolutions to your account](#topic_g2n_q3x_4wb)
- [Avoiding automated resolution overages](#topic_awx_qp1_ccc)

### Default automated resolution allocation per plan

Most Zendesk usage plans include a number of automated resolutions. If you’re not part of a Suite
or Support plan or find that your plan doesn’t provide
enough automated resolutions, you will be able to purchase
more as needed.

The following table shows how many automated resolutions are
included in each plan. Light agents are not included in the
default allocation calculation. Accounts on all plans have a
maximum of 10,000 allocated automated resolutions per year,
applied [after the new pricing
plan takes effect](https://support.zendesk.com/hc/en-us/articles/5352026794010#topic_fy3_fzc_1cc). If you need more automated
resolutions, you can [add them to your account](#topic_g2n_q3x_4wb).

| **Plan** | **Zendesk Suite** | **Support (standalone)** |
| --- | --- | --- |
| Enterprise | 15 automated resolutions/agent/month | 15 automated resolutions/agent/month |
| Professional  Growth | 10 automated resolutions/agent/month | 10 automated resolutions/agent/month |
| Team | 5 automated resolutions/agent/month | 5 automated resolutions/agent/month |

Note: Legacy Support plans include access to AI agents but do not come with included automated
resolutions. Those customers can purchase automated
resolutions as needed.

Your allocation of automated resolutions expires annually or at the end of your subscription term
(if less than a year) unless you are on a non-standard
subscription term.

### Adding automated resolutions to your account

You can increase the number of automated resolutions to avoid exceeding
your allotted amount. Using more than your allotted resolutions can result in
overage charges.

You can add to your automated resolution allotment by purchasing 100 or
more automated resolutions ahead of time. Also called committed usage, this
approach allows you to raise the maximum number of automated resolutions
available to you in advance. Committed usage provides a better per-resolution
cost than overage billing (or pay-as-you-go).

If you choose an overage billing (or pay-as-you-go) approach to
automated resolutions management, the cost per automated resolution over your
allotment will be greater than the cost per automated resolution when you buy a
fixed number to increase your allotment. You can prevent overage billing by
limiting the number of automated resolutions available in your account each
month. Overage is billed monthly, regardless of your subscription terms.

### Avoiding automated resolution overages

You can choose how your account responds when you reach your
automated resolution limit.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bot_overage_limit.png)

For more information, see [Maintaining or
pausing functionality when you reach your automated
resolution limit](https://support.zendesk.com/hc/en-us/articles/6958358659226#topic_iw3_b2h_bdc).

## Finding more information

If you have feedback or questions related to AI agents, visit our [community forum](https://support.zendesk.com/hc/en-us/community/posts/7155717341594) where
we collect and manage customer product feedback. For general
assistance with your Zendesk products, contact [Zendesk Customer
Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).