# Using Zendesk Support advanced search

Source: https://support.zendesk.com/hc/en-us/articles/4408835086106-Using-Zendesk-Support-advanced-search

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

In addition to full text search, you can perform an advanced search using common
search operators combined with data property keywords and values to narrow
your results.

Administrators can search everything and agents can search the tickets and users
that they have permission to see. Use this article in conjunction with the
[Zendesk Support search reference](https://support.zendesk.com/hc/en-us/articles/4408886879258), which
contains tables listing and describing the full set of keywords and values
you can use, to perform an advanced search.

Topics covered in this article:

- [Performing an advanced
  search](#topic_v5y_pp3_y5)
- [Advanced search terms and
  terminology](#topic_j4c_44w_rm)
- [Search
  operators](#topic_ngr_frb_vc)
- [Searching for properties
  that contain no data](#topic_qmq_oxc_vc)
- [Searching by date and
  time](#topic_gbg_dvw_ld)
- [Sorting search
  results](#topic_bbp_5rc_y5)
- [Using the 'type'
  keyword](#topic_fqt_ztc_y5)
- [Suspended and verified users](#topic_c2b_gwj_h2b)
- [Search FAQ](#topic_ftq_rqf_x5)

Related articles:

- [Searching the data in Zendesk
  Support](https://support.zendesk.com/hc/en-us/articles/4408894221594)
- [Saving Zendesk
  Support searches](https://support.zendesk.com/hc/en-us/articles/8050806061210)

## Performing an advanced search

You can perform an advanced search in Zendesk Support.

**To perform an advanced search**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410),
   click the **Search** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_icon.png)) in the upper-right of
   the top toolbar.

   You can also hover your mouse
   over the **+Add** button, then select
   **Search** from the drop-down menu.

   Your
   most recent searches and viewed content appear in
   a menu. See [Accessing your
   recent searches](https://support.zendesk.com/hc/en-us/articles/4408894221594#topic_mn4_xxj_f1c) to learn more.
2. Enter your search terms, using the terminology,
   operators, and formatting described in the sections
   below.
3. When the search results appear, click the
   **Tickets**, **Users**, **Articles**, or
   **Organizations** tab to filter the results.

   If you anticipate performing this
   search often, you may want to [save](https://support.zendesk.com/hc/en-us/articles/8050806061210) it so
   that it's easily accessible.

   - If you currently have a ticket open and the
     [similar tickets
     feature is turned on](https://support.zendesk.com/hc/en-us/articles/8036381366426), filtering by
     **Tickets** shows you a **Similar tickets**
     header that includes any tickets related to the
     ticket you’re currently working on, if
     applicable.
   - If you’ve [turned on AI agent
     tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346-Understanding-and-viewing-AI-agent-tickets-for-AI-agent-only-conversations-EAP#topic_myq_2r1_2gc), for the initial suggested results,
     the tooltip below the ticket subject says either
     AI agent or Agent.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_similar_tickets_search.png)

Note: Due to [API rate
limits](https://developer.zendesk.com/rest_api/docs/support/search#results-limit), advanced search returns only the
first 1,000 results.

## Advanced search terms and terminology

Advanced search allows you to narrow your results by using *data
property keywords*, *operators*, and *search
terms*. In the context of an advanced search:

- **Data property keywords** indicate that you are
  restricting a search to one or more specific data
  properties.
- **Operators** are symbols used to modify the keywords
  and focus the search.
- **Search terms** are the words, phrases, or values
  you are searching for.

Search terms can include any string, including user, organization, or
group names. For example, you can search for "vip" to list all users
tagged as VIPs. However, the results will also include other data
that match the term "vip." For instance, if an
organization has "vip" in its name, like "Midwest VIP
Transportation" or "Viper Reptile Supplies,", it will appear in your
search results even if it doesn't have the VIP tag.

Note: It can take a few minutes for Support to index new and modified
tickets, users, and other resources. If they don't appear in your
search results, wait a few minutes and try again.

The following is an example of a search string looking for anything with
the tag "vip" that was created before May 1, 2015:

```
tags:vip created<2015-05-01
```

- **tags** is a keyword indicating you are searching
  only within a specific data property, in this case a
  *tag*.
- **:** is an operator indicating the *tag*
  property needs to match the subsequent search term.
  Note that there is no space before or after the
  **:**.
- **vip** is the search term referred to by the prior
  property/operator combination.
- **created** is a keyword indicating you are searching
  the *created* data property for items created
  relative to a certain date.
- **<** is an operator indicating you are searching
  for users, tickets, organizations, or articles
  created before a certain date.
- **2015-05-01** is a search term indicating the date
  you want to use.

If submitting multiple search terms, search has a default AND behavior,
rather than an OR behavior. For example, searching for the following
phrase returns results only if **all** of the words are present,
in any order.

```
Please upgrade my account
```

However, when you use a data property keyword multiple times in a query,
there is an OR search across the values you specified. The following
phrase returns results that contain **either** the tag "silver"
or the tag "bronze".

```
tags:silver tags:bronze
```

To perform an AND search on multiple data property keywords, wrap the
keywords in double quotes. The following phrase returns only results
that contain **both** tags, "superman" and "is\_awesome".

```
tags:"superman is_awesome"
```

## Search operators

The following search operators can be used to build your search
statements.

Table 1. Search operators

| Operator | Description |
| --- | --- |
| : | The colon indicates that the given field should equal the specified value.  ``` status:open ``` |
| < | Less than.  ``` status<closed ``` |
| > | Greater than.  ``` priority>normal ``` |
| <= | Less than or equal to.  ``` status<=pending ``` |
| >= | Greater than or equal to.  ``` priority>=normal ``` |
| " " | Double quotes. In a simple keyword search, this is referred to as a phrase search and returns the exact words in the exact order; however, punctuation characters are not included.  ``` "Please upgrade my account" ```   Note: In the Japanese version of Support, this feature does not work as expected. A simple keyword search that includes double quotes returns results, but the results are not the exact words in the exact order.  In a search including data properties, use double quotes to perform an inclusive AND search, returning results that include *all* properties in the search.  ``` tags:"superman is_awesome" ``` |
| - | Minus sign. Excludes items containing a word (or property value) from the search results. For example, the following statement searches for any tickets with the status 'pending', but excludes any tickets containing the tag 'invoice' from the search results:  ``` status:pending -tags:invoice ``` |
| \* | The wildcard operator is useful when you want to search various forms of a word. For example, searching for `photo*` returns results that would include photography, photographer, photograph and any other words that began with 'photo'. However, because of the performance issues involved with doing wildcard searches, unqualified wildcard searches are not currently supported. In other words, you need to use a property keyword to make your search specific to the data you're trying to locate.  ``` subject:photo* ``` |

## Searching for properties that contain no data

Properties that contain no data can be searched for using
`none` as the search term, along with the
*group*, *tags*, *via*, *organization*,
or *assignee* keywords, as in this
example:

```
assignee:none
```

This returns all unassigned tickets.

## Searching by date and time

Date property keywords - *created*, *updated*, *solved*,
and *due date*) can be combined with search operators to return
data from a specific date, before a certain date, and after a
certain date. To search dates in any locale, use the format
YYYY-MM-DD. You can also use locale-specific formats such as
MM/DD/YYYY in the United States.

To search for data before a certain date, use the less than (**<**)
operator:

```
created<2011-05-01
```

To search for data after a certain date, use the greater than (>)
operator:

```
due_date>2010-01-10
```

To search for a specific date, use the equals (**:**)
operator:

```
solved:2010-01-10
```

You can also use the *<=* or *>=* operators to indicate
*less-than-or-equal-to* and
*greater-than-or-equal-to* respectively.

### Searching with combined dates and times

You can specify a combined date and time using [ISO8601 syntax](https://en.wikipedia.org/wiki/ISO_8601):

```
created>2015-09-01T12:00:00-08:00
updated<2015-09-01T12:00:00Z
```

The first example above searches for anything created after
September 1, 2015 at 12:00 p.m. (Pacific Standard Time).

The second example above searches for anything updated before
September 1, 2015 at 12:00 p.m. (UTC).

### Searching within a date/time range

You can search within a date range, for example August 2, 2014
through August 4, 2014, using the following search
statement:

```
created>2014-08-01 created<2014-08-05
```

You can also include specific times in your search range. The
following example searches for anything created between
August 1, 2014 at 11:59 p.m. (UTC) and August 2, 2014 at
midnight (UTC):

```
created>2014-08-01T11:59:00Z created<2014-08-05T24:00:00Z
```

### Searching with relative times

You can search for a time relative to the present time, using the
time units *hours*, *minutes*, *days*,
*weeks*, *months*, or *years*. The
following search returns anything created in the last four
hours:

```
created>4hours
```

## Searching for tickets with a specific ticket form

You can search for a ticket form and get results for all tickets where
that ticket form is applied. For example, the following search
returns all tickets that use the Change Request ticket form:

```
form:"Change Request"
```

## Sorting search results

You can sort your search results by field, in ascending or descending
order, using the following keyword phrases:

- `order_by:field`
- `sort:asc` or
  `sort:desc`

Sorting is available on the following fields:

- `created`
- `commented`
- `priority`
- `status`
- `ticket_type`

Using the `order_by` and `sort` keywords is
equivalent to using the API parameters `sort_by` and
`sort_order`.

## Using the 'type' keyword

For API searches, one of the tools you have available for narrowing your
search results is the `type` keyword. It is
used to explicitly declare that you want to search for one of the
following types:

- ticket
- user
- organization
- group
- article (Help Center)
- entry or topic (forums)

Using the `type` keyword means that you are explicitly
searching on the type you specify. For example, you can search for
all the users that belong to the customer's organization using this
search statement:

```
type:user organization:customers
```

If you instead searched for `organization:customers` you
would also get all the tickets that have requesters who belong to
this organization. This is because searches that do not explicitly
specify type return results for all types, including tickets (and
organization is a ticket property).

Using `type:user`, your search returns all users that
belong to the Customers organization. So, you're narrowing your
search to the user type and excluding tickets.

While organizations and groups are properties of the user object, they
have their own properties that can be searched as well. The
following query allows you search only for organization tags,
excluding tags of the same name that may be used in other elements
of Zendesk Support such as tickets and forum topics.

```
type:organization tags:premium
```

## Suspended and verified users

You can search for users based on whether or not they are suspended, and
whether or not they are verified. Users with any verified identity,
not just an email address, are included in the search results. For
example, users with verified phone numbers are listed.

To search for suspended users:

```
is_suspended:true
```

To search for verified users:

```
is_verified:true
```

## Search FAQ

- **How soon can new data be searched?**

  When you add
  new data to Zendesk Support, it typically takes
  about a minute before it's indexed and can be
  searched. It can take 10
  to 12 minutes before [live chat and
  messaging conversations](https://support.zendesk.com/hc/en-us/articles/4408846801946) are indexed.
- **How does punctuation affect search?**

  Punctuation
  characters are generally not included in
  searches.
- **Are there limitations to wildcard searches?**

  You
  can only do wildcard searches when combined with
  property keywords
  (`subject:photo*`). The wildcard
  must go at the end of the search term.
- **Who can search what?**

  Administrators can search
  all the data in Zendesk Support. Agents can search
  the data that they've been granted access to.
  End-users can do full text searches of the
  knowledge base.
- **What languages are supported?**

  There is language-specific support for searching
  in the following languages:
  - Brazilian Portuguese
  - Dutch
  - English
  - French
  - German
  - Italian
  - Japanese
  - Russian
  - Spanish

  The support includes dictionary-based
  tokenization for Japanese because words are not
  separated by spaces in that language. For the
  other languages, the language-specific support is
  primarily stemming, which allows different forms
  of the same word to match. In particular, the
  singular and plural forms of a word will generally
  match.