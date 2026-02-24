# Turning on and setting up omnichannel routing

Source: https://support.zendesk.com/hc/en-us/articles/5866925319962-Turning-on-and-setting-up-omnichannel-routing

---

Omnichannel routing can be used to route new and open tickets fromemail (including web form, side conversations, and API), calls, and messaging. Depending on your plan, the date your Zendesk account was created, and your routing preferences, there are some considerations and configuration required to begin usingomnichannel routing. This article explains how to activate and start using omnichannel routing.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Objects and rules > Omnichannel routing > Routing configuration

Omnichannel routing can be used to route new and open tickets from [email (including web form, side conversations, and API)](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb), calls, and messaging. Depending on your plan, the date your Zendesk account was created, and your routing preferences, there are some considerations and configuration required to begin using [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514). This article explains how to activate and start using omnichannel routing.

It contains the following topics:

- [Considerations for using omnichannel routing](#topic_wbv_vbn_jvb)
- [Turning on omnichannel routing and managing your settings](#topic_lzk_btp_m5b)
- [Requirements for the routing trigger for group-based routing](#topic_asz_ljb_yxb)

## Considerations for using omnichannel routing

In addition to the [omnichannel routing requirements and limitations](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_zlk_c3p_m5b), consider the following details about turning on and using omnichannel routing:

To use omnichannel routing, the [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) must be activated for your account. If your account has a Chat subscription, native messaging or Sunshine Conversations must also be activated.

Omnichannel routing works out of the box. That means it can start routing new or updated calls and messaging conversations as soon as it's turned on, and new or updated email tickets as soon as the auto-routing tag is added to them or custom queues are created. To minimize the risk of disruptions, we recommend [creating a plan for your routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_frn_1vc_yxb) ahead of time. If your Zendesk account was created prior to December 5, 2024, we also recommend turning on omnichannel routing during off-hours or your least-busy time of day.

When omnichannel routing is on, the option to activate [focus mode for live channels in the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408835750042) is hidden. Instead, you must use the focus mode option in your [omnichannel routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210).

Additionally, you should also train your agents and team leads on the omnichannel routing experience:

- **Routing new and updated tickets**: For tickets to be routed by omnichannel routing, they must be created or updated after omnichannel routing is turned on or a configuration setting is changed. Don't expect stale existing tickets to be routed to agents automatically if there is a lull in new ticket volume. If you need omnichannel routing to route older tickets to agents, you can update the tickets.
- **Unified agent statuses**: If your agents are used to the Agent Workspace without omnichannel routing, make sure they understand what will change. Specifically, the moment omnichannel routing is turned on, all agents are set to offline. They're prompted to set a new status and will see new options in the status picker. The statuses available to them when omnichannel routing is on are unified agent statuses and apply across email, messaging, and talk channels. The idle timeout settings can help ensure agents stop receiving time-sensitive work when they're no longer active, but it's still best to encourage agents to set themselves to *Away* or *Offline* any time they step away from their computers. Team leads should also understand the real-time reporting that is available when the agents start using unified agent statuses. See [About unified agent status](https://support.zendesk.com/hc/en-us/articles/5133523363226).

 If you use Zendesk Workforce Management, you can configure WFM to calculate adherence and track activities based on unified agent statuses instead of general tasks. [Synchronizing unified agent status data with WFM](https://support.zendesk.com/hc/en-us/articles/10114746509978) also eliminates the need for agents to update their availability in two systems. Make sure your agents understand whether they need to set their status in WFM or if their unified agent statuses are used.
- **Omnichannel queue**: Tickets are created for all channels as soon as they are received. With the standard omnichannel routing configuration, all tickets go into a single queue. However, it is possible for admins to create additional custom queues for omnichannel routing. When using custom queues, the auto-routing tag isn't required and all tickets for email, messaging, and calls are automatically matched to queues; if an email ticket doesn't match any custom queues, it falls back to the standard queue. It might help agents if they [understand omnichannel routing queues](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_nlb_c3p_m5b) and how tickets are ordered and assigned to agents.
- **Auto-assignment of work**: Email tickets (including web form, side conversations, and API) are automatically assigned when they reach the front of the queue. With the standard omnichannel routing configuration, messaging and talk tickets are automatically offered to an agent when they reach the front of the queue, but the agent must accept the conversation or call. If they don't accept the conversation or call within a specified amount of time, it is automatically offered to the next agent and so on, in a round-robin until it is accepted. If you'd like omnichannel routing to automatically assign messaging conversations, you can turn on auto-accept for messaging in your routing configuration.

Finally, if you have configured an IVR menu for calls, make sure to remove all non-primary groups from your IVR menu before turning on omnichannel routing. Failure to do so can cause confusing routing behavior.

## Turning on omnichannel routing and managing your settings

Newer accounts have omnichannel routing turned on by default. However, some setup is still required to ensure it works for all channels. The options available vary by plan:

- **Team and Growth plans**: Omnichannel routing uses group-based routing.
 That means tickets must have a group assigned in order to be routed.
 Furthermore, email tickets must also have the auto-routing tag. Ticket triggers are the best way to ensure all new tickets are assigned a group and get the auto-routing tag.
- **Professional and Enterprise plans**: On these plans, you can choose between using [custom queues](https://support.zendesk.com/hc/en-us/articles/6716530152858) or [group-based routing](https://support.zendesk.com/hc/en-us/articles/6712096584090) with the standard omnichannel routing queue. If you choose to use custom queues, you must create custom queues with conditions that match most or all of your tickets. If you choose group-based routing, you must create one or more ticket triggers to assign a group and add the auto-routing tag to tickets.

**To set up omnichannel routing**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Omnichannel routing > Routing configuration**.
2. On the Routing configuration page, click **Turn on omnichannel routing**.
3. (Accounts created before December 5, 2024 only) On the Manage settings page, click **Turn on omnichannel routing**.

   Accounts created on or after December 5, 2024 have omnichannel routing on by default.
4. Enter an **Auto-routing tag**, which is used to indicate which tickets originating from email channels are routed by omnichannel routing through the standard queue.

   The auto-routing tag is only used in queue-based routing if an email ticket doesn't match any custom queues, and you still want it to be routed by omnichannel routing through the standard queue.
5. (Recommended for Professional plans and above) [Create custom queues](https://support.zendesk.com/hc/en-us/articles/6716530152858) that match all or most of your tickets and route them to the proper groups of agents.
6. (Recommended for all plans relying on group-based routing) [Create at least one ticket trigger](https://support.zendesk.com/hc/en-us/articles/4408886797466)
   that can be used to add a group and the auto-routing tag to email tickets (including web form, side conversations, and API) you want to route. On Professional plans and above, you can also configure the triggers to set the ticket's priority. See [Requirements for the routing triggers](#topic_asz_ljb_yxb).
7. Click **Save**.

   You can use omnichannel routing as-is at this point, or you can review and adjust your [routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210) to better meet your needs.

If you need to turn off omnichannel routing, see [Turning off omnichannel routing](https://support.zendesk.com/hc/en-us/articles/5095079121690).

## Requirements for the routing trigger for group-based routing

With group-based routing through the standard omnichannel routing queue, tickets must be assigned to an appropriate group before they can be routed to an agent.
Additionally, [email tickets](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb) must have the auto-routing tag to be routed and tickets must have skills if you want to route based on that.
You can manually assign the group, skills, and add the routing tag, but [triggers](https://support.zendesk.com/hc/en-us/articles/4408822236058) provide an automated way to accomplish this.

If you [create custom queues](https://support.zendesk.com/hc/en-us/articles/6716530152858), omnichannel routing automatically routes all email, call, and messaging conversation tickets, regardless of the presence of the auto-routing tag, and uses the queue's groups rather than the ticket's assigned group. The ticket's assigned group is ignored. However, tickets that don't match to any of your custom queues will still require a group assignment, and email tickets also require the auto-routing tag, before they can be routed by omnichannel routing through the standard queue.

Triggers that are used for standard omnichannel routing must have the following parameters:

- Conditions that define the tickets you want to route, such as a [channel](https://support.zendesk.com/hc/en-us/articles/4408824097050) or [tag](https://support.zendesk.com/hc/en-us/articles/4408888664474). This includes tags added to calls from an IVR menu. See [Building trigger condition statements](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_i3y_fkz_1cb).
- Actions to define the routing.
 - Required actions:
    - Assign a group (not required if using [omnichannel routing queues](https://support.zendesk.com/hc/en-us/articles/6712096584090), but good to have for tickets that don't match any of your custom queues)
    - Add the auto-routing tag (email tickets only)
 - Optional actions for Professional and Enterprise plans:
    - (Professional and Enterprise plans) Assign a priority
    - (Professional and Enterprise plans) If you're using skills with omnichannel routing, you can [use triggers to add and update skills on tickets](https://support.zendesk.com/hc/en-us/articles/5833458075930) and set each skill's priority.

See [Building trigger action statements](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_ncz_4kz_1cb).

Note: Triggers run only on new or updated tickets. Other tickets won’t be processed.

**Example of adding the routing tag and groups**

- You want email tickets that come in from the “Very important bank” organization to be assigned the routing tag and assigned to the “VIP” group:
 - Create a trigger with the condition **Ticket >
    Organization** > **is** > **Very important bank**.
 - Add an action **Ticket > Add tags** >
    AUTO\_ROUTING\_TAG.
 - Add an action **Ticket > Group** > **VIP**.