# Chat Analytics CSV glossary

Source: https://support.zendesk.com/hc/en-us/articles/4408893283098-Chat-Analytics-CSV-glossary

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Professional or Enterprise |

This article contains a glossary of metrics used in Analytics. These terms are used in the following reports:

- [Agent activity](#h_01F2SEA6XR7747DTPCM44K4XFT)
- [Chat activity](#h_01F2SEAH3VR3PEP0904HSYQP4X)
- [Log in times](#h_01F2SEAX9XK8QP3JCM2ZT1AY3X)
- [Serving times](#h_01F2SEB6X5A7ZN48ASA94T3385)
- [Status sessions](#Status)
- [Agent and chat activity by department](#h_01F2SEBQH2Z2E3SGKGAJPN0Q7E)
- [Chat activity by department](#h_01F2SEBYX4J8BQN5G0BQVZS9BE)

## Agent activity

Number of chats that are assigned by system to an agent. This does not include agent initiated Chats.

| **Agent Report** | **Description** |
| --- | --- |
   | First Name | The agent's first name |
| Last Name | The agent's last name |
| Email | The agent's email address |
| Enabled | Whether this agent is currently enabled in the dashboard |
| Start Time (UTC+0) | The start time for the stats in that row (with the time zone indicated) |
| End Time (UTC+0) | The end time for the stats in that row (with the time zone indicated) |
| Assigned Chats | Number of chats that are assigned by system to an agent. This does not include agent initiated Chats. |
| Accepted Chats | Number of chats that agent accepted from system assigned chats. An agent can serve more chats than assigned chats by proactively initiating chat with a visitor, join a chat of other agents, receive a transferred chat from other agent, and manually pick up an unassigned chat when chat limit is reached. |
| Completed Chats | The number of chats which end with a reply from this agent |
| Dropped Chats | The number of chats accepted by or assigned to this agent which end with an unanswered message from a visitor |
| Missed Chats | The number of chats where this agent does not answer the incoming chat request and the visitor subsequently leaves |
| Visitor Initiated | The number of chats started by a visitor and served by this agent |
| Agent Initiated | The number of chats started by an agent and served by this agent |
| Trigger Initiated | The number of chats started by a trigger and served by this agent |
| Visitor Initiated (Completed) | The number of chats started by a visitor which have been completed by this agent |
| Agent Initiated (Completed) | The number of chats started by an agent which have been completed by this agent |
| Trigger Initiated (Completed) | The number of chats started by a trigger which have been completed by this agent |
| Visitor Initiated (Dropped) | The number of chats started by a visitor which have been dropped by this agent |
| Agent Initiated (Dropped) | The number of chats started by an agent which have been dropped by this agent |
| Trigger Initiated (Dropped) | The number of chats started by a trigger which have been dropped by this agent |
| Visitor Initiated (Missed) | The number of chats initiated by a visitor which have been missed by this agent |
| Agent Initiated (Missed) | The number of chats initiated by an agent which have been missed by this agent |
| Trigger Initiated (Missed) | The number of chats started by a trigger which have been missed by this agent |
| Unresponsive Chats | The number of chats which are started by this agent or a trigger, to which the visitor does not respond |
| Agent Initiated (Unresponsive) | The number of chats started by this agent where the visitor is unresponsive |
| Trigger Initiated (Unresponsive) | The number of chats started by a trigger and joined by this agent, where the visitor is unresponsive |
| Chat Satisfaction | The satisfaction rating, if any, the visitor applied to the chat session |
| Chats Rated | Total number of chats rated for this agent |
| Good | Total number of chats rated Good for this agent |
| Bad | Total number of chats rated Bad for this agent |
| Average of First Response Time (sec) | The average time it takes for an agent to respond to an initial chat request from a visitor (across all their chats) |
| Maximum of First Response Time (sec) | The longest amount of time it takes for this agent to respond to an initial chat request from a visitor (across all their chats) |
| Minimum of First Response Time (sec) | The shortest amount of time it takes for this agent to respond to an initial chat request from a visitor (across all their chats) |
| Average Chat Duration (sec) | The average length of time a chat session takes across all chats served by this agent. Chat duration is calculated by subtracting the timestamp of the first message from the timestamp of the last message. |
| Maximum Chat Duration (sec) | The longest length of time a chat session takes for chats served by this agent. Chat duration is calculated by subtracting the timestamp of the first message from the timestamp of the last message. |
| Minimum Chat Duration (sec) | The shortest length of time a chat session takes for chats served by this agent. Chat duration is calculated by subtracting the timestamp of the first message from the timestamp of the last message. |
| Average Response Time (sec) | Each individual chat has its own average response time. This is calculated as the average time it takes for this agent to respond to the last visitor message in that chat. The “Average Response Time” refers to the average value of the average response time across all the agents chats. |
| Maximum of Average Response Time (sec) | The highest Average Response Time across all the agent's chats. |
| Minimum of Average Response Time (sec) | The highest Average Response Time across all the agent's chats. |
| Acceptance | The percentage of Assigned chats that were served by agents out of all the chats routed to the agent.  Note: If [auto-accept](https://support.zendesk.com/hc/en-us/articles/6009407849754) is turned on, this report is not displayed. and activity monitor. |
| Conversions (Agent Attributed) | Total number of goal conversions that are attributed to chats assigned or served by this specific agent. |

## 

## 

## Chat activity

| **Chat Report** | **Description** |
| --- | --- |
   | Start Time (UTC+0) | The start time for the stats in that row (with the time zone indicated) |
| End Time (UTC+0) | The end time for the stats in that row (with the time zone indicated) |
| Total Chats | The total number of missed, dropped and served chats combined |
| Completed Chats | The number of chats which end with a reply from an agent |
| Dropped Chats | The number of chats which end with an unanswered visitor message |
| Missed Chats | The number of chats where the agent does not answer the incoming chat request and the visitor subsequently leaves |
| Visitor Initiated | The number of chats started by a visitor on your website |
| Agent Initiated | The number of chats started by one of your agents |
| Trigger Initiated | The number of chats started by a trigger and served by this agent |
| Visitor Initiated (Completed) | The number of chats started by a visitor which have been completed |
| Agent Initiated (Completed) | The number of chats started by an agent which have been completed |
| Trigger Initiated (Completed) | The number of chats started by a trigger which have been completed by this agent |
| Visitor Initiated (Dropped) | The number of chats started by a visitor which have been dropped |
| Agent Initiated (Dropped) | The number of chats started by an agent which have been dropped |
| Trigger Initiated (Dropped) | The number of chats started by a trigger which have been dropped by this agent |
| Visitor Initiated (Missed) | The number of chats started by a visitor which have been missed |
| Agent Initiated (Missed) | The number of chats started by an agent which have been missed |
| Trigger Initiated (Missed) | The number of chats started by a trigger which have been missed by this agent |
| Unresponsive Chats | The number of chats which are started by an agent or trigger, to which the visitor does not respond |
| Agent Initiated (Unresponsive) | The number of chats started by an agent where the visitor is unresponsive |
| Trigger Initiated (Unresponsive) | The number of chats started by a trigger and joined by this agent where the visitor is unresponsive |
| Chat Satisfaction | The satisfaction rating, if any, the visitor applies to the chat session |
| Chats Rated | Total number of chats rated for this agent |
| Good | Total number of chats rated Good for this agent |
| Bad | Total number of chats rated Bad for this agent |
| Average of First Response Time (sec) | The average time it takes for an agent to respond to an initial chat request from a visitor (across all chats) |
| Maximum of First Response Time (sec) | The longest amount of time it takes for an agent to respond to an initial chat request from a visitor (across all chats) |
| Minimum of First Response Time (sec) | The shortest amount of time it takes for an agent to respond to an initial chat request from a visitor (across all chats) |
| Average Chat Duration (sec) | The average length of time a chat session takes (across all chats). Chat duration is calculated by subtracting the timestamp of the first message from the timestamp of the last message. |
| Maximum Chat Duration (sec) | The longest length of time a chat session takes. Chat duration is calculated by subtracting the timestamp of the first message from the timestamp of the last message. |
| Minimum Chat Duration (sec) | The shortest length of time a chat session takes. Chat duration is calculated by subtracting the timestamp of the first message from the timestamp of the last message. |
| Average Response Time (sec) | Each individual chat has its own average response time. This is calculated as the average time it takes for an agent to respond to messages in that chat. The "Average Response Time" refers to the average value of the average response time across all chats. |
| Average Response Time - Maximum (sec) | The highest Average Response Time across all chats. |
| Average Response Time - Minimum (sec) | The shortest Average Response Time across all chats. |
| Wait Time (Served) | The amount of time before an agent first responds to a chat request. |
| Wait Time (Missed) | The amount of time between a visitor's last comment and when they ended the chat, without an agent reply. |
| Conversions (Agent Attributed) | Total number of goal conversions that are attributed to chats assigned or served by a specific agent. |
| Conversions (Unattributed) | Total number of goal conversions, including conversions not attributed to a chat. |

## Log in times

| **Agent Report** | **Description** |
| --- | --- |
   | First Name | The agent's first name |
| Last Name | The agent's last name |
| Email | The agent's email address |
| Enabled | Whether this agent is currently enabled in the dashboard |
| Login Time (UTC+0) | The time the agent logged in to the dashboard (with the time zone indicated) |
| Logout Time (UTC+0) | The time the agent logged out of the dashboard (with the time zone indicated) |
| Duration (sec) | The length of time (in seconds) the agent was logged in to the dashboard |

## Serving times

| **Agent Report** | **Description** |
| --- | --- |
   | First Name | The agent's first name |
| Last Name | The agent's last name |
| Email | The agent's email address |
| Enabled | Whether this agent is currently enabled in the dashboard |
| Serving Start Time (UTC+0) | The start time for the chats the agent takes part in (with the time zone indicated) |
| Serving End Time (UTC+0) | The end time for the chats the agent takes part in (with the time zone indicated) |
| Duration (sec) | The length of time (in seconds) the agent was involved in the chats |

## Status Sessions

|  |  |
| --- | --- |
| Name | The agent's complete name |
| Email | The agent's email address |
| Enabled | Whether the agent is currently enabled |
| Status | The agent's current availability status |
| Start Time (UTC+0) | The start time for the stats in that row (with the time zone indicated) |
| End Time (UTC+0) | The end time time for the stats in that row (with the time zone indicated) |
| Duration (sec) | The length of time (in seconds) the agent held the status |

## 

## Agent and chat activity by department

| **Agent Report** | **Description** |
| --- | --- |
   | Department | The department handling the activity |
| First Name | The agent's first name |
| Last Name | The agent's last name |
| Email | The agent's email address |
| Enabled | Whether this agent is currently enabled in the dashboard |
| Start Time (UTC+0) | The start time for the stats in that row (with the time zone indicated) |
| End Time (UTC+0) | The end time for the stats in that row (with the time zone indicated) |
| Completed Chats | The number of chats which end with a reply from this agent |
| Dropped Chats | The number of chats which end with an unanswered visitor message (from this agent) |
| Missed Chats | The number of chats where this agent does not answer the incoming chat request and the visitor subsequently leaves |
| Visitor Initiated | The number of chats started by a visitor and served by this agent |
| Agent Initiated | The number of chats started by an agent and served by this agent |
| Trigger Initiated | The number of chats started by a trigger and served by this agent |
| Visitor Initiated (Completed) | The number of chats started by a visitor which have been completed by this agent |
| Agent Initiated (Completed) | The number of chats started by an agent which have been completed by this agent |
| Trigger Initiated (Completed) | The number of chats started by a trigger which have been completed by this agent |
| Visitor Initiated (Dropped) | The number of chats started by a visitor which have been dropped by this agent |
| Agent Initiated (Dropped) | The number of chats started by an agent which have been dropped by this agent |
| Trigger Initiated (Dropped) | The number of chats started by a trigger which have been dropped by this agent |
| Visitor Initiated (Missed) | The number of chats initiated by a visitor which have been missed by this agent |
| Agent Initiated (Missed) | The number of chats initiated by an agent which have been missed by this agent |
| Trigger Initiated (Missed) | The number of chats started by a trigger which have been missed by this agent |
| Unresponsive Chats | The number of chats which are started by this agent or a trigger, to which the visitor does not respond |
| Agent Initiated (Unresponsive) | The number of chats started by this agent where the visitor is unresponsive |
| Trigger Initiated (Unresponsive) | The number of chats started by a trigger and joined by this agent, where the visitor is unresponsive |
| Chat Satisfaction | The satisfaction rating, if any, the visitor applied to the chat session |
| Chats Rated | Total number of chats rated for this agent |
| Good | Total number of chats rated Good for this agent |
| Bad | Total number of chats rated Bad for this agent |
| Average of First Response Time (sec) | The average time it takes for an agent to respond to an initial chat request from a visitor (across all their chats) |
| Maximum of First Response Time (sec) | The longest amount of time it takes for this agent to respond to an initial chat request from a visitor (across all their chats) |
| Minimum of First Response Time (sec) | The shortest amount of time it takes for this agent to respond to an initial chat request from a visitor (across all their chats) |
| Average Chat Duration (sec) | The average length of time a chat session takes across all chats served by this agent. Chat duration is calculated by subtracting the timestamp of the first message from the timestamp of the last message. |
| Maximum Chat Duration (sec) | The longest length of time a chat session takes for chats served by this agent. Chat duration is calculated by subtracting the timestamp of the first message from the timestamp of the last message. |
| Minimum Chat Duration (sec) | The shortest length of time a chat session takes for chats served by this agent. Chat duration is calculated by subtracting the timestamp of the first message from the timestamp of the last message. |
| Average Response Time (sec) | Each individual chat has its own average response time, which is calculated as the average time it takes for this agent to respond to messages in that chat. The "Average Response Time" refers to the average value of the average response time across all the agents' chats. |
| Maximum of Average Response Time (sec) | The highest Average Response Time across all the agent's chats. |
| Minimum of Average Response Time (sec) | The highest Average Response Time across all the agent's chats. |

## Chat activity by department

| **Chat Report** | **Description** |
| --- | --- |
   | Department | The department handling the activity |
| Start Time (UTC+0) | The start time for the stats in that row (with the time zone indicated) |
| End Time (UTC+0) | The end time for the stats in that row (with the time zone indicated) |
| Completed Chats | The number of chats which end with a reply from an agent |
| Dropped Chats | The number of chats which end with an unanswered visitor message |
| Missed Chats | The number of chats where the agent does not answer the incoming chat request and the visitor subsequently leaves |
| Visitor Initiated | The number of chats started by a visitor on your website |
| Agent Initiated | The number of chats started by one of your agents |
| Trigger Initiated | The number of chats started by a trigger and served by this agent |
| Visitor Initiated (Completed) | The number of chats started by a visitor which have been completed |
| Agent Initiated (Completed) | The number of chats started by an agent which have been completed |
| Trigger Initiated (Completed) | The number of chats started by a trigger which have been completed by this agent |
| Visitor Initiated (Dropped) | The number of chats started by a visitor which have been dropped |
| Agent Initiated (Dropped) | The number of chats started by an agent which have been dropped |
| Trigger Initiated (Dropped) | The number of chats started by a trigger which have been dropped by this agent |
| Visitor Initiated (Missed) | The number of chats started by a visitor which have been missed |
| Agent Initiated (Missed) | The number of chats started by an agent which have been missed |
| Trigger Initiated (Missed) | The number of chats started by a trigger which have been missed by this agent |
| Unresponsive Chats | The number of chats which are started by an agent or trigger, to which the visitor does not respond |
| Agent Initiated (Unresponsive) | The number of chats started by an agent where the visitor is unresponsive |
| Trigger Initiated (Unresponsive) | The number of chats started by a trigger and joined by this agent where the visitor is unresponsive |
| Chat Satisfaction | The satisfaction rating, if any, the visitor applies to the chat session |
| Chats Rated | Total number of chats rated for this agent |
| Good | Total number of chats rated Good for this agent |
| Bad | Total number of chats rated Bad for this agent |
| Average of First Response Time (sec) | The average time it takes for an agent to respond to an initial chat request from a visitor (across all chats) |
| Maximum of First Response Time (sec) | The longest amount of time it takes for an agent to respond to an initial chat request from a visitor (across all chats) |
| Minimum of First Response Time (sec) | The shortest amount of time it takes for an agent to respond to an initial chat request from a visitor (across all chats) |
| Average Chat Duration (sec) | The average length of time a chat session takes (across all chats). Chat duration is calculated by subtracting the timestamp of the first message from the timestamp of the last message. |
| Maximum Chat Duration (sec) | The longest length of time a chat session takes. Chat duration is calculated by subtracting the timestamp of the first message from the timestamp of the last message. |
| Minimum Chat Duration (sec) | The shortest length of time a chat session takes. Chat duration is calculated by subtracting the timestamp of the first message from the timestamp of the last message. |
| Average Response Time (sec) | Each individual chat has its own average response time, which is calculated as the average time it takes for an agent to respond to messages in that chat. The "Average Response Time" refers to the average value of the average response time across all chats. |
| Average Response Time - Maximum (sec) | The highest Average Response Time across all chats. |
| Average Response Time - Minimum (sec) | The shortest Average Response Time across all chats. |