# Understanding AI agent tickets for AI agent–only conversations

Source: https://support.zendesk.com/hc/en-us/articles/9204149016346-Understanding-AI-agent-tickets-for-AI-agent-only-conversations

---

AI agent tickets are tickets for messaging conversations that were handled entirely by yourAI agentorbasic messaging response, meaning they haven’t yet been or never were escalated to a human agent. Agents and admins can view AI agent tickets in the Agent Workspace.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

AI agent tickets are tickets for messaging conversations that were handled entirely by
your [AI agent](https://support.zendesk.com/hc/en-us/articles/6970583409690) or [basic messaging response](../zendesk-messaging/configuring-messaging-responses-and-business-hours.md), meaning they haven’t
yet been or never were escalated to a human agent. Agents and admins can view AI agent
tickets in the Agent Workspace.

AI agent tickets help you:

- **Identify customer requests that are ongoing or have been solved without human
  intervention.** Search for or create views for AI agent tickets to quickly
  discover which types of issues are being solved without human agent involvement.
- **Provide context for customer interactions.** AI agent tickets appear in the
  interaction history for customers who have had previous interactions with the AI
  agent. This gives agents who are handling a ticket more context on the engagements
  that this customer has had with your business.
- **Audit conversations to analyze AI agent responses.** Read the full
  conversations between your AI agent and customers to see how your AI agent is
  responding and identify areas for improvement.
- **Gain better visibility into your automated resolutions.** Examine your solved
  and closed AI agent tickets to confirm that interactions counted as [automated resolutions](https://support.zendesk.com/hc/en-us/articles/5352026794010#topic_m1n_sq4_jwb) are being resolved
  appropriately.

*Viewing AI agent conversations as tickets in the Agent Workspace (4:17)*

This article contains the following topics:

- [About AI agent tickets](#topic_rxc_2r1_2gc)
- [Turning the AI agent tickets feature on or off](#topic_myq_2r1_2gc)
- [Identifying an AI agent ticket](#topic_yqf_fr1_2gc)
- [Understanding functionality limitations for AI agent tickets](#topic_cts_fr1_2gc)

Related article:

- [Finding AI agent tickets in your
  account](https://support.zendesk.com/hc/en-us/articles/9966620612634)

## About AI agent tickets

AI agent tickets can be created for any [level of Zendesk AI agent functionality](https://support.zendesk.com/hc/en-us/articles/6970583409690#topic_zps_zmk_f2c),
including Essential, Advanced, and legacy, as well as third-party bots. Note that AI
agent tickets are also created for conversations customers have with your [basic messaging responses](../zendesk-messaging/configuring-messaging-responses-and-business-hours.md).

When a customer begins a messaging conversation with an AI agent (or just in the Web
Widget), an AI agent ticket is created. AI agent tickets are always read-only.

The first customer message in the conversation triggers the creation of the AI agent
ticket. This means any initial message sent by the AI agent or basic message
response (for example, a welcome message) is not included. However, if the
conversation is escalated to a human agent, then the conversation history is
backfilled and any initial messages are inserted in the ticket upon escalation.

As long as a conversation is not escalated to a human agent, it is considered an AI
agent ticket. When an AI agent ticket is escalated to a human agent, the ticket is
no longer considered an AI agent ticket and becomes a regular, editable ticket.

While an AI agent conversation is ongoing, the AI agent ticket is in the Open status.
The conversation is no longer considered ongoing when:

- 4 days have passed since the last response, or
- The AI agent releases control, which marks the conversation as Solved, or
- (For third-party bots only) The third-party bot logic deems the conversation
  resolved.

At that point, an AI agent ticket moves into the Solved status, and then into the
Closed status [based on your business rules](https://support.zendesk.com/hc/en-us/articles/8263915942938#topic_zxw_4yk_fdc).

AI agent tickets can be deleted only when they’re in the Solved or Closed status.
This prevents agents or admins from accidentally deleting the ticket for an ongoing
AI agent conversation.

Note: Deleting an AI agent ticket doesn’t delete the
underlying Sunshine Conversations data associated with that conversation. In a
future release, Zendesk plans to introduce the ability to remove these
conversations from Sunshine Conversations too.

AI agent tickets don’t disrupt existing workflows based on business rules, including
automations, triggers, and more. These types of workflows continue to function only
on regular tickets and cannot act on AI agent tickets. This means that these
workflows take effect as expected when an AI agent ticket is escalated to a human
agent. If an AI agent ticket is escalated, its status is set back from Open to New,
allowing it to be processed as any other newly submitted ticket would be.

Note: For AI agent tickets, [tags based on users and organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658#topic_olv_kmn_dsb)
are populated at ticket creation, but any triggers or automations based on these
tags don’t fire until a ticket is escalated to a human agent.

AI agent tickets count toward your account’s [data storage limits](https://support.zendesk.com/hc/en-us/articles/4408835043994#topic_izq_c22_hlb). If necessary, you can
[create a ticket deletion schedule](https://support.zendesk.com/hc/en-us/articles/9752192560410) to
target AI agent tickets specifically.

Note: Messages sent by a [suspended user](https://support.zendesk.com/hc/en-us/articles/4408889293978) don’t create an AI
agent ticket. If you need to delete these messages for General Data Protection
Regulation (GDPR) or other compliance reasons, [create a deletion schedule for bot-only
conversations](https://support.zendesk.com/hc/en-us/articles/8499219792154).

## Turning the AI agent tickets feature on or off

You can turn the AI agent tickets feature on or off to control whether tickets are
created for conversations between your AI agents and your customers.

Note: On February 18, 2026, this feature will be turned on by
default but can still be turned off. On May 4, 2026, this feature will be turned
on by default and cannot be turned off.

If you turn AI agent tickets off, AI
agent–only conversations won’t appear in Zendesk QA until May 4, 2026,
unless you turn the feature back on before that date. Only conversations
created while the feature is turned on will appear in Zendesk QA.

**To turn the AI agent tickets feature on or off**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click **Manage settings**.
3. Click the **AI agent conversations as tickets in Agent Workspace**
   section to expand it.
4. Select or deselect **Turn on AI agent conversations as
   tickets**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_ai_agent_tickets_setting_banner.png)
5. Click **Save settings**.

## Identifying an AI agent ticket

To help you distinguish between AI agent tickets and regular tickets, AI agent
tickets have a number of visual identifiers:

1. A bot icon appears in the ticket tab.
2. An “AI agent” badge appears in the ticket header (and the filter is
   missing).
3. All the fields in the ticket properties panel are grayed out.
4. The composer and macros menu are hidden.
5. A message in the ticket footer notes that this is an AI agent
   ticket.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_ai_agent_ticket_identifying.png)

Additionally, AI agent tickets include helpful indicators when an automated
resolution is consumed:

- The Resolution type field lists Automated as the value.
- In the [events view](https://support.zendesk.com/hc/en-us/articles/4408829602970), a system entry notes the
  date and time the automated resolution occurred.
- The Resolution type field can be used when [creating custom reports](https://support.zendesk.com/hc/en-us/articles/4408821589530).

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aia_resolution_type_ticket_field.png)

Note: Deleting an AI agent ticket with a Resolution type value
of Automated doesn’t undo the consumption of an automated resolution.

To help agents and admins identify AI agent tickets in views and search results in
Support, the Assignee column includes a bot icon for AI agent tickets.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_ai_agent_tickets_view_column.png)

In Support, the profile associated with the AI agent assignee has the [Contributor role](https://support.zendesk.com/hc/en-us/articles/4408832171034#topic_pzw_3bs_qmb).

For more information, see [Finding AI agent tickets in your account](https://support.zendesk.com/hc/en-us/articles/9966620612634).

## Understanding functionality limitations for AI agent tickets

AI agent tickets have different limitations and considerations than regular tickets.
The following sections provide more details:

- [Functionality limitations](#topic_lgf_ht1_2gc)
- [Sunshine Conversations considerations](#topic_xqh_3t1_2gc)

### Functionality limitations

The following functionality does not currently work on AI agent tickets until
they are escalated to a human agent (at which point they become regular,
editable tickets):

- Deleting tickets for ongoing AI agent conversations
- Modifying ticket properties
- Adding public comments or internal notes
- Applying macros
- Triggers and automations
- SLAs
- Omnichannel routing
- Skills calculation
- Ticket assignment/reassignment
- Bulk editing
- Ticket sharing
- Custom ticket statuses
- Problem/incident ticket linking
- Exporting ticket data
- Ticket merging
- Auto assist (including actions)
- AI-based redaction suggestions
- Workflows that rely on the “created\_at” event
- Domain-level events in integrations
- Zendesk Apps framework (ZAF) apps

Additionally, AI agent tickets don’t appear in the following places:

- Agent Home
- Explore reports
- The outputs of APIs that list tickets (such as the endpoints [listed here](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#list-tickets))

### Sunshine Conversations considerations

The following Sunshine Conversations considerations apply to AI agent tickets:

- Pre-existing conversations are not backfilled as AI agent tickets.
- Each new [zd:agentWorkspace](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#basic-switchboard-configuration:~:text=Product-,zd%3AagentWorkspace,-Zendesk%20Support%20/%20Agent) conversation
  generates a regular ticket.
- Each new non-zd:agentWorkspace conversation generates an AI agent ticket.
- User data is synced either when an AI agent ticket is marked as Solved or
  when the ticket is escalated to an agent.
- The [releaseControl](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#release-control) action marks the
  associated AI agent ticket as Solved.