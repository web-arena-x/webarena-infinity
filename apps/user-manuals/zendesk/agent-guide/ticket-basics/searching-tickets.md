# Searching tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408882086298-Searching-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Full text searches return results from all the data in Zendesk Support. To search exclusively for ticket data, you can use ticket property keywords.

```
status:open
```

In the example above, `status` is the keyword and `open` is the value. This search returns all the tickets with status set to open. This of course directly maps to the ticket fields and their values.

You can combine these keyword search statements to narrow your results even further.

```
status:open group:"Level 2"
```

This returns all the open tickets that are assigned to the Level 2 support group.

This article covers the following topics:

- [Ticket property keywords](#topic_cw3_lb3_mv)
- [Searching ticket user roles](#topic_xca_cjv_uc)
- [Searching custom ticket fields](#topic_wly_fev_uc)
- [Searching for ticket attachments](#topic_nb2_pjb_n3)
- [Searching for tickets with a specific ticket form](#topic_khr_wsc_3v)
- [Searching for tickets by telephone number](#topic_zmj_mnd_3v)
- [Searching for yourself](#topic_x5b_xrb_mv)
- [Ordering and sorting ticket search results](#topic_ctp_yiv_uc)

For a quick reference to all searchable data, see [Zendesk Support search reference](https://support.zendesk.com/hc/en-us/articles/4408886879258).

## Ticket property keywords

The ticket property keywords and their values that you can use in your searches are described in the following table. Not all of the ticket data is searchable. Administrators and agents can search for tickets using these keywords.

Table 1. Searchable ticket properties

| Keyword | Description |
| --- | --- |
| Ticket ID | There isn't a property keyword for the ticket ID. Instead, you simply search for the ticket by its ID number in the following format: ``` 233 ``` |
| `created` | The date, or date and time, the ticket was created. Enter date in yyy-mm-dd format. ``` created:2011-05-01 ``` Search within a date or time range. Enter times using [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) syntax. For example, to search for a ticket created between 10:30 a.m. and 12 p.m. (UTC) on August 1, 2014: ``` created>2014-08-01T10:30:00Z created<2014-08-01T12:00:00Z ``` For more information on using date and time in your search, see [Searching by date and time](https://support.zendesk.com/hc/en-us/articles/4408835086106#topic_gbg_dvw_ld). |
| `updated` | The date of the most recent ticket update. ``` updated>2011-05-15 ``` For more information on using date and time in your search, see [Searching by date and time](https://support.zendesk.com/hc/en-us/articles/4408835086106#topic_gbg_dvw_ld). |
| `solved` | The date the ticket was set to solved. ``` solved<2011-06-01 ``` For more information on using date and time in your search, see [Searching by date and time](https://support.zendesk.com/hc/en-us/articles/4408835086106#topic_gbg_dvw_ld). |
| `due_date` | The due date of tickets. ``` due_date:2011-06-01 ``` For more information on using date and time in your search, see [Searching by date and time](https://support.zendesk.com/hc/en-us/articles/4408835086106#topic_gbg_dvw_ld). |
| `assignee` | The assigned agent or other entity. You can specify "none", "me", user name (full name or partial), email address, user ID, or phone number (see the [`phone` user property](https://support.zendesk.com/hc/en-us/articles/4408886879258#topic_rvz_afv_uc) for help searching by phone number). ``` assignee:"Susan Warren" ``` |
| `submitter` | The ticket submitter. This may be different than the requester if the ticket was submitted by an agent on behalf of the requester. You can specify "none", "me", user name (full name or partial), email address, user ID, or phone number (see the [`phone` user property](https://support.zendesk.com/hc/en-us/articles/4408886879258#topic_rvz_afv_uc) for help searching by phone number). See [Searching ticket user roles](https://support.zendesk.com/hc/en-us/articles/4408882086298#topic_xca_cjv_uc). ``` submitter:me ``` |
| `requester` | The ticket requester. You can specify "none", "me", user name (full name or partial), email address, user ID, or phone number (see the [`phone` user property](https://support.zendesk.com/hc/en-us/articles/4408886879258#topic_rvz_afv_uc) for help searching by phone number). ``` requester:amy@mondocam.com ``` |
| `subject` | The text in the ticket's subject. ``` subject:"upgrade account" ``` |
| `description` | The text in the ticket's description and comments. ``` description:defective ``` |
| `custom_status_id` | If [custom ticket statuses are activated](https://support.zendesk.com/hc/en-us/articles/4412575841306), search for a specific system or custom ticket status. Specify the status by its numeric ID, which you can find on the Ticket statuses page when [editing a ticket status](https://support.zendesk.com/hc/en-us/articles/4412575941402#topic_wqd_t1h_vrb). ``` custom_status_id:2393906 ``` |
| `status` | Possible values: new, open, pending, hold, solved, closed. ``` status<closed ``` |
| `ticket_type` | Possible values: question, incident, problem, task. ``` ticket_type:problem ``` |
| `priority` | Possible values: low, normal, high, urgent. ``` priority>low ``` |
| `group` | Specify the name or ID of a group. Returns tickets assigned to agents who are members of the group. Examples: ``` group:"Level 2" ``` ``` group:20663166 ``` |
| `organization` | Specify the name or ID of an organization. Returns tickets by requesters who are members of the organization. Examples: ``` organization:customers ``` ``` organization:22989442 ``` You can also specify "none" to return tickets by requesters who are not members of any organization. ``` organization:none ``` |
| `tags` | Specify tags that have been added to the ticket or "none." ``` tags:premium ``` To find tickets that include either of two tags, use: ``` tags:important tags:urgent ``` To find tickets that include both tags: ``` tags:"important urgent" ``` |
| `via` | The ticket's source, for example: - mail (from an email message) - get\_satisfaction, get\_sat, "get satisfaction" (from Get   Satisfaction) - closed\_ticket (from a followup ticket) - ticket\_sharing - dropbox (from the Zendesk Feedback Tab) - chat (from Chat) - twitter\_dm, "twitter dm", "twitter direct" (from a Twitter   direct message) - twitter\_fav, twitter\_favorite, "twitter favorite" (from a   Twitter favorite) - twitter\_like, "twitter like" (from a Twitter like; alias of   twitter\_fav) - twitter (from any Twitter method including direct message and   favorite) - voicemail (from a voicemail message) - phone\_call\_inbound (from an inbound phone call) - phone\_call\_outbound (from an outbound phone call) - phone (from voicemail, CTI, or an inbound call) - sms, text, "text message" (from a text message) - api (from API call or integrated web service) - logmein, logmein\_rescue, "logmein rescue" (from LogMeIn) - facebook\_post, "facebook post" (from a Facebook wall post to a   page) - facebook\_message, "facebook message" (from a Facebook private   message to a page) - facebook (from any Facebook method including private message and   wall post) - web, "web form" (from a web form) - mobile\_sdk (tickets created using the Zendesk mobile SDK) - "any\_channel" (from the channel framework) - native\_messaging (from the messaging channel) - side\_conversation (from a side conversation) - answer\_bot\_for\_web\_widget (from Answer bot tickets)   ``` via:phone ``` For a full list of sources, see [Via types reference in the Zendesk developer documentation](https://developer.zendesk.com/documentation/ticketing/reference-guides/via-types/). |
| `commenter` | People who have added comments to tickets. You can specify "none", "me", user name (full name or partial), email address, user ID, or phone number (see the [`phone` user property](https://support.zendesk.com/hc/en-us/articles/4408886879258#topic_rvz_afv_uc) for help searching by phone number). ``` commenter:"Mike" ``` |
| `cc` | People who have been CC'd on tickets. You can specify "none", "me", user name (full name or partial), email address, user ID, or phone number (see the [`phone` user property](https://support.zendesk.com/hc/en-us/articles/4408886879258#topic_rvz_afv_uc) for help searching by phone number). ``` cc:amanda@mondocam.com ``` |
| `fieldvalue` | Search for a specific value in any custom ticket fields by using the `fieldvalue` keyword. For example: ``` fieldvalue:12345 ``` This returns all the tickets that have a custom field with the value "12345." For drop-down custom fields, search for tags associated with the field value you want to find. For checkbox custom fields, you can search for tickets with the field checked or unchecked. For example: ``` custom_field_<Field ID>:checked ``` |
| `custom_field_{id}` | Search for a value of a specific custom ticket field. Specify the field by its numeric ID, which you can get from the URL of the Ticket Fields page in the admin interface or with the [Ticket Fields](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_fields/) API. The syntax is `custom_field_<custom field ID>:<value>`. Example: ``` custom_field_455214213:shoes ``` You can search for values ranging from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807. See [Searching custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4408882086298#topic_wly_fev_uc). |
| `brand` | Search for a specific brand on a ticket using the brand name or the brand ID. A brand with two or more words requires quotation marks. For example: ``` brand:Nordstrom ```   Or ``` brand: "Banana Republic" ``` Or   ``` brand:<ID number> ``` |
| `has_attachment` | Search for all tickets with or without attachments using `true` or `false`. To search for tickets with attachments:   ``` has_attachment:true ```   To search for all tickets without attachments:   ``` has_attachment:false ``` |
| `form` | Search for all tickets created with a particular ticket form. If the name of the ticket form includes multiple words, use quotation marks. For example:   ``` form:"default ticket form" ```   If the name of the ticket form is a single word, you don't have to use the quotation marks. For example:   ``` form:legal ``` |
| `recipient` | Search for all tickets created with a particular recipient. This only works for Zendesk support addresses (the ultimate destination) of emails forwarded from external addresses. ``` recipient:support@yoursubdomain.zendesk.com ``` |
| `comment` | Search for text within a ticket's comment. ``` comment:fancy ```   To search for an exact match within the comments of a ticket, use double quotes.   ``` comment:"fancy things here" ```   Note: Only the first 500 comments in a ticket are searched. |

All of the ticket property keywords can be used in search statements alone, in combination with other ticket property keywords, or with the `type` keyword (see Using the type keyword).

## Searching ticket user roles

Users have various roles on tickets (requester, assignee, etc). These user roles can be searched by the user's ID, their name (partial or full), or their email address, as in these examples:

```
requester:52789480
submitter:amy
assignee:"amy moore"
requester:amy@mondocam.com
```

Notice that none of these searches required the ID, or name, or email to be explicitly declared. Each of these keywords accepts all of these user identifiers.

## Searching custom ticket fields

You can search for a specific value in custom ticket fields by using the `fieldvalue` keyword. For example:

```
fieldvalue:12345
```

This returns all the tickets that have a custom field with the value "12345."

If your custom field assigns a tag to the ticket, you can also search for custom ticket fields using the tags that you assigned to the custom field. For example, if you created a drop-down list, you can search for the tags assigned to each list box item.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_custom_ddlist.png)

To search for specific drop-down list selections, you use the `tags` keyword.

```
tags:product_question
```

This applies to the custom field types that can be assigned tags: the drop-down list and the checkbox. The checkbox custom field can include a tag to indicate that the user has clicked the checkbox.

All of the other custom fields types except the lookup relationship field (text, multi-line text, numeric, decimal, regular expression) can be searched by the text or number values submitted by ticket requesters. For example, if you added a numeric custom field to the support request form to collect demographic information such as age, you can search for the numbers that the requesters entered in the form (`type:ticket "18"`).

Searching by the lookup relationship field is not supported.

Additionally, you can search only a specified custom ticket field using its ID (found on the Ticket fields page in Admin Center > Objects and rules > Tickets > Fields). For example:

| Syntax | Example |
| --- | --- |
| `custom_field_<custom field ID>:<phrase>` | `custom_field_1413:new` Returns a list of tickets where the custom ticket field with ID 1413 includes the phrase"new". |
| `-custom_field_<custom field ID>:*` | `-custom_field_1413:*` Returns a list of tickets where the custom ticket field with ID 1413 is blank. |
| `custom_field_<custom field ID>:*` | `custom_field_1413:*` Returns a list of tickets where the custom ticket field with ID 1413 is used, and not blank. |

## Searching for ticket attachments

You can use the following keywords when searching for ticket attachments.

Table 2. Ticket attachment keywords

| Keyword | Description |
| --- | --- |
| `has_attachment` | You use this keyword to search for tickets that either do or not contain file attachments. There are two valid values for this keyword: `true` and `false`. ``` has_attachment:true ``` ``` has_attachment:false ``` |
| `attachment_name` | You can also search for a file attachment by name. ``` attachment_name:image001.jpg ``` |

## Searching for tickets with a specific ticket form

You can search for a ticket form and get results for all tickets where that ticket form is applied. For example, the following search returns all tickets that use the Change Request ticket form:

```
form:"Change Request"
```

## Searching for tickets by telephone number

To locate a user's tickets based on their phone number, you can use a search statement like this:

```
requester:+14154187506 status:new
```

This works with all of the ticket user roles: `submitter`, `requester`, and `assignee`.

## Searching for yourself

The `me` keyword value allows you to search user properties in tickets where the value is your own user account (as the currently logged in user).

```
assignee:me
```

This works for all the user role properties in tickets:

- `requester:me`
- `submitter:me`
- `assignee:me`

For information about searching for user profile data, see [Searching users](../customer-management-and-profiles/searching-users-groups-and-organizations.md#topic_duj_sbb_vc).

## Ordering and sorting ticket search results

Search results can be ordered and sorted using the `order_by` and `sort` keywords.

You need to use both of the keywords together in a search statement, as in this example:

```
status:new order_by:updated_at sort:asc
```

Here are the valid sorting and ordering keyword and value pairs that you can use:

- `sort:asc`
- `sort:desc`
- `order_by:priority`
- `order_by:status`
- `order_by:ticket_type`
- `order_by:updated_at`
- `order_by:created_at`

All of the `order_by` and `sort` keyword/values pairs can be used when searching ticket data.