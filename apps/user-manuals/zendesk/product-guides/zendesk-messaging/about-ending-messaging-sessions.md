# About ending messaging sessions

Source: https://support.zendesk.com/hc/en-us/articles/8009788438042-About-ending-messaging-sessions

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Verified AI summary ◀▼

Ending messaging sessions lets you manage conversations by stopping interactions when needed. Agents can end sessions to wrap up tasks or switch channels, while end users can close sessions to start new issues. This feature impacts ticket routing, triggers, and agent capacity, and can be configured for agents, end users, or both, enhancing workflow flexibility.

In a messaging conversation, a *session* is the real-time exchange between the end
user and a human or AI agent. A messaging session can be ended – manually by agents or
end users, or automatically using triggers – providing the flexibility to disconnect the
conversation in the messaging channel when needed.

For instance, ending a messaging session can be useful for an agent when:

- They have all the information they need from the customer but must perform some
  wrap-up tasks before closing the ticket. Ending the session prevents the
  customer from continuing the discussion or bringing up different issues within
  the same conversation.
- The conversation can be handled better in another channel, such as email or voice.

Ending a messaging session can be useful for an end user when they have resolved the issue
being discussed on their own, and wants to raise a new one immediately without waiting
for the agent to end the session.

When you’re ready, you can turn the feature on for [agents](https://support.zendesk.com/hc/en-us/articles/8372292195354), for [end users](https://support.zendesk.com/hc/en-us/articles/10046732687770), or for both..

This article includes the following sections:

- [About the terminology used in this article](#topic_wh1_jnv_kdc)
- [Understanding workflow changes when you allow agents or end users to end messaging sessions](#topic_z1v_gf2_tcc)
- [Understanding the agent experience when messaging sessions are ended](#topic_ozy_hf2_tcc)
- [Understanding the end-user experience when messaging sessions are ended](#topic_fcd_nnv_kdc)

## About the terminology used in this article

Some terms used in this article are also used as general references when discussing
Zendesk messaging features. In this article:

- **Conversation**: The entire lifecycle of a customer request. A
  conversation begins when the end user clicks the Web Widget launch button
  and enters a comment or otherwise initiates communication and ends when the
  related ticket is *Closed*.
- **Session**: The real-time, live chat-style interaction between an end
  user and an agent. Agents can end sessions, which prevents the end user from
  interacting with the agent through any messaging channel. Each messaging
  conversation has only one session.
- **Ticket**: Messaging tickets are created when messaging conversations
  are handed off from an AI agent and routed to a human agent, group, or queue
  in Support. Each messaging ticket is associated with a messaging session.
  Tickets include all manual and automatic events applied to the ticket, such
  as status changes, triggers and other business rules, and both public and
  internal replies.

## Understanding workflow changes when you allow agents or end users to end messaging sessions

When an agent or end user ends a messaging session, the messaging channel is
essentially turned off for that conversation, which affects the following aspects of
the conversation lifecycle:

- [Ticket routing](#topic_gl2_rjl_hdc)
- [Triggers](#topic_rn4_hf2_tcc)
- [Agent capacity](#topic_py5_hf2_tcc)
- [Ticket status](#topic_c1g_j4v_kdc)
- [CSAT surveys](#topic_dxl_j4v_kdc)

### Ticket routing

When an agent ends a messaging session, the associated ticket can be
treated as an email ticket rather than a messaging ticket for the purposes of
omnichannel routing and agent capacity.

Depending on your [routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_hr4_1lh_n2c), you can route
all tickets associated with an agent-ended messaging session as messaging
tickets or email tickets. Alternatively, if you want to route some agent-ended
messaging session tickets as email tickets but not all of them, you can [create ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) using either
the *Ticket > End session* or the *Ticket > Set routing channel*
actions. Both of these actions automatically end the ticket's messaging session,
but the *Set routing channel* action also changes the ticket's routing
channel to *email*. Don't use these actions together.

To remain eligible for routing by omnichannel routing when the messaging session
ends, the ticket's routing channel must be changed to *email* and the
ticket must have your auto-routing tag. To route these tickets, you can create a
custom queue using the *Ticket > Channel | Is | Messaging* and *Ticket
> Routing channel | Is | Email*
conditions.

Note: If a ticket's routing channel is *messaging* after the messaging session
is ended, it is ineligible for routing and removed from any queue it might be
in. You must use the routing configuration setting or ticket trigger action to
change the routing channel to *email* for the ticket to remain eligible for
routing by omnichannel routing.

### Triggers

Because the messaging channel is unavailable on a ticket with an ended session,
[messaging triggers](https://support.zendesk.com/hc/en-us/articles/5973077601562) can’t run on them.
However, [ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) will still act on them
when conditions are met, including triggers with the *Ticket > Channel | Is
| Messaging* condition.

When you allow agents to end messaging sessions, a new ticket trigger condition
is added: *Ticket > Messaging session ended reason*. When used in
combination with the *Ticket > Channel | Is | Messaging* condition, you
can build ticket triggers that fire on messaging tickets with ended messaging
sessions. These conditions are helpful if you need to replace the bypassed
messaging triggers or want to [send a CSAT survey](https://support.zendesk.com/hc/en-us/articles/8082415949210) when an agent ends
a session.

Two new ticket trigger actions are added as well: *Ticket > Messaging
session | End Session*, which automatically ends the ticket's messaging
session and *Ticket > Set routing channel*, which changes the routing
channel to *email* and ends the messaging session if it's ongoing. These
can can be helpful when managing surges in tickets, ticket received outside of
business hours, and reporting on messaging tickets after their sessions are
ended.

The following recipes can help you create ticket triggers with these conditions
and actions:

- [Recipe: Managing a surge in
  messaging traffic (messaging routing configuration)](https://support.zendesk.com/hc/en-us/articles/9339278067482)
- [Recipe: Managing a surge in
  messaging traffic (omnichannel routing
  configuration)](https://support.zendesk.com/hc/en-us/articles/9339297143834)
- [Recipe: Managing tickets created
  outside of business hours using End session as a ticket trigger
  action](https://support.zendesk.com/hc/en-us/articles/9340032656026)
- [Recipe: Reporting on messaging
  tickets with ended sessions](https://support.zendesk.com/hc/en-us/articles/9340024053402)

### Agent capacity

The agent’s [messaging ticket capacity](https://support.zendesk.com/hc/en-us/articles/4776409839770) is released
after they end a messaging conversation session. The agent’s email ticket
capacity is not affected.

### Ticket status

A ticket’s status does not automatically change when an agent ends the associated
messaging session.

### CSAT surveys

Because the messaging channel is turned off when an agent ends a messaging
session, the action of solving the ticket doesn’t occur in the messaging channel
and, therefore, the conditions in the default messaging CSAT trigger can’t be
met.

Using [customizable CSAT](https://support.zendesk.com/hc/en-us/articles/7689997846554) (available on Suite Growth plans
and above), you can create a trigger that automatically sends the survey to end
users when an agent ends their messaging session. See [Recipe: Sending a CSAT survey when a
messaging session ends](https://support.zendesk.com/hc/en-us/articles/8082415949210-).

## Understanding the agent experience when messaging sessions are ended

When you allow agents to end messaging sessions, they can do so in the
composer in Agent Workspace.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/end_session-AW.png)

When an agent ends a messaging session in a conversation, the related ticket is
updated in the Agent Workspace in several ways:

- In the composer, the messaging channel option is deactivated for that
  conversation. Agents can contact the customer through other available
  channels.
- If the end user’s email address is known, the composer defaults to public
  reply; if no email is provided, the composer defaults to an internal
  note.
- The end session event is captured and displayed in the ticket event
  history.
- Agents can continue communicating with one another on the ticket using
  internal notes.
- The status of the associated ticket isn’t influenced by the messaging
  session’s state.

## Understanding the end-user experience when messaging sessions are ended

The end user’s experience when a messaging session ends is slightly different
depending on whether that session was ended by an agent or by the end user.

**When an agent ends a messaging session**, the end user can’t reply to the
related ticket through that messaging conversation. If an end user enters new
replies in the Web Widget after the session is ended, it’s treated as a new agent
interaction that initiates a new messaging session and, ultimately, a new
ticket.

Customers aren’t automatically notified when an agent ends a messaging session. To
prevent customer confusion, you may want to instruct your agents to inform the
customer that they're ending the conversation and any new replies will result in a
new messaging conversation and ticket. To streamline this communication, admins can
[create a macro](https://support.zendesk.com/hc/en-us/articles/4408844187034) with a standardized
statement for them to use.

**When an end user ends a messaging session**, as with agent-ended
sessions, the end-user can no longer reply to the related ticket through the Web
Widget. Additionally:

- A message appears in the conversation confirming that the
  conversation has ended.
- A New conversation button appears at the bottom of the messaging
  session in the Web Widget, [unless the button has been
  removed](allowing-multiple-conversations-for-your-end-users.md#topic_nwd_wjy_1dc).
- A CSAT survey is sent to the end user, if configured to do so.
- If the end conversation request fails, a banner message appears
  informing end users the conversation didn’t end.