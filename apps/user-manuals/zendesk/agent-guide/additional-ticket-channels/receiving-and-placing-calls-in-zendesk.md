# Receiving and placing calls in Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/4408844104986-Receiving-and-placing-calls-in-Zendesk

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article describes a few of the features agents can use to provide voice support.
It assumes that an administrator has [set up voice support](https://support.zendesk.com/hc/en-us/articles/4408838035866) for your Zendesk account and you have [set up your browser or phone for calls](https://support.zendesk.com/hc/en-us/articles/4408823796890).

This article contains the following topics:

- [Setting your agent state for voice support](#topic_j53_h5h_bhb)
- [Receiving calls](#topic_zbx_bxd_chb)
- [Making outbound calls from a ticket](#topic_lzz_mq1_zhb)

Related article:

- [Setting your agent status for email, messaging, and voice](https://support.zendesk.com/hc/en-us/articles/4410545721114)

## Setting your agent state for voice support

You can set your agent state directly from the ticket interface. This description
shows you how to set your agent state for voice support only.

If your admin has enabled omnichannel routing for your account, you [set a single status across multiple channels](https://support.zendesk.com/hc/en-us/articles/4410545721114) (email, messaging,
and voice).

**To set your state**

1. Click the call icon on the right side of the toolbar.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_talk_icon2.png)
2. Select an [agent state](https://support.zendesk.com/hc/en-us/articles/4408829114138) from the drop-down menu in the call console.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_call_status3.png)

   Choices are:

   - **Online**: Signifies you're available to answer calls. If you don't
     answer within 30 seconds, the call is routed to the next online agent.
   - **Away**: Signifies internally to other agents that you're not
     available to take calls. For example, during a break. Calls are routed to another
     agent who is available to answer.
   - **Offline**: Signifies internally to other agents that you're not
     available to take calls for an extended period of time. For example, outside your
     regular working hours.
   - **Transfer only**: An agent in this state is not available to take calls from the
     current queue, but another agent can transfer calls to them.

   If all agents are offline, incoming calls are routed to voicemail. If all agents
   are away, incoming calls continue to be queued and the values your administrator has set
   for maximum queue size and maximum queue wait time behavior are in effect.

## Receiving calls

This section describes basics of how to talk with callers in the agent workspace.
Agents can answer calls directly from the workspace.

If you're in Zendesk, online, and receive a call, the call console appears in the
upper-right corner of the Support page.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_talk_call_incoming.png)

**To take the call**

1. Click **Accept** to answer the call.

   When you accept the call, the call console
   begins recording the call and a ticket is created. For details, see [Understanding how calls become
   tickets](https://support.zendesk.com/hc/en-us/articles/4408821302810-Understanding-how-Talk-calls-become-tickets).

   The counter in the upper-right shows the time of your call.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_call_timer.png)

   You can use the button bar in the ticket to mute, hold,
   transfer, or end the call.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_talk_call_ticket_icons.png)

   | Button | Function |
   | --- | --- |
   |  | Mute or unmute the call. |
   |  | Place the call on hold. |
   |  | Transfer the call. |
   |  | End the call. |
2. To learn more about the caller, click **User** to see the caller's essentials card
   and interaction history.
3. When you're finished with a call, click the **Hang up** button to end the
   conversation.

## Making outbound calls from a ticket

In the agent workspace, you can call from an existing ticket. When you make a call from an
existing ticket, the call details are added to that ticket.

**To make an outbound call from an existing ticket**

1. Select the ticket you want to use to call the requester.
2. Open the channel menu in the composer and click **Call**.
3. Select an existing telephone number or click **Enter a new number** to manually enter
   a new number to dial.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/call_button_expanded.png)

The call console opens and calls the selected number.

In addition to calling from a ticket, you can also make calls from the call console or from
the user's profile. For more information, see [Making outbound calls](https://support.zendesk.com/hc/en-us/articles/4408836235162).