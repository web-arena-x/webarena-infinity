# Using omnichannel routing while migrating from chat to messaging

Source: https://support.zendesk.com/hc/en-us/articles/6249962577690-Using-omnichannel-routing-while-migrating-from-chat-to-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Many Chat customers want to transition to messaging and begin using omnichannel routing, but aren't sure how to preserve as many of their settings and processes as possible during the transition. This article describes key considerations for the transition and how to map Chat settings to messaging and omnichannel routing settings.

This article contains the following topics:

- [Considerations for using omnichannel routing with Chat](#topic_bjj_3lh_czb)
- [Translating Chat settings into your omnichannel routing configuration](#topic_j24_jlh_czb)

## Considerations for using omnichannel routing with Chat

The following requirements must be met to use omnichannel routing with chat:

- The [Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) must be activated for your account.
- [Messaging must be activated](https://support.zendesk.com/hc/en-us/articles/4408827701530). Omnichannel routing isn't supported for Chat-only accounts.
- At least one [web or mobile messaging channel must be configured](https://support.zendesk.com/hc/en-us/articles/4408827701530#topic_i3s_3yr_zqb).

Consider the following changes you and your team will experience when you begin using omnichannel routing:

- When omnichannel routing is turned on, none of the existing Chat routing functionality will work and all of the Chat routing settings are hidden.
- Changes to agent status functionality after omnichannel routing is activated:
  - Agent statuses will be managed as [unified agent statuses](https://support.zendesk.com/hc/en-us/articles/5133523363226) after omnichannel routing is activated. [Chat availability statuses](https://support.zendesk.com/hc/en-us/articles/4408828519706) aren't supported.
  - Operating hours aren't supported to automatically change agent statuses.
  - After activating omnichannel routing, if you use the [Agent Availability APIs](https://developer.zendesk.com/api-reference/agent-availability/agent-availability-api/introduction/) to manage agent statuses, the *Department status* and *Account status* Chat trigger conditions won't work.
  - Agent statuses set using the [Conversation APIs](https://docs.smooch.io/rest/) can't be used to route live chats after omnichannel routing is activated.
  - If operating hours remain activated while omnichannel routing is in use, missed chats are routed by omnichannel routing.
- Changes to Explore reporting for Chats routed through omnichannel routing:
  - When omnichannel routing is activated, assigned chats (meaning chats that have been offered to an agent but not accepted) are counted as *incoming* in the queue. The *assigned* value will appear empty. In Chat without omnichannel routing activated, the [Real time monitor](https://support.zendesk.com/hc/en-us/articles/4408888768410) showed a count of offered chats in the queue as well as assigned chats.
  - The **Team > View all** report, used to monitor agent status and workload, will appear empty when omnichannel routing is activated. Instead, the [Omnichannel agent state and activity dashboard](https://support.zendesk.com/hc/en-us/articles/5600291364378) in Explore can be used to find equivalent information.
  - The **Chat Analytics > Acceptance rate** data isn't supported and no equivalent data is currently available when you switch to omnichannel routing.
  - Filtering of **Visitor list** by **Currently served** and **Assigned** activity isn't supported. Additionally, the list can't be filtered by **Serving agent** group activity.
  - In the [Engagements dataset](https://support.zendesk.com/hc/en-us/articles/4409149177242) for live chat, the **Engagement duration** is calculated from the time the ticket is assigned to an agent rather than when it is offered to an agent.

## Translating Chat settings into your omnichannel routing configuration

Before you activate omnichannel routing, make sure to record your Chat routing settings. They won't be visible after omnichannel routing is turned on, but you'll want to reference them when [managing your omnichannel routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210).

The following table maps Chat settings to omnichannel routing configuration settings.

| Chat feature | Omnichannel routing setting | Notes |
| --- | --- | --- |
| [Assigning a group or department](https://support.zendesk.com/hc/en-us/articles/4408881953434) | Chat triggers can be used to automatically assign incoming Chats to groups. | Groups replace departments in the Agent Workspace. Chat triggers will continue to work. |
| [Routing modes](https://support.zendesk.com/hc/en-us/articles/4408836490138) | N/A | Only "assigned" is supported with omnichannel routing. |
| [Chat skills-based routing](https://support.zendesk.com/hc/en-us/articles/4408836348058) | [Ticket skills-based routing](https://support.zendesk.com/hc/en-us/articles/5833468891674#topic_d2l_bnx_txb) | Standalone Chat skills-based routing isn't supported. You must [recreate](https://support.zendesk.com/hc/en-us/articles/4408838892826) your Chat skills as ticket skills and [configure triggers to apply the skills to tickets](https://support.zendesk.com/hc/en-us/articles/5833458075930#topic_bbs_lrt_5xb). Not all Chat trigger conditions are available in ticket triggers. |
| [Chat limits](https://support.zendesk.com/hc/en-us/articles/4408836490138#topic_dlr_wt1_q5) | [Capacity rules](https://support.zendesk.com/hc/en-us/articles/4776409839770) | The omnichannel routing capacity rule configured for messaging conversations will be applied to Chat tickets as well. Agents can be assigned up to the specified capacity of messaging conversations and the same number of live chats. You can't configure a Chat-only capacity rule. |
| [Hybrid assignment mode](https://support.zendesk.com/hc/en-us/articles/4408836490138#topic_wyd_vy1_q5) | N/A | Hybrid assignment isn't supported with omnichannel routing. |
| [Automatic idle](https://support.zendesk.com/hc/en-us/articles/4408828519706#topic_egs_t4j_ws) | [Idle timeout for unified agent statuses](https://support.zendesk.com/hc/en-us/articles/5286614817562) |  |
| [Chat reassignment](https://support.zendesk.com/hc/en-us/articles/4408836490138#topic_wyd_vy1_q5) | [Messaging reassignment timing](https://support.zendesk.com/hc/en-us/articles/4828787357210) | Use the Messaging reassignment timing setting in your [omnichannel routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_ymt_btp_m5b) to automatically reassign messaging conversations and chats to other agents. |