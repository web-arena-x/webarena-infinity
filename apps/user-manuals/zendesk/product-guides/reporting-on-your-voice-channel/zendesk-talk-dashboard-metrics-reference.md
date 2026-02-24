# Zendesk Talk dashboard metrics reference

Source: https://support.zendesk.com/hc/en-us/articles/4408883025690-Zendesk-Talk-dashboard-metrics-reference

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

This article lists and defines the metrics used in the Talk dashboard. For details about the
dashboard, see [Analyzing call activity with the Talk Team dashboard](https://support.zendesk.com/hc/en-us/articles/4408821396762)
and [Analyzing call activity with the Talk Professional dashboard](https://support.zendesk.com/hc/en-us/articles/4408831823514).

Note: You might sometimes see differences in results between the Explore live dashboard and
the Talk live calls dashboard. To learn why these can occur, see [Discrepancies between the Talk Live calls dashboard and the
Explore Enterprise live dashboard](https://support.zendesk.com/hc/en-us/articles/4408828509210).

This article lists reports in the following sections:

- [Current queue activity](#topic_ond_2rw_bpb)
- [Overview](#topic_dyk_2rw_bpb)
- [Agent activity](#topic_qyl_2rw_bpb)

## Current queue activity

| **Metric** | **Definition** |
| --- | --- |
| Total calls in queue | Number of calls waiting for an agent in the queue, including caller on the line and callback requests |
| Callbacks in queue (Professional and Enterprise plans) | Number of calls waiting for callback in the queue including requests from the API |
| Widget callbacks in queue | Number of callback requests coming in the from Web Widget (Classic) |
| Agents online | Number of agents online and available for calls. Note: Agents in the away state are counted as online. Calls are routed to agents in the away state, but they are placed in the queue for an agent who is available to answer. |
| Average wait time | Average wait time for customers currently waiting in the queue. Excludes Available agents greeting. |
| Longest wait time | Longest time any customer has currently been waiting for an agent in the queue |

## Overview

| Metric | Definition |
| --- | --- |
| Total calls | Total number of inbound and outbound calls |
| Total callback calls (Professional and Enterprise plans) | Number of callback request (successful or not) for the day |
| Total widget callback calls | Number of successful callback requests (successful or not) for the day made through Web Widget (Classic) |
| Total text back requests (Professional and Enterprise plans) | Total number of text back messages sent from IVR |
| Total inbound calls (Professional and Enterprise plans) | Total number of inbound calls |
| Total outbound calls (Professional and Enterprise plans) | Total number of outbound calls |
| Total calls in queue | Number of calls queued |
| Max calls waiting | Maximum number of calls waiting at any point in the specified window |
| Abandoned in queue (Professional and Enterprise plans) | Total number of calls where customer hung up while waiting in the queue |
| Exceeded queue wait time (Professional and Enterprise plans) | Total number of calls sent to voicemail after exceeding the max wait time in the queue |
| Voicemail | Total number of calls that went to voicemail for any reason |
| Outside business hours (Professional and Enterprise plans) | Total number of calls received outside business hours |
| Customer requested voicemail (Professional and Enterprise plans) | Number of calls where customer requested to be put through to voicemail by dialing 1 |
| Average callback wait time (Professional and Enterprise plans) | Average callback time a customer has been waiting for an agent in the queue. Excludes Available agents greeting. |
| Average wait time | Calculates all calls that have passed the initial greeting and averages those times throughout the day from 00:00 - 23:59. Excludes Available agents greeting. |
| Average time to answer (Professional and Enterprise plans) | Average time between system answering a call and customer being connected with an agent. Includes greetings and other recordings played. |
| Average duration time | Average length of call |
| Average hold time (Professional and Enterprise plans) | Average time spent on hold per call (based only on calls where hold is used at least once) |
| Average wrap-up time | Average wrap-up time across all calls |

## Agent activity

| Metric | Definition |
| --- | --- |
| Agent | The name of the agent |
| Agents online | The number of agents online within a specified timeframe |
| Status | The current online status of the agent |
| Total online time | Total time the agent was on a call, in wrap-up mode, or online. |
| Time available | Total time the agent was available to answer calls and set to Online. Does not include time on calls or in wrap-up mode. |
| Total away time | Total time the agent was in the Away status. |
| Average talk time (Professional and Enterprise plans) | Average talk time across all calls (excludes hold time and consultation) |
| Total talk time | Total talk time (excludes hold time and consultation) |
| Average hold time (Professional and Enterprise plans) | Average time spent on hold per call (based only on calls where hold is used at least once) |
| Total hold time | Total time with calls on hold |
| Calls accepted | Total number of calls the agent answered. The results of this metric might differ from the [Accepted call legs metric](https://support.zendesk.com/hc/en-us/articles/4409156145434-Metrics-and-attributes-for-Zendesk-Talk#:~:text=quality%20agent%20legs))-,Accepted%20call%20legs,-The%20number%20of) in the Talk - Calls dataset in Explore. |
| Number of calls transferred | Total number of calls the agent transferred to someone else |
| Transfers accepted | Total number of transfers the agent accepted. This metric reflects transfers to a specific agent. It does not reflect transfers to a group of agents. |
| Calls missed | Total number of calls that rang for 30 seconds with no response and were placed back in the queue |
| Calls declined | Total number of incoming calls where agent clicked **Decline** in the given time period |
| Calls put on hold | Total number of calls placed on hold |
| Average wrap up time | Average wrap-up time across all calls |
| Total wrap up time | Total time spent in wrap-up across all calls |