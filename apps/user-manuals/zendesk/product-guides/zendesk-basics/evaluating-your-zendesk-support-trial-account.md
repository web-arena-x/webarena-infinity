# Evaluating your Zendesk Support trial account 

Source: https://support.zendesk.com/hc/en-us/articles/4408828179482-Evaluating-your-Zendesk-Support-trial-account

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This guide shows you how to get familiar with your Zendesk trial account, helps you evaluate Zendesk features to see how they'll work for you, and provides guidelines on where to find more information. Follow the steps in this guide to get your trial account up and running. Each task typically takes less than 10 minutes to complete.

Before you begin, we recommend watching [Video: New to Zendesk?](https://fast.wistia.net/embed/channel/di1kla9in3)

- [Get to know the agent workspace](#topic_ot5_kjb_gnb)
- [Step 1: Add agents to manage tickets](#topic_gqz_cm5_w3b)
- [Step 2: Create agent groups for different ticket types](#topic_cgt_fp5_w3b)
- [Step 3: Add email addresses to match ticket issues](#topic_adk_3zb_x3b)
- [Step 4: Organize your tickets into views](#topic_wjp_21c_x3b)
- [Step 5: Create macros for consistent, canned responses](#topic_fkp_21c_x3b)
- [Step 6: Add custom ticket fields to improve ticket workflow](#topic_rjh_53v_w3b)
- [Step 7: Automate repetitive tasks with triggers and automations](#topic_rjf_xkv_w3b)
- [Step 8: Use Explore to analyze and improve performance](#topic_n4q_fcw_w3b)

## Get to know the agent workspace

Before you dive in, take some time to get familiar with the Zendesk Agent Workspace. This is where agents work on tickets, across Zendesk channels, all within a single ticket interface.

Having an understanding of how agents work with tickets will help you as an administrator.
You'll learn about key features in the following sections that you need to set up to make agents successful and efficient.

There's a sample ticket in your trial that you can open to see the agent workspace.

**To see the agent workspace**

- In **Home**, click "Sample ticket: Meet the ticket" to open the sample ticket, then click **User** in the upper-right corner.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/open_sample_ticket.png)

To learn more, see [About the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) and watch this short video.

Make the most of Agent Workspace (2:33)

## Step 1: Add agents to manage tickets

As the site administrator, you can invite agents to your trial account to work on tickets.
Each new agent you add receives a welcome email and verification link.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_adding_agents2.png)

### Plan it

You can organize agents by a variety of factors including skills, geographic locations, product type, or experience level. When you add agents consider:

- What actions do they perform?
- What workflows do they need?
- What special skills do they have?

### Try it out

For this trial, only add a few agents to test-drive your site. Later, after you plan how to arrange agents into groups and organizations, you can add them using a bulk import or through the Zendesk API.

**To add an agent**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
 **People** in the sidebar, then select **Team > Team members**.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trial_guide_agent2.png)

 You add agents in Support, but you use Admin Center to manage [user roles and access](https://support.zendesk.com/hc/en-us/articles/4408824375450) across products.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trial_guide_rolls.png)

### Learn more about agents

- [Lesson: Organizing tickets and users](https://support.zendesk.com/hc/en-us/articles/4408883609370)
- [Bulk importing users](https://support.zendesk.com/hc/en-us/articles/4408893496218-Bulk-importing-users-and-organizations)
- [Importing users with the Zendesk API](https://developer.zendesk.com/rest_api/docs/support/users)

## Step 2: Create agent groups for different ticket types

Groups collect agents together, allowing admins to manage agent ticket assignments. Groups can reflect your own internal teams, departments, or subject-matter experts. Once groups are defined, you can assign tickets to the entire group so that each member is notified and the first available agent can reply. Agents can be in more than one group at a time. It’s easy to change group members and assignments without messing with group settings.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_groups.png)

### Plan it

Identify a specific purpose for groups in your company that will use Zendesk.
What groups can you create to add value? You can report upon the performance or workload of different groups too. For example:

- Team
- Departments
- Subject matter experts

In addition to reporting on the workload or performance of individual agents, you'll now be able to do the same for your different groups.

### Try it out

For this trial, only add one or two groups and assign agents to the groups. Later, after you plan your ticket workflows, you can add more groups as needed.

**To add a group**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
 **People** in the sidebar, then select **Team > Groups**.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trial_guide_groups.png)

### Learn more about groups

- [About organizations and groups](../end-users-and-organizations/about-organizations-and-groups.md)
- [Creating groups](https://support.zendesk.com/hc/en-us/articles/4408894175130-Creating-managing-and-using-groups)
- [Managing groups](https://support.zendesk.com/hc/en-us/articles/4408821199258)

## Step 3: Add email addresses to match ticket issues

Connect your organization’s customer service email addresses to your account so that new emails begin creating tickets for your agents to manage. While you can set up any number of channels to communicate with your customers, the industry staple is still email.

When you set up Zendesk Support, you have one related email address to submit tickets:
[support@*your-account*.zendesk.com](mailto:support@myaccount.zendesk.com), but you can provide your end users with alternative email addresses, called *support addresses*. You can add as many support addresses as you need. Support addresses can be either variations of your Zendesk email address or external email addresses.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_email_support_addesses1.png)

### Plan it

You might have a single email address for all customer inquiries, or you might have many different email addresses for the unique types of queries you receive. Either way, they can all be forwarded into your Zendesk account so that tickets are automatically created for agents to manage.

Use support addresses to match your ticket issues. Consider the customer experience when configuring support email addresses. Often, the address alone can communicate the type of service provided. For example:

- support@yourcompany.com
- sales@yourcompany.com
- billing@yourcompany.com
- shipping@yourcompany.com

### Try it out

For this trial, just add one more address with @yoursubdomain.zendesk.com. Later, you can update your account to include additional support addresses or to [forward tickets](https://support.zendesk.com/hc/en-us/articles/4408887388058) to your existing support account.

**To add a support address**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
 **Channels** in the sidebar, then select **Talk and email > Email**.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trial_guide_support_address2.png)

### Learn more

- [Adding support addresses for users to submit tickets](https://support.zendesk.com/hc/en-us/articles/4408842868506-Adding-support-addresses-for-users-to-submit-tickets)
- [Incoming email requests and notifications](https://support.zendesk.com/hc/en-us/articles/4408887388058)

## Step 4: Organize your tickets into views

Views dynamically organize tickets based on specific criteria that you define. Views can be thought of as meaningful collections (or play lists) of tickets, each with their own set of filters. Views are where your agents will spend most of their time so it's critically important that they are set up in a way that actually reflects their workflow.

Using views can help you determine what tickets need attention and plan accordingly. By sharing views with your agents, you can ensure that everyone is working from the same perspective instead of leaving it up to each agent’s own interpretation.

Before you begin, we recommend watching [Video: Drive agent efficiency](https://fast.wistia.net/embed/channel/di1kla9in3?wchannelid=di1kla9in3&wvideoid=epy5b55625)

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_views.png)

### Plan it

Customize your ticket views to reflect the ideal workflow for your agents to follow based on a number of different factors. Views are commonly based on things like:

- The assigned agent or group
- Type of request
- Product
- Priority (low vs. urgent)
- Customer

It's common for administrators to create views for different teams or about different types of requests. For example, a view for technical questions and a view for billing issues. Another option might be to create views based on the customer who submitted the ticket, especially if you're supporting VIP accounts.

Once you have the right collection of tickets, you can sort the views so that the most important tickets are at the top, perhaps prioritizing the oldest tickets first.
A couple of valuable columns to include with your views are the time remaining until an SLA breach or even the predicted customer satisfaction.

### Try it out

For this trial, just add one or two views. Later, after you plan your ticket types and workflows, you can add more views as needed.

**To add a view**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
 **Workspaces** in the sidebar, then select **Agent tools > Views**.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trial_guide_views2.png)

### Learn more about views

- [Using views to manage agent workflow](https://support.zendesk.com/hc/en-us/articles/4408888828570-Using-views-to-manage-ticket-workflow)
- [Views: Best practice](https://support.zendesk.com/hc/en-us/community/posts/203188553)

## Step 5: Create macros for consistent, canned responses

Embed macros within tickets to help agents save time, automatically fill-in ticket fields, and provide consistent, thorough, and error-free responses. Macros are a predefined set of actions that agents apply to a ticket with one click.

Create macros for support requests that can be answered with a single, standard response. This saves your agents the time and effort of crafting a separate response to each customer with the same issue. Macros are more than just canned-replies to FAQs, they can provide placeholders like the customer's name and can update other ticket properties, like the type, group, and status.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_macros.png)

### Plan it

Plan and create macros so your agents can reply to common requests with a click of a button instead of typing out the same replies over and over again. Common macros include:

- Password reset
- Answering FAQs
- Assigning ticket to another agent

You can introduce macros to create better internal escalations from one agent group to another. For example, suppose an agent wants to escalate a ticket from your support team to a developer so they can investigate a bug. Developers typically need some pieces of information before they can begin their work. You can create a macro that lists what information is needed as part of an internal comment, making it easy for an agent to complete before escalating the ticket. This ensures that the developer has the information they need from the start and can get right to work.

### Try it out

For this trial, just add one or two macros for your most-common requests. Later, after you plan your ticket types and workflows, you can add more macros as needed.

**To add a macro**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
 **Workspaces** in the sidebar, then select **Agent tools > Macros**.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trial_guide_macros.png)

### Learn more about macros

- [Using macros to update tickets](../../agent-guide/ticket-automation-and-collaboration/using-macros-to-update-tickets.md)
- [Creating macros for tickets](https://support.zendesk.com/hc/en-us/articles/4408844187034)
- [Organizing and managing your macros](../../agent-guide/ticket-automation-and-collaboration/organizing-and-managing-your-macros.md)

## Step 6: Add custom ticket fields to improve ticket workflow

A ticket is a record of the conversation between the agent and the customer. Ticket fields live in the ticket sidebar and allow you to store information, route, and prioritize each ticket. Zendesk includes a default set of fields for your tickets. You can add custom fields as needed so you can categorize your tickets in whatever way makes the most sense for your business.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_ticket_fields.png)

### Plan it

Identify the most common types of requests by tracking each ticket’s topic with a custom field that your agents or customers can fill out. Custom fields provide valuable data for you for ticket processing and reporting purposes. For example:

- Issue the ticket is about
- Product in question
- Due date for resolution

Custom fields can help you analyze the types of requests you are fielding most often, those that are taking the most time to resolve, and those that are leading to happy (or unhappy) customers.

### Try it out

For this trial, add one or two custom ticket fields. Later, after you plan your ticket workflows, you can add more custom fields as needed.

**To add a custom ticket field**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
 **Objects and rules** in the sidebar, then select **Tickets > Fields**..

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trial_guide_custom_fields.png)

### Learn more about custom ticket fields

- [Adding custom fields to your tickets](https://support.zendesk.com/hc/en-us/articles/4408883152794)
- [About ticket fields](../ticket-management/about-ticket-fields.md)
- [Viewing ticket fields](https://support.zendesk.com/hc/en-us/articles/4408832419738-Managing-ticket-fields)
- [Best practices for altering your custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4408886624410-Best-practices-for-altering-your-custom-ticket-fields)

## Step 7: Automate repetitive tasks with triggers and automations

You can create triggers and automations to intelligently process tickets, reduce redundant work, and save agents' time. At their core, triggers and automations are cause and effect statements. **If** a ticket meets a set of conditions, **then** one or more actions are performed. Triggers control all the email notifications sent to your customers.
You can improve customer satisfaction with quicker updates and communication around their requests.

Triggers are **event-based** business rules you define that run immediately after tickets are created or updated. Automations are **time-based** business rules that perform an action in your account based on time elapsed. For example, a trigger could be used to immediately route a new ticket about a shipment to the Shipping department, while an automation could escalate that ticket four hours later if it hasn't been assigned to an agent.

Before you begin, we recommend watching [Video: Automate repetitive tasks](https://fast.wistia.net/embed/channel/di1kla9in3?wchannelid=di1kla9in3&wvideoid=gyr97su20q)

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_automations.png)

### Plan it

To ensure that nothing slips through the cracks, you should automate any actions that need to be completed every single time a situation calls for it. Common uses of these workflows include:

- Routing new requests to the right team
- Sending notifications to customers or agents
- Escalating tickets in need of a response

By automating stages throughout the ticket lifecycle, you can decrease handle times and reduce the number of reassignments from one agent to the next. This ultimately helps you deliver a better customer and agent experience. Your agents now spend their time helping customers instead of performing repetitive tasks.

### Try it out

For this trial, only add one trigger and one automation. Later, after you plan your ticket workflows, you can add more triggers and automations as needed.

**To add triggers and automations**

- For triggers: In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
 **Objects and rules** in the sidebar, then select **Business rules >
 Triggers**.
- For automations: In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
 **Objects and rules** in the sidebar, then select **Business rules >
 Automations**.

For this trial, do not remove any default triggers. Some default triggers are essential and control important email notifications to your customers. See [About the standard Support triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trial_guide_automations.png)

### Learn more about automating repetitive tasks

- [Routing and automation options for incoming tickets](https://support.zendesk.com/hc/en-us/articles/4408831658650)
- [Automations vs. Triggers - When to use what](https://support.zendesk.com/hc/en-us/articles/4408832924314-Automations-vs-Triggers-When-To-Use-What)
- [About triggers and how they work](https://support.zendesk.com/hc/en-us/articles/4408822236058-About-triggers-and-how-they-work)
- [Creating and managing automations for time-based events](../business-rules/creating-and-managing-automations-for-time-based-events.md)
- [About automations and how they work](../business-rules/about-automations-and-how-they-work.md)

## Step 8: Use Explore to analyze and improve performance

Zendesk Explore provides you with analytics to measure and improve the entire customer experience.

Explore comes with best practice dashboards and analysis built in, so teams of any size get the metrics that help them track towards success. You can analyze team performance, take stock of operational metrics, or get a better understanding of your customer experience.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trial_guide_explore.png)

### Learn more about Explore

- [Getting started with Explore](https://support.zendesk.com/hc/en-us/sections/360004062174)
- [Turning on pre-built dashboards](https://support.zendesk.com/hc/en-us/articles/4408846844826)

## What's next?

Congratulations! You've completed your trial set up. Here are some other things to consider:

- You can set up other channels for your account. For instructions, see [Evaluating your Zendesk Suite trial](https://support.zendesk.com/hc/en-us/articles/4408839376154) and the [Launch guide for Zendesk Suite products](https://support.zendesk.com/hc/en-us/articles/4408881507098).
- To learn more about Support, see [Getting started with Support.](https://support.zendesk.com/hc/en-us/articles/4408884056346-Introduction)
- Visit the [Zendesk Marketplace](https://www.zendesk.com/apps/) to find partners, apps, and integrations - everything you need to increase agent productivity and streamline workflows.

### Questions? Let us help

- [Contact the Zendesk support team](https://support.zendesk.com/hc/en-us/articles/4408843597850-)
- [Contact your Zendesk account representative](https://support.zendesk.com/hc/en-us/articles/4408833631002)