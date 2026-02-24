# Metrics and attributes for Zendesk Knowledge

Source: https://support.zendesk.com/hc/en-us/articles/4409155064090-Metrics-and-attributes-for-Zendesk-Knowledge

---

Use this article to discover the metrics and attributes you can use to build reports based on your usage of Knowledge. These datasets are also used for the prebuilt dashboards (seeOverview of the Zendesk Knowledge dashboard).

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Use this article to discover the metrics and attributes you can use to build reports
based on your usage of Knowledge. These datasets are also used for the prebuilt
dashboards (see [Overview of the Zendesk Knowledge
dashboard](https://support.zendesk.com/hc/en-us/articles/4408823886874)).

This article contains the following topics:

- [Knowledge Capture dataset](#topic_e45_ngh_bfb)
- [Team Publishing dataset (Enterprise only)](#topic_aff_45y_jnb)
- [Knowledge base dataset](#topic_zwt_jht_cnb)
- [Search dataset](#topic_anj_4gj_nrb)
- [Community dataset](#topic_n5d_4dj_ktb)
- [Page efficiency dataset](#topic_cz1_1lw_x2c)
- [User session dataset](#topic_cck_rlw_x2c)
- [Quick answers dataset](#topic_jk2_x3n_13c)

Related articles:

- [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530)

## Knowledge Capture dataset

The Knowledge Capture dataset contains metrics and attributes that relate to
Knowledge in the context panel in Agent Workspace. This section lists all the
available elements for the Knowledge Capture dataset. Use this dataset to help you
understand the efficiency of selecting articles to deflect support tickets.

This section contains the following topics:

- [Knowledge Capture dataset schema](#topic_ag2_swf_kkb)
- [Knowledge Capture metrics](#topic_f45_ngh_bfb)
- [Knowledge Capture attributes](#topic_g45_ngh_bfb)

### Knowledge Capture dataset schema

Use this diagram to help you understand the elements of the Knowledge Capture
dataset and their relationships.

![Knowledge Capture dataset schema](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Knowledge%20Capture.jpg)

### Knowledge Capture metrics

This section lists and defines all metrics available in the Knowledge Capture
dataset.

Table 1. Knowledge Capture metrics

| Metric | Definition | Explore formula |
| --- | --- | --- |
| Knowledge Capture events | Knowledge base article updates made using Knowledge or the Knowledge Capture app. | [Knowledge Capture event ID] |
| Linked articles | Count of the number of articles linked using Knowledge or the Knowledge Capture app in a ticket. | IF ([Knowledge Capture type]="Linked") THEN [Knowledge Capture event ID] ENDIF |
| Flagged articles | Counts the number of articles flagged for update using Knowledge or the Knowledge Capture app in an existing ticket. | IF ([Knowledge Capture type]="Flagged") THEN [Knowledge Capture event ID] ENDIF |
| Created articles | Counts the number of articles created using Knowledge or the Knowledge Capture app in a ticket. | IF ([Knowledge Capture type]="Created") THEN [Knowledge Capture event ID] ENDIF |
| Resolution articles | Count of articles linked through Knowledge or the Knowledge Capture app that were marked as helpful by end users and resolved their request. | IF ([Knowledge Capture type]="Solved") THEN [Knowledge Capture event ID] ENDIF |
| % Resolution rate | The percentage of resolution articles against articles offered to end users via Knowledge or the Knowledge Capture app. | COUNT(Resolution articles)/COUNT(Linked articles) |
| Knowledge Capture tickets | Tickets where any update using Knowledge or the Knowledge Capture app took place. | [Knowledge Capture ticket ID] |
| Linked article tickets | Counts tickets where a knowledge base article was linked using Knowledge or the Knowledge Capture app. | IF ([Knowledge Capture type]="Linked") THEN [Knowledge Capture ticket ID] ENDIF |
| Flagged article tickets | Counts tickets where a knowledge base article was flagged for update using Knowledge or the Knowledge Capture app. | IF ([Knowledge Capture type]="Flagged") THEN [Knowledge Capture ticket ID] ENDIF |
| Created article tickets | Counts the number of tickets where an article was created using Knowledge or the Knowledge Capture app. | IF ([Knowledge Capture type]="Created") THEN [Knowledge Capture ticket ID] ENDIF |
| Resolution article tickets | Count of tickets that were resolved by end users through articles linked via Knowledge or the Knowledge Capture app. | IF ([Knowledge Capture type]="Solved") THEN [Knowledge Capture ticket ID] ENDIF |
| % Agent engagement rate | The percentage of total tickets on which Knowledge or the Knowledge Capture app was used. | D\_COUNT(Knowledge Capture tickets)/DCOUNT\_VALUES([Ticket ID]) |
| % Article linking rate | The percentage of tickets where an article was linked using Knowledge or the Knowledge Capture app. | D\_COUNT(Linked article tickets)/DCOUNT\_VALUES([Ticket ID]) |
| % Ticket resolution rate | The percentage of tickets that were resolved by end users against tickets on which articles were linked via Knowledge or the Knowledge Capture app. | D\_COUNT(Resolution article tickets)/D\_COUNT(Linked article tickets) |
| Linked articles - Ticket average | The average number of articles linked using Knowledge or the Knowledge Capture app to all tickets where a Knowledge or Knowledge Capture event took place. | D\_COUNT(Linked article tickets)/DCOUNT\_VALUES([Ticket ID]) |
| Agent replies | The number of public replies added to a ticket by an agent. | VALUE(Agent replies) |
| Assignee stations | The number of agents a ticket has been assigned to. | VALUE(Assignee stations) |
| Group stations | The number of groups a ticket has been assigned to. | VALUE(Group stations) |
| Reopens | The number of times a ticket was reopened. | VALUE(Reopens) |

### Knowledge Capture attributes

This section lists and defines all attributes available in the Knowledge Capture
dataset.

Table 2. Knowledge Capture attributes

| Attribute | Definition |
| --- | --- |
| Knowledge Capture type | The type of event performed by Knowledge or the Knowledge Capture app. Possible values are **Created**, **Flagged**, and **Linked**. |
| Knowledge Capture ticket ID | The ID of the ticket that was updated using Knowledge or the Knowledge Capture app. |
| Knowledge Capture event ID | The ID of the knowledge base article that was updated using Knowledge or the Knowledge Capture app. |
| Knowledge Capture brand | The brand of the knowledge base where Knowledge or the Knowledge Capture app was used. |
| Knowledge Capture language | The language of the knowledge base where Knowledge or the Knowledge Capture app was used. |
| Knowledge Capture locale | The locale of the knowledge base where Knowledge or the Knowledge Capture app was used. |
| Ticket ID | The ID number of the ticket. |
| Ticket status | The current status of the ticket. |
| Ticket group | The name of the group where the ticket was assigned. |
| Ticket assignee | The name of the user to who the ticket is assigned. |
| Ticket brand | The brand of the ticket. |
| Ticket channel | The channel a ticket was created from. For more information about the ticket channels Explore collects, see [Understanding ticket channels in Explore](https://support.zendesk.com/hc/en-us/articles/4408836378394). |
| Ticket form | Ticket form used on the ticket. |
| Ticket organization | The name of the organization associated with the ticket. |
| Ticket priority | The ticket's priority. |
| Ticket problem ID | The ID of the associated problem ticket. |
| Ticket requester | The name of the user that requested the ticket. |
| Ticket satisfaction rating | The satisfaction rating given to the ticket. |
| Ticket support type | Identifies whether tickets were resolved by an AI agent or a human agent. Possible values are Agent and AI agent. |
| Ticket subject | The subject of ticket. |
| Ticket tags | The tags associated with a ticket. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket type | The ticket type: Question, Incident, Problem, or Task. |
| Sharing agreement inbound | Affiliated instances of Zendesk Support and companies who share tickets with the current instance of Zendesk Support. |
| Sharing agreement outbound | Affiliated Zendesk accounts and companies tickets are shared with. |
| Article ID | The ID of the knowledge base article. |
| Article ID and locale | The ID and locale of the knowledge base article. |
| Article translation title | The title of the knowledge base article |
| Article translation URL | The URL of the knowledge base article. |
| Article author | The name of the user who originally created a knowledge base article. |
| User name | The name of the user associated with the article. |
| User role | The role of the user associated with the article. |
| User ID | The ID of the user associated with the article. |
| User email | The email address of the user associated with the article. |
| User locale | The locale of the user associated with the article. |
| User status | The Zendesk status of the user associated with the article. |
| User tags | A list of tags associated with the user for the article. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| User time zone | The time zone of the user associated with the article. |
| Intent (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what the ticket is about. To see the possible values, [open the Taxonomy tab of the Intent settings page](https://support.zendesk.com/hc/en-us/articles/9488234915610) to see the AI Intents list under the **Taxonomy values** heading. |
| Intent confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the intent prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Language (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of what language the ticket is written in. To see the possible values, open the Taxonomy tab of the settings page. |
| Language confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the language prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Sentiment (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | A prediction of how the customer feels about their request. Possible values are **Very Positive**, **Positive**, **Neutral**, **Negative**, and **Very Negative**. |
| Sentiment confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538)) | The likelihood that the sentiment prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Time – Knowledge capture event | Includes several attributes that return the time and date when an update using Knowledge or the Knowledge Capture app was registered. |
| Time – Ticket created | Includes several attributes that return the time and date when tickets were created. |
| Time – Ticket solved | Includes several attributes that return the time and date when tickets were solved. |
| Time – Ticket last updated | Includes several attributes that return the time and date when tickets were last updated. |
| Time – Article created | Includes several attributes that return the time when an article was created. |
| Time – Article last updated | Includes several attributes that return the time when an article was last updated. |
| Ticket Status – Unsorted | The status of the ticket. |
| Ticket Priority – Unsorted | The ticket’s priority. |
| Ticket Type - Unsorted | The ticket type. |

## Team Publishing dataset (Enterprise only)

The Team Publishing dataset contains metrics and attributes that relate to knowledge
activity. This section lists all the available elements for the Team Publishing
dataset. Use this dataset to help you understand the efficiency of your knowledge
management workflows.

This section contains the following topics:

- [Team Publishing metrics](#topic_apk_q5y_jnb)
- [Team Publishing attributes](#topic_v4r_q5y_jnb)

### Team Publishing metrics

This section lists and defines all metrics available in the Team Publishing
dataset.

Table 3. Team Publishing metrics

| Metric | Definition | Explore formula |
| --- | --- | --- |
| Articles created | The number of articles that have been created. | IF [Publishing event type - Unsorted]="Article created" THEN [Event ID] ENDIF |
| Articles published | The number of articles that have been published. | IF [Publishing event type - Unsorted]="Translation published" THEN [Event article ID] ENDIF |
| Articles verified | The number of articles that have been verified to ensure they are up to date. | IF [Publishing event type - Unsorted]="Article verified" THEN [Event article ID] ENDIF |
| Articles unverified | The number of articles that have come up for verification. | IF [Publishing event type - Unsorted]="Article unverified" THEN [Event article ID] ENDIF |
| Articles archived | The number of articles that have been archived. | IF [Publishing event type - Unsorted]="Article archived" THEN [Event article ID] ENDIF |
| Articles deleted | The number of articles that have been deleted. | IF [Publishing event type - Unsorted]="Article deleted" THEN [Event article ID] ENDIF |
| Articles restored | The number of articles that have been restored from archive. | IF [Publishing event type - Unsorted]="Article restored" THEN [Event article ID] ENDIF |
| Articles edited | The number of articles that have been edited. | IF [Publishing event type - Unsorted]="Article edited" THEN [Event article ID] ENDIF |
| Translations created | The number of article translations that have been created. An article can contain multiple translations, for example, English, French, or Japanese. | IF [Publishing event type - Unsorted]="Translation created" THEN [Event ID] ENDIF |
| Translations published | The number of article translations that have been published. | IF [Publishing event type - Unsorted]="Translation published" THEN [Event article ID] ENDIF |
| Translations unpublished | The number of article translations that have been unpublished. | IF [Publishing event type - Unsorted]="Translation unpublished" THEN [Event article ID] ENDIF |
| Translations edited | The number of article translations that have been edited. | IF [Publishing event type - Unsorted]="Translation edited" THEN [Event article translation ID] ENDIF |
| Translations assigned | The number of times that article translations have been assigned to somebody. | IF [Publishing event type - Unsorted]="Translation assigned" THEN [Event article translation ID] ENDIF |
| Translations submitted for review | The number of article translations submitted for review. | IF [Publishing event type - Unsorted]="Translation submitted for review" THEN [Event article translation ID] ENDIF |
| Translations approved for publishing | The number of article translations approved for publishing. | IF [Publishing event type - Unsorted]="Translation approved for publishing" THEN [Event article translation ID] ENDIF |
| Translations deleted | The number of article translations that have been deleted. | IF [Publishing event type - Unsorted]="Translation deleted" THEN [Event ID] ENDIF |
| Events | The total number of all publishing events like article creation, archiving, restoration, and deletion. | [Publishing event type - Unsorted] |
| Translation updates | The number of edits that have been made to article translations. | IF [Publishing event type - Unsorted]="Translation edited" THEN [Event ID] ENDIF |
| Translation assignments | The number of times that article translations have been assigned to somebody. | IF [Publishing event type - Unsorted]="Translation assigned" THEN [Event ID] ENDIF |
| Translation review submissions | The number of article translations submitted for review. | IF [Publishing event type - Unsorted]="Translation submitted for review" THEN [Event ID] ENDIF |
| Translation publishing approvals | The number of article translations approved for publishing. | IF [Publishing event type - Unsorted]="Translation approved for publishing" THEN [Event ID] ENDIF |
| Translation publishing events | The total number of all publishing events like article creation, archiving, restoration, and deletion. | IF [Publishing event type - Unsorted]="Translation published" THEN [Event ID] ENDIF |
| Translation unpublishing events | The number of article translations that have been unpublished. | IF [Publishing event type - Unsorted]="Translation unpublished" THEN [Event ID] ENDIF |
| Article verifications | The number of articles that have been verified to ensure they are up to date. | IF [Publishing event type - Unsorted]="Article verified" THEN [Event ID] ENDIF |
| Article archiving events | The number of articles that have been archived. | IF [Publishing event type - Unsorted]="Archived" THEN [Event ID] ENDIF |
| Article deletions | The number of articles that have been deleted. | IF [Publishing event type - Unsorted]="Article deleted" THEN [Event ID] ENDIF |
| Article restorations | The number of articles that have been restored from archive. | IF [Publishing event type - Unsorted]="Article restored" THEN [Event ID] ENDIF |

### Team Publishing attributes

This section lists and defines all attributes available in the Team Publishing
dataset.

Note: When an agent [schedules an article for
publication](https://support.zendesk.com/hc/en-us/articles/4408820403226), the publish event in Explore is attributed to a
system user, not the agent who scheduled the event. The agent details (such
as name and ID) appear as null values because that's how system users are
represented in Explore.

Table 4. Team Publishing attributes

| Attribute | Definition |
| --- | --- |
| Event article ID | The ID of the article that recorded a Team Publishing event. |
| Event article brand | The [brand](https://support.zendesk.com/hc/en-us/articles/4408824139546) of the article that recorded a Team Publishing event. |
| Event article language | The language of the article that recorded a Team Publishing event. |
| Event article locale | The locale of the article that recorded a Team Publishing event, for example, **French**. |
| Event article translation ID | The ID of the article that recorded a Team publishing event with the locale appended, for example, **12345678\_fr**. |
| Article translation title | The title of the article that recorded a Team Publishing event. This attribute also returns translated versions of the title. |
| Article translation URL | The URL of the article that recorded a Team Publishing event. This attribute also returns URLs for any translated versions of the article. |
| Event ID | A unique ID number for each Team Publishing event. |
| Event type | The type of Team Publishing event, for example, **Article archived** or **Translation published**. |
| Agent name | The name of the agent who performed the Team Publishing event. |
| Agent role | The role of the agent who performed the Team Publishing event, for example, **Agent**, |
| Agent ID | The ID of the agent who performed the Team Publishing event. |
| Agent email | The email address of the agent who performed the Team Publishing event. |
| Agent locale | The locale of the agent who performed the Team Publishing event. |
| Agent status | The status of the agent who performed the Team Publishing event, for example, **Active**. |
| Agent tags | Displays tags associated with the agent who performed the Team Publishing event. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Agent time zone | The time zone of the agent who performed the Team Publishing event. |
| Article event update time | A collection of attributes that return when a Team Publishing event occurred in different time and date formats. |

## Knowledge base dataset

This section contains the following topics:

- [Knowledge Base metrics](#topic_bxt_jht_cnb)
- [Knowledge Base attributes](#topic_dxt_jht_cnb)

### Knowledge Base metrics

This section lists and defines all metrics available in the Knowledge Base
dataset. These metrics are event-driven, meaning that the data represents the
last time an event took place. They do not indicate current values. For example,
the article comments metric only updates when a comment is added.

Table 5. Knowledge Base metrics

| Metric | Definition | Explore formula |
| --- | --- | --- |
| Published articles | The total number of articles in your knowledge base excluding any translated articles. If the section or category containing an article is in draft mode, any articles they contain are not included in the knowledge base reports. | DCOUNT\_VALUES([Article ID]) |
| Published translations | The total number of articles in your knowledge base including translated articles. If the section or category containing an article is in draft mode, any articles they contain are not included in the knowledge base reports. | [Article ID]+[Article locale] |
| Articles viewed | The number of articles that have been viewed at least once. Each article is counted only once, even if it is viewed multiple times. | IF(VALUE(Article views)>0) THEN [Engagement ID]+[Engagement locale] ENDIF |
| Article views | The number of views for each of your articles. All article views are recorded, no matter how many times a user has viewed the article in the selected period of time. The default aggregator for this metric is average views (AVG) aggregated each hour, but you can change it to SUM, MIN, or MAX. Note: Ad blockers might prevent Explore from recording article views. | AVG(Article views) |
| Article comments | The number of comments on articles. Data is available from February 25, 2023 onwards. | [Article comments] |
| Article subscriptions | The number of subscriptions to articles. Data is available from February 25, 2023 onwards. | [Article subscriptions] |
| Article upvotes | The number of upvotes on articles. Data is available from February 25, 2023 onwards. | [Article upvotes] |
| Article downvotes | The number of downvotes on articles. Data is available from February 25, 2023 onwards. | [Article downvotes] |
| Article votes | The total number of votes on articles (upvotes plus downvotes). Data is available from February 25, 2023 onwards. | [Article upvotes]+[Article downvotes] |
| Net article votes | The net number of votes on articles (upvotes minus downvotes). Data is available from February 25, 2023 onwards. | [Article upvotes]-[Article downvotes] |
| Net article votes - all time | The current state of the votes on an article. This metric is an all-time total that is not affected by time-based filters. For a metric that is affected by time-based filters, use **Net article votes** instead. |  |

### Knowledge Base attributes

This section lists and defines all attributes available in the Knowledge Base
dataset. These attributes are event-driven, meaning that the data represents the
last time an event took place. They do not indicate current values.

Table 6. Knowledge Base attributes

| Attribute | Definition |
| --- | --- |
| Engagement ID | A unique ID number for the article engagement (view, comment, subscription, or vote). This is the same as the article ID. |
| Engagement brand | The Zendesk brand from which the engagement came. Brands are a customer-facing identity, represented by one or more help centers, Web Widgets, Talk, X (formerly Twitter), or Facebook accounts. |
| Engagement channel | The Zendesk channel from where the article visitor came, for example, help center, Mobile SDK, or Web Widget. |
| Engagement language | The Zendesk language of the article visitor. |
| Engagement locale | The Zendesk locale setting of the article visitor. |
| Engagement user role | The user role and sign-in status of the article visitor, for example End-user (signed in), Staff member (signed in), or Anonymous. |
| Views user role - ungrouped | Internal system user role data. Typically you'll use the **Engagement user role** attribute instead. |
| Article ID | Each article has a unique ID which you can see in the article URL. This attribute returns each ID. The article ID is the same for each translated version of an article. |
| Author name | The name of the article author. |
| Article brand | Brands are a customer-facing identity, represented by one or more help centers or Web Widget, Talk, X (formerly Twitter), or Facebook accounts. |
| Article translation language | The language of each article. |
| Article locale | The locale of each article, for example, en-us. |
| Article section ID | The ID of the section containing the article. Sections without any articles are not included (for example, sections that consist of subsections only). Event data (such as views or comments) is returned for an article's current section only. |
| Article section title | The section name for each article. Sections without any articles are not included (for example, sections that consist of subsections only). Event data (such as views or comments) is returned for an article's current section only. |
| Article title | The title of each article. |
| Article category title | The name of the category containing the article. Data is available only for articles published (or republished) after February 25, 2023. |
| Article URL | The URL of each article. |
| Time - Article engagement recorded | Includes several attributes that return the time when each article was engaged with. |
| Time - Article created | Includes several attributes that return the time when each article was created. |

## Search dataset

The Search dataset contains metrics and attributes that relate to the
searches that users performed and the terms they searched for in your knowledge
base. This section lists all the available elements for the dataset.

Note: The data in this dataset is retained for a maximum of
390 days in the past.

This section contains the following topics:

- [Search dataset schema](#topic_anj_4gj_nrb__section_xrw_pgj_nrb)
- [Search metrics](#topic_anj_4gj_nrb__section_zrw_pgj_nrb)
- [Search attributes](#topic_anj_4gj_nrb__section_bsw_pgj_nrb)

### Search dataset schema

Use this diagram to help you understand the elements of the Search
dataset and their relationships.

![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_search_dataset_schema.png)

### Search metrics

This section lists and defines all of the Search metrics available.

Table 7. Search metrics

|  |  |  |
| --- | --- | --- |
| **Metric** | **Definition** | **Calculation** |
| Searches | The total number of searches performed. | IF ([Event type] = "Search") THEN [Search query] ELSE NULL ENDIF |
| Clicks | The number of searches where the user selected a result. | IF ([Event type] = "Click") THEN [Search query] ELSE NULL ENDIF |
| Tickets created | The total number of tickets created in the help center. | IF ([Event type] = "Ticket") THEN [Search query] ELSE NULL ENDIF |
| Avg click-through rate | The number of clicks relative to the number of searches. | COUNT(Clicks)/COUNT(Searches) |
| Searches with no results | The number of searches that returned zero results. | IF ([Event type] = "Search" AND VALUE(Search results count) = 0) THEN [Search query] ENDIF |
| Percentage of searches with no result | The number of searches that returned zero results divided by the number of searches performed. | COUNT(Searches with no results)/COUNT(Searches) |
| Searches with no clicks | The number of searches where the user didn’t select a result. | IF MAX(Clicks by query)=0 THEN COUNT(Searches) ELSE 0 ENDIF |
| Clicks by query | The number of clicks per search query. | ATTRIBUTE\_ADD(COUNT(Clicks), [Search query]) |
| Search results count | The number of results that were returned for the search query. | IF [Event type] = "Search" THEN VALUE(All event results count) ELSE 0 ENDIF |
| All event results count | The number of times an event (click, search, or ticket creation) occurred. | SUM(All event results count) |
| Avg number of results | The average number of results that were returned for the search query. | [Search results count]/COUNT(Searches) |
| Tickets created / Search ratio | The number of tickets divided by the number of searches. | COUNT(Tickets created)/COUNT(Searches) |

### Search attributes

This section lists and defines all the Search attributes available.

Table 8. Search attributes

|  |  |
| --- | --- |
| **Attribute** | **Definition** |
| Article ID | The ID of the knowledge base article. |
| Article title | The title of the article. |
| Article locale | The locale of the article (for example, en-us). |
| Event type | The type of search event. Valid values are Search event, Click event or Ticket submitted event. |
| Search query | The query string that was searched for by a user. |
| Search channel | The channel where the search was performed. |
| Search click type | If the event is a click event, the search result clicked could be either an article or community post. |
| Search locale | The locale of the search. |
| Search brand ID | The brand ID of the help center that the search was performed on. |
| Search brand name | The brand name of the help center that the search was performed on. |
| Search user role | The role of the user that performed the search event. The values are: Anonymous, End user (signed in), Staff member (signed in). |
| Search user role - ungrouped | Internal system user role data. Typically you'll use the **Search user role** attribute instead of this. |
| Search language | The language of the search query. |
| Search outcome | The outcome of a search. The values are true if the search generated no results, false if it has at least one result. |
| Search timestamp | Includes several attributes that return the time and date when a search occurred. |

## Community dataset

The Community dataset contains metrics and attributes that relate to your Zendesk
community activity. This section lists all the available elements for the dataset.

Note: Data in this dataset is available from February 9, 2022
onwards.

This section contains the following topics:

- [Community metrics](#topic_emc_qdj_ktb)
- [Community attributes](#topic_b5q_rdj_ktb)

### Community metrics

This section lists and defines all of the available community metrics.

Table 9. Community metrics

|  |  |  |
| --- | --- | --- |
| **Metric** | **Definition** | **Calculation** |
| Community events | The total actions taken on a community forum, including created posts, viewed posts, added votes, created comments, added subscriptions, and submitted tickets. | [guide\_community\_engagement\_community\_post\_id] |
| Existing community posts | The number of existing posts in the community. | [guide\_community\_posts\_community\_post\_id] |
| Posts created | The total number of posts created in the selected time period. | IF ([guide\_community\_engagement\_event\_type] = "Post created") THEN [guide\_community\_engagement\_community\_post\_id] ENDIF |
| Post views | The total number of post views on the community forum. | IF ([guide\_community\_engagement\_event\_type] = "Post viewed") THEN [guide\_community\_engagement\_community\_post\_id]  ENDIF |
| Post votes | The total number of votes—either up or down—on a community post. | IF ([guide\_community\_engagement\_event\_type] = "Vote added") THEN [guide\_community\_engagement\_community\_post\_id]  ENDIF |
| Post upvotes | The total number of upvotes on a post. | IF ([guide\_community\_engagement\_event\_type] = "Vote added" AND [guide\_community\_engagement\_vote\_direction]  = "Up") THEN [guide\_community\_engagement\_community\_post\_id] ENDIF |
| Post downvotes | The total number of downvotes on a post. | IF ([guide\_community\_engagement\_event\_type] = "Vote added" AND [guide\_community\_engagement\_vote\_direction]  = "Down") THEN [guide\_community\_engagement\_community\_post\_id] ENDIF |
| Comments | The total number of comments made on the community forum. | IF ([guide\_community\_engagement\_event\_type] = "Comment created") THEN  [guide\_community\_engagement\_community\_post\_id] ENDIF |
| Post subscriptions | The total number of subscriptions to posts on the community forum. | IF ([guide\_community\_engagement\_event\_type] = "Subscription added")  THEN [guide\_community\_engagement\_community\_post\_id] ENDIF |
| Post creation timestamps | The exact time when a community post was created. | IF ([guide\_community\_engagement\_event\_type] = "Post created") THEN  DATE\_TO\_TIMESTAMP([timeDimension##guide\_community\_engagement\_timestamp##date])  ENDIF |
| Post creation timestamp by community post | The exact time when each community post was created. | ATTRIBUTE\_FIX(MIN(guide\_community\_post\_creation\_timestamps), [guide\_community\_engagement\_community\_post\_id]) |
| Staff response timestamps | The exact time when a staff member commented on a community post. | IF ([guide\_community\_engagement\_event\_type] = "Comment created" AND  [guide\_community\_engagement\_grouped\_user\_role] = "Staff member (signed in)")  THEN DATE\_TO\_TIMESTAMP([timeDimension##guide\_community\_engagement\_timestamp##date])  ENDIF |
| Staff response timestamp by community post | The exact time when a staff member commented on each community post. | ATTRIBUTE\_FIX(MIN(guide\_community\_staff\_response\_timestamps), [guide\_community\_engagement\_community\_post\_id]) |
| Response timestamps | The exact time when a community member responded to a post. | IF ([guide\_community\_engagement\_event\_type] = "Comment created") THEN  DATE\_TO\_TIMESTAMP([timeDimension##guide\_community\_engagement\_timestamp##date])  ENDIF |
| First response timestamp by community post | The exact time when a community member responded to each post. | ATTRIBUTE\_FIX(MIN(guide\_community\_response\_timestamps), [guide\_community\_engagement\_community\_post\_id]) |
| Time to staff response (hours) | The time in hours between when a post was created and when the first staff member responded. | (MIN(guide\_community\_staff\_response\_timestamp) - MIN(guide\_community\_post\_creation\_timestamp))  / 3600 |
| Time to first response (hours) | The time in hours between when a post was created and when the first comment was made. | (MIN(guide\_community\_response\_timestamp) - MIN(guide\_community\_post\_creation\_timestamp))  / 3600 |
| Number of posts without any comments | The total number of community posts that don't have a response from any user. | IF ([Community engagement event type] = "Post created") THEN 1 ELIF ([First reply time] != NULL AND VALUE(Post creation timestamp by community post) != NULL) THEN -1 ELSE 0 ENDIF |
| Number of posts without staff comments | The total number of community posts that don’t have a staff member response. | IF ([guide\_community\_engagement\_event\_type] = "Post created") THEN  1 ELIF ([guide\_community\_engagement\_first\_staff\_response] != NULL AND VALUE(guide\_community\_post\_creation\_timestamp)  != NULL) THEN -1 ELSE 0 ENDIF |
| Number of days without comments | The total number of days since the last comment was made on the community forum. | IF ([guide\_community\_engagement\_response\_time\_bracket] = "No comments")  THEN DATE\_DIFF(DATE\_LAST\_FIX([timeDimension##guide\_community\_engagement\_timestamp##date]),  [timeDimension##guide\_community\_posts\_created\_at##date], "nb\_of\_days") ENDIF |
| Submitted tickets | The total number of tickets created in the help center. | IF ([guide\_community\_engagement\_event\_type] = "Ticket submitted") THEN  [guide\_community\_engagement\_event\_type] ENDIF |

### Community attributes

This section lists and defines all of the available community attributes.

Table 10. Community attributes

|  |  |
| --- | --- |
| **Attribute** | **Definition** |
| Community user email | The email address of the community member. |
| Community user ID | The unique ID of the community member. |
| Community user name | The name of the community member. |
| Community user created at | Includes several attributes that return the time and date when a community user was created. |
| Author ID | The unique ID of the community member who created a post. |
| Author name | The name of the community member who created a post. |
| Community post ID of existing posts | The unique ID of a community post. |
| Community post title | The title of a community post. |
| Community topic ID | The unique ID of the topic that a post or comment is part of. |
| Community topic title | The title of the topic that a post or comment is part of. |
| Brand ID | The unique ID of the brand associated with the community forum. |
| Brand name | The name of the brand associated with the community forum. |
| Channel | The channel from which a user viewed a post. Possible values are **HC** (help center), **Agent workspace**, and **API**.  For more information about the ticket channels Explore collects, see [Understanding ticket channels in Explore](https://support.zendesk.com/hc/en-us/articles/4408836378394). |
| Community post ID | The unique ID of a community post. |
| Community engagement event type | The type of action taken on a community forum. Possible values are **Post created**, **Post viewed**, **Vote added**, **Comment created**, **Subscription added**, and **Ticket submitted**. |
| User role | The role of the community member. Possible values are **End user**, **Anonymous**, **Agent**, **Admin**, and **Viewer**. |
| Vote direction | Whether a vote was an upvote or a downvote. |
| First reply time | The time between when a post was created and the first comment made by any community member. |
| First staff reply time | The time between when a post was created and the first comment made by an agent. |
| First staff reply time bracket | The time between when a post was created and the first comment made by an agent. Values are returned as **<8 hours**, **8-24 hours**, **1-7 days**, **8-14 days**, and **>14 days**. |
| First reply time bracket | The time between when a post was created and the first comment made by any community member. Values are returned as **<8 hours**, **8-24 hours**, **1-7 days**, **8-14 days**, and **>14 days**. |
| Community engagement user ID | The unique ID of the community member. |
| Grouped user role | The role of the community member. Possible values are **End user**, **Staff member**, and **Anonymous**. |
| Community engagement timestamp | Includes several attributes that return the time and date when a community engagement event (such as a vote) occurred. |
| Community post created at | Includes several attributes that return the time and date when a community post was created. |

## Page efficiency dataset

The Page efficiency dataset helps you examine help center page analytics to pinpoint
self-service content that effectively provides answers, as well as content that may
need enhancement. This section lists all the available elements for the dataset.
Self-service data is available from January 15, 2025 onwards.

Important: As of April 4, 2025, the self-service datasets have been
filtered to only events that originate from the help center. Before this date,
some events from other sources, such as the Agent Workspace including page views
(articles and community posts), searches, and quick answers might appear in
reports. All ticket deflection reports, such as confirmed and assumed
deflections, only track tickets submitted using the help center request form.

Depending on your usage of other channels, the inclusion of these
additional events will have some impact on session duration, page view
duration, and number of sessions and visitors.

This section contains the following topics:

- [Page efficiency metrics](#topic_fz1_1lw_x2c)
- [Page efficiency attributes](#topic_hz1_1lw_x2c)

### Page efficiency metrics

This section lists and defines all of the available page efficiency metrics.

Table 11. Page efficiency metrics

|  |  |  |
| --- | --- | --- |
| **Metric** | **Definition** | **Calculation** |
| Confirmed deflections | The number of confirmed deflections attributed to the page. A confirmed deflection is registered as a help center session when a user selected an article from the suggested articles on the request form and did not submit a ticket during their session. | VALUE(Confirmed deflections) |
| Assumed deflections | The number of assumed deflections attributed to the page. An assumed deflection happens when a user visits the help center and doesn’t ask for help or submit a ticket, but also didn’t confirm they found an answer. It’s assumed they found what they needed on their own. | VALUE(Assumed deflections) |
| Page exits | The number of times the page was viewed as the last event in a session. | VALUE(Page exits) |
| Tickets submitted after view | The number of tickets submitted. When comparing this metric to page views, each page a user views before submitting a ticket is counted. This helps you find articles where users couldn’t get the answers they needed. | VALUE(Tickets submitted after view) |
| Page views | The number of times a user has viewed an article or a community post. | VALUE(Page views) |
| Average time on page (sec) | The time between a page view event and the next recorded event in seconds. | VALUE(Average time on page (sec)) |
| Average time on page (min) | The time between a page view event and the next recorded event in minutes. | VALUE(Average time on page (sec))/60 |

### Page efficiency attributes

This section lists and defines all of the available page efficiency
attributes.

Table 12. Page efficiency attributes

|  |  |
| --- | --- |
| **Attribute** | **Definition** |
| Page type | Identifies whether the page is an article or a community post. |
| Page brand | The name of the brand of the help center where the page resides. |
| Page title | The title of the article or community post. |
| Page ID | The page ID consists of the article ID or the community post ID of the help center content which your users have interacted with. This enables you to report on both article and community post views without having to use filters. |
| Page language | The language of the article being viewed. This offers the ability to see which article translation is providing the most assistance in a help center. |
| Page locale | The locale of the article being viewed, for example, en-us. |
| Page visitor role | The user role of users who have viewed the help center page. For example:  - Anonymous - End user - Viewer - Agent - Admin |
| Page author name | The name of the author of the community post or the help center article. |
| Page author ID | The user ID of the author of a page. |
| Article category | The name of the top-level category where the article resides in the help center's hierarchy. |
| Article section | The name of the section where the article resides in the help center's hierarchy. |
| Article title | The title of the article. |
| Article ID | The ID of the article with which a user has interacted. In instances where a user has interacted with a community post and not an article, this value is expected to be NULL. |
| Article author name | The name of the article author. |
| Article author ID | The Zendesk ID of the article author. |
| Community topic | The name of the topic where the community post resides in the community hierarchy. |
| Community post title | The title of the community post. |
| Community post ID | The ID of the community post with which a user has interacted. In instances where a user has interacted with an article and not a community post, this value is expected to be NULL. |
| Community post author name | The name of the community post author. |
| Community post author ID | The Zendesk ID of the community post author. |
| Activity recorded | The timeframe in which the page activities such as deflections and tickets submitted were performed. The page analytics are aggregated on an hourly basis, so the most granular timestamp will correlate to the hour for which the data was aggregated. |

## User session dataset

The user session dataset helps you see user session outcomes for specific users and
identify trends across different roles. This section lists all the available
elements for the dataset. Self-service data is available from January 15, 2025
onwards.

Important: As of April 4, 2025, the self-service datasets have been
filtered to only events that originate from the help center. Before this date,
some events from other sources, such as the Agent Workspace including page views
(articles and community posts), searches, and quick answers might appear in
reports. All ticket deflection reports, such as confirmed and assumed
deflections, only track tickets submitted using the help center request form.

Depending on your usage of other channels, the inclusion of these
additional events will have some impact on session duration, page view
duration, and number of sessions and visitors.

This section contains the following topics:

- [User session metrics](#topic_gck_rlw_x2c)
- [User session attributes](#topic_ick_rlw_x2c)

### User session metrics

This section lists and defines all of the available user session metrics.

Table 13. User session metrics

|  |  |  |
| --- | --- | --- |
| **Metric** | **Definition** | **Calculation** |
| Sessions | The count of user sessions where the user has interacted with the help center. | [Session ID] |
| Sessions per visitor | The ratio of sessions to unique visitors. | COUNT(Sessions)/D\_COUNT(Visitors) |
| Self-service ratio | The ratio of tickets to help center sessions. | COUNT(Sessions)/SUM(Tickets submitted) |
| Bounce rate | The percent of sessions where the user did not view a page (article or community post). This means the session either resulted in a search with no deeper exploration of the provided content or the user submits a ticket without interacting with the knowledge base. | COUNT(guide\_user\_sessions\_without\_page\_view)/COUNT(Sessions) |
| Confirmed deflections | The number of confirmed deflections attributed to the page. A confirmed deflection is registered as a help center session when a user selected an article from the suggested articles on the request form and did not submit a ticket during their session. | IF ([guide\_user\_sessions\_deflection] = 3) THEN [Session ID] ELSE NULL ENDIF |
| Assumed deflections | The number of assumed deflections attributed to the page. An assumed deflection happens when a user visits the help center and doesn’t ask for help or submit a ticket, but also didn’t confirm they found an answer. It’s assumed they found what they needed on their own. | IF ([guide\_user\_sessions\_deflection] = 2) THEN [Session ID] ELSE NULL ENDIF |
| Assumed deflections after page view | The number of sessions where it was assumed an article or community post was successful in deflecting a customer because it was the last page viewed in the session. | IF ([guide\_user\_sessions\_deflection] = 2 AND [guide\_user\_sessions\_last\_activity\_type] = 1) THEN [Session ID] ELSE NULL ENDIF |
| Ticket submitted sessions | The number of sessions where a user submitted at least one ticket. | IF (VALUE(Tickets submitted) > 0) THEN [Session ID] ELSE NULL ENDIF |
| Search used sessions | Number of sessions in which at least one search was performed. | IF (VALUE(Searches) > 0) THEN [Session ID] ELSE NULL ENDIF |
| Standard search sessions | Number of user sessions with at least one search performed, but no generative search results are displayed for any of their searches. Accounts without quick answers will only see standard searches. | IF (VALUE(Searches with quick answer) = 0 AND VALUE(Total searches) > 0) THEN TRUE ELSE NULL ENDIF |
| No search sessions | Number of user sessions with no standard or generative search performed. | IF (VALUE(Total searches) = 0) THEN TRUE ELSE NULL ENDIF |
| No page view sessions | Number of sessions where no pages were viewed. | IF (VALUE(Article views) = 0 AND VALUE(Community post views) = 0) THEN [Session ID] ELSE NULL ENDIF |
| Quick answer sessions | Number of sessions where at least one generative search result was displayed. Relies on the customer activating the applicable AI features. | IF (VALUE(Searches with quick answer) > 0) THEN TRUE ELSE NULL ENDIF |
| Search exits | The number of sessions where the search page was the last page viewed by the user. | IF ([guide\_user\_sessions\_last\_activity\_type] = 2 OR [guide\_user\_sessions\_last\_activity\_type] = 5) THEN [Session ID] ELSE NULL ENDIF |
| Quick answer exits | The number of sessions where a quick answer being presented is the last event, potentially meaning the user found the information they needed in the AI-generated answer. | IF ([guide\_user\_sessions\_last\_activity\_type] = 5) THEN [Session ID] ELSE NULL ENDIF |
| Page views | Count of total page views (article and community posts combined). | VALUE(Article views) + VALUE(Community post views) |
| Page views per session | Average number of page views across sessions. | SUM(Page views) / COUNT(Sessions) |
| Page exits | The number of sessions where an article or community post view was the last event in the user session. | IF ([guide\_user\_sessions\_last\_activity\_type] = 1) THEN [Session ID] ELSE NULL ENDIF |
| Article views | Count of total article views. | VALUE(Article views) |
| Community post views | Count of total community post views. | VALUE(Community post views) |
| Tickets submitted | The total number of tickets submitted. | VALUE(Tickets submitted) |
| Searches per session | The number of searches per user session, filtered for sessions with at least one search. | SUM(Total searches) / COUNT(guide\_user\_sessions\_with\_at\_least\_one\_search) |
| Standard searches | Number of user sessions with at least one search performed, but no quick answers are displayed for any of their searches. Accounts without quick answers will only see standard searches. | VALUE(Total searches) - VALUE(Searches with quick answer) |
| Quick answer searches | The number of search events with a quick answer presented. Number of sessions where at least one quick answer result was displayed. You must activate quick answers to see results from this metric. | VALUE(Searches with quick answer) |
| Search depth | The number of page views per search. | VALUE(Page views) / VALUE(Total searches) |
| Visitors | The number of unique visitors to the help center. | [Visitor ID] |
| Anonymous visitors | The number of anonymous visitors to the help center. | IF [Visitor role]="Anonymous" THEN [Visitor ID] ENDIF |
| Signed in visitors | The number of signed in visitors to the help center. | IF [Visitor role]!="Anonymous" THEN [Visitor ID] ENDIF |
| Session duration (sec) | The duration of a session in seconds. Single-event sessions (one search, one page view, only a ticket submission) are disregarded in calculating overall session length values. | VALUE(Session duration (sec)) |
| Session duration (min) | The duration of a session in minutes. Single-event sessions (one search, one page view, only a ticket submission) are disregarded in calculating overall session length values. | VALUE(Session duration (sec))/60 |

### User session attributes

This section lists and defines all of the available user session attributes.

Table 14. User session attributes

|  |  |
| --- | --- |
| **Attribute** | **Definition** |
| Session ID | Identifier for the unique user session. |
| Session brand | Brand of the help center where the tracked user activity occurred. |
| Session language | Language of the user session based on the locale of the help center content with which the user last interacted. Eligible content types are searches, article views, and clicks on suggested articles from the help center request form. If one of these events does not occur in a session, it is expected that the language is not recorded for that session. |
| Session locale | The locale of the session, for example, "en-us". |
| Session deflection type | The deflection type of the session. Values include assumed deflection, confirmed deflection, and no deflection. |
| Session last activity | The type of activity last recorded. Values include page view, quick answer search, and ticket submitted. |
| Session with search | Indicates whether a session had one or more searches performed, allowing for admins to drill in on sessions with or without search and the impact that has on their self-service efficiency. |
| Visitor name | The name of the help center visitor. Anonymous users will show a NULL value. |
| Visitor role | Role of the user interacting with the help center. |
| Visitor ID | The visitor ID of the user interacting with the help center content. Authenticated users are represented by their Zendesk user ID, and anonymous users are represented by a unique ID which can be used to join multiple sessions, but is not tied to any identifiable information. Important: By default, these datasets track only authenticated users, meaning users who are signed into their Zendesk account. If you want to track anonymous user activity, see [Enabling anonymous user tracking for your help center](https://support.zendesk.com/hc/en-us/articles/6297027870618). |
| Visitor email | The email address of the visitor. |
| Visitor status | The status of the visitor, for example, Active. |
| Visitor tags | Any tags associated with the visitor. |
| Exit page type | The type of the page associated with a page exit. Values include community post and article. |
| Exit page title | The title of the page associated with a page exit in the session. |
| Exit page ID | The ID of the page (community post or article) associated with a page exit in the user session. |
| Time - User session start | The timestamp representing when a user session begins. |
| Session locale | The locale associated with the session. Eligible content types are searches, article views, and clicks on suggested articles from the help center request form. If one of these events does not occur in a session, the locale is not recorded for that session. |
| Session deflection type | The type of deflection associated with the session. |
| Session last activity | The last event type recorded in a session. |
| Visitor email | The email address of the user associated with the session. |
| Visitor status | The Zendesk status of the visitor associated with the session. |
| Visitor tags | A list of tags associated with the help center visitor. For important information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Exit page type | The type of the page associated with a page exit. Values include community post and article. |
| Exit page title | The title of the page associated with a page exit in the session. |
| Exit page ID | The ID of the page (community post or article) associated with a page exit in the user session. |
| Time - User session start | The timestamp representing when a user session begins. |
| Time - User session end | The timestamp representing when a user session ends. |

## Quick answers dataset

Quick answers reports help you understand how your customers interact with your help
center, including what they’re searching for and how successfully they find answers.
They help you identify topics that interest customers most, and also helps you
detect gaps in your knowledge base that need to be addressed.

This section contains the following topics:

- [Quick answers metrics](#topic_itw_z3n_13c)
- [Quick answers attributes](#topic_erh_1jn_13c)

### Quick answers metrics

This section lists and defines the metrics available in the Quick
answers dataset.

|  |  |  |
| --- | --- | --- |
| Metric | Definition | Formula |
| Searches | The total number of searches performed. | [Search ID] |
| Searches with quick answer | The total number of searches with quick answers returned. | IF ([Search result type] = "With quick answers") THEN [Search ID] ELSE NULL ENDIF |
| Searches with article-only results | The total number of searches with article-only results returned. Results returned can be articles or community posts from the Knowledge base. | IF ([Search result type] = "With article-only results") THEN [Search ID] ELSE NULL ENDIF |
| Searches with no results | The total number of searches with no results returned. | IF ([Search result type] = "No results") THEN [Search ID] ELSE NULL ENDIF |
| % Quick answer rate | The percentage of searches with quick answers returned. | COUNT(Searches with quick answer)/COUNT(Searches) |
| % Article-only results rate | The percentage of searches with article-only results returned. | COUNT(Search results with article-only results)/COUNT(Searches) |
| % No result rate | The percentage of searches with no results returned | COUNT(Searches with no results)/COUNT(Searches) |
| Search article-only results | The number of article-only results that were returned for the search query. | IF ([guide\_generative\_searches\_result\_type] = "Without Quick Answer") THEN [guide\_generative\_searches\_result\_count] ELSE NULL ENDIF |
| Ratings | The total number of ratings given to quick answers. | COUNT(Positive ratings)+COUNT(Negative ratings) |
| Positive ratings | The total number of positive ratings given to quick answers. | IF ([Search result type] = "With quick answers" AND [Rating] = "Positive") THEN [Search ID] ELSE NULL ENDIF |
| Negative ratings | The total number of negative ratings given to quick answers. | IF ([Search result type] = "With quick answers" AND [Rating] = "Negative") THEN [Search ID] ELSE NULL ENDIF |
| % Positive ratings | The percentage of positive ratings given to quick answers. | COUNT(Positive ratings)/SUM(Ratings) |
| % Negative ratings | The percentage of negative ratings given to quick answers. | COUNT(Negative ratings)/SUM(Ratings) |

### Quick answers attributes

This section lists and defines the attributes available in the quick
answers dataset.

|  |  |
| --- | --- |
| Attribute | Definition |
| Search ID | The ID of the search. |
| Search query | The query entered in the search bar. |
| Search brand ID | The brand ID of the help center that the search was performed on. |
| Search brand name | The brand name of the help center that the search was performed on. |
| Search channel | The channel where the search was performed. |
| Search language | The language of the search query. |
| Search locale | The locale of the search query. |
| Search result type | The type of the search result. It can be quick answer, article-only result or no result. |
| Search result details | Content of the quick answer returned or status message if no quick answer was generated or no results were found. "Article-only results found" or "No results found" |
| Content type | The type of the article. |
| Content title | The title of the content. |
| Content ID | The ID of the content. |
| Content language | The language of the content. |
| Content locale | The locale of the content (for example, en-us). |
| Article category | The article of the article. |
| External content URL | The URL of the external content. |
| Rating | Rating provided by the user for the quick answer. it can be Positive, Negative or - |
| Rating feedback | Feedback provided by the user for the quick answer. |
| User name | Name of the user who performed the search. |
| User role | Role of the user who performed the search |
| User ID | The ID of the user who performed the search |
| User email | Email of the user who performed the search |
| User status | Status of the user who performed the search |
| User tags | Tags of the user who performed the search |
| Time - search made | The time each search was made. |