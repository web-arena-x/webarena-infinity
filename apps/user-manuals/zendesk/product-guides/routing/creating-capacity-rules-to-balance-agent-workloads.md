# Creating capacity rules to balance agent workloads

Source: https://support.zendesk.com/hc/en-us/articles/4776409839770-Creating-capacity-rules-to-balance-agent-workloads

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Objects and rules > Omnichannel routing > Capacity rules

Capacity rules are part of [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) that help you balance your team's
workload by setting capacities on automatically assigned work. The standard omnichannel
routing configuration [assigns work](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_nlb_c3p_m5b) to the agent with the highest
spare capacity for the channel who has an eligible status.
For example, you could specify that only 10 open email
tickets can be assigned to an agent at a time. This can be a great way of ensuring that
your less experienced agents are not assigned too much work while they ramp up.

Additionally, you can decide whether you want omnichannel routing to [evaluate agent spare capacity](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_y3p_mh2_rcc) based on the
percentage of their capacity currently assigned or the number of tickets they're still
able to receive based on their maximum capacity for the channel.

However, you can also configure omnichannel routing to use [round robin assignment](https://support.zendesk.com/hc/en-us/articles/7990049158554). When using round robin assignment,
omnichannel routing checks that agents have some amount of spare capacity, but assigns
work based on time elapsed since last assignment for the channel rather than how much
spare capacity agents have.

Omnichannel routing comes with a default capacity rule that you can use as-is
or edit. Admins can also create your own capacity rules to suit your needs. Agents are
always assigned to whichever capacity rule you set as the default initially, but you can
change their assignment if needed. An agent can only be assigned to one capacity rule,
so if you assign an agent to a new rule, they are automatically unassigned from their
current one.

Tip: Capacity rules prevent omnichannel routing from automatically assigning
work to agents who are at capacity for a given channel. However, it's still possible
for agents to exceed the specified capacity by manually assigning work in excess of
the limits or inactive tickets assigned to them becoming active again.

This article contains the following topics:

- [Adding capacity rules](#topic_wzz_wxp_m5b)
- [Understanding how capacity rules work for messaging conversations and live chats](#topic_n2p_wxx_41c)

## Adding capacity rules

Omnichannel routing comes with a built-in capacity rule to get you started,
but you can add additional rules as required. You must be an admin to create and
manage capacity rules.

**To add a capacity rule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Omnichannel routing > Capacity
   rules**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocr_5_GA.png)
2. On the Capacity rules page, click **Add capacity rule**.
3. On the **Add capacity rule** page, provide the following
   information:
   1. **Name**: Enter a descriptive name for the capacity
      rule.
   2. **Description**: Optionally, enter a description that helps
      you to identify the capacity rule.
   3. **Set as default**: New team members are automatically
      assigned to the default capacity rule. Team members who are already
      assigned to a capacity rule won’t change.

      Note: If you create a new capacity rule and assign a team member to
      it, they are removed from the default capacity rule. If you
      delete a capacity rule, all team members assigned to it are
      assigned back to the default rule.
   4. **Assignees**: Click **Add assignee** to specify the
      agents to whom this rule applies.
   5. **Capacities** > **Email**: Enter the number of open
      [email tickets (including web form,
      side conversations, and API)](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb) that can be assigned to an agent
      at one time. This includes all open email tickets, regardless of how
      they were assigned to the agent. Tickets
      that are pending or on hold are not counted towards capacity. (Maximum
      500)
   6. **Capacities** > **Messaging**: Enter the number of
      messaging tickets that can be assigned to an agent at one time. Inactive
      messaging tickets are counted if [Count inactive conversations towards
      an agent's capacity](https://support.zendesk.com/hc/en-us/articles/4828787357210) is selected. Otherwise, only active
      messaging tickets are considered. This capacity also [applies to chats in some
      circumstances](https://support.zendesk.com/hc/en-us/articles/6249962577690). When applicable to live chats, an agent can be
      assigned up to this number of live chats and this number of messaging
      conversations at the same time. (Maximum
      500)

      See [Understanding how capacity rules work for messaging
      conversations and live chats](#topic_n2p_wxx_41c).
   7. **Capacities** > **Talk**: Enter the number of call tickets
      that can be assigned to an agent at one time. Options are 0 or 1. If you
      choose 0, the agents cannot receive calls. Calls are no longer counted
      towards an agent's capacity after the [wrap-up time](https://support.zendesk.com/hc/en-us/articles/4408823877146) ends, if
      configured, or after the agent hangs up.
4. When you are finished, click **Add capacity rule**.

   Your new
   capacity rule is displayed on the Capacity rules page and begins to work
   immediately.

## Understanding how capacity rules work for messaging conversations and live chats

When using capacity rules with conversational channels, it's important to
consider the following information:

- The value you specify for Messaging capacity applies to both messaging
  conversations and live chats separately. If you specify a messaging capacity
  of 3, agents could be assigned up to 3 messaging conversation tickets and 3
  live chats simultaneously.
- In conversations, there is a concept of active and inactive tickets. Zendesk
  defines a messaging conversation as inactive when an end user hasn't sent a
  reply in the last 10 minutes. However, admins can use the [capacity release settings](https://support.zendesk.com/hc/en-us/articles/7043034053658) to
  modify this value and change the status of inactive messaging tickets.
- The omnichannel routing configuration contains a [Count inactive conversations towards an
  agent's capacity](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_ymt_btp_m5b) setting.

  This setting is off by default. When
  off, omnichannel routing counts only active messaging tickets towards an
  agent's capacity. This means agents can have any number of inactive
  messaging conversations and live chats assigned to them in addition to
  the specified capacity of active conversations. Customizing your
  capacity release settings can help you fine-tune agent capacity in this
  scenario. When an inactive conversation becomes active again, agents can
  exceed the specified capacity. Omnichannel routing won't assign them any
  new tickets for that channel until they have spare capacity
  again.

  When this setting is on, omnichannel routing counts all
  open active and inactive messaging tickets towards an agent's capacity.
  Omnichannel routing assigns new conversational tickets to agents only
  when their total number of assigned messaging and live chat tickets,
  respectively, are below the specified capacity.