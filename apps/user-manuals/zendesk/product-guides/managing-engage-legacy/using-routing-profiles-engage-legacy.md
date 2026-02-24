# Using Routing Profiles (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731500485914-Using-Routing-Profiles-Engage-Legacy

---

A routing profile in Amazon Connect specifies the channels that an agent can handle (like voice, chat, etc.) and how contacts incoming on those channels are routed to the agent. When you create a routing profile, you specify:

- The channels the agents will support.
- The queues of customers that the agents will handle.
- You can use a single queue to handle all incoming contacts, or you can set up multiple queues.
- Queues are linked to agents through a routing profile.
- Priority and delay of the queues.

## Edit a routing profile

1. In the [Amazon Connect Dashboard](https://aws.amazon.com/connect/) navigate to **Users** then **Routing profiles**.
2. Select the routing profile to edit.
3. You can change settings like channels, queues, and concurrency.
4. Save the changes.

![](https://support.zendesk.com/hc/article_attachments/9731464031386)

Routing profiles Edit Screen in AWS Connect Console

**Further Reading:** For more information on routing profiles please see the [AWS Administration Guide](https://docs.aws.amazon.com/connect/latest/adminguide/routing-profiles.html)

## Change an agent’s routing profile in Amazon Connect

The routing profile determines what types of contacts an agent can receive and the routing priority.

- Each agent is assigned to one routing profile.
- A routing profile can have multiple agents assigned to it.

The only way to change an agent’s routing profile is for an admin to log in to the Amazon Connect Dashboard and make the change in User Management. This means it is not possible for an agent to quickly change the profile themselves.

## Allowing agents to change their routing profiles

In some contact centers, agents may need to switch between routing profiles during their shift to handle different types of contacts.

### How does it work?

Routing profiles need to be grouped using a square bracket naming convention, please see the image below.

The routing profiles list would only show the profiles in the same group as the currently assigned one. If the current profile doesn’t have a group then the routing profile tab is hidden.

![](https://support.zendesk.com/hc/article_attachments/9731500510490)

Agents can switch Routing Profiles using the Agent Status menu

Once a different routing profile is chosen, the change happens immediately. Changing profiles during a live contact does not interfere with the ongoing interaction.

Following the switch to a new routing profile, agents will stop receiving contacts from the previous routing profile. They will start receiving new contacts associated with the new profile straight away, even if there’s still an open contact from the previous profile. Remember, this only applies to chat contacts, since agents can’t handle more than one call at the same time.

‍

‍