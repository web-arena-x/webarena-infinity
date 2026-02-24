# Creating custom omnichannel routing queues

Source: https://support.zendesk.com/hc/en-us/articles/6716530152858-Creating-custom-omnichannel-routing-queues

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Location:  Admin Center > Objects and rules > Omnichannel routing >
Queues

Omnichannel routing assigns tickets from [email (including web form, side conversations, and
API)](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb), calls, and messaging directly to agents based on agent availability and
capacity and, on Professional plans and above, ticket priority and skills. The standard
omnichannel routing configuration directs all [eligible tickets](https://support.zendesk.com/hc/en-us/articles/6712096584090#topic_by4_fyz_31c) into a single queue,
assigning work to agents in the group assigned to the ticket. If you want to use
omnichannel routing to direct work to agents in multiple groups or configure secondary
or fallback groups, you can create custom queues.

If you create custom queues, new tickets are inserted into the first custom queue they
meet the conditions for, and omnichannel routing uses the standard queue only if the
ticket doesn't match any custom queues. On Team and Growth plans, email and messaging
tickets that are reassigned back to a group are automatically inserted into the standard
queue and assigned to an agent in the ticket's group. On Professional plans and above,
admins can choose whether to [reassign email and messaging tickets](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_g4r_x1z_rcc) through
the custom queues or the standard queue.

You must have the [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) to use omnichannel routing.

## Creating a custom omnichannel routing queue

Before creating queues, ensure you [understand how queues work in omnichannel routing](https://support.zendesk.com/hc/en-us/articles/6712096584090). You
can create up to 199 custom queues in addition to the standard omnichannel routing
queue.

**To create a custom omnichannel routing queue**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Omnichannel routing >
   Queues**.
2. Click **Create queue**.
3. Enter a **Name** for the queue.
4. (Optional) Enter a **Description** for the queue.
5. Click **Add condition** to set up the queue to meet **All** or
   **Any** conditions.

   Conditions are the qualifications needed for a
   ticket to be added to the queue.
6. Select a **Condition**, **Field operator**, and **Value** for each
   condition you add.

   See [Building queue condition statements](#topic_amf_zjd_42c).
7. (Optional, Enterprise plans only) Select **Distribute tickets across
   subqueues** if you want to route specific percentages of the tickets
   meeting this queue's conditions to different primary and secondary groups.
   You can create up to five subqueues per custom queue.

   If you select this
   option, provide a unique **Name** and configure the
   **Percentage**, **Priority**, **Primary groups**, and
   **Secondary groups** (as described below) for each subqueue
   rather than the custom queue as a whole. The sum of the subqueue
   percentages must equal 100%.

   After creating all of your
   subqueues, click **Save**.
8. Specify the queue's **Priority** relative to other queues.

   Valid
   values are *1-100*, with *1* being the highest
   priority.

   Queue priority is only
   considered when an agent receives work from multiple queues. In that
   case, work from the queue with the higher priority is assigned
   first.
9. Select at least one **Primary group**.

   You can select up to 20 primary
   groups. Omnichannel routing treats all primary groups as a single pool
   of agents.
10. (Optional) If you want to configure secondary groups for the queue, select
    **Turn on secondary groups** and then select at least one
    **Secondary group**.

    You can select up to 20 secondary groups.
    Omnichannel routing treats all secondary groups as a single
    pool of agents.

    Omnichannel routes
    work to the primary groups first, falling back to the secondary groups
    only if no agents in the primary groups are available. If no agents are
    available in any of the primary or secondary groups, the tickets remain
    in the queue until an agent from any of the groups becomes
    available.
11. Click **Save**.

    Note: New queues are automatically added to the bottom of
    the list on the Queues page. If you want your newly created queue to be
    evaluated prior to other omnichannel routing queues, you must [reorder the list](https://support.zendesk.com/hc/en-us/articles/6716541571994#topic_kkb_g43_j1c). See [Managing custom omnichannel routing
    queues](https://support.zendesk.com/hc/en-us/articles/6716541571994).

After you create custom queues, you can report on their performance to see how well
work is being routed through them, including how much work is awaiting available
agents and how long work items spend in each queue on average. See [Explore recipe: Reporting on custom omnichannel queue
performance](https://support.zendesk.com/hc/en-us/articles/7217081202714).

## Building queue condition statements

Condition statements consist of a condition, operator, and value. Conditions are the
qualifications needed for a ticket to enter the queue. The field operator
determines the relationship between the condition and the value. For example, if you
select the field operator "Is," your condition must equal the specified value.
Supported field operators differ by condition.

The following conditions are available for custom omnichannel routing queues:

- **Routing channel**: Indicates how omnichannel routing is treating a
  ticket for routing purposes. Often this aligns with the ticket's channel
  (also known as the via type). However, some settings, such as [treating agent-ended messaging sessions
  as email tickets](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_hr4_1lh_n2c), can result in this value being different from
  the ticket's channel.

  For example, you can use the following conditions
  to create a queue that routes agent-ended messaging session tickets
  only:
  - **Channel | Is | Messaging**
  - **Routing channel | Is | Email**
- **All [ticket trigger
  conditions](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_i3y_fkz_1cb)**

  Note: The *Ticket > Channel* condition returns
  a complete list of ticket channels, including those that aren't
  supported by omnichannel routing. See [Channels supported by omnichannel
  routing](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_hhb_2xk_3yb).