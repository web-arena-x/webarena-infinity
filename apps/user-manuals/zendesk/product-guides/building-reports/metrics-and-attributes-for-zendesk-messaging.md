# Metrics and attributes for Zendesk messaging

Source: https://support.zendesk.com/hc/en-us/articles/4724624097818-Metrics-and-attributes-for-Zendesk-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

Use this article to discover the metrics and attributes you can use to build Explore reports based on your usage of Zendesk messaging and [messaging goals](https://support.zendesk.com/hc/en-us/articles/9435878261402). These datasets are also used for the messaging prebuilt dashboard (see [Overview of the Zendesk Messaging dashboard](https://support.zendesk.com/hc/en-us/articles/4724611131418)).

Note: Zendesk has launched the omnichannel engagements reporting API Early Access Program (EAP). See [this community post](https://support.zendesk.com/hc/en-us/community/posts/8369061705882) for details.

For more information about how to create reports with Explore, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530-Creating-queries).

Tip: On the [dataset selection page](working-with-datasets.md#topic_ig1_whf_5y), the messaging dataset is grouped with the live chat datasets. For more information on the live chat datasets, see [Metrics and attributes for live chat](https://support.zendesk.com/hc/en-us/articles/4409149177242).

This article includes the following datasets:

- [Messaging tickets dataset](#topic_tjl_whb_y5b)
- [Messaging goal conversions dataset](#topic_n5j_4rv_33c)

## Messaging tickets dataset

The Messaging tickets dataset contains metrics and attributes that relate to all messaging channels, including web, mobile, and social messaging channels.

Note: Data is available from September 20, 2022 and after.

This section lists all the available elements for the dataset. It contains the following topics:

- [Messaging tickets metrics](#topic_wjl_whb_y5b)
- [Messaging tickets attributes](#topic_yjl_whb_y5b)

### Messaging tickets metrics

This section lists and defines all the Messaging tickets metrics available.

Note: These metrics will not be computed for any ticket after the [messaging session has ended](https://support.zendesk.com/hc/en-us/articles/8009788438042).

| | | |
| --- | --- | --- |
| **Metric** | **Definition** | **Calculation** |
| Messaging tickets | The total number of tickets created from messaging channels. | [Ticket ID] |
| Solved messaging tickets | The number of solved or closed messaging tickets. | IF ([Ticket status - Unsorted] = "Solved" OR [Ticket status - Unsorted] = "Closed") THEN [Ticket ID] ENDIF |
| One-touch messaging tickets | The number of messaging tickets that were solved in the first interaction, indicated by transitioning from Open to Solved, without going through Pending and On-hold. | IF ([Ticket status - Unsorted] = "Solved" OR [Ticket status - Unsorted] = "Closed") AND VALUE(Agent replies) > 0 AND NOT([Wait status changed]) AND [Reopens] = 0 THEN [Ticket ID] ENDIF |
| % One-touch messaging tickets | The percentage of messaging tickets that were solved in the first interaction, indicated by transitioning from Open to Solved, without going through Pending and On-hold. | COUNT(One-touch messaging tickets) / COUNT(Solved messaging tickets) |
| Unsolved messaging tickets | The number of unsolved messaging tickets. This includes tickets in every status, except Solved and Closed. | IF [Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed" THEN [Ticket ID] ENDIF |
| Unassigned unsolved messaging tickets | The number of unsolved messaging tickets currently not assigned. | IF [Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed" AND [Assignee ID] = NULL THEN [Ticket ID] ENDIF |
| Assigned unsolved messaging tickets | The number of unsolved messaging tickets that are assigned. This includes tickets in every status except Solved and Closed. | IF [Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed" AND [Assignee ID] != NULL THEN [Ticket ID] ENDIF |
| Unreplied unsolved messaging tickets | The number of unsolved messaging tickets that currently have no agent replies. | IF [Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed" AND VALUE(Agent replies) = 0 THEN [Ticket ID] ENDIF |
| Agent messages | The number of messages sent by an agent. | |
| Agent replies | The total number of messaging conversations an agent had with an end user and the number of replies they sent via email. | |
| Requester messages | The number of messages sent by the requester. | |
| Requester replies | The number of replies sent by the requester. Replies are messages sent by the end user in response to an agent message. | |
| Good satisfaction tickets | The number of messaging tickets with a good satisfaction rating. | IF [Ticket satisfaction rating] = "Good" THEN [Ticket ID] ENDIF |
| Bad satisfaction tickets | The number of messaging tickets with a bad satisfaction rating. | IF [Ticket satisfaction rating] = "Bad" THEN [Ticket ID] ENDIF |
| Rated satisfaction tickets | Messaging tickets that were rated either bad or good by the requester. | IF [Ticket satisfaction rating] = "Good" OR [Ticket satisfaction rating] = "Bad" THEN [Ticket ID] ENDIF |
| % Satisfaction score | The percentage of satisfaction surveys rated good. | COUNT(Good satisfaction tickets) / COUNT(Rated satisfaction tickets) |
| First reply time (sec) | The duration in seconds between when the messaging ticket was created and the first agent reply on the ticket. | |
| First reply time (min) | The duration in minutes between when the messaging ticket was created and the first agent reply on the ticket. | VALUE(First reply time (sec))/60 |
| First reply time (hrs) | The duration in hours between when the messaging ticket was created and the first agent reply on the ticket. | VALUE(First reply time (sec))/3600 |
| First reply time (days) | The duration in days between when the messaging ticket was created and the first agent reply on the ticket. | VALUE(First reply time (sec))/86400 |
| First reply time - Business hours (sec) | The time in seconds between when the messaging ticket was created and the first agent reply on the ticket, excluding out-of-business hours. | |
| First reply time - Business hours (min) | The time in minutes between when the messaging ticket was created and the first agent reply on the ticket, excluding out-of-business hours. | VALUE(First reply time - Business hours (sec))/60 |
| First reply time - Business hours (hrs) | The time in hours between when the messaging ticket was created and the first agent reply on the ticket, excluding out-of-business hours. | VALUE(First reply time - Business hours (sec))/3600 |
| First reply time - Business hours (days) | The duration in hours between when the messaging ticket was created and the first agent reply on the ticket, excluding out-of-business hours. | VALUE(First reply time - Business hours (sec))/86400 |
| Requester wait time (sec) | The time in seconds from the end user sending a message and the agent’s response. | |
| Requester wait time (min) | The time in minutes from the end user sending a message and the agent’s response. | VALUE(Requester wait time (sec))/60 |
| Requester wait time (hrs) | The time in hours from the end user sending a message and the agent’s response. | VALUE(Requester wait time (sec))/3600 |
| Requester wait time (days) | The time in days from the end user sending a message and the agent’s response. | VALUE(Requester wait time (sec))/86400 |
| Requester wait time - Business hours (sec) | The time in seconds from the end user sending a message and the agent’s response, excluding out-of-business hours. It measures how long requesters were waiting for agents' replies. | |
| Requester wait time - Business hours (min) | The time in minutes from the end user sending a message and the agent’s response, excluding out-of-business hours. It measures how long requesters were waiting for agents' replies. | VALUE(Requester wait time - Business hours (sec))/60 |
| Requester wait time - Business hours (hrs) | The time in hours from the end user sending a message and the agent’s response, excluding out-of-business hours. It measures how long requesters were waiting for agents' replies. | VALUE(Requester wait time - Business hours (sec))/3600 |
| Requester wait time - Business hours (days) | The time in hours from the end user sending a message and the agent’s response, excluding out-of-business hours. It measures how long requesters were waiting for agents' replies. | VALUE(Requester wait time - Business hours (sec))/86400 |
| Requester wait time average (sec) | The average time in seconds from the end user sending a message and agent’s response. | VALUE(Requester wait time (sec)) / VALUE(Agent replies) |
| Requester wait time average (min) | The average time in minutes from the end user sending a message and the agent’s response. | VALUE(Requester wait time average (sec))/60 |
| Requester wait time average (hrs) | The average time in hours from the end user sending a message and the agent’s response. | VALUE(Requester wait time average (sec))/3600 |
| Requester wait time average (days) | The average time in days from the end user sending a message and the agent’s response. | VALUE(Requester wait time average (sec))/86400 |
| Requester wait time average - Business hours (sec) | The average time in seconds from the end user sending a message and agent’s response, excluding out-of-business hours. | VALUE(Requester wait time - Business hours (sec)) / VALUE(Agent replies) |
| Requester wait time average - Business hours (min) | The average time in minutes from the end user sending a message and the agent’s response, excluding out-of-business hours. | VALUE(Requester wait time average - Business hours (sec))/60 |
| Requester wait time average - Business hours (hrs) | The average time in hours from the end user sending a message and the agent’s response, excluding out-of-business hours. | VALUE(Requester wait time average - Business hours (sec))/3600 |
| Requester wait time average - Business hours (days) | The average time in hours from the end user sending a message and the agent’s response, excluding out-of-business hours. | VALUE(Requester wait time average - Business hours (sec))/86400 |
| Agent wait time (sec) | The time in seconds from the agent sending a message and the end user’s response. It measures how long agents were waiting for end user replies. | |
| Agent wait time (min) | The time in minutes from the agent sending a message and the end user’s response. It measures how long agents were waiting for end user replies. | VALUE(Agent wait time (sec))/60 |
| Agent wait time (hrs) | The time in hours from the agent sending a message and the end user’s response. It measures how long agents were waiting for end user replies. | VALUE(Agent wait time (sec))/3600 |
| Agent wait time (days) | The time in days from the agent sending a message and the end user’s response. It measures how long agents were waiting for end user replies. | VALUE(Agent wait time (sec))/86400 |
| Agent wait time - Business hours (sec) | The time in seconds from the agent sending a message and the end user’s response, excluding out-of-business hours. It measures how long agents were waiting for end user replies. | |
| Agent wait time - Business hours (min) | The time in minutes from the agent sending a message and the end user’s response, excluding out-of-business hours. It measures how long agents were waiting for end user replies. | VALUE(Agent wait time - Business hours (sec))/60 |
| Agent wait time - Business hours (hrs) | The time in hours from the agent sending a message and the end user’s response, excluding out-of-business hours. It measures how long agents were waiting for end user replies. | VALUE(Agent wait time - Business hours (sec))/3600 |
| Agent wait time - Business hours (days) | The time in hours from the agent sending a message and the end user’s response, excluding out-of-business hours. It measures how long agents were waiting for end user replies. | VALUE(Agent wait time - Business hours (sec))/86400 |
| Agent wait time average (sec) | The average time in seconds from the agent sending a message and the end user’s response. It measures how long agents were waiting for end user replies. | VALUE(Agent wait time (sec)) / VALUE(Requester replies) |
| Agent wait time average (min) | The average time in minutes from the agent sending a message and the end user’s response. It measures how long agents were waiting for end user replies. | VALUE(Agent wait time average (sec))/60 |
| Agent wait time average (hrs) | The average time in hours from the agent sending a message and the end user’s response. It measures how long agents were waiting for end user replies. | VALUE(Agent wait time average (sec))/3600 |
| Agent wait time average (days) | The average time in days from the agent sending a message and the end user’s response. It measures how long agents were waiting for end user replies. | VALUE(Agent wait time average (sec))/86400 |
| Agent wait time average - Business hours (sec) | The average time in seconds from the agent sending a message and the end user’s response, excluding out-of-business hours. It measures how long agents were waiting for end user replies. | VALUE(Agent wait time - Business hours (sec)) / VALUE(Requester replies) |
| Agent wait time average - Business hours (min) | The average time in minutes from the agent sending a message and the end user’s response, excluding out-of-business hours. It measures how long agents were waiting for end user replies. | VALUE(Agent wait time average - Business hours (sec))/60 |
| Agent wait time average (hrs) | The average time in hours from the agent sending a message and the end user’s response, excluding out-of-business hours. It measures how long agents were waiting for end user replies. | VALUE(Agent wait time average - Business hours (sec))/3600 |
| Agent wait time average - Business hours (days) | The average time in days from the agent sending a message and the end user’s response, excluding out-of-business hours. It measures how long agents were waiting for end user replies. | VALUE(Agent wait time average - Business hours (sec))/86400 |
| Assignment to first reply (sec) | The time in seconds from last assignment to the first agent reply. | |
| Assignment to first reply (min) | The time in minutes from the last assignment to the first agent reply. | VALUE(Assignment to first reply (sec))/60 |
| Assignment to first reply (hrs) | The time in hours from the last assignment to the first agent reply. | VALUE(Assignment to first reply (sec))/3600 |
| Assignment to first reply (days) | The time in days from the last assignment to the first agent reply. | VALUE(Assignment to first reply (sec))/86400 |
| Assignment to first reply - Business hours (sec) | The time in seconds from last assignment to the first agent reply, excluding out-of-business hours. | |
| Assignment to first reply - Business hours (min) | The time in minutes from the last assignment to the first agent reply, excludes out-of-business hours. | VALUE(Assignment to first reply - Business hours (sec))/60 |
| Assignment to first reply (hrs) | The time in hours from the last assignment to the first agent reply, excluding out-of-business hours. | VALUE(Assignment to first reply - Business hours (sec))/3600 |
| Assignment to first reply - Business hours (days) | The time in days from the last assignment to the first agent reply, excluding out-of-business hours. | VALUE(Assignment to first reply - Business hours (sec))/86400 |
| First resolution time - Messaging (min) | The number of minutes between when the messaging ticket was created and when it was first resolved. | IF [Ticket ID] != NULL THEN VALUE(First resolution time (min)) ENDIF |
| First resolution time - Business hours (min) | The number of minutes between when the messaging ticket was created and when it was first resolved, excluding out-of-business hours. | |
| Full resolution time - Messaging (min) | The duration in minutes from when the messaging ticket was created to its latest resolution. | IF [Ticket ID] != NULL THEN VALUE(Full resolution time (min)) ENDIF |
| Full resolution time - Business hours (min) | The duration in minutes from when the messaging ticket was created to its latest resolution, excluding out-of-business hours. | |
| Unsolved tickets age (min) | The duration in minutes between when an unsolved messaging ticket was created and now. | IF [Ticket ID] != NULL AND [Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed" THEN DATE\_DIFF(NOW(), [Ticket created - Timestamp], "nb\_of\_minutes") ENDIF |
| Unsolved tickets age (hrs) | The duration in hours between when an unsolved messaging ticket was created and now. | IF [Ticket ID] != NULL AND [Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed" THEN DATE\_DIFF(NOW(), [Ticket created - Timestamp], "nb\_of\_hours") ENDIF |
| Unsolved tickets age (days) | The duration in days between when an unsolved messaging ticket was created and now. | IF [Ticket ID] != NULL AND [Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed" THEN DATE\_DIFF(NOW(), [Ticket created - Timestamp], "nb\_of\_days") ENDIF |
| Unsolved tickets time since update (min) | The duration in minutes between an unsolved messaging ticket’s last update and now. | IF [Ticket ID] != NULL AND [Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed" THEN DATE\_DIFF(NOW(), [Ticket updated - Timestamp], "nb\_of\_minutes") ENDIF |
| Unsolved tickets time since update (hrs) | The duration in hours between an unsolved messaging ticket’s last update and now. | IF [Ticket ID] != NULL AND [Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed" THEN DATE\_DIFF(NOW(), [Ticket updated - Timestamp], "nb\_of\_hours") ENDIF |
| Unsolved tickets time since update (days) | The duration in days between an unsolved messaging ticket’s last update and now. | IF [Ticket ID] != NULL AND [Ticket status - Unsorted] != "Solved" AND [Ticket status - Unsorted] != "Closed" THEN DATE\_DIFF(NOW(), [Ticket updated - Timestamp], "nb\_of\_days") ENDIF |
| Reassigned messaging tickets | The number of messaging tickets that have been assigned to more than one agent. Data is available only from July 18, 2023 and after. | IF VALUE(Assignee stations) > 1 THEN [Ticket ID] ENDIF |
| Reopened messaging tickets | The number of messaging tickets that were reopened after being solved. Data is available only from July 18, 2023 and after. | IF [Reopens] > 0 THEN [Ticket ID] ENDIF |
| Messaging tickets created outside of business hours | The number of messaging tickets created outside of the schedule assigned at the time of ticket creation. Data is available only from July 18, 2023 and after. | IF [Created outside business hours] THEN [Ticket ID] ENDIF |
| New messaging tickets | The number of messaging tickets that are currently in the New status. Data is available only from July 18, 2023 and after. | IF [Ticket status - Unsorted] = "New" THEN [Ticket ID] ENDIF |
| Open messaging tickets | The number of messaging tickets that are currently in the Open status. Data is available only from July 18, 2023 and after. | IF [Ticket status - Unsorted] = "Open" THEN [Ticket ID] ENDIF |
| Pending messaging tickets | The number of messaging tickets that are currently in the Pending status. Data is available only from July 18, 2023 and after. | IF [Ticket status - Unsorted] = "Pending" THEN [Ticket ID] ENDIF |
| On-hold messaging tickets | The number of messaging tickets that are currently in the On-hold status. Data is available only from July 18, 2023 and after. | IF [Ticket status - Unsorted] = "Hold" THEN [Ticket ID] ENDIF |
| First assignment time (sec) | The time in seconds between when a messaging ticket was created and the first time it was assigned to an agent. Data is available only from July 18, 2023 and after. | IF [Ticket ID] != NULL THEN DATE\_DIFF([Ticket first assigned - Timestamp], [Ticket created - Timestamp], "nb\_of\_seconds") ENDIF |
| First assignment time (min) | The time in minutes between when a messaging ticket was created and the first time it was assigned to an agent. Data is available only from July 18, 2023 and after. | IF [Ticket ID] != NULL THEN DATE\_DIFF([Ticket first assigned - Timestamp], [Ticket created - Timestamp], "nb\_of\_minutes") ENDIF |
| First assignment time (hrs) | The time in hours between when a messaging ticket was created and the first time it was assigned to an agent. Data is available only from July 18, 2023 and after. | IF [Ticket ID] != NULL THEN DATE\_DIFF([Ticket first assigned - Timestamp], [Ticket created - Timestamp], "nb\_of\_hours") ENDIF |
| First assignment time (days) | The time in days between when a messaging ticket was created and the first time it was assigned to an agent. Data is available only from July 18, 2023 and after. | IF [Ticket ID] != NULL THEN DATE\_DIFF([Ticket first assigned - Timestamp], [Ticket created - Timestamp], "nb\_of\_days") ENDIF |
| Handle time (sec) | The time in seconds that the agent spends interacting with the end user on the messaging ticket. For details, see [How is the Handle time metric calculated?](https://support.zendesk.com/hc/en-us/articles/5940001113754) Data is available only from July 18, 2023 and after. | |
| Handle time (min) | The time in minutes that the agent spends interacting with the end user on the messaging ticket. For details, see [How is the Handle time metric calculated?](https://support.zendesk.com/hc/en-us/articles/5940001113754) Data is available only from July 18, 2023 and after. | |
| Handle time (hrs) | The time in hours that the agent spends interacting with the end user on the messaging ticket. For details, see [How is the Handle time metric calculated?](https://support.zendesk.com/hc/en-us/articles/5940001113754) Data is available only from July 18, 2023 and after. | |
| Handle time (days) | The time in days that the agent spends interacting with the end user on the messaging ticket. For details, see [How is the Handle time metric calculated?](https://support.zendesk.com/hc/en-us/articles/5940001113754) Data is available only from July 18, 2023 and after. | |
| Handle time - Business hours (sec) | The time in seconds that the agent spends interacting with the end user on the messaging ticket, excluding non-business hours. Business hours are based on the schedule applied to the ticket at the time of creation. For details, see [How is the Handle time metric calculated?](https://support.zendesk.com/hc/en-us/articles/5940001113754) Data is available only from July 18, 2023 and after. | |
| Handle time - Business hours (min) | The time in minutes that the agent spends interacting with the end user on the messaging ticket, excluding non-business hours. Business hours are based on the schedule applied to the ticket at the time of creation. For details, see [How is the Handle time metric calculated?](https://support.zendesk.com/hc/en-us/articles/5940001113754) Data is available only from July 18, 2023 and after. | |
| Handle time - Business hours (hrs) | The time in hours that the agent spends interacting with the end user on the messaging ticket, excluding non-business hours. Business hours are based on the schedule applied to the ticket at the time of creation. For details, see [How is the Handle time metric calculated?](https://support.zendesk.com/hc/en-us/articles/5940001113754) Data is available only from July 18, 2023 and after. | |
| Handle time - Business hours (days) | The time in days that the agent spends interacting with the end user on the messaging ticket, excluding non-business hours. Business hours are based on the schedule applied to the ticket at the time of creation. For details, see [How is the Handle time metric calculated?](https://support.zendesk.com/hc/en-us/articles/5940001113754) Data is available only from July 18, 2023 and after. | |
| Assignee stations | The number of agents a ticket has been assigned to. Data is available only from July 18, 2023 and after. | (Assignee stations) |
| First offer time (sec) | The time in seconds from ticket creation to the first time it was offered to an agent to accept. Data is available only from October 30, 2023 and after. | First offer time (sec) |
| First offer to assignment (sec) | The time spent in an offer state, in seconds, between first offer and first assignment to an agent. It will be 0 if the first assignment occurred before offering, either by directly assigning the ticket to the agents via triggers or manually. Data is available only from October 30, 2023 and after. | IF VALUE(First assignment time (sec)) - VALUE(First offer time (sec)) < 0 THEN NULL ELSE VALUE(First assignment time (sec)) - VALUE(First offer time (sec)) ENDIF |
| First offer time (min) | The time in minutes from ticket creation to the first time it was offered to an agent to accept. Data is available only from October 30, 2023 and after. | VALUE(First offer time (sec))/60 |
| First offer to assignment (min) | The time spent in an offer state, in minutes, between first offer and first assignment to an agent. It will be 0 if the first assignment occurred before offering, either by directly assigning the ticket to the agents via triggers or manually. Data is available only from October 30, 2023 and after. | IF VALUE(First assignment time (sec)) - VALUE(First offer time (sec)) < 0 THEN NULL ELSE (VALUE(First assignment time (sec)) - VALUE(First offer time (sec)))/60 ENDIF |
| First offer time (hrs) | The time in hours from ticket creation to the first time it was offered to an agent to accept. Data is available only from October 30, 2023 and after. | VALUE(First offer time (sec))/3600 |
| First offer to assignment (hrs) | The time spent in an offer state, in hours, between first offer and first assignment to an agent. It will be 0 if the first assignment occurred before offering, either by directly assigning the ticket to the agents via triggers or manually. Data is available only from October 30, 2023 and after. | IF VALUE(First assignment time (sec)) - VALUE(First offer time (sec)) < 0 THEN NULL ELSE (VALUE(First assignment time (sec)) - VALUE(First offer time (sec)))/3600 ENDIF |
| First offer time (days) | The time in days from ticket creation to the first time it was offered to an agent to accept. Data is available only from October 30, 2023 and after. | VALUE(First offer time (sec))/86400 |
| First offer to assignment (days) | The time spent in an offer state, in days, between first offer and first assignment to an agent. It will be 0 if the first assignment occurred before offering, either by directly assigning the ticket to the agents via triggers or manually. Data is available only from October 30, 2023 and after. | IF VALUE(First assignment time (sec)) - VALUE(First offer time (sec)) < 0 THEN NULL ELSE (VALUE(First assignment time (sec)) - VALUE(First offer time (sec)))/86400 ENDIF |
| First assignment time - Business hours (sec) | The time in seconds between when a messaging ticket was created and the first time it was assigned to an agent, excluding out-of-business hours. Business hours are based on the schedule applied at time of first assignment. If there is no schedule assigned, the default schedule is used. Data is available only from October 30, 2023 and after. | First assignment time - Business hours (sec) |
| First offer time - Business hours (sec) | The time in seconds from ticket creation to the first time it was offered to an agent to accept, excluding out-of-business hours. Business hours are based on the schedule applied at time of first offer. If there is no schedule assigned, the default schedule is used. Data is available only from October 30, 2023 and after. | First offer time - Business hours (sec) |
| First offer to assignment - Business hours (sec) | The time spent in an offer state, in seconds, between first offer and first assignment to an agent, excluding out-of-business hours. It will be 0 if the first assignment occurred before offering, either by directly assigning the ticket to the agents via triggers or manually. Business hours are based on the schedule applied at time of first assignment. If there is no schedule assigned, the default schedule is used. Data is available only from October 30, 2023 and after. | IF VALUE(First assignment time - Business hours (sec)) - VALUE(First offer time - Business hours (sec)) < 0 THEN NULL ELSE (VALUE(First assignment time - Business hours (sec)) - VALUE(First offer time - Business hours (sec))) ENDIF |
| First assignment time - Business hours (mins) | The time in minutes between when a messaging ticket was created and the first time it was assigned to an agent, excluding out-of-business hours. Business hours are based on the schedule applied at time of first assignment. If there is no schedule assigned, the default schedule is used. Data is available only from October 30, 2023 and after. | First assignment time - Business hours (sec)/60 |
| First offer time - Business hours (mins) | The time in minutes from ticket creation to the first time it was offered to an agent to accept, excluding out-of-business hours. Business hours are based on the schedule applied at time of first offer. If there is no schedule assigned, the default schedule is used. Data is available only from October 30, 2023 and after. | VALUE(First offer time - Business hours (sec))/60 |
| First offer to assignment - Business hours (min) | The time spent in an offer state, in minutes, between first offer and first assignment to an agent, excluding out-of-business hours. It will be 0 if the first assignment occurred before offering, either by directly assigning the ticket to the agents via triggers or manually. Business hours are based on the schedule applied at time of first assignment. If there is no schedule assigned, the default schedule is used. Data is available only from October 30, 2023 and after. | IF VALUE(First assignment time - Business hours (sec)) - VALUE(First offer time - Business hours (sec)) < 0 THEN NULL ELSE (VALUE(First assignment time - Business hours (sec)) - VALUE(First offer time - Business hours (sec)))/60 ENDIF |
| First assignment time - Business hours (hours) | The time in hours between when a messaging ticket was created and the first time it was assigned to an agent, excluding out-of-business hours. Business hours are based on the schedule applied at time of first assignment. If there is no schedule assigned, the default schedule is used. Data is available only from October 30, 2023 and after. | First assignment time - Business hours (sec)/3600 |
| First offer time - Business hours (hrs) | The time in hours from ticket creation to the first time it was offered to an agent to accept, excluding out-of-business hours. Business hours are based on the schedule applied at time of first offer. If there is no schedule assigned, the default schedule is used. Data is available only from October 30, 2023 and after. | VALUE(First offer time - Business hours (sec))/3600 |
| First offer to assignment - Business hours (hrs) | The time spent in an offer state, in hours, between first offer and first assignment, excluding out-of-business hours to an agent. It will be 0 if the first assignment occurred before offering, either by directly assigning the ticket to the agents via triggers or manually. Business hours are based on the schedule applied to the ticket at the time of creation. Data is available only from October 30, 2023 and after. | IF VALUE(First assignment time - Business hours (sec)) - VALUE(First offer time - Business hours (sec)) < 0 THEN NULL ELSE (VALUE(First assignment time - Business hours (sec)) - VALUE(First offer time - Business hours (sec)))/3600 ENDIF |
| First assignment time - Business hours (days) | The time in days between when a messaging ticket was created and the first time it was assigned to an agent, excluding out-of-business hours. Business hours are based on the schedule applied at time of first assignment. If there is no schedule assigned, the default schedule is used. Data is available only from October 30, 2023 and after. | First assignment time - Business hours (sec)/86400 |
| First offer time - Business hours (days) | The time in days from ticket creation to the first time it was offered to an agent to accept, excluding out-of-business hours. Business hours are based on the schedule applied at time of first offer. If there is no schedule assigned, the default schedule is used. Data is available only from October 30, 2023 and after. | VALUE(First offer time - Business hours (sec))/86400 |
| First offer to assignment - Business hours (days) | The time spent in an offer state, in days, between first offer and first assignment to an agent, excluding out-of-business hours. It will be 0 if the first assignment occurred before offering, either by directly assigning the ticket to the agents via triggers or manually. Business hours are based on the schedule applied at time of first assignment. If there is no schedule assigned, the default schedule is used. Data is available only from October 30, 2023 and after. | IF VALUE(First assignment time - Business hours (sec)) - VALUE(First offer time - Business hours (sec)) < 0 THEN NULL ELSE (VALUE(First assignment time - Business hours (sec)) - VALUE(First offer time - Business hours (sec)))/86400 ENDIF |
| Messaging tickets with multiple offers | The number of messaging tickets offered to an agent, not accepted, and re-offered to other agents. If the ticket was never accepted, this metric returns 0. Data is available only from October 30, 2023 and after. | IF (VALUE(Offers before first acceptance) != NULL AND VALUE(Offers before first acceptance) > 1) THEN [Ticket ID] ENDIF |
| Offers | The number of times a messaging ticket was offered to agents during its lifecycle. Explore records a maximum of 20 offers per ticket. Data is available only from October 30, 2023 and after. | |
| Offers before first acceptance | The number of times a messaging ticket was offered to agents before first acceptance. If a ticket was directly assigned to an agent using triggers or manually, this value will be null. Data is available only from October 30, 2023 and after. | |
| Acceptances | The number of times a messaging ticket was accepted by agents clicking the Accept button. Data is available only from October 30, 2023 and after. Note: Starting December 11, 2023, auto-assignment to agents as part of omnichannel routing is excluded from this metric. Note: Starting July 2, 2024, auto-accept by agents is excluded from this metric. | |
| Queue entries | The number of times the ticket was placed in the queue. A ticket is in the queue when it’s in a status of New or Open and unassigned. Data is available only from October 30, 2023 and after. | |
| % First acceptance rate | The percentage of acceptances from the number of offers before first acceptance on the ticket. One hundred percent indicates that the ticket was accepted by the first agent it was offered to. Less than one hundred percent indicates that the ticket was offered to multiple agents before it was first accepted, resulting in an increase in first reply time. Data is available only from October 30, 2023 and after. | IF (VALUE(Offers before first acceptance) != NULL AND VALUE(Offers before first acceptance) > 0) THEN 1/VALUE(Offers before first acceptance) ELSE 0 ENDIF |
| % Acceptance rate | The percentage of acceptances of all offers on the ticket. One hundred percent indicates the ticket was accepted by all the agents it was offered to. Less than one hundred percent indicates that the ticket was offered to multiple agents before it was accepted, resulting in an increase in resolution time. Data is available only from October 30, 2023 and after. | IF VALUE(Offers) > 0 THEN MINIMUM(VALUE(Acceptances)/VALUE(Offers), 1) ELSE 0 ENDIF |
| Messaging tickets with session ended | Number of messaging tickets where a [messaging session ended](../zendesk-messaging/about-ending-messaging-sessions.md). Data is available only from September 30 , 2025 and after. | |
| Messaging tickets with routing channel changed | Number of messaging tickets where the [routing channel changed from messaging to email](https://support.zendesk.com/hc/en-us/articles/8993549728154). Data is available only from September 30 , 2025 and after. | |
| Session end time (sec) | The time in seconds between when a messaging ticket was created and the [messaging session ended](../zendesk-messaging/about-ending-messaging-sessions.md). Data is available only from September 29, 2025 and after. | |
| Routing channel change time (sec) | The time in seconds between when a messaging ticket was created and the [routing channel was updated from messaging to email.](https://support.zendesk.com/hc/en-us/articles/8993549728154-Announcing-the-option-to-route-messaging-conversations-as-email-tickets-with-omnichannel-routing) Data is available only from September 29, 2025 and after. | |
| Session end time (min) | The time in minutes between when a messaging ticket was created and the [messaging session ended](../zendesk-messaging/about-ending-messaging-sessions.md). Data is available only from September 29, 2025 and after. | VALUE(Session end time (sec))/60 |
| Routing channel change time (min) | The time in minutes between when a messaging ticket was created and the [routing channel was updated from messaging to email.](https://support.zendesk.com/hc/en-us/articles/8993549728154-Announcing-the-option-to-route-messaging-conversations-as-email-tickets-with-omnichannel-routing) Data is available only from September 29, 2025 and after. | VALUE(Routing channel change time (sec) )/60 |
| Session end time (hrs) | The time in hours between when a messaging ticket was created and the [messaging session ended](../zendesk-messaging/about-ending-messaging-sessions.md). Data is available only from September 29, 2025 and after. | VALUE(Session end time (sec))/3600 |
| Routing channel change time (hrs) | The time in hours between when a messaging ticket was created and the [routing channel was updated from messaging to email.](https://support.zendesk.com/hc/en-us/articles/8993549728154-Announcing-the-option-to-route-messaging-conversations-as-email-tickets-with-omnichannel-routing) Data is available only from September 29, 2025 and after. | VALUE(Routing channel change time (sec) )/3600 |
| Session end time (days) | The time in days between when a messaging ticket was created and the [messaging session ended](../zendesk-messaging/about-ending-messaging-sessions.md). Data is available only from September 29, 2025 and after. | VALUE(Session end time (sec))/86400 |
| Routing channel change time (days) | The time in days between when a messaging ticket was created and the [routing channel was updated from messaging to email.](https://support.zendesk.com/hc/en-us/articles/8993549728154-Announcing-the-option-to-route-messaging-conversations-as-email-tickets-with-omnichannel-routing) Data is available only from September 29, 2025 and after. | VALUE(Routing channel change time (sec) )/86400 |
| Session end time - Business hours (sec) | The time in seconds between when a messaging ticket was created and [messaging session ended](../zendesk-messaging/about-ending-messaging-sessions.md), excluding out-of-business hours. Business hours are based on the schedule applied at time of first assignment. If there is no schedule assigned, the default schedule is used. Data is available only from September 29, 2025 and after. | |
| Routing channel change time - Business hours (sec) | The time in seconds between when a messaging ticket was created and the [routing channel was updated from messaging to email](https://support.zendesk.com/hc/en-us/articles/8993549728154-Announcing-the-option-to-route-messaging-conversations-as-email-tickets-with-omnichannel-routing), excluding out-of-business hours. Business hours are based on the schedule applied at time of first assignment. If there is no schedule assigned, the default schedule is used. Data is available only from September 29, 2025 and after. | |
| Session end time - Business hours (min) | The time in minutes between when a messaging ticket was created and the [messaging session ended](../zendesk-messaging/about-ending-messaging-sessions.md), excluding out-of-business hours. Business hours are based on the schedule applied at time of first assignment. If there is no schedule assigned, the default schedule is used. Data is available only from September 29, 2025 and after. | VALUE(Session end time - Business hours (sec))/60 |
| Routing channel change time - Business hours (min) | The time in minutes between when a messaging ticket was created and the [routing channel was updated from messaging to email](https://support.zendesk.com/hc/en-us/articles/8993549728154-Announcing-the-option-to-route-messaging-conversations-as-email-tickets-with-omnichannel-routing), excluding out-of-business hours. Business hours are based on the schedule applied at time of first assignment. If there is no schedule assigned, the default schedule is used. Data is available only from September 29, 2025 and after. | VALUE(Routing channel change time - Business hours (sec))/60 |
| Session end time - Business hours (hrs) | The time in hours between when a messaging ticket was created and [messaging session ended](../zendesk-messaging/about-ending-messaging-sessions.md), excluding out-of-business hours. Business hours are based on the schedule applied at time of first assignment. If there is no schedule assigned, the default schedule is used. Data is available only from September 29, 2025 and after. | VALUE(Session end time - Business hours (sec))/3600 |
| Routing channel change time - Business hours (hrs) | The time in hours between when a messaging ticket was created and the [routing channel was updated from messaging to email](https://support.zendesk.com/hc/en-us/articles/8993549728154-Announcing-the-option-to-route-messaging-conversations-as-email-tickets-with-omnichannel-routing), excluding out-of-business hours. Business hours are based on the schedule applied at time of first assignment. If there is no schedule assigned, the default schedule is used. Data is available only from September 29, 2025 and after. | VALUE(Routing channel change time - Business hours (sec))/3600 |
| Session end time - Business hours (days) | The time in days between when a messaging ticket was created and [messaging session ended](../zendesk-messaging/about-ending-messaging-sessions.md), excluding out-of-business hours. Business hours are based on the schedule applied at time of first assignment. If there is no schedule assigned, the default schedule is used. Data is available only from September 29, 2025 and after. | VALUE(Session end time - Business hours (sec))/86400 |
| Routing channel change time - Business hours (days) | The time in days between when a messaging ticket was created and the [routing channel was updated from messaging to email](https://support.zendesk.com/hc/en-us/articles/8993549728154-Announcing-the-option-to-route-messaging-conversations-as-email-tickets-with-omnichannel-routing), excluding out-of-business hours. Business hours are based on the schedule applied at time of first assignment. If there is no schedule assigned, the default schedule is used. Data is available only from September 29, 2025 and after. | VALUE(Routing channel change time - Business hours (sec))/86400 |

### Messaging tickets attributes

This section lists and defines all the Messaging tickets attributes available.

| | |
| --- | --- |
| **Attribute** | **Definition** |
| Ticket ID | The ID number of the messaging ticket. |
| Ticket status | The status of the messaging ticket. |
| Ticket custom status name | The name of a custom ticket status. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). For tickets that existed before custom ticket statuses were enabled, this attribute returns **NULL**. Data is available only from October 19, 2023 onward. |
| Ticket custom status category | The category that a custom ticket status is mapped to. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). For tickets that existed before custom ticket statuses were enabled, this attribute returns **Ticket Status**. Data is available only from October 19, 2023 onward. |
| Ticket custom status state | Returns **true** if a custom ticket status is active, or **false** if a custom ticket status is deactivated. This attribute appears only if you've [enabled custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306). Data is available only from October 19, 2023 onward. |
| Ticket group | Name of the group where the messaging ticket was assigned. |
| Ticket brand | The brand of the messaging ticket. |
| Ticket channel | The channel a messaging ticket was created from. For more information about the ticket channels Explore collects, see [Understanding ticket channels in Explore](https://support.zendesk.com/hc/en-us/articles/4408836378394). |
| Ticket priority | The messaging ticket's priority. |
| Ticket tags | The tags associated with the messaging ticket. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket satisfaction rating | The satisfaction rating left by the customer on the messaging ticket. Values: Good, Bad, Offered, Unoffered. |
| Wait status changed | Returns **true** or **false** depending on whether a ticket has previously gone into the Pending or On-hold status. |
| Assignee name | The name of the assignee. Values for this attribute (and for the other Assignee attributes below) include users who currently have an agent or admin role, as well as users who previously had an agent or admin role and were assigned to a ticket at least once. |
| Assignee role | The role of an assignee. Possible values: admin, agent, or end user. |
| Assignee ID | The messaging ticket's assignee ID. |
| Assignee email | The messaging ticket assignee’s email address. |
| Requester name | The name of the user who is asking for support through a messaging ticket. |
| Requester ID | The ID number for a messaging ticket's requester. |
| Requester email | The email address of the messaging ticket requester. |
| Requester tags | Tags associated with the requester. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket organization name | The name of the organization associated with the messaging ticket. |
| First reply time brackets | The time between when the messaging ticket was first created and when an agent first replied. Values are returned as **0-1 mins**, **1-3 mins**, **3-10 mins**, **>10 mins**, and **no replies.** |
| Requester wait time brackets | The time a requester was waiting for agent replies. The values are returned as **no wait**, **0-1 mins**, **1-3 mins**, **3-10 mins**, **10-30 mins**, and **>30 mins.** |
| First resolution time brackets | The time between when the messaging ticket was first created and the first time it was set to solved. The values are returned as **Unsolved**, **0-30 mins**, **30-90 mins**, **1.5-6 hrs**, **6-24 hrs**, and **>24 hrs**. |
| Intent (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what the ticket is about. To see the possible values, [open the Taxonomy tab of the Intent settings page](https://support.zendesk.com/hc/en-us/articles/9488234915610) to see the AI Intents list under the **Taxonomy values** heading. |
| Intent confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the intent prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Language (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what language the ticket is written in. To see the possible values, open the Taxonomy tab of the settings page. |
| Language confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the language prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Sentiment (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of how the customer feels about their request. Possible values are **Very Positive**, **Positive**, **Neutral**, **Negative**, and **Very Negative**. |
| Sentiment confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the sentiment prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Time - Ticket created | Includes a number of attributes that return the time and date when the messaging ticket was created in various time measurements. |
| Time - Ticket solved | Includes a number of attributes that return the time and date when the messaging ticket was marked as solved in various time measurements. |
| Time - Ticket last updated | The time when the messaging ticket was last updated. |
| Time - Ticket requester updated | The time when the messaging ticket was last updated by its requester. |
| Time - Ticket last assigned | The time when the messaging ticket was last assigned to an agent. |
| Time - Ticket first assigned | The time when the messaging ticket was first assigned to an agent. |
| Time - Ticket type - Task due | When a messaging ticket is configured as a task, this is the date at which the task must be completed. |
| Custom ticket fields | The name of a custom ticket field. This attribute appears only if you’ve [created custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4408883152794). Data is available only from July 18, 2023 and after. |
| Created outside business hours | Indicates whether a ticket was created within (FALSE) or outside of (TRUE) business hours based on the schedule applied to the messaging ticket at the time of ticket creation. Data is available only from July 18, 2023 and after. |
| Session ended | Indicates whether the messaging ticket had a [session end](../zendesk-messaging/about-ending-messaging-sessions.md) or not. Data is available only from September 29, 2025 and after. |
| Session ended reason | Indicates the reason for [messaging session ended](../zendesk-messaging/about-ending-messaging-sessions.md) - agent ended the session, session ended by trigger or session ended due to channel change. Data is available only from September 29, 2025 and after. |
| Routing channel changed | Indicates whether the [routing channel changes from messaging to email](https://support.zendesk.com/hc/en-us/articles/8993549728154-Announcing-the-option-to-route-messaging-conversations-as-email-tickets-with-omnichannel-routing), when the messaging session ended. Data is available only from September 29, 2025 and after. |

### Messaging goal conversions dataset

This section includes the metrics and attributes you can use to build Explore reports based on goal conversion for messaging. See [Analyzing your messaging tickets](../zendesk-messaging/analyzing-your-messaging-tickets.md).

For more information about how to create reports with Explore, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530-Creating-queries).

This article includes the following topics:

- [Goal conversion metrics](#topic_kfw_prv_33c)
- [Goal conversion attributes](#topic_inw_trv_33c)

#### Goal conversion metrics

This section lists and defines all the goal conversion metrics available.

Note: To calculate the messaging goal conversion rate, divide Total conversions by the total number of messaging conversations.

| | | |
| --- | --- | --- |
| **Attribute** | **Definition** | **Calculation** |
| Total conversions | The total number of Goal conversions. | COUNT(Goal conversions) |
| Total transaction value | The total transaction value from Goal conversion events. | VALUE(Total amount collected from Sales from Goal conversion events) |
| % Satisfaction score | The percentage of satisfaction surveys rated good for tickets with Goal conversions. | COUNT(Good satisfaction tickets) / COUNT(Rated satisfaction tickets) |
| Conversion time | The time in seconds that the agent spends interacting with the end user on the messaging ticket until the Goal has been reached. | VALUE(Goal conversion achievement time - The agent is first assigned to the ticket) |

#### Goal conversion attributes

This section lists and defines all the goal conversion attributes available.

| | |
| --- | --- |
| **Attribute** | **Definition** |
| Goal name | The name of the Goal. |
| Ticket Id(s)> multiple | The system ID of the Ticket. |
| Agent assigned Id | The ID of the agent. |
| Agent assigned name | The name of the agent. |
| Agent assigned email | The email address of the agent. |
| Conversion time brackets | The time in seconds that the agent spends interacting with the end user on the messaging ticket until the Goal has been reached. Values are returned as 0-1 mins, 1-3 mins, 3-10 mins, >10 mins, and no replies. |
| Ticket satisfaction rating | The satisfaction rating left by the customer on the messaging ticket. Values: Good, Bad, Offered, Unoffered. |
| group\_id | Id of the group the goal was assigned to |
| brand\_id | ID of the brand the goal was assigned to |