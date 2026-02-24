# Using Support for your Business-to Employee (B2E) business

Source: https://support.zendesk.com/hc/en-us/articles/4408832551706-Using-Support-for-your-Business-to-Employee-B2E-business

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Jane is an IT support analyst working for a large corporation, MegaCorp, and supports the London office. A member of the MegaCorp HR team in London, Dan, has a problem with his computer and opens a support ticket. Jane gets a notification email and opens their Zendesk Support. She realizes that this problem can be fixed by a software update. In the ticket, Jane asks Dan to give her a convenient time to perform the update. After a time is agreed, Jane updates the computer, verifies that Dan is satisfied, then solves the ticket. Finally, she updates the in-house documentation to inform other users what to do if they get the problem.

This article contains the following sections:

- [How can views help my B2E business?](#topic_afj_j5z_hlb)
- [How can organizations and groups help my B2E business?](#topic_nk3_m5z_hlb)
- [How can ticket fields help my B2E business?](#topic_gw3_m5z_hlb)
- [How can business rules help my B2E business?](#topic_jhj_m5z_hlb)
- [How can macros help my B2E business?](#topic_mjg_gxz_hlb)
- [How can a help center help my B2E business?](#topic_ifd_4xz_hlb)
- [How can apps and integrations help my B2E business?](#topic_qbs_xxz_hlb)
- [How can Web Widget (Classic) help my B2E business?](#topic_wv2_hyz_hlb)
- [How can support addresses help my B2E business?](#topic_ggy_qyz_hlb)

## How can views help my B2E business?

Views are a way to organize your tickets by grouping them into lists based on certain criteria. Using views can help you determine which tickets need attention from you or your team, allowing you to plan accordingly.

Your IT support department might receive internal support requests from offices all over the world. It can be challenging to isolate only tickets from the London office. Using a [custom field](https://support.zendesk.com/hc/en-us/articles/4408883152794) and a [view](https://support.zendesk.com/hc/en-us/articles/4408888828570) can help you show only requests from a single office.

### Example

Let’s take a look at an example.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Views_b2e_1.png)

In this example, a view is configured to display only tickets that are not solved and where the custom office location field is set as London. Here’s an example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Views_b2e_2.png)

You can configure the information that the view displays by choosing the columns you want. Additionally, you can configure which of your agents can see the view in their Support console.

### Related articles

- [Creating views to manage ticket workflow](https://support.zendesk.com/hc/en-us/articles/4408888828570)

## How can organizations and groups help my B2E business?

Organizations are collections of your users (both end users and agents). Groups collect agents together based on criteria those agents have in common.

As a B2E business, you will probably use organizations and groups to organize the people in your Zendesk Support account.

Organizations and groups are often used to:

- Escalate tickets based on complexity
- Support service-level agreements
- Provide support by expertise
- Support customers by location and language

You may also want to use organizations to tightly manage your workflow and create security boundaries by funneling tickets directly to agents who have restricted access.

### Example

Let’s say you’re part of MegaCorp's IT department.

You may want to create organizations for each of the departments and divisions in your company. Or, maybe you want to base your organizations on geographic areas, so requests can be routed to local IT analysts and fixed faster. You can add “conditions”, based on MegaCorp's organizations, to triggers, automations, macros, and views to make it easier to work with your tickets.

Each of these organizations is a department at your company:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_people_orgs.png)

You may want to create groups based on common types of IT requests such as computers and equipment, software, urgent care, meeting rooms, or internet and security. You can add “actions” based on groups to triggers, automations, and macros, but not views.

Each of these groups is for types of requests you frequently get:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_people_groups.png)

### Related articles

- [About organizations and groups](https://support.zendesk.com/hc/en-us/articles/4408886146842)
- [About triggers and how they work](https://support.zendesk.com/hc/en-us/articles/4408822236058)
- [About automations and how they work](https://support.zendesk.com/hc/en-us/articles/4408832701850)
- [Using macros to update tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602)
- [Creating views to manage ticket workflow](https://support.zendesk.com/hc/en-us/articles/4408888828570)

## How can ticket fields help my B2E business?

Ticket fields include data that agents need in order to solve a problem. In order to use ticket fields effectively, it’s important to learn about the different types of ticket fields—there are system fields and custom ticket fields. Also, make sure you understand what kinds of permissions you can set on a ticket field, the relationship between ticket fields and ticket forms, and where ticket fields will appear for your agents and end users.

Ticket fields and ticket forms are highly customizable. It’s worth spending some time to figure out how to use them in a way that works best for you. This can reduce resolution times and improve customer satisfaction.

As a B2E business, when you get a request, you want to know certain information right away. You don’t want to have to go back to the customer and ask for more information. That takes time and can slow down resolution.

### Example

Let’s say you're part of MegaCorp's IT department.

You have a custom ticket field called “Request type.” It’s a drop-down list that includes common types of IT requests such as computers and equipment, software, urgent care, meeting rooms, or internet and security. This custom field is part of your default ticket form.

Here’s what your colleagues see when they go to submit an IT request:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_fields_ww_request.png)

This field is a drop-down list that includes common types of IT requests such as computers and equipment, software, urgent care, meeting rooms, or internet and security. It’s a custom field that is part of your default ticket form.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_fields_ww_dropdown.png)

You have triggers that automatically route tickets to the appropriate group of agents. When one of your colleagues submits a support request about their computer, the ticket is immediately assigned to the Computers & Equipment group, so it can be processed quickly.

### Related articles

- [About ticket fields](https://support.zendesk.com/hc/en-us/articles/4408886739098)
- [Adding custom fields to your tickets and support request form](https://support.zendesk.com/hc/en-us/articles/4408883152794)

## How can business rules help my B2E business?

You can create triggers and automations to intelligently process tickets, reduce redundant work, and save agents' time. Triggers are **event-based** business rules you define that run immediately after tickets are created or updated.
Automations are **time-based** business rules that perform an action in your account based on time elapsed.

Common uses of triggers and automations include:

- Routing new requests to the right team
- Sending notifications to employees or other IT support agents
- Escalating tickets in need of a response

By automating stages throughout the ticket lifecycle, you can decrease ticket handling times and reduce the number of reassignments from one IT support agent to the next. This ultimately helps you deliver a better experience for your employees.

As a B2E business, business rules can help your department to keep employees informed about the status of their requests, expedite employee repairs so they can get back to work quickly, and collect employee feedback.

### Triggers example

MegaCorp is a large multi-national organization, and each office has their own team of support analysts. For example, Jan is a support analyst for the London office. This trigger automatically routes equipment failure requests from employees in the London organization to the group of support analysts that serve the London office.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_trigger_condition.png)

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_trigger_action.png)

### Automation example

To help support MegaCorp's support analysts, automations can be used to send reminders when critical service requests are pending. For example, this automation sends an email reminder to the support analyst (ticket assignee) 24 hours before a software update is due. The reminder includes the ticket number and the full name of the employee who requested the update.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_automation.png)

Here’s an example of the email Jan would receive:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_automation_email.png)

### Related articles

- [About triggers and how they work](https://support.zendesk.com/hc/en-us/articles/4408822236058)
- [About automations and how they work](https://support.zendesk.com/hc/en-us/articles/4408832701850)
- [Routing and automation options for incoming tickets](https://support.zendesk.com/hc/en-us/articles/4408831658650)

## How can macros help my B2E business?

Macros are a pre-defined set of actions that agents apply to a ticket with one click. You can create macros to address support requests that can be answered with a single, standard response, and embed macros within tickets to help agents quickly provide consistent responses. This saves your support agents the time and effort of crafting a separate response to each employee with the same issue.

**Macros can:**

- Add comment text
- Update ticket fields (drop-down and checkboxes)
- Add or remove ticket tags
- Add CCs
- Change the assignee
- Set the ticket subject (title)
- Add attachments to ticket comments

As a B2E business, you can use macros to direct employees to help center articles to answer common questions, ask employees to provide more information, or ask employees to be patient during high traffic volume.

### Example

After Jane, MegaCorp's IT support analyst, receives a ticket about a hardware problem, she recognizes that this issue isn’t really with the hardware, and it can be fixed with a software patch. Jane opens the ticket and applies the following macro to change the ticket form from Equipment Problem to Software Update. The macro also changes the ticket subject to Patch request, so she doesn’t have incorrect information in the ticket title.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_macro.png)

The new ticket form applied by the macro enables Jane to enter the software patch number needed to fix the issue along with the date and time she has scheduled to make the change.

### Related articles

- [Creating macros](https://support.zendesk.com/hc/en-us/articles/4408844187034)
- [Using macros to update tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602)
- [Macros resources](https://support.zendesk.com/hc/en-us/articles/4408824631578)

## How can a help center help my B2E business?

A [help center](https://support.zendesk.com/hc/en-us/articles/4408846795674) provides a smart knowledge base for better self-service. You can set up your knowledge base to contain information (articles) covering frequently-asked questions, policies, product details, and more, to help users find the information they need, without having to raise a support ticket.

As a B2E customer, you can create FAQs or What’s New topics, for example, that contain articles about troubleshooting or company policies, or any type of information that you want to present to help answer everyday questions.

For example, you could show topics by department or by most asked questions:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_hc_customer_site.png)

You’ll need to [enable your help center in setup mode](https://support.zendesk.com/hc/en-us/articles/4408846795674#topic_ndf_fpf_mk), and then create and add content before you [activate it](https://support.zendesk.com/hc/en-us/articles/4408846795674#topic_ckn_wc4_qy).

You can start small with just a few articles that answer the most commonly-asked questions. For example, you could write an article explaining common problems and how to resolve them, or configuration guidance.

You need to be a Knowledge admin or an agent with [management permissions](https://support.zendesk.com/hc/en-us/articles/4408827952538) to create an article. See [Creating and editing an article](https://support.zendesk.com/hc/en-us/articles/4408839258778) for more information.

### Related articles

- [Getting started with your help center](https://support.zendesk.com/hc/en-us/articles/4408846795674)
- [Creating and editing an article](https://support.zendesk.com/hc/en-us/articles/4408839258778)

## How can apps and integrations help my B2E business?

There are a variety of apps in the [Zendesk Marketplace](https://www.zendesk.com/apps/) and integrations to improve your productivity with agents to resolve tickets and improve communication with employees. Here is an app and integration that you can try to support your B2E business.

### Slack integration

The Slack for Zendesk Support integration allows you to interact with Support tickets in your Slack channels.

For example, the Slack app is installed by an admin in the MegaCorp Slack workspace. After installing the app, under **Recent Apps** >
**Zendesk**, the #ask-ithelp Slack channel is added to connect with Support, then configured to receive notifications.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_slack1.png)

When Dan in HR has an issue with his computer, he can go to the #ask-ithelp Slack channel to discuss his issue. He can also create a ticket in the channel by entering the Slack command /zendesk create\_ticket or create a Slack action The channel posts a notification when the status of a ticket is changed.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_slack2.png)

To learn more about the integration, see the [Slack integration](https://support.zendesk.com/hc/en-us/sections/360005906734).

### Attachment Manager app

The [Attachment Manager app](https://www.zendesk.com/apps/support/attachment-manager/?source=app_directory) helps manage attachments for tickets in your ticket sidebar. It provides several features including an attachment library, restricting attachment types for security or compliance purposes, and the ability to redact attachments.

In this example, an IT support agent adds a link to the in-house documentation in the attachment library. It can be sent to Dan’s support ticket and tickets with the same issue.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_attachment_manager.png)

To learn more about the Attachment Manager app, see [Installing and using the Attachment Manager app](https://support.zendesk.com/hc/en-us/articles/4408823467674).

## How can Web Widget (Classic) help my B2E business?

[Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408833907354) is a separate web application that is embedded in a web page. It gives customers access to your help center and the agents in your Zendesk support channels.

By embedding Web Widget (Classic) in your website, you can encourage employees to self-serve by searching for help center articles. It can also make it easier to get help from an agent by displaying ticket forms for support requests and start a chat.

Web Widget (Classic) is configured in your [Support Admin](https://support.zendesk.com/hc/en-us/articles/4408838063258). Zendesk also provides [Web Widget APIs](https://developer.zendesk.com/embeddables/docs/widget/introduction) to extensively configure and customize the widget to suit your requirements.

### Example

In this example, the Web Widget (Classic) is configured by a MegaCorp admin in Support under **Admin** > **Channels** > **Web Widget (Classic)**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2c_webwidget.png)

Help center search and Contextual Help is enabled to create ticket deflection. So Dan, who has a problem with his equipment, must first search and find articles to help address his issue.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_webwidget_ex_1.png)

Ticket forms is enabled so Dan can submit a ticket if he is unsuccessful in finding a help center article that addresses his issue.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/b2e_webwidget_ex_2.png)

### Related articles

- [Providing omnichannel support using Web Widget for the Suite](https://support.zendesk.com/hc/en-us/articles/4408844047898)
- [Web Widget resources](https://support.zendesk.com/hc/en-us/articles/4408833907354)
- [Using Web Widget to embed customer service in your website](https://support.zendesk.com/hc/en-us/articles/4408836216218)

## How can support addresses help my B2E business?

Support addresses are email addresses that allow your users to submit support tickets. Support addresses can be variations of your Zendesk email address, or your external email addresses. Any email address you want to use to receive support request as tickets (whether it's a Zendesk address or an external address)
must be added to your Zendesk as a support address.

By creating multiple support addresses, a B2E company can route support tickets directly to agents, or groups, who are trained to handle the issue at hand.
Support addresses can be based on task or department (IT, Payroll, etc.), location (such as city, time zone, or region), or language -- really, anything that works for your business.

You can create as many support email addresses as you need. They can be used throughout your Zendesk to help you organize and direct your support requests to your agents:

- [Create views](https://support.zendesk.com/hc/en-us/articles/4408888828570) that organize tickets based on which address received them.
- [Customize email notifications](https://support.zendesk.com/hc/en-us/articles/4408886168090) for each email address, to automatically reply to incoming requests.
- [Build triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466), using email addresses as a condition. For example, you can add tags or priority levels to tickets, or assign them to specific groups or agents, based on which email address received them.
- [Create reports](https://support.zendesk.com/hc/en-us/articles/4408821589530) to monitor how many tickets are generated through email addresses, and write custom formulas to break down how each address is performing.

### Example

By creating multiple support addresses, a B2E account can route internal support tickets directly to the IT team located in Dan’s London office.

In the scenario above, here’s how having an issue-specific support address might work:

Dan goes to MegaCorp’s internal website and clicks the IT Help Page link. On the web page, he sees a list of MegaCorp’s office locations, each with a different email address associated with it:

San Francisco HQ: Contact it-HQ@megacorp.com

London office: Contact it-LDN@megacorp.co.uk

Copenhagen office: Contact it-CPH@megacorp.dk

Singapore office: Contact it-SGP@megacorp.com.sg

Dan clicks it-LDN@megacorp.co.uk, fills out the support form, and clicks **submit**. All tickets sent through that support address are routed to a view monitored by the London-based IT department. Jane, who is on duty at the time, sees his request come in and contacts him to find out what’s wrong.
They figure out a solution, and his computer is up and running again within the hour.

### Related articles

- [Adding support addresses for users to submit tickets](https://support.zendesk.com/hc/en-us/articles/4408842868506)