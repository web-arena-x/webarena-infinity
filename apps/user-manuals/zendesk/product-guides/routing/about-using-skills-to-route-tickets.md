# About using skills to route tickets

Source: https://support.zendesk.com/hc/en-us/articles/5833468891674-About-using-skills-to-route-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Verified AI summary ◀▼

Use skills-based routing to match tickets with agents who have the right skills, improving response times and workload distribution. Skills can be used alone or with omnichannel routing to consider agent status and capacity. Set up skills, assign them to agents, and use triggers to update them on tickets. Skills timeout settings ensure flexibility in agent assignment when needed.

Skills can be used as a standalone routing method for Support tickets, or as one of several factors considered for omnichannel routing and applied to tickets from [email (including web form, side conversations, and API)](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb), calls, and messaging. This article explains more about each of these options.

This article includes the following topics:

- [Understanding skills](#topic_rkh_3nj_5xb)
- [Using skills with omnichannel routing](#topic_d2l_bnx_txb)
- [Using standalone skills-based routing](#topic_s2n_dnx_txb)

## Understanding skills

Skills are agent attributes that determine their suitability to work a ticket that requires them. They can be something the agent is able to do, as we'd typically think of a skill, or another type of attribute, such as the agent's location, timezone.

When adding skills, you'll create skill types to categorize the skills. For example, you could have agents dedicated to supporting specific products; in this scenario you could create a *Product* skill type and add *ProductA*, *ProductB*, and *ProductC* as the skills.

You can define up to 10 skill types. Each skill type can contain up to 30 skills.

Although a skill can technically exist with just a name, skills are fully defined when they have:

- A name
- A way to add that skill to tickets
- A set of agents who have that skill

### Setting up skills-based routing

The first several steps for setting up skills-based routing are the same whether you're using it as a standalone solution or as part of [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514).

- [Plan out your skills](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_x5d_cvs_5xb).
- [Create skills](https://support.zendesk.com/hc/en-us/articles/4408838892826).
- [Assign them to agents](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_w3m_th2_bbb).
- [Configure an automated way to assign skills to tickets](https://support.zendesk.com/hc/en-us/articles/5833458075930).

After that, you either need to [configure skills as part of your omnichannel routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210), which automatically assigns tickets to agents, or [define one or more views](https://support.zendesk.com/hc/en-us/articles/4408883700122) for your agents to pull tickets from based on their skills.

## Using skills with omnichannel routing

[Omnichannel routing with unified agent status](https://support.zendesk.com/hc/en-us/articles/4409149119514) allows you to direct tickets from email (including web form, side conversations, and API), messaging conversations, calls, and [chats in some circumstances](https://support.zendesk.com/hc/en-us/articles/6249962577690) to agents based on their availability and capacity. On Professional plans and above, tickets from all of these channels can also be routed based on priority and skills. Turning on skills in omnichannel routing means you're routing based on agent status, capacity, skills, and ticket priority all at once.

When using skills in omnichannel routing, agents must have skills that match the ticket in addition to having an eligible status and spare capacity for that channel of work. You have the option to enforce the skill matching, meaning you wait for an agent with the matching skill to become available, or to let skills time out and "fall back" to the omnichannel routing model without optional skills if agents with the matching skills aren't available within a specified amount of time after the ticket is created. This flexibility gives admins the most control possible over their workflow without requiring their manual intervention.

Skill timeouts work as you'd expect for email tickets, which are always assigned to agents by omnichannel routing. If an email ticket can't be assigned to an available agent that has all of the matching skills, after a specified time, the optional skills are dropped. However, for messaging and calls, a skills timeout can occur only if no agents with the matching skills are available (online, with spare capacity) for the timeout duration. If any agent with matching skills is available, omnichannel routing will continuously offer the ticket to them until either they accept it or all agents with matching skills become unavailable for the specified timeout duration.

However you decide to configure skills in omnichannel routing, tickets from all channels are automatically assigned (email) or offered to (messaging and calls) to the best-suited available agent. This has many benefits, including faster response times and more equitable workloads for your agents, and can also improve your end users' experience since they're more likely to interact with agents with specialized skills to meet their needs.

Skill timeouts reset after the ticket has been assigned to an agent. If a ticket re-enters an omnichannel routing queue to be assigned to an agent, all skills will be respected and allowed to time out in order of priority again until an eligible agent is found.

For more information, see [About omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514), [Turning on omnichannel routing](https://support.zendesk.com/hc/en-us/articles/5866925319962), and [Managing your omnichannel routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocr_skills_surfboard_example.png)

### Prioritizing agent skills

Separate from the priority of the ticket's skills, which can timeout for the purposes of routing, you can also configure the priority of an agent's skills.
When using agent skill priority, omnichannel routing looks for tickets in the queue with that high priority skill to assign to the agent whenever they have spare capacity. Other tickets the agent is eligible to receive are assigned to them only when there are no tickets in the queue with the agent's high priority skills. That means the prioritization of an agent's skill can result in tickets with lower priority or newer routing eligibility timestamps being assigned to the agent before tickets nearer to the front of the routing queue.

For more information, see [Configuring the priority of an agent's skills](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_ysc_fq4_ghc).

### Using skills with messaging and call tickets

Unlike standalone skills-based routing, you can use omnichannel routing to route messaging conversations, calls, and [sometimes chats](https://support.zendesk.com/hc/en-us/articles/6249962577690794) based on skills, too.
For all channels, tickets are created as soon as the request enters the queue.
That means triggers can run on them. This is how skills are applied to tickets in the queue so that omnichannel routing can match the best agent to the ticket.

Configuring the skills timeout setting for omnichannel routing is particularly important for calls, messaging conversations, and [chats](https://support.zendesk.com/hc/en-us/articles/6249962577690). Doing so means omnichannel routing first attempts to assign the work to an eligible agent with all of the matching skills. However, if an agent with the matching skills is unavailable for a specified amount of time after the ticket reaches the top of the queue, omnichannel routing stops considering the optional skills and assigns the ticket to the first available agent in the appropriate groups that has spare capacity.

If you don't turn on the skills timeout:

- All skills on tickets are considered required.
- Calls remain in the queue until they reach the maximum queue wait time and are sent to voicemail.
- Messaging conversations, chats, and email tickets remain in the queue indefinitely until an agent with all of the ticket's skills becomes available.

### Using triggers to add and update skills on tickets

When omnichannel routing is turned on, you can use triggers to assign skills upon ticket creation and ticket updates. This provides significantly more flexibility and responsiveness than the skill-specific routing rules, which can only apply skills when a ticket is created. When using triggers to apply skills to a ticket, you can mark each skill as optional or required. Optional skills are dropped from consideration when a skills timeout occurs, while required skills never time out. Each skill that is dropped from consideration increases the number of agents eligible to receive the ticket and, in turn, increases the likelihood of it being assigned. For more information about adding and updating skills with triggers, see [Adding and managing skills on tickets](https://support.zendesk.com/hc/en-us/articles/5833458075930).

## Using standalone skills-based routing

Skills-based routing is a great option if you're only receiving tickets via email, web form, side conversations, and the API. However, it functions more as a way to sort incoming tickets by skills rather than actually routing them directly to agents. When you use skills as a standalone routing solution, agents rely on Views based on skills to manually assign tickets to themselves.

Note: Standalone skills-based routing can't be used with voice and messaging tickets. To do that, you must [use omnichannel routing](https://support.zendesk.com/hc/en-us/articles/5833468891674#topic_d2l_bnx_txb).

For more information, see [Using standalone skills-based routing](https://support.zendesk.com/hc/en-us/articles/4408883700122).