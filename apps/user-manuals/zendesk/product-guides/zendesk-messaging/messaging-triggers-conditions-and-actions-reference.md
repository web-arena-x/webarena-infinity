# Messaging triggers conditions and actions reference

Source: https://support.zendesk.com/hc/en-us/articles/8015292388378-Messaging-triggers-conditions-and-actions-reference

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Zendesk messaging triggers allow you to send messages to customers and optimize your
workflows.

This article contains the following tables:

- [Channels](#topic_cpt_1gd_23c)
- [Trigger firing events](#topic_pgr_rsj_d4b)
- [Trigger operators](#topic_abf_q5f_rhb)
- [Trigger conditions](#topic_d3p_q5f_rhb)
- [Trigger actions](#topic_hxz_q5f_rhb)
- [Trigger placeholders](#topic_n5j_r5f_rhb)

Related articles:

- [About messaging triggers in Admin
  Center](https://support.zendesk.com/hc/en-us/articles/5973077601562)
- [Working with messaging triggers in Admin
  Center](https://support.zendesk.com/hc/en-us/articles/6058753945242#topic_w1p_vpn_q5b)

## Channels

Messaging triggers can be used on Zendesk messaging channels, including:

- Web Widget
- Mobile SDKs (iOS, Android, Unity)
- Zendesk-supported [social channels](https://support.zendesk.com/hc/en-us/articles/4408831648794)

*Web Widget & SDKs* is selected by default. You can delete this selection,
or add any social messaging channels when creating a messaging trigger.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/messaging_triggers_social_channels.png)

## Trigger firing events

Every trigger starts with a firing event. These events dictate whether the trigger
will run, then evaluate its conditions and fire its specified actions. Use the
**Run trigger** dropdown to choose a trigger’s firing events.

Note: Messaging tickets are created when an AI agent hands off control of a
messaging conversation, and the conversation is assigned to a group or live
agent.

- **When a customer requests a conversation**: The trigger runs when a
  conversation is handed off by the AI agent and a ticket is created, or the
  end user re-engages in the conversation after [agent capacity is released](https://support.zendesk.com/hc/en-us/articles/7043034053658).
- **When a message is sent**: The trigger runs when a customer
  enters the conversation and sends a message in the messaging Web Widget.
- **When a conversation is added to the queue**: The trigger runs when a
  messaging conversation is placed in the queue.
- **When a conversation is assigned from a queue**: The trigger runs when a
  messaging ticket is assigned to an agent from the queue, using the [Accept button](https://support.zendesk.com/hc/en-us/articles/5020833543450#topic_nzf_pdb_pmb) or [auto-accept](https://support.zendesk.com/hc/en-us/articles/6442469463194). It doesn't run when
  an agent reassigns the ticket to another agent, or when the agent claims the
  ticket from a group view.

## Trigger operators

Use the following operators to build trigger condition statements.

Table 1. Trigger operators

| Operator | Description |
| --- | --- |
| is | Exact match. ``` = 5 returns true only when 5 ``` |
| Less than | Less than the number entered, but not including. ``` < 10 returns true from 0-9 ``` |
| Greater than | More than the number entered but not including. ``` > 120 returns true from 121 to 1,000,000,000,000,000,000 ``` |
| Less than or equal to | An exact match or less than the number entered. ``` <= 3 returns true on a 3, 2, 1, or 0 ``` |
| Greater than or equal to | An exact match or more than the number entered. ``` >= 600 returns true from 600 to 1,000,000,000,000,000 ``` |
| Is not | Anything but the value entered. ``` != 0 returns true for any number but 0 ``` |
| Contains | String includes the following text. ``` "help" matches true with "help, i need somebody" ``` |
| Contains (case sensitive) | String includes the following text. ``` "Hello" matches with "Hello, it's me" ``` |
| Does not contain | String does not include the following text. ``` "help" matches true with "not just anybody" ``` |
| Reg Ex | Matches for regular expression values using the [Python RegEx framework](https://docs.python.org/2/library/re.html). This field looks for a *full* match, not a partial. For assistance, you can use [Pythex](https://pythex.org/) as a quick reference and validation tool. ``` (?P<year>(?:19|20)\d\d)(?P<delimiter>[- /.])(?P<month>0[1-9]|1[012])\2(?P<day>0[1-9]|[12][0-9]|3[01])                                             Test String:  2014-07-28                                             String match:  2014-07-28 ``` |
| Reg Ex (case sensitive) | Field looks for a full case-sensitive match, not a partial match. |
| Is one of the following | Multi-select field; looks for a match that includes any of the selections. |
| Is not one of the following | Multi-select field; looks for a match that excludes all the selections. |

## Trigger conditions

Condition statements are collections of conditions, field operators, and
condition values. Available values can vary based on the condition selected.
Condition statements are essentially ‘if’ statements that return all tickets that
meet the specified criteria.

You must select one – and only one – of the condition statements to save
and use a trigger in both the Visual and Developer views:

- **Check All of the Following Conditions** requires all
  conditions to be met to execute a trigger’s actions.
- **Check Any of the Following Conditions** requires only one
  condition to be met to execute a trigger’s actions.

Note: Zendesk has implemented limits on certain trigger conditions. Any existing
triggers that exceed these limits will be disabled. If you attempt to re-enable
them, an error message will appear. The table below includes these condition
limits.

Table 2. Trigger conditions

| Condition | Description |
| --- | --- |
| **Date and time** | |
| Hour of day | Hour of the day (Universal Time Clock): **0** = midnight  **23** = 11 p.m.  Note that the Hour of day condition uses the hour only, and does not include minutes. |
| Day of week | Day of the week: **0** = Monday  **6** = Sunday |
| **Previous conversation** | |
| Customer previous conversations | Number of times the customer has previously had a conversation with an agent. (New conversation = 0). Limited to 32,000 previous conversations. |
| **Customer Information** | |
| Customer name | Name of customer |
| Customer triggered | Triggered customer (activated by *Set triggered* action).  Values are **True** or **False** |
| Customer email | Email of customer |
| Customer page URL | The location of the Web Widget during the most recent customer event. An event can be when the customer requests a conversation, or when the customer sends a message in the conversation. *Not supported in social channels.* |
| **Customer Location** | |
| Customer country | The country associated with the customer's IP address. *Not supported in social channels.* |
| Customer IP | IP address of the customer. *Not supported in social channels.* |
| **Customer device information** | |
| Customer browser | Browser used by the customer. Version number does not include patch updates. *Not supported in social channels.* |
| Customer OS | Operating system used by the customer. Does not include OS version. *Not supported in social channels.* |
| Customer platform | Platform used by the visitor. *Not supported in social channels.* |
| **Online Status** | |
| Account status | Status of your Zendesk account. Values are:  - **Online**: If at least one agent is online and the   rest are away or invisible, then the account status is   Online and the trigger fires. - **Away**: If at least one agent is away and the rest   are invisible, the account status is Away and the   trigger fires. - **Invisible**: If all agents are invisible, the   account status is Invisible and the trigger fires. |
| Group status | Status of the selected Zendesk group. Values are:   - **Online**: If at least one agent in the group is   online, and the rest are away or invisible, then the   group status is Online, and the trigger fires. - **Away**: If at least one agents in a group is away,   and the rest are invisible, the group status is Away and   the trigger fires. - **Invisible**: If all agents in a group are   invisible, the group status is Invisible, and the   trigger fires. |
| **Conversation-related information** | |
| Brand | Multi-select field lets you add your active and inactive brands. |
| Customer is in active conversation | Values are: - **True** if the customer is currently engaged in   a conversation. - **False** if the customer is not currently   engaged in a conversation. |
| Customer is requesting conversation | Values are:  - **True** if the customer is requesting to start a   conversation. - **False** if no agent has responded to the   customer. |
| Customer served | Values are:  - **True** if the customer is actively being   assisted by an agent (for example, the agent has   accepted the conversation and sent an initial   message). - **False** if no agent has responded to the   customer.  *Not supported in social channels.* |
| Group | Name of the group assigned to the conversation. |
| Sender | Name of the message sender. |
| Sender Type | Values are **Agent** or **Customer**. |
| Message | The message being sent. |
| Initial routing | The conversation is added to a queue for the first time, and applies only to tickets with the New ticket status. Does not apply to tickets that are transferred from one group or agent queue to another.  This condition can be used to differentiate between the messaging tickets added to the queue for the first time and tickets transferred to the queue.  Values are:  - **True** if the messaging ticket is added to the   queue for the first time. - **False** if the ticket is transferred from   another queue, or if the ticket is sent to an [overflow   queue](https://support.zendesk.com/hc/en-us/articles/6712096584090). |
| Tags | Enter ticket tags in the text field. Matching tags are automatically suggested. |
| **Customer queue** | |
| Queue Size | The total number of incoming conversation requests for the account. This condition targets the *overall account queue*, not the department-specific queue. Note: If you’re using the [multi-conversations](https://support.zendesk.com/hc/en-us/articles/8008427696410) feature, multiple conversations from a single user are counted as a single request. |

## Trigger actions

Action statements define what occurs if all the condition statements are true and the
trigger fires. You can think of action statements as ‘then’ statements: if all of
your conditions are true, *then* perform these actions to execute these actions
to update the conversation.

Table 3. Trigger actions

| Action | Description |
| --- | --- |
| Send message to customer | Sends a predefined message to the user. When a message is sent to an end user by a messaging or system trigger:  - If an AI agent is configured and in use, the [AI agent   avatar](https://support.zendesk.com/hc/en-us/articles/6447066520986) appears with the message. - If no AI agent is in use, the [logo defined for   the Web Widget](https://support.zendesk.com/hc/en-us/articles/4500747797914#topic_ubc_nmd_btb) appears with the   message. |
| Wait | Introduces a delay before the next action is fired Note: Triggers run simultaneously. If multiple triggers need to be fired in a specific sequence, add at least a one-second delay to each subsequent trigger. |
| Request email | Sends an automated message to the customer requesting their email to facilitate [continuous conversation](https://support.zendesk.com/hc/en-us/articles/4408829095706) re-engagement. |
| Set triggered | Applies a flag that can be used with the **Customer triggered** condition. Values are: **True** or **False** |
| Add tags | Adds tags to the ticket. |
| Remove tags | Removes tags from the ticket. |
| Suspend user | Suspends a user, preventing them from using your messaging service. See [Suspending messaging users](https://support.zendesk.com/hc/en-us/articles/8009733465370) for more information. Note: When using this action in a trigger, include it as the trigger's final action. |

## Trigger placeholders

Placeholders are references to customer and agent details you can use in trigger
action statements. When the trigger is fired, the placeholder pulls in the current
visitor and session information.

Table 4. Trigger placeholders

| Placeholder | Type | Description |
| --- | --- | --- |
| @hour\_of\_day | Integer | Current hour of the day (UTC timezone). 0 - 23 |
| @day\_of\_week | Integer | Current day of the week (0 = Monday, 6 = Sunday) |
| @customer\_prev\_conversations | Integer | Number of previous independent conversations initiated with agent (New conversation = 0) |
| @customer\_name | String | Name of the customer. |
| @customer\_triggered | String | True if the customer has previously received a messaging trigger. |
| @account\_status | String | Status of the account (**Online**, **Away**, or **Invisible**). |
| @bot\_name | String | [Name](https://support.zendesk.com/hc/en-us/articles/4408824263578#topic_dw4_xnd_f2c) of the AI agent published to the current messaging channel. |
| @customer\_is\_in\_active\_conversation | String | True if the customer is active in the conversation. |
| @customer\_requesting\_conversation | String | True if the customer is requesting a conversation. |
| @customer\_served | String | True if customer is currently being served by an agent. |
| @sender | String | The name of the sender. |
| @customer\_email | String | The email of the customer. |
| @sender\_type | String | The type of sender (**Agent** or **Customer**). |
| @customer\_page\_url | String | The URL of the page the customer is on. |
| @customer\_ip | Integer | The customer's IP address |
| @message | String | The message sent. |
| @tag | String | The tags applied to the ticket. |
| @queue\_size | Integer | The incoming conversation requests. |
| @wait\_time\_min | Integer | Minimum estimated wait time for the first response from an agent to the ticket (in minutes). The wait time is available only for groups with at least 1 ticket routed in the last 7 days. |
| @wait\_time\_max | Integer | Maximum estimated wait time for the first response from an agent to the ticket (in minutes). The wait time is available only for groups with at least 1 ticket routed in the last 7 days. |