# Setting up notification routing for live chat

Source: https://support.zendesk.com/hc/en-us/articles/4408836490138-Setting-up-notification-routing-for-live-chat

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Professional or Enterprise |

Note: This article applies to accounts using Zendesk Chat. If you are using messaging, see [Setting up notifcation routing for messaging](https://support.zendesk.com/hc/en-us/articles/5020833543450). If you are using messaging with omnichannel, see [Turning on omnichannel routing](https://support.zendesk.com/hc/en-us/articles/5866925319962) and [Managing your omnichannel routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210).

You can specify how agents are notified about incoming live chat requests with Chat routing settings. These settings are accessed from your Chat dashboard.

This article includes the following topics:

- [Understanding and configuring basic notification routing options](#topic_nzf_pdb_pmb)
- [Configuring chat limits](#topic_dlr_wt1_q5)
- [Understanding Assigned notification routing behavior](#topic_u3c_rrn_mpb)
- [Configuring additional settings for Assigned routing](#topic_wyd_vy1_q5)
- [Monitoring chat routing data in Analytics](#topic_dcs_kh2_gw)

## Understanding and configuring basic notification routing options

There are two options for how notifications for incoming chat requests are sent to your agents:

- **Broadcast**: All agents are notified of all incoming requests, and the agent has to click on **Serve Request** to start serving the request. This is the default setting.
- **Assigned**: Online agents are evenly notified of incoming requests, so only one agent is notified of each incoming request at any time.

Requests are added to a queue in chronological order, based on time of ticket creation. Incoming requests received while agents are offline are sent to the Unassigned tickets view or the agent’s Group view. Offline requests can be assigned to agents as part of triaging, or they can be manually picked up by agents themselves.

In the Zendesk Agent Workspace, incoming live chat request notifications appear in the top-right corner of the workspace, in the Accept button.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_social_message_accept_button.png)

If you do not have the Agent Workspace enabled, assigned live chat requests appear at the bottom of the Chat dashboard:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_incoming_assigned.png)

**To configure the notification routing method for your account**

1. From the Chat dashboard, select **Settings** > **Routing**.
2. In the Chat Routing section, select a notification routing method.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_routing_method.png)
3. Click **Save changes**.

## Configuring chat limits

Chat limits allow you to cap the number of notifications assigned or broadcast to each agent, based on an agent's workload. You can adjust these limits to help your agents better manage the volume or complexity of service requests.

An agent's workload is determined by the number of active live chat requests assigned to them. A request is considered active if it has received a response in the past 10 minutes.

The way the limit works depends on your routing method:

- **Broadcast:** When agents are at the specified limit, they will no longer be notified of incoming requests, and they will not be able to serve requests through the Serve Request or Accept button.
- **Assigned**: Agents will be routed incoming requests only up to their chat limit.

You can select from the following two types of notification limits:

- **Account**: Set one limit that applies to all agents in your account.
- **Agent**: Notification limits are configured in each agent's profile. You can specify that only admins can edit agent limits, or allow agents to set their own limits.

Chat limit settings have no effect on your widget or its online status. Even if all agents are at their limits, visitors can still submit chat requests, which are then queued until an agent becomes available. Agents can see the increase in the number of queued requests in the Serve Request or Accept button but aren't able to serve them.

Note: If you created [Chat roles](creating-custom-chat-roles-and-assigning-users.md) that allow agents to **Initiate and view chats** in the **Proactive Chatting** option, those agents can serve chats over their specified limits. This option allows agents the ability to see visitors and manually select and prioritize certain visitors from the visitor's list.

**To enable notification limits**

1. From the Chat dashboard, select **Settings** > **Routing**.
2. Next to Chat Limit, select **On**.
3. Next to Limit Type, select **Account** or **Agent**.
4. If you selected **Account**, enter a value in the **Maximum chats** field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/routing_chatlimit_account3.png)
5. If you selected **Agent**, limits are configured in each agent's profile:
   - With the **Assigned** routing method, select the **Personal limits** check box that appears for agents to set their own notification limits in their profiles.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_limits_personal_limits_updated)
   - If you're using the **Broadcast** routing method or using **Assigned** but don't select the **Personal limits** check box, set a chat limit for each agent's profile. Select an agent to edit under **Settings** > **Agents** and enter a value in the **Chat limit** field.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_limit_per_agent_updated)
6. Click **Save changes**.

## Understanding Assigned notification routing behavior

When Assigned routing is activated, by default chat notifications are routed as follows:

- First, the incoming request is assigned to the agent currently serving the fewest ongoing conversations.
- If multiple agents are tied for the fewest number of conversations, the incoming request is assigned to the agent with no missed assignments in the last 15 minutes.
- If more than one of the available agents has no missed assignments in the last 15 minutes, or if all agents have a missed assignment in the last 15 minutes, the incoming request is assigned to the agent with the oldest last missed assignment timestamp.
- If all available agents have not served any requests yet, the incoming request is assigned to an agent by random.

Note: An agent with an existing incoming chat assignment that has not yet been served will *not* be assigned a second conversation.

When all eligible agents are *offline*, notifications are not sent. If incoming requests are later assigned as part of manual request triaging, agents will receive a notification when a request is assigned to them or their group.

Additionally, activating skills-based routing, hybrid assignment mode, or chat reassignment can impact assigned notification behavior. See [Configuring additional settings for Assigned routing](#topic_wyd_vy1_q5) for more information.

## Configuring additional settings for Assigned routing

If you select the Assigned routing method, there are additional settings you can configure.

### Configuring skills routing

Note: Skills-based routing is available on Suite Professional and Enterprise plans, as well as Support and Chat Professional (with the Skills-Based Routing add-on) and Enterprise plans.

If you're using **Assigned** routing, you can set up skills routing. For details, see [Routing chats based on agent skills](https://support.zendesk.com/hc/en-us/articles/4408836348058).

### Configuring hybrid assignment mode

The Hybrid Assignment Mode setting is only available if notification requests are **Assigned** and you have set [chat limits](#topic_dlr_wt1_q5).

Hybrid assignment mode gives agents the option of voluntarily serving additional requests after they've reached their set chat limits.

With this setting activated, if an agent reaches their chat limit and a new incoming chat request is not picked up by other available agents, that agent does *not* hear the incoming chat [notification sound](https://support.zendesk.com/hc/en-us/articles/4408821476378#topic_rb2_fs5_bdb) and the Serve Request/Accept button does *not* light up.

**To enable Hybrid Assignment Mode**

1. Go to **Settings** > **Routing**.
2. In the **Hybrid Assignment Mode** section, select the **Allow Hybrid Assignment** check box.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_routing_hybridassignmentmode.png)
3. Click **Save Changes**.

### Configuring reassignment

The Reassignment setting is only available if you're using **Assigned** routing.

When this setting is activated, a reassignment timeout period is attached to each incoming chat request. If the agent initially assigned the chat request doesn't respond before the assignment times out, the incoming request will be reassigned to the next available agent based on their capacity and set chat limit. When this option is enabled, if an agent doesn't respond to an assigned request for a set period of time, another agent is automatically notified of the request.

If this option is not enabled (if **Reassignment** is set to **Off**), once a notification is assigned to an agent, it is *not* automatically reasssigned to another agent.

**To enable reassignment**

1. Go to **Settings** > **Routing**.
2. Next to **Reassignment**, select **On**.
3. Enter a **number of seconds** in the Reassignment timeout window. For example, if you want notifications to be reassigned after 15 seconds with no response, enter 15.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_routing_reassignmenttimeout.png)
4. Click **Save Changes**.

### Configuring automatic idle settings

This setting applies only if you're using **Assigned** routing and have enabled **Reassignment** above.

Enable this setting to automatically set chat agents' status to Away or Invisible after a specified number of notifications are automatically reassigned. Agents are notified when their status is changed.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_routing_idle_timeout.png)

**To enable automatic idle status**

1. Go to **Settings** > **Routing**.
2. Next to **Automatic Idle**, select **On**.
3. Enter a value in the **Chats Reassigned** field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_automaticidle_chatsreassigned.png)
4. Select a status option next to **Idle Status**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_automaticidle_status.png)
5. Click **Save Changes**.

## Monitoring live chat routing data in Analytics

You can analyze live chat routing data in Analytics with two statistics:

- **Acceptance**: the percentage of assigned chats that were served by agents out of all the chats routed to the agent.

  Note: If [auto-accept](https://support.zendesk.com/hc/en-us/articles/6009407849754) is turned on, acceptance stats are not displayed.
- **Capacity (beta)**: The estimated amount of chats that can be served by the account in a given period of time. The capacity is a function of 1) the number of agents logged in, 2) the average chat duration of an account and 3) the chat limit set by the agent.

For more details about where to view these stats, see [Monitoring chat activity with Analytics](https://support.zendesk.com/hc/en-us/articles/4408828193562).