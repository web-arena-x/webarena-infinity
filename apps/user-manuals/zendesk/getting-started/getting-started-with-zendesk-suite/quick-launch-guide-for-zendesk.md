# Quick launch guide for Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/4408824587802-Quick-launch-guide-for-Zendesk

---

## Quick launch checklists

|  |  |
| --- | --- |
| **PEOPLE** Structure your team | [Create groups](#create-groups) - 4 mins Create containers to organize your team |
| [Add agents and admins](#add-agents-and-admins) - 6 mins Invite your team members |
| **EMAIL** Set up your email channel | [Create custom support addresses](#create-custom-support-addresses) - 6 mins Create additional Zendesk email addresses |
| [Connect your existing email](#connect-your-existing-email) - 20 mins Forward your existing email into Zendesk |
| [Customize email notifications](#customize-email-notifications) - 10 mins Brand emails with your logo and color |
| **WORKSPACE** Set up tools for agent efficiency | [Filter tickets using views](#filter-tickets-using-views) - 7 mins Organize tickets based on criteria you define |
| [Create agent macros](#create-agent-macros) - 10 mins Enable agents to make responses in one click |
| **WORKFLOWS** Set up routing and automation | [Capture data with ticket fields](#capture-data-with-ticket-fields) - 10 mins Create custom fields to capture relevant data |
| [Set up omnichannel routing](#setup-routing) - 10 mins Configure your ticket routing experience |
| [Automate workflows with ticket triggers](#automate-workflows-with-triggers) - 10 mins Create rules to help route and process tickets |

# PEOPLE: Structure your team

Let's get started by creating your groups, which are containers for organizing your staff members. Then you'll add your staff members, who are the the agents and admins who'll be working in your instance.

## Create groups

[Groups](../../product-guides/end-users-and-organizations/about-organizations-and-groups.md#topic_iny_3jg_sz) collect agents together, allowing admins to manage agent ticket assignments and access to tools like views and macros at the group level. Agents can be in more than one group at a time. It’s easy to change group members and assignments without messing with group settings.

The following example shows Chat, Talk, and Support groups.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_groups.png)

### Did you know?

Agent groups are important building blocks for creating business rules that impact ticket routing, ticket security, and ticket views. Make sure you create a comprehensive set of agent groups with consistent naming and clear definitions before you continue with the launch setup. This feature is available on all Zendesk Support plans.

### Examples

- You can define groups of agents based on the Zendesk channels they support.  
  **Zendesk > Triage > Chat, Talk, Support**
- You can define groups based on the functions agents perform, or their level of expertise.  
  **Zendesk > Triage > Sales, Finance, Shipping**  
  **Zendesk > Triage > Tier 1 Agents, Tier 2 Agents, Tier 3 Agents**

### Best practice

Groups matter because you can use them to manage ticket routing and define ticket views. Create groups with a clear purpose and give them a name that matches their function.

### Show me how

- [Create a group](https://support.zendesk.com/hc/en-us/articles/4408894175130)

## Add agents and admins

You can start adding agents and admins when you're ready. You can add them manually, through a bulk import of users, or through the Zendesk API. You must be an administrator to add agents and admins. Each new agent and admin you add receives a welcome email and verification link.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_adding_agents2.png)

### Did you know?

- You can add as many agents or administrators as you have agent subscriptions in your account.
- If you'd like to bulk import both users and organizations, you must [bulk import organizations](../../product-guides/end-users-and-organizations/bulk-importing-organizations.md) first.
- On Support Enterprise, you set the agent's groups in the agent's profile, but you do not set agent permissions or ticket access in the agent's profile. Agent permissions and access (except for groups) are determined by the [agent's custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882).
- This feature is available on all Zendesk Support plans.

### Examples

- You can add an agent and assign them to the Legal group for the North American organization with English as their preferred language.
- When you add agents, you can give senior agents permission to all tickets and give junior agents access to tickets in their group only.

### Best practices

Avoid too many cooks in the kitchen by having just a few administrators (approximately 1-5).

**Important:** At this point, you can add another admin and maybe an agent to help you with set up and testing, then add the rest of your team later. Or, you can go ahead and add everyone now. Anyone you add will receive a welcome email and have access to Zendesk.

### Show me how

- [Add an agent or admin manually](https://support.zendesk.com/hc/en-us/articles/4408886939930)
- [Bulk import users](https://support.zendesk.com/hc/en-us/articles/4408893496218-Bulk-importing-users-and-organizations)

[Back to the checklists](#checklists)

# EMAIL: Set up your email channel

Now, let's set up your email so that customers can contact you. You already have one email address in your Zendesk account, ready to use. You can create as many additional email addresses as needed. If you already have your own email address for support, you can set up forwarding into Zendesk. And you can customize your email notifications to match your brand.

To get a better understanding of how email works in Zendesk, see [The complete guide to understanding email in Zendesk](https://support.zendesk.com/hc/en-us/articles/4408888639258).

## Create custom support email addresses

Your account already provides end users with one email address to submit tickets: support@myaccount.zendesk.com. You can provide your end users with alternative email addresses called *support addresses*. You can add as many support addresses as you need. Support addresses can be either variations of your Zendesk email address or external email addresses.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_email_support_addesses1.png)

### Did you know?

This feature is supported on all Zendesk Support plans. If you plan to use Zendesk email addresses, follow the task in this section to set up alternative email addresses.

If you plan to use your own existing, external email address, you can [connect your existing support email address](#connect-your-existing-email) later. When you set up an external email address, you have an additional step to set up email forwarding. But *do not* set up [email forwarding](https://support.zendesk.com/hc/en-us/articles/4408886828698) yet. You’ll need time to finish setting up your account before you’re ready to receive emails in Zendesk.

### Examples

- training@mycompany.zendesk.com, help@mycompany.zendesk.com
- hr@mycompany.com, support@mycompany.com, webmaster@mycompany.com, ap@mycompany.com

### Best practices

Use support addresses to match your ticket issues. Consider the customer experience when configuring support email addresses. Often, the address alone can communicate the type of service provided.

### Show me how

- [Create additional Zendesk support addresses](https://support.zendesk.com/hc/en-us/articles/4408842868506#topic_kby_k3w_jw)

## Connect an existing support email address

You can use your own existing, external email address for support, if you'd like. To receive support requests at an external email address (instead of your Zendesk Support email address), you need to forward email received at your external email address to an email address in your Zendesk account.

If you're not planning on using an external email address, you can skip this step.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_email_forward2.png)

### Did you know?

You configure email forwarding in your own email account, not in Zendesk Support. Exactly how this is done depends on the email provider you're using. A number of email providers allow you to create email forwarding rules so that you can select the incoming mail that should be forwarded to your Zendesk account. This feature is available on all Zendesk Support plans. Do not set up forwarding until you are ready for all email sent to that address to become tickets in Zendesk.

### Examples

You can set up email forwarding from Microsoft Exchange and Outlook, Google Gmail, Yahoo Mail, and others.

### Best practices

Be sure to set up automatic forwarding, rather than manually forwarding. Manually forwarding an email that originates from an external support address will result in a suspended ticket.

### Show me how

- [Connect an external support email address](https://support.zendesk.com/hc/en-us/articles/4408842868506#topic_glt_l3w_jw)

## Customize your email notifications

You can customize the look and feel of email notifications sent to customers to give your account a recognizable corporate identity. All the email notifications sent from your Zendesk are formatted for both HTML and plain text emails. You can customize the HTML template to match your branding by making a few simple style changes.

If you want to edit the text in a specific email notification, you need to edit the trigger that controls the notification. There are already some [default triggers for email notifications](https://support.zendesk.com/hc/en-us/articles/4408828984346) set up in your account.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_email_template.png)

### Did you know?

The email template includes a {{content}} placeholder that displays the email content, which can include ticket comments and user profile photos. The content is defined in the [trigger](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_triggers), [automation](https://support.zendesk.com/hc/en-us/articles/4408836154266#intro_auto), or anything else that sends email from your account. This feature is available on all Zendesk Support plans.

### Examples

You can change the HTML email template to include your company logo, font type, and font colors.

### Best practices

In general, keep your customization as simple as possible. Designing HTML emails is hard because of the way HTML and CSS are rendered in different web browsers and email clients. Also certain types of formatting can trigger spam filters.

### Show me how

- [Customize templates for your email notifications](https://support.zendesk.com/hc/en-us/articles/4408886168090-Customizing-templates-for-your-email-notifications)
- [Customize the text in your email notifications](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_dwq_zoy_tb)

[Back to the checklists](#checklists)

# WORKSPACE: Set up tools for agent efficiency

Now let's set up your agents for success by giving them tools to work efficiently.

## Filter tickets using views

Use shared views to enhance agent productivity. Views dynamically organize tickets based on specific criteria that you define. Using views can help you determine what tickets need attention from you or your team and plan accordingly. Administrators can create views to share among agents and agents can create their own personal views.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_views.png)

### Did you know?

There is a pre-defined set of views provided by default for the day-to-day support workflow, which you can modify as needed. You can also create custom views. This feature is available on all Zendesk Support plans.

### Examples

- Create a view for agents to see the tickets assigned to them. Use **Ticket: Assignee is (current user)** as a condition to have the shared view dynamically change based on the agent who’s logged in.
- Create a triage view for new tickets that need to be assigned.
- Create a view for unassigned tickets received over 24 hrs ago.

### Best practices

- When you define shared views, consider the following: Are there certain tickets that take precedence over others? What are their characteristics?
- Agents can get very attached to their views. Before changing the order of shared views, or the columns and order of a view, consult with your agents.

### Show me how

- [Create a view](https://support.zendesk.com/hc/en-us/articles/4408888828570-Using-views-to-manage-ticket-workflow)

## Create agent macros

Embed macros within tickets to help agents save time and provide consistent responses. Macros are a pre-defined set of actions that agents apply to a ticket with one click. Create macros for support requests that can be answered with a single, standard response. This saves your agents the time and effort of crafting a separate response to each customer with the same issue.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_macros.png)

### Did you know?

Macros are available on all Zendesk Support plans. Unlike triggers and automations, agents must manually apply macros to tickets. Macros cannot be set up for specific channels, but you can [restrict macros by brand](https://support.zendesk.com/hc/en-us/articles/1-Restrict-macros-by-brand).

### Examples

- Your team is receiving a high number of password reset inquiries. You want to send such incoming inquiries a reply with a list of self-service instructions as well as links to help center articles.
- Occasionally, your agents receive an angry support email from unhappy customers demanding certain things. Your legal department requests that agents respond to such inquiries with pre-defined, consistent verbiage.

### Best practices

- Instead of creating a complex macro with lots of actions, create multiple macros, each with a small number of actions.
- Use in macros to personalize customer replies and avoid typos.

### Show me how

- [Create macros for tickets](https://support.zendesk.com/hc/en-us/articles/4408844187034)

[Back to the checklists](#checklists)

# WORKFLOWS: Define routing and workflows

Now let's set up your agents for success, by giving them tools to work efficiently.

## Capture more data with custom ticket fields

A ticket is the record of the conversation between the agent and the customer. [Ticket fields](../../product-guides/ticket-management/about-ticket-fields.md) live in the ticket sidebar and allow you to store information, route, and prioritize each ticket. Zendesk includes a default set of fields for your tickets. You can add custom fields as needed.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_ticket_fields.png)

### Did you know?

Support Enterprise enables you to have multiple ticket forms, so you can tailor your ticket fields to match your ticket type. Other Support plans allow only one ticket form. You can use ticket field values as input to help you manage workflows and views.

### Examples

- A real estate company might include a custom ticket field for property location.
- Finance and Purchasing departments might include a custom ticket field for PO number.

### Best practices

- Think about the data you want to collect in ticket fields and include in reports. For example, you could add an internal field that tracks what types of issues generate the most tickets.
- When you design ticket fields, think about which fields you need the end user to fill out before submitting the ticket and which fields are required for the agent to solve the ticket. Also consider which fields need to be end-user facing and which need to be internal only.
- Encourage agents to complete ticket fields as early as possible so that the ticket appears in the right views and automated workflows work as intended.
- If you add custom fields, it’s almost always best to use drop-down fields when possible. Drop-downs allow you to have nice clean reporting, apply simple business rules effectively, and simplify the experience for your agents and end users.

### Show me how

- [Add custom ticket fields to your tickets](https://support.zendesk.com/hc/en-us/articles/4408883152794)

## Set up omnichannel routing

[Omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) is the default routing experience in Zendesk Suite. It applies consistent routing logic to tickets from email, messaging conversations, and calls. Omnichannel routing is highly configurable, so admins can optimize for their unique workflows, improve agent efficiency, and increase adherence to SLAs.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocrdiag22.png)

### Did you know?

Omnichannel routing provides the only automated "push" routing model at Zendesk and it leverages many existing business rules to provide more sophisticated and effective ticket workflows. On Professional plans and above, omnichannel routing includes enhancements to existing business rule functionality, such as ticket trigger actions to assign skills and skill priorities.

### Examples

- You can prioritize work based on time to SLA breach
- You can ensure reassigned tickets are routed to the most appropriate available agents to resolve them.
- You can use custom queues to route tickets to multiple primary and secondary groups of agents, which helps decrease first response time.

### Best practice

Omnichannel routing is the best way to direct tickets to agents. You can start with the standard set up and configuration, then add more complex options as your workflows evolve. It's best to review options and have a plan before you modify your routing configuration.

### Show me how

- [Turning on and setting up omnichannel routing](https://support.zendesk.com/hc/en-us/articles/5866925319962)

## Automate workflows with triggers

You can create [triggers](https://support.zendesk.com/hc/en-us/articles/4408822236058) to intelligently process tickets and save agents time. Triggers are **event-based** business rules you define that run immediately after tickets are created or updated. At their core, triggers are cause and effect statements. **If** a ticket meets a set of conditions, **then** an action is performed.

You can create an unlimited number of triggers based on your business needs. For example, you might have a trigger that automatically replies to customers when they create a new ticket, or you might have a trigger that automatically assigns a high priority to tickets from VIP customers.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/launch_guide_triggers2.png)

### Did you know?

Zendesk Support has a [few default triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346) that you may want to deactivate or alter. If you don’t check through your list of triggers before you go live, you may end up with an inbox full of unwanted notifications. Triggers are available on all Zendesk Support plans.

### Examples

You can use triggers to:

- Notify customers when you’re out-of-office
- Send customer satisfaction score follow-ups
- Route your priority customers to a specialized support group automatically
- Notify agents when a problem ticket has reached a certain number of incidents

### Best practices

- Be as specific as possible when building triggers. One way to do this is to use the “Ticket is” condition to define whether the trigger fires at ticket creation or update.
- Triggers can affect one another, so it’s important to think about the order of triggers to make sure you don’t have an unexpected, cascading effect. See [Understanding when triggers run and fire](https://support.zendesk.com/hc/en-us/articles/4408822236058#h_15524764971513292862138).
- If you are not sure your triggers are behaving as expected, you can [view all events of a ticket](https://support.zendesk.com/hc/en-us/articles/4408829602970) to see which triggers have affected that ticket and help you troubleshoot any issues.

### Show me how

- [Create a trigger](https://support.zendesk.com/hc/en-us/articles/4408886797466)

[Back to the checklists](#checklists)