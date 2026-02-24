# Routing chats based on agent skills

Source: https://support.zendesk.com/hc/en-us/articles/4408836348058-Routing-chats-based-on-agent-skills

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Professional or Enterprise |

Skills routing provides a way to identify specific skills for both visitors and agents and route chats accordingly, helping make sure your customers get the relevant and targeted support they need. For example, you might want to create a skill for customers from Spain, so you can route chats to agents who are qualified to work with them (fluent in the Spanish language and familiar with the laws and practices in Spain).

To use skills-based routing, you must have *assigned chat routing* enabled. See [Setting up notification routing for live chat and messaging](https://support.zendesk.com/hc/en-us/articles/4408836490138-Setting-up-chat-routing) for information.

Note: Skills-based routing does not currently work with web messaging.

This article contains the following sections:

- [Enabling skills routing](#topic_pj4_tqx_q1b)
- [Understanding how skills routing works](#topic_lvt_qf2_r1b)
- [Creating skills](#topic_hzp_gpx_q1b)
- [Assigning skills to agents](#topic_ycj_zpx_q1b)
- [Adding skill tags to visitors](#topic_exc_rqx_q1b)

## Understanding how skills routing works

With skills-based routing, incoming chats are given tags to indicate that they require assistance from agents with specific skills. Only agents with the skills that match those tags are notified of and able to serve that incoming chat.

There are a few different conditions that affect how chats are routed with skills routing. Keep in mind the following:

- Agents must have all of the skills a visitor has to be routed chats for that visitor. For example, if a visitor is tagged with skills A, B, and C, but an agent is only tagged with skills A and B, that visitor's chats will not be routed to the agent.
- Maximum wait time, which is set when you enable the feature (see [Enabling skills routing](#topic_pj4_tqx_q1b) below) specifies the amount of time a chat will wait for an agent with the exact set of skills. Once the maximum wait time has elapsed, the chat is assigned to any other agent within the department, based on the number of concurrent chats being served.
- Agents set to Invisible, Away, or Offline are not included in the queue for routing.

## Enabling skills routing

First, you should enable the skills-based routing feature. Note that in order to use this feature, you must already have chat routing enabled. For details about chat routing, see [Setting up chat routing](https://support.zendesk.com/hc/en-us/articles/4408836490138-Setting-up-chat-routing).

**To enable skills routing**

1. Select **Settings** > **Routing**.
2. Click the **Settings** tab, and make sure you have selected **Assigned** for chat routing.
3. In the Skills Routing section, select **On**.
4. Select a value in the **Maximum Wait Time** field. This setting determines how many seconds a visitor should wait in the queue for an agent with matching skills before being reassigned to another available agent.
5. Click **Save Changes**.

## Creating skills

Once skills-based routing is enabled, you need to create the skills that you'll later assign to your agents and visitors.

**To create a skill**

1. Select **Settings** > **Routing**, then select the **Skills** tab.
2. Click **Add Skills**.
3. Enter a name for your skill. Note that the name you give your skill must match the tag applied to incoming chats requiring this skill, so you may want to keep this short (this is important when you're [adding skill tags to visitors](#topic_exc_rqx_q1b)).
4. Click **Create Skill**.

   Using the example from the beginning of this article, we'd want to add the skill *ES* :

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_skill_creation_ES.png)

   We'd then assign this skill to our qualified agents, as described in the next section.

When you create a skill, it is enabled by default. However, skills can be disabled, and when disabled they will still appear in the skills list, but will not be available for skills-based routing. If you find you need to use a disabled skills, you can re-enable it.

**To enable a disabled skill**

1. Select **Settings** > **Routing**, then select the **Skills** tab.
2. Click the skill to be enabled.
3. For Skill status, click **Enable skill**.
4. Click **Save skill**.

## Assigning skills to agents

After you've created the appropriate skills, you need to assign them to agents so they can be routed the correct chats. Agents can be assigned a maximum of five skills.

There are a few different ways you can manage agent skills.

**To assign skills to agents in bulk**

1. Select **Settings** > **Agents**.
2. Select the check boxes next to the agents you want to assign skills to.
3. Click the **Actions** drop-down menu and select **Assign Skills**.
4. Click in the Skills window and select a skill to add from the options. Repeat as needed until all skills are applied.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_assign_skills_bulk.png)
5. Click **Assign**.

**To assign skills for individual agents**

1. Select **Settings** > **Agents**.
2. Click the name of the agent you want to assign skills to to open their profile.
3. Click in the **Skills** field and select a skill from the list that appears. Note that autofill is not enabled in this field.
4. Click **Save changes**.

**To assign skills to yourself**

1. Select **Settings** > **Personal** > **Profile**.
2. In the **Profile** tab under **Preferences**, select the drop-down menu in the **Skills** field and search for or select skills to assign.
3. Click **Save Changes**.

**To remove skills from agents**

1. Select **Settings** > **Agents**.
2. Click the name of the agent you want to assign skills to to open their profile.
3. In the **Skills** field, click the X next to the skill you want to remove.
4. Click **Save changes**.

## Adding skill tags to visitors

Next, you'll need to make sure skill tags are assigned to the appropriate visitors. You can do this using triggers or with the Javascript API. Just like agents, visitors can be assigned a maximum of five skills.

Note: When tagging visitors with a two-letter country code, make sure the code is uppercase. Lowercase codes are not recognized in triggers.

**To set up a trigger to assign tags**

1. From the dashboard, select **Settings** > **Triggers**.
2. Click **Add Trigger**.
3. At the top of the page, make sure Trigger status is **Enabled**.
4. Enter a name and brief description for your trigger.
5. In the **Customize Trigger** section, configure to check conditions related to your skill and assign a tag that matches the name of the skill required. Note that tag matching is not case-sensitive (the tag *tier\_1* would match with the skill *Tier\_1*, for example), and autofill is not enabled when entering a skill tag – you'll need to type in the entire tag. Make sure to set the value of **Run trigger** to **When a visitor has loaded the chat widget** to ensure that the trigger runs at the correct time.

   For example, chats from visitors containing Spain's country code (ES) could be given the tag *ES*:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_trigger_routing_ES.png)
6. Click **Create Trigger**. Now, only agents with the ES skill are notified when a visitor with the ES tag requests a chat.

For more details on setting up triggers, see [Working with triggers](https://support.zendesk.com/hc/en-us/articles/4408884148762-Working-with-triggers).

**To add skill tags using the Javascript API**

- Learn more about the Javascript API [here](https://developer.zendesk.com/documentation/classic-web-widget-sdks/chat-widget/getting-started/chat-widget-api-overview/).