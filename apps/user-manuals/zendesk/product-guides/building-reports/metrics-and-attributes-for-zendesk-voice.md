# Metrics and attributes for Zendesk Voice

Source: https://support.zendesk.com/hc/en-us/articles/4409156145434-Metrics-and-attributes-for-Zendesk-Voice

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Professional or Enterprise |

Use this article to discover the metrics and attributes you can use to build reports based on your usage of Zendesk Voice. These datasets are also used for the Voice prebuilt dashboards (see [Overview of the Zendesk Voice dashboard](https://support.zendesk.com/hc/en-us/articles/4408827894554)).

For more information about how to create reports, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530).

## Calls dataset

The Calls dataset contains metrics and attributes that relate to your call statistics. This sections lists all the available elements for the dataset, and contains the following topics:

This section contains the following topics:

- [Voice dataset schema](#topic_smk_45f_kkb)
- [Zendesk Talk metrics](#topic_ucn_xdh_5bb)
- [Zendesk Talk attributes](#topic_w5f_xdh_5bb)

### Voice dataset schema

Use this diagram to help you understand the elements of the Voice dataset and their relationships.

![Talk calls dataset schema](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Calls.jpg)

### Voice metrics

This section lists and defines all of the Voice metrics available.

Table 1. Voice metrics

| Metric | Definition | Calculation |
| --- | --- | --- |
| Calls | The total number of calls. | [Call ID] |
| Completed calls | The total number of calls that were completed. | IF ([Call completion status]="Completed") THEN [Call ID] ENDIF |
| Abandoned calls | The number of calls that were abandoned while in your IVR, queue, voicemail, or on-hold. | IF ([Call completion status]="Abandoned In IVR" OR [Call completion status]="Abandoned In queue" OR [Call completion status]="Abandoned In voicemail" OR [Call completion status]="Abandoned in on-hold" ) THEN [Call ID] ENDIF |
| Non-answered calls | The number of calls during which the end user wasn’t connected with an agent, voicemail or external number and didn't abandon the call in one of the defined call stages. | IF ([Call completion status]="Not answered") THEN [Call ID] ENDIF |
| Recorded calls | The number of calls that were recorded. | IF ([Call recorded] = "TRUE") THEN [Call ID] ENDIF |
| Non-recorded calls | The number of calls that were not recorded. | IF ([Call recorded] = "FALSE") THEN [Call ID] ENDIF |
| Multi-assist calls | The number of calls that were assisted by more than one agent. | IF ([Leg consultation type]!=NULL) THEN [Call ID] ENDIF |
| Consultation calls | The number of calls that had a consultation with an additional agent or external number. | IF ([Leg consultation type]="Consultation") THEN [Call ID] ENDIF |
| Unattended transfer calls | The number of calls that were transferred to another agent without the consultation phase. | IF ([Leg consultation type]="Unattended transfer") THEN [Call ID] ENDIF |
| Conference calls | The number of calls that had a 3 person conference. | IF ([Leg consultation type]="Conference") THEN [Call ID] ENDIF |
| Good quality calls | The number of good quality calls. These are calls that had no audio or network issues. | IF ([Call quality]="Good") THEN [Call ID] ENDIF |
| Bad quality calls | The number of bad quality calls. These are calls that had at least one audio or network issue. | IF ([Call quality]="Bad") THEN [Call ID] ENDIF |
| % Call completion rate | The percentage of the calls that were completed successfully. | D\_COUNT(Completed calls)/D\_COUNT(Calls) |
| % Call multi-assist rate | The percentage of the calls that were assisted by more than one agent. | D\_COUNT(Multi-assist calls)/D\_COUNT(Calls) |
| % Call quality rate | The percentage of the calls that had good quality from the total number of calls on which the quality was measured. | D\_COUNT(Good quality calls)/(D\_COUNT(Good quality calls)+D\_COUNT(Bad quality calls)) |
| Calls - Daily average | The average number of calls each day. | D\_COUNT(Calls)/DCOUNT\_VALUES([Call - Date]) |
| Inbound calls | The total number of inbound calls. | IF [Call direction]="inbound" THEN [Call ID] ENDIF |
| Completed inbound calls | The total number of inbound calls that were completed. | IF ([Call direction]="Inbound" AND [Call completion status]="Completed") THEN [Call ID] ENDIF |
| Abandoned inbound calls | The total number of incoming calls that were abandoned by the end user. | IF ([Call direction]="Inbound" AND ([Call completion status]="Abandoned in IVR" OR [Call completion status]="Abandoned in queue" OR [Call completion status]="Abandoned in voicemail" OR [Call completion status]="Abandoned in on-hold" )) THEN [Call ID] ENDIF |
| Non-answered inbound calls | The number of inbound calls during which the end user wasn’t connected with an agent, voicemail or external number and didn't abandon the call in one of the defined call stages. | IF ([Call direction]="Inbound" AND [Call completion status]="Not answered") THEN [Call ID] ENDIF |
| Regular inbound calls | The number of regular inbound calls. | IF ([Call direction]="Inbound" AND [Call type]="Regular") THEN [Call ID] ENDIF |
| Callback calls | The number of inbound calls for which the callback feature was used. | IF ([Call type]="Callback") THEN [Call ID] ENDIF |
| Forwarded calls | The number of inbound calls forwarded to external phone numbers via IVR. | IF ([Call type]="Forwarded") THEN [Call ID] ENDIF |
| Overflow calls | The number of inbound calls forwarded to overflow phone numbers. | IF ([Call type]="Overflow") THEN [Call ID] ENDIF |
| Text back calls | The number of inbound calls forwarded to external phone numbers via IVR. | IF ([Call type]="Text back") THEN [Call ID] ENDIF |
| Voicemail calls | The total number of calls routed to voicemail. | IF ([Call type]="Voicemail") THEN [Call ID] ENDIF |
| Bad quality inbound calls | The number of bad quality inbound calls. | IF ([Call direction]="Inbound" AND [Call quality]="Bad") THEN [Call ID] ENDIF |
| Good quality inbound calls | The number of good quality inbound calls. | IF ([Call direction]="Inbound" AND [Call quality]="Good") THEN [Call ID] ENDIF |
| % Inbound completion rate | The percentage of inbound calls that were completed successfully. | D\_COUNT(Completed inbound calls)/D\_COUNT(Inbound calls) |
| % Inbound quality rate | The percentage of the inbound calls that had a good quality from the total number of inbound calls on which the quality was measured. | D\_COUNT(Good quality inbound calls)/(D\_COUNT(Good quality inbound calls)+D\_COUNT(Bad quality inbound calls)) |
| Inbound calls - Daily average | The average number of inbound calls each day. | D\_COUNT(Inbound calls)/DCOUNT\_VALUES([Call - Date]) |
| Outbound calls | The total number of outbound calls made. | IF ([Call direction]="Outbound") THEN [Call ID] ENDIF |
| Completed outbound calls | The total number of outbound calls that were completed. | IF ([Call direction]="Outbound" AND [Call completion status]="Completed") THEN [Call ID] ENDIF |
| Abandoned outbound calls | The total number of outbound calls that were abandoned while on-hold. | IF ([Call direction]="Outbound" AND [Call completion status]="Abandoned in on-hold") THEN [Call ID] ENDIF |
| Non-answered outbound calls | The number of outbound calls that end users didn’t answer. | IF ([Call direction]="Outbound" AND [Call completion status]="Not answered") THEN [Call ID] ENDIF |
| Good quality outbound calls | The number of good quality outbound calls. | IF ([Call direction]="Outbound" AND [Call quality]="Good") THEN [Call ID] ENDIF |
| Bad quality outbound calls | The number of bad quality outbound calls. | IF ([Call direction]="Outbound" AND [Call quality]="Bad") THEN [Call ID] ENDIF |
| % Outbound completion rate | The percentage of outbound calls that were completed successfully. | D\_COUNT(Completed outbound calls)/D\_COUNT(Outbound calls) |
| % Outbound quality rate | The percentage of outbound calls that had a good quality from the total number of outbound calls on which the quality was measured. | D\_COUNT(Good quality outbound calls)/(D\_COUNT(Good quality outbound calls)+D\_COUNT(Bad quality outbound calls)) |
| Outbound calls - Daily average | The average number of outbound calls each day. | D\_COUNT(Outbound calls)/DCOUNT\_VALUES([Call - Date]) |
| Legs | The total number of call legs. A leg is a segment of a phone call. | [Leg ID] |
| Agent legs | The total number of agent call legs. These are calls initiated by an agent. | IF ([Leg type]="Agent" ) THEN [Leg ID] ENDIF |
| End user legs | The total number of end user call legs. These are calls initiated by an end user. | IF ([Leg type]="End-user" ) THEN [Leg ID] ENDIF |
| External legs | The number of call legs associated with external users. | IF ([Leg type]="External") THEN [Leg ID] ENDIF |
| Consultation legs | The number of call legs that were initiated by the agents for consulting with other agents of external users. | IF ([Leg consultation type]="Consultation") THEN [Leg ID] ENDIF |
| Unattended transfer legs | The number of call legs that were initiated by the agents for consulting with other agents of external users and were transferred to that person. | IF ([Leg consultation type]="Unattended transfer") THEN [Leg ID] ENDIF |
| Conference legs | The number of call legs that were initiated by the agents for consulting with other agents of external users and resulted in a 3 person conference. | IF ([Leg consultation type]="Conference") THEN [Leg ID] ENDIF |
| Good quality legs | The number of good quality call legs. | IF ([Leg quality]="Good") THEN [Leg ID] ENDIF |
| Bad quality legs | The number of bad quality call legs. | IF ([Leg quality]="Bad") THEN [Leg ID] ENDIF |
| Good quality agent legs | The number of good quality agent call legs. | IF ([Leg quality]="Good" AND [Leg type]="Agent") THEN [Leg ID] ENDIF |
| Bad quality agent legs | The number of bad quality agent call legs. | IF ([Leg quality]="Bad" AND [Leg type]="Agent") THEN [Leg ID] ENDIF |
| % Leg quality rate | The percentage of call legs that had a good quality from the total number of call legs on which the quality was measured. | D\_COUNT(Good quality legs)/(D\_COUNT(Good quality legs)+D\_COUNT(Bad quality legs)) |
| % Agent leg quality rate | The percentage of agent call legs that had a good quality from the total number of agent call legs on which the quality was measured. | D\_COUNT(Good quality agent legs)/(D\_COUNT(Good quality agent legs)+D\_COUNT(Bad quality agent legs)) |
| Accepted call legs | The number of inbound calls completed by agents. The leg talk time must be greater than 0. As a result, this metric's results might differ from the [Calls accepted metric](https://support.zendesk.com/hc/en-us/articles/4408883025690#topic_qyl_2rw_bpb:~:text=calls%20on%20hold-,Calls%20accepted,-Total%20number%20of) on the Voice dashboard. | IF ([Call direction]="Inbound" AND [Leg type]="Agent" AND [Leg completion status]="Completed" AND VALUE(Leg talk time (sec))>0) THEN [Leg ID] ENDIF |
| Missed call legs | The number of inbound calls missed by agents. | IF ([Call direction]="Inbound" AND [Leg type]="Agent" AND [Leg completion status]="Agent missed") THEN [Leg ID] ENDIF |
| Declined call legs | The number of inbound calls an agent declined. | IF ([Call direction]="Inbound" AND [Leg type]="Agent" AND ([Leg completion status]="Agent declined" OR [Leg completion status]="Agent declined transfer")) THEN [Leg ID] ENDIF |
| Recording interactions | The number of times agents turned on or off recording during the call. | (Recording interactions) |
| IVR transitions | The number of key presses the caller has made in the IVR menu. | (IVR transitions) |
| Call agents | The name of all call agents. | [Call agent ID] |
| Call end users | The name of all registered end users. | [End-user ID] |
| Call organizations | The number of call organizations. | [Organization ID] |
| Call duration (sec) | The total call duration in seconds for an end user from when the call is connected until it is disconnected. | VALUE(Call duration (sec)) |
| Call talk time (sec) | The duration in seconds that an end user spends actually talking with an agent during a call. | (Call talk time (sec)) |
| Call wait time (sec) | The duration in seconds that an end user spends waiting to talk to an agent after being routed to where they want. For more information, see [What is the difference between Call wait time and Call answer time?](https://support.zendesk.com/hc/en-us/articles/4408846281498) | (Call wait time (sec)) |
| Call answer time (sec) | The duration in seconds that an end user waits for a call to be answered by an agent, including the greetings and IVR. For more information, see [What is the difference between Call wait time and Call answer time?](https://support.zendesk.com/hc/en-us/articles/4408846281498) | (Call answer time (sec)) |
| Call IVR time (sec) | The duration in seconds that an end user spent in an interactive voice response (IVR) system. | (Call IVR time (sec)) |
| Call consultation time (sec) | The duration in seconds that an agent spent consulting with another agent. | (Call consultation time (sec)) |
| Call on-hold time (sec) | The duration in seconds that an end user spent on-hold. | (Call on-hold time (sec)) |
| Call recorded time (sec) | The call recording duration in seconds. This metric always returns 0 for voicemail calls. | (Call recorded time (sec)) |
| Call not recorded time (sec) | The duration in seconds during which a call wasn't recorded. | (Call not recorded time (sec)) |
| Call wrap-up time (sec) | The duration in seconds that an agent spent in the wrap-up stage after a call. | (Call wrap-up time (sec)) |
| Call duration (min) | The total call duration in minutes for an end user from when the call is connected until it is disconnected. | VALUE(Call duration (sec))/60 |
| Call talk time (min) | The duration in minutes that an end user spends actually talking with an agent during a call. | (Call talk time (sec))/60 |
| Call wait time (min) | The duration in minutes that an end user spends waiting to talk to an agent after being routed to where they want. For more information, see [What is the difference between Call wait time and Call answer time?](https://support.zendesk.com/hc/en-us/articles/4408846281498) | (Call wait time (sec))/60 |
| Call answer time (min) | The duration in minutes that an end user waits for a call to be answered by an agent, including the greetings and IVR. For more information, see [What is the difference between Call wait time and Call answer time?](https://support.zendesk.com/hc/en-us/articles/4408846281498) | (Call answer time (sec))/60 |
| Call IVR time (min) | The duration in minutes that an end user spent in an interactive voice response (IVR) system. | (Call IVR time (sec))/60 |
| Call consultation time (min) | The duration in minutes that an agent spent consulting with another agent. | (Call consultation time (sec))/60 |
| Call on-hold time (min) | The duration in minutes that an end user spent on-hold. | (Call on-hold time (sec))/60 |
| Call recorded time (min) | The call recording duration in minutes. This metric always returns 0 for voicemail calls. | (Call recorded time (sec))/60 |
| Call not recorded time (min) | The duration in minutes during which call wasn't recorded. | (Call not recorded time (sec))/60 |
| Call wrap-up time (min) | The duration in minutes that an agent spent in the wrap-up stage after a call. | (Call wrap-up time (sec))/60 |
| Call billed time (min) | The number of minutes for which a call incurred a charge. | (Call billed time (min)) |
| Call duration (hrs) | The total call duration in hours for an end user from when the call is connected until it is disconnected. | VALUE(Call duration (sec))/60/60 |
| Call talk time (hrs) | The duration in hours that an end user spends actually talking with an agent during a call. | (Call talk time (sec))/60/60 |
| Call wait time (hrs) | The duration in hours that an end user spends waiting to talk to an agent after being routed to where they want. For more information, see [What is the difference between Call wait time and Call answer time?](https://support.zendesk.com/hc/en-us/articles/4408846281498) | (Call wait time (sec))/60/60 |
| Call answer time (hrs) | The duration in hours that an end user waits for a call to be answered by an agent, including the greetings and IVR. For more information, see [What is the difference between Call wait time and Call answer time?](https://support.zendesk.com/hc/en-us/articles/4408846281498) | (Call answer time (sec))/60/60 |
| Call IVR time (hrs) | The duration in hours that an end user spent in an interactive voice response (IVR) system. | (Call IVR time (sec))/60/60 |
| Call consultation time (hrs) | The duration in hours that an agent spent consulting with another agent. | (Call consultation time (sec))/60/60 |
| Call recorded time (hrs) | The call recording duration in hours. This metric always returns 0 for voicemail calls. | (Call recorded time (sec))/60/60 |
| Call not recorded time (hrs) | The duration in hours during which call wasn't recorded. | (Call not recorded time (sec))/60/60 |
| Call wrap-up time (hrs) | The duration in hours that an agent spent in the wrap-up stage after a call. | (Call wrap-up time (sec))/60/60 |
| Call on-hold time (hrs) | The duration in hours that an end user spent on-hold. | (Call on-hold time (sec))/60/60 |
| Call billed time (hrs) | The number of hours for which a call incurred a charge. | (Call billed time (min))/60 |
| Leg duration (sec) | By default, gives the average duration in seconds for all legs in seconds. | (Leg duration (sec)) |
| Leg talk time (sec) | The average time in seconds spent actually talking in a call leg. | (Leg talk time (sec)) |
| Leg consultation time (sec) | The average time in seconds when agents consulted with other agents during a call leg. | (Leg consultation time (sec)) |
| Leg conference time (sec) | The time in seconds leg user spent in the 3 person conference. | (Leg conference time (sec)) |
| Leg on-hold time (sec) | The average time in seconds spent on hold in a call leg. | (Leg on-hold time (sec)) |
| Leg wrap-up time (sec) | By default, returns the average wrap-up time in seconds. | (Leg wrap-up time (sec)) |
| Leg duration (min) | By default, returns the average duration for all legs in minutes. | (Leg duration (sec))/60 |
| Leg talk time (min) | The average time in minutes spent actually talking in a call leg. | (Leg talk time (sec))/60 |
| Leg consultation time (min) | The average time in minutes when agents consulted with other agents during a call leg. | (Leg consultation time (sec))/60 |
| Leg conference time (min) | The time in minutes leg user spent in the 3 person conference. | (Leg conference time (sec))/60 |
| Leg on-hold time (min) | The average time in minutes spent on hold in a call leg. | (Leg on-hold time (sec))/60 |
| Leg wrap-up time (min) | By default, returns the average wrap-up time in minutes. | (Leg wrap-up time (sec))/60 |
| Leg duration (hrs) | By default, returns the average duration for all legs in hours. | (Leg duration (sec))/60/60 |
| Leg talk time (hrs) | The average time in hours spent actually talking in a call leg. | (Leg talk time (sec))/60/60 |
| Leg consultation time (hrs) | The average time in hours when agents consulted with other agents during a call leg. | (Leg consultation time (sec))/60/60 |
| Leg conference time (hrs) | The time in hours leg user spent in the 3 person conference. | (Leg conference time (sec))/60/60 |
| Leg on-hold time (hrs) | The average time in hours spent on hold in a call leg. | (Leg on-hold time (sec))/60/60 |
| Leg wrap-up time (hrs) | By default, returns the average wrap-up time in hours. | (Leg wrap-up time (sec))/60/60 |

### Voice attributes

This section lists and defines all the Voice attributes available.

Table 2. Voice attributes

| Attribute | Definition |
| --- | --- |
| Call ID | The ID number of a call. |
| Call direction | Shows whether the call was inbound or outbound. |
| Call type | The type of call. Values are: - **Callback:** A call where a customer has   selected the [callback   option](../setting-up-your-voice-channel/enabling-customer-callback.md), meaning their places are held in   the queue and their call is automatically returned   when an agent is available to speak with   them. - **Forwarded:** A call that has been forwarded   from the initially dialed number to a different   number, like calls routed to an external number   from the IVR menu. - **Overflow:** A call that cannot currently be   taken by any agents or answered by voicemail, for   any of the reasons described in [Managing overflow   calls and after-hours routing](https://support.zendesk.com/hc/en-us/articles/4408832017690-Managing-overflow-calls-and-after-hours-routing-with-Talk). - **Text back:** A call that is switched over   to text by confirming the customer's number, then   disconnecting the call and sending a text message,   as described in [Routing incoming calls with IVR](../managing-your-voice-channel/routing-incoming-calls-with-ivr.md#topic_sms_bsf_yt). - **Voicemail:** A call that is routed to the   number’s voicemail. - **Regular:** A standard inbound or outbound   call that isn't one of the types above. |
| Call channel | The channel the call came in on. Allowed values are **phone**, **mobile-sdk**, **web-widget**, **messaging-widget**, and **messaging-mobile-sdk**. |
| Line type | The type of line the call originated from. Allowed values are **phone** or **digital**. |
| Call completion status | Indicates how the call was completed. Values are **Abandoned in IVR**, **Abandoned in queue**, **Abandoned in voicemail**, **Abandoned in on-hold**, **Completed**, and **Not answered**. **Completed** means that the call was successful and the end user was connected with the agent or the call was directed to voicemail or forwarded to an external number. **Not answered** means that the call wasn’t successful. An example of an inbound not answered call is when the end user wasn’t connected with the agent, or the customer left the call in a transition stage that is not included in the abandoned statuses. An example of outbound not answered call is when the end user didn’t answer the agent’s call. |
| Call Voice number | The phone number registered in Zendesk. |
| Call group | Name of the group where the call was answered. |
| Call callback source | The place from where the callback was requested. Values are **Phone** and **Web Widget (Classic)**. |
| Call exceeded queue wait time | Indicates if the customer exceeded the set time limit waiting for the agent in the queue. |
| Call group is default | Indicates if the call was answered in the default group or not. Values: **True** and **False**. |
| Call IVR action | The last IVR action end user selected. Values are **Group, Invalid keypress, IVR menu, Phone number, Text back,** and **Voicemail.** |
| Call IVR destination | The last IVR destination of the call, possible values are group names and external phone numbers. |
| Call outside business hours | Indicates if the call was outside of business hours. |
| Call overflow number | The phone number to which an overflow call was directed. |
| Call quality | Indicates if a call had good or bad network and audio quality. Values are **Bad, Good,** and **No information.** |
| Call recorded | Indicates if a call was recorded or not. Values are **True** or **False**. |
| Call recording setting | The phone number recording setting used for the call. Values are **Always off,****Always on,****Opt-in** and **Opt-out**. |
| Call recording consent | The recording consent option end user selected at the beginning of the call. Values are **Opted in** and **Opted out**. |
| Call with requested voicemail | Indicates if the caller requested to be put through to voicemail. |
| Leg ID | The unique ID of the call leg. |
| Leg type | The type of call leg, either associated with the agent or customer. |
| Leg completion status | Indicates whether an agent declined an incoming call, missed the prompt to accept the call, or accepted the call for an individual call leg. |
| Leg consultation type | Indicates if a call leg was initiated as part of the consultation and warm transfer feature and what type of consultation it was. Values are **Consultation, Conference**and **Unattended transfer.** |
| Leg agent available via | Indicates the method used by the agent to speak, either phone or browser. |
| Leg agent forwarding number | The phone number to which a call is forwarded when the agent is not available. |
| Leg instance | The unique ID of the call leg. |
| Leg quality | Indicates if a call leg had a good or bad network and audio quality. Values are **Bad**, **Good**, and **No information.** |
| Leg quality issues | Lists the quality issues encountered during the call leg. Values are **High jitter**, **High latency**, **High packet loss**, **High post-dial delay**, **PSTN short duration**, and **Silence**. For definitions of these values, see [Reporting on call quality issues](https://support.zendesk.com/hc/en-us/articles/4408833546522-Reporting-on-Talk-network-and-audio-quality#topic_akd_jd5_hlb). |
| Ticket ID | The Ticket ID associated with a call. |
| Ticket status | The status of the ticket associated with the call. |
| Ticket custom status name | The name of a custom ticket status. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). For tickets that existed before custom ticket statuses were enabled, this attribute returns **NULL**. Data is available only from October 19, 2023 onward. |
| Ticket custom status category | The category that a custom ticket status is mapped to. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). For tickets that existed before custom ticket statuses were enabled, this attribute returns **Ticket Status**. Data is available only from October 19, 2023 onward. |
| Ticket custom status state | Returns **true** if a custom ticket status is active, or **false** if a custom ticket status is deactivated. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). Data is available only from October 19, 2023 onward. |
| Ticket group | Name of the group where the ticket was assigned. |
| Ticket assignee | The person who is assigned the ticket |
| Ticket brand | The brand of the ticket associated with the call. |
| Ticket channel | The channel a ticket was created from. For more information about the ticket channels Explore collects, see [Understanding ticket channels in Explore](https://support.zendesk.com/hc/en-us/articles/4408836378394). |
| Ticket form | Ticket form used on the ticket. |
| Ticket organization | The organization associated with the ticket. |
| Ticket priority | The priority of the ticket associated with the call. |
| Ticket problem ID | The ID of the associated problem ticket. |
| Ticket requester | The name of the ticket requester. |
| Ticket satisfaction rating | The satisfaction rating associated with the ticket. |
| Ticket subject | The subject line of the ticket. |
| Ticket support type | Identifies whether tickets were resolved by an AI agent or a human agent. Possible values are Agent and AI agent. |
| Ticket tags | A list of tags for the ticket associated with the call. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket type | The type of the ticket, for example, incident, or problem. |
| Sharing agreement inbound | The number of tickets a Zendesk Support account shared with your Zendesk Support account. |
| Sharing agreement outbound | The number of tickets your Zendesk Support account shared with another Zendesk Support account. |
| Call agent name | The name of the first agent associated with the call. Values for this attribute (and for the other Call agent attributes below) include users who currently have an agent or admin role, as well as users who previously had an agent or admin role and were assigned to a ticket at least once. |
| Call agent role | The role of the first agent during the call. |
| Call agent ID | The ID of the first agent associated with the call. |
| Call agent email | The email address of the first agent associated with the call. |
| Call agent locale | The locale of the first agent associated with the call. |
| Call agent status | The Zendesk status of the first agent associated with the call. |
| Call agent tags | A list of tags associated with the first agent for the call. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Call agent time zone | The time zone of the first agent associated with the call. |
| End-user name | The name, or phone number of the end user associated with the call. |
| End-user role | The role of the end user associated with the call |
| End-user ID | The ID number of the end user associated with the call. |
| End-user email | The email address of the end user associated with the call. |
| End-user locale | The locale of the end user associated with the call, for example, en-US. |
| End-user status | The status in Zendesk Support of the end user associated with the call. |
| End-user tags | A list of tags associated with the end user for the call. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| End-user time zone | The time zone of the end user associated with the call. |
| Leg agent name | The name of the agent for a specific call leg. |
| Leg agent role | The role of the agent for a specific call leg. |
| Leg agent ID | The unique ID of the agent for a specific call leg. |
| Leg agent email | The email address of the agent for a specific call leg. |
| Leg agent locale | The locale of the agent for a specific call leg |
| Leg agent status | The Zendesk status of the agent for a specific call leg. |
| Leg agent tags | A list of tags associated with the agent for a specific call leg. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Leg agent time zone | The time zone of the agent associated with this leg of the call. |
| Leg user name | The name of the end user for a specific call leg. |
| Leg user role | The role of the end user for a specific call leg. |
| Leg user ID | The unique ID of the end user for a specific call leg. |
| Leg user email | The email address of the end user for a specific call leg. |
| Leg user locale | The locale of the end user for a specific call leg |
| Leg user status | The Zendesk status of the end user for a specific call leg. |
| Leg user tags | A list of tags associated with the end user for a specific call leg. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Leg user time zone | The time zone of the end user associated with this leg of the call. |
| Organization name | The name of the end user organization that initiated the call. |
| Organization ID | The unique ID of the end user organization that initiated the call. |
| Organization domains | The web domain of the end user organization, for example, zendesk.com. |
| Organization status | The Zendesk status of the end user organization that initiated the call. |
| Organization tags | The tags associated with the end user organization. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Call duration brackets | Splits call durations into brackets. Possible values are **0-5 min**, **5-10 min**, **10-20 min**, **20-30 min**, **30-60 min**, **>60 min**, and **Not recorded** (null). |
| Call talk time brackets | Splits call talk time into brackets. Possible values are **0-5 min**, **5-10 min**, **10-20 min**, **20-30 min**, **30-60 min**, **>60 min**, and **Not recorded** (null). |
| Call wait time brackets | Splits call wait time into brackets. Possible values are **0-5 sec**, **5-15 sec**, **15-30 sec**, **30-60 sec**, **60-300 sec**, **>300 sec**, and **Not recorded** (null). |
| Call answer time brackets | Splits call answer time into brackets. Possible values are **0-5 min**, **5-10 min**, **10-20 min**, **20-30 min**, **30-60 min**, **>60 min**, and **Not recorded** (null). |
| Call IVR time brackets | Splits call IVR time into brackets. Possible values are **0-5 min**, **5-10 min**, **10-20 min**, **20-30 min**, **30-60 min**, **>60 min**, and **Not recorded** (null). |
| Call consultation time brackets | Splits any metric by the call consultation time brackets. Possible values are **0-15 sec**, **15-30 sec**, **30-60 sec**, **60-300 sec**, **>300 sec**, and **Not recorded** (null). |
| Call on-hold time brackets | Splits call on-hold time into brackets. Possible values are **0-5 min**, **5-10 min**, **10-20 min**, **20-30 min**, **30-60 min**, **>60 min**, and **Not recorded** (null). |
| Call not recorded time brackets | Splits any metric by the call not recorded time brackets. Possible values are **0-1 min**, **1-2 min**, **2-3 min**, **3-5 min**, **>5 min**, and **Not recorded** (null). |
| Call wrap-up time brackets | Splits any metric by the call wrap-up time brackets. Possible values are **0-1 min**, **1-2 min**, **2-3 min**, **3-5 min**, **5-10 min**, **>10 min**, and **Not recorded** (null). |
| Leg duration brackets | Splits the duration of each call leg into brackets. Possible values are **0-5 min**, **5-10 min**, **10-20 min**, **20-30 min**, **30-60 min**, **>60 min**, and **Not recorded** (null). |
| Let talk time brackets | Splits the duration of each call leg talk time into brackets. Possible values are **0-5 min**, **5-10 min**, **10-20 min**, **20-30 min**, **30-60 min**, **>60 min**, and **Not recorded** (null). |
| Leg consultation time brackets | Splits any metric by the leg consultation time brackets. Possible values are **0-15 sec**, **15-30 sec**, **30-60 sec**, **60-300 sec**, **>300 sec**, and **Not recorded** (null). |
| Leg conference time brackets | Splits any metric by the leg conference time brackets. Possible values are **0-1 min**, **1-2 min**, **2-3 min**, **3-5 min**, **5-10 min**, **>10 min**, and **Not recorded** (null). |
| Leg on-hold time brackets | Splits the duration of each call leg on-hold time into brackets. Possible values are **0-5 min**, **5-10 min**, **10-20 min**, **20-30 min**, **30-60 min**, **>60 min**, and **Not recorded** (null). |
| Leg wrap-up time brackets | Splits the duration of each call leg wrap-up time into brackets. Possible values are **0-5 min**, **5-10 min**, **10-20 min**, **20-30 min**, **30-60 min**, **>60 min**, and **Not recorded** (null). |
| Intent (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what the ticket is about. To see the possible values, [open the Taxonomy tab of the Intent settings page](https://support.zendesk.com/hc/en-us/articles/9488234915610) to see the AI Intents list under the **Taxonomy values** heading. |
| Intent confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the intent prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Language (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what language the ticket is written in. To see the possible values, open the Taxonomy tab of the settings page. |
| Language confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the language prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Sentiment (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of how the customer feels about their request. Possible values are **Very Positive**, **Positive**, **Neutral**, **Negative**, and **Very Negative**. |
| Sentiment confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the sentiment prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Time - Call started | Includes a number of attributes that return the time and date when calls were initiated. |
| Time - Leg started | Includes a number of attributes that return the time and date when call legs were initiated. |
| Time - Ticket created | Includes a number of attributes that return the time and date when tickets were created. |
| Time - Ticket solved | Includes a number of attributes that return the time and date when tickets were solved. |
| Time - Ticket last updated | Includes a number of attributes that return the time and date when tickets were last updated. |