# Using routing profiles in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9791029507738-Using-routing-profiles-in-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Routing profiles in Contact Center let you manage how agents handle different communication channels. You can edit profiles to adjust channels, queues, and concurrency settings. Admins can change an agent's routing profile during shifts to match contact needs. This flexibility ensures agents receive the right contacts without disrupting ongoing interactions, especially in chat scenarios.

A routing profile in Amazon Connect specifies the channels that an agent can handle and how contacts incoming on those channels are routed to the agent. Each agent is assigned to one routing profile, and a routing profile can have multiple agents assigned to it.

When you create a routing profile, you configure channels and queues for the routing profile. To learn more about routing profiles, see [Create a routing profile in Amazon Connect to link queues to agents](https://docs.aws.amazon.com/connect/latest/adminguide/routing-profiles.html) in the AWS documentation.

You can edit a routing profile in Amazon Connect to update the settings, including channels, queues, and concurrency. You can allow agents to change profiles during their shift as needed.

This article contains the following topics:

- [Editing a routing profile](#topic_ukk_rnn_wgc)
- [Changing an agent's routing profile](#topic_dtv_tnn_wgc)

## Editing a routing profile

You can edit a routing profile in Amazon Connect to customize settings, such as channels, queues, and concurrency.

**To edit a routing profile**

1. In your [Amazon Connect Dashboard](https://aws.amazon.com/connect/), navigate to **Users** >
   **Routing profiles**.
2. Select the routing profile you want to edit.
3. Update settings, such as channels, queues, and concurrency, as needed.
4. Click **Save**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cont_cent_rp_1.png)

## Changing an agent's routing profile

Agents might need to switch between routing profiles during their shift to handle different types of contacts. The only way to change an agent’s routing profile is for an admin to make the change. It's not possible for an agent to change the profile themselves.

Changing profiles during a live contact does not interfere with the ongoing interaction. Following the switch to a new routing profile, agents stop receiving contacts from the previous routing profile. They start receiving contacts associated with the new profile, even if there’s still an open contact from the previous profile. Remember, this applies to chat contacts only, because agents can’t handle more than one call at the same time.

Routing profiles can be grouped using a square bracket naming convention. The routing profiles list shows only profiles in the same group as the currently assigned one.
If the current profile doesn’t have a group, then the routing profile tab is hidden.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cont_cent_rp_2.png)

**To change an agent's routing profiles**

- In the Connect Dashboard, navigate to User Management, then find the agent and change their routing profile.