# Setting up notification routing for messaging

Source: https://support.zendesk.com/hc/en-us/articles/5020833543450-Setting-up-notification-routing-for-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

Note: If you've turned on omnichannel routing, you'll manage notification settings in Admin Center. Omnichannel settings override the settings described in this article. See [Turning on omnichannel routing](https://support.zendesk.com/hc/en-us/articles/5866925319962) and [Managing your omnichannel routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210) for more information.

You can specify how agents are notified about incoming web or mobile messaging requests with Chat routing settings. These settings are accessed from the Chat dashboard.

You can also specify how long a messaging conversation can go without input from an end user before it is considered inactive, which can impact [agent capacity](https://support.zendesk.com/hc/en-us/articles/4776409839770) and ticket status. See [Automatically releasing agent capacity for messaging conversations](https://support.zendesk.com/hc/en-us/articles/7043034053658).

This article includes the following topics:

- [Understanding and configuring basic notification routing options](#topic_nzf_pdb_pmb)
- [Configuring chat limits](#topic_dlr_wt1_q5)
- [Understanding Assigned notification routing behavior](#topic_u3c_rrn_mpb)
- [Configuring additional settings for Assigned routing](#topic_wyd_vy1_q5)

## Understanding and configuring basic notification routing options

There are two options for how notifications for incoming web and mobile messaging requests are sent to your agents:

- **Broadcast**: All agents are notified of all incoming requests, and the agent clicks **Serve Request** to start serving the request. This is the default setting. It cannot be used for messaging with [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514).
- **Assigned**: Online agents are evenly notified of incoming requests, so only one agent is notified of each incoming request at any time.

Requests are added to a queue in chronological order, based on time of ticket creation. Incoming requests received while agents are offline are sent to the Unassigned tickets view or the agent’s Group view. Offline requests can be assigned to agents as part of triaging, or they can be manually picked up by agents themselves.

In the Zendesk Agent Workspace, incoming messaging request notifications appear in the top-right corner of the workspace, in the Accept button.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_social_message_accept_button.png)

Important: Messaging users *must* make sure Chat departments are enabled for notification routing rules to work. See [Creating and editing a Chat department](https://support.zendesk.com/hc/en-us/articles/4408894143898#topic_mfr_wyk_4fb) for information on updating department settings.

**To configure the notification routing method for your account**

1. From the Chat dashboard, select **Settings** > **Routing**.
2. In the Chat Routing section, select a notification routing method.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_routing_method.png)
3. Click **Save changes**.

## Configuring notification limits

Notification limits allow you to cap the number of notifications assigned or broadcast to each agent, based on an agent's workload. You can adjust these limits to help your agents better manage the volume or complexity of service requests.

Note: If you've turned on omnichannel routing, [capacity rules](https://support.zendesk.com/hc/en-us/articles/4776409839770) override any limits set here for messaging.

An agent's workload is determined by the number of messaging requests assigned to them. A request is considered active if it has received a response in the past 10 minutes. Admins can modify the [messaging inactivitiy period](https://support.zendesk.com/hc/en-us/articles/7043034053658) as needed.

The way the limit works depends on your routing method:

- **Broadcast:** When agents are at the specified limit, they will no longer be notified of incoming requests and will not be able to serve requests through the Serve Request button.
- **Assigned**: Agents will be routed incoming requests only up to their notification limit.

You can apply these limits at the account or agent level:

- **Account**: Sets one limit that applies to all agents in your account.
- **Agent**: Notification limits are configured in each agent's profile. You can specify that only admins can edit agent limits, or allow agents to set their own limits.

Even if all agents are at their limits, visitors can still submit messaging requests, which are then queued until an agent becomes available.

**To activate notification limits**

1. From the Chat dashboard, select **Settings** > **Routing**.
2. Next to Chat limit, select **On**.
3. Next to Apply to, select **Account** or **Agent**.
4. If you selected **Account**, enter a value in the Maximum chats field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/routing_chatlimit_account3.png)
5. If you selected **Agent**, limits are configured in each agent's profile:
   - With the **Assigned** routing method, select the **Personal Limits** check box that appears for agents to set their own notification limits in their profiles.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_routing_chatlimit_agent_assigned.png)
   - If you're using the **Broadcast** routing method or using **Assigned** but don't select the **Personal Limits** check box, set a limit for each agent's profile. Select an agent to edit under **Manage** > **Agents** and enter a value in the Chat limit field.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_routing_chatlimit_editagentprofile.png)
6. Click **Save Changes**.

## Understanding Assigned notification routing behavior

When Assigned routing is activated, incoming messaging notifications are routed as follows:

- First, the incoming request is assigned to the agent currently serving the fewest ongoing conversations.
- If multiple agents are tied for the fewest number of conversations, the incoming request is assigned to the agent with no missed assignments in the last 15 minutes.
- If more than one of the available agents has no missed assignments in the last 15 minutes, or if all agents have a missed assignment in the last 15 minutes, the incoming request is assigned to the agent with the oldest last assignment timestamp.
- If all available agents have not served any requests yet, the incoming request is assigned to an agent at random.

Note: An agent with an existing incoming chat assignment that has not yet been served will *not* be assigned a second conversation.

If an agent does not serve an incoming request before it is [reassigned](#topic_fvw_mz1_q5), it will not be routed to them again until an attempt has been made to route the request to all other eligible agents. Additionally, enabling [Hybrid Assignment mode](#topic_trj_mz1_q5) changes assigned notification behavior.

When all eligible agents are *offline*, notifications are not sent. If incoming requests are later assigned as part of manual request triaging, agents will receive a notification when a request is assigned to them or their group.

## Configuring additional settings for Assigned routing

If you've selected the Assigned routing method, there are additional settings you can configure:

- [Configuring Hybrid Assignment Mode](#topic_trj_mz1_q5)
- [Configuring reassignment](#topic_fvw_mz1_q5)
- [Configuring automatic idle settings](#topic_jlj_4z1_q5)

### Configuring Hybrid Assignment Mode

This setting applies only if notification requests are **Assigned** and limits are activated.

Hybrid Assignment Mode gives agents the option of serving additional requests once they've reached their set limits. Agents will have the option of clicking the Serve Request button to pick up additional requests. If this option isn't enabled, agents can see incoming requests but aren't able to click on the button.

**To enable Hybrid Assignment Mode**

1. Go to **Settings** > **Routing**.
2. In the **Hybrid Assignment Mode** section, select the **Allow Hybrid Assignment** check box.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_routing_hybridassignmentmode.png)
3. Click **Save Changes**.

### Configuring reassignment

This setting applies only if you're using **Assigned** routing.

With this option enabled, if an agent doesn't respond to an assigned request for a set period of time, another agent is automatically notified of the request. If this option is not enabled, (if **Reassignment** is set to **Off**), once a notification is assigned to an agent, it is *not* automatically reassigned to another agent.

Note: This setting applies only if you're using **Assigned** routing. If you’re using omnichannel routing, [its configuration options](https://support.zendesk.com/hc/en-us/articles/4828787357210) include reassignment timing and will override anything set here for messaging.

**To enable reassignment**

1. Go to **Settings** > **Routing**.
2. Next to **Reassignment**, select **On**.
3. Enter a **number of seconds** in the Reassignment timeout window. For example, if you want notifications to be reassigned after 15 seconds with no response, enter 15.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_routing_reassignmenttimeout.png)
4. Click **Save Changes**.

### Configuring automatic idle settings

This setting applies only if you're using **Assigned** routing and have enabled **Reassignment** above. If you’re using [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514), automatic idle is not supported.

Activate this setting to automatically set agent's status to Away or Invisible after a specified number of notifications are automatically reassigned. Agents are notified when their status is changed.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_routing_idle_timeout.png)

**To activate automatic idle status**

1. Go to **Settings** > **Routing**.
2. Next to **Automatic Idle**, select **On**.
3. Enter a value in the **Chats Reassigned** field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_automaticidle_chatsreassigned.png)
4. Select a status option next to **Idle Status**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_automaticidle_status.png)
5. Click **Save Changes**.