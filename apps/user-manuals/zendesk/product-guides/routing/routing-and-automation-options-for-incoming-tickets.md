# Routing and automation options for incoming tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408831658650-Routing-and-automation-options-for-incoming-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Improve your ticket workflows by using routing and automation options. Choose between push and pull models to assign tickets to agents or let them self-assign. Utilize business rules like triggers, automations, and macros to automate actions and keep tickets moving. Explore omnichannel routing for consistent logic across channels, and consider skills-based routing for specialized handling.

One of the best ways to increase agent efficiency and streamline your support tasks is
to use routing options to manage your ticket workflows.

Zendesk provides a number of business rules and routing options to make sure
your tickets get to the right agent as quickly as possible. You can either configure a
"push" routing model, which assigns tickets to agents, or a "pull" model, where agents
assign work to themselves. This article explains these options and how they can be
combined to meet your unique needs.

This article contains the following topics:

- [About the standard Zendesk ticket routing framework](#topic_wl4_cwk_wxb)
- [Understanding the routing models](#topic_fxc_1zk_wxb)
- [Using business rules and configuration options to automate ticket workflows and routing](#topic_pd3_d4n_cyb)

## About the standard Zendesk ticket routing framework

When you create an account, you can start receiving support requests right
away using the default support email address created during the registration
process. All support requests sent to your account, via email or another channel,
automatically become tickets in your system. Zendesk provides standard [views](https://support.zendesk.com/hc/en-us/articles/4408829483930#topic_gnx_2tm_vt) and [triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346) that work together to create a basic routing
framework for tickets.

Without any configuration beyond the initial registration process, the
standard triggers and views work together so that every new and updated ticket
appears in at least one view and triggers at least one notification.

When a new ticket is submitted to your support address, it appears in the
following standard views and could appear in others depending on your plan type and
other agents on your account.

- Your unsolved tickets
- All unsolved tickets
- Recently updated tickets

When a ticket is created or updated, the following standard triggers fire:

- Notify requester and CCs of received request
- Notify all agents of received request

In this basic framework, agents can use the trigger notifications and views to assign
tickets to themselves or tickets can be assigned to them manually.

## Understanding the routing models

In the simplest workflows, fine-tuning the standard views and triggers might provide
sufficient routing. However, even simple workflows can benefit from more advanced
routing logic. There are two types of routing models you can configure: "push"
models, which assign tickets to agents, or a "pull" models, where agents assign work
to themselves.

### Routing models

You can configure the following routing models:

- Push routing models:
  - **Omnichannel routing**: Route tickets from [email (including web form,
    side conversations, and API)](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb), calls, and messaging
    conversations based on agent status and capacity. On
    Professional and Enterprise plans, you can also route tickets
    based on priority and skills. On all plans, you can run triggers
    against new tickets from all channels, and you can use triggers
    to set and manage skills on tickets. See [About omnichannel routing
    with unified agent status](https://support.zendesk.com/hc/en-us/articles/4409149119514) and [Using skills with omnichannel
    routing](https://support.zendesk.com/hc/en-us/articles/5833468891674#topic_d2l_bnx_txb).
  - **Round robin**: A way to assign tickets by rotating through
    your agents. Round robin ticket management ensures tickets are
    distributed evenly among agents, but doesn't consider ticket
    complexity or expertise requirements. You can configure
    omnichannel routing to assign based on round robin rather than
    spare capacity. See [Using round robin routing for
    email, messaging conversations, and call
    tickets](https://support.zendesk.com/hc/en-us/articles/7990049158554).
  - **Manual ticket assignment**: Manually triage tickets and
    assign them to your agents. This works best for small teams with
    low-volume ticket queues. This routing model is best used in
    conjunction with [other business rules and configuration options](#topic_pd3_d4n_cyb).
- Pull routing models
  - **Play mode**: Play mode allows agents to click through a
    view using the play button and be assigned to the next available
    ticket automatically. Play mode can be restricted to only
    display tickets from a specific view and, on Enterprise plans,
    admins can configure [Guided mode](https://support.zendesk.com/hc/en-us/articles/4408825479066) so agents
    are only allowed to access tickets using the Play button.
    See [Using the Play button](https://support.zendesk.com/hc/en-us/articles/9186492658714)
    and [Using a Play button-centered
    workflow](https://support.zendesk.com/hc/en-us/community/posts/209299228).
  - **Standalone skills-based routing**: Skills are agent
    attributes that determine an agent's suitability to work a ticket
    that requires them. Skills can be used as a standalone routing
    method, where agents use filtered views to assign tickets with
    matching skills to themselves, or as part of omnichannel routing
    (push method). [See About using skills to
    route tickets](https://support.zendesk.com/hc/en-us/articles/5833468891674).
  - **Manually self-assigning tickets from views**: Allow agents
    to assign tickets directly to themselves from views. Letting
    agents choose their own work at their own pace can work well for
    some small teams, but can quickly become unmanageable.

### Deciding whether to use omnichannel routing

Omnichannel routing is Zendesk's most sophisticated and complete routing
solution. It provides consistent routing logic across the email (including web
form, side conversations, and API), messaging, and voice channels. Tickets are
assigned to agents based on their [availability](https://support.zendesk.com/hc/en-us/articles/5133523363226) and [capacity](https://support.zendesk.com/hc/en-us/articles/4776409839770). On Professional plans and
above, tickets can also be routed based on priority and [skills](https://support.zendesk.com/hc/en-us/articles/4408838892826). Using omnichannel routing also
means agents can set a single unified status for all channels rather than
setting statuses for each channel separately.

When using omnichannel routing, tickets are created as soon as a request is
received from any channel. This means triggers can be run on all channels,
including the voice channel. Additionally, omnichannel routing enables you to
use triggers to assign skills to tickets. This means skills can be automatically
updated when tickets are created or updated, not just upon creation.

With omnichannel routing, you can also organize your tickets into [multiple queues](https://support.zendesk.com/hc/en-us/articles/6712096584090). Creating additional
queues allows you to use all of the omnichannel routing logic but
route tickets to different groups of agents and even specify secondary (also
known as fallback) groups for each queue.

So, is omnichannel routing the right routing solution for you? Consider the
following:

- Omnichannel routing has some [requirements and limitations](https://support.zendesk.com/hc/en-us/articles/4409149119514)
  to be aware of before choosing this routing solution.
- What Zendesk account plan do you have? See the [Summary of features by plan](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_r5j_c3p_m5b) to
  ensure you'd have access to the functionality you want to use.
- The size of your organization. Omnichannel routing will provide
  increased efficiency at any scale, but especially for larger and more
  complex organizations.
- The [channels](https://support.zendesk.com/hc/en-us/articles/4408824097050) through which you
  receive tickets. Even if you only use one of the channels supported by
  omnichannel routing, it can still be a great fit as your routing
  solution. However, it also means simpler routing solutions could also
  work well for you.
- The business rules you already have in place to help route tickets.
  Standard triggers and views provide a simple, but effective routing
  framework. You may have added new ones or modified the originals. Are
  those business rules accomplishing what you want? What, specifically,
  are you looking to address by considering alternative routing solutions?

After considering all of this, if you've decided to use omnichannel routing, see
[About omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514), [Turning on omnichannel routing](https://support.zendesk.com/hc/en-us/articles/5866925319962), and
[Managing your omnichannel routing
configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210).

If, on the other hand, you want to use routing solutions such as standalone
skills-based routing, play mode, or some custom solution, revisit the list of
[tools and configuration
options](#topic_fxc_1zk_wxb) you can use.

## Using business rules and configuration options to automate ticket workflows and routing

The following business rules and configuration options can also be used to define and
automate ticket routing behavior within Zendesk's routing solutions or in a custom
configuration. Different tools are most helpful at different points in the ticket
workflow, so they're organized accordingly:

- [Kicking off the ticket workflow](#topic_dcd_pvh_qbc)
- [Performing automated actions to keep things moving](#topic_h5j_dwh_qbc)
- [Monitoring your ticket workflows](#topic_azx_wyh_qbc)

Additionally, you can refer to [Recipes
for automated ticket workflows](#topic_ym1_p13_qbc) to see some examples of how these business
rules and configurations can be used together.

### Kicking off the ticket workflow

The following business rules and configuration options are commonly used early in
the ticket workflow because they can be leveraged by other business rules later
in the workflow.

- **Support addresses**: By default, you have one email address for
  users to submit tickets to. Using multiple Support email addresses
  provides a way to route tickets based on the email address the customer
  used to contact support. See [A complete guide to understanding
  email in Zendesk: How the email channel works](https://support.zendesk.com/hc/en-us/articles/4408888639258) and [Adding support addresses for users to
  submit tickets](https://support.zendesk.com/hc/en-us/articles/4408842868506).
- **Ticket forms**: A predefined set of ticket fields for support
  requests. Using multiple ticket forms provides a way to collect more
  specialized information from customers. This helps ensure agents have
  the information they need to assist the customer, but also makes it
  possible to route tickets based on the ticket form that the customer
  used. See [Creating multiple ticket
  forms](https://support.zendesk.com/hc/en-us/articles/4408846520858), [Presenting ticket forms to end
  users](https://support.zendesk.com/hc/en-us/articles/4408842873498), and [Adding custom fields to your tickets
  and support requests forms](https://support.zendesk.com/hc/en-us/articles/4408883152794). (Suite Growth and above or
  Support Enterprise)
- **Tags**: A word or phrase you can use to add more context to ticket
  and incorporate into business rule logic. You can also search for
  tickets by tags and use tags when configuring views. See [About tags](https://support.zendesk.com/hc/en-us/articles/4408888664474) and [Working with ticket tags](https://support.zendesk.com/hc/en-us/articles/4408835059482).
- **Channels**: The way you communicate with your customers and can be
  used as a condition in triggers to route tickets based on the channel
  through which it was received. See [About Zendesk channels](https://support.zendesk.com/hc/en-us/articles/4408824097050).
- **Service Level Agreements (SLAs)**: An agreed upon measure of the
  response and resolution times that your support team delivers to your
  customer. SLAs are great stand-alone tools to help you attain your
  service goals. However, they can also be used as conditions in views and
  automations to reroute and prioritize tickets based on service promises
  made to customers. See [About SLA policies and how they
  work](https://support.zendesk.com/hc/en-us/articles/5600997516058) and [Defining SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866).
  (Professional and Enterprise)
- **Custom ticket fields**: You can customize your ticket forms and web
  forms to require certain information from customers before a ticket is
  accepted into the queue or you can add custom ticket fields to the
  tickets themselves. Then you can use that information as conditions in
  business rules to route tickets. Information stored in custom ticket
  fields can also help agents have necessary context for tickets. Examples
  of how you can use custom ticket fields include: a *Language* field
  to automate routing to an agent who speaks that language or asset
  management fields such as *order number* or *product type* to
  help surface key information.
- **Intelligent triage** (Copilot add-on): If you [use intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538), you
  can automatically route email and messaging tickets to the right teams
  based on what the ticket is about (its intent), the language it's
  written in, whether the customer's message is positive or negative (its
  sentiment), or a combination of all three. See [Choosing a routing method for
  automatically triaged tickets](https://support.zendesk.com/hc/en-us/articles/4973607684506).

### Performing automated actions to keep things moving

The following business rules are used to actually perform automated actions when
tickets meet certain criteria. You can define ticket criteria based on the
business rules and configuration options listed under [Kicking off the ticket
workflow](#topic_dcd_pvh_qbc).

- **Triggers**: Event-based business rules that perform actions any
  time a ticket is created or updated. They can send notifications and
  modify ticket properties. See [About Zendesk triggers and how they
  work](https://support.zendesk.com/hc/en-us/articles/4408822236058), [About the standard ticket
  triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346), and Creating ticket triggers.
- **Automations**: Time-based business rules that perform actions based
  on time elapsed. Similar to triggers, they can send notifications and
  modify ticket properties. See [About automations and how they
  work](https://support.zendesk.com/hc/en-us/articles/4408832701850) and [About the standard Support
  automations](https://support.zendesk.com/hc/en-us/articles/4408835051546).
- **Macros**: Predefined set of actions that agents apply to a ticket
  with one click. Macros can be used to automatically fill in ticket
  fields and provide consistent responses, saving your agents time and
  effort for common questions and scenarios.

### Monitoring your ticket workflows

The following business rules and configuration options can help you monitor the
ticket workflow and ensure tickets keep moving through it.

- **Views**: A way to organize tickets based on certain criteria. You
  can think of them as containers for your tickets. A single ticket can
  appear in multiple views or no views at all. When you begin using
  Support, every ticket appears in at least one [standard view](https://support.zendesk.com/hc/en-us/articles/4408829483930#topic_gnx_2tm_vt). You can also
  define targeted views, which allows agents to self-assign tickets from a
  pre-filtered set of tickets in their view. See [Creating views to build customized lists of tickets](https://support.zendesk.com/hc/en-us/articles/4408888828570).
- **Explore reporting**: [Explore](https://support.zendesk.com/hc/en-us/articles/4408831710618) data sets now include
  a lot of information about channel, routing, and agent capacity and
  availability. See [Analyzing your Support ticket
  activity and agent performance](https://support.zendesk.com/hc/en-us/articles/4408835846810).

### Recipes for automated ticket workflows and routing

These articles provide some examples of how you can use these Zendesk business
rules and configuration options together to automate ticket workflows and
routing:

- [Streamlining your Support
  workflow](https://support.zendesk.com/hc/en-us/articles/4408889268378)
- [Workflow: Using omnichannel routing
  to achieve first reply time SLAs](https://support.zendesk.com/hc/en-us/articles/6865919184282)
- [Workflow: Using skills to route calls
  to specific agents with omnichannel routing](https://support.zendesk.com/hc/en-us/articles/5897949816730)
- [Workflow recipe: Manage outages using
  SLA policies](https://support.zendesk.com/hc/en-us/articles/4408834732954)
- [Workflow recipe: Using triggers to
  manage requests from important customers](https://support.zendesk.com/hc/en-us/articles/4408842979994)
- [Workflow recipe: Funneling orders
  through Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408882427418)
- [Workflow recipe: Creating an approval
  process](https://support.zendesk.com/hc/en-us/articles/4408832737818)
- [Workflow recipe: Sending automated
  ticket reminders to customers](https://support.zendesk.com/hc/en-us/articles/4408832749210-Sending-automated-ticket-reminders-to-customers)