# Adding and managing skills on tickets

Source: https://support.zendesk.com/hc/en-us/articles/5833458075930-Adding-and-managing-skills-on-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Location:  Admin Center > Objects and rules > Business rules >
Skills

To use skills for routing purposes, they must be assigned to tickets. We recommend that
you use triggers to automatically evaluate new or updated tickets and add skills, but
you can also use routing rules to apply skills at ticket creation or manually add or
remove skills at any time.

This article contains the following topics:

- [Assigning skills to tickets](#topic_ncp_krt_5xb)
- [Removing skills from a ticket](#topic_obh_qrt_5xb)
- [Understanding how skills are applied to follow-up tickets](#topic_vgq_xxv_3mb)

For information about who can see the skills field on tickets, see [Viewing a ticket's skills](https://support.zendesk.com/hc/en-us/articles/5834247413786).

## Assigning skills to tickets

A ticket must have at least one skill assigned to it if you want it to be routed to
an agent based on skills. The best way to do this is using triggers or routing
rules, so that skills are automatically added to tickets meeting the specified
criteria, but they can also be added or adjusted manually.

Even when skills are added automatically, it's important to make sure tickets without
skills are also assigned to agents. Omnichannel routing handles this seamlessly, by
considering skills if they are present, but otherwise assigning tickets based on
priority and agent availability. For standalone skills-based routing, you may want
to define a view specifically for tickets without skills. You should also consider
if there is a missing skill or skill condition that would have resulted in a skill
being assigned to a ticket.

Skills cannot be assigned to [AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346).

Note: All agents are considered matches to tickets that have no skills
assigned.

There are three ways you can add skills to tickets:

- [Using triggers to add skills to tickets (recommended)](#topic_bbs_lrt_5xb)
- [Using routing rules to add skills to tickets](#topic_m2t_mrt_5xb)
- [Manually adding skills to tickets](#topic_ams_nrt_5xb)

### Using triggers to add skills to tickets (recommended)

When omnichannel routing is turned on, you can use triggers to assign skills to
tickets because they can add skills when tickets are updated as well as when
they're created. Additionally, the skills actions for ticket triggers also allow
you to specify the priority of the skills for routing purposes. Skills marked as
*required* can't time out and are always part of the criteria for
routing the ticket to an agent, but *optional* skills stop being considered
for routing purposes when a skills timeout occurs. Trigger actions related to
skills are available when you have created at least one skill. For more
information, see the [Triggers conditions and actions
reference](https://support.zendesk.com/hc/en-us/articles/4408893545882).

Note: If you were previously using skills and had defined routing rules, we
recommend that you delete them and recreate the logic with triggers. If you
don't delete them, they will run before triggers and other business rules when a
ticket is created, but can't be used to add or update skills after the initial
creation.

**To configure a trigger to add skills to tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/4408886797466) or [edit](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_dwq_zoy_tb) a trigger.
3. Under **Conditions**, [specify the conditions](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_i3y_fkz_1cb) under which
   you want the skills to be added.
4. Under **Actions**, select **Add skills** and then select the
   individual skills to be added. See [Building trigger action
   statements](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_ncz_4kz_1cb).
5. For each skill you select, specify a priority:
   - **Required**: Omnichannel routing considers only agents with
     required skills eligible to receive the tickets.
   - **Optional**: Optional skills are subject to the [skills timeout](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_ag5_tlr_wbc) defined in
     the omnichannel routing configuration. When a skills timeout occurs,
     omnichannel routing ignores all optional skills when looking for
     available agents.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/ocr_skills_priority_trigger.png)

   Note: Each skill that is
   dropped from consideration increases the number of agents eligible to
   receive the ticket and, in turn, increases the likelihood of it being
   assigned.
6. Click **Save**.

### Using routing rules to add skills to tickets

If you choose not to use omnichannel routing and [triggers to assign skills to tickets](#topic_bbs_lrt_5xb), you'll need to
define conditions for each skill that determine which tickets they're applied
to. These sets of conditions are called *routing rules*. When a ticket is
created that meets the conditions defined in a skill's routing rule, that skill
is attached to the ticket. Routing rules are applied only upon ticket creation,
which means:

- If a ticket is created before a routing rule is set up, it won't have
  that skill attached to it.
- If a ticket is updated so that it no longer meets a skill's conditions,
  the ticket will still require that skill until you manually remove it
  from the ticket.
- If a ticket is updated so that it meets the conditions for a new skill,
  the ticket will not start to require that new skill until you manually
  add it to the ticket.

**To create a routing rule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
2. Click the skill you want to add a routing rule for.
3. Under **Tickets** > **All of the following conditions** or **Any
   of the following conditions**, click **Add condition**.
4. Select a condition, a field operator, and a value.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sbr_ticket_condition.png)
5. (Optional) Repeat these steps until you've added all of the conditions
   for the skill.
6. Click **Save**.

**To edit a routing rule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
2. Click the skill you want to modify the routing rules for.
3. Under **Tickets**, click the delete icon (**x**) next to each
   skill you want to remove.
4. Click **Save**.

### Manually adding skills to tickets

In addition to automatically adding skills to tickets using triggers and
routing rules, admins and agents with permission can also manually add or update
skills on tickets at any time.

**To manually add skills to a ticket**

1. In Support, [open the ticket](https://support.zendesk.com/hc/en-us/articles/4408882039450-Working-with-tickets-#topic_xlz_zsm_pf:~:text=syntax%20(if%20applicable).-,To%20open%20a%20ticket,-Locate%20the%20ticket).
2. Under the **Skills** field, use the dropdown so select the skills
   you want to add.
3. Click **Submit**.

## Removing skills from a ticket

You can use triggers to remove skills from tickets when they are created or updated.
You can also remove skills from tickets manually at any time.

**To use triggers to remove a skill from a ticket**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/4408886797466) or [edit](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_dwq_zoy_tb) a trigger.
3. Under **Conditions**, [specify the conditions](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_i3y_fkz_1cb) under which
   you want the skill to be removed.
4. Under **Actions**, select **Remove skills** and then select the
   individual skills to be removed. See [Building trigger action
   statements](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_ncz_4kz_1cb).
5. Click **Save**.

**To manually remove skills from a ticket**

1. In Support, [open the ticket](https://support.zendesk.com/hc/en-us/articles/4408882039450-Working-with-tickets-#topic_xlz_zsm_pf:~:text=syntax%20(if%20applicable).-,To%20open%20a%20ticket,-Locate%20the%20ticket).
2. Under the **Skills** field, click the **x** icon next to the name of
   the skill you want to remove.
3. Click **Submit**.

## Understanding how skills are applied to follow-up tickets

When a follow-up ticket is created for a closed ticket, you may notice that skills on
the follow-up ticket don't always match the skills on the original ticket.
Generally, when a follow-up ticket is created, it inherits data from the original
ticket (see [Creating a follow-up for a closed ticket](../../agent-guide/ticket-management/creating-a-follow-up-for-a-closed-ticket.md)).
Skills are an exception to this rule.

Follow-up tickets don't inherit skills. Instead, skills are applied to the follow-up
ticket based on your triggers or routing rules when the follow-up ticket is
created.