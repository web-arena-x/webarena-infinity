# Getting started with Zendesk Suite - Part 6: Routing incoming support requests

Source: https://support.zendesk.com/hc/en-us/articles/4944922385050-Getting-started-with-Zendesk-Suite-Part-6-Routing-incoming-support-requests

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Articles in the series

- [Introduction: Getting started with Zendesk Suite](https://support.zendesk.com/hc/en-us/articles/4408881937306)
- [Part 1: Accessing Zendesk Suite admin settings](https://support.zendesk.com/hc/en-us/articles/4944856070426)
- [Part 2: Adding team members](https://support.zendesk.com/hc/en-us/articles/4944849237658)
- [Part 3: Understanding how end user accounts are handled](https://support.zendesk.com/hc/en-us/articles/4944925937818)
- [Part 4: Managing user access security and authentication](https://support.zendesk.com/hc/en-us/articles/4944919944730)
- [Part 5: Adding support channels](https://support.zendesk.com/hc/en-us/articles/4944930820506)
- [Part 6: Routing incoming support requests](https://support.zendesk.com/hc/en-us/articles/4944922385050)
- [Part 7: Managing support requests during non-business hours](https://support.zendesk.com/hc/en-us/articles/4945055494170)
- [Part 8: Guaranteeing customer support expectations with service level agreements](https://support.zendesk.com/hc/en-us/articles/4944993140762)
- [Part 9: Reporting on support activity](https://support.zendesk.com/hc/en-us/articles/4944968790426)
- [Part 10: Enabling customer satisfaction ratings](https://support.zendesk.com/hc/en-us/articles/4944994159130)
- [Part 11: Leveraging AI features with Zendesk](https://support.zendesk.com/hc/en-us/articles/6501074649242)
- [Part 12: Using the Zendesk developer platform to extend your support solution](https://support.zendesk.com/hc/en-us/articles/4944970330138)
- [Part 13: Rolling out your Zendesk Suite support solution](https://support.zendesk.com/hc/en-us/articles/4944970747418)
- [Part 14: Additional features](https://support.zendesk.com/hc/en-us/articles/6579939982746)

Live channels (voice and messaging) are directly routed to the pool of agents who have been assigned to provide support to those channels. If no agents are available or during off hours, requests from those live channels can be followed up on.

Incoming support requests from most channels can be routed directly to agents by [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514), or you can use business rules such as ticket triggers and automations to direct tickets from any channel to specific agents or groups and organized into views.

Omnichannel routing is the default routing experience and sends work directly to the agents most available and suited to handle them. Calls are always offered to agents, messaging conversations can be offered or auto-accepted, and email tickets are always assigned to agents. Within omnichannel routing, you can prioritize tickets based on ticket priority or time to SLA breach, uses queues to route tickets to multiple groups of agents to increase the odds of a quick response, and use many other settings to tailor your routing configuration to your needs. All other business rules involved in routing tickets provide a *pull* routing model, where tickets are assigned to groups and then agents manually assign tickets to themselves from the pool of tickets assigned to the groups they are members of.

If you turn off omnichannel routing, you can use ticket triggers and automations to assign incoming tickets to groups. After a group is assigned, calls and messaging conversations are offered to agents within the group, and tickets created through email channels are visible in views and agents can self-assign tickets. Some examples of how you might use standalone business rules to route tickets include assigning voice calls to specific groups so that only agents in those groups can see and respond to the calls, automatically assigning tickets sent to a specific email address to a specific group, and using skills-based routing to send email tickets or live chats to agents with the matching skills. All of these examples can also be accomplished with omnichannel routing.

You set up and manage ticket routing in Admin Center.

To automatically route your tickets with omnichannel routing, you either need to create custom queues (recommended) or configure ticket triggers that assign groups to all incoming tickets and add the auto-routing tag to email tickets. Queue-based routing provides the most sophisticated routing features, while group-based routing within omnichannel routing works automatically for calls and messaging conversations and provides a routing experience similar to the standalone business rule routing options.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocrdiag22.png)

Business rules, such as ticket triggers and automations, can be used with omnichannel routing or on their own. They evaluate ticket data and then take action on tickets that meet the specified criteria. For example, incoming support requests from a specific channel are assigned to a specific group, as in the example above. You can also modify the other ticket data, such as setting the ticket’s priority based on who sent you the support request. Whether you use omnichannel routing or not, ticket triggers and automations are still the primary mechanism that sends notifications to end users.

![How triggers work](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/routing_workflow1.png)

It is also possible to handle ticket routing manually. As an example, if you want to triage all incoming tickets before assigning them to agents, you can assign someone the role of triage agent who evaluates the incoming tickets in a view that’s been created for that task and then manually assigns the tickets to the appropriate agent or group.
However, this approach is only viable with relatively low ticket volumes.

For a detailed explanation of ticket routing and links to articles that provide setup instructions, read [Routing options for incoming tickets](https://support.zendesk.com/hc/en-us/articles/4408831658650).

Continue to [Part 7: Managing support requests during non-business hours](https://support.zendesk.com/hc/en-us/articles/4945055494170-Getting-started-with-Zendesk-Suite-Part-8-Managing-support-requests-during-non-business-hours).