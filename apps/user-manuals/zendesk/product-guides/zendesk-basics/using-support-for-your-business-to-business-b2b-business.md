# Using Support for your Business-to-Business (B2B) business

Source: https://support.zendesk.com/hc/en-us/articles/4408825510938-Using-Support-for-your-Business-to-Business-B2B-business

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Dave is an Engineering Manager at BestAds, a startup that makes marketing
software. His team uses a source code storage application from MegaCorp. They are having
trouble checking in their source and are seeing an error message each time they attempt
a check-in. Dave goes to the MegaCorp help center and looks for information about the
error message, but doesn’t find anything that matches his issue. He uses the Web Widget
(Classic) to submit a request. MegaCorp gets the ticket and Dave gets notified. The
MegaCorp Customer Support, Engineering, and Documentation teams reply to the various
questions/comments on the ticket, and then someone sends Dave instructions about what to
do next. The ticket can then be closed.

This article contains the following sections:

- [How can views help my B2B business?](#topic_afj_j5z_hlb)
- [How can organizations and groups help my B2B business?](#topic_rlq_j5z_hlb)
- [How can ticket fields help my B2B business?](#topic_n1r_j5z_hlb)
- [How can business rules help my B2B business?](#topic_k4r_j5z_hlb)
- [How can macros help my B2B business?](#topic_pt1_db1_3lb)
- [How can a help center help my B2B business?](#topic_nbq_2b1_3lb)
- [How can apps and integrations help my B2B business?](#topic_pwq_2b1_3lb)
- [How can Web Widget (Classic) help my B2B business?](#topic_r4p_hc1_3lb)
- [How can support addresses help my B2B business?](#topic_ejq_hc1_3lb)

## How can views help my B2B business?

Views are a way to organize your tickets by grouping them into lists based
on certain criteria. Using views can help you determine what tickets need attention
from you or your team and plan accordingly.

As a member of the customer service team, it’s important to be able to
easily see open support requests and who is currently responsible for actioning
them. You can take this further by using an [about field](https://support.zendesk.com/hc/en-us/articles/4409155792026) to create custom categories for your
different software products. If you make the about field required to solve a ticket
then you’ll be able to easily categorize your support calls.

### Example

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Views_b2b_1.png)

In this example, the view is configured to display open tickets for the
“Mega software tax” software that are assigned to the “Assistance” group. The
**Ticket: Software package** field is used as the about field.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Views_b2b_2.png)

### Related articles

- [Creating views to manage ticket
  workflow](https://support.zendesk.com/hc/en-us/articles/4408888828570)

## How can organizations and groups help my B2B business?

As a B2B business, you will probably use organizations and groups to
organize the people in your Zendesk Support account.

Organizations and groups are often used to:

- Escalate tickets based on complexity
- Support service-level agreements
- Provide support by expertise
- Support customers by location and language

You may also want to use organizations to tightly manage your workflow and
create security boundaries by funneling tickets directly to agents who have
restricted access.

### Example

Let’s say that you are MegaCorp, the software company that produces a widely-used
source code storage application. Many other software companies use this
application while they are building their own products, checking their own code
in to and out of repositories, making the reliability of your product very
important to them.

You may want to create organizations for each of the software companies
you work with. You can then add “conditions” based on those organizations to
your triggers, automations, macros, and views to make it easier to work with
your tickets.

Each of these organizations is a software company that uses your
source-code software:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_people_orgs.png)

You may want to create groups based on departments or divisions in your
company (for example, Engineering, Legal, Program Management, Sales,
Documentation). You can add “actions” based on groups to triggers, automations,
and macros, but not views.

Each of these groups are a department at your company:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_people_groups.png)

### Related articles

- [About organizations and
  groups](https://support.zendesk.com/hc/en-us/articles/4408886146842)
- [About triggers and how they
  work](https://support.zendesk.com/hc/en-us/articles/4408822236058)
- [About automations and how they
  work](https://support.zendesk.com/hc/en-us/articles/4408832701850)
- [Using macros to update
  tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602)
- [Creating views to manage ticket
  workflow](https://support.zendesk.com/hc/en-us/articles/4408888828570)

## How can ticket fields help my B2B business?

Ticket fields include data that agents need in order to solve a problem. In
order to use ticket fields effectively, it’s important to learn about the different
types of ticket fields—there are system fields and custom ticket fields. Also, make
sure you understand what kinds of permissions you can set on a ticket field, the
relationship between ticket fields and ticket forms, and where ticket fields will
appear to your agents and end users.

Ticket fields and ticket forms are very customizable. It’s worth spending
some time to figure out how to use them in a way that works best for you. This often
reduces resolution times and improves customer satisfaction.

As a B2B business, when you get a request, you want to know certain
information right away. You don’t want to have to go back to the customer and ask
for more information. That takes time and can slow down resolution.

### Example

Let’s say that you are MegaCorp, the software company that produces a
widely-used source-code storage application. Many other software companies use
this application while they are building their own products, checking their own
code in and out of repositories, which make the reliability of your product very
important to them.

You have a custom ticket field called “Plan type.” It’s a drop-down
list that includes options for Platinum, Gold, Silver, and Bronze. You want to
make sure that your Platinum customers are routed to a special group of agents
and receive special care.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_fields_dropdown.png)

You set permissions on the “Plan type” field and enter the values that
will appear in the drop-down list.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_fields_permissions.png)

Finally, after you create the ticket field, you add it to your default
ticket form. Here’s what your customer sees when they go to submit a
request:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_fields_ww_request.png)

You have triggers that automatically route tickets based on plan type. When a
Platinum customer submits a support request, the ticket is immediately assigned
to a special group of agents, and can be processed quickly.

### Related articles

- [About ticket fields](https://support.zendesk.com/hc/en-us/articles/4408886739098)
- [Adding custom fields to your tickets and
  support request form](https://support.zendesk.com/hc/en-us/articles/4408883152794)

## How can business rules help my B2B business?

As a B2B business, business rules can help your business to automatically
reply to customers when their request is received or when their request is updated,
notify customers about your standard operating hours (business hours), and help you
remind customers when they don’t reply to requests for more information.

### Triggers example

Because MegaCorp is getting so many customer tickets about check in
errors, they have created a special trigger to help them manage the ticket
volume. This trigger automatically looks for the error number in the ticket
content and routes the request to a special group they set up to triage these
tickets. It also updates the ticket priority and sends an email to the requester
with an estimate on when the issue will be fixed.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_trigger_conditions.png)

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_trigger_actions.png)

Here’s an example of the email message Dave would receive:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_trigger_email.png)

### Automation example

After the 1 hour window has expired and the issue is fixed, this
automation sends an email to ticket requesters to let them know they can resume
their check ins. It also includes information on who to contact if they are
still having trouble.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_automation_conditions.png)

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_automation_actions.png)

Here’s an example of the email Dave would receive:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_automation_email.png)

### Related articles

- [About triggers and how they
  work](https://support.zendesk.com/hc/en-us/articles/4408822236058)
- [About automations and how they
  work](https://support.zendesk.com/hc/en-us/articles/4408832701850)
- [Routing and automation options for
  incoming tickets](https://support.zendesk.com/hc/en-us/articles/4408831658650)

## How can macros help my B2B business?

Macros are a pre-defined set of actions that agents apply to a ticket with
one click. You can create macros to address support requests that can be answered
with a single, standard response, and embed macros within tickets to help agents
quickly provide consistent responses. This saves your agents the time and effort of
crafting a separate response to each customer with the same issue.

**Macros can:**

- Add comment text
- Update ticket fields (drop-down and checkboxes)
- Add or remove ticket tags
- Add CCs
- Change the assignee
- Set the ticket subject (title)
- Add attachments to ticket comments

As a B2B business, you can use macros to direct customers to help center
articles to answer common questions, ask customers to provide more information, or
ask customers to be patient during high traffic volume.

### Example

When the agents in the Checkin Triage group receive the checkin failed
tickets, they notice that a few of the tickets they received include two error
numbers (error\_547 and error\_001) instead of just one. These errors show that
there are two issues causing checkin to fail for these customers: a software
failure on the MegaCorp site and a password authentication issue.

Once the checkin software is fixed on the MegaCorp site and the first
problem is solved, the Checkin Triage agents can then open a ticket and apply a
macro that specifically describes how these customers can solve the
authentication issue by resetting their password.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_macro.png)

### Related articles

- [Creating macros](https://support.zendesk.com/hc/en-us/articles/4408844187034)
- [Using macros to update
  tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602)
- [Macros resources](https://support.zendesk.com/hc/en-us/articles/4408824631578)

## How can a help center help my B2B business?

A [help center](https://support.zendesk.com/hc/en-us/articles/4408846795674) provides a smart
knowledge base for better self-service. You can set up your knowledge base to
contain information (articles) covering frequently-asked questions, policies,
product details, and more, to help users find the information they need, without
having to raise a support ticket.

As a B2B customer, you can create FAQ or What’s New topics, for example,
that contain articles about troubleshooting or return policies, or any type of
information that you want to present to help answer everyday questions.

The [TechSmith help center](https://support.techsmith.com/hc/en-us) does a great job of showing
the topics with the most asked questions using a variety of graphic sizes, and
includes products and other areas, such as buying and licensing:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_hc_customer_site.png)

You’ll need to [enable your help center in setup
mode](https://support.zendesk.com/hc/en-us/articles/4408846795674#topic_ndf_fpf_mk), and then you can start adding content before you [activate it](https://support.zendesk.com/hc/en-us/articles/4408846795674#topic_ckn_wc4_qy).

You can start small with just a few articles that answer the most commonly-asked
questions. For example, you could write an article explaining common problems and
how to resolve them, or configuration guidance. The more articles you write, the
more your Support agents can concentrate on answering the tricky questions and
problems.

You need to be a Knowledge admin or an agent with [management permissions](https://support.zendesk.com/hc/en-us/articles/4408827952538) to create an article. See [Creating and editing an article](https://support.zendesk.com/hc/en-us/articles/4408839258778) for full
instructions.

### Example

If you create an article describing how customers can troubleshoot
source code check in issues, and add labels like **troubleshoot** and
**checkin** to the article to boost it in search results (labels are not
available on Suite Team), then Dave could search and find this information and
might not need to raise a ticket.

Your article might look like this in draft format:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_hc_draft_article.png)

### Related articles

- [Getting started with your help
  center](https://support.zendesk.com/hc/en-us/articles/4408846795674)
- [Creating and editing an
  article](https://support.zendesk.com/hc/en-us/articles/4408839258778)

## How can apps and integrations help my B2B business?

B2B companies are using a variety of apps in the [Zendesk
Marketplace](https://www.zendesk.com/apps/) and integrations to customize their platform or
solution. Here are a few apps which can support your B2B business.

### SLA Event tracker app

Businesses that have a Service Level Agreement (SLA) can use the SLA
Event Tracker app which displays SLA data when viewing the ticket.

In this example, the SLA metrics are set up in the app to address an
issue. An agent in MegaCorp Customer Support can view the ticket Dave has
created and see SLA metrics when the issue has been actioned, completed, or
breached.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_sla_tracker.png)

To learn more about the app, see [Installing and using the SLA Event Tracker
app](https://support.zendesk.com/hc/en-us/articles/4409148550554).

### Attachment manager app

The Attachment Manager app helps manage attachments for tickets in your
ticket sidebar. It provides several features including an attachment library,
restricting attachment types for security or compliance purposes, and the
ability to redact attachments.

In this example, workaround documentation provided by the Engineering
team is attached to a ticket so Dave can resolve the issue himself. The document
is then stored in the attachment library so it can be attached to tickets with
the same issue.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_attachment_manager.png)

To learn more about the Attachment Manager app, see [Installing and using the Attachment
Manager app](https://support.zendesk.com/hc/en-us/articles/4408823467674).

### Jira integration

The Jira integration encourages collaboration between support teams and
engineering teams by linking, syncing, and tracking Support tickets and Jira
issues.

The app downloaded from the Zendesk Marketplace integrates with Jira in
Support. In the ticket editor, an agent can create a Jira issue or link a ticket
with a Jira issue. They have visibility on the progress of any Jira issues
linked to the Zendesk ticket.

In this example, an agent creates a Jira issue for Dave in the Support
ticket sidebar.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_jira1.png)

An agent can see the Jira issue associated with the ticket and
customize the information they want to see.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_jira3.png)

The Zendesk app downloaded from the Atlassian Marketplace integrates
with Jira Cloud and Jira Server. It provides engineering teams visibility of
Support tickets associated with the Jira issues they are working on. They can
see linked ticket details and all communications with customers. And they can
link tickets to Jira issues and add comments to tickets in Jira.

In this example, the engineering team can see in Jira the Support
ticket associated with the issue that was created by an agent.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_jira2.png)

For more information about the Jira integration, see [Jira integration resources](https://support.zendesk.com/hc/en-us/articles/4408845662746).

## How can Web Widget (Classic) help my B2B business?

[Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408833907354) is a separate
web application that is embedded in a web page. It gives customers access to your
help center and the agents in your Zendesk support channels.

By embedding Web Widget (Classic) in your website, it encourages customers
to self-serve by searching for help center articles and the widget providing article
suggestions. It can also make it easier to get help from an agent by displaying
ticket forms for support requests, request a call back, and start a chat.

Web Widget (Classic) can be configured in your [Support Admin](https://support.zendesk.com/hc/en-us/articles/4408838063258). Zendesk also provides [Web Widget APIs](https://developer.zendesk.com/embeddables/docs/widget/introduction) to extensively
configure and customize the widget to suit your needs. For example, you can choose
which channels you would like to show on a particular web page, or enable Google
Analytics tracking to see how your customers are interacting with widget.

### Example

In this example, the Web Widget (Classic) is configured in Support
under **Admin** > **Channels** > **Web Widget (Classic)**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_web_widget.png)

Help Center search and Contextual Help is enabled to create ticket
deflection. So Dave must first search and find articles to help address his
issue.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_web_widget_ex_1.png)

Ticket forms is enabled so Dave can submit a ticket if he is unsuccessful in
finding a help center article that addresses his issue.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2b_web_widget_ex_2.png)

### Related articles

- [Providing omnichannel support using Web
  Widget (Classic) for the Suite](https://support.zendesk.com/hc/en-us/articles/4408844047898)
- [Web Widget (Classic)
  resources](https://support.zendesk.com/hc/en-us/articles/4408833907354)
- [Using Web Widget (Classic) to embed
  customer service in your website](https://support.zendesk.com/hc/en-us/articles/4408836216218)

## How can support addresses help my B2B business?

Support addresses are email addresses that allow your users to submit
support tickets. You can add as many support addresses as you need. Support
addresses can be either variations of your Zendesk email address or external email
addresses. Any email address you want to use to receive support request as tickets
(whether it's a Zendesk address or an external address) must be added to your
Zendesk as a support address.

By creating multiple support addresses, a B2B company can route support
tickets directly to agents, or groups, who are trained to handle the issue at hand.
Support addresses can be based on task or department (TechSupport, Billing, etc.),
location (such as city, time zone, or region), language -- really, anything that
works for your business.

You can create as many support email addresses as you need. They can be
used throughout your Zendesk to help you organize and direct your support requests
to your agents:

- [Create views](https://support.zendesk.com/hc/en-us/articles/4408888828570) that organize tickets
  based on which address received them.
- [Customize email notifications](https://support.zendesk.com/hc/en-us/articles/4408886168090) for each
  support address, to automatically reply to incoming requests.
- [Build triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466), using email addresses
  as a condition. For example, you can add tags or priority levels to tickets, or
  assign them to specific groups or agents, based on which email address received
  them.
- [Create reports](https://support.zendesk.com/hc/en-us/articles/4408821589530) to monitor how many
  tickets are generated through email addresses, and write custom formulas to
  break down how each address is performing.

### Example

By creating multiple support addresses, MegaCorp can route its
customers’ support tickets directly to the department that can best handle the
issue.

In the sample scenario above, here’s how having an issue-specific
support address might work:

Dave goes to the MegaCorp website and clicks the **Support** link.
On the web page, he sees a list of potential reasons for contacting MegaCorp,
each with a different email address associated with it:

Billing problem? Contact [billing@megacorpinc.com](mailto:billing@megacomputersinc.com)

Technical problem? Contact techsupport[@](mailto:returns@megacomputersinc.com)[megacorpinc.com](mailto:billing@megacomputersinc.com)

Something else you want help with? Contact [support@](mailto:other@megacomputersinc.com)[megacorpinc.com](mailto:billing@megacomputersinc.com)

Dave clicks techsupport[@](mailto:returns@megacomputersinc.com)[megacorpinc.com](mailto:billing@megacomputersinc.com), fills out the support form, and clicks
**submit**.

All tickets sent through that email address are routed to a view
monitored by the tech support department. A ticketing triage agent sees that
Dave’s problem is related to source code storage, flags the ticket as Urgent,
and reassigns it to an agent with storage expertise. The agent contacts Dave
immediately and walks him through the steps required to resolve the issue.

### Related articles

- [Adding support addresses for users to
  submit tickets](https://support.zendesk.com/hc/en-us/articles/4408842868506)
- [Top feature recommendations for
  business-to-business (B2B) support](https://support.zendesk.com/hc/en-us/articles/5194505387674-Top-feature-recommendations-for-business-to-business-B2B-support-)