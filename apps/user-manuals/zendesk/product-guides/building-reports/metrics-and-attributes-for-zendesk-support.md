# Metrics and attributes for Zendesk Support

Source: https://support.zendesk.com/hc/en-us/articles/4408827693594-Metrics-and-attributes-for-Zendesk-Support

---

Use this article to discover the metrics and attributes you can use to build Explore reports based on your usage of Zendesk Support. These datasets are also used for the Zendesk Support prebuilt dashboards (seeOverview of the Zendesk Support dashboard).

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

Use this article to discover the metrics and attributes you can use to build Explore reports based on your usage of Zendesk Support. These datasets are also used for the Zendesk Support prebuilt dashboards (see [Overview of the Zendesk Support dashboard](../viewing-and-using-dashboards/overview-of-the-zendesk-support-dashboard.md)).

For more information about how to create reports with Explore, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530-Creating-queries).

Tip: [Read this Zendesk blog post](https://www.zendesk.com/blog/customer-service-metrics-matter/) to learn the key customer service metrics that measure performance and drive revenue.

This article contains the following topics:

- [Tickets dataset](#topic_zlf_slp_4y)
- [Updates history dataset](#topic_as3_slp_4y)
- [Backlog history dataset](#topic_dfb_ydg_ndb)
- [SLAs dataset](#topic_cyq_fr4_l2b)
- [Group SLAs dataset](#topic_svt_cjx_kxb)

## Tickets dataset

This section lists the metrics and attributes for the Tickets dataset. The dataset contains general ticket information, not including changes or updates to tickets.
For objects related to ticket changes or updates, see [Updates history dataset](#topic_as3_slp_4y).

This section contains the following topics:

- [Tickets dataset schema](#topic_smk_45f_kkb)
- [Tickets metrics](#topic_sq4_mhq_4y)
- [Tickets attributes](#topic_jnb_4hq_4y)

### Tickets dataset schema

Use this diagram to help you understand the elements of the Tickets dataset and their relationships.

![Tickets dataset schema](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Tickets.jpg)

### Tickets metrics

This sections lists and defines all of the metrics available in the Tickets dataset.

Table 1. Tickets metrics

| Metric | Definition | Explore Formula |
| --- | --- | --- |
| Tickets | The total number of tickets. Note: Deleted tickets are not included in the Tickets dataset. For help, see [Reporting on ticket deletions](https://support.zendesk.com/hc/en-us/articles/4423506813210). | (Ticket ID) |
| Solved tickets | The number of solved or closed tickets. | IF ([Ticket status - Unsorted] = "Solved" OR [Ticket status - Unsorted] = "Closed") THEN [Ticket ID] ENDIF |
| End-user submitted tickets | The number of tickets submitted by customers or by agents who [have been downgraded](https://support.zendesk.com/hc/en-us/articles/4409155967258#topic_n1j_vq5_w2b). | IF ([Submitter role] = "End-user" ) THEN [Ticket ID] ENDIF |
| Agent submitted tickets | The number of tickets submitted by agents or administrators. | IF ([Submitter role] = "Agent" OR [Submitter role] = "Admin") THEN [Ticket ID] ENDIF |
| Reassigned tickets | The number of tickets that have been assigned to more than one agent. | IF (VALUE(Assignee stations)>1) THEN [Ticket ID] ENDIF |
| Reopened tickets | The number of tickets that were reopened after being solved. Doesn’t include tickets solved and reopened during the same update. | IF (VALUE(Reopens)>0) THEN [Ticket ID] ENDIF |
| Unreplied tickets | The number of tickets that have not received an agent response. | IF (VALUE(Agent replies)<1) THEN [Ticket ID] ENDIF |
| Incidents | The number of tickets where the ticket type is Incident. | IF ([Ticket type - Unsorted] = "Incident") THEN [Ticket ID] ENDIF |
| Problems | The number of tickets where the ticket type is 'Problem'. | IF ([Ticket type - Unsorted] = "Problem") THEN [Ticket ID] ENDIF |
| Inbound shared tickets | The number of tickets a Zendesk Support account shared with your Zendesk Support account. | IF ([Sharing agreement inbound]!=NULL) THEN [Ticket ID] ENDIF |
| Outbound shared tickets | The number of tickets your Zendesk Support account shared with another Zendesk Support account | IF ([Sharing agreement outbound]!=NULL) THEN [Ticket ID] ENDIF |
| Tickets created - Daily average | The average number of tickets created each day. | COUNT(Tickets)/DCOUNT\_VALUES([Ticket created - Date]) |
| Tickets solved - Daily average | The average number of tickets solved each day. Tickets are counted only if they are currently solved or closed. | COUNT(Tickets)/DCOUNT\_VALUES([Ticket solved - Date]) |
| Unsolved tickets | The number of unsolved tickets. This includes tickets in every status, except Solved and Closed. | IF ([Ticket status - Unsorted] != "Closed" AND [Ticket status - Unsorted]!= "Solved") THEN [Ticket ID] ENDIF |
| New tickets | The number of tickets that are currently in the New status. | IF ([Ticket status - Unsorted]= "New") THEN [Ticket ID] ENDIF |
| Open tickets | The number of tickets that are currently in the Open status. | IF ([Ticket status - Unsorted]= "Open") THEN [Ticket ID] ENDIF |
| Pending tickets | The number of tickets that are currently in the Pending status. | IF ([Ticket status - Unsorted]= "Pending") THEN [Ticket ID] ENDIF |
| On-hold tickets | The number of tickets that are currently in the On-hold status. | IF ([Ticket status - Unsorted]= "Hold") THEN [Ticket ID] ENDIF |
| Unassigned unsolved tickets | The number of open tickets currently not assigned. | IF ([Assignee ID] = NULL AND [Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed") THEN [Ticket ID] ENDIF |
| Assigned unsolved tickets | The number of open, assigned tickets. | IF ([Assignee ID] != NULL AND [Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed") THEN [Ticket ID] ENDIF |
| Unreplied unsolved tickets | The number of open tickets without a first reply. | IF (VALUE(Agent replies)<1 AND [Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed") THEN [Ticket ID] ENDIF |
| Agent replies | The number of public replies added to a ticket by an agent. | (Agent replies) |
| Assignee stations | The number of agents a ticket has been assigned to. | (Assignee stations) |
| Group stations | The number of groups a ticket has been assigned to. | (Group stations) |
| Reopens | The number of times a ticket was reopened. | (Reopens) |
| One-touch tickets | The number of tickets that were solved after one agent reply. When a chat session is added to a ticket with at least one message from an agent, this counts as one touch. | IF (VALUE(Agent replies) <2 AND ([Ticket status - Unsorted] = "Solved" OR [Ticket status - Unsorted] ="Closed")) THEN [Ticket ID] ENDIF |
| Two-touch tickets | The number of tickets that were solved after two agent replies. | IF (VALUE(Agent replies) =2 AND ([Ticket status - Unsorted] = "Solved" OR [Ticket status - Unsorted] ="Closed")) THEN [Ticket ID] ENDIF |
| Multi-touch tickets | The number of tickets that were solved after more than two agent replies. | IF (VALUE(Agent replies) >2 AND ([Ticket status - Unsorted] = "Solved" OR [Ticket status - Unsorted] ="Closed")) THEN [Ticket ID] ENDIF |
| % One-touch tickets | The percentage of tickets that were solved after one agent reply. | COUNT(One-touch tickets)/COUNT(Solved tickets) |
| % Two-touch tickets | The percentage of tickets that were solved after two agent replies. | COUNT(Two-touch tickets)/COUNT(Solved tickets) |
| % Multi-touch tickets | The percentage of tickets that were solved after more than two agent replies. | COUNT(Multi-touch tickets)/COUNT(Solved tickets) |
| Good satisfaction tickets | The number of tickets with a good satisfaction rating. | IF ([Ticket satisfaction rating]="Good") THEN [Ticket ID] ENDIF |
| Bad satisfaction tickets | The number of tickets with a bad satisfaction rating. | IF ([Ticket satisfaction rating]="Bad") THEN [Ticket ID] ENDIF |
| Good satisfaction tickets w/comment | Tickets that have a good satisfaction rating and an associated comment. | IF ([Ticket satisfaction rating]="Good" AND [Ticket satisfaction comment]!=NULL) THEN [Ticket ID] ENDIF |
| Bad satisfaction tickets w/comment | Tickets that have a bad satisfaction rating and an associated comment. | IF ([Ticket satisfaction rating]="Bad" AND [Ticket satisfaction comment]!=NULL) THEN [Ticket ID] ENDIF |
| Rated satisfaction tickets | Tickets that were rated either bad or good by the requester. | IF ([Ticket satisfaction rating]="Good" OR [Ticket satisfaction rating]="Bad") THEN [Ticket ID] ENDIF |
| Surveyed satisfaction tickets | Tickets that were surveyed by a satisfaction survey | IF ([Ticket satisfaction rating] = "Offered") OR ([Ticket satisfaction rating]="Good" OR ([Ticket satisfaction rating]="Bad" THEN [Ticket ID] ENDIF |
| Unsurveyed satisfaction tickets | Tickets that were not surveyed by a satisfaction survey. | IF ([Ticket satisfaction rating] = "Unoffered") THEN [Ticket ID] ENDIF |
| % Satisfaction score | The percentage of satisfaction surveys rated good. | COUNT(Good satisfaction tickets)/COUNT(Rated satisfaction tickets) |
| % Satisfaction rated | The percentage of tickets rated with either good or bad satisfaction. | COUNT(Rated satisfaction tickets)/COUNT(Surveyed satisfaction tickets) |
| % Satisfaction surveyed | The percentage of tickets that were surveyed by a satisfaction survey. | COUNT(Surveyed satisfaction tickets)/COUNT(Tickets) |
| Tickets w/skills | The number of tickets that have a skill associated with them. | IF ([Ticket skills]!=NULL) THEN [Ticket ID] ENDIF |
| Tickets w/o skills | The number of tickets that do not have a skill associated with them. | IF ([Ticket skills]=NULL) THEN [Ticket ID] ENDIF |
| Set ticket skills | The number of skills in tickets where agent skills were applied. | IF ([Ticket skills]!=NULL) THEN [Ticket ID] ENDIF |
| Fulfilled ticket skills | The number of tickets where skills in an agents profile were matched with ticket skills. | IF ([Ticket skills]!=NULL AND [Assignee skills]!=NULL AND [Assignee skills]=[Ticket skills]) THEN [Ticket ID] ENDIF |
| % Ticket skill fulfillment rate | The percentage of tickets where agent skills were matched with ticket skills to the total number of tickets with skills applied. | COUNT(Fulfilled ticket skills)/COUNT(Set ticket skills) |
| % Ticket skill usage rate | The percentage of tickets with skills set to the total number of tickets. | D\_COUNT(Tickets w/skills)/COUNT(Tickets) |
| Users | The number of active user profiles. | IF ([Requester status] = "Active") THEN [Requester ID] ENDIF |
| Agents | The number of active agents and administrators in your Zendesk account. | IF ([Requester status] = "Active" AND [Requester role] != "End-user") THEN [Requester ID] ENDIF |
| End-users | The number of active end-user (customer) profiles. | IF ([Requester status] = "Active" AND [Requester role] = "End-user") THEN [Requester ID] ENDIF |
| Suspended users | The number of users in the suspended status. | IF ([Requester status] = "Suspended") THEN [Requester ID] ENDIF |
| Deleted users | The number of users in the deleted status. | IF ([Requester status] = "Deleted") THEN [Requester ID] ENDIF |
| Assignees | The number of agents that were assigned to the ticket at least once. | IF ([Assignee status]= "Active") THEN [Assignee ID] ENDIF |
| Requesters | The number of current requesters. | IF ([Requester status]= "Active" AND [Ticket ID]!=NULL) THEN [Requester ID] ENDIF |
| Organizations | The number of active organizations. | IF ([Requester organization status]="Active") THEN [Requester organization ID] ENDIF |
| Deleted organizations | The number of organizations that have been deleted. | IF ([Requester organization status]="Deleted") THEN [Requester organization ID] ENDIF |
| First reply time (min) | The duration in minutes between when the ticket was created and the first public agent reply on the ticket. | (First reply time (min)) |
| First reply time (sec) | The duration in seconds between when the ticket was created and the first public agent reply on the ticket. This metric applies only to the [Messaging ticket channel](https://support.zendesk.com/hc/en-us/articles/4408836378394#topic_wp4_gvb_lhb:~:text=follow%2Dup%20tickets.)-,Messaging,-Messaging). | (First reply time (sec)) |
| First resolution time (min) | The number of minutes between when the ticket was created and when it was first resolved. | (First resolution time (min)) |
| Full resolution time - min | The duration in minutes from when the ticket was created to its latest resolution. | (Full resolution time (min)) |
| Requester wait time (min) | The number of minutes a ticket spends in the New, Open, and On-hold statuses. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | (Requester wait time (min)) |
| Agent wait time (min) | The total time in minutes that a ticket was in the pending status. It measures how long agents were waiting for the customer replies. | (Agent wait time (min)) |
| On-hold time (min) | The total time in minutes that a ticket was in the on-hold status. | (On-hold time (min)) |
| First assignment time (min) | The time in minutes between when a ticket was created and the first time it was assigned to an agent. | DATE\_DIFF([Ticket first assigned - Timestamp], [Ticket created - Timestamp], "nb\_of\_minutes") |
| Last assignment time (min) | The duration in minutes between when the ticket was created and the last time an agent was assigned to the ticket. | DATE\_DIFF([Ticket assigned - Timestamp], [Ticket created - Timestamp], "nb\_of\_minutes") |
| First assignment to resolution time (min) | The duration in minutes between the first agent assignment and the resolution of the ticket. | DATE\_DIFF([Ticket solved - Timestamp],[Ticket first assigned - Timestamp], "nb\_of\_minutes") |
| Last assignment to resolution time (min) | The duration in minutes between the last agent assignment and the resolution of the ticket. | DATE\_DIFF([Ticket solved - Timestamp],[Ticket assigned - Timestamp], "nb\_of\_minutes") |
| First reply time (hrs) | The duration in hours between when the ticket was created and the first public agent reply on the ticket. | VALUE(First reply time (min))/60 |
| First resolution time (hrs) | The number of hours between when the ticket was created and when it was first resolved. | VALUE(First resolution time (min))/60 |
| Full resolution time (hrs) | The duration in hours from when the ticket was created to its latest resolution. | VALUE(Full resolution time (min))/60 |
| Requester wait time (hrs) | The number of hours a ticket spends in the New, Open, and On-hold statuses. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | VALUE(Requester wait time (min))/60 |
| Agent wait time (hrs) | The total time in hours that a ticket was in the pending status. It measures how long agents were waiting for the customer replies. | VALUE(Agent wait time (min))/60 |
| On-hold time (hrs) | The total time in hours that a ticket was in the on-hold status. | VALUE(On-hold time (min))/60 |
| First assignment time (hrs) | The time in hours between when a ticket was created and the first time it was assigned to an agent. | DATE\_DIFF([Ticket first assigned - Timestamp], [Ticket created - Timestamp], "nb\_of\_hours") |
| Last assignment time (hrs) | The duration in hours between when the ticket was created and the last time an agent was assigned to the ticket. | DATE\_DIFF([Ticket assigned - Timestamp], [Ticket created - Timestamp], "nb\_of\_hours") |
| First assignment to resolution time (hrs) | The duration in hours between the first agent assignment and the resolution of the ticket. | DATE\_DIFF([Ticket solved - Timestamp],[Ticket first assigned - Timestamp], "nb\_of\_hours") |
| Last assignment to resolution time (hrs) | The duration in hours between the last agent assignment and the resolution of the ticket. | DATE\_DIFF([Ticket solved - Timestamp],[Ticket assigned - Timestamp], "nb\_of\_hours") |
| First reply time (days) | The duration in days between when the ticket was created and the first public agent reply on the ticket. | VALUE(First reply time (min))/60/24 |
| First resolution time (days) | The number of days between when the ticket was created and when it was first resolved. | VALUE(First resolution time (min))/60/24 |
| Full resolution time (days) | The duration in days from when the ticket was created to its latest resolution. | VALUE(Full resolution time (min))/60/24 |
| Requester wait time (days) | The number of days a ticket spends in the New, Open, and On-hold statuses. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | VALUE(Requester wait time (min))/60/24 |
| Agent wait time (days) | The total time in days that a ticket was in the pending status. It measures how long agents were waiting for the customer replies. | VALUE(Agent wait time (min))/60/24 |
| On-hold time (days) | The total time in days that a ticket was in the on-hold status. | VALUE(On-hold time (min))/60/24 |
| First assignment time (days) | The time in days between when a ticket was created and the first time it was assigned to an agent. | DATE\_DIFF([Ticket first assigned - Timestamp], [Ticket created - Timestamp], "nb\_of\_days") |
| Last assignment time (days) | The duration in days between when the ticket was created and the last time an agent was assigned to the ticket. | DATE\_DIFF([Ticket assigned - Timestamp], [Ticket created - Timestamp], "nb\_of\_days") |
| First assignment to resolution time (days) | The duration in days between the first agent assignment and the resolution of the ticket. | DATE\_DIFF([Ticket solved - Timestamp],[Ticket first assigned - Timestamp], "nb\_of\_days") |
| Last assignment to resolution time (days) | The duration in days between the last agent assignment and the resolution of the ticket. | DATE\_DIFF([Ticket solved - Timestamp],[Ticket assigned - Timestamp], "nb\_of\_days") |
| Unsolved tickets age (min) | The duration in minutes between when an unsolved ticket was created and now. | IF ([Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed") THEN DATE\_DIFF(NOW(), [Ticket created - Timestamp], "nb\_of\_minutes") ENDIF |
| Unsolved tickets time since update (min) | The duration in minutes between an unsolved tickets last update and now. | IF ([Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed") THEN DATE\_DIFF(NOW(), [Ticket updated - Timestamp], "nb\_of\_minutes") ENDIF |
| Time since user login (min) | The time passed in minutes since the last user logged in. | IF ([Requester status] = "Active" AND [Requester Sign-in - Date] != NULL) THEN DATE\_DIFF(NOW(), [Requester Sign-in - Timestamp], "nb\_of\_minutes") ENDIF |
| Time since assignee login (min) | The time passed in minutes since the last assignee logged in. | IF ([Assignee status] = "Active" AND [Assignee Sign-in - Date] != NULL AND [Assignee ID] !=NULL) THEN DATE\_DIFF(NOW(), [Assignee Sign-in - Timestamp], "nb\_of\_minutes") ENDIF |
| Unsolved tickets age (hrs) | The duration in hours between when an unsolved ticket was created and now. | IF ([Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed") THEN DATE\_DIFF(NOW(), [Ticket created - Timestamp], "nb\_of\_hours") ENDIF |
| Unsolved tickets time since update (hrs) | The duration in hours between an unsolved tickets last update and now. | IF ([Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed") THEN DATE\_DIFF(NOW(), [Ticket updated - Timestamp], "nb\_of\_hours") ENDIF |
| Time since user login (hrs) | The time passed in hours since the last user logged in. | IF ([Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed") THEN DATE\_DIFF(NOW(), [Ticket updated - Timestamp], "nb\_of\_hours") ENDIF |
| Time since assignee login (hrs) | The time passed in hours since the last assignee logged in. | IF ([Assignee status] = "Active" AND [Assignee Sign-in - Date] != NULL AND [Assignee ID] !=NULL) THEN DATE\_DIFF(NOW(), [Assignee Sign-in - Timestamp], "nb\_of\_hours") ENDIF |
| Unsolved tickets age (days) | The duration in days between when an unsolved ticket was created and now. | IF ([Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed") THEN DATE\_DIFF(NOW(), [Ticket created - Timestamp], "nb\_of\_days") ENDIF |
| Unsolved tickets time since update (days) | The duration in days between an unsolved tickets last update and now. | IF ([Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed") THEN DATE\_DIFF(NOW(), [Ticket updated - Timestamp], "nb\_of\_days") ENDIF |
| Time since user login (days) | The time passed in days since the last user logged in. | IF ([Requester status] = "Active" AND [Requester Sign-in - Date] != NULL) THEN DATE\_DIFF(NOW(), [Requester Sign-in - Timestamp], "nb\_of\_days") ENDIF |
| Time since assignee login (days) | The time passed in days since the last assignee logged in. | IF ([Assignee status] = "Active" AND [Assignee Sign-in - Date] != NULL AND [Assignee ID] !=NULL) THEN DATE\_DIFF(NOW(), [Assignee Sign-in - Timestamp], "nb\_of\_days") ENDIF |
| First reply time - Business hours (min) | The duration in minutes between when the ticket was created and the first public agent reply on the ticket within business hours. | (First reply time - Business hours (min)) |
| First resolution time - Business hours (min) | The duration in minutes between when the ticket was created and its first resolution within business hours. | (First resolution time - Business hours (min)) |
| Full resolution time - Business hours (min) | The duration in minutes between when the ticket was created and its latest resolution within business hours. | (Full resolution time - Business hours (min)) |
| Requester wait time - Business hours (min) | The number of minutes a ticket spends in the New, Open, or On-hold status during business hours. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | (Requester wait time - Business hours (min)) |
| Agent wait time - Business hours (min) | The total combined time in minutes that the ticket was in the pending status within business hours. It measures how long agents were waiting for the customer replies within business hours. | (Agent wait time - Business hours (min)) |
| On-hold time - Business hours (min) | The total combined time in minutes that the ticket was in the on-hold status during business hours. | On-hold time - Business hours (min) |
| First reply time - Business hours (hrs) | The duration in hours between when the ticket was created and the first public agent reply on the ticket within business hours. | VALUE(First reply time - Business hours (min))/60 |
| First resolution time - Business hours (hrs) | The duration in hours between when the ticket was created and its first resolution within business hours. | VALUE(First resolution time - Business hours (min))/60 |
| Full resolution time - Business hours (hrs) | The duration in hours between when the ticket was created and its latest resolution within business hours. | VALUE(Full resolution time - Business hours (min))/60 |
| Requester wait time - Business hours (hrs) | The number of hours a ticket spends in the New, Open, or On-hold status during business hours. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | VALUE(Requester wait time - Business hours (min))/60 |
| Agent wait time - Business hours (hrs) | The total combined time in hours that the ticket was in the pending status within business hours. It measures how long agents were waiting for the customer replies within business hours. | VALUE(Agent wait time - Business hours (min))/60 |
| On-hold time - Business hours (hrs) | The total combined time in hours that the ticket was in the on-hold status during business hours. | VALUE(On-hold time - Business hours (min))/60 |
| Tickets created - Last 7 days | The number of tickets created in the last 7 days. | (Tickets created - Last 7 days) |
| Tickets created - Previous 7 days | The number of tickets created between 7 and 14 days ago. | (Tickets created - Previous 7 days) |
| Tickets created - Last 30 days | The number of tickets created in the last 30 days. | (Tickets created - Last 30 days) |
| Tickets created - Previous 30 days | The number of tickets created between 30 and 60 days ago. | (Tickets created - Previous 30 days) |
| Tickets created - This week | The number of tickets created over the current week. | (Tickets created - This week) |
| Tickets created - Last week | The number of tickets created over the previous week. | (Tickets created - Last week) |
| Tickets created - This month | The number of tickets created over the current month. | (Tickets created - This month) |
| Tickets created - last month | The number of tickets created over the previous month. | (Tickets created - last month) |
| Tickets created - This year | The number of tickets created this year. | (Tickets created - This year) |
| Tickets created - Last year | The number of tickets created last year. | (Tickets created - Last year) |
| Tickets solved - Last 7 days | The number of tickets solved in the last 7 days. Tickets are counted only if they are currently solved or closed. | (Tickets solved - Last 7 days) |
| Tickets solved - Previous 7 days | The number of tickets solved between 7 and 14 days ago. Tickets are counted only if they are currently solved or closed. | (Tickets solved - Previous 7 days) |
| Tickets solved - Last 30 days | The number of tickets solved in the last 30 days. Tickets are counted only if they are currently solved or closed. | (Tickets solved - Last 30 days) |
| Tickets solved - Previous 30 days | The number of tickets solved between 30 and 60 days ago. Tickets are counted only if they are currently solved or closed. | (Tickets solved - Previous 30 days) |
| Tickets solved - This week | The number of tickets solved over the current week. Tickets are counted only if they are currently solved or closed. | (Tickets solved - This week) |
| Tickets solved - Last week | The number of tickets solved over the previous week. Tickets are counted only if they are currently solved or closed. | (Tickets solved - Last week) |
| Tickets solved - This month | The number of tickets solved over the current month. Tickets are counted only if they are currently solved or closed. | (Tickets solved - This month) |
| Tickets solved - Last month | The number of tickets solved over the previous month. Tickets are counted only if they are currently solved or closed. | (Tickets solved - Last month) |
| Tickets solved - This year | The number of tickets solved this year. Tickets are counted only if they are currently solved or closed. | (Tickets solved - This year) |

### Tickets attributes

This section lists and defines all of the attributes available in the Tickets dataset.

Table 2. Tickets attributes

| Attribute | Definition |
| --- | --- |
| Ticket ID | The ID number of the ticket. |
| Ticket status | The status of the ticket. |
| Ticket custom status name | The name of a custom ticket status. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). For tickets that existed before custom ticket statuses were enabled, this attribute returns **NULL**. Data is available only from January 18, 2023 onward. |
| Ticket custom status category | The category that a custom ticket status is mapped to. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). For tickets that existed before custom ticket statuses were enabled, this attribute returns **Ticket Status**. Data is available only from January 18, 2023 onward. |
| Ticket custom status state | Returns **true** if a custom ticket status is active, or **false** if a custom ticket status is deactivated. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). Data is available only from January 18, 2023 onward. |
| Ticket group | Name of the group where the ticket was assigned. |
| Ticket brand | The brand of the ticket. |
| Ticket channel | The channel a ticket was created from. For more information about the ticket channels Explore collects, see [Understanding ticket channels in Explore](https://support.zendesk.com/hc/en-us/articles/4408836378394). |
| Ticket email address | The support email address currently set on the ticket. See [Adding support email addresses for users to submit tickets](https://support.zendesk.com/hc/en-us/articles/4408842868506). |
| Ticket external ID | The external ID of the ticket. |
| Ticket form | The current ticket form used on the ticket. |
| Ticket priority | The ticket's priority. |
| Ticket problem ID | The ID of the ticket defined as a problem ticket. |
| Ticket skills | The skill requirements for an agent to work on a ticket. |
| Ticket skill types | The grouping of skills into skill types. |
| Ticket subject | The subject of the ticket. |
| Ticket tags | The tags associated with the ticket. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket type | The ticket type: Question, Incident, Problem, or Task. |
| Sharing agreement inbound | Affiliated instances of Zendesk Support and companies who share tickets with current instance of Zendesk Support. |
| Sharing agreement outbound | Affiliated instances of Zendesk Support and companies tickets are shared with. |
| Assignee name | The name of the assignee. Values for this attribute (and for the other Assignee attributes below) include users who currently have an agent or admin role, as well as users who previously had an agent or admin role and were assigned to a ticket at least once. |
| Assignee role | The role of an assignee, either admin, agent, or end user. |
| Assignee ID | The ticket's assignee ID. |
| Assignee email | The ticket assignees email address. |
| Assignee external ID | The external ID of the ticket assignee. |
| Assignee locale | The locale of the assignee. |
| Assignee Guide admin | Returns whether the agent has Knowledge admin permissions (True or False). |
| Assignee skills | The skills associated with the ticket assignee. |
| Assignee skill types | The skill types associated with an assignee. |
| Assignee status | The current status of the ticket assignee. |
| Assignee tags | Tags added to the assignee. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Assignee time zone | Timezone of an assignee. |
| Requester name | The name of the user who is asking for support through a ticket. By default, the requester of a ticket is the submitter, but the requester can be changed. For example, if an agent opens a ticket on behalf of a customer, the customer would be the requester and the agent would be the submitter. |
| Requester role | The role of a requester, either admin, agent, or end user. |
| Requester ID | The ID number for a ticket's requester. |
| Requester email | The email address of the ticket requester. By default, this returns the primary email of the ticket requester. However, if a user has an unverified primary email addresses and a verified secondary email address, Explore uses the verified secondary email address. |
| Requester phone number | The primary phone number associated with the user’s profile. |
| Requester external ID | The external ID of the ticket requester. |
| Requester locale | The locale of the ticket requester. |
| Requester Guide admin | Designates whether the requester has Knowledge admin permissions. Returns either true or false. |
| Requester status | The Zendesk status of the ticket requester. |
| Requester tags | Tags associated with the requester. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Requester time zone | The requester's timezone. |
| Submitter name | The name of the user who actually created a ticket. By default, the submitter of a ticket is the requester, but the requester can be changed (the submitter cannot be). For example, if an agent opens a ticket on behalf of a customer, the agent would be the submitter and the customer would be the requester. |
| Submitter role | The role of the submitter, either admin, agent, or end user. |
| Submitter ID | The ID of the ticket submitter. |
| Submitter email | The email address of the ticket submitter. By default, this returns the primary email of the ticket submitter. However, if a user has an unverified primary email addresses and a verified secondary email address, Explore uses the verified secondary email address. |
| Submitter external ID | The external ID of the ticket submitter. |
| Submitter locale | The locale of the ticket submitter. |
| Submitter Guide admin | Returns whether the ticket submitter has Knowledge admin permissions, either true or false. |
| Submitter status | The status of the ticket submitter. |
| Submitter tags | Tags added to the ticket submitter. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Submitter time zone | The ticket submitter timezone. |
| Ticket organization name | The name of the organization associated with the ticket. |
| Ticket organization ID | The ID of the organization associated with the ticket. |
| Ticket organization domains | The domains of the organization associated with the ticket. |
| Ticket organization external ID | The external ID of the organization associated with the ticket. |
| Ticket organization status | The status of the organization associated with the ticket. |
| Ticket organization tags | The tags of the organization associated with the ticket. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Requester organization name | The current [default organization](https://support.zendesk.com/hc/en-us/articles/4408838309530-Managing-users-in-multiple-organizations-Professional-and-Enterprise-#topic_cjl_trp_dp) name of the ticket requester. |
| Requester organization ID | The current [default organization](https://support.zendesk.com/hc/en-us/articles/4408838309530-Managing-users-in-multiple-organizations-Professional-and-Enterprise-#topic_cjl_trp_dp) ID of the ticket requester. |
| Requester organization domains | The domain name of the current [default organization](https://support.zendesk.com/hc/en-us/articles/4408838309530-Managing-users-in-multiple-organizations-Professional-and-Enterprise-#topic_cjl_trp_dp) of the ticket requester, for example, zendesk.com. |
| Requester organization external ID | The external ID of the ticket requester's current [default organization](https://support.zendesk.com/hc/en-us/articles/4408838309530-Managing-users-in-multiple-organizations-Professional-and-Enterprise-#topic_cjl_trp_dp). |
| Requester organization status | The system status of the current [default organization](https://support.zendesk.com/hc/en-us/articles/4408838309530-Managing-users-in-multiple-organizations-Professional-and-Enterprise-#topic_cjl_trp_dp) of the ticket requester, either active or deleted. |
| Requester organization tags | The tags associated with the current [default organization](https://support.zendesk.com/hc/en-us/articles/4408838309530-Managing-users-in-multiple-organizations-Professional-and-Enterprise-#topic_cjl_trp_dp) of the ticket requester. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket satisfaction rating | The satisfaction rating left by the customer on the ticket. Values: Good, Bad, Offered, Unoffered. |
| Ticket satisfaction comment | The comment left by the customer along with the satisfaction rating. |
| Ticket satisfaction reason | The reason selected by the customer along with the satisfaction rating. |
| Agent replies brackets | The number of agent replies left on the ticket. Values are returned as **0**, **1**, **2**, or **3-5** or **>5**. |
| Assignee stations brackets | The number of agents to whom the ticket was assigned. Values are returned as **0**, **1**, **2**, or **>2**. |
| Group stations brackets | The number of groups that the ticket was involved with, for example, the assignee group of all ticket assignees. Values are returned as **1**, **2**, **3**, **>3**. |
| Reopens brackets | The number of times the ticket was reopened. Values are returned as **1**, **2**, **3**, **>3**. |
| First reply time brackets | The time between when the ticket was first opened, and when an agent first replied. Values are returned as **No replies**, **0-1 hrs**, **1-8 hrs**, **8-24 hrs**, or **>24 hrs**. |
| First resolution time brackets | The time between when the ticket was first opened, and the first time it was set to solved. Values are returned as **0-5 hrs**, **5-24 hrs**, **1-7 days**, **7-30 days**, **>30 days**, or **Unsolved**. |
| Full resolution time brackets | The time between when the ticket was first opened, and the last time it was set to solved. Values are returned as **0-5 hrs**, **5-24 hrs**, **1-7 days**, **7-30 days**, **>30 days**, or **Unsolved**. |
| Requester wait time brackets | The time a requester was waiting for agent replies. The values are returned as **0-1 hrs**, **1-24 hrs**, **1-3 days**, **3-7 days**, **>7 days** or **No wait**. |
| Unsolved tickets age brackets | The duration in days between when an unsolved ticket was created and now. The values are returned as **1 day**, **1-7 days**, **7-30 days**, **>30 days**, or **Solved**. |
| Intent (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what the ticket is about. To see the possible values, [open the Taxonomy tab of the Intent settings page](https://support.zendesk.com/hc/en-us/articles/9488234915610) to see the AI Intents list under the **Taxonomy values** heading. |
| Intent confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the intent prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Language (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what language the ticket is written in. To see the possible values, open the Taxonomy tab of the settings page. |
| Language confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the language prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Sentiment (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of how the customer feels about their request. Possible values are **Very Positive**, **Positive**, **Neutral**, **Negative**, and **Very Negative**. |
| Sentiment confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the sentiment prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Ticket created | Includes a number of attributes that return the time and date when the ticket was created in various time measurements. |
| Ticket solved | Includes a number of attributes that return the time and date when the ticket was most recently solved in various time measurements. |
| Ticket updated | The time when the ticket was last updated. |
| Ticket requester updated | The time when the ticket was last updated by its requester. |
| Ticket assigned | The time when the ticket was last assigned to an agent. |
| Ticket first assigned | The time when the ticket was first assigned to an agent. |
| Ticket due | When a ticket is configured as a task, this is the date at which the task must be completed. |
| Requester created | The time when the ticket requester user profile was created. |
| Requester updated | The last time that the ticket requester user profile was updated. |
| Requester sign-in | The time when the ticket requester last signed in. |
| Assignee sign-in | The time when the ticket assignee last signed in. |
| Organization created | The time when the ticket requester organization was created. |
| Organization updated | The time when the ticket requester organization was last updated. |

## Updates history dataset

The Updates history dataset contains metrics and attributes that relate to updates and changes in tickets. This section list all available elements for the dataset.

This section contains the following topics:

- [Updates history dataset schema](#topic_pct_fyf_kkb)
- [Updates history metrics](#topic_krx_1lq_4y)
- [Updates history attributes](#topic_zdl_flq_4y)

### Updates history dataset schema

Use this diagram to help you understand the elements of the Updates history dataset and their relationships.

![Updates history dataset schema](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Ticket%20updates.jpg)

### Updates history metrics

This section lists and defines all metrics available in the Updates history dataset.

Table 3. Updates history metrics

| Metric | Definition | Explore formula |
| --- | --- | --- |
| Updates | The total number of updates made to the ticket. | [Update ID] |
| Agent updates | The number of updates agents made to tickets meaning the changes they made to any ticket field. | IF ([Updater role] != "End-user") THEN [Update ID] ENDIF |
| End-user updates | The number of updates end-users made to tickets. | IF ([Updater role] = "End-user") THEN [Update ID] ENDIF |
| Comments | The total number of comments on tickets. | IF ([Comment present] = TRUE) THEN [Update ID] ENDIF |
| Public comments | The number of public comments on tickets. | IF ([Comment present] = TRUE AND [Comment public] = TRUE) THEN [Update ID] ENDIF |
| Internal comments | The number of internal comments on tickets. | IF ([Comment present] = TRUE AND [Comment public] = FALSE) THEN [Update ID] ENDIF |
| Agent comments | The number of agent comments on tickets. | IF ([Comment present] = TRUE AND [Updater role] != "End-user") THEN [Update ID] ENDIF |
| End-user comments | The number of end-user comments on tickets. | IF ([Comment present] = TRUE AND [Updater role] = "End-user") THEN [Update ID] ENDIF |
| Tickets created | The number of tickets that have been created. | IF ([Changes - Field name]="status" AND [Changes - Previous value]=NULL) THEN [Update ID] ENDIF |
| Tickets solved | The number of solved tickets. Tickets are counted only if they are currently solved or closed. | IF ([Changes - Field name]="status" AND [Changes - Previous value]!="solved" AND ([Changes - New value]="solved" OR [Changes - New value]="closed") AND ([Ticket status - Unsorted] = "Solved" OR [Ticket status - Unsorted] = "Closed") AND [Update - Timestamp]=[Ticket solved - Timestamp]) THEN [Update ID] ENDIF |
| Tickets updated | The number of updated tickets. | [Update ticket ID] |
| Tickets updated w/comment | The total number of tickets that were updated with a comment. | IF ([Comment present] = TRUE) THEN [Update ticket ID] ENDIF |
| Tickets updated w/public comment | The total number of tickets that were updated with a public comment. | IF ([Comment present] = TRUE AND [Comment public] = TRUE) THEN [Update ticket ID] ENDIF |
| Tickets updated w/internal comment | The total number of tickets that were updated with an internal comment. | IF ([Comment present] = TRUE AND [Comment public] = FALSE) THEN [Update ticket ID] ENDIF |
| Tickets assigned | The number of tickets that have been assigned to agents. | IF ([Changes - Field name]="assignee\_id" AND [Changes - New value]!="0") THEN [Update ticket ID] ENDIF |
| Tickets reopened | The number of tickets that have been solved at least once, then reopened. Includes tickets solved and reopened during the same update. | IF ([Changes - Field name] = "status" AND [Changes - Previous value] ="solved" AND [Changes - New value] !="solved" AND [Changes - New value] !="closed" ) THEN [Update ticket ID] ENDIF |
| Assignee reassignments | The number of times tickets were reassigned to another agent. | IF ([Changes - Field name] = "assignee\_id" AND [Changes - Previous value]!=NULL AND [Changes - New value]!="0") THEN [Update ID] ENDIF |
| Group reassignments | The number of tickets that were reassigned to another group. | IF ([Changes - Field name] = "group\_id" AND [Changes - Previous value]!=NULL AND [Changes - New value]!="0") THEN [Update ID] ENDIF |
| Resolutions | The number of times tickets were set to Solved. | IF ([Changes - Field name]="status" AND [Changes - Previous value]!="solved" AND ([Changes - New value]="solved" OR [Changes - New value]="closed")) THEN [Update ID] ENDIF |
| Reopens | The number of times tickets were reopened. | IF ([Changes - Field name] = "status" AND [Changes - Previous value] ="solved" AND [Changes - New value] !="solved" AND [Changes - New value] !="closed" ) THEN [Update ID] ENDIF |
| Deletions | The number of tickets that were deleted. | IF ([Changes - Field name]="status" AND [Changes - New value]="deleted") THEN [Update ID] ENDIF |
| Recoveries | The number of deleted tickets that were recovered. | IF ([Changes - Field name]="status" AND [Changes - Previous value]="deleted") THEN [Update ID] ENDIF |
| Satisfaction updates | The number of satisfaction updates submitted by the requester. | IF ([Changes - Field name]="satisfaction\_score" THEN [Update ID] ENDIF |
| Good initial satisfaction ratings | The number of tickets with a good initial satisfaction rating. | IF ([Changes - Field name]="satisfaction\_score" AND ([Changes - Previous value]="offered" OR [Changes - Previous value]= NULL) AND [Changes - New value]="good") THEN [Update ID] ENDIF |
| Bad initial satisfaction ratings | The number of tickets with a bad initial satisfaction rating. | IF ([Changes - Field name]="satisfaction\_score" AND ([Changes - Previous value]="offered" OR [Changes - Previous value]= NULL) AND [Changes - New value]="bad") THEN [Update ID] ENDIF |
| Bad to good satisfaction ratings | The number of tickets with a bad initial satisfaction rating that later changed to a good rating. | IF ([Changes - Field name]="satisfaction\_score" AND [Changes - Previous value]= "bad" AND [Changes - New value]="good") THEN [Update ID] ENDIF |
| Good to bad satisfaction ratings | The number of tickets with a good initial satisfaction rating that later changed to a bad rating. | IF ([Changes - Field name]="satisfaction\_score" AND [Changes - Previous value]= "good" AND [Changes - New value]="bad") THEN [Update ID] ENDIF |
| Field changes time (min) | The time in minutes between changes to the ticket fields. | (Field changes time (min)) |
| New status time (min) | The time in minutes that tickets spent with a status of New. | IF ([Changes - Field name] = "status" AND [Changes - Previous value]= "new") THEN VALUE(Field changes time (min)) ENDIF |
| Open status time (min) | The time in minutes that tickets were in the Open status. | IF ([Changes - Field name] = "status" AND [Changes - Previous value]= "open") THEN VALUE(Field changes time (min)) ENDIF |
| Pending status time (min) | The time in minutes that tickets were in the Pending status. | IF ([Changes - Field name] = "status" AND [Changes - Previous value]= "pending") THEN VALUE(Field changes Time (min)) ENDIF |
| On-hold status time (min) | The time in minutes that tickets were in the On-hold status. | IF ([Changes - Field name] = "status" AND [Changes - Previous value]= "hold") THEN VALUE(Field changes time (min)) ENDIF |
| Unassigned time (min) | The time in minutes that a ticket was not assigned to any agents. | IF ([Changes - Field name] = "assignee\_id" AND ([Changes - Previous value] = NULL OR [Changes - Previous value] = "0")) THEN IF (VALUE(Field changes time (min)) = NULL) THEN DATE\_DIFF([Update - Timestamp], [Ticket created - Timestamp], "nb\_of\_minutes") ELSE VALUE(Field changes time (min)) ENDIF ENDIF |
| Previously assigned time (min) | The time in minutes that a ticket was assigned to agents before the current assigned agent. | IF ([Changes - Field name] = "assignee\_id" AND [Changes - Previous value] != NULL AND [Changes - Previous value] != "0") THEN VALUE(Field changes time (min)) ENDIF |
| Field changes time (hrs) | The time in hours between changes to the ticket fields. | VALUE(Field changes time (min))/60 |
| New status time (hrs) | The time in hours that tickets spent with a status of New. | IF ([Changes - Field name] = "status" AND [Changes - Previous value]= "new") THEN VALUE(Field changes time (min))/60 ENDIF |
| Open status time (hrs) | The time in hours that tickets were in the Open status. | IF ([Changes - Field name] = "status" AND [Changes - Previous value]= "open") THEN VALUE(Field changes time (min))/60 ENDIF |
| Pending status time (hrs) | The time in hours that tickets were in the Pending status. | IF ([Changes - Field name] = "status" AND [Changes - Previous value]= "pending") THEN VALUE(Field changes time (min))/60 ENDIF |
| On-hold status time (hrs) | The time in hours that tickets were in the On-hold status. | IF ([Changes - Field name] = "status" AND [Changes - Previous value]= "hold") THEN VALUE(Field changes time (min))/60 ENDIF |
| Unassigned time (hrs) | The time in hours that a ticket was not assigned to any agents. | IF ([Changes - Field name] = "assignee\_id" AND ([Changes - Previous value] = NULL OR [Changes - Previous value] = "0")) THEN IF (VALUE(Field changes time (min)) = NULL) THEN DATE\_DIFF([Update - Timestamp], [Ticket created - Timestamp], "nb\_of\_hours") ELSE VALUE(Field changes time (min)) / 60 ENDIF ENDIF |
| Previously assigned time (hrs) | The time in hours that a ticket was assigned to agents before the current assigned agent. | IF ([Changes - Field name] = "assignee\_id" AND [Changes - Previous value] != NULL AND [Changes - Previous value] != "0") THEN VALUE(Field changes time (min))/60 ENDIF |
| Field changes time (days) | The time in days between changes to the ticket fields. | VALUE(Field changes time (min))/60/24 |
| New status time (days) | The time in days that tickets spent with a status of New. | IF ([Changes - Field name] = "status" AND [Changes - Previous value]= "new") THEN VALUE(Field changes time (min))/60/24 ENDIF |
| Open status time (days) | The time in days that tickets were in the Open status. | IF ([Changes - Field name] = "status" AND [Changes - Previous value]= "open") THEN VALUE(Field changes time (min))/60/24 ENDIF |
| Pending status time (days) | The time in days that tickets were in the Pending status. | IF ([Changes - Field name] = "status" AND [Changes - Previous value]= "pending") THEN VALUE(Field changes time (min))/60/24 ENDIF |
| On-hold status time (days) | The time in days that tickets were in the On-hold status. | IF ([Changes - Field name] = "status" AND [Changes - Previous value]= "hold") THEN VALUE(Field changes time (min))/60/24ENDIF |
| Unassigned time (days) | The time in days that a ticket was not assigned to any agents. | IF ([Changes - Field name] = "assignee\_id" AND ([Changes - Previous value] = NULL OR [Changes - Previous value] = "0")) THEN IF (VALUE(Field changes time (min)) = NULL) THEN DATE\_DIFF([Update - Timestamp], [Ticket created - Timestamp], "nb\_of\_days") ELSE VALUE(Field changes time (min)) / 60 / 24 ENDIF ENDIF |
| Previously assigned time (days) | The time in days that a ticket was assigned to agents before the current assigned agent. | IF ([Changes - Field name] = "assignee\_id" AND [Changes - Previous value] != NULL AND [Changes - Previous Value] != "0") THEN VALUE(Field changes time (min))/60/24 ENDIF |

### Updates history attributes

This section lists and defines all attributes available in the Updates history dataset.

Table 4. Updates history metrics

| Attribute | Definition |
| --- | --- |
| Update ID | The unique ID of an update |
| Update channel | The channel that initiated a ticket update. Note that there is not a unique channel value for the bot. This may skew results in reports based on the update channel for bot workflows. For more information about the ticket channels Explore collects, see [Understanding ticket channels in Explore](https://support.zendesk.com/hc/en-us/articles/4408836378394). |
| Update country | The country from which a ticket update was initiated. |
| Update country and region | The country and region from which a ticket update was initiated. |
| Update latitude | The latitude from which the ticket update was initiated. |
| Update longitude | The longitude from which a ticket updated was initiated. |
| Comment present | Indicates where there is currently a comment on the ticket. |
| Comment type | The type of comment, internal or public. |
| Comment public | Returns true or false based on whether public comments are present on the ticket. |
| Update ticket ID | The unique ID of a ticket update. Includes deleted tickets. See [What's the difference between Update ticket ID and Ticket ID?](https://support.zendesk.com/hc/en-us/articles/5493627275546) |
| Update ticket status | The status of a ticket after an update. |
| Update ticket group | The group to which a ticket was assigned at the end of an update. For example, if a ticket was reassigned from Tier 1 to Tier 2, the attribute returns Tier 2. |
| Update ticket assignee | The ticket assignee after an update. |
| Update ticket brand | The brand of the ticket after an update. |
| Update ticket priority | The priority of the ticket after an update. |
| Update ticket type | The type of the ticket after an update. |
| Changes - Field name | Records the field name that was updated. |
| Changes - Field type | Records the field type that was updated. |
| Changes - Previous value | Records the value of the field before the update. See [How do I find the right value to use with the "Changes - Previous/New value" attribute?](https://support.zendesk.com/hc/en-us/articles/4991340434586) |
| Changes - New value | Records the new value of the field after the update. See [How do I find the right value to use with the "Changes - Previous/New value" attribute?](https://support.zendesk.com/hc/en-us/articles/4991340434586) |
| Ticket ID | The ticket's unique ID. Does not include deleted tickets. See [What's the difference between Update ticket ID and Ticket ID?](https://support.zendesk.com/hc/en-us/articles/5493627275546) |
| Ticket status | The status of the ticket. |
| Ticket custom status name | The name of a custom ticket status. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). For tickets that existed before custom ticket statuses were enabled, this attribute returns **NULL**. Data is available only from October 19, 2023 onward. |
| Ticket custom status category | The category that a custom ticket status is mapped to. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). For tickets that existed before custom ticket statuses were enabled, this attribute returns **Ticket Status**. Data is available only from October 19, 2023 onward. |
| Ticket custom status state | Returns **true** if a custom ticket status is active, or **false** if a custom ticket status is deactivated. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). Data is available only from October 19, 2023 onward. |
| Ticket group | Name of the group where the ticket is assigned. |
| Ticket brand | The brand associated with the ticket. |
| Ticket channel | The channel that initiated creation of the ticket. For more information about the ticket channels Explore collects, see [Understanding ticket channels in Explore](https://support.zendesk.com/hc/en-us/articles/4408836378394). |
| Ticket external ID | The external system ID of the ticket. |
| Ticket form | The current ticket form used on the ticket. |
| Ticket priority | The priority of the ticket. |
| Ticket problem ID | The IDs of the ticket defined as a problem ticket. |
| Ticket subject | The subject of the ticket. |
| Ticket tags | Any tags associated with the ticket. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket type | The type of ticket. |
| Sharing agreement inbound | Affiliated instances of Zendesk Support and companies who share tickets with current instance of Zendesk Support. |
| Sharing agreement outbound | Affiliated instances of Zendesk Support and companies tickets are shared with. |
| Updater name | The name of the updater. This value is the string associated with the user at the time of the update. If a user's name changes, a new username is created in Explore and is not linked to the original name. For example, if the username "John Smith" was updated to "John K Smith", both values exist independently and are not linked. |
| Updater agent name | Displays the name of the updater if an agent. This attribute provides the fastest way to display agent names in the report. |
| Updater role | The role of the updater. |
| Updater ID | The ID of the users whom made the update. |
| Updater email | The email address of the ticket updater. |
| Updater external ID | The external ID of the ticket updater. |
| Updater Guide admin | Indicates whether the user who updated the ticket is a Guide admin. |
| Updater locale | The locale of the updater. |
| Updater status | The status of the user who updated the ticket. Can be Active, Suspended, or Deleted. |
| Updater tags | The tags associated with the user who updated the ticket. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Updater time zone | The timezone of the updater. |
| Assignee name | The name of the user the ticket is assigned to. Values for this attribute (and for the other Assignee attributes below) include users who currently have an agent or admin role, as well as users who previously had an agent or admin role and were assigned to a ticket at least once. |
| Assignee role | The role of the user the ticket is assigned to. |
| Assignee ID | The ID of the user the ticket is assigned to. |
| Assignee email | The email address of the user the ticket is assigned to. |
| Assignee status | The status of the user the ticket is assigned to. Can be Active, Suspended, or Deleted. |
| Assignee tags | The tags that are associated with the user the ticket is assigned to. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Requester name | The name of the user who is asking for support through a ticket. By default, the requester of a ticket is the submitter, but the requester can be changed. For example, if an agent opens a ticket on behalf of a customer, the customer would be the requester and the agent would be the submitter. |
| Requester role | The requester's role. |
| Requester ID | The requester's ID. |
| Requester email | The requester's email address. By default, this returns the primary email of the ticket requester. However, if a user has an unverified primary email addresses and a verified secondary email address, Explore uses the verified secondary email address. |
| Requester status | The status of the requester's profile. Can be Active, Suspended, or Deleted. |
| Requester tags | Any tags associated with the requester. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Submitter name | The name of the user who actually created a ticket. By default, the submitter of a ticket is the requester, but the requester can be changed (the submitter cannot be). For example, if an agent opens a ticket on behalf of a customer, the agent would be the submitter and the customer would be the requester. |
| Submitter role | The role of the user who submitted the ticket. |
| Submitter ID | The ID of the user who submitted the ticket. |
| Submitter email | The email address of the user who submitted the ticket. By default, this returns the primary email of the ticket submitter. However, if a user has an unverified primary email addresses and a verified secondary email address, Explore uses the verified secondary email address. |
| Submitter status | The status of the user who submitted the ticket. Can be Active, Suspended, or Deleted. |
| Submitter tags | The tags associated with the user who submitted the ticket. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Updater organization name | The organization name of the user who made the ticket update. |
| Updater organization ID | The organization ID of the user who made the ticket update. |
| Updater organization domains | The web domain of the updater's (person who made the ticket update) organization. Examples: google.com, company.com, wiki.com. |
| Updater organization status | The organization status of the user who made the ticket update. |
| Updater organization tags | The organization tags of the person who made the ticket update. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket organization name | The name of the organization associated with the ticket. |
| Ticket organization ID | The ID of the organization associated with the ticket. |
| Ticket organization status | The status of the organization associated with the ticket; either Active or Deleted. |
| Ticket organization tags | The tags associated with the ticket organization. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Requester organization name | The current [default organization](https://support.zendesk.com/hc/en-us/articles/4408838309530-Managing-users-in-multiple-organizations-Professional-and-Enterprise-#topic_cjl_trp_dp) associated with the user set as requester in the ticket. |
| Requester organization ID | The current [default organization](https://support.zendesk.com/hc/en-us/articles/4408838309530-Managing-users-in-multiple-organizations-Professional-and-Enterprise-#topic_cjl_trp_dp) ID associated with the user set as requester in the ticket. |
| Requester organization status | The current [default organization](https://support.zendesk.com/hc/en-us/articles/4408838309530-Managing-users-in-multiple-organizations-Professional-and-Enterprise-#topic_cjl_trp_dp) status associated with the user set as requester in the ticket. |
| Requester organization tags | The tags of the current [default organization](https://support.zendesk.com/hc/en-us/articles/4408838309530-Managing-users-in-multiple-organizations-Professional-and-Enterprise-#topic_cjl_trp_dp) associated with the user set as requester in the ticket. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket satisfaction rating | The satisfaction rating left by the customer in the ticket; either Good, Bad, Offered, or Unoffered. |
| Ticket satisfaction comment | The comment left by the customer with the satisfaction rating. |
| Ticket satisfaction reason | The reason selected by the customer along with the satisfaction rating. |
| Intent (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what the ticket is about. To see the possible values, [open the Taxonomy tab of the Intent settings page](https://support.zendesk.com/hc/en-us/articles/9488234915610) to see the AI Intents list under the **Taxonomy values** heading. |
| Intent confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the intent prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Language (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what language the ticket is written in. To see the possible values, open the Taxonomy tab of the settings page. |
| Language confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the language prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Sentiment (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of how the customer feels about their request. Possible values are **Very Positive**, **Positive**, **Neutral**, **Negative**, and **Very Negative**. |
| Sentiment confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the sentiment prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Time - Ticket update | A collection of attributes that return the time of each update (such as a comment) in various time measurements. When [added as a time filter](../creating-dashboards/best-practices-for-using-dashboard-filters.md#h_a2bcbc01-a036-416b-8108-3b66318bcd83) within a dashboard, this attribute is called Update. |
| Time - Ticket created | A collection of attributes that return the time a ticket was created in various time measurements. |
| Time - Ticket solved | A collection of attributes that return the time a ticket was most recently solved in various time measurements. |
| Time - Ticket last updated | A collection of attributes that return the time a ticket was last updated in various time measurements (for example when an agent saves the ticket). When [added as a time filter](../creating-dashboards/best-practices-for-using-dashboard-filters.md#h_a2bcbc01-a036-416b-8108-3b66318bcd83) within a dashboard, this attribute is called Ticket updated. |
| Time - Ticket requester updated | The time when the ticket was last updated by its requester. |
| Time - Ticket last assigned | A collection of attributes that return the time a ticket was last assigned in various time measurements. When [added as a time filter](../creating-dashboards/best-practices-for-using-dashboard-filters.md#h_a2bcbc01-a036-416b-8108-3b66318bcd83) within a dashboard, this attribute is called Ticket assigned. |
| Time - Ticket first assigned | A collection of attributes that return the time a ticket was first assigned in various time measurements. |
| Time - Ticket type - Task due | A collection of attributes that return the time a ticket that has been configured as a task is due in various time measurements. When [added as a time filter](../creating-dashboards/best-practices-for-using-dashboard-filters.md#h_a2bcbc01-a036-416b-8108-3b66318bcd83) within a dashboard, this attribute is called Ticket due. |
| Time - Updater last sign-in | A collection of attributes that return the last time a ticket updater logged in, in various time measurements. When [added as a time filter](../creating-dashboards/best-practices-for-using-dashboard-filters.md#h_a2bcbc01-a036-416b-8108-3b66318bcd83) within a dashboard, this attribute is called Updater login. |

## Backlog history dataset

The Backlog history dataset contains metrics and attributes related to your backlog history. The dataset will show you a snapshot of unsolved tickets at any given date.
Explore collects backlog information every time your [data synchronizes](https://support.zendesk.com/hc/en-us/articles/4408820703386-How-frequently-does-my-Zendesk-data-sync-to-Explore-) with Explore.

This section contains the following topics:

- [Backlog history dataset schema](#topic_et2_myf_kkb)
- [Backlog history metrics](#topic_elz_t2g_ndb)
- [Backlog history attributes](#topic_lvl_52g_ndb)

### Backlog history dataset schema

Use this diagram to help you understand the elements of the Backlog history dataset and their relationships.

![Backlog history dataset schema](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Backlog%20history.png)

### Backlog history metrics

This section lists and defines all metrics available in the Backlog history dataset.

Table 5. Backlog history metrics

| Metric | Definition | Explore formula |
| --- | --- | --- |
| Tickets | Counts the number of backlog tickets. | VALUE (Tickets) |
| Unassigned tickets | Counts the number of backlog tickets where the assignee value was empty. | IF ([Assignee]=NULL) THEN VALUE (Tickets) ELSE 0 ENDIF |
| Assigned tickets | Counts the number of backlog tickets where the assignee value was not empty. | IF ([Assignee]!=NULL) THEN VALUE (Tickets) ELSE 0 ENDIF |
| Incidents | Counts the number of backlog tickets where the ticket type was Incident. | IF ([Type - Unsorted]="Incident") THEN VALUE (Tickets) ELSE 0 ENDIF |
| Problems | Counts the number of backlog tickets where the ticket type was Problem. | IF ([Type - Unsorted]="Problem") THEN VALUE (Tickets) ELSE 0 ENDIF |
| Tickets - Daily average | The daily average of the backlog tickets. | SUM(Tickets)/DCOUNT([Backlog recorded - Data]) |

### Backlog history attributes

This section lists and defines all attributes available in the Backlog history dataset. Explore collects backlog information every time your data synchronizes with Explore.

Table 6. Backlog history attributes

| Attribute | Definition |
| --- | --- |
| Status - unsorted | The status of the backlog ticket. |
| Group | The group for the backlog ticket. |
| Assignee | The assignee of the backlog ticket. Values include users who currently have an agent or admin role, as well as users who previously had an agent or admin role and were assigned to a ticket at least once. |
| Brand | The brand of the backlog ticket. |
| Channel | The channel the backlog ticket was most recently updated by. For more information about the ticket channels Explore collects, see [Understanding ticket channels in Explore](https://support.zendesk.com/hc/en-us/articles/4408836378394). |
| Priority | The priority of the backlog ticket. |
| Type | The type of the backlog ticket. |
| Time - Backlog recorded | The date the backlog snapshot was taken. Includes year, half-year, quarter, month and week. For an example of how to use this, see [What is the difference between Backlog recorded and Backlog end of period?](https://support.zendesk.com/hc/en-us/articles/4412965304858) |
| Time - Backlog end of period | The last day of the backlog snapshot period. Includes year, quarter, month, and week. For an example of how to use this, see [What is the difference between Backlog recorded and Backlog end of period?](https://support.zendesk.com/hc/en-us/articles/4412965304858) |

## SLAs dataset

The SLAs dataset contains metrics and attributes that relate to your [SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866-Defining-and-using-SLA-policies-Professional-and-Enterprise-). This section list all the available elements for the Zendesk SLA dataset. If you have active SLA policies, the SLA reporting dashboard enables you to easily view how well you are meeting these policies.

- [SLAs dataset schema](#topic_lq4_tyf_kkb)
- [SLAs metrics](#topic_wcv_4s4_l2b)
- [SLAs attributes](#topic_oyw_ps4_l2b)

Note: This dataset appears only if you have tickets with SLA policies applied and includes SLA data from deleted tickets. See [Defining and using SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866).

### SLAs dataset schema

Use this diagram to help you understand the elements of the SLAs dataset and their relationships.

![SLAs dataset schema](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/SLAs.jpg)

### SLAs metrics

This section lists and defines all metrics available in the SLAs dataset.

Table 7. SLAs metrics

| Metric | Definition | Explore formula |
| --- | --- | --- |
| SLA tickets | The number of tickets that have SLA targets applied. | [Ticket ID] |
| Achieved SLA tickets | The number of tickets that met all applied SLA policy targets. | D\_COUNT(SLA tickets)-D\_COUNT(Breached or active SLA tickets) |
| Breached SLA tickets | The number of tickets that have breached at least one SLA policy target. | IF ( [SLA target status]="Breached") THEN [Ticket ID] ENDIF |
| Active SLA tickets | The number of SLA tickets whose metrics have not been completed yet. | IF ([SLA metric status]= "Active") THEN [Ticket ID] ENDIF |
| Breached active SLA tickets | The number of SLA tickets whose metrics have not yet been completed, but at least one SLA policy target has been breached. | IF ([SLA metric status]= "Active" AND [SLA target status]= "Breached") THEN [Ticket ID] ENDIF |
| Breached or active SLA tickets | The number of SLA tickets whose metrics have not yet been completed or at least one SLA policy target has been breached. | IF ([SLA metric status]= "Active" OR [SLA target status]= "Breached") THEN [SLA policy ticket ID] ENDIF |
| Unbreached active SLA tickets | The number of SLA tickets whose metrics have not been completed yet and no SLA policy targets have been breached, yet. | D\_COUNT(Active SLA tickets)-D\_COUNT(Breached active SLA tickets) |
| % Achieved SLA tickets | The number of tickets that met all applied SLA policy targets expressed as a percentage of all SLA tickets. | SUM(Achieved SLA tickets)/(SUM(Achieved SLA tickets)+D\_COUNT(Breached SLA tickets)) |
| % Breached SLA tickets | The number of tickets that have breached at least one SLA policy target expressed as a percentage of all SLA tickets. | D\_COUNT(Breached SLA tickets)/(SUM(Achieved SLA tickets)+D\_COUNT(Breached SLA tickets)) |
| SLA policies | The number of SLA policies. | IF ( [SLA policy ID]!=NULL AND LENGTH(STRING([SLA policy ID]))>0) THEN COUNT\_VALUES([SLA policy unique ID]) ENDIF |
| Achieved SLA policies | The number of SLA policies that have been achieved. | COUNT(SLA policies)-COUNT(Breached or active SLA policies) |
| Breached SLA policies | The number of SLA policies that have been breached. | IF ( [SLA target status]="Breached" AND [SLA policy ID]!=NULL AND LENGTH(STRING([SLA policy ID]))>0) THEN COUNT\_VALUES([SLA policy unique ID]) ENDIF |
| Active SLA policies | The number of SLA policies whose metrics have not been completed yet. | IF ( [SLA metric status]= "Active" AND [SLA policy ID]!=NULL AND LENGTH(STRING([SLA policy ID]))>0) THEN COUNT\_VALUES([SLA policy unique ID]) ENDIF |
| Breached active SLA policies | The number of SLA policies whose metrics have not yet been completed, but at least one SLA policy target has been breached. | IF ( [SLA metric status]= "Active" AND [SLA target status]= "Breached" AND [SLA policy ID]!=NULL AND LENGTH(STRING([SLA policy ID]))>0) THEN COUNT\_VALUES([SLA policy unique ID]) ENDIF |
| Breached or active SLA policies | The number of SLA policies whose metrics have not yet been completed, or at least one SLA policy target has been breached. | IF ([SLA metric status]= "Active" OR [SLA target status]= "Breached" AND [SLA policy ID]!=NULL AND LENGTH(STRING([SLA policy ID]))>0) THEN COUNT\_VALUES([SLA policy unique ID]) ENDIF |
| Unbreached active SLA policies | The number of SLA policies whose metrics have not been completed and no policy targets have been breached. | COUNT(Active SLA policies)-COUNT(Breached active SLA policies) |
| SLA targets | The number of SLA targets. | [SLA event ID] |
| Achieved SLA targets | The number of SLA targets that were achieved. | IF ([SLA target status]= "Achieved" ) THEN [SLA event ID] ENDIF |
| Breached SLA targets | The number of SLA targets that were breached. | IF ([SLA target status]= "Breached") THEN [SLA event ID] ENDIF |
| Active SLA targets | The number of active SLA targets. An active SLA target is one whose metric has not been completed yet. | IF ([SLA metric status]= "Active") THEN [SLA event ID] ENDIF |
| Breached active SLA targets | The number of active SLA targets that have been breached. | IF ([SLA metric status]= "Active" AND [SLA target status]="Breached") THEN [SLA event ID] ENDIF |
| Unbreached active SLA targets | The number of active SLA targets that have not been breached. | IF ([SLA metric status]= "Active" AND [SLA target status]=NULL) THEN [SLA event ID] ENDIF |
| % Achieved SLA targets | The percentage of SLA targets that were achieved out of the total number of targets that were achieved and breached. | COUNT(Achieved SLA targets)/(COUNT(Achieved SLA targets)+COUNT(Breached SLA targets)) |
| % Breached SLA targets | The percentage of SLA targets that were breached out of the total number of targets that were achieved and breached. | COUNT(Breached SLA targets)/(COUNT(Achieved SLA targets)+COUNT(Breached SLA targets)) |
| Achieved SLA targets - Daily average | The daily average of the achieved SLA targets. | COUNT(Achieved SLA targets)/DCOUNT\_Values([SLA update - Date]) |
| Breached SLA targets - Daily average | The daily average of the breached SLA targets. | COUNT(Breached SLA targets)/DCOUNT\_Values([SLA update - Date]) |
| SLA metric breach time (min) | The time duration between the target time and actual SLA fulfillment (in minutes) for the SLA metric has been breached. | IF ([SLA target status]= "Breached") THEN VALUE(SLA metric completion time (min))- VALUE(SLA metric target time (min)) ENDIF |
| SLA metric target time (min) | The SLA target time (in minutes) for the SLA metric. | (SLA metric target time (min)) |
| SLA metric completion time (min) | The amount of time (in minutes) the SLA metric was active. | (SLA metric completion time (min)) |
| SLA metric breach time (hrs) | The time duration between the target time and actual SLA fulfillment (in hours) for the SLA metric has been breached. | IF ([SLA target status]= "Breached") THEN (VALUE(SLA metric completion time (min))- VALUE(SLA metric target time (min)))/60 ENDIF |
| SLA metric target time (hrs) | The SLA target time (in hours). | VALUE(SLA metric target time (min))/60 |
| SLA metric completion time (hrs) | The amount of time (in hours) the SLA metric was active. | VALUE(SLA metric completion time (min))/60 |
| SLA metric breach time (days) | The time duration between the target time and actual SLA fulfillment (in days) for the SLA metric has been breached. | IF ([SLA target status]= "Breached") THEN (VALUE(SLA metric completion time (min))- VALUE(SLA metric target time (min)))/60/24 ENDIF |
| SLA metric target time (days) | The SLA target time (in days). | VALUE(SLA metric target time (min))/60/24 |
| SLA metric completion time (days) | The amount of time (in hours) the SLA metric was active. | VALUE(SLA metric completion time (min))/60/24 |
| First reply time (min) | The duration in minutes between when the ticket was created and the first public agent reply on the ticket. | (First reply time (min)) |
| First resolution time (min) | The number of minutes between when the ticket was created and when it was first resolved. | (First resolution time (min)) |
| Full resolution time - min | The duration in minutes from when the ticket was created to its latest resolution. | (Full resolution time (min)) |
| Requester wait time (min) | The number of minutes a ticket spends in the New, Open, and On-hold statuses. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | (Requester wait time (min)) |
| Agent wait time (min) | The total time in minutes that a ticket was in the pending status. It measures how long agents were waiting for the customer replies. | (Agent wait time (min)) |
| On-hold time (min) | The total time in minutes that a ticket was in the on-hold status. | (On-hold time (min)) |
| First reply time (hrs) | The duration in hours between when the ticket was created and the first public agent reply on the ticket. | VALUE(First reply time (min))/60 |
| First resolution time (hrs) | The number of hours between when the ticket was created and when it was first resolved. | VALUE(First resolution time (min))/60 |
| Full resolution time (hrs) | The duration in hours from when the ticket was created to its latest resolution. | VALUE(Full resolution time (min))/60 |
| Requester wait time (hrs) | The number of hours a ticket spends in the New, Open, and On-hold statuses. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | VALUE(Requester wait time (min))/60 |
| Agent wait time (hrs) | The total time in hours that a ticket was in the pending status. It measures how long agents were waiting for the customer replies. | VALUE(Agent wait time (min))/60 |
| On-hold time (hrs) | The total time in hours that a ticket was in the on-hold status. | VALUE(On-hold time (min))/60 |
| First reply time (days) | The duration in days between when the ticket was created and the first public agent reply on the ticket. | VALUE(First reply time (min))/60/24 |
| First resolution time (days) | The number of days between when the ticket was created and when it was first resolved. | VALUE(First resolution time (min))/60/24 |
| Full resolution time (days) | The duration in days from when the ticket was created to its latest resolution. | VALUE(Full resolution time (min))/60/24 |
| Requester wait time (days) | The number of days a ticket spends in the New, Open, and On-hold statuses. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | VALUE(Requester wait time (min))/60/24 |
| Agent wait time (days) | The total time in days that a ticket was in the pending status. It measures how long agents were waiting for the customer replies. | VALUE(Agent wait time (min))/60/24 |
| On-hold time (days) | The total time in days that a ticket was in the on-hold status. | VALUE(On-hold time (min))/60/24 |
| First reply time - Business hours (min) | The duration in minutes between when the ticket was created and the first public agent reply on the ticket within business hours. | (First reply time - Business hours (min)) |
| First resolution time - Business hours (min) | The duration in minutes between when the ticket was created and its first resolution within business hours. | (First resolution time - Business hours (min)) |
| Full resolution time - Business hours (min) | The duration in minutes between when the ticket was created and its latest resolution within business hours. | (Full resolution time - Business hours (min)) |
| Requester wait time - Business hours (min) | The number of minutes a ticket spends in the New, Open, or On-hold status during business hours. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | (Requester wait time - Business hours (min)) |
| Agent wait time - Business hours (min) | The total combined time in minutes that the ticket was in the pending status within business hours. It measures how long agents were waiting for the customer replies within business hours. | (Agent wait time - Business hours (min)) |
| On-hold time - Business hours (min) | The total combined time in minutes that the ticket was in the on-hold status during business hours. | On-hold time - Business hours (min) |
| First reply time - Business hours (hrs) | The duration in hours between when the ticket was created and the first public agent reply on the ticket within business hours. | VALUE(First reply time - Business hours (min))/60 |
| First resolution time - Business hours (hrs) | The duration in hours between when the ticket was created and its first resolution within business hours. | VALUE(First resolution time - Business hours (min))/60 |
| Full resolution time - Business hours (hrs) | The duration in hours between when the ticket was created and its latest resolution within business hours. | VALUE(Full resolution time - Business hours (min))/60 |
| Requester wait time - Business hours (hrs) | The number of hours a ticket spends in the New, Open, or On-hold status during business hours. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | VALUE(Requester wait time - Business hours (min))/60 |
| Agent wait time - Business hours (hrs) | The total combined time in hours that the ticket was in the pending status within business hours. It measures how long agents were waiting for the customer replies within business hours. | VALUE(Agent wait time - Business hours (min))/60 |
| On-hold time - Business hours (hrs) | The total combined time in hours that the ticket was in the on-hold status during business hours. | VALUE(On-hold time - Business hours (min))/60 |

### SLAs attributes

This section lists and defines all attributes available in the SLAs dataset.

Table 8. SLAs attributes

| Attribute | Definition |
| --- | --- |
| SLA policy name | The name of the SLA policy that the ticket is measured against. |
| SLA policy ID | The ID number of the SLA policy that the ticket is measured against. |
| SLA policy unique ID | The ID number of the SLA policy that is unique (unrepeatable). |
| SLA policy ticket ID | The ticket ID of the SLA Policy |
| SLA metric | Which SLA metric is being measured (Agent Work Time, First Reply Time, Next Reply Time, Pausable Update Time, Periodic Update Time, Requester Wait Time, or Total Resolution Time). |
| SLA metric status | The status of the SLA metric. The status can be Active or Completed. |
| SLA metric instance | Which reactivation instance of the metric is being measured on the ticket. |
| SLA target status | The status of the SLA Target (goal). Attribute values are: Achieved or Breached. |
| SLA target operation hours | The type of operating hours associated with the SLA target. Attribute values are: Business Hours, Calendar Hours. |
| SLA target in business hours | Indicates whether the hours of operation for the SLA policy is set to business hours. Attribute values are: True or False. For another way to report on this information, see the **SLA target operation hours** metric. |
| SLA event ID | The ID number for an SLA event associated with the ticket. |
| Ticket ID | The ID number of the ticket. |
| Ticket status | The status of the ticket. |
| Ticket custom status name | The name of a custom ticket status. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). For tickets that existed before custom ticket statuses were enabled, this attribute returns **NULL**. Data is available only from October 19, 2023 onward. |
| Ticket custom status category | The category that a custom ticket status is mapped to. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). For tickets that existed before custom ticket statuses were enabled, this attribute returns **Ticket Status**. Data is available only from October 19, 2023 onward. |
| Ticket custom status state | Returns **true** if a custom ticket status is active, or **false** if a custom ticket status is deactivated. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). Data is available only from October 19, 2023 onward. |
| Ticket group | Name of the group where the ticket was assigned. |
| Ticket channel | The channel a ticket was created from. For more information about the ticket channels Explore collects, see [Understanding ticket channels in Explore](https://support.zendesk.com/hc/en-us/articles/4408836378394). |
| Ticket brand | The brand of the ticket. |
| Ticket external ID | The external ID of the ticket. |
| Ticket form | The current ticket form used on the ticket. |
| Ticket priority | The ticket's priority. |
| Ticket subject | The subject of the ticket. |
| Ticket problem ID | The ID of the ticket defined as a problem ticket. |
| Ticket tags | The tags associated with the ticket. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket type | The ticket type: Question, Incident, Problem, or Task. |
| Sharing agreement inbound | Affiliated instances of Zendesk Support and companies who share tickets with current instance of Zendesk Support. |
| Sharing agreement outbound | Affiliated instances of Zendesk Support and companies tickets are shared with. |
| Assignee name | The name of the assignee. Values for this attribute (and for the other Assignee attributes below) include users who currently have an agent or admin role, as well as users who previously had an agent or admin role and were assigned to a ticket at least once. |
| Assignee role | The role of an assignee, either admin, agent, or end user. |
| Assignee ID | The ticket's assignee ID. |
| Assignee email | The ticket assignees email address. |
| Assignee status | The current status of the ticket assignee. |
| Assignee tags | Tags added to the assignee. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Requester name | The name of the user who is asking for support through a ticket. By default, the requester of a ticket is the submitter, but the requester can be changed. For example, if an agent opens a ticket on behalf of a customer, the customer would be the requester and the agent would be the submitter. |
| Requester role | The role of a requester, either admin, agent, or end user. |
| Requester ID | The ID number for a ticket's requester. |
| Requester email | The email address of the ticket requester. By default, this returns the primary email of the ticket requester. However, if a user has an unverified primary email addresses and a verified secondary email address, Explore uses the verified secondary email address. |
| Requester status | The Zendesk status of the ticket requester. |
| Requester tags | Tags associated with the requester. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Submitter name | The name of the user who actually created a ticket. By default, the submitter of a ticket is the requester, but the requester can be changed (the submitter cannot be). For example, if an agent opens a ticket on behalf of a customer, the agent would be the submitter and the customer would be the requester. |
| Submitter role | The role of the submitter, either admin, agent, or end user. |
| Submitter ID | The ID of the ticket submitter. |
| Submitter email | The email address of the ticket submitter. By default, this returns the primary email of the ticket submitter. However, if a user has an unverified primary email addresses and a verified secondary email address, Explore uses the verified secondary email address. |
| Submitter status | The status of the ticket submitter. |
| Submitter tags | Tags added to the ticket submitter. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket organization name | The name of the organization associated with the ticket. |
| Ticket organization ID | The ID of the organization associated with the ticket. |
| Ticket organization status | The status of the organization associated with the ticket. |
| Ticket organization tags | The tags of the organization associated with the ticket. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Requester organization name | The organization name of the ticket requester. |
| Requester organization ID | The organization ID of the ticket requester. |
| Requester organization status | The organization status of the ticket requester. |
| Requester organization tags | The organization tags associated with the ticket requester. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket satisfaction rating | The satisfaction rating left by the customer on the ticket. Values: Good, Bad, Offered, Unoffered. |
| Ticket satisfaction comment | The comment left by the customer along with the satisfaction rating. |
| Ticket satisfaction reason | The reason selected by the customer along with the satisfaction rating. |
| Intent (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what the ticket is about. To see the possible values, [open the Taxonomy tab of the Intent settings page](https://support.zendesk.com/hc/en-us/articles/9488234915610) to see the AI Intents list under the **Taxonomy values** heading. |
| Intent confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the intent prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Language (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what language the ticket is written in. To see the possible values, open the Taxonomy tab of the settings page. |
| Language confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the language prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Sentiment (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of how the customer feels about their request. Possible values are **Very Positive**, **Positive**, **Neutral**, **Negative**, and **Very Negative**. |
| Sentiment confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the sentiment prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Time - SLA status update | Includes a number of attributes that return the time and date when the SLA status was last updated. |
| Time - Ticket created | Includes a number of attributes that return the time and date when the ticket was created in various time measurements. |
| Time - Ticket solved | Includes a number of attributes that return the time and date when the ticket was most recently solved in various time measurements. |
| Time - Ticket last updated | Includes a number of attributes that return the time and date when the ticket was last updated. |
| Time - Ticket requester updated | The time when the ticket was last updated by its requester. |
| Time - Ticket last assigned | Includes a number of attributes that return the time and date when the ticket was last assigned to an agent. |
| Time - Ticket first assigned | Includes a number of attributes that return the time and date when the ticket was first assigned to an agent. |
| Time - Ticket type - Task due | Includes a number of attributes that return the due date by which a ticket of type "Task" should be completed. |

Tip: You can also report on custom fields that you’ve created in Zendesk Support. See [Reporting with custom fields](https://support.zendesk.com/hc/en-us/articles/4408824384538).

## Group SLAs dataset

The Group SLAs dataset contains metrics and attributes that relate to your [group SLA policies](https://support.zendesk.com/hc/en-us/articles/5322445643802). This section list all the available elements for the Zendesk Group SLA dataset. If you have active group SLA policies, the Group SLAs reporting dashboard enables you to easily view how well you are meeting these policies.

- [Group SLAs metrics](#topic_xvt_cjx_kxb)
- [Group SLAs attributes](#topic_zvt_cjx_kxb)

Note: This dataset appears only if you have tickets with group SLA policies applied. See [Defining group SLA policies](https://support.zendesk.com/hc/en-us/articles/5322445643802).

### Group SLAs metrics

This section lists and defines all metrics available in the Group SLAs dataset.

Table 9. Group SLAs metrics

| Metric | Definition | Explore formula |
| --- | --- | --- |
| Group SLA tickets | The number of tickets that have group SLA targets applied. | [Ticket ID] |
| Achieved group SLA tickets | The number of tickets that met all applied group SLA policy targets. | D\_COUNT(Group SLA tickets)-D\_COUNT(Breached group SLA tickets)-SUM(Unbreached active group SLA tickets) |
| Breached group SLA tickets | The number of tickets that have breached at least one group SLA policy target. | IF ( [Group SLA target status]="Breached") THEN [Ticket ID] ENDIF |
| Active group SLA tickets | The number of group SLA tickets whose metrics have not been completed yet. | D\_COUNT(Group SLA tickets)-D\_COUNT(Breached or active Group SLA tickets) |
| Breached active group SLA tickets | The number of group SLA tickets whose metrics have not yet been completed, but at least one SLA policy target has been breached. | IF ([Group SLA metric status]= "Active" AND [Group SLA target status]= "Breached") THEN [Ticket ID] ENDIF |
| Breached or active group SLA tickets | The number of group SLA tickets whose metrics have not yet been completed, or at least one SLA policy target has been breached. | IF ([Group SLA metric status]= "Active" OR [Group SLA target status]= "Breached") THEN [Group SLA policy ticket ID] ENDIF |
| Unbreached active group SLA tickets | The number of group SLA tickets whose metrics have not been completed yet and no group SLA policy targets have been breached, yet. | D\_COUNT(Active group SLA tickets)-D\_COUNT(Breached active group SLA tickets) |
| % Achieved group SLA tickets | The number of tickets that met all applied group SLA policy targets expressed as a percentage of all group SLA tickets. | SUM(Achieved group SLA tickets)/(SUM(Achieved group SLA tickets)+D\_COUNT(Breached group SLA tickets)) |
| % Breached group SLA tickets | The number of tickets that have breached at least one group SLA policy target expressed as a percentage of all group SLA tickets. | D\_COUNT(Breached group SLA tickets)/(SUM(Achieved group SLA tickets)+D\_COUNT(Breached group SLA tickets)) |
| Group SLA policies | The number of group SLA policies. | IF ( [Group SLA policy ID]!=NULL AND LENGTH(STRING([Group SLA policy ID]))>0) THEN COUNT\_VALUES([Group SLA policy unique ID]) ENDIF |
| Achieved group SLA policies | The number of group SLA policies that have been achieved. | COUNT(Group SLA policies)-COUNT(Breached or active Group SLA policies) |
| Breached group SLA policies | The number of group SLA policies that have been breached. | IF ( [Group SLA target status]="Breached" AND [Group SLA policy ID]!=NULL AND LENGTH(STRING([Group SLA policy ID]))>0) THEN COUNT\_VALUES([Group SLA policy unique ID]) ENDIF |
| Active group SLA policies | The number of group SLA policies whose metrics have not been completed yet. | IF ( [Group SLA metric status]= "Active" AND [Group SLA policy ID]!=NULL AND LENGTH(STRING([Group SLA policy ID]))>0) THEN COUNT\_VALUES([Group SLA policy unique ID]) ENDIF |
| Breached active group SLA policies | The number of group SLA policies whose metrics have not yet been completed, but at least one group SLA policy target has been breached. | IF ( [Group SLA metric status]= "Active" AND [Group SLA target status]= "Breached" AND [Group SLA policy ID]!=NULL AND LENGTH(STRING([Group SLA policy ID]))>0) THEN COUNT\_VALUES([Group SLA policy unique ID]) ENDIF |
| Breached or active group SLA policies | The number of group SLA policies whose metrics have not yet been completed, or at least one group SLA policy target has been breached. | IF ( [Group SLA metric status]= "Active" OR [Group SLA target status]= "Breached" AND [Group SLA policy ID]!=NULL AND LENGTH(STRING([Group SLA policy ID]))>0) THEN COUNT\_VALUES([Group SLA policy unique ID]) ENDIF |
| Unbreached active group SLA policies | The number of group SLA policies whose metrics have not been completed and no policy targets have been breached. | COUNT(Active group SLA policies)-COUNT(Breached active group SLA policies) |
| Group SLA targets | The number of group SLA targets. | [Group SLA event ID] |
| Achieved group SLA targets | The number of group SLA targets that were achieved. | IF ([Group SLA target status]= "Achieved" ) THEN [Group SLA event ID] ENDIF |
| Breached group SLA targets | The number of group SLA targets that were breached. | IF ([Group SLA target status]= "Breached") THEN [Group SLA event ID] ENDIF |
| Active group SLA targets | The number of active group SLA targets. An active group SLA target is one whose metric has not been completed yet. | IF ([Group SLA metric status]= "Active") THEN [Group SLA event ID] ENDIF |
| Breached active group SLA targets | The number of active group SLA targets that have been breached. | IF ([Group SLA metric status]= "Active" AND [Group SLA target status]="Breached") THEN [Group SLA event ID] ENDIF |
| Unbreached active group SLA targets | The number of active group SLA targets that have not been breached. | IF ([Group SLA metric status]= "Active" AND [Group SLA target status]=NULL) THEN [Group SLA event ID] ENDIF |
| % Achieved group SLA targets | The percentage of group SLA targets that were achieved out of the total number of targets that were achieved and breached. | COUNT(Achieved group SLA targets)/(COUNT(Achieved group SLA targets)+COUNT(Breached group SLA targets)) |
| % Breached group SLA targets | The percentage of group SLA targets that were breached out of the total number of targets that were achieved and breached. | COUNT(Breached group SLA targets)/(COUNT(Achieved group SLA targets)+COUNT(Breached group SLA targets)) |
| Achieved group SLA targets - Daily average | The daily average of the achieved group SLA targets. | COUNT(Achieved group SLA targets)/DCOUNT\_Values([Group SLA update - Date]) |
| Breached group SLA targets - Daily average | The daily average of the breached group SLA targets. | COUNT(Breached group SLA targets)/DCOUNT\_Values([Group SLA update - Date]) |
| Group SLA metric breach time (min) | The time duration between the target time and actual group SLA fulfillment (in minutes) for the group SLA metric has been breached. | IF ([Group SLA target status]= "Breached") THEN VALUE(Group SLA metric completion time (min))- VALUE(Group SLA metric target time (min)) ENDIF |
| Group SLA metric target time (min) | The group SLA target time (in minutes) for the group SLA metric. | (Group SLA metric target time (min)) |
| Group SLA metric completion time (min) | The amount of time (in minutes) the group SLA metric was active. | (Group SLA metric completion time (min)) |
| Group SLA metric breach time (hrs) | The time duration between the target time and actual group SLA fulfillment (in hours) for the group SLA metric has been breached. | IF ([Group SLA target status]= "Breached") THEN (VALUE(Group SLA metric completion time (min))- VALUE(Group SLA metric target time (min)))/60 ENDIF |
| Group SLA metric target time (hrs) | The group SLA target time (in hours). | VALUE(Group SLA metric target time (min))/60 |
| Group SLA metric completion time (hrs) | The amount of time (in hours) the group SLA metric was active. | VALUE(Group SLA metric completion time (min))/60 |
| Group SLA metric breach time (days) | The time duration between the target time and actual group SLA fulfillment (in days) for the group SLA metric has been breached. | IF ([Group SLA target status]= "Breached") THEN (VALUE(Group SLA metric completion time (min))- VALUE(Group SLA metric target time (min)))/60/24 ENDIF |
| Group SLA metric target time (days) | The group SLA target time (in days). | VALUE(Group SLA metric target time (min))/60/24 |
| Group SLA metric completion time (days) | The amount of time (in hours) the group SLA metric was active. | VALUE(Group SLA metric completion time (min))/60/24 |
| First reply time (min) | The duration in minutes between when the ticket was created and the first public agent reply on the ticket. | (First reply time (min)) |
| First resolution time (min) | The number of minutes between when the ticket was created and when it was first resolved. | (First resolution time (min)) |
| Full resolution time - min | The duration in minutes from when the ticket was created to its latest resolution. | (Full resolution time (min)) |
| Requester wait time (min) | The number of minutes a ticket spends in the New, Open, and On-hold statuses. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | (Requester wait time (min)) |
| Agent wait time (min) | The total time in minutes that a ticket was in the pending status. It measures how long agents were waiting for the customer replies. | (Agent wait time (min)) |
| On-hold time (min) | The total time in minutes that a ticket was in the on-hold status. | (On-hold time (min)) |
| First reply time (hrs) | The duration in hours between when the ticket was created and the first public agent reply on the ticket. | VALUE(First reply time (min))/60 |
| First resolution time (hrs) | The number of hours between when the ticket was created and when it was first resolved. | VALUE(First resolution time (min))/60 |
| Full resolution time (hrs) | The duration in hours from when the ticket was created to its latest resolution. | VALUE(Full resolution time (min))/60 |
| Requester wait time (hrs) | The number of hours a ticket spends in the New, Open, and On-hold statuses. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | VALUE(Requester wait time (min))/60 |
| Agent wait time (hrs) | The total time in hours that a ticket was in the pending status. It measures how long agents were waiting for the customer replies. | VALUE(Agent wait time (min))/60 |
| On-hold time (hrs) | The total time in hours that a ticket was in the on-hold status. | VALUE(On-hold time (min))/60 |
| First reply time (days) | The duration in days between when the ticket was created and the first public agent reply on the ticket. | VALUE(First reply time (min))/60/24 |
| First resolution time (days) | The number of days between when the ticket was created and when it was first resolved. | VALUE(First resolution time (min))/60/24 |
| Full resolution time (days) | The duration in days from when the ticket was created to its latest resolution. | VALUE(Full resolution time (min))/60/24 |
| Requester wait time (days) | The number of days a ticket spends in the New, Open, and On-hold statuses. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | VALUE(Requester wait time (min))/60/24 |
| Agent wait time (days) | The total time in days that a ticket was in the pending status. It measures how long agents were waiting for the customer replies. | VALUE(Agent wait time (min))/60/24 |
| On-hold time (days) | The total time in days that a ticket was in the on-hold status. | VALUE(On-hold time (min))/60/24 |
| First reply time - Business hours (min) | The duration in minutes between when the ticket was created and the first public agent reply on the ticket within business hours. | (First reply time - Business hours (min)) |
| First resolution time - Business hours (min) | The duration in minutes between when the ticket was created and its first resolution within business hours. | (First resolution time - Business hours (min)) |
| Full resolution time - Business hours (min) | The duration in minutes between when the ticket was created and its latest resolution within business hours. | (Full resolution time - Business hours (min)) |
| Requester wait time - Business hours (min) | The number of minutes a ticket spends in the New, Open, or On-hold status during business hours. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | (Requester wait time - Business hours (min)) |
| Agent wait time - Business hours (min) | The total combined time in minutes that the ticket was in the pending status within business hours. It measures how long agents were waiting for the customer replies within business hours. | (Agent wait time - Business hours (min)) |
| On-hold time - Business hours (min) | The total combined time in minutes that the ticket was in the on-hold status during business hours. | On-hold time - Business hours (min) |
| First reply time - Business hours (hrs) | The duration in hours between when the ticket was created and the first public agent reply on the ticket within business hours. | VALUE(First reply time - Business hours (min))/60 |
| First resolution time - Business hours (hrs) | The duration in hours between when the ticket was created and its first resolution within business hours. | VALUE(First resolution time - Business hours (min))/60 |
| Full resolution time - Business hours (hrs) | The duration in hours between when the ticket was created and its latest resolution within business hours. | VALUE(Full resolution time - Business hours (min))/60 |
| Requester wait time - Business hours (hrs) | The number of hours a ticket spends in the New, Open, or On-hold status during business hours. This number is measured only after a ticket's status changes from New/Open/On-hold to Pending/Solved/Closed. See [Requester wait time](about-native-support-time-duration-metrics.md#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617) for further explanation. | VALUE(Requester wait time - Business hours (min))/60 |
| Agent wait time - Business hours (hrs) | The total combined time in hours that the ticket was in the pending status within business hours. It measures how long agents were waiting for the customer replies within business hours. | VALUE(Agent wait time - Business hours (min))/60 |
| On-hold time - Business hours (hrs) | The total combined time in hours that the ticket was in the on-hold status during business hours. | VALUE(On-hold time - Business hours (min))/60 |

### Group SLAs attributes

This section lists and defines all attributes available in the Group SLAs dataset.

Table 10. Group SLAs attributes

| Attribute | Definition |
| --- | --- |
| Group SLA policy name | The name of the group SLA policy that the ticket is measured against. |
| Group SLA policy ID | The ID number of the group SLA policy that the ticket is measured against. |
| Group SLA policy unique ID | The ID number of the group SLA policy that is unique (unrepeatable). |
| Group SLA policy ticket ID | The ticket ID of the group SLA Policy |
| Group SLA metric | Which group SLA metric is being measured (Group ownership time). |
| Group SLA metric status | The status of the group SLA metric. The status can be Active or Completed. |
| Group SLA metric instance | Which reactivation instance of the metric is being measured on the ticket. |
| Group SLA target status | The status of the group SLA Target (goal). Attribute values are: Achieved or Breached. |
| Group SLA target operation hours | The type of operating hours associated with the group SLA target. Attribute values are: Business Hours, Calendar Hours. |
| Group SLA target in business hours | Indicates whether the hours of operation for the group SLA policy is set to business hours. Attribute values are: True or False. For another way to report on this information, see the **Group SLA target operation hours** metric. |
| Group SLA event ID | The ID number for a group SLA event associated with the ticket. |
| Ticket ID | The ID number of the ticket. |
| Ticket status | The status of the ticket. |
| Ticket custom status name | The name of a custom ticket status. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). For tickets that existed before custom ticket statuses were enabled, this attribute returns **NULL**. Data is available only from October 19, 2023 onward. |
| Ticket custom status category | The category that a custom ticket status is mapped to. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). For tickets that existed before custom ticket statuses were enabled, this attribute returns **Ticket Status**. Data is available only from October 19, 2023 onward. |
| Ticket custom status state | Returns **true** if a custom ticket status is active, or **false** if a custom ticket status is deactivated. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). Data is available only from October 19, 2023 onward. |
| Ticket group | Name of the group where the ticket was assigned. |
| Ticket channel | The channel a ticket was created from. For more information about the ticket channels Explore collects, see [Understanding ticket channels in Explore](https://support.zendesk.com/hc/en-us/articles/4408836378394). |
| Ticket brand | The brand of the ticket. |
| Ticket external ID | The external ID of the ticket. |
| Ticket form | The current ticket form used on the ticket. |
| Ticket priority | The ticket's priority. |
| Ticket subject | The subject of the ticket. |
| Ticket problem ID | The ID of the ticket defined as a problem ticket. |
| Ticket tags | The tags associated with the ticket. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket type | The ticket type: Question, Incident, Problem, or Task. |
| Sharing agreement inbound | Affiliated instances of Zendesk Support and companies who share tickets with current instance of Zendesk Support. |
| Sharing agreement outbound | Affiliated instances of Zendesk Support and companies tickets are shared with. |
| Assignee name | The name of the assignee. Values for this attribute (and for the other Assignee attributes below) include users who currently have an agent or admin role, as well as users who previously had an agent or admin role and were assigned to a ticket at least once. |
| Assignee role | The role of an assignee, either admin, agent, or end user. |
| Assignee ID | The ticket's assignee ID. |
| Assignee email | The ticket assignees email address. |
| Assignee status | The current status of the ticket assignee. |
| Assignee tags | Tags added to the assignee. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Requester name | The name of the user who is asking for support through a ticket. By default, the requester of a ticket is the submitter, but the requester can be changed. For example, if an agent opens a ticket on behalf of a customer, the customer would be the requester and the agent would be the submitter. |
| Requester role | The role of a requester, either admin, agent, or end user. |
| Requester ID | The ID number for a ticket's requester. |
| Requester email | The email address of the ticket requester. By default, this returns the primary email of the ticket requester. However, if a user has an unverified primary email addresses and a verified secondary email address, Explore uses the verified secondary email address. |
| Requester status | The Zendesk status of the ticket requester. |
| Requester tags | Tags associated with the requester. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Submitter name | The name of the user who actually created a ticket. By default, the submitter of a ticket is the requester, but the requester can be changed (the submitter cannot be). For example, if an agent opens a ticket on behalf of a customer, the agent would be the submitter and the customer would be the requester. |
| Submitter role | The role of the submitter, either admin, agent, or end user. |
| Submitter ID | The ID of the ticket submitter. |
| Submitter email | The email address of the ticket submitter. By default, this returns the primary email of the ticket submitter. However, if a user has an unverified primary email addresses and a verified secondary email address, Explore uses the verified secondary email address. |
| Submitter status | The status of the ticket submitter. |
| Submitter tags | Tags added to the ticket submitter. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket organization name | The name of the organization associated with the ticket. |
| Ticket organization ID | The ID of the organization associated with the ticket. |
| Ticket organization status | The status of the organization associated with the ticket. |
| Ticket organization tags | The tags of the organization associated with the ticket. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Requester organization name | The organization name of the ticket requester. |
| Requester organization ID | The organization ID of the ticket requester. |
| Requester organization status | The organization status of the ticket requester. |
| Requester organization tags | The organization tags associated with the ticket requester. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket satisfaction rating | The satisfaction rating left by the customer on the ticket. Values: Good, Bad, Offered, Unoffered. |
| Ticket satisfaction comment | The comment left by the customer along with the satisfaction rating. |
| Ticket satisfaction reason | The reason selected by the customer along with the satisfaction rating. |
| Time - Group SLA status update | Includes a number of attributes that return the time and date when the group SLA status was last updated. |
| Intent (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what the ticket is about. To see the possible values, [open the Taxonomy tab of the Intent settings page](https://support.zendesk.com/hc/en-us/articles/9488234915610) to see the AI Intents list under the **Taxonomy values** heading. |
| Intent confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the intent prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Language (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what language the ticket is written in. To see the possible values, open the Taxonomy tab of the settings page. |
| Language confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the language prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Sentiment (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of how the customer feels about their request. Possible values are **Very Positive**, **Positive**, **Neutral**, **Negative**, and **Very Negative**. |
| Sentiment confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the sentiment prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Time - Ticket created | Includes a number of attributes that return the time and date when the ticket was created in various time measurements. |
| Time - Ticket solved | Includes a number of attributes that return the time and date when the ticket was most recently solved in various time measurements. |
| Time - Ticket last updated | Includes a number of attributes that return the time and date when the ticket was last updated. |
| Time - Ticket requester updated | The time when the ticket was last updated by its requester. |
| Time - Ticket last assigned | Includes a number of attributes that return the time and date when the ticket was last assigned to an agent. |
| Time - Ticket first assigned | Includes a number of attributes that return the time and date when the ticket was first assigned to an agent. |
| Time - Ticket type - Task due | Includes a number of attributes that return the due date by which a ticket of type "Task" should be completed. |

Tip: You can also report on custom fields that you’ve created in Zendesk Support. See [Reporting with custom fields](https://support.zendesk.com/hc/en-us/articles/4408824384538).