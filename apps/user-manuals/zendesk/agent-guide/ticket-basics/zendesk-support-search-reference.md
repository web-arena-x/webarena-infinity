# Zendesk Support search reference

Source: https://support.zendesk.com/hc/en-us/articles/4408886879258-Zendesk-Support-search-reference

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article contains tables listing and describing data property keywords and values that can be used, along with common search operators, to narrow your search results. There are also sections describing more advanced search methods and formatting.

This article is aimed at administrators and support managers with full access to the data in Zendesk Support. If you're an agent, start with [Searching the data in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408894221594) and refer back to this reference article if you want to perform more advanced searches.

This article includes the following topics on advanced search methods:

- [Search terms and terminology](#topic_mq4_5qj_nlb)
- [Searching for properties that contain no data](#topic_fhr_wsc_3v)
- [Searching by date and time](#topic_ghr_wsc_3v)
- [Sorting search results](#topic_lhr_wsc_3v)
- [Using the 'type' keyword](#topic_ohr_wsc_3v)
- [Using the 'user' keyword](#topic_usk_q2b_pmb)
- [Search FAQ](#topic_qhr_wsc_3v)

This article includes the following reference tables:

- [Search operators](#topic_ngr_frb_vc)
- [Ticket property keywords](#topic_crj_yev_uc)
- [User property keywords](#topic_rvz_afv_uc)
- [Organization property keywords](#topic_gok_ffv_uc)
- [Group property keywords](#topic_wcx_ifv_uc)
- [Satisfaction rating searchable values](#topic_nms_sgd_jf)

Note: It can take a few minutes for Zendesk Support to index new and modified tickets, users, and other resources, so they might not appear in search results right away. Also, search returns only the first 1,000 results even if there are more results.

## Search terms and terminology

### Search terms

Search terms are user-defined words, phrases, or values. Examples:

- 3245227
- Greenbriar
- serial number
- "Jane Doe"

Search terms are case-insensitive. For example, "App" and "app" return the same results.

A single-word search term returns a result if it appears in the data as follows:

- a single word
- a single word in a longer phrase
- the prefix of a longer word

The search term will not return a result if it appears in the data as follows:

- in the middle of a word
- at the end of a word

For example, the search term "top" would match "top", "top tier", "Top Ten Trucking", "Tip-Top Mops", "Big Top Entertainment", and "Dessert Toppings, Inc". It would not match "Desktop Solutions" or "One-Stop Publishing".

Search terms can consist of multiple words. There is a 64 word limit in a search query. Enclose the words in double quotes if you want the search to only return exact matches. Example: "Jane Doe". You can omit the quotes, in which case search reverts to AND matching logic. In other words, all the words must be present in the record in any order for a match. For example, searching for the following phrase returns results only if all the words are present, in any order.

```
Please upgrade my account
```

### Property keywords

You can narrow your results by combining *property keywords* with search terms and [operators](#topic_ngr_frb_vc). Example:

```
status<solved
```

A property keyword is the name of a property in a ticket, a user, an organization, or a group. Examples:

- assignee
- created
- name

See the following property keyword references for all the properties and details about each:

- [Ticket property keywords](#topic_crj_yev_uc)
- [User property keywords](#topic_rvz_afv_uc)
- [Organization property keywords](#topic_gok_ffv_uc)
- [Group property keywords](#topic_wcx_ifv_uc)

Example property searches:

| Search | Property keyword | Returns |
| --- | --- | --- |
| priority>normal | priority | Tickets with a priority of high or urgent |
| subject:2fa | subject | Tickets with the search term 2fa in the subject |
| email:jdoe@example.com | email | The user with the email jdoe@example.com |

Some properties have predefined values. For example, the ticket status property has the following predefined values: new, open, pending, hold, solved, closed. You can only search by these values. Example search: `status:open`. See the property keyword references for details about each property.

Other properties accept user-defined search terms. Example: `subject:2fa`. See [Search terms](#topic_jfw_rsj_nlb). The same matching rules apply for property searches with the exception of prefix matching. Results are not returned if the search term appears as the prefix of a longer word. For example, the search term "tier" would return results for "tier 1" and "tier 2" but not "tiered".

You can search for multiple values of a single property by including the property keyword multiple times in a query. Example:

```
tags:silver tags:bronze
```

Search uses OR logic for matching in this case. The previous example returns results that contain either the tag "silver" or the tag "bronze".

### Example search

The following search expression looks for anything with the tag "vip" that was created before May 1, 2019:

```
tags:vip created<2019-05-01
```

How it works:

- **tags** is a property keyword indicating you're searching only within a specific data property, in this case a *tag*.
- **:** is the "equal to" operator indicating the *tag* property value needs to be equal to the subsequent search term. Note that there's no space before or after the **:**.
- **vip** is the search term.
- **created** is a property keyword indicating you're searching the *created* data property for items created relative to a certain date.
- **<** is the "less than" operator indicating you're searching for records created before a certain date.
- **2015-05-01** is a search term indicating the date you want to use.

## Searching for properties that contain no data

Properties that contain no data can be searched for using `none` as the search term, along with the *group*, *tags*, *via*, *organization*, or *assignee* keywords, as in this example:

```
assignee:none
```

This returns all unassigned tickets.

## Searching by date and time

Date property keywords - *created*, *updated*, *solved*, and *due date*) can be combined with search operators to return data from a specific date, before a certain date, and after a certain date. To search dates in any locale, use the format YYYY-MM-DD. You can also use locale-specific formats such as MM/DD/YYYY in the United States.

To search for data before a certain date, use the less than (**<**) operator:

```
created<2011-05-01
```

To search for data after a certain date, use the greater than (>) operator:

```
due_date>2010-01-10
```

To search for a specific date, use the equals (**:**) operator:

```
solved:2010-01-10
```

You can also use the *<=* or *>=* operators to indicate *less-than-or-equal-to* and *greater-than-or-equal-to* respectively.

### Searching with combined dates and times

You can specify a combined date and time using [ISO8601 syntax](https://en.wikipedia.org/wiki/ISO_8601):

```
created>2015-09-01T12:00:00-08:00
updated<2015-09-01T12:00:00Z
```

The first example above searches for anything created after September 1, 2015 at 12:00 p.m. (Pacific Standard Time).

The second example above searches for anything updated before September 1, 2015 at 12:00 p.m. (UTC).

### Searching within a date/time range

You can search within a date range, for example August 2, 2014 through August 4, 2014, using the following search statement:

```
created>2014-08-01 created<2014-08-05
```

You can also include specific times in your search range. The following example searches for anything created between August 1, 2014 at 11:59 p.m. (UTC) and August 4, 2014 at midnight (UTC):

```
created>2014-08-01T23:59:00Z created<2014-08-04T23:59:59Z
```

### Searching with relative times

You can search for a time relative to the present time, using the time units *hours*, *minutes*, *days*, *weeks*, *months*, or *years*. The following search returns anything created in the last four hours:

```
created>4hours
```

## Sorting search results

You can sort your search results by field, in ascending or descending order, using the following keyword phrases:

- `order_by:field`
- `sort:asc` or `sort:desc`

Sorting is available on the following fields:

- `created`
- `commented`
- `priority`
- `status`
- `ticket_type`

Using the `order_by` and `sort` keywords is equivalent to using the API parameters `sort_by` and `sort_order`.

## Using the 'type' keyword

One of the tools you have available for narrowing your search results is the `type` keyword. It is used to explicitly declare that you want to search for one of the following types:

- ticket
- user
- organization
- group

Using the `type` keyword means that you are explicitly searching on the type you specify. For example, you can search for all the users that belong to the customer's organization using this search statement:

```
type:user organization:customers
```

If you instead searched for `organization:customers` you would also get all the tickets that have requesters who belong to this organization. This is because searches that do not explicitly specify type return results for all types, including tickets (and organization is a ticket property).

Using `type:user`, your search returns all users that belong to the Customers organization. So, you're narrowing your search to the user type and excluding tickets.

While organizations and groups are properties of the user object, they have their own properties that can be searched as well. The following query allows you search only for organization tags, excluding tags of the same name that may be used in other elements of your Zendesk Support instance such as tickets and forum topics.

```
type:organization tags:premium
```

## Using the 'user' keyword

To search for a user's profile data, you have the following two options.

Using the `user` keyword:

```
user:amy
```

Or, using the `type:user` keyword:

```
type:user amy
```

For more information about the `user`keyword and how it's different from the `type:user` keyword, see the section about [The user and type keywords](https://support.zendesk.com/hc/en-us/articles/4408883318554#ariaid-title3) in *Searching users, groups, and organizations*.

## Search FAQ

- **How soon can new data be searched?**

 When you add new data to Zendesk Support, it typically takes about a minute before it's indexed and can be searched.
- **How does punctuation affect search?**

 Punctuation characters are generally not included in searches.
- **Are there limitations to wildcard searches?**

 You can only do wildcard searches when combined with property keywords (`subject:photo*`).
- **Who can search what?**

 Administrators can search all the data in Zendesk Support. Agents can search the data that they've been granted access to. End-users can do full text searches of the knowledge base.
- **What languages are supported?**

 There is language-specific support for searching in the following languages:
 - Brazilian Portuguese
 - Dutch
 - English
 - French
 - German
 - Italian
 - Japanese
 - Russian
 - Spanish

 The support includes dictionary-based tokenization for Japanese, because words are not separated by spaces in that language. For the other languages, the language-specific support is primarily stemming. This means that different forms of the same word can be matched. For instance, both singular and plural forms of a word will typically match. Additionally, if you use the plural form in quotation marks (for example, "cats"), the search will still return results for both "cat" and "cats".

## Search operators

You can use the following search operators to build your search statements.

When using operators in your search queries, you must *not* enter a space before or after the operator. For example, entering `updated<2025-07-04` uses “updated” as the operator, while `updated < 2025-07-04` searches for the word “updated”.

Table 1. Search operators

   | Operator | Description |
| --- | --- |
| : | The colon indicates that the given field should equal the specified value. ``` status:open ``` |
| < | Less than. ``` status<closed ``` |
| > | Greater than. ``` priority>normal ``` |
| <= | Less than or equal to. ``` status<=pending ``` |
| >= | Greater than or equal to. ``` priority>=normal ``` |
| " " | Double quotes. In a simple keyword search, this is referred to as a phrase search and returns the exact words in the exact order; however, punctuation characters are not included. ``` "Please upgrade my account" ```   Note: In the Japanese version of Support, this feature does not work as expected. A simple keyword search that includes double quotes returns results, but the results are not the exact words in the exact order. In a search including data properties, use double quotes to perform an inclusive AND search, returning results that include *all* properties in the search. ``` tags:"superman is_awesome" ``` |
| - | Minus sign. Excludes items containing a word (or property value) from the search results. For example, the following statement searches for any tickets with the status 'pending', but excludes any tickets containing the tag 'invoice' from the search results: ``` status:pending -tags:invoice ``` |
| \* | The wildcard operator is useful when you want to search various forms of a word. For example, searching for `photo*` returns results that would include photography, photographer, photograph and any other words that began with 'photo'. However, because of the performance issues involved with doing wildcard searches, unqualified wildcard searches are not currently supported. In other words, you need to use a property keyword to make your search specific to the data you're trying to locate. ``` subject:photo* ``` |

## Ticket property keywords

You can search on the following ticket properties.

For more information about ticket search, see [Searching tickets](https://support.zendesk.com/hc/en-us/articles/4408882086298).

Table 2. Searchable ticket properties

   | Keyword | Description |
| --- | --- |
| Ticket ID | There isn't a property keyword for the ticket ID. Instead, you simply search for the ticket by its ID number in the following format: ``` 233 ``` |
| `created` | The date, or date and time, the ticket was created. Enter date in yyy-mm-dd format. ``` created:2011-05-01 ``` Search within a date or time range. Enter times using [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) syntax. For example, to search for a ticket created between 10:30 a.m. and 12 p.m. (UTC) on August 1, 2014: ``` created>2014-08-01T10:30:00Z created<2014-08-01T12:00:00Z ``` For more information on using date and time in your search, see [Searching by date and time](https://support.zendesk.com/hc/en-us/articles/4408835086106#topic_gbg_dvw_ld). |
| `updated` | The date of the most recent ticket update. ``` updated>2011-05-15 ``` For more information on using date and time in your search, see [Searching by date and time](https://support.zendesk.com/hc/en-us/articles/4408835086106#topic_gbg_dvw_ld). |
| `solved` | The date the ticket was set to solved. ``` solved<2011-06-01 ``` For more information on using date and time in your search, see [Searching by date and time](https://support.zendesk.com/hc/en-us/articles/4408835086106#topic_gbg_dvw_ld). |
| `due_date` | The due date of tickets. ``` due_date:2011-06-01 ``` For more information on using date and time in your search, see [Searching by date and time](https://support.zendesk.com/hc/en-us/articles/4408835086106#topic_gbg_dvw_ld). |
| `assignee` | The assigned agent or other entity. You can specify "none", "me", user name (full name or partial), email address, user ID, or phone number (see the [`phone` user property](#topic_rvz_afv_uc) for help searching by phone number). ``` assignee:"Susan Warren" ``` |
| `submitter` | The ticket submitter. This may be different than the requester if the ticket was submitted by an agent on behalf of the requester. You can specify "none", "me", user name (full name or partial), email address, user ID, or phone number (see the [`phone` user property](#topic_rvz_afv_uc) for help searching by phone number). See [Searching ticket user roles](https://support.zendesk.com/hc/en-us/articles/4408882086298#topic_xca_cjv_uc). ``` submitter:me ``` |
| `requester` | The ticket requester. You can specify "none", "me", user name (full name or partial), email address, user ID, or phone number (see the [`phone` user property](#topic_rvz_afv_uc) for help searching by phone number). ``` requester:amy@mondocam.com ``` |
| `subject` | The text in the ticket's subject. ``` subject:"upgrade account" ``` |
| `description` | The text in the ticket's description and comments. ``` description:defective ``` |
| `custom_status_id` | If [custom ticket statuses are activated](https://support.zendesk.com/hc/en-us/articles/4412575841306), search for a specific system or custom ticket status. Specify the status by its numeric ID, which you can find on the Ticket statuses page when [editing a ticket status](https://support.zendesk.com/hc/en-us/articles/4412575941402#topic_wqd_t1h_vrb). ``` custom_status_id:2393906 ``` |
| `status` | Possible values: new, open, pending, hold, solved, closed. ``` status<closed ``` |
| `ticket_type` | Possible values: question, incident, problem, task. ``` ticket_type:problem ``` |
| `support_type` | (Applicable only for messaging tickets) Indicates whether a ticket was handled entirely by an AI agent or whether a human agent was involved. Possible values: ai\_agent, agent. For more information, see [Understanding and viewing AI agent tickets for AI agent–only conversations](https://support.zendesk.com/hc/en-us/articles/9204149016346). ``` support_type:ai_agent ``` |
| `priority` | Possible values: low, normal, high, urgent. ``` priority>low ``` |
| `group` | Specify the name or ID of a group. Returns tickets assigned to agents who are members of the group. Examples: ``` group:"Level 2" ``` ``` group:20663166 ``` |
| `organization` | Specify the name or ID of an organization. Returns tickets by requesters who are members of the organization. Examples: ``` organization:customers ``` ``` organization:22989442 ``` You can also specify "none" to return tickets by requesters who are not members of any organization. ``` organization:none ``` |
| `tags` | Specify tags that have been added to the ticket or "none." ``` tags:premium ``` To find tickets that include either of two tags, use: ``` tags:important tags:urgent ``` To find tickets that include both tags: ``` tags:"important urgent" ``` |
| `via` | The ticket's source, for example: - mail (from an email message) - get\_satisfaction, get\_sat, "get satisfaction" (from Get Satisfaction) - closed\_ticket (from a followup ticket) - ticket\_sharing - dropbox (from the Zendesk Feedback Tab) - chat (from Chat) - twitter\_dm, "twitter dm", "twitter direct" (from a Twitter direct message) - twitter\_fav, twitter\_favorite, "twitter favorite" (from a Twitter favorite) - twitter\_like, "twitter like" (from a Twitter like; alias of twitter\_fav) - twitter (from any Twitter method including direct message and favorite) - voicemail (from a voicemail message) - phone\_call\_inbound (from an inbound phone call) - phone\_call\_outbound (from an outbound phone call) - phone (from voicemail, CTI, or an inbound call) - sms, text, "text message" (from a text message) - api (from API call or integrated web service) - logmein, logmein\_rescue, "logmein rescue" (from LogMeIn) - facebook\_post, "facebook post" (from a Facebook wall post to a page) - facebook\_message, "facebook message" (from a Facebook private message to a page) - facebook (from any Facebook method including private message and wall post) - web, "web form" (from a web form) - mobile\_sdk (tickets created using the Zendesk mobile SDK) - "any\_channel" (from the channel framework) - native\_messaging (from the messaging channel) - side\_conversation (from a side conversation) - sunshine\_conversations\_facebook\_messenger - answer\_bot\_for\_web\_widget (from Answer bot tickets)   ``` via:phone ``` For a full list of sources, see [Via types reference in the Zendesk developer documentation](https://developer.zendesk.com/documentation/ticketing/reference-guides/via-types/). |
| `commenter` | People who have added comments to tickets. You can specify "none", "me", user name (full name or partial), email address, user ID, or phone number (see the [`phone` user property](#topic_rvz_afv_uc) for help searching by phone number). ``` commenter:"Mike" ``` |
| `cc` | People who have been CC'd on tickets. You can specify "none", "me", user name (full name or partial), email address, user ID, or phone number (see the [`phone` user property](#topic_rvz_afv_uc) for help searching by phone number). ``` cc:amanda@mondocam.com ``` |
| `fieldvalue` | Search for a specific value in any custom ticket fields by using the `fieldvalue` keyword. For example: ``` fieldvalue:12345 ``` This returns all the tickets that have a custom field with the value "12345." For drop-down custom fields, search for tags associated with the field value you want to find. For checkbox custom fields, you can search for tickets with the field checked or unchecked. For example: ``` custom_field_<Field ID>:checked ``` |
| `custom_field_{id}` | Search for a value of a specific custom ticket field. Specify the field by its numeric ID, which you can get from the URL of the Ticket Fields page in the admin interface or with the [Ticket Fields](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_fields/) API. The syntax is `custom_field_<custom field ID>:<value>`. Example: ``` custom_field_455214213:shoes ``` See [Searching custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4408882086298#topic_wly_fev_uc). |
| `brand` | Search for a specific brand on a ticket using the brand name or the brand ID. A brand with two or more words requires quotation marks. For example: ``` brand:Nordstrom ```   Or ``` brand: "Banana Republic" ``` Or   ``` brand:<ID number> ``` |
| `has_attachment` | Search for all tickets with or without attachments using `true` or `false`. To search for tickets with attachments:   ``` has_attachment:true ```   To search for all tickets without attachments:   ``` has_attachment:false ``` |
| `form` | Search for all tickets created with a particular ticket form. If the name of the ticket form includes multiple words, use quotation marks. For example:   ``` form:"default ticket form" ```   If the name of the ticket form is a single word, you don't have to use the quotation marks. For example:   ``` form:legal ``` |
| `recipient` | Search for all tickets created with a particular recipient. This only works for Zendesk support addresses (the ultimate destination) of emails forwarded from external addresses. ``` recipient:support@yoursubdomain.zendesk.com ``` |
| `comment` | Search for text within a ticket's comment. ``` comment:fancy ```   To search for an exact match within the comments of a ticket, use double quotes.   ``` comment:"fancy things here" ```   Note: Only the first 500 comments in a ticket are searched. |

## User property keywords

Here's the list of user properties that can be searched.

For more information about searching users, see [Searching for users, groups, and organizations](https://support.zendesk.com/hc/en-us/articles/4408883318554).

Table 3. User property keywords

   | Keyword | Description |
| --- | --- |
| `name` | The user's partial or full name. ``` name:"alex anderson" ``` |
| `role` | The user's designated role. ``` role:admin ``` |
| `email` | Specify the user's email address, or specify none to search for users without an email address. ``` email:alex@mondocam.com ``` ``` email:"none" ```   Using double quotes to search for an email address does not return an exact match like other keyword searches. For example, if you search the following the results may return any user whose email starts with "dwight": ``` email:"dwight@mondocam.com" ``` Tip: Wildcards do not work for email address searches. For example, the following search returns no results: ``` email:dwight* ``` |
| `group` | The user's group name. This only applies to admin and agent users. ``` group:"Level 2" ``` |
| `organization` | Specify the user's organization name or ID, or specify `none` to search for users without an organization. If the user belongs to more than one organization, searching on any of those organizations will return their profile. ``` organization:mondocam ``` |
| `created` | The date the user was added to your Zendesk. ``` created<2011-05-01 ```   For more information on using date and time in your search, see [Searching by date and time](https://support.zendesk.com/hc/en-us/articles/4408835086106#topic_gbg_dvw_ld). |
| `notes` | All text in the notes field in the user's profile. ``` notes:"manager" ``` |
| `details` | All text in the details field in the user's profile. ``` details:"madison, wi" ``` |
| `external_id` | Specify the user's external ID, if used, or specify`none` to search for users without an external ID. ``` external_id:0098884412 ``` |
| `phone` | Specify the user's phone number, or specify `none` to search for users without a phone number. ``` phone:+555-111-2222 ```   When searching by phone number, you must include a plus sign (+) before the number. When searching by phone number using the API, you must include %2B (the URL-encoded version of +) before the number (for example, `/api/v2/search?query=type:phone:%2B555-111-2222`). |
| `tags` | Specify tags on the user's profile, or specify `none` to search for users without tags. ``` tags:premium tags:wholesale ``` For more information about tagging users and organizations, see [Adding tags to users and organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658). |
| `customfield` | Custom user fields. ``` plan_type:platinum ``` For more information, see [Searching custom user and organization fields](https://support.zendesk.com/hc/en-us/articles/4408883318554#topic_pyt_m1s_vk). |
| `is_verified` | Indicates whether any of a user's identities have been verified. - **is\_verified:false Sunita** returns all users named Sunita who do not have a verified identity. - **is\_verified:true** returns all users with a verified identity.   Any user created via [ticket sharing](https://support.zendesk.com/hc/en-us/articles/4408893967514) is automatically verified. |
| `is_suspended` | Indicates whether the user has been suspended. - **is\_suspended:true Sunita** returns all users named Sunita who have been suspended. - **is\_suspended:true** returns all users who have been suspended. |
| whatsapp | Search for users based on a WhatsApp phone number. For more information see [Searching for tickets by WhatsApp number](https://support.zendesk.com/hc/en-us/articles/5869718332954). |

## Organization property keywords

Here's the list of organization properties that can be searched. For more information, see [Searching for users, groups, and organizations](https://support.zendesk.com/hc/en-us/articles/4408883318554).

Table 4. Organization property keywords

   | Keyword | Description |
| --- | --- |
| `name` | The organization's partial or full name. ``` name:mondocam ``` |
| `created` | The date the organization was added. ``` created<2011-05-01 ```   For more information on using date and time in your search, see [Searching by date and time](https://support.zendesk.com/hc/en-us/articles/4408835086106#topic_gbg_dvw_ld). |
| `notes` | All text in the notes field in the user's profile. ``` notes:EMEA ``` |
| `details` | All text in the details field in the organization's profile. ``` details:london ``` |
| `tags` | Specify tags that have been added to the organization, or specify `none` to search for organizations without tags. ``` tags:premium ```   For more information about tagging users and organizations, see [Adding tags to users and organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658). |
| `customfield` | Custom organization fields. ``` plan_type:platinum ``` For more information, see [Searching custom user and organization fields](https://support.zendesk.com/hc/en-us/articles/4408883318554#topic_pyt_m1s_vk). |
| `external_id` | The external ID of the organization or specify **none** to search for users without an external ID. ``` external_id:00112345 ``` |

## Group property keywords

Here's the list of group properties that can be searched. For more information, see [Searching for users, groups, and organizations](https://support.zendesk.com/hc/en-us/articles/4408883318554).

Table 5. Group property keywords

   | Keyword | Description |
| --- | --- |
| `name` | The group's name. ``` name:"level 2" ``` |
| `created` | The date the group was added. ``` created<2011-05-01 ``` For more information on using date and time in your search, see [Searching by date and time](https://support.zendesk.com/hc/en-us/articles/4408835086106#topic_gbg_dvw_ld). |

## Satisfaction rating searchable values

You can use the `satisfaction` keyword with rating values to search your customer satisfaction ratings. For more information on customer satisfaction, see [Using customer satisfaction rating](https://support.zendesk.com/hc/en-us/articles/4408886173338).

Table 6. Satisfaction rating keywords

   | Value | Description |
| --- | --- |
| `bad` | Tickets that have been rated 'bad'. ``` satisfaction:bad ``` |
| `badwithcomment` | Tickets that have been rated 'bad' that also include a comment from the ticket requester. ``` satisfaction:badwithcomment ``` |
| `good` | Tickets that have been rated 'good'. ``` satisfaction:good ``` |
| `goodwithcomment` | Tickets that have been rated 'good' that also include a comment from the ticket requester. ``` satisfaction:goodwithcomment ``` |
| `offered` | When you request a customer satisfaction rating, the ticket satisfaction rating status is set to 'offered'. The following notification is added to the ticket: Customer satisfaction feedback was offered. This means that you've asked for but not yet received a response to the rating request. ``` satisfaction:offered ``` |