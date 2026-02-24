# About ticket fields

Source: https://support.zendesk.com/hc/en-us/articles/4408886739098-About-ticket-fields

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Ticket fields help you organize and manage support requests by collecting essential information from users. Standard fields capture basic details, while custom fields let you gather specific data like product type. These fields are part of ticket forms, visible to both users and agents. You can manage them on the Fields admin page, enhancing your support workflow with placeholders, APIs, triggers, and automations.

Typically, when end users submit support requests, they provide the subject and description of their question or support issue in *standard ticket fields*. They may also be prompted to provide additional data such as a product type or model number using *custom ticket fields*.

Collectively, a predefined set of ticket fields are a *ticket form*. Ticket fields on a ticket form are visible to end users in the contact form, in the help center or Web Widget (Classic) for example, and to agents in a ticket, as shown here.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_fields4.png)

Tickets contain other data that you can access using [placeholders](https://support.zendesk.com/hc/en-us/articles/4408886858138#topic_giz_opl_rc), [Zendesk APIs](https://developer.zendesk.com/api-reference/), [triggers](https://support.zendesk.com/hc/en-us/articles/4408843730458), and [automations](https://support.zendesk.com/hc/en-us/articles/4408882001690). Ticket fields don't need to be on a ticket form to be used in these places.

There are two types of ticket fields:

- **Standard ticket fields** are the predefined fields that agents see in a ticket.
 Additional standard fields are added to the ticket page when you activate additional Zendesk Support features, such as ticket sharing. You can deactivate and reactivate some (but not all) of the standard fields.

 See the [complete list of standard ticket fields](#topic_drw_ft1_3nb).
- **Custom ticket fields** can be created in addition to standard ticket fields to gather additional information from the person who is requesting support. For example, you may add a custom field prompting them to select a product name or model number.

 See the [complete list of custom ticket field types](https://support.zendesk.com/hc/en-us/articles/4408838961562).

 Also, see the following articles:

 - [Optimizing your ticket form](https://support.zendesk.com/hc/en-us/articles/4408888481178) to understand ticket fields and do some planning to build an optimal ticket form.
 - [Adding custom fields to your tickets and support request form](https://support.zendesk.com/hc/en-us/articles/4408883152794) to create the custom ticket fields you need.

You can view and manage all of your ticket fields on the Fields admin page. See [Viewing your ticket fields](https://support.zendesk.com/hc/en-us/articles/4408832419738).

## Standard ticket fields

The following fields are considered standard ticket fields and are part of tickets by default for all Zendesk Suite and Support accounts. Some standard fields can't be edited.
See [About system ticket rules](https://support.zendesk.com/hc/en-us/articles/4408894213018).

Depending on your plan type, you may have access to additional standard ticket fields:

- [Additional ticket fields for employee services](#topic_djc_ky3_q2c)
- [Additional ticket fields for the Copilot add-on](#topic_z1x_mtp_xgc)

| Standard field | Description |
| --- | --- |
| Requester | All tickets require a requester. The requester is the person who made the support request. If a ticket is created by an agent and the requester field is left empty, then the agent will be the requester of the ticket. If needed, the ticket requester can be changed to someone else. See [Updating the ticket requester](https://support.zendesk.com/hc/en-us/articles/4408886900506). You can also create a ticket on someone else's behalf. See [Creating a ticket on behalf of the requester](https://support.zendesk.com/hc/en-us/articles/4408882462618). |
| Follower | Followers can be agents, light agents, or admins, but not end users. Similar to a persistent BCC, followers receive notifications when ticket updates occur, and they can view and create internal notes. Followers are invisible to end users, but CCs are not. See [When to use CCs and followers](https://support.zendesk.com/hc/en-us/articles/4408829504154#topic_kzy_zwq_4fb). |
| Assignee | The assignee can be either a group or a specific agent. See [Manually assigning a ticket to yourself, another agent, or a group](https://support.zendesk.com/hc/en-us/articles/4408887127450). |
| CCs | If you have been configured to allow it, other people can be copied on tickets. Both the requester and agents can add CCs to a ticket. The requester does it by adding CC email addresses if they requested support via your support email address. Agents can add CCs using the CC field when updating the ticket. See [Using CCs, followers, and @mentions](https://support.zendesk.com/hc/en-us/articles/4408822451482). |
| Share | The Share field is only displayed if you have enabled ticket sharing, which means that tickets can be shared with other Zendesk Support accounts. See [Sharing tickets](https://support.zendesk.com/hc/en-us/articles/4408886265370). |
| Subject | The Subject field is required and can be up to 255 characters. It's typically included in the support request submitted by the requester. For example, when someone submits a support request through email, the subject line of the email is used as the ticket's subject. If the ticket title does not appear in the ticket subject, your Subject field might not be visible to end users. To correct this, see this [Support Tech Note](https://support.zendesk.com/hc/en-us/articles/4408827535770). |
| Description | The Description field is required. This is the text of the support request. When an end user submits a support request via email, the body of the email request is used as the description. The description becomes the first comment in the ticket. |
| Status | There are six standard ticket status values. A ticket's status can be set and updated either manually by an agent or automatically via your business rules. If you've [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), your account may include additional ticket statuses. The standard ticket statuses listed below are the default ticket statuses of your ticket status categories. See [Managing ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575941402).   - **New** means that the request was received but that it has not been opened   and has not been assigned to an agent. The New status can indicate that the   support team is evaluating it to determine who should be assigned to resolve it.   After changing the status from New to another status, you can't change the   status back to New. - **Open** means that the request has been assigned to an agent who is   working to resolve it. Once a ticket status changes to Open, it can never return   to New. If your tickets are being created in the Open status instead of New, see   [Why are new tickets being created in Open   status?](https://support.zendesk.com/hc/en-us/articles/4408827594266) - **Pending** means that the assigned agent has a follow-up question for the   requester. The agent may need more information about the support issue. Requests   that are set to Pending typically remain that way until the requester responds   and provides the information the agent needs to continue resolving the request. - **On-hold** means that the support request is awaiting a resolution from a   third party, someone who is not a member of your support staff and does not have   an agent account. This status is optional and must be added. See [Adding the On-hold ticket status to Zendesk   Support](https://support.zendesk.com/hc/en-us/articles/4408889282458). - **Solved** means that the agent has resolved the support issue. Solved   tickets are closed, typically, a number of days after they have been set to   Solved (the exact number of days depends on how an Administrator set this up).   Until a ticket is closed, the requester can reopen the ticket. For example, the   requester may not agree with the agent that the support issue is resolved and   reply back to the ticket solved email notification. - **Closed** means that the ticket is complete and can't be reopened.   Requesters however can create follow-up requests for closed requests. A ticket's   status cannot be changed to Closed manually. Closing a ticket is handled   automatically via your business rules. |
| Type | There are four values for type. Setting the type helps you to categorize your tickets, which you can then use in your workflow. For example, you can create views of tickets by their type. While the field can be blank initially (and through any number of updates), once you change the field to a specified type, you can't change it to blank again. - **Question** is used to indicate that the requester's issue is a question   rather than a problem that needs to be solved. - **Incident** is used to indicate that the requester is experiencing a   single occurrence of a larger problem that is affecting multiple users. - **Problem** is used to indicate that the requester is having an issue with   your product or service that needs to be resolved and that is affecting multiple   users. For example, if the wireless network in an office stops working, the   problem will probably generate several support requests. Instead of handling   each ticket separately, create one ticket describing the problem and set the   type to Problem. - Link incident tickets to problem tickets. When you solve the problem ticket,   all linked incident tickets are solved too. See [Working with problem and incident   tickets](https://support.zendesk.com/hc/en-us/articles/4408835103898). - **Task** is used when you want to assign the ticket as a task to a specific   agent. After you select **Task**, you have the option to set a **Task Due   Date**. The due date is defined as 12pm in the user's browser's local   timezone on the date specified.   Note: If you [deactivate](https://support.zendesk.com/hc/en-us/articles/4408828883738#topic_l24_3gw_jz) the Type field, all your tickets default to Incident, which is one of the most-common ticket types. |
| Priority | There are four values for priority: **Low**, **Normal**, **High**, and **Urgent**. By default, all of these four values are available, but you can allow only the Normal and High values to appear. To do so, [edit the priority field](https://support.zendesk.com/hc/en-us/articles/4408828883738#topic_vgj_3gw_jz), then change the setting under **Field values**. Priority is not a required field, so you do not always need to select a value. How you weigh the priority of your tickets is up to you. If you [deactivate](https://support.zendesk.com/hc/en-us/articles/4408828883738#topic_l24_3gw_jz) the Priority field, Zendesk SLA targets will not apply. See [Setting up SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866#topic_tsz_1yv_rr). |
| Tags | Tags are used throughout to add additional information to tickets, which can then be used in your ticket workflow. Tags can be added to tickets in the following ways: - You can add them manually. - Tags can be added (and removed) automatically based on your business rules. - Tags can be added to users and organizations and these tags are   automatically added to tickets. Tags are enabled by default but can be disabled. See [Enabling and disabling ticket tags](https://support.zendesk.com/hc/en-us/articles/4408829424794). |
| Approval status | Visible only after approval requests have been [turned on](https://support.zendesk.com/hc/en-us/articles/9475816348442). This field is automatically updated to reflect the status an approval request associated with the ticket. There are four values: **Pending**, **Approved**, **Denied**, and **Withdrawn**. Note: For accounts with more than one ticket form, this field must be manually [added to ticket forms](https://support.zendesk.com/hc/en-us/articles/4408883152794). |

### Additional ticket fields for employee services

Employee Service Suite plans include several additional ticket forms that are specialized for common HR and IT inquiries. To support those specialized ticket forms, the following ticket fields are predefined for Employee Service Suite plans.

All of these fields are labeled as *[SAMPLE]* on the Ticket fields page in Admin Center for clarity. However, *[SAMPLE]* is excluded from the titles shown to customers.

These fields are active by default, but can be [deactivated or deleted](https://support.zendesk.com/hc/en-us/articles/4408828883738) if you don't need them. See [Using the sample data for employee services](https://support.zendesk.com/hc/en-us/articles/9012803758362).

| Field | Industry | Description | Ticket forms |
| --- | --- | --- | --- |
| [SAMPLE] New hire name | HR | A text field in the New hire onboarding ticket form that contains a new employee's name. | New hire onboarding |
| [SAMPLE] Expected start date | HR | A date field in the New hire onboarding ticket form that indicates a new employee's expected start date. | New hire onboarding |
| [SAMPLE] New hire office location | HR | A text field in the New hire onboarding ticket form that contains the new employee's office location. | New hire onboarding |
| [SAMPLE] Laptop requested | HR | A text field in the New hire onboarding ticket form that indicates whether a laptop has been requested for the new employee. | New hire onboarding |
| [SAMPLE] Software name | IT | A text field indicating the name of the software for which access is being requested. | Software access |
| [SAMPLE] Leave type | HR | A text field indicating the type of leave being requested or inquired about. For example, FMLA or parental leave. | Leave request, Parental leave |
| [SAMPLE] Expected leave duration | HR | A text field indicating how long the requested leave is expected to be. | Leave request |
| [SAMPLE] Expected leave start date | HR | A date field indicating the start date of the requested leave. | Leave request |
| [SAMPLE] Employee ID | HR | A text field indicating the employee's ID. | Payroll questions |
| [SAMPLE] Department | HR, IT | A text field indicating the employee's department within the organization. In employee service accounts, [brands](https://support.zendesk.com/hc/en-us/articles/7584022494874) are expected to be used to differentiate groups of agents within the account (HR, IT, Legal, etc.), while this custom field could be used to designate the employee's location within the organization, such as Engineering. | New hire onboarding, Payroll question, New laptop request, Software access |
| [SAMPLE] Approval status | HR, IT | A text field, editable by agents and admins only, indicating whether a request made in the ticket is approved. | New hire onboarding, Payroll question, New laptop request, Software access |

### Additional ticket fields for the Copilot add-on

If you have the [Copilot add-on](https://support.zendesk.com/hc/en-us/articles/5524125586330), then your account includes additional standard ticket fields. These fields store AI-generated values and associated information.

The Copilot add-on also includes custom ticket fields that are populated with prebuilt predictions by the Zendesk machine learning model. See [Understanding intelligent triage fields](https://support.zendesk.com/hc/en-us/articles/4550640560538#topic_ybp_w54_pgc) to learn more.

| Standard field | Description |
| --- | --- |
| Summary | The AI-generated summary of a ticket. AI-generated ticket summaries are a concise recap of all the public comments and internal notes that have been added to a ticket so far. To learn more, see [About ticket summarization](https://support.zendesk.com/hc/en-us/articles/8037565521946#topic_iz1_hp1_xcc). The Summary field is populated only when [an agent manually refreshes the ticket summary](https://support.zendesk.com/hc/en-us/articles/8037649972634#topic_uxh_1m1_xcc). The field stores the latest summary generated by the agent in the language in which it was created. |
| Summary agent ID | The ID of the agent who last generated a ticket's summary. |
| Summary date and time | The time stamp of when a ticket's summary was last generated. |
| Summary locale | The locale of the agent who last generated a ticket's summary. |