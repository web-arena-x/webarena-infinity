# Placeholder reference for business rules

Source: https://support.zendesk.com/hc/en-us/articles/4408886858138-Placeholder-reference-for-business-rules

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Placeholders are containers for dynamically generated ticket, user, and custom data. The format is a data reference contained within double curly brackets. Since you can also access ticket, user, and custom data when defining programming logic, it may be helpful to think beyond placeholders and think instead of data objects and their properties that can be used for either purpose.

There are two primary data objects in Zendesk Support: Ticket and User. Each has its own set of properties; the User object, for example, contains user properties such as name and email.
In addition to these two data objects, there are associated data objects. For tickets, there are the Comment and Satisfaction Rating objects. For users, there are the Organization and Agent objects. There are also custom objects, which are defined by users and can be associated with tickets, users, and other Zendesk objects.

Although placeholders can be in HTML format, when a placeholder is sent to a URL target or webhook, unformatted text is used to render the placeholder, not HTML. Also, placeholders won't work within code blocks.

Note: If you're supporting multiple languages, be aware that placeholder values will match the language of the requester on the ticket, in most instances. This automatic translation cannot be disabled.

Support includes *inborn system rules* that suppress placeholders in ticket triggers in certain situations. Inborn system rules are rules that you cannot change, modify, or override, which dictate the default behavior of Support. These rules may sometimes make it seem like placeholders in ticket triggers failed to work, but this isn’t a mistake. These rules protect you because they prevent spammers from using your account to distribute spam messages. For more information, see [Understanding placeholder suppression rules](https://support.zendesk.com/hc/en-us/articles/4408833443226).

The HTML template for email notifications has its own set of placeholders. See [Placeholder reference for the HTML email template](https://support.zendesk.com/hc/en-us/articles/4408886168090#topic_mqn_hpd_x3).

This article categorizes the placeholders by the data they display. When you specify placeholders, remember they are case sensitive.

- [User data](#topic_qdz_opl_rc)
- [Organization data](#topic_qgz_opl_rc)
- [Agent data](#topic_hmx_zzw_4v)
- [Ticket data](#topic_giz_opl_rc)
- [Comment data](#topic_jkz_opl_rc)
- [Satisfaction rating data](#topic_nnz_opl_rc)
- [Custom object data](#topic_zj1_1w1_qbc)

Related articles:

- [Understanding placeholder suppression rules](https://support.zendesk.com/hc/en-us/articles/4408833443226)
- [Using placeholders](using-placeholders.md)
- [Configuring email autoreplies to deflect requests](https://support.zendesk.com/hc/en-us/articles/4408825385242)

## User data

In the context of updating a ticket, there are a number of different types of users. These include the following:

- ticket.requester, who is the person who requested the ticket
- ticket.assignee, who is the agent assigned to the ticket
- ticket.submitter, who is either the user who submitted the request or the agent that opened the ticket on behalf of the requester
- current\_user, who is the user currently updating the ticket (an end user, agent, or Zendesk as the system user)

This means that most of the user data listed in the following table can be returned for each type of user (for example, {{ticket.submitter.name}}, {{current\_user.name}}, and so on).

Table 1. User object data

| Properties/placeholders | Description |
| --- | --- |
| {{*user*.name}} Important: Remember to replace *user* with one of the user types shown above (for example, ticket.requester). | The user's full name. |
| {{*user*.first\_name}} | The user's first name. |
| {{*user*.last\_name}} | The user's last name. |
| {{*user*.email}} | The user's email address. |
| {{*user*.language}} | The user's language preference. |
| {{*user*.phone}} | The user's telephone number. |
| {{*user*.external\_id}} | The user's external ID (if one exists). Optional for accounts that have activated enterprise single sign-on using JWT or SAML. |
| {{*user*.details}} | The user's details. |
| {{*user*.notes}} | The user's notes. |
| {{*user*.time\_zone}} | The user's time zone. |
| {{*user*.role}} | The user's role (Admin, Agent, or End user). |
| {{*user*.extended\_role}} | When using Support Enterprise agent roles, this returns the name of the agent's Enterprise role. These are the predefined roles: - Advisor - Light Agent - Staff - Team Leader - Legacy Agent - Administrator If you've created custom agent roles, those role names are returned. If you're not an Enterprise account, using this placeholder returns 'Agent' for all agent users and 'End user' for all end users. For more information about custom agent roles, see [Creating custom agent roles and assigning agents](https://support.zendesk.com/hc/en-us/articles/4408882153882). |
| {{*user*.id}} | The user's ID. |
| {{*user*.locale}} | The user's locale (for example: en-US). |
| {{*user*.signature}} | The agent's signature. Only agents have signatures. |
| {{*user*.organization...}} | See [Organization data](#topic_qgz_opl_rc) below. |
| {{*user*.tags}} | Tags. See [Adding tags to users and organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658). |
| {{*user*.custom\_fields.*<field\_key>*}} | Property/placeholder format for the value of a custom user fields (except drop-down fields). For example, {{ticket.requester.custom\_fields.my\_custom\_field}}. See [Adding custom fields to users](https://support.zendesk.com/hc/en-us/articles/4408822051866). |
| {{*user*.custom\_fields.<*field\_key*>.id}} | The ID of the target record in a lookup relationship field. |
| {{*user*.custom\_fields.*<field\_key>*.title}} | Property/placeholder format for the value of a custom user drop-down field. For example, {{ticket.requester.custom\_fields.manager\_for\_approval.title}}. See [Adding custom fields to users](https://support.zendesk.com/hc/en-us/articles/4408822051866). |

### About user name placeholders

The behavior of the first name and last name placeholders depends on the formatting of the name on the profile. For example, if you use the name Dutch van der Linde, the placeholder *user*.last\_name will show 'Linde'. If you use the name van der Linde, Dutch on the profile, then the placeholder *user*.last\_name will show 'van der Linde'.

Additionally, in Japan, the first name placeholder refers to the user's last name and the last name placeholder refers to the user's first name.

## Organization data

Each type of user can be added to an organization. An organization contains the following data properties.

Table 2. Organization data object

| Properties/placeholders | Description |
| --- | --- |
| {{*user*.organization.id}} Important: Remember to replace *user* with one of the user types shown below. | The ID of the organization that the user is assigned to. |
| {{*user*.organization.name}} | The name of the organization that the user is assigned to. |
| {{*user*.organization.is\_shared}} | True or False. Indicates if the organization is a shared organization. |
| {{*user*.organization.is\_shared\_comments}} | True or False. Indicates if the organization allows users to add comments to other user's tickets. |
| {{*user*.organization.details}} | Details about the organization. |
| {{*user*.organization.notes}} | Notes about the organization. |
| {{*user*.organization.tags}} | Tags. See [Adding tags to users and organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658). |

Since all users can be added to an organization, you can access the organization data for each using Liquid markup. For example, you can return data for each of the these types of users (shown here as placeholders):

- {{ticket.organization.name}}, which is the ticket requester's organization
- {{ticket.requester.organization.name}}, which the same as {{ticket.organization.name}} (the requester)
- {{current\_user.organization.name}}, who is the user currently updating the ticket (an end user or agent)
- {{ticket.assignee.organization.name}}, who is the agent assigned to the ticket
- {{ticket.submitter.organization.name}}, who is either the user who submitted the request or the agent that opened the ticket on behalf of the requester

## Agent data

You can use the following placeholders in agent signatures only. For information on agent signatures, see [Adding an agent signature to ticket email notifications](https://support.zendesk.com/hc/en-us/articles/4408822471322).

Table 3. Agent data object

| Properties/placeholders | Description |
| --- | --- |
| {{agent.name}} | The agent's full name (or alias, if present). |
| {{agent.first\_name}} | The agent's first name. |
| {{agent.last\_name}} | The agent's last name. |
| {{agent.role}} | The agent's role. |
| {{agent.signature}} | The agent's signature. |
| {{agent.email}} | The agent's email address. |
| {{agent.phone}} | The agent's phone number. |
| {{agent.organization}} | The agent's organization. |
| {{agent.language}} | The agent's language. |
| {{agent.time\_zone}} | The agent's time zone. |

## Ticket data

Zendesk Support tickets contain the following data properties.

Table 4. Ticket object data

| Properties/placeholders | Description |
| --- | --- |
| {{ticket.account}} | The Zendesk account name. |
| {{ticket.assignee.name}} | Ticket assignee full name or alias (if any). See [User data](#topic_qdz_opl_rc) above. |
| {{ticket.brand.name}} | The ticket's assigned brand name. |
| {{ticket.cc\_names}} | Returns the names CCs on the ticket. Note: If you are using [the new CCs and followers](https://support.zendesk.com/hc/en-us/articles/4408843795482) experience and you are adding or updating your placeholders, we recommend using `ticket.email_cc_names` instead of `tickets.cc_names`. They do the same thing. If you want to return the email addresses of the people CC'd on the message, you can use this Liquid code: ``` {% for cc in ticket.ccs %}    {{cc.name}} ({{cc.email}}) {% endfor %} ``` |
| {{ticket.email\_cc\_names}} | With the [new CCs and followers experience](https://support.zendesk.com/hc/en-us/articles/4408843795482), returns the names of CCs on the ticket. With the old CCs experience, returns empty. Note: If you are using the [new CCs and follower experience](https://support.zendesk.com/hc/en-us/articles/4408843795482) and you are adding or updating your placeholders, we recommend using `ticket.email_cc_names` instead of `tickets.cc_names`. They do the same thing. |
| {{ticket.follower\_names}} | With the [new CCs and followers experience](https://support.zendesk.com/hc/en-us/articles/4408843795482), returns the names of followers. With the old CCs experience, returns empty. |
| {{ticket.follower\_reply\_type\_message}} | With the [new CCs and followers experience](https://support.zendesk.com/hc/en-us/articles/4408843795482), indicates what type of comment (public or private) triggered the notification. Causes the phrase "Reply to this email to add a comment to the request" or "Reply to this email to add an internal note to the request" to appear in the email notification (see [Customizing default email notifications for CCs and followers](https://support.zendesk.com/hc/en-us/articles/4408843866394)). With the old CCs experience, returns empty. |
| {{ticket.created\_at}} | Date the ticket was created (for example, May 18, 2014). Note: The year is not included if the ticket was created in the current year. |
| {{ticket.created\_at\_with\_timestamp}} | Time the ticket was created expressed as an iso8601 format date/time. Example: 2013-12-12T05:35Z, which translates to December 12th, 2013 at 05:35am UTC. |
| {{ticket.created\_at\_with\_time}} | Date and time the ticket was created. For example, February 10, 14:29. |
| {{ticket.current\_holiday\_name}} | If the placeholder is used outside of a holiday, it is null. If it is used within a holiday, the holiday's name is displayed. If you've set up multiple schedules, this placeholder respects the list of holidays set in the schedule applied to the ticket. |
| {{ticket.description}} | The ticket description. This includes the requester's name, the comment date, and the ticket description (the first comment). Note: If the subject field is empty or not visible to the requester, then this first comment will be used and sent to the requester. This is true for private tickets as well. |
| {{ticket.due\_date}} | The ticket due date (relevant for tickets of type Task). The format is: May-18. |
| {{ticket.due\_date\_with\_timestamp}} | The ticket due date (relevant for tickets of type Task) expressed as an iso8601 format date/time. Example: 2013-12-12T05:35+0100 which translates to December 12th, 2013 at 06:35am UTC+1. |
| {{ticket.external\_id}} | The external ticket ID (if one exists). |
| {{ticket.encoded\_id}} | The encoded ID is used for threading incoming email replies into existing tickets. |
| {{ticket.group.name}} | The group assigned to the ticket. |
| {{ticket.id}} | The ticket ID. `#{{ticket.id}}` creates a clickable link. `{{ticket.id}}` renders the ticket number in plain text. |
| {{ticket.in\_business\_hours}} | True or False. True if the ticket update is during business hours. See [Setting your business hours](https://support.zendesk.com/hc/en-us/articles/4408842938522). |
| {{ticket.link}} | Full URL path to ticket. |
| {{ticket.organization.custom\_fields.*<field\_key>*}} | Property/placeholder format for [custom organization fields](https://support.zendesk.com/hc/en-us/articles/4408838961562). See [Adding custom fields to organizations](https://support.zendesk.com/hc/en-us/articles/4408842677786). |
| {{ticket.organization.custom\_fields.<*field\_key*>.id}} | The ID of the target record in a custom [lookup relationship field](https://support.zendesk.com/hc/en-us/articles/4591924111770). |
| {{ticket.organization.custom\_fields.*<field\_key>*.title}} | Property/placeholder format for the value of a [custom organization drop-down field](https://support.zendesk.com/hc/en-us/articles/4408838961562). See [Adding custom fields to organizations](https://support.zendesk.com/hc/en-us/articles/4408842677786) |
| {{ticket.organization.external\_id}} | External ID of the ticket requester's organization. |
| {{ticket.organization.id}} | The ID of the ticket requester's organization. |
| {{ticket.organization.name}} | See [Organization data](#topic_qgz_opl_rc) above. |
| {{ticket.priority}} | The ticket priority (Low, Normal, High, Urgent). |
| {{ticket.requester.first\_name}} | Ticket requester first name. If you have an [open Zendesk Support instance](https://support.zendesk.com/hc/en-us/articles/4408881989018#topic-1__ul_l2w_x13_4y), this placeholder can be a target for spam in first-reply triggers. See [Using Zendesk Support-specific features to combat spam](https://support.zendesk.com/hc/en-us/articles/4408832828186#h_667502120121539295305407). |
| {{ticket.requester.last\_name}} | Ticket requester last name. If you have an [open Zendesk Support instance](https://support.zendesk.com/hc/en-us/articles/4408881989018#topic-1__ul_l2w_x13_4y), this placeholder can be a target for spam in first-reply triggers. See [Using Zendesk Support-specific features to combat spam](https://support.zendesk.com/hc/en-us/articles/4408832828186#h_667502120121539295305407). |
| {{ticket.requester.name}} | Ticket requester full name. If you have an [open Zendesk Support instance](https://support.zendesk.com/hc/en-us/articles/4408881989018#topic-1__ul_l2w_x13_4y), this placeholder can be a target for spam in first-reply triggers. See [Using Zendesk Support-specific features to combat spam](https://support.zendesk.com/hc/en-us/articles/4408832828186#h_667502120121539295305407). |
| {{ticket.requester.email}} | Ticket requester email address. |
| {{ticket.requester.custom\_fields.*<field\_key>*}} | Property/placeholder format for custom user fields. For example, {{ticket.requester.custom\_fields.my\_custom\_field}}. See [Adding custom fields to users](https://support.zendesk.com/hc/en-us/articles/4408822051866). |
| {{ticket.requester.custom\_fields.<*field\_key*>.id}} | The ID of the target record in a lookup relationship field. |
| {{ticket.requester.custom\_fields.*<field\_key>*.title}} | Property/placeholder format for the value of a custom user drop-down field. For example, {{ticket.requester.custom\_fields.manager\_for\_approval.title}}. See [Adding custom fields to organizations](https://support.zendesk.com/hc/en-us/articles/4408842677786). |
| {{ticket.requester.details}} | The contents of the Details field on the requester’s user profile. |
| {{ticket.status}} | The standard ticket status (New, Open, Pending, On-hold, Solved, Closed). Note: If you've [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306), this placeholder displays the same value as `{{ticket.status_category}}`. |
| {{ticket.status\_category}} | If [custom ticket statuses are activated](https://support.zendesk.com/hc/en-us/articles/4412575841306), returns the status category the ticket's status belongs to (New, Open, Pending, On-hold, Solved, Closed). Learn more about [ticket status categories](https://support.zendesk.com/hc/en-us/articles/4412575841306#topic_hmv_5kl_dwb). |
| {{ticket.custom\_status}} | If [custom ticket statuses are activated](https://support.zendesk.com/hc/en-us/articles/4412575841306), returns the custom ticket status. |
| {{ticket.tags}} | All of the tags attached to the ticket. |
| {{ticket.ticket\_field\_*<field ID number>*}} | Property/placeholder format for custom fields. For example, {{ticket.ticket\_field\_123}}. See [Placeholders for custom fields](https://support.zendesk.com/hc/en-us/articles/4408887218330#topic_nfp_nja_vb). |
| {{ticket.ticket\_field\_<*field ID number*>.id}} | The ID of the target record in a lookup relationship field. |
| {{ticket.ticket\_field\_<*field ID number*>.name}} | The name of the target record in a lookup relationship field. |
| {{ticket.ticket\_field\_option\_title\_*<field ID number>*}} | Property/placeholder format for the value of a dropdown custom field. For example, {{ticket.ticket\_field\_option\_title\_456}}. See [Placeholders for custom fields](https://support.zendesk.com/hc/en-us/articles/4408887218330#topic_nfp_nja_vb). |
| {{ticket.ticket\_form}} | Form name for end users. |
| {{ticket.ticket\_type}} | Ticket type (Question, Incident, Problem, Task). If the ticket type is not specified, this placeholder returns "Ticket". |
| {{ticket.title}} | The ticket subject. End users may see different text in this field. For troubleshooting information about this placeholder, see [The ticket title placeholder displays first comment instead of the subject](https://support.zendesk.com/hc/en-us/articles/4408827535770) and [Why does the subject line in my email notifications say "Untitled ticket"](https://support.zendesk.com/hc/en-us/articles/4970929848090). If you have an [open Zendesk Support instance](https://support.zendesk.com/hc/en-us/articles/4408881989018#topic-1__ul_l2w_x13_4y), this placeholder can be a target for spam in first-reply triggers. See [Using Zendesk Support-specific features to combat spam](https://support.zendesk.com/hc/en-us/articles/4408832828186#h_667502120121539295305407). |
| {{ticket.updated\_at}} | Date the ticket was last updated (for example, May18). |
| {{ticket.updated\_at\_with\_time}} | Time and date the ticket was last updated. For example, February 10, 14:29. |
| {{ticket.updated\_at\_with\_timestamp}} | Time the ticket was last updated expressed as an iso8601 format date/time. Example: 2013-12-12T05:35Z, which translates to December 12th, 2013 at 05:35am UTC. |
| {{ticket.url}} | The full URL path to the ticket (excluding "http://"). |
| {{ticket.verbatim\_description}} | The plain text value of the ticket description (the first comment). If [Allow agents to attach files in emails](https://support.zendesk.com/hc/en-us/articles/4408832757146) is activated, attachments are included. Note: This placeholder cannot be used to send attachments in a webhook. |
| {{ticket.via}} | The source type of the ticket (Web form, Mail, etc.). |
| {{account.incoming\_phone\_number\_ID}} | Zendesk inbound phone number. For example,{{account.incoming\_phone\_number\_123}}. |

## Comment data

Because comments are added to tickets, they're accessed with the ticket data object. There are four types of comment placeholders:

- [**HTML comment placeholders**](#topic_jkz_opl_rc__table_zrv_bzk_wtb) are used for simplified email threading in email applications such as Gmail. For best results, they should not be used with other comment placeholders.
- [**Standard comment placeholders**](#topic_jkz_opl_rc__table_tlz_opl_rc) allow you to use [liquid hashes](https://support.zendesk.com/hc/en-us/articles/4408883291290) to choose what you want to display, and return a collection of comment and attachment data. For example, you can set up [templates](https://support.zendesk.com/hc/en-us/articles/4408886168090) to iterate over comments using `{{ticket.comments}}`.
- [**Formatted comment placeholders**](#topic_jkz_opl_rc__table_w5b_hl2_mg) allow you to return preformatted, rendered HTML representations of the standard placeholders, but without a large degree of customization. They simply return comments in predefined formats. For example, `{{ticket.comments_formatted}}` returns a chunk of rendered HTML. The ticket comments will include dates, author, the author’s avatar, and the like.
- [**Rich text comment placeholders**](#topic_jkz_opl_rc__table_l22_wph_sbb) allow you to use rich text in your customized template (as with the formatted object placeholders) without being restricted to the predefined formatting rules, so you can have more control over the look and feel of your notifications. Rich text objects allow inclusion of attachments only if [Allow agents to attach files in emails](https://support.zendesk.com/hc/en-us/articles/4408832757146) is activated.

**Considerations**:

- It is recommended that [HTML comment placeholders](#topic_jkz_opl_rc__table_zrv_bzk_wtb) be used to avoid issues with attachment [size limits](https://support.zendesk.com/hc/en-us/articles/4408832757146#topic_lv2_cnx_xdb). These placeholders include attachments as inline links if they exceed the size limit. Single attachments and total attachment sizes over the size limit will not be included in placeholders such as `ticket.latest_comment` or `ticket.latest_comment_rich`.
- With simplified email threading, outbound emails from Zendesk Support don't include inline image attachments from previous user emails. See [Understanding simplified email threading](https://support.zendesk.com/hc/en-us/articles/4565992897562).
- Agents who are assigned to or following the ticket receive both public comments and internal notes. End users receive only public comments.
- If you have CCs activated, CCs (including agent CCs) receive email notifications only for public comments. See [Understanding how email notifications are sent to CCs by default](https://support.zendesk.com/hc/en-us/articles/4408843866394).
- If you're using dynamic content in your placeholder, some formatting issues may occur.
 Notably, line breaks may not be applied to multi-line or custom-text fields.

Table 5. HTML comment data

| Properties/placeholders | Description |
| --- | --- |
| {{ticket.latest\_comment\_html}} | The most recent comment, including any attachments. Agents receive the most recent public or private comment. End users receive the most recent public comment. Attachments are attached to email or added as inline links if they exceed the [size limit](https://support.zendesk.com/hc/en-us/articles/4408832757146#topic_lv2_cnx_xdb). |
| {{ticket.latest\_public\_comment\_html}} | The most recent public comment, including any attachments. Attachments are attached to email or added as inline links if they exceed the [size limit](https://support.zendesk.com/hc/en-us/articles/4408832757146#topic_lv2_cnx_xdb). |

Table 6. Standard comment data

| Properties/placeholders | Description |
| --- | --- |
| {{ticket.comments}} | Used as a placeholder, {{ticket.comments}} displays all the comments in a ticket in unformatted text. The ticket.comments placeholder also serves as a collection for comment and attachment details. You can access the following data using Liquid markup:   - comment.author.name - comment.created\_at - comment.created\_at\_with\_time - comment.is\_public (**true**  for public comments and  **false**  for   private comments) - comment.value - comment.value\_rich - comment.id - comment.attachments   - attachment.filename   - attachment.url   For an example of accessing this data in business rules, see [Customizing the format and placement of text in comments and email notifications](https://support.zendesk.com/hc/en-us/articles/4408832790042). Note: This same comment data collection is available when using the ticket.public\_comments, ticket.latest\_comment, and ticket.latest\_public\_comment placeholders. |
| {{ticket.public\_comments}} | All public comments, most recent first. Unformatted text. |
| {{ticket.latest\_comment}} | The most recent comment. Unformatted text. Does not include attachments, unless [Allow agents to attach files in emails](https://support.zendesk.com/hc/en-us/articles/4408832757146) is activated. To return attachments, use ticket.latest\_comment\_formatted. |
| {{ticket.latest\_public\_comment}} | The most recent public comment. Unformatted text. |

Table 7. Formatted comment data

| Properties/placeholders | Description |
| --- | --- |
| {{ticket.comments\_formatted}} | All comments, most recent first. |
| {{ticket.public\_comments\_formatted}} | All public comments, most recent first. |
| {{ticket.latest\_comment\_formatted}} | The most recent comment including any attachments. |
| {{ticket.latest\_public\_comment\_formatted}} | The most recent public comment including any attachments. |

Table 8. Rich text comment data

| Properties/placeholders | Description |
| --- | --- |
| {{ticket.latest\_comment\_rich}} | The most recent comment. Rich text formatting. If [Allow agents to attach files in emails](https://support.zendesk.com/hc/en-us/articles/4408832757146) is activated, attachments are included. |
| {{ticket.latest\_public\_comment\_rich}} | The most recent public comment. Rich text formatting. If [Allow agents to attach files in emails](https://support.zendesk.com/hc/en-us/articles/4408832757146) is activated, attachments are included. |

Note: [Under certain circumstances](https://support.zendesk.com/hc/en-us/articles/4408833443226) comment placeholders are suppressed for *received request* email notifications and will not receive them.

## Satisfaction rating data

On Suite Growth and above or Support Professional and Enterprise, the following data properties are available for [customer satisfaction rating for email and messaging](https://support.zendesk.com/hc/en-us/articles/4408886173338).

This table lists both current and legacy CSAT placeholders. Legacy placeholders work only for the [legacy CSAT experience](https://support.zendesk.com/hc/en-us/articles/4408822875034). The [updated CSAT option](https://support.zendesk.com/hc/en-us/articles/7689997846554) lets you customize the CSAT question, rating scale, and rating labels.

Note: Using satisfaction rating placeholders outside of business rules can result in users other than the requester submitting satisfaction scores.

Table 9. Satisfaction rating data object

| Properties | Description |
| --- | --- |
| {{satisfaction.survey\_section}} | A block of text in the CSAT email directing users to complete the CSAT survey. |
| {{satisfaction.survey\_url}} | The URL for customers to rate their support experience. |
| {{satisfaction.rating\_section}} (Legacy CSAT) | A formatted block of text prompting the user to rate satisfaction. |
| {{satisfaction.rating\_url}} (Legacy CSAT) | A URL to rate the support. |
| {{satisfaction.current\_rating}} (Legacy CSAT) | The text of the current satisfaction rating (e.g. "Good, I am satisfied"). |
| {{satisfaction.positive\_rating\_url}} (Legacy CSAT) | A URL to rate the support positively. |
| {{satisfaction.negative\_rating\_url}} (Legacy CSAT) | A URL to rate the support negatively. |
| {{satisfaction.current\_comment}} (Legacy CSAT) | The comment that the user added when rating the ticket. |

## Custom object data

On all Zendesk Suite plans and Support Enterprise plans, the following data properties are available for custom objects. These placeholders are supported by [object triggers](https://support.zendesk.com/hc/en-us/articles/6294230624410).

The standard custom object data includes the object's *name*, *ID*, and *external ID* values, which all custom objects have. These are a custom object's standard fields. The variable custom object data is unique to each custom object and depends on the custom fields created to define the object's schema.

Table 10. Standard custom object data

| Properties | Description |
| --- | --- |
| {{custom\_objects.*<object\_key>*.external\_id}} | The external ID of the custom object record. |
| {{custom\_objects.*<object\_key>*.id}} | The ID of the custom object record. |
| {{custom\_objects.*<object\_key>*.name}} | The name of the custom object record. |

Table 11. Variable custom object data

| Properties | Description |
| --- | --- |
| {{custom\_objects.*<object\_key>*.custom\_fields.*<field\_key>*}} | The value of a custom object's field. |
| {{custom\_objects.*<object\_key>*.custom\_fields.*<field\_key>*.title}} | The value of a drop-down field. |
| {{custom\_objects.*<object\_key>*.custom\_fields.*<field\_key>*.id}} | The ID of the target object in a lookup relationship field. |
| {{custom\_objects.*<object\_key>*.custom\_fields.*<field\_key>*.name}} | The name of the lookup relationship field. |