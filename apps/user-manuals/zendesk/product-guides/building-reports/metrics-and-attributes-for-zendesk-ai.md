# Metrics and attributes for Zendesk AI

Source: https://support.zendesk.com/hc/en-us/articles/6961660060186-Metrics-and-attributes-for-Zendesk-AI

---

The metrics and attributes described in this article are used to create the reports included in theZendesk Copilot: Agent productivity prebuilt dashboardand theGenerative AI Agent Tools prebuilt dashboard.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

The metrics and attributes described in this article are used to create the reports
included in the [Zendesk Copilot: Agent productivity prebuilt
dashboard](https://support.zendesk.com/hc/en-us/articles/9308443151258) and the [Generative AI Agent Tools prebuilt dashboard](https://support.zendesk.com/hc/en-us/articles/6961627955994).

This article contains the following topics:

- [Copilot auto assist dataset](#topic_qsz_4fd_mfc)
- [Copilot suggestions dataset](#topic_jly_x2d_mfc)
- [Generative AI agent tools dataset](#topic_cpd_pqk_3bc)
- [Intelligent triage dataset](#topic_hcc_4pv_ngc)

## Copilot auto assist dataset

This section contains the following topics:

- [Copilot auto assist metrics](#topic_tsz_4fd_mfc)
- [Copilot auto assist attributes](#topic_vsz_4fd_mfc)

Note: This dataset retains data only from the previous 90 days.

### Copilot auto assist metrics

This section lists and defines the metrics available in the Copilot auto assist
dataset.

Actions and action flows are planned to be added to the dataset at a later stage.
Currently, only standard actions data is available in this dataset.

|  |  |  |
| --- | --- | --- |
| **Metric** | **Definition** | **Formula** |
| Auto assists | The number of Auto assist interactions that were shown to agents. | [Auto assist ID] |
| Applied auto assists | The number of Auto assist interactions that were applied to the ticket by agents through accepting or editing them. | IF [Auto assist status]!="Dismissed" THEN [Auto assist ID] ENDIF |
| Accepted auto assists | Auto assist interactions that were accepted by agents. | IF [Auto assist status]="Accepted" THEN [Auto assist ID] ENDIF |
| Edited auto assists | Auto assist interactions that were edited by agents. | IF [Auto assist status]="Edited" THEN [Auto assist ID] ENDIF |
| Dismissed auto assists | Auto assist interactions that were dismissed by agents. | IF [Auto assist status]="Dismissed" THEN [Auto assist ID] ENDIF |
| % Acceptance rate | Auto assist interactions that were accepted or edited, divided by the total number of auto assist interactions shown. | D\_COUNT(Applied auto assists)/D\_COUNT(Auto assists) |
| % Dismissal rate | Auto assist interactions that were dismissed divided by the total number of auto assist interactions shown. | D\_COUNT(Dismissed auto assists)/D\_COUNT(Auto assists) |
| Suggestions | The number of auto assist suggestions that were shown to agents. | [Suggestion ID] |
| Applied suggestions | The number of auto assist suggestions that were applied to the ticket by agents through accepting or editing them. | IF [Suggestion status]!="Dismissed" THEN [Suggestion ID] ENDIF |
| Accepted suggestions | The number of Auto assist suggestions that were accepted by agents. | IF [Suggestion status]="Accepted" THEN [Suggestion ID] ENDIF |
| Edited suggestions | The number of Auto assist suggestions that were edited by agents. | IF [Suggestion status]="Edited" THEN [Suggestion ID] ENDIF |
| Dismissed suggestions | The number of Auto assist suggestions that were dismissed by agents. | IF [Auto assist status]="Dismissed" THEN [Suggestion ID] ENDIF |
| % Suggestion acceptance rate | The number of Auto assist suggestions that were accepted or edited, divided by the total number of auto assist interactions shown. | COUNT(Applied suggestions)/COUNT(Suggestions) |
| Auto assist tickets | The number of tickets where Auto assist was provided at least once. | [Auto assist ticket ID] |
| Applied auto assist tickets | The number of tickets where Auto assist was applied at least once. | IF [Auto assist status]!="Dismissed" THEN [Auto assist ticket ID] ENDIF |
| Accepted auto assist tickets | The number of tickets where Auto assist suggestion was accepted at least once | IF [Auto assist status]="Accepted" THEN [Auto assist ticket ID] ENDIF |
| Edited auto assist tickets | The number of tickets where Auto assist suggestion was edited at least once. | IF [Auto assist status]="Edited" THEN [Auto assist ticket ID] ENDIF |
| Dismissed auto assist tickets | The number of tickets where Auto assist suggestion was dismissed at least once. | IF [Auto assist status]="Dismissed" THEN [Auto assist ticket ID] ENDIF |
| Tickets with all auto assists accepted | The number of solved tickets that had all auto assist interactions accepted by the agents. | D\_COUNT(Auto assist tickets)-D\_COUNT(Dismissed auto assist tickets) |
| Tickets | The total number of tickets. | [Ticket ID] |
| Good satisfaction tickets | The number of tickets with a good satisfaction rating. | IF ([Ticket satisfaction rating]="Good") THEN [Ticket ID] ENDIF |
| Rated satisfaction tickets | Tickets that were rated either bad or good by the requester. | IF ([Ticket satisfaction rating]="Good" OR [Ticket satisfaction rating]="Bad") THEN [Ticket ID] ENDIF |
| % Satisfaction score | The percentage of satisfaction surveys rated good. | D\_COUNT(Good satisfaction tickets)/D\_COUNT(Rated satisfaction tickets) |
| Agent replies | The number of public replies added to a ticket by an agent. |  |
| Assignee stations | The number of agents a ticket has been assigned to. |  |
| Group station | The number of groups a ticket has been assigned to. |  |
| Reopens | The number of times a ticket was reopened. |  |
| Agents | The number of active agents and administrators in your Zendesk account. | [Agent ID] |
| Agents used auto assist | The number of agents who used auto assist at least once by accepting, editing or dismissing it. | [Auto assist agent ID] |
| First reply time (min) | The duration in minutes between when the ticket was created and the first public agent reply on the ticket. | VALUE(First reply time (min)) |
| First reply time (hrs) | The duration in days between when the ticket was created and the first public agent reply on the ticket. | VALUE(First reply time (min))/60 |
| First reply time (days) | The duration in hours from when the ticket was created to its latest resolution. | VALUE(First reply time (min))/60/24 |
| Full resolution time (min) | The duration in hours between when the ticket was created and the first public agent reply on the ticket. | VALUE(Full resolution time (min)) |
| Full resolution time (hrs) | The duration in minutes from when the ticket was created to its latest resolution. | VALUE(Full resolution time (min))/60 |
| Full resolution time (days) | The duration in days from when the ticket was created to its latest resolution. | VALUE(Full resolution time (min))/60/24 |

### Copilot auto assist attributes

This section lists and defines the attributes available in the Copilot auto
assist dataset.

|  |  |
| --- | --- |
| **Attribute** | **Definition** |
| Auto assist ID | The Auto assist interaction ID. |
| Auto assist status | The status of the Auto assist interaction: Accepted, Edited or Dismissed. |
| Auto assist procedure | The Auto assist procedure. See [Creating procedures for auto assist](../providing-ai-assistance-with-auto-assist/creating-procedures-for-auto-assist.md). |
| Auto assist agent ID | The user ID of the agent who interacted with the Auto assist. |
| Auto assist ticket ID | The ID of the ticket on which Auto assist was provided. |
| Suggestion ID | The Auto assist suggestion ID. |
| Suggestion status | The status of the Auto assist suggestion: Accepted, Edited or Dismissed. |
| Suggestion type | The type of the Auto Assist suggestion: Reply or Action. |
| Suggestion standard action | The name of the Auto Assist suggestion action. |
| Suggestion action type | The type of the Auto Assist suggestion action: Default or Custom. |
| Ticket ID | The ID number of the ticket. |
| Ticket status | The current status of the ticket. Values: New, Open, Pending, On-Hold, Solved, Closed. |
| Ticket custom status name | The name of a custom ticket status. This attribute appears only if you've enabled [custom ticket statuses](../ticket-customization/activating-custom-ticket-statuses.md). |
| Ticket custom status category | The category that a custom ticket status is mapped to. This attribute appears only if you've enabled [custom ticket statuses](../ticket-customization/activating-custom-ticket-statuses.md). |
| Ticket custom status state | Returns true if a custom ticket status is active, or false if a custom ticket status is deactivated. |
| Ticket group | Name of the group where the ticket is currently assigned. |
| Ticket assignee | The name of the latest ticket assignee. |
| Ticket brand | The brand associated with the ticket. |
| Ticket channel | The channel that initiated creation of the ticket. |
| Ticket form | The current ticket form used on the ticket. |
| Ticket organization | The name of the organization associated with the ticket. |
| Ticket priority | The ticket's priority. |
| Ticket problem ID | The ID of the ticket defined as a problem ticket. |
| Ticket requester | The name of the user who is asking for support through a ticket. |
| Ticket satisfaction rating | The satisfaction rating left by the customer on the ticket. Values: Good, Bad, Offered, Unoffered. |
| Ticket subject | The subject of the ticket. |
| Ticket support type | Identifies whether tickets were resolved by an AI agent or a human agent. Possible values are Agent and AI agent. |
| Ticket tags | Any tags associated with the ticket. |
| Ticket type | The type of ticket. Values: Question, Incident, Problem, Task. |
| Sharing agreement inbound | Affiliated instances of Zendesk Support and companies who share tickets with current instance of Zendesk Support. |
| Sharing agreement outbound | Affiliated instances of Zendesk Support and companies tickets are shared with. |
| Agent name | The name of the agent. |
| Agent role | The role of the agent. |
| Agent ID | The user ID of the agent. |
| Agent email | The email address of the agent. |
| Agent locale | The locale of the agent. |
| Agent status | The user status of the agent. |
| Agent tags | A list of tags associated with the agent. |
| Agent time zone | The time zone of the agent. |
| Time - Auto assist provided | The time when Auto assist was provided to the agent. |
| Time - Ticket created | The time when a ticket was created. |
| Time - Ticket solved | The time when a ticket was solved. |
| Time - Ticket updated | The time when a ticket was last updated. |

## Copilot suggestions dataset

The Copilot suggestions dataset lists the metrics and attributes you can use to [create Explore reports](https://support.zendesk.com/hc/en-us/articles/4408821589530) to measure the engagement and
performance of the following Copilot features: [similar tickets](../setting-up-ai-powered-agent-tools/turning-on-similar-tickets.md), [merging suggestions](https://support.zendesk.com/hc/en-us/articles/8044075423514-Turning-on-merging-suggestions), [quick answers](https://support.zendesk.com/hc/en-us/articles/8079579364250-Turning-on-quick-answers-for-Agent-Workspace), [suggested replies](../setting-up-ai-powered-agent-tools/turning-on-suggested-first-replies.md), and [suggested macros](../setting-up-ai-powered-agent-tools/turning-on-suggested-macros.md).

This dataset is used to create reports in the AI suggestions tab of the [Zendesk Copilot: Agent productivity prebuilt
dashboard](https://support.zendesk.com/hc/en-us/articles/9308443151258).

This section contains the following topics:

- [Copilot suggestions metrics](#topic_jf5_1fd_mfc)
- [Copilot suggestions attributes](#topic_nd5_bfd_mfc)

### Copilot suggestions metrics

This section lists and defines the metrics available in the Copilot suggestions
dataset.

|  |  |  |
| --- | --- | --- |
| **Metric** | **Definition** | **Formula** |
| Suggestions | The number of AI suggestions shown to agents. AI suggestions include similar tickets, merging suggestions, quick answers, suggested first replies, and suggested macros. Auto assist suggestions aren't included. | [Suggestion ID] |
| Accepted suggestions | The number of AI suggestions accepted by agents.  - A [similar ticket](https://support.zendesk.com/hc/en-us/articles/8036381366426#topic_vlg_33v_xyb)   suggestion is considered accepted when a user opens or   hovers over at least one of the suggested similar   tickets. - A [merging   suggestion](https://support.zendesk.com/hc/en-us/articles/8044075423514) is considered accepted when the   user merges at least one of the suggested tickets. - A [quick answer](https://support.zendesk.com/hc/en-us/articles/8079579364250)   is considered accepted when a user gives it a thumbs-up   or copies it to the conversation. - A [suggested first   reply](https://support.zendesk.com/hc/en-us/articles/8037936748570) is counted as accepted when a user   presses Tab to accept the suggestion. Acceptance also   includes suggestions which were accepted and edited by   agents. - A [suggested   macro](https://support.zendesk.com/hc/en-us/articles/4408824813722) is considered accepted when a user   applies a suggested macro. | IF [Suggestion status]="Accepted" THEN [Suggestion ID] ENDIF |
| Ignored suggestions | The number of AI suggestions that were not accepted by agents. | IF [Suggestion status]="Ignored" THEN [Suggestion ID] ENDIF |
| % Acceptance rate | The number of AI suggestions that were accepted, divided by the total number of AI suggestions shown. | COUNT(Accepted suggestions)/COUNT(Suggestions) |
| AI suggestions tickets | The number of tickets with an AI suggestion shown at least once. | [Suggestion ticket ID] |
| Accepted AI suggestions tickets | The number of tickets where an AI suggestion was accepted at least once. | IF [Suggestion status]="Accepted" THEN [Suggestion ticket ID] ENDIF |
| Tickets with all AI suggestions ignored | The number of tickets where no AI suggestion was accepted. | D\_COUNT(AI suggestion tickets)-D\_COUNT(Accepted AI suggestion tickets) |
| Tickets | The total number of tickets. | [Ticket ID] |
| Good satisfaction tickets | The number of tickets with a good satisfaction rating. | IF ([Ticket satisfaction rating]="Good") THEN [Ticket ID] ENDIF |
| Rated satisfaction tickets | Tickets that were rated either bad or good by the requester. | IF ([Ticket satisfaction rating]="Good" OR [Ticket satisfaction rating]="Bad") THEN [Ticket ID] ENDIF |
| % Satisfaction score | The percentage of satisfaction surveys rated good. | COUNT(Good satisfaction tickets)/COUNT(Rated satisfaction tickets) |
| Agent replies | The number of public replies added to a ticket by an agent. | (Agent replies) |
| Assignee stations | The number of agents a ticket has been assigned to. | (Assignee stations) |
| Group station | The number of groups a ticket has been assigned to. | (Group stations) |
| Reopens | The number of times a ticket was reopened. | (Reopens) |
| Agents | The number of active agents and administrators in your Zendesk account. | [Agent ID] |
| Agents used AI suggestions | The number of agents who used AI suggestions at least once by accepting or ignoring it. | [Suggestion agent ID] |
| First reply time (min) | The duration in minutes between when the ticket was created and the first public agent reply on the ticket. | [First reply time (min)] |
| Full resolution time (min) | The duration in minutes from when the ticket was created to its latest resolution. | [Full resolution time (min)] |
| First reply time (hrs) | The duration in hours between when the ticket was created and the first public agent reply on the ticket. | VALUE(First reply time (min))/60 |
| Full resolution time (hrs) | The duration in hours from when the ticket was created to its latest resolution. | VALUE(Full resolution time (min))/60 |
| First reply time (days) | The duration in days between when the ticket was created and the first public agent reply on the ticket. | VALUE(First reply time (min))/60/24 |
| Full resolution time (days) | The duration in days from when the ticket was created to its latest resolution. | VALUE(Full resolution time (min))/60/24 |

### Copilot suggestions attributes

This section lists and defines the attributes available in the Copilot
suggestions dataset.

|  |  |
| --- | --- |
| **Attribute** | **Definition** |
| Suggestion ID | The unique ID for the AI suggestion. |
| Suggestion status | The status of the AI suggestion. Values can be Accepted or Ignored. |
| Suggestion type | The type of the AI suggestion. Values can be [suggested macros](../setting-up-ai-powered-agent-tools/turning-on-suggested-macros.md), [suggested first replies](../setting-up-ai-powered-agent-tools/turning-on-suggested-first-replies.md), [similar tickets](../setting-up-ai-powered-agent-tools/turning-on-similar-tickets.md), [merging suggestions](https://support.zendesk.com/hc/en-us/articles/8044075423514-Turning-on-merging-suggestions), or [quick answers](https://support.zendesk.com/hc/en-us/articles/8079579364250-Turning-on-quick-answers-for-Agent-Workspace). |
| Suggestion agent ID | The user ID of the agent who interacted with the AI suggestion. |
| Suggestion ticket ID | The ID of the ticket on which AI suggestion was provided. |
| Ticket ID | The ID number of the ticket. |
| Ticket status | The current status of the ticket. Values can be New, Open, Pending, On-Hold, Solved or Closed. |
| Ticket custom status name | The name of a custom ticket status. This attribute appears only if you've activated [custom ticket statuses](../ticket-customization/activating-custom-ticket-statuses.md). |
| Ticket custom status category | The category that a custom ticket status is mapped to. This attribute appears only if you've activated [custom ticket statuses](../ticket-customization/activating-custom-ticket-statuses.md). |
| Ticket custom status state | Returns true if a custom ticket status is active, or false if a custom ticket status is deactivated. |
| Ticket group | Name of the group where the ticket is currently assigned. |
| Ticket assignee | The name of the latest ticket assignee. |
| Ticket brand | The brand associated with the ticket. |
| Ticket channel | The channel that initiated creation of the ticket. |
| Ticket form | The current ticket form used on the ticket. |
| Ticket organization | The name of the organization associated with the ticket. |
| Ticket priority | The ticket's priority. |
| Ticket problem ID | The ID of the ticket defined as a problem ticket. |
| Ticket requester | The name of the user who is asking for support through a ticket. |
| Ticket satisfaction rating | The satisfaction rating left by the customer on the ticket. Values can be Good, Bad, Offered, Unoffered. |
| Ticket subject | The subject of the ticket. |
| Ticket support type | Identifies whether tickets were resolved by an AI agent or a human agent. Possible values are Agent and AI agent. |
| Ticket tags | Any tags associated with the ticket. |
| Ticket type | The type of ticket. Values can be Question, Incident, Problem, Task. |
| Sharing agreement inbound | Affiliated instances of Zendesk Support and companies who share tickets with current instance of Zendesk Support. |
| Sharing agreement outbound | Affiliated instances of Zendesk Support and companies tickets are shared with. |
| Agent name | The name of the agent. |
| Agent role | The role of the agent. |
| Agent ID | The user ID of the agent. |
| Agent email | The email address of the agent. |
| Agent locale | The locale of the agent. |
| Agent status | The user status of the agent. |
| Agent tags | A list of tags associated with the agent. |
| Agent time zone | The time zone of the agent. |
| Time - AI suggestion provided | A collection of attributes that return the time an AI suggestion was provided to an agent. |
| Time - Ticket created | A collection of attributes that return the time of the ticket creation. |
| Time - Ticket solved | A collection of attributes that return the time of the ticket resolution. |
| Time - Ticket last updated | A collection of attributes that return the time of the last ticket update. |

## Generative AI agent tools dataset

The Generative AI agent tools dataset lists the metrics and attributes you can use to
[create Explore reports](https://support.zendesk.com/hc/en-us/articles/4408821589530) based on agents’
usage of the following generative AI features: [summarize](https://support.zendesk.com/hc/en-us/articles/5608712782362#topic_ky3_wvc_3xb), [expand](https://support.zendesk.com/hc/en-us/articles/5608712782362#topic_r5d_xvc_3xb), and [make more friendly and make more formal](https://support.zendesk.com/hc/en-us/articles/5608712782362#topic_w25_xvc_3xb).
This dataset is used to create reports included in the AI agent tools tab of the
[Zendesk Copilot: Agent productivity prebuilt
dashboard](https://support.zendesk.com/hc/en-us/articles/9308443151258).

This dataset is also used to create the reports included in the [Generative AI Agent Tools prebuilt dashboard](https://support.zendesk.com/hc/en-us/articles/6961627955994).

The Generative AI agent tools dashboard will be removed in
September 2025 as part of the [Dashboard Builder transition
process](https://support.zendesk.com/hc/en-us/articles/6307402972186-Explore-Analytics-dashboard-builder-transition).

This section contains the following topics:

- [Generative AI agent tools metrics](#topic_mfq_brk_3bc)
- [Generative AI agent tools attributes](#topic_zx2_drk_3bc)

Note: This dataset retains data only from the previous 1200
days. Data is available from August 7th, 2025, onwards.

### Generative AI agent tools metrics

This section lists and defines the metrics available in the Generative AI agent
tools dataset.

|  |  |  |
| --- | --- | --- |
| **Metric** | **Definition** | **Explore formula** |
| Tickets | The total number of tickets. | [Ticket ID] |
| Tickets - No AI | The number of tickets that did not use any AI tools. | IF ([ai\_tool\_usage\_use\_case] = NULL) THEN [Ticket ID] ENDIF |
| Tickets - AI used | The number of tickets where an agent used AI tools. | IF ([ai\_tool\_usage\_use\_case] != NULL) THEN [Ticket ID] ENDIF |
| First assignment to resolution time (min) | The duration in minutes between the first agent assignment and the ticket resolution. | DATE\_DIFF([Ticket solved - Timestamp],[Ticket first assigned - Timestamp], "nb\_of\_minutes") |
| Full resolution time (min) | The duration in minutes between ticket creation and its latest resolution. | VALUE(Full resolution time (min)) |
| First reply time (min) | The duration in minutes between ticket creation and the first public agent reply on the ticket. | VALUE(First reply time (min)) |
| Requester wait time (min) | The total combined time in minutes the ticket was in the New, Open, and On-hold statuses. It measures how long a requester was waiting for the agent to reply. | VALUE(Requester wait time (min)) |
| First assignment to resolution time (hrs) | The time in hours between the first agent assignment and the ticket resolution. | DATE\_DIFF([Ticket solved - Timestamp],[Ticket first assigned - Timestamp], "nb\_of\_hours") |
| Full resolution time (hrs) | The duration in hours between ticket creation and its latest resolution. | VALUE(Full resolution time (min))/60 |
| First reply time (hrs) | The duration in hours between ticket creation and the first public agent reply on the ticket. | VALUE(First reply time (min))/60 |
| Requester wait time (hrs) | The total combined time in hours the ticket was in the New, Open, and On-hold statuses. It measures how long a requester was waiting for the agent to reply. | VALUE(Requester wait time (min))/60 |
| Full resolution time (days) | The duration in days between ticket creation and its latest resolution. | VALUE(Full resolution time (min))/60/24 |
| First assignment to resolution time (days) | The time in days between the first agent assignment and resolution of the ticket. | DATE\_DIFF([Ticket solved - Timestamp],[Ticket first assigned - Timestamp], "nb\_of\_days") |
| Requester wait time (days) | The total combined time in days the ticket was in the New, Open, and On-hold statuses. It measures how long a requester was waiting for the agent to reply. | VALUE(Requester wait time (min))/60/24 |
| First reply time (days) | The duration in days between ticket creation and the first public agent reply on the ticket. | VALUE(First reply time (min))/60/24 |
| Full resolution time - No AI Usage Tickets (days) | The duration in days between ticket creation and its latest resolution for tickets that did not use AI tools. | IF ([ai\_tool\_usage\_use\_case] = NULL) THEN VALUE(Full resolution time (min))/60/24 ENDIF |
| Full resolution time - AI Usage Tickets (days) | The duration in days between ticket creation and its latest resolution for tickets that used AI tools. | IF ([ai\_tool\_usage\_use\_case] != NULL) THEN VALUE(Full resolution time (min))/60/24 ENDIF |
| First reply time - Business hours (min) | The duration in minutes between ticket creation and the first public agent reply on the ticket within business hours. | VALUE(First reply time - Business hours (min)) |
| Full resolution time - Business hours (min) | The duration in minutes between ticket creation and its latest resolution within business hours. | VALUE(Full resolution time - Business hours (min)) |
| Requester wait time - Business hours (min) | The total combined time in minutes the ticket was in the New, Open, and On-hold statuses within business hours. It measures how long a requester was waiting for the agent to reply within business hours. | VALUE(Requester wait time - Business hours (min)) |
| First reply time - Business hours (hrs) | The duration in hours between ticket creation and the first public agent reply on the ticket within business hours. | VALUE(First reply time - Business hours (min))/60 |
| Full resolution time - Business hours (hrs) | The duration in hours between ticket creation and its latest resolution within business hours. | VALUE(Full resolution time - Business hours (min))/60 |
| Requester wait time - Business hours (hrs) | The total combined time in hours the ticket was in the New, Open, and On-hold statuses within business hours. | VALUE(Requester wait time - Business hours (min))/60 |
| Public comments | The number of public comments posted on the ticket. | [public\_comment\_ticket\_update\_id] |
| Public comments per ticket | The number of public comments posted per ticket. | DCOUNT\_VALUES([public\_comment\_ticket\_update\_id]) / DCOUNT\_VALUES([Ticket ID]) |
| Agent comments | The number of comments posted on the ticket by agents. | [agent\_comment\_ticket\_update\_id] |
| Agent comments per ticket | The number of agent comments posted per ticket. | COUNT(Agent comments]) / COUNT([Ticket ID]) |
| Good satisfaction tickets | The number of tickets that were rated as Good by the requester (end user). | IF ([Ticket satisfaction rating]="Good") THEN [Ticket ID] ENDIF |
| Rated satisfaction tickets | The number of tickets that were rated as Bad or Good by the requester (end user). | IF ([Ticket satisfaction rating]="Good" OR [Ticket satisfaction rating]="Bad") THEN [Ticket ID] ENDIF |
| % Satisfaction score | The percentage of the tickets that were rated as Good by the requester (end user) from the total amount of satisfaction-rated tickets. | COUNT(Good satisfaction tickets)/COUNT(Rated satisfaction tickets) |
| Summarize ticket | The number of times a ticket summary is generated by an agent. | IF ([ai\_tool\_usage\_use\_case] = 4) THEN [ai\_tool\_usage\_object\_id] ENDIF |
| Expand text | The number of times the expand feature is applied to a comment in the composer by an agent. | IF ([ai\_tool\_usage\_use\_case] = 3) THEN [ai\_tool\_usage\_object\_id] ENDIF |
| Tone shift - Any | The number of times the tone shift features (make more friendly or make more formal) are applied to a comment in the composer by an agent. | IF ([ai\_tool\_usage\_use\_case] = 2 OR [ai\_tool\_usage\_use\_case] = 1 ) THEN [ai\_tool\_usage\_object\_id] ENDIF |
| Tone shift - Formal | The number of times the tone shift feature (make more formal) is applied to a comment in the composer by an agent. | IF ([ai\_tool\_usage\_use\_case] = 1) THEN [ai\_tool\_usage\_object\_id] ENDIF |
| Tone shift - Friendly | The number of times the tone shift feature (make more friendly) is applied to a comment in the composer by an agent. | IF ([ai\_tool\_usage\_use\_case] = 2) THEN [ai\_tool\_usage\_object\_id] ENDIF |
| AI tool usage event id | The AI tool usage event ID. Used to count the number of times an agent AI tool was used. | [ai\_tool\_usage\_object\_id] |

### Generative AI agent tools attributes

This section lists and defines the attributes available in the Generative AI
agent tools dataset.

|  |  |
| --- | --- |
| **Attribute** | **Definition** |
| AI usage type | The AI tool usage type. Possible values include **No AI Usage**, **Make more formal**, **Make more friendly**, **Expand**, and **Summarize**. |
| AI usage - Ticket ID | The ticket ID associated with the AI tool usage.  **Note:** If an agent uses any AI tools on a new ticket before submitting their first comment, no associated ticket ID is recorded because no ticket ID exists until the agent clicks Submit. However, the AI tool usage is still counted as part of the **AI usage type** metric. |
| Agent name | The name of the agent who used the AI tool. |
| Ticket ID | The ID of the ticket. |
| Ticket status | The status of the ticket. Possible values include **New**, **Open**, **Pending**, **On-hold**, **Solved**, and **Closed**. |
| Ticket group | The group to which the ticket belongs. |
| Ticket brand | The brand of the ticket. |
| Ticket channel | The channel a ticket was created from. |
| Ticket form | The current ticket form used on the ticket. |
| Ticket priority | The ticket's priority. |
| Ticket problem ID | The IDs of the ticket defined as a problem ticket. |
| Ticket assignee | The name of the assignee. |
| Ticket requester | The name of the user who is asking for support through a ticket. |
| Ticket subject | The subject line (title) of a ticket. |
| Ticket support type | Identifies whether tickets were resolved by an AI agent or a human agent. Possible values are Agent and AI agent. |
| Ticket tags | The tags associated with the ticket. |
| Ticket type | The ticket type: Question, Incident, Problem, or Task. |
| Ticket organization name | The name of the organization associated with the ticket. |
| Ticket satisfaction rating | The satisfaction rating left by the customer on the ticket. Possible values include **Good**, **Bad**, **Offered**, and **Unoffered**. |
| Ticket brand | The brand to which the ticket belongs. |
| Time - Ticket first assigned | Includes a number of attributes that return the time when a ticket was first assigned to an agent in the ticket history in various time measurements. |
| Time - Ticket solved | Includes a number of attributes that return the time the ticket was last solved in various time measurements. |
| Time - Ticket created | Includes a number of attributes that return the time when the ticket was created in various time measurements. |
| Time - AI tool used | Includes a number of attributes that return the time when the AI tool was used in various time measurements. |

## Intelligent triage dataset

The Intelligent triage dataset contains metrics and attributes that relate to tickets
enriched with intent, language, and sentiment. This section lists all the available
elements for the dataset.

This section contains the following topics:

- [Intelligent triage metrics](#topic_tk3_2rv_ngc)
- [Intelligent triage attributes](#topic_wzs_frv_ngc)

## Intelligent triage metrics

This section lists and defines all metrics available in the Intelligent triage
dataset.

| Metric | Definition | Explore formula |
| --- | --- | --- |
| Tickets | The total number of tickets | [Ticket ID] |
| Solved tickets | The number of solved or closed tickets. | IF ([tickets\_status] = "Solved" OR [tickets\_status] = "Closed") THEN [Ticket ID] ENDIF |
| One-touch tickets | The number of tickets that were solved after one agent reply. | IF (VALUE(Agent replies) <2 AND ([tickets\_status] = "Solved" OR [tickets\_status] ="Closed")) THEN [Ticket ID] ENDIF |
| Two-touch tickets | The number of tickets that were solved after two agent replies. | IF (VALUE(Agent replies) =2 AND ([tickets\_status] = "Solved" OR [tickets\_status] ="Closed")) THEN [Ticket ID] ENDIF |
| Multi-touch tickets | The number of tickets that were solved after more than two agent replies. | IF (VALUE(Agent replies) >2 AND ([tickets\_status] = "Solved" OR [tickets\_status] ="Closed")) THEN [Ticket ID] ENDIF |
| % One-touch tickets | The percentage of tickets that were solved after one agent reply. | COUNT(One-touch tickets)/COUNT(Solved tickets) |
| % Two-touch tickets | The percentage of tickets that were solved after two agent replies. | COUNT(Two-touch tickets)/COUNT(Solved tickets) |
| % Multi-touch tickets | The percentage of tickets that were solved after more than two agent replies. | COUNT(Multi-touch tickets)/COUNT(Solved tickets) |
| Agent replies | The number of public replies added to a ticket by an agent. | (Agent replies) |
| Good satisfaction tickets | The number of tickets with a good satisfaction rating. | IF ([Ticket satisfaction rating]="Good") THEN [Ticket ID] ENDIF |
| Rated satisfaction tickets | Tickets that were rated either bad or good by the requester. | IF ([Ticket satisfaction rating]="Good" OR [Ticket satisfaction rating]="Bad") THEN [Ticket ID] ENDIF |
| % Satisfaction score | The percentage of satisfaction surveys rated good. | COUNT(Good satisfaction tickets)/COUNT(Rated satisfaction tickets) |
| % Enriched | The number of tickets enriched divided by the total number of tickets. | COUNT(Enriched tickets)/COUNT(Tickets) |
| Group stations | The number of groups a ticket has been assigned to. | (Group stations) |
| Assignee stations | The number of agents a ticket has been assigned to. | (Assignee stations) |
| Sentiment rating | Sentiment ratings for all sentiment-enriched tickets. | (Sentiment rating) |
| First reply time (sec) | The duration in seconds between ticket creation and the first public agent reply on the ticket. | (First reply time (sec)) |
| First reply time (min) | The duration in minutes between ticket creation and the first public agent reply on the ticket. | (First reply time (min)) |
| Full resolution time (min) | The duration in minutes from when the ticket was created to its latest resolution. | (Full resolution time (min)) |
| Requester wait time (min) | The number of minutes a ticket spends in the New, Open, and On-hold statuses. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | (Requester wait time (min)) |
| First assignment to resolution time (min) | The duration in minutes between the first agent assignment and the resolution of the ticket. | DATE\_DIFF([Ticket solved - Timestamp],[Ticket first assigned - Timestamp], "nb\_of\_minutes") |
| First reply time (hrs) | The duration in hours between when the ticket was created and the first public agent reply on the ticket. | VALUE(First reply time (min))/60 |
| Full resolution time (hrs) | The duration in hours from when the ticket was created to its latest resolution. | VALUE(Full resolution time (min))/60 |
| First assignment time (hrs) | The time in hours between when a ticket was created and the first time it was assigned to an agent. | DATE\_DIFF([Ticket first assigned - Timestamp], [Ticket created - Timestamp], "nb\_of\_hours") |
| Requester wait time (hrs) | The number of hours a ticket spends in the New, Open, and On-hold statuses. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | VALUE(Requester wait time (min))/60 |
| First assignment to resolution time (hrs) | The duration in hours between the first agent assignment and the resolution of the ticket. | DATE\_DIFF([Ticket solved - Timestamp],[Ticket first assigned - Timestamp], "nb\_of\_hours") |
| Full resolution time (days) | The duration in days from when the ticket was created to its latest resolution. | VALUE(Full resolution time (min))/60/24 |
| First reply time (days) | The duration in days between when the ticket was created and the first public agent reply on the ticket. | VALUE(First reply time (min))/60/24 |
| First assignment time (days) | The time in days between when a ticket was created and the first time it was assigned to an agent. | DATE\_DIFF([Ticket first assigned - Timestamp], [Ticket created - Timestamp], "nb\_of\_days") |
| Requester wait time (days) | The number of days a ticket spends in the New, Open, and On-hold statuses. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. | VALUE(Requester wait time (min))/60/24 |
| First assignment to resolution time (days) | The duration in days between the first agent assignment and the resolution of the ticket. | DATE\_DIFF([Ticket solved - Timestamp],[Ticket first assigned - Timestamp], "nb\_of\_days") |
| First reply time - Business hours (min) | The duration in minutes between when the ticket was created and the first public agent reply on the ticket within business hours. | (First reply time - Business hours (min)) |
| Full resolution time - Business hours (min) | The duration in minutes between when the ticket was created and its latest resolution within business hours. | (Full resolution time - Business hours (min)) |
| Requester wait time - Business hours (min) | The number of minutes a ticket spends in the New, Open, or On-hold status during business hours. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See Requester wait time for further explanation. | (Requester wait time - Business hours (min)) |
| First reply time - Business hours (hrs) | The duration in hours between when the ticket was created and the first public agent reply on the ticket within business hours. | VALUE(First reply time - Business hours (min))/60 |
| Full resolution time - Business hours (hrs) | The duration in hours between when the ticket was created and its latest resolution within business hours. | VALUE(Full resolution time - Business hours (min))/60 |
| Requester wait time - Business hours (hrs) | The number of hours a ticket spends in the New, Open, or On-hold status during business hours. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See Requester wait time for further explanation. | VALUE(Requester wait time - Business hours (min))/60 |

## Intelligent triage attributes

This section lists and defines all attributes available in the Intelligent triage
dataset.

| Attribute | Definition |
| --- | --- |
| Ticket enriched | If the ticket is enriched with sentiment, language, or intent, returns True; otherwise, returns False. |
| Intent category | The category of the intent. |
| Intent subcategory | The subcategory of the intent. |
| Intent | The name of the intent. |
| Intent confidence | The confidence level of the intent prediction, Low, Medium, or High. |
| Intent prediction added | Indicates if a prediction was added for the intent, True or False. |
| Entity | The name of the entity. For example, "Product". |
| Entity value | The name of the value detected on the ticket. For example, "Washing machine V23". |
| Entity prediction added | Indicates if an entity was detected. |
| Time - Entity detected | The time when the entity was detected on the ticket. |
| Sentiment confidence | The confidence level of the sentiment prediction, Low, Medium, or High. |
| Sentiment rating | The ticket's sentiment rating. One of:  - 1 - Very negative - 2 - Negative - 3 - Neutral - 4 - Positive - 5 - Very positive |
| Sentiment prediction added | Indicates if a prediction was added for the sentiment, True or False. |
| Sentiment | The detected sentiment level, Negative, Neutral, or Positive. |
| Language | The language that intelligent triage detected for the ticket. |
| Language confidence | The confidence level of the language prediction, Low, Medium, or High. |
| Language prediction added | Indicates if a prediction was added for the language, True or False. |
| Ticket ID | The ID number of the ticket. |
| Ticket status | The status of the ticket. |
| Ticket group | Name of the group where the ticket is assigned. |
| Ticket channel | The channel a ticket was created from. For more information about the ticket channels Explore collects, see [Understanding ticket channels in Explore](https://support.zendesk.com/hc/en-us/articles/4408836378394). |
| Ticket form | The current ticket form used on the ticket. |
| Ticket priority | The ticket's priority. |
| Ticket subject | The subject of the ticket. |
| Ticket support type | Identifies whether tickets were resolved by an AI agent or a human agent. Possible values are Agent and AI agent. |
| Ticket tags | The tags associated with the ticket. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](reporting-with-tags.md#topic_a15_bjp_plb). |
| Ticket type | The ticket type: Question, Incident, Problem, or Task. |
| Ticket brand | The brand of the ticket. |
| Assignee name | The name of the assignee. Values for this attribute (and for the other Assignee attributes below) include users who currently have an agent or admin role, as well as users who previously had an agent or admin role and were assigned to a ticket at least once. |
| Submitter role | The role of the submitter, either admin, agent, or end user. |
| Ticket satisfaction rating | The satisfaction rating left by the customer on the ticket. Values: Good, Bad, Offered, Unoffered. |
| Assignee stations | The number of agents to whom the ticket was assigned. |
| Time - Ticket created | Includes a number of attributes that return the time and date when the ticket was created in various time measurements. |
| Time - Ticket solved | Includes a number of attributes that return the time and date when the ticket was most recently solved in various time measurements. |
| Time - Ticket first assigned | The time when the ticket was first assigned to an agent. |