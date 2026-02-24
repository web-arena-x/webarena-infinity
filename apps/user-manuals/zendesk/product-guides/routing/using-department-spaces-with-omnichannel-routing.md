# Using department spaces with omnichannel routing

Source: https://support.zendesk.com/hc/en-us/articles/8125262923802-Using-department-spaces-with-omnichannel-routing

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

While both [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) and [department spaces](https://support.zendesk.com/hc/en-us/articles/7584022494874) (also known as restricting agent ticket
access by brand) can significantly improve how your team manages tickets, it’s important
to understand that special configuration is required when using them together to prevent
potential routing issues.

This article provides the required configuration for using these features together.

This article includes the following topics:

- [Ensuring the department spaces and omnichannel routing features work together](#topic_ljs_swc_1dc)
- [Mitigating routing issues when using both features](#topic_axs_5wc_1dc)

## Ensuring the department spaces and omnichannel routing features work together

Department spaces allows companies to restrict agent access to tickets by specific
brands. Agents aren’t supposed to be able to view or be assigned tickets associated
with a brand they don’t belong to.

However, omnichannel routing doesn’t recognize which brands agents belong to and
tickets are associated with. As a result, it may attempt to assign tickets to agents
who don’t have the necessary brand membership. While using omnichannel routing with
department spaces won’t cause security incidents, it can lead to several issues:

- **Silent failures**: When an agent is online and available but doesn’t belong
  to the relevant brand, the routing assignment may fail silently. It won't be
  immediately apparent why the ticket wasn’t assigned to the agent. This failure
  condition isn’t reflected in reporting or ticket events.
- **Endless loops**: In scenarios where the only available agent in a group is
  not a member of the ticket's brand, the routing engine may continuously attempt
  to assign the ticket to that agent, resulting in a loop of failed
  assignments.
- **Delayed responses**: Because omnichannel routing doesn’t recognize brands,
  the silent failure and endless loop issues can result in tickets becoming stuck
  in queues awaiting assignment to eligible agents. This can lead to delayed
  response times and negatively impact customer satisfaction.

## Mitigating routing issues when using both features

There are three things you can do to reduce routing issues:

- Ensure alignment between group and brand assignments of agents
- Use triggers or custom queues to ensure tickets are routed to groups based on
  brand
- Monitor agent group and brand assignments

### Ensure alignment between group and brand assignments of agents

Omnichannel routing doesn’t recognize brands, but it does assign tickets to
agents based on the groups they belong to. Aligning agent group assignments with
brand assignments can bridge this gap.

**To align group and brand assignments for agents**

1. [Create](https://support.zendesk.com/hc/en-us/articles/4408894175130) or select a group of
   agents to handle tickets for a brand.
2. Ensure all agents in the group are also [members of the brand](https://support.zendesk.com/hc/en-us/articles/7584022494874#topic_p4k_grx_xbc).

### Use triggers or custom queues to ensure tickets are routed to agents based on brand

When using the standard omnichannel routing queue, tickets are routed to agents
in the ticket’s assigned group. You can create triggers that assign groups to
tickets based on the ticket’s brand. If all agents in a brand are in a single
group, this method can work. However, if the agents in a brand are split across
multiple groups, custom queues will work better for you.

**To use ticket triggers to assign a ticket group based on the ticket’s
brand**

1. [Create](https://support.zendesk.com/hc/en-us/articles/4408886797466) or [modify](https://support.zendesk.com/hc/en-us/articles/4408882237722) a ticket trigger to use the
   following condition:

   **Ticket > Brand** | **Is** | **<brand
   name>**
2. Configure the following action:

   **Ticket > Group** | **<group
   name>**
3. Click **Save**.
4. Repeat for each brand.

Custom queues provide a way for you to specify ticket routing behavior based on
specific criteria, such as a ticket’s brand, while providing a larger pool of
agents who can be assigned because tickets can be routed to agents in multiple
groups. Make the brand a condition for the queue, and then only configure
primary and secondary groups whose agents belong to that brand. This setup
ensures tickets are routed only to agents with the appropriate brand
membership.

**To use custom queues to route tickets to groups based on the ticket’s
brand**

1. [Create](https://support.zendesk.com/hc/en-us/articles/6716530152858) or [modify](https://support.zendesk.com/hc/en-us/articles/6716541571994) a custom queue to use the
   following condition:

   **Ticket > Brand** | **Is** | **<brand
   name>**
2. Under **Groups**, select only groups whose agents are all members of the
   specified brand.
3. Click **Save**.
4. Repeat for each brand.

### Monitor agent group and brand assignments

Regularly review agent assignments to ensure consistency between your group and
brand membership and your routing logic.

If agents frequently move between groups or brands, the likelihood of routing
failures increases significantly. We don’t recommend using brands and
omnichannel routing in this scenario.