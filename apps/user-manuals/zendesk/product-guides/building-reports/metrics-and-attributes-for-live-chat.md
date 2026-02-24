# Metrics and attributes for live chat

Source: https://support.zendesk.com/hc/en-us/articles/4409149177242-Metrics-and-attributes-for-live-chat

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Professional or Enterprise |

Use this article to discover the metrics and attributes you can use to build Explore
reports based on your usage of Zendesk Chat. These datasets are also used for the [Chat prebuilt dashboards](https://support.zendesk.com/hc/en-us/articles/4408843698842).

For more information about how to create reports with Explore, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530-Creating-queries).

Tip: On the [dataset selection page](working-with-datasets.md#topic_ig1_whf_5y), the live chat
datasets are grouped with the messaging dataset. For more information on the
messaging dataset, see [Metrics and attributes for Zendesk messaging](https://support.zendesk.com/hc/en-us/articles/4724624097818).

This article contains the following topics:

- [Engagement dataset](#topic_r34_grl_mfb)
- [Chat Concurrency
  dataset](#topic_ecm_gdp_mrb)

## Engagement dataset

The Engagement dataset contains metrics and attributes that relate to your Chat
engagement. This section lists all the available elements for the dataset, and
contains the following topics:

- [Engagement dataset schema](#topic_smk_45f_kkb)
- [Engagement metrics](#topic_j5r_5rl_mfb)
- [Engagement attributes](#topic_p1z_vrl_mfb)

### Engagement dataset schema

Use this diagram to help you understand the elements of the Engagement dataset
and their relationships.

![Chat dataset schema](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Chats.jpg)

### Engagement metrics

This section lists and defines all of the Engagement metrics available.

*Chat engagement* time-based metrics begin measuring specifically when an
*agent* interacts with a chat. Other Chat time-based metrics begin
measuring when an end user (or a representative, such as an agent or trigger,
beginning a chat on their behalf) interacts with the chat.

Note: Messaging tickets are not calculated as part of the Chat Engagements
dataset.

Table 1. Engagement metrics

| Metric | Definition | Calculation |
| --- | --- | --- |
| Chats | The number of Chat sessions. | IF ([Chat type - Unsorted]!="Offline Message") THEN [Chat ID] ENDIF |
| Served chats | The number of Chat sessions served by agents. A Chat session can have multiple agent engagements, but only one served chat. | IF ([Chat type - Unsorted]!="Offline Message" AND [Chat completion]!="Missed") THEN [Chat ID] ENDIF |
| Completed chats | The number of Chat sessions successfully completed by agents (excludes agent-dropped and missed chats). | IF ([Chat type - Unsorted]!="Offline Message" AND [Chat completion]="Completed") THEN [Chat ID] ENDIF |
| Non-completed chats | The number of chat sessions dropped or missed by agents. | IF ([Chat type - Unsorted]!="Offline Message" AND [Chat completion]!="Completed") THEN [Chat ID] ENDIF |
| Dropped chats | The number of chats accepted by or assigned to the agent where the end user responds to an agent message, then leaves the chat. | IF ([Chat type - Unsorted]!="Offline Message" AND [Chat completion]="Dropped") THEN [Chat ID] ENDIF |
| Deleted chats | The number of chat sessions which were deleted. | IF ([Chat type - Unsorted]!="Offline Message" AND [Chat deleted]="true") THEN [Chat ID] ENDIF |
| Skills fulfilled chats | The number of chats that were served by the agent with the required set of skills. | IF ([Chat type - Unsorted]!="Offline Message" AND [Chat skills fulfilled]="true") THEN [Chat ID] ENDIF |
| Transferred chats | The number of chats that were transferred to other departments or agents. | IF ([Chat type - Unsorted]!="Offline Message" AND [Engagement started by]="Transfer") THEN [Chat ID] ENDIF |
| Trigger fired chats | The number of chats on which the system trigger had fired. | IF ([Chat type - Unsorted]!="Offline Message" AND [Chat trigger fired]="true") THEN [Chat ID] ENDIF |
| Offline messages | The number of offline message left when no agents were online. | IF ([Chat type - Unsorted]="Offline Message") THEN [Chat ID] ENDIF |
| % Chat completion rate | The percentage of completed chats from the total amount of chats. | D\_COUNT(Completed chats)/D\_COUNT(Chats) |
| % Chat drop rate | The percentage of chats dropped by agents from the total amount of chats. | D\_COUNT(Dropped chats)/D\_COUNT(Chats) |
| % Chat skill fulfillment rate | The percentage of chats that were served by the agent with the required set of skills from the total amount of chats. | D\_COUNT(Skills fulfilled chats)/D\_COUNT(Chats) |
| % Chat transfer rate | The percentage of chats that were transferred to other departments or agents from the total amount of chats. | D\_COUNT(Transferred chats)/D\_COUNT(Chats) |
| % Chat trigger fired rate | The percentage of chats on which the system trigger had fired (was executed) from the total amount of chats. | D\_COUNT(Trigger fired chats)/D\_COUNT(Chats) |
| Chats - Daily average | The average number of chats started each day. | D\_COUNT(Chats)/DCOUNT\_VALUES([Chat started - Date]) |
| Inbound chats | The number of inbound chats initiated by end users. | IF ([Chat type - Unsorted]="Inbound") THEN [Chat ID] ENDIF |
| Completed inbound chats | The number of inbound chats successfully completed by agents (excludes the agent dropped and missed chats). The inbound chat sessions are initiated by end users (end users). | IF ([Chat type - Unsorted]="Inbound" AND [Chat completion]="Completed") THEN [Chat ID] ENDIF |
| Missed inbound chats | The number of inbound chat sessions where the end user ends the chat without an agent response. The inbound chat sessions are initiated by end users. | IF ([Chat type - Unsorted]="Inbound" AND [Chat completion]="Missed") THEN [Chat ID] ENDIF |
| Trigger fired inbound chats | The number of inbound chats on which the system trigger had fired. The inbound chat sessions are initiated by end users. | IF ([Chat type - Unsorted]="Inbound" AND [Chat trigger fired]="true") THEN [Chat ID] ENDIF |
| % Chat inbound rate | The percentage of chats initiated by end users from the total number of chats. | D\_COUNT(Inbound chats)/D\_COUNT(Chats) |
| % Chat miss rate | The percentage of chats missed from the total number of chats. | D\_COUNT(Missed inbound chats)/D\_COUNT(Chats) |
| Inbound chats - Daily average | The average number of inbound chats started each day. | D\_COUNT(Inbound chats)/DCOUNT\_VALUES([Chat started - Date]) |
| Outbound chats | The number of outbound chats initiated by agents. | IF ([Chat type - Unsorted]="Outbound") THEN [Chat ID] ENDIF |
| Completed outbound chats | The number of outbound chats successfully completed by agents (excludes the agent dropped chats). The outbound chats are initiated by agents. | IF ([Chat type - Unsorted]="Outbound" AND [Chat completion]="Completed") THEN [Chat ID] ENDIF |
| Non-engaged outbound chats | The number of outbound chats that were started by an agent but didn't engage the end user to start the chat conversation. | IF ([Chat type - Unsorted]="Outbound" AND [Chat completion]="Not Engaged") THEN [Chat ID] ENDIF |
| Trigger fired outbound chats | The number of outbound chats on which the system trigger fired (was executed). The outbound chats are initiated by agents. | IF ([Chat type - Unsorted]="Outbound" AND [Chat trigger fired]="true") THEN [Chat ID]ENDIF |
| % Chat outbound rate | The percentage of chats initiated by agents from the total number of chats. | D\_COUNT(Outbound chats)/D\_COUNT(Chats) |
| Outbound chats - Daily average | The average number of outbound chats started each day. | D\_COUNT(Outbound chats)/DCOUNT\_VALUES([Chat started - Date]) |
| Good satisfaction chats | The number of chat sessions rated by the end user as good. | IF ([Chat type - Unsorted]!="Offline Message" AND [Chat satisfaction rating]="Good") THEN [Chat ID] THEN [Chat ID] |
| Bad satisfaction chats | The number of chat sessions rated by the end user as bad. | IF ([Chat type - Unsorted]!="Offline Message" AND [Chat satisfaction rating]="Bad") THEN [Chat ID] ENDIF |
| Rated satisfaction chats | The total number of chat sessions rated by the end user as good or bad. | IF ([Chat type - Unsorted]!="Offline Message" AND [Chat satisfaction rating]!=NULL) THEN [Chat ID] ENDIF |
| % Chat satisfaction score | The percentage of chat sessions rated by the end user as good from the total number of rated chats. | D\_COUNT(Good satisfaction chats)/D\_COUNT(Rated satisfaction chats) |
| % Chat satisfaction rated | The percentage of chat sessions rated by the end user as good or bad from the total number of chats. | D\_COUNT(Rated satisfaction chats)/D\_COUNT(Chats) |
| Chat messages | The number of comments submitted during the chat session by the end user or agent. | (Chat messages) |
| Chat agent messages | Refers to the number of comments entered by an agent during the Chat session. | (Chat agent messages) |
| Chat visitor messages | The number of comments submitted during the chat session by the end user. | (Chat visitor messages) |
| Engagements | The number of chat engagements. During a chat session, end users can interact with multiple agents. Each interaction is counted as a different engagement. | [Engagement ID] |
| Assignments | The number of engagements which were assigned to agents. During a chat session, end users can interact with multiple agents. Each interaction is counted as different engagement. | IF ([Engagement assignment]!="Self-assigned") THEN [Engagement ID] ENDIF |
| Missed assignments | The number of engagements which were assigned to the agent but were missed (no agent reply). During a chat session, end users can interact with multiple agents. Each interaction is counted as a different engagement. | IF ([Engagement assignment]="Assignment Missed") THEN [Engagement ID] ENDIF |
| Accepted assignments | The number of engagements which were assigned to an agent and accepted. During a chat session, end users can interact with multiple agents. Each interaction is counted as a different engagement. | IF ([Engagement assignment]="Assignment Accepted") THEN [Engagement ID] ENDIF |
| Self-assignments | The number of engagements to which an agent assigned themselves. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. | IF ([Engagement assignment]="Self-assigned") THEN [Engagement ID] ENDIF |
| Skill fulfilments | The number of chat engagements that were served by the agent with the required set of skills. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. | IF ([Engagement skills fulfilled]="true") THEN [Engagement ID] ENDIF |
| Transfers | The number of chat engagements that were transferred to other departments or agents. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. | IF ([Chat started by]="Transfer") THEN [Engagement ID] ENDIF |
| % Assignment acceptance rate | The percentage of assignments which were assigned and accepted by an agent to the total number of agent assignments. | D\_COUNT(Accepted assignments)/D\_COUNT(Assignments) |
| Good satisfaction engagements | The number of chat engagements rated by the end user as good. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. | IF ([Engagement satisfaction rating]="Good") THEN [Engagement ID] ENDIF |
| Bad satisfaction engagements | The number of chat engagements rated by the end user as bad. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. | IF ([Engagement satisfaction rating]="Bad") THEN [Engagement ID] ENDIF |
| Rated satisfaction engagements | The total number of chat engagements rated by the end user as good or bad. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. | IF ([Engagement satisfaction rating]!=NULL) THEN [Engagement ID] ENDIF |
| % Engagement satisfaction score | The percentage of chat engagements rated by the end user as good from the total number of rated engagements. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. | D\_COUNT(Good satisfaction engagements)/D\_COUNT(Rated satisfaction engagements) |
| % Engagement satisfaction rated | The percentage of chat engagements rated by the end user as good or bad from the total number of engagements. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. | D\_COUNT(Rated satisfaction engagements)/D\_COUNT(Engagements) |
| Engagement messages | The number of comments submitted during the chat engagement by the end user or agent. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. | (Engagement messages) |
| Engagement agent messages | The number of comments submitted during the chat engagement by the agent. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. | (Engagement agent messages) |
| Engagement visitor messages | The number of comments submitted during the chat engagement by the end user. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. | (Engagement visitor messages) |
| Chat duration (sec) | The time duration from the first to the last chat message in seconds. The first message can come from an end user or from a proactive chat trigger. | (Chat duration (sec)) |
| Chat wait time (sec) | The time the end user waited for the first reply from an agent. If no agent replies, then this returns the total time the end user waited before leaving the chat session. | IF [Chat completion]="Missed" THEN VALUE(Chat no reply time (sec)) ELSE VALUE(Chat first reply time (sec)) ENDIF |
| Chat first reply time (sec) | The time in seconds between the end user joining the chat and the agent's first response. An end user joins a chat when they send the first chat message or reply to a proactive message. | (Chat first reply time (sec)) |
| Chat average reply time (sec) | The average time in seconds it took for agent to reply to end user comments during the chat session. | (Chat average reply time (sec)) |
| Chat longest reply time (sec) | The maximum time in seconds it took for agent to reply to end user comments during the chat session. | (Chat longest reply time (sec)) |
| Chat no reply time (sec) | The time in seconds from the end user's last unanswered comment to the end user leaving the chat session. | (Chat no reply time (sec)) |
| Chat missed no reply time (sec) | The time from the end user's last comment to the end user leaving the chat session without getting an agent reply. | IF [Chat completion]="Missed" THEN VALUE(Chat no reply time (sec)) ENDIF |
| Chat dropped no reply time (sec) | The time from the end user's last comment to the end user leaving the chat session without getting a reply. | IF [Chat completion]="Dropped" THEN VALUE(Chat no reply time (sec)) ENDIF |
| Chat duration (min) | The time duration from the first to the last chat message in minutes. The first message can come from an end user or from a proactive chat trigger. | VALUE(Chat duration (sec))/60 |
| Chat wait time (min) | The time the end user waited for the first reply from an agent. If no agent replies, then this returns the total time the end user waited before leaving the chat session. | IF [Chat completion]="Missed" THEN VALUE(Chat no reply time (sec))/60 ELSE VALUE(Chat first reply time (sec))/60 ENDIF |
| Chat first reply time (min) | The time in minutes between the end user joining the chat and the agent's first response. An end user joins a chat when they send the first chat message or reply to a proactive message. | VALUE(Chat first reply time (sec))/60 |
| Chat average reply time (min) | The average time in minutes it took for agent to reply to end user comments during the chat session. | VALUE(Chat average reply time (sec))/60 |
| Chat longest reply time (min) | The maximum time in minutes it took for agent to reply to end user comments during the chat session. | VALUE(Chat longest reply time (sec))/60 |
| Chat no reply time (min) | The time in seconds from the end user's last unanswered comment to the end user leaving the chat session. | VALUE(Chat no reply time (sec))/60 |
| Chat missed no reply time (min) | The time from the vistior's last comment to the end user leaving the chat session without getting an agent reply. | IF [Chat completion]="Missed" THEN VALUE(Chat no reply time (sec))/60 ENDIF |
| Chat dropped no reply time (min) | The time from the end user's last comment to the end user leaving the chat session without getting a reply. | IF [Chat completion]="Dropped" THEN VALUE(Chat no reply time (sec))/60 ENDIF |
| Chat duration (hrs) | The time duration from the first to the last chat message in minutes. The first message can come from an end user or from a proactive chat trigger. | VALUE(Chat duration (sec))/60/60 |
| Chat wait time (hrs) | The time the end user waited for the first reply from an agent. If no agent replies, then this returns the total time the end user waited before leaving the chat session. | IF [Chat completion]="Missed" THEN VALUE(Chat no reply time (sec))/60/60 ELSE VALUE(Chat first reply time (sec))/60/60 ENDIF |
| Chat first reply time (hrs) | The time in hours between the end user joining the chat and the agent's first response. An end user joins a chat when they send the first chat message or reply to a proactive message. | VALUE(Chat first reply time (sec))/60/60 |
| Chat average reply time (hrs) | The average time in minutes it took for agent to reply to end user comments during the chat session. | VALUE(Chat average reply time (sec))/60/60 |
| Chat longest reply time (hrs) | The maximum time in minutes it took for agent to reply to end user comments during the chat session. | VALUE(Chat longest reply time (sec))/60/60 |
| Chat no reply time (hrs) | The time in seconds from the end user's last unanswered comment to the end user leaving the chat session. | VALUE(Chat no reply time (sec))/60/60 |
| Chat missed no reply time (hrs) | The time from the end user's last comment to the end user leaving the chat session without getting an agent reply. | IF [Chat completion]="Missed" THEN VALUE(Chat no reply time (sec))/60/60 ENDIF |
| Chat dropped no reply time (hrs) | The time from the end user's last comment to the end user leaving the chat session without getting a reply. | IF [Chat completion]="Dropped" THEN VALUE(Chat no reply time (sec))/60/60 ENDIF |
| Engagement duration (sec) | The time in seconds from the agent joining the chat to when the end user or agent leaves the chat, whichever occurs first. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. When assigned routing is enabled, the timer starts counting when chats are offered to agents. | Engagement duration (sec) |
| Engagement first reply time (sec) | During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. For assignment routing mode, this is the time in seconds between the agent’s assignment time to the chat and the agent's first response.  For broadcast routing mode, this is the time in seconds between the end user's first unanswered message to the agent's first response. | Engagement first reply time (sec) |
| Engagement average reply time (sec) | The average time it took for the agent to reply to each of the end user's messages in the engagement. | Engagement average reply time (sec) |
| Engagement longest reply time (sec) | The maximum time it took for an agent to reply to an end user comment during the chat engagement. | Engagement longest reply time (sec) |
| Engagement duration (min) | The time in minutes from the agent joining the chat to when the end user or agent leaves the chat, whichever occurs first. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. | VALUE(Engagement duration (sec))/60 |
| Engagement first reply time (min) | During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. For assignment routing mode, this is the time in minutes between the agent’s assignment time to the chat and the agent's first response.  For broadcast routing mode, this is the time in minutes between the end user's first unanswered message to the agent's first response. | VALUE(Engagement first reply time (sec))/60 |
| Engagement average reply time (min) | The average time it took for the agent to reply to each of the end user's messages in the engagement. | VALUE(Engagement average reply time (sec))/60 |
| Engagement longest reply time (min) | The maximum time it took for an agent to reply to an end user's comment during the chat engagement. | VALUE(Engagement longest reply time (sec))/60 |
| Engagement duration (hrs) | The time in hours from the agent joining the chat to when the end user or agent leaves the chat, whichever occurs first. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. | VALUE(Engagement duration (sec))/60/60 |
| Engagement first reply time (hrs) | During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. For assignment routing mode, this is the time in hours between the agent’s assignment time to the chat and the agent's first response.  For broadcast routing mode, this is the time in hours between the end user's first unanswered message to the agent's first response. | VALUE(Engagement first reply time (sec))/60/60 |
| Engagement average reply time (hrs) | The average time it took for the agent to reply to each of the end user's messages in the engagement. | VALUE(Engagement average reply time (sec))/60/60 |
| Engagement longest reply time (hrs) | The maximum time it took for an agent to reply to a end user's comment during the chat engagement. | VALUE(Engagement longest reply time (sec))/60/60 |

### Engagement attributes

This section lists and defines all the Engagement attributes available.

Table 2. Engagement attributes

| Attribute | Definition |
| --- | --- |
| Chat ID | The system ID of the Chat session. |
| Chat type | The specific chat type being assigned depending on the way it was initiated. Refers to unsorted values of this attribute. |
| Chat started by | The way chat session was started. Who or what started the chat session? Values: Agent, Visitor and Trigger. |
| Chat completion | The specific status assigned depending on the way the chat session was completed. Values include Missed, Dropped, Completed, and Not Engaged. |
| Chat department | The department to which the Chat session was assigned. |
| Chat deleted | States if a Chat message was deleted. Can be True or False. |
| Chat satisfaction rating | The satisfaction rating that end user left during or after the chat session. Values: Good, Bad or none. |
| Chat skills | Agent abilities necessary to serve the chat session. |
| Chat skills fulfilled | Parameter showing whether this chat was served by an agent with the required set of skills. Values: True or False. |
| Chat tags | The tags applied to a particular Chat session. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Chat trigger fired | Parameter showing whether a system trigger had fired (executed) during the chat session. Values: True or False. |
| Chat country | The country of the chat end user. |
| Chat region | The province or state of the chat end user. |
| Chat city | The city of the chat end user. |
| Chat platform | The platform of device used by end user to initiate chat. For example: iOS, Android, Windows. |
| Chat browser | The browser used by the end user to initiate a chat session. For example: Google Chrome, Mozilla Firefox, Internet Explorer. |
| Engagement ID | The system ID of the chat engagement. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. |
| Engagement started by | The way chat engagement was started. Who or what initiated the chat engagement? During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. Values: Agent, Visitor and Transfer. |
| Engagement assignment | Shows how the engagement was assigned to an agent. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. Values: Self-assigned,\* Assignment Accepted, Assignment Missed  \*The Self-assigned value is applied when the agent accepts a chat in broadcasting mode, when the agent transfers a chat to another agent, or when the agent assigns a chat to themselves. |
| Engagement department | The department to which the chat engagement was assigned. Examples include Support, Sales, or Shipping. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. |
| Engagement satisfaction rating | The satisfaction response that end user left during or after the chat engagement. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. Values: Good, Bad or none |
| Engagement skills | The Agent abilities necessary to serve the chat engagement. During a chat session, end user can interact with multiple agents. Each interaction is counted as a different engagement. |
| Engagement skills fulfilled | Parameter showing whether this chat engagement was served by an agent with the required set of skills. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. Values: True or False |
| Ticket ID | The Ticket ID associated with a chat. |
| Ticket status | The status of the ticket associated with the chat. |
| Ticket custom status name | The name of a custom ticket status. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). For tickets that existed before custom ticket statuses were enabled, this attribute returns **NULL**. Data is available only from October 19, 2023 onward. |
| Ticket custom status category | The category that a custom ticket status is mapped to. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). For tickets that existed before custom ticket statuses were enabled, this attribute returns **Ticket Status**. Data is available only from October 19, 2023 onward. |
| Ticket custom status state | Returns **true** if a custom ticket status is active, or **false** if a custom ticket status is deactivated. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). Data is available only from October 19, 2023 onward. |
| Ticket group | Name of the group where the ticket was assigned. |
| Ticket assignee | The user to whom the ticket is assigned. |
| Ticket brand | The brand of the ticket associated with the chat. |
| Ticket channel | The channel a ticket was created from. For more information about the ticket channels Explore collects, see [Understanding ticket channels in Explore](https://support.zendesk.com/hc/en-us/articles/4408836378394). |
| Ticket form | Ticket form used on the ticket. |
| Ticket organization | The name of the organization associated with the ticket. |
| Ticket priority | The priority of the ticket. |
| Ticket problem ID | The IDs of problem tickets linked with an incident. |
| Ticket requester | The name of the user who requested the ticket. |
| Ticket satisfaction rating | The customer satisfaction rating. |
| Ticket subject | The subject name of the ticket. |
| Ticket support type | Identifies whether tickets were resolved by an AI agent or a human agent. Possible values are Agent and AI agent. |
| Ticket tags | The tags associated with the ticket. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket type | The ticket type. |
| Sharing agreement inbound | Affiliated instances of Zendesk Support and companies who share tickets with current instance of Zendesk Support. |
| Sharing agreement outbound | Affiliated instances of Zendesk Support and companies tickets are shared with. |
| Agent name | The name of the agent associated with the chat. Values for this attribute (and for the other Agent attributes below) include users who currently have an agent or admin role, as well as users who previously had an agent or admin role and were assigned to a ticket at least once. |
| Agent role | The role of the agent associated with the chat. |
| Agent ID | The ID of the agent associated with the chat. |
| Agent email | The email address of the agent associated with the chat. |
| Agent locale | The locale of the agent associated with the chat. |
| Agent status | The status of the agent associated with the chat. Can be Active, Suspended, or Deleted. |
| Agent tags | A list of tags associated with the agent for the chat. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Agent time zone | The user profile time zone of the agent serving the chat. |
| Chat messages brackets | Defined by the number of agent messages. The number of comments submitted during the chat session by the agent. Values: 1-5, 5-10,10-20. |
| Chat agent messages brackets | The numeric ranges that split metrics into the predefined segments. In this case, the brackets are defined by the number of agent messages. Chat agent messages is the number of comments submitted during the chat session by the agent. Values: 1-5, 5-10,10-20. |
| Chat visitor messages brackets | Defined by the number of end user messages. Comments submitted during the chat session by the end user. Values: 1-5, 5-10,10-20. |
| Chat duration brackets | Defined by the Chat duration attribute. The time duration from the first to the last chat message. The first message can come from an end user or from a proactive chat trigger. Calculated in seconds. Values: 0-3 min, 3-6 min, 6-9 min, 9-12 min, >12 min. |
| Chat wait time brackets | Defined by the Chat wait time. The time that the end user was awaiting for the first agent's reply. Calculated in seconds. Values: 0-3 min, 3-6 min, 6-9 min, 9-12 min, >12 min. |
| Chat first reply time brackets | Defined by the Chat first reply time attribute. The time in seconds between the end user joining the chat and the agent’s first response. An end user joins a chat when they send the first chat message or reply to a proactive message. Values: 0-3 min, 3-6 min, 6-9 min, 9-12 min, >12 min |
| Chat average reply time brackets | Defined by the Chat average reply time attribute. The average time it took for an agent to reply to end user comments during the chat session. Values: 0-3 min, 3-6 min, 6-9 min, 9-12 min, >12 min. |
| Chat longest reply time brackets | Defined by the Chat longest reply time attribute. The maximum time it took for an agent to reply to the end user comments during the chat session. Values: 0-3 min, 3-6 min, 6-9 min, 9-12 min, >12 min. |
| Chat no reply time brackets | Defined by the Chat longest reply time attribute. The time from an end users last unanswered comment to the end user leaving the chat session. Values: 0-3 min, 3-6 min, 6-9 min, 9-12 min, >12 min. |
| Engagement messages brackets | The number of engagement messages. 'Chat Messages' is the number of comments submitted during the chat engagement. A chat session can consist of multiple engagements. Values: 1-5, 5-10,10-20. |
| Engagement agent messages brackets | The number of agent engagement messages. 'Chat Agent Messages' are comments submitted during the chat engagement by the agent. A chat session can consist of multiple engagements. Values: 1-5, 5-10,10-20. |
| Engagement visitor messages brackets | The number of end user engagement messages. 'Chat Visitor Messages' is the number of comments submitted during the chat engagement by the end user. A chat session can consist of multiple engagements. Values: 1-5, 5-10,10-20. |
| Engagement duration brackets | The time duration in seconds from the agent joining the chat to when the end user or agent leaves the chat, whichever occurs first. A chat session can consist of multiple engagements. Values: 0-3 min, 3-6 min, 6-9 min, 9-12 min, >12 min. |
| Engagement first reply time brackets | The time between the first end user comment and the first comment provided by an agent during the engagement. A chat session can consist of multiple engagements. Values: 0-3 min, 3-6 min, 6-9 min, 9-12 min, >12 min. |
| Engagement average reply time brackets | The average time it took for an agent to reply to end user comments during the chat engagement. A chat session can consist of multiple engagements. Values: 0-3 min, 3-6 min, 6-9 min, 9-12 min, >12 min. |
| Engagement longest reply time brackets | The maximum time it took for an agent to reply to the end user comments during the chat engagement. A chat session can consist of multiple engagements. Values: 0-3 min, 3-6 min, 6-9 min, 9-12 min, >12 min. |
| Intent (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what the ticket is about. To see the possible values, [open the Taxonomy tab of the Intent settings page](https://support.zendesk.com/hc/en-us/articles/9488234915610) to see the AI Intents list under the **Taxonomy values** heading. |
| Intent confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the intent prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Language (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what language the ticket is written in. To see the possible values, [open the Taxonomy tab of the Intent settings page](https://support.zendesk.com/hc/en-us/articles/9488234915610). |
| Language confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the language prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Sentiment (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of how the customer feels about their request. Possible values are **Very Positive**, **Positive**, **Neutral**, **Negative**, and **Very Negative**. |
| Sentiment confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the sentiment prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Time - Chat started | A collection of attributes in different units that return when a chat started. |
| Time - Chat last updated | A collection of attributes in different units that return when a chat was last updated. This timestamp is affected by certain read-only actions. See [Why are chats being updated after they’re completed?](https://support.zendesk.com/hc/en-us/articles/6845788700698) |
| Time - Engagement started | A collection of attributes in different units that return when chat engagement started. |
| Time - Ticket created | A collection of attributes in different units that return when the ticket associated with the chat was created. |
| Time - Ticket solved | A collection of attributes in different units that return when the ticket associated with the chat was solved. |
| Time - Ticket last updated | A collection of attributes in different units that return when the ticket associated with the chat was last updated. |

## Chat Concurrency dataset

The Chat Concurrency dataset contains metrics and attributes that relate to your
agents’ handling of concurrent chat engagements. We only show data for agents who
had at least a single chat within the hour. Chat agents who were signed in and
available but did not accept any chats will not be reflected.

This section lists all the available elements for the dataset, and contains the
following topics:

- [Chat Concurrency metrics](#topic_ecm_gdp_mrb__section_pnb_jdp_mrb)
- [Chat Concurrency attributes](#topic_ecm_gdp_mrb__section_rnb_jdp_mrb)

### Chat Concurrency metrics

This section lists and defines all of the Chat Concurrency metrics available.

Note: Chat Concurrency metrics include messaging tickets
in addition to chats.

Table 3. Chat Concurrency metrics

| Metric | Definition | Calculation |
| --- | --- | --- |
| Average chat concurrency | The average number of active chats per agent per hour. | [Average chat concurrency] |
| Minimum chat concurrency | The minimum number of active chats per agent per hour. | [Minimum chat concurrency] |
| Maximum chat concurrency | The maximum number of active chats per agent per hour. | [Maximum chat concurrency] |

### Chat Concurrency attributes

This section lists and defines all the Chat Concurrency attributes available.

Table 4. Chat Concurrency attributes

| Attribute | Definition |
| --- | --- |
| Agent name | The name of the agent associated with the chat. Values for this attribute (and for the other Agent attributes below) include users who currently have an agent or admin role, as well as users who previously had an agent or admin role and were assigned to a ticket at least once. |
| Agent role | The role of the agent associated with the chat. |
| Agent email | The email address of the agent associated with the chat. |
| Agent ID | The ID of the agent associated with the chat. |
| Agent status | The status of the agent associated with the chat. Can be Active, Suspended, or Deleted. |
| Agent locale | The locale of the agent associated with the chat. |
| Agent active | Whether the agent is currently active or not. Can be True or False. |
| Time - Agent created | A collection of attributes in different units that return when an agent was created. |
| Time - Agent concurrency | A collection of attributes in different units that return when an agent's concurrent chats occurred. |
| Time - Agent last login | A collection of attributes in different units that return when an agent last logged in to Chat. |