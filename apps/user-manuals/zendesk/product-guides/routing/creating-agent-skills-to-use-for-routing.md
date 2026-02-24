# Creating agent skills to use for routing

Source: https://support.zendesk.com/hc/en-us/articles/4408838892826-Creating-agent-skills-to-use-for-routing

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Verified AI summary ◀▼

Use skills-based routing to match tickets with agents who have the necessary skills. Create skill types and assign skills to agents, ensuring tickets reach the right person. Plan strategically to replace existing business rules and consider agent attributes like location or expertise. Configure skill priorities to manage ticket queues effectively, ensuring high-priority skills are utilized appropriately.

Location:  Admin Center > Objects and rules > Business rules >
Skills

With skills-based routing, admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can create *skills* and
associate each one with individual agents. For each skill, you also define a set of ticket
conditions that require the skills.

This article contains the following topics:

- [Understanding skills](#topic_kxq_pny_hdb)
- [Planning your skills](#topic_x5d_cvs_5xb)
- [Creating skill types](#topic_sx3_hqt_cs)
- [Adding skills to skill types](#topic_ug2_j4y_hdb)
- [Assigning agents to skills](#topic_w3m_th2_bbb)
- [Configuring the priority of an agent's skill](#topic_ysc_fq4_ghc)

## Understanding skills

Skills are agent attributes that determine their suitability to work a ticket that requires them. They can be something the agent is able to do, as we'd typically think of a skill, or another type of attribute, such as the agent's location, timezone.

When adding skills, you'll create skill types to categorize the skills. For example, you could
have agents dedicated to supporting specific products; in this scenario you could
create a *Product* skill type and add *ProductA*, *ProductB*, and
*ProductC* as the skills.

You can define up to 10 skill types. Each skill type can contain up to 30 skills.

Although a skill can technically exist with just a name, skills are fully defined when they have:

- A name
- A way to add that skill to tickets
- A set of agents who have that skill

### Understanding how skills are used for routing

There are two ways to [use skills to route tickets](https://support.zendesk.com/hc/en-us/articles/5833468891674):

- Omnichannel routing. Tickets are automatically assigned to agents with matching
  skills. Optionally, you can configure a skills timeout, after which a ticket can be
  automatically assigned to agents without regard to skills.
- Standalone skills-based routing. Agents use one or more views to identify tickets that
  match their skills and then manually assign tickets to themselves.

## Planning your skills

Whether you're using skills with omnichannel routing or as a standalone routing solution,
it's important to plan out your skills strategically. You should understand what skills you
need, who has them, and how they might replace existing business rules.

Review the following details for your organization to help identify the skills you want to
use:

- Your triggers, groups, and views. Which ones exist to segregate tickets to
  certain agents? Many of those can be replaced with skills-based routing.
- Zendesk’s localization feature or intelligent triage. If you're using
  localization or intelligent triage, the same language detection can be used as a condition
  to add a language skill to a ticket.
- Figure out what sets your agents apart from each other. Seniority? Training?
  Consider if you’d like to set up skills and route tickets based on those variables.
- Figure out what sets your tickets apart from each other. Is there a lot of
  variation?
- Talk to your team or team lead. Are there generally understood to be “go-to”
  or “no-go” people for certain topics? Of the skills you've determined you need, who can do
  what?
- Agents are only considered a match if they have all of the skills required by a ticket.
  After deciding which skills to use, identify common skill combinations and how many agents
  have all of them. You might need to train or hire agents to get the coverage you
  want.
- Of the skills you've decided you need, what is the most logical way to categorize them?
  These categories will become your skill types. Does thinking about categories of skills
  lead you to consider using skills you hadn't considered yet?

## Creating a skill type

You must create at least one skill type before you can add skills. You can create up to 10
skill types.

**To create a skill type**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
2. On the Skills page, click the **New skill type** button.
3. Enter a unique name for the skill type. Names cannot exceed 96 characters.
4. Press **Enter** to save the skill type.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sbr_skill_type_new.png)

## Adding skills

After you've created one or more skill types, you can add your skills. Each skill type can
contain up to 30 skills.

Be intentional about the skill types you're adding skills to. After a skill is created, you
can’t move it to a different skill type. Instead, it must be recreated in the skill type you
want it to be in.

After you've added your first skill to a skill type, a Skills ticket field is added to
tickets and visible to admins. If you want agents to be able to see or modify skills on
tickets, see [Configuring who can see the skills ticket field](https://support.zendesk.com/hc/en-us/articles/5834247413786#topic_qxr_glw_vxb).

**To add a skill to a skill type**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
2. Find the skill type you want to add a skill to and click **New skill**.
3. Enter a name for the new skill and press **Enter**.

   Names can't exceed 96
   characters and must be unique within a skill type. Skills in separate skill types can
   have the same name, but we recommend against it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sbr_skills_list.png)

## Managing the skills assigned to agents

Each skill must be assigned to at least one agent. Admins can assign skills to all agents
and other admins. On Enterprise plans, [agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) with the **View user profile list** and
**Skills** permissions can assign skills to other agents.

There are two ways you can assign skills to agents:

- [Assigning skills to agents from the Skills page](#topic_pgz_ckt_5xb)
- [Assigning skills to agents from the agent's profile](#topic_fqg_2kt_5xb)

Note: When you add a skill to an agent, the [priority](#topic_ysc_fq4_ghc) is automatically set to *Normal*.

### Assigning skills to agents from the Skills page

Use the Skills page to manage agents assigned to skills when you add a new skill or need
to assign multiple agents to a skill. You can select up to 50 agents at a time to add or
remove from a skill.

**To assign a skill to agents using the Skills page**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
2. Click the skill you want to add agents to.
3. Under **Agents**, click **Add agents**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sbr_agent_list.png)
4. In the **Add agents to skill** dialog, select the agents you want to assign to the
   skill. You can select up to 50 agents at a time.

   To locate agents:
   - Scroll through the list of agents.
   - Enter an agent's name in the search box
   - Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)) and select the group name to filter by group

   As you select agents, their names appear in the **Agents with skill**
   list.
5. Click **Save**.
6. (Optional) [Configure the priority of
   agents' skills](#topic_ysc_fq4_ghc).

**To remove agents from a skill using the Skills page**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
2. Click the skill you want to add agents to.
3. Under **Agents**, click **Manage**.
4. In the **Agents with skill** list, click the delete icon (**x**) next to the
   name of the agent you want to remove from the skill.
5. Click **Save**.

### Assigning skills to agents from the agent's profile

Use the agent's profile to manage skill assignments if you need to add multiple skills to
a single agent or when you're onboarding a new agent.

**To assign skills to an agent's profile**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. Find the agent's name, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)) on that row, and select **Manage in Support**.
3. In the **Skills** field in the left sidebar, select the skills from the
   dropdown list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/skills_field_profile.png)
4. (Optional) [Configure the priority of the
   agent's skills](#topic_ysc_fq4_ghc).

**To remove skills from an agent’s profile**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. Find the agent's name, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)) on that row, and select **Manage in Support**.
3. In the **Skills** field, click the delete icon (**x**) next to the
   skill you want to remove.

## Configuring the priority of an agent's skill

In addition to using triggers to configure the priority of a ticket's skills, which are
used to determine eligible agents, it's also possible to prioritize an agent's skills when
using omnichannel routing. Configuring the priority of an agent's skill is helpful because
this can ensure that agents with a high-priority skill are receiving tickets that require
those skills over other tickets in the queue. Without this, agents with the high priority
skills might otherwise have their capacity consumed by tickets that don't require their high
priority skills.

Agent skill priority is defined for each agent individually, but can be configured in bulk.
The default agent skill priority is *Normal*.

**To configure the agent skill priority**

1. Make sure the skill is [assigned to the
   agents](#topic_w3m_th2_bbb) for whom you want to modify the priority.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
3. Click the skill you want to configure agents' priority for.
4. Under **Agents**, click **Edit prioritization**.
5. Select the agents for whom you want to modify the skill's priority.

   Optionally,
   filter the list by group, search for agents by name, or use the checkbox in the
   heading row of the list to select all agents with the skill.
6. Click **Edit skill priority** and select **Normal** or **High**.
7. Click **Save**.