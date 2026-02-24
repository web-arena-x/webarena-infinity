# Designing your conversational messaging workflow

Source: https://support.zendesk.com/hc/en-us/articles/5746068733338-Designing-your-conversational-messaging-workflow

---

- [Messaging deployment guide:
  Introduction](https://support.zendesk.com/hc/en-us/articles/5746900266906)
- [Part 1: About conversational support with
  messaging](https://support.zendesk.com/hc/en-us/articles/4408846454682)
- Part 2: Designing your conversational messaging workflow
- [Part 3: Planning your staffing and
  operational requirements](https://support.zendesk.com/hc/en-us/articles/5746038824346)
- [Part 4: Rolling out conversational messaging
  support](https://support.zendesk.com/hc/en-us/articles/5746034323866)

Articles in the series

At its core, messaging is a way for your customers to have direct conversations with your
agents. This is known as conversational support.

As your support needs grow, you may want to automate some of this communication, such as
offering a simple greeting before handing the customer over to an agent or deflecting
inquiries using knowledge base articles. Later, design a more complex bot that automates
more of the conversation, asks the customer questions to help clearly define their
support issue, routes conversations to the right agent, collects useful data from
customers, and presents options to help them self-solve their problems. For many
accounts, the ideal configuration is somewhere in between no automations and very
complex automations.

This article contains the following topics:

- [Identifying your conversational support goals](#topic_oxk_syt_szb)
- [Choosing your messaging channels](#topic_z44_wbc_tzb)
- [Considering offline scenarios](#topic_od4_vyt_szb)
- [Choosing a conversation style](#topic_wkl_tyt_szb)
- [Considering automating conversations with bots](#topic_nfp_wyt_szb)
- [Next steps](#topic_atw_wls_b1c)

## Identifying your conversational support goals

Customers want their issues resolved quickly, through a single conversation, across a
range of channels, and without having to repeat themselves. Conversational support
with messaging provides this and more.

There are many reasons you might add conversational support, but it's important to
understand the specific reasons it's right for your organization. Your goals and
intentions should inform the decisions you make about setting up and maintaining
your conversational support workflows in the future.

To help articulate your goals, consider the following questions:

**Understanding your customers**

- What channels are your customers most likely to use?
- What are your customers' communication preferences?
- What devices do your customers use when seeking support?
- When do you receive the heaviest volumes of messages? Time of day? Day of
  the week? Specific times of month or year?
- How likely are your customers to have simultaneous separate conversations
  with your agents?

**Understanding your business**

- How long does it take for your agents to engage with a ticket? What about
  solving a ticket? On average? What about longest and shortest times?
- Are your customers satisfied with the queue wait times and resolution times?
  Are you hoping to improve customer satisfaction?
- How many agents are typically involved in solving a ticket?
- Do you need extensive reporting capabilities?
- How much of your agents' work is repetitive? How much of the repetition
  could be eliminated with bots and automation?
  - If you're planning to use bots and automation to deflect tickets
    away from agents, what are your specific goals around deflection?
    Completely deflect the tickets with self-service options? Deflect
    some of the tickets, but expect a majority to still reach an agent?
    Provide customers with more information to aid the conversation when
    an agent is available?
- What channels can you realistically support with your current organization?
  - What channels do you currently use?
  - Are there any channels you can remove because they are
    under-utilized or too expensive for the value they provide?
  - Are there specific channels you're looking to add based on agent or
    customer feedback?
  - If you're considering social messaging channels, which specific
    social channels would work well for you?
  - Are there specific types of inquiries that need more immediate,
    conversation-based support?
  - Are you able to adjust staffing and schedules to support more or
    different channels?
- How do you want to handle customer requests that come in during non-business
  hours?
- How important is efficiency? How efficient are your agents currently? Are
  you looking to increase efficiency?
- How do you route work to agents? Do you need a push-model for work
  assignment, or does a pull-model work well in your organization?

## Choosing your messaging channels

After identifying your goals for providing conversational support with messaging, you
should have a clear idea of the messaging channels you want to implement. These are
likely a compromise between what's most affordable for your company to provide and
what your customers will benefit from the most. You can choose from the
following:

- [Website channels](https://support.zendesk.com/hc/en-us/articles/4408827701530)
- [Mobile channels for Android, iOS, or
  Unity SDKs](https://support.zendesk.com/hc/en-us/articles/4408827701530)
- [Social channels](https://support.zendesk.com/hc/en-us/articles/4408831648794)

## Considering offline scenarios

Messaging offers a persistent and often asynchronous style of communication. It's
important to plan for situations where either an agent or customer isn't available
to respond immediately to a message. Consider the following common scenarios you
should take into account when designing your messaging workflows.

**Agent is offline or customer responds after business hours**

There are a few ways you can handle this scenario:

- If you have agents online 24/7, you can implement a policy that agents
  should reassign tickets before their shifts end to prevent communication
  bottlenecks from occuring while they're offline. You could
  [create a view](https://support.zendesk.com/hc/en-us/articles/4408888828570)
  of unassigned
  messaging tickets to aid in this.
- If you don't have 24/7 customer support and an end user responds to an
  unsolved ticket while your agents are offline, the agent will see the
  message in the notification list when they next sign in to Zendesk.
- For longer periods of agent unavailability, consider using the
  [Out of Office app from the Zendesk
  Marketplace](https://www.zendesk.com/marketplace/apps/support/49617/out-of-office/?_ga=2.215444375.140212733.1702309808-2105806428.1699381783).

**Customer is no longer responsive**

A conversation is considered idle if no message has been received in 10 minutes.
Likewise, users are considered idle after 10 minutes of inactivity. If an end user
stops responding mid-conversation, you have two options:

- The agent can ask whether additional help is still needed. Then, after the
  end user has been idle for 10 minutes, the agent can communicate to the end
  user that they are updating the ticket status to Pending or Solved.
- You can leverage automation to change the ticket status to Pending, Solved,
  or Closed after the 10-minute idleness threshold is reached.

In both cases, you should keep in mind that changing the ticket status to Solved
could trigger your bots to display a customer satisfaction (CSAT) query. It's
considered a best practice to exclude auto-solved tickets from the CSAT trigger, if
you have one.

**Customer responds after the ticket was solved or closed**

When a customer responds to a solved ticket, the conversation goes back to the
original agent with a status of Open. However, if a customer responds to a closed
ticket, they start over with your messaging workflow.

## Choosing a conversation style

Depending on your organizational needs, you can build a messaging workflow that's as
simple or complex as you like. We recommend adopting this golden rule: don't
over-engineer your messaging workflows.

It can be quite difficult to undo bots and automations after you've implemented them.
Therefore, it's important to be pragmatic. Design your workflows for simplicity
first. Then, as your knowledge of messaging and conversational support grows, you
can iterate and improve your messaging workflows with more complex automations.

Consider the following conversation styles:

- **Short and simple**

  If a streamlined, live chat-like approach works best
  for your agents and customers, you can implement a workflow with little or
  no automation. With minimal configuration, you can offer an automated
  greeting and create a simple form to collect essential information from the
  customer to aid the agent who helps them.
- **Intricate and comprehensive**

  Alternatively, you can use conversation bots to address
  complex customer service scenarios and provide equally complex messaging
  solutions. Conversation bots can include preconfigured options for your
  customer to choose from, pull information from external sources into the
  conversation using API calls, offer choices based on customer location or
  time of day, and more.
- **Meet in the middle**

  If you're like most Zendesk admins, you probably
  want to design a messaging workflow that falls somewhere between simple and
  intricate. You can use bots to automate as much or as little of your
  messaging workflow as you want. Just remember the golden rule: don't
  over-engineer your messaging workflows.

## Considering automating conversations with bots

While choosing your conversation style, you might have realized you want to
incorporate some bots and automations. Before you start planning it all out, it's
important to understand the three basic components of a messaging conversation:

- **Greetings**
  are
  the customer's first interaction with your customer support organization,
  either from an agent or an automated bot.
- **Self-service
  options** can be used as a next step to deflect simple tickets,
  leaving your agents more bandwidth to focus on more complex requests.
- **Conversation
  workflow**
  includes an agent's or bot's back-and-forth with
  the customer, how and when a bot passes the conversation to a live agent,
  and the path tickets take to being solved.

Each of these components can be automated, so think back to the conversation style
you want to achieve and your goals for your messaging workflow when deciding how to
configure them. Then consider the configuration options for each of these
components.

### Greetings

Greetings set the tone for the messaging conversation. When you configure a
messaging widget for web or mobile, the standard messaging response is
activated. This includes a basic conversation greeting that customers see when
they launch the widget, followed by a message letting them know they're being
connected to an agent.

The standard greeting can be
[modified](https://support.zendesk.com/hc/en-us/articles/4500737327258#topic_kzg_ync_gnb)
to suit your needs.
Similarly, you can
[configure automatic responses](https://support.zendesk.com/hc/en-us/articles/4408838007578)to new
customer requests for social messages, too.

Consider the following questions when designing your customer's first
interaction:

- What do you want your first impression to be? Casual and friendly, or
  more formal and professional?
- What information do you want to immediately convey to your customers?
  You can use an automated greeting to set customer expectations for
  services you'll provide, agent availability, and possible wait
  times.
- How personalized do you want your first message to the customer to
  be?

### Self-service

Deflecting tickets can benefit both your customers and agents by saving time and
expediting the resolution of customer issues. There are a number of ways you can
implement automated self-service options within your messaging workflow. Usually
these will come at the beginning of the conversation, but they could be useful
at other points as well.

- **Suggest help center articles**. The
  [standard autoreply bot](https://support.zendesk.com/hc/en-us/articles/6478320791962)evaluates new customer requests submitted through email or web forms for
  key concepts, identifies relevant content in your help center, and
  automatically replies to the customer request with links to the articles
  that are most likely to have the information the customer needs to solve
  their problem.
- **Provide predefined answers to common questions**. Identifying
  common questions and automating answers to them can provide customers
  with immediate answers.
- **Pull data from external sources into conversations**. Using API
  calls, you can automatically incorporate third-party data in response to
  customer requests. This is particularly helpful when customers need
  information that's updated frequently or unique to them.
- **Ask whether a question is resolved**. After providing one or more
  of the self-service options listed above, you can also prompt the
  customer to tell you whether the self-serve options resolved their
  issue. This way, they can close tickets before it gets to an agent.

### Conversation workflow

Regardless of the complexity of your messaging workflow and bots, there will
always be some customer support requests that need to be transferred to a live
agent. When configuring messaging with any level of automation, you need to
consider how and when the transfer to an agent occurs and establish rules for
how the conversation is managed after the transfer.

#### Design your bot and automation

If you choose to incorporate a conversation bot into your messaging workflow,
take time to map out the flow of the bot before you start implementing it.
It will be easier to implement a single version all at once instead of
potentially creating multiple versions if you use a phased approach.

We recommend using process mapping to create this plan, but you can use any
tool you find helpful. The important thing is that you have a visual
representation of every action the customer can take when interacting with
your conversation bot, where those actions take them, and–most
importantly–label these actions with the bot step type, feature, or
messaging functionality that makes them possible.

After you create this plan, preserve it in a way that you and your team can
refer back to.

#### Consider the handoff from bot to agent

The handoff to an agent can be a simple message letting the customer know
they're being transferred and then adding the conversation to an agent's
queue. If necessary, you can incorporate any of the following into the
handoff interaction:

- **Forms**: Gather additional information the agent might need to
  solve the customer's issue.
- **Estimated wait times**: Set customer expectations
  appropriately.
- **Notification options**: Give the customer options for how they
  want to be contacted when an agent is available to assist them.

#### Decide how conversations are routed to agents and resolved

You also need to plan how the conversation is managed after the bots hand it
off to an agent. Consider the following:

- How do agents receive messaging conversations? Are they assigned to
  groups and agents (push model) or do agents need to pick them up
  themselves from
  [views](https://support.zendesk.com/hc/en-us/articles/4408829483930#topic_gnx_2tm_vt)
  (pull model)? You
  can choose from the following options:
  - [Omnichannel
    routing](https://support.zendesk.com/hc/en-us/articles/4409149119514)
    provides Zendesk's most sophisticated
    routing logic and the ability to route tickets from multiple
    channels based on agent availability and capacity. On
    Professional plans and above, tickets can also be routed
    based on skills and priority. Omnichannel routing works out
    of the box for messaging tickets.
  - [Notification
    routing](https://support.zendesk.com/hc/en-us/articles/5020833543450#topic_nzf_pdb_pmb)
    broadcasts notifications to all agents
    for all relevant conversations. Agents can click
    *Serve
    Request*
    to start working on the message.
  - [Assigned routing](https://support.zendesk.com/hc/en-us/articles/5020833543450#topic_u3c_rrn_mpb)
    evenly distributes messaging conversations among online
    agents. Only one agent is notified for each incoming message
    at any given time.
- How are you going to notify customers when an agent enters the
  conversation?
- How are you going to manage the tickets generated by messaging
  conversations?

## Next steps

Continue walking through the
[Messaging deployment guide](https://support.zendesk.com/hc/en-us/articles/5746900266906). The next article in the
series is
[Planning your staffing and operational
requirements for messaging](https://support.zendesk.com/hc/en-us/articles/5746038824346), which will help you consider your staffing
needs for conversational messaging.