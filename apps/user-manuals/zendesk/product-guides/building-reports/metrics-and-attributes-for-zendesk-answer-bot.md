# Metrics and attributes for Zendesk Answer Bot

Source: https://support.zendesk.com/hc/en-us/articles/4408824748698-Metrics-and-attributes-for-Zendesk-Answer-Bot

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Zendesk has renamed our bot capabilities. Answer Bot is now *AI agents*, Flow Builder is *bot builder*, and Article Recommendations are *[autoreplies with articles](https://support.zendesk.com/hc/en-us/articles/4408820349850)*. The Explore dashboard described in this article uses legacy names.

Use this article to discover the metrics and attributes you can use to build Explore reports based on your usage of Zendesk bots. These datasets are also used for the Answer Bot prebuilt dashboards (see [Overview of the Answer Bot dashboard](https://support.zendesk.com/hc/en-us/articles/4408838386842)
).

For more information about how to create reports with Explore, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530).

This article contains the following topics:

- [Article Recommendations dataset](#topic_u23_1rs_crb)
- [Flow Builder dataset](#topic_mxt_wqs_crb)

## Article Recommendations dataset

This section contains the following topics:

- [Article Recommendations dataset schema](#topic_e22_3rs_crb)
- [Article Recommendations metrics](#topic_m5k_grs_crb)
- [Article Recommendations attributes](#topic_b4y_2rs_crb)

### Article Recommendations schema

Use this diagram to help you understand the elements of the Article Recommendations dataset and their relationships.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Answer_Bot.jpg)

### Article Recommendations metrics

This section lists and defines all metrics available in the Article Recommendations dataset.

Note:
Article Recommendations metrics aren’t fully supported for the messaging channel. Supported metrics include answers and attempts, but not clicks and resolutions.

Table 1. Article Recommendations metrics

| Metric | Definition | Explore formula |
| --- | --- | --- |
| Attempts | All instances in tickets and chats where Article Recommendations was available to recommend articles, regardless of whether the bot identified relevant articles to suggest. | [Answer ID] |
| Answers | Instances in tickets and chats where the bot identified articles relevant to a customer’s query and suggested them to the customer. | IF ([Answer status - Unsorted]="Offered" OR [Answer status - Unsorted]="Clicked" OR [Answer status - Unsorted]="Resolved") THEN [Answer ID] ENDIF |
| Unsuccessful attempts | Instances in tickets and chats where the bot could not identify any articles relevant to a customer’s query and did not make a suggestion to the customer. | IF ([Answer status - Unsorted]="Unoffered" ) THEN [Answer ID] ENDIF |
| Clicks | Counts successful attempts where at least one generated suggestion was clicked. | IF ([Answer status - Unsorted]="Clicked" OR [Answer status - Unsorted]="Resolved") THEN [Answer ID] ENDIF |
| Resolutions | Count of recommended articles that resolved the end user’s request. | IF ([Answer status - Unsorted]="Resolved") THEN [Answer ID] ENDIF |
| Indirect resolutions | The number of recommended articles that indirectly resolved the end user’s request. In some situations, suggested articles don’t resolve the customer’s enquiry directly but instead point them in the right direction in the help center to find the answer to their question. These resolutions are known as *indirect resolutions*. Indirect resolutions are reflected in **Resolutions**, **Indirect resolutions** and **Answer status** fields. | D\_COUNT(Resolutions)-COUNT(Resolution articles) |
| % Suggestion rate | The percentage of enquiries where the bot offered suggestions from the total number of enquiries it attempted to answer. | D\_COUNT(Offered answers)/D\_COUNT(Attempted answers) |
| % Resolution rate | The percentage of enquiries resolved from the total enquiries where it offered suggestions. | COUNT(Resolutions)/D\_COUNT(Offered answers) |
| Suggested articles | Count of the suggestions offered. | [Suggestion ID] |
| Clicked articles | The number of suggestions that have been clicked by a user. | IF ([Suggestion clicked]="true" ) THEN [Suggestion ID] ENDIF |
| Resolution articles | Count of solved tickets solved through a suggestion. | IF ([Suggestion resolved]="true" ) THEN [Suggestion ID] ENDIF |
| Rejected articles | The number of suggestions that have been marked as unhelpful by end users. | IF ([Suggested article rejected]=TRUE) THEN [Suggestion ID] ENDIF |
| % Article click-through rate | The percentage of suggestions that have been clicked by an end user. | COUNT(Clicked suggestions)/COUNT(Suggestions) |
| % Rejection rate | The percentage of suggestions that have been marked as unhelpful by end users. | COUNT(Rejected articles)/COUNT(Suggested articles) |
| Answered tickets | Count of tickets where articles were recommended, a suggestion was clicked, and this resulted in the ticket being solved. | IF ([Answer status - Unsorted]="Offered" OR [Answer status - Unsorted]="Clicked" OR [Answer status - Unsorted]="Resolved" ) THEN [Answer ticket ID] ENDIF |
| Unanswered tickets | Count of tickets where a suggestion was not given. | IF ([Answer status - Unsorted]="Unoffered" ) THEN [Answer ticket ID] ENDIF |
| Answer clicked tickets | Count of tickets where a suggestion was generated that resulted in the ticket being resolved. | IF ([Answer Status - Unsorted]="Clicked" OR [Answer status - Unsorted]="Resolved" ) THEN [Answer ticket ID] ENDIF |
| Solved tickets | Count of tickets with a status of **Solved**. | IF ([Answer status - Unsorted]="Resolved") THEN [Answer ticket ID] ENDIF |
| Non-reopened solved tickets | Count of tickets with a status of **Solved**, that have not been re-opened. | IF ([Answer status - Unsorted]="Resolved" AND VALUE(Reopens)<1) THEN [Answer ticket ID] ENDIF |
| Reopened solved tickets | Count of tickets that were set to a status of **Solved** and were subsequently re-opened. | IF ([Answer status - Unsorted]="Resolved" AND VALUE(Reopens)>0) THEN [Answer ticket ID] ENDIF |
| Agent unassisted solved tickets | Count of tickets with no Assignee set, and with a status of **Solved** through a suggestion. | IF ([Answer status - Unsorted]="Resolved" AND VALUE(Agent replies)<1) THEN [Answer ticket ID] ENDIF |
| Agent assisted solved tickets | Count of tickets that are assigned to an agent, where the agent has replied, and the ticket status is **Resolve** using a suggestion. | IF ([Answer status - Unsorted]="Resolved" AND VALUE(Agent replies)>0) THEN [Answer ticket ID] ENDIF |
| % Ticket usage rate | The rate of tickets that were assisted by suggestions in comparison to total number of tickets. | DCOUNT\_VALUES([Answer ticket ID])/DCOUNT\_VALUES([Ticket ID]) |
| % Ticket resolution rate | The percentage of tickets resolved by suggestions compared to the total solved ticket volume where a response was given. | D\_COUNT(Solved tickets)/D\_COUNT(Answered tickets) |
| % Ticket non-reopened resolution rate | The rate of ticket resolutions that have not been re-opened provided by suggestions in comparison to total tickets where an answer was generated. | D\_COUNT(Non-reopened solved tickets)/D\_COUNT(Answered tickets) |
| % Ticket unassisted resolution rate | The rate of ticket resolutions provided by suggestions in comparison to total tickets where an answer was generated. | D\_COUNT(Agent unassisted solved tickets)/D\_COUNT(Answered tickets) |
| Click time (min) | The duration in minutes between a suggestion being generated and this suggestion being clicked. | (Click time (min)) |
| Resolution time (min) | The duration in minutes between a suggestion being generated and this suggestion solving the ticket. | (Resolution time (min)) |
| Click time (hrs) | The duration in hours between a suggestion being generated and this suggestion being clicked. | VALUE(Click time (min))/60 |
| Resolution time (hrs) | The duration in hours between a suggestion being generated and this suggestion solving the ticket. | VALUE(Resolution time (min))/60 |
| Agent replies | Counts the total number of agent replies to a ticket. | (Agent replies) |
| Reopens | The number of times a ticket status changed from **Solved** to **Open**. | (Reopens) |

### Article Recommendations attributes

This section lists and defines all attributes available in the Article Recommendations dataset. You can use this diagram to help you understand the meaning of some of the attributes in the list:

![Common Answer Bot attributes](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_Answer_Bot_attributes.png)

Table 2. Article Recommendations attributes

| Attribute | Definition |
| --- | --- |
| Answer status | The status of a suggestion provided. The status is set depending on the end user's response. Values include **Unoffered**, **Offered**, **Clicked** or **Resolved**. |
| Answer channel | The channel on which a suggestion was offered to an end user or agent. Values include: - **Agents**   (when an agent uses the Knowledge Capture   app or the knowledge section of the context panel from   within a ticket) - **Conversation Bots**   (on messaging channels   including Web Widget, mobile SDKs, and social messaging   apps) - **API** - **Email** - **SDK**   (Classic mobile SDKs only) - **Slack** - **Web form** - **Web Widget**   (Classic only) |
| Answer brand | The brand of ticket corresponding to the brand of the knowledge base where a suggestion for an answer was generated. |
| Answer enquiry | The end user’s question for which suggestions were offered. The attribute values are limited to the first 255 characters. This attribute does not include the Generate a reply and Don't answer based on articles bot response options. To report on these, use the Content text attribute in the [Flow Builder dataset](#topic_jtk_crs_crb). |
| Answer ID | The ID of the notification with suggestions sent. |
| Answer resolution article ID | The ID of the knowledge base article which resolved the end user’s enquiry. |
| Answer ticket ID | The ID of the ticket from which the response was triggered. |
| Suggested article clicked | The event of the suggestion generated being clicked by an end user. Values are **True** and **False**. |
| Suggested article resolved | The event of the suggested article being clicked from the answer generated that led to the ticket being resolved. Values are **True** and **False**. |
| Suggested article rejected | The article suggestion generated being marked as unhelpful by an end user. Values are **True** and **False**. |
| Suggestion ID | The ID of the knowledge base article suggestion sent. |
| Suggested article language | The language of the knowledge base article suggestion sent. |
| Suggested article locale | The locale of the knowledge base article suggestion sent. Values include **EN-US**, **EN-GB**, **DE**, **FR**, **RU**. |
| Article ID | The ID of the knowledge base article. |
| Article ID and locale | The ID and locale of the knowledge base article. |
| Article translation title | The title of the knowledge base article in a specific language. |
| Article translation URL | The URL of the knowledge base article. |
| Article author | The name of the user who originally created a knowledge base article. |
| Ticket ID | The ID number of the ticket. |
| Ticket status | The current status of the ticket. |
| Ticket group | The name of the group where the ticket was assigned. |
| Ticket assignee | The name of the user to who the ticket is assigned. |
| Ticket brand | The brand of the ticket. |
| Ticket channel | The channel a ticket was created from. For more information about the ticket channels Explore collects, see [Understanding ticket channels in Explore](https://support.zendesk.com/hc/en-us/articles/4408836378394). |
| Ticket form | Ticket form used on the ticket. |
| Ticket organization | The name of the organization associated with the ticket. |
| Ticket priority | The ticket’s priority. |
| Ticket problem ID | The ID of the associated problem ticket. |
| Ticket requester | The name of the user that requested the ticket. |
| Ticket satisfaction rating | The satisfaction rating of the ticket, **Good** or **Bad**. |
| Ticket subject | The subject of ticket. |
| Ticket tags | The tags associated with a ticket. For information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Ticket type | The ticket type. |
| Sharing agreement inbound | Affiliated instances of Zendesk Support and companies who share tickets with the current instance of Zendesk Support. |
| Sharing agreement outbound | Affiliated Zendesk accounts and companies tickets are shared with. |
| User name | The name of the user who was assisted. |
| User role | The role of the user who was assisted. |
| User ID | The ID of the user who was assisted. |
| User email | The email address of the user who was assisted. |
| User locale | The locale of the user who was assisted. |
| User status | The Zendesk status of the user who was assisted. Values are **Active**, **Suspended** or **Deleted**. |
| User tags | A list of tags associated with the user who was assisted. For information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| User time zone | The time zone of the user who was assisted. |
| User organization name | The organization name of the user. |
| User organization ID | The organization ID of the user. |
| User organization domains | The domain name of the organization of the user, for example, zendesk.com. |
| User organization status | The system status of the organization of the user, either active or deleted. |
| User organization tags | The tags associated with the organization of the user. For information about filtering reports using tags, see [Reporting on ticket tags using filters](https://support.zendesk.com/hc/en-us/articles/4408838151450#topic_a15_bjp_plb). |
| Intent (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538) ) | A prediction of what the ticket is about. To see the possible values, [open the Taxonomy tab of the Intent settings page](https://support.zendesk.com/hc/en-us/articles/9488234915610) to see the AI Intents list under the **Taxonomy values** heading. |
| Intent confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538) ) | The likelihood that the intent prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Language (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538) ) | A prediction of what language the ticket is written in. To see the possible values, [open the Taxonomy tab](https://support.zendesk.com/hc/en-us/articles/9488234915610) of the settings page. |
| Language confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538) ) | The likelihood that the language prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Sentiment (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538) ) | A prediction of how the customer feels about their request. Possible values are **Very Positive**, **Positive**, **Neutral**, **Negative**, and **Very Negative**. |
| Sentiment confidence (Requires [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538) ) | The likelihood that the sentiment prediction is correct. Possible values are **High**, **Medium**, and **Low**. |
| Time – Answer Bot answer created | Includes several **Answer created** attributes that refer to the time when an answer was generated containing relevant knowledge base articles. |
| Time – Answer Bot answer last event | Includes several **Answer event** attributes that refer to the last answer notification. |
| Time – Answer Bot suggested article last event | Includes several **Suggested article event** attributes that refer to the last time a suggestion was triggered. |
| Time – Answer Bot suggested article clicked | Includes several **Suggested article clicked** attributes that refer the time a suggested article was clicked from an answer. |
| Time – Answer Bot suggested article resolved | Includes several **Suggested article resolved** attributes that refer to the time a suggested article was clicked from an answer, which led to ticket being resolved. |
| Time – Ticket created | Includes several attributes that return the time and date when tickets were created. |
| Time – Ticket solved | Includes several attributes that return the time and date when tickets were solved. |
| Time – Ticket last updated | Includes several attributes that return the time and date when tickets were last updated. |
| Time – Article created | Includes several attributes that return the time when an article was created. |
| Time – Article updated | Includes several attributes that return the time when an article was last updated. |

## Flow Builder dataset

This section contains the following topics:

- [Flow Builder metrics](#topic_dzk_drs_crb)
- [Flow Builder attributes](#topic_jtk_crs_crb)

### Flow Builder metrics

This section lists and defines all metrics available in the Flow Builder dataset.

Table 3. Flow Builder metrics

| Metric | Definition | Explore formula |
| --- | --- | --- |
| Total users | The number of unique users who received a message from the bot. A user does not have to engage with the bot (sending a message or clicking a quick reply) to be included in this count. | [Sunshine Conversations app user ID] |
| Engaged with bot | The number of unique users who have sent a message to the bot or responded to a prompt. | IF ([Activity event type] = "user\_input\_received") THEN [Sunshine Conversations app user ID] ELSE NULL ENDIF |
| Transferred to agent | The number of unique users who have successfully completed the transfer step from the bot to an agent. A Support ticket is created for each successful transfer. | IF ([Activity event type] = "agent\_transfer\_completed") THEN [Sunshine Conversations app user ID] ELSE NULL ENDIF |
| % total users who engaged with bot | The percentage of total users who have sent a message to the bot or responded to a prompt. | D\_COUNT(Engaged with bot) / D\_COUNT(Total users) |
| % engaged users transferred to agent | The percentage of engaged users who have successfully completed the transfer step from the bot to an agent. | D\_COUNT(Transferred to agent) / D\_COUNT(Engaged with bot) |
| User input count | The total number of user inputs (messages of any type) received by the bot. | [Content text] |
| Total users in previous 30 days | The total number of users in the period from 62 days to 32 days before today. | |
| Total users in last 30 days | The total number of users in the period from 31 days ago to yesterday. | |
| Engaged users in previous 30 days | Users who engaged with the bot in the period from 62 days to 32 days before today. | |
| Engaged users in last 30 days | Users who engaged with the bot in the period from 31 days ago to yesterday. | |
| Transferred users in previous 30 days | Users who were transferred from the bot to an agent in the period from 62 days to 32 days before today. | |
| Transferred users in last 30 days | Users who were transferred from the bot to an agent in the period from 31 days ago to yesterday. | |
| Containment rate | The proportion of engaged users whose conversation was *not* transferred from the bot to an agent. The inverse of **% transferred to agent**. | |
| Resolution feedback prompts | The number of times the bot asked for feedback via an “Ask if question resolved” step. **Note:** This metric and the following metrics are counted based on each instance of the event and not aggregated per user. So if a user went through the same flow and replied to a feedback prompt more than once, this metric counts each instance of a prompt being sent or a feedback reply interaction. | |
| Resolution feedback replies | The number of feedback prompt replies received by the bot. | |
| % resolution feedback replies | The proportion of times the bot received a reply after sending a feedback prompt. This is the count of replies of any type divided by the count of prompts sent. | |
| Resolved feedback replies | The number of *resolved* feedback prompt replies received by the bot (for example, “Yes, problem solved”). | |
| % resolved | The proportion of total replies that were *resolved* replies. This is the count of resolved replies divided by the count of total replies. | |
| Unresolved feedback replies | The number of *unresolved* feedback prompt replies received by the bot (for example, “No, I still need help”). | |
| % unresolved | The proportion of total replies that were *unresolved* replies. This is the count of unresolved replies divided by the count of total replies. | |

### Flow Builder attributes

This section lists and defines all attributes available in the Flow Builder dataset.

Table 4. Flow Builder attributes

| Attribute | Definition |
| --- | --- |
| Brand ID | The ID of the brand associated with the bot the user engaged with. |
| Brand name | The name of the brand associated with the Flow Builder flow the user engaged with. |
| Sunshine Conversations app user ID | The unique identifier of the user participating in a messaging conversation. |
| Activity event type | The event type recorded as a result of certain bot conversation interactions. Values include: Conversation started (journey\_started), Engaged with bot (user\_input\_received), Transferred to agent (agent\_transfer\_completed), (resolution\_prompt\_sent), (subflow\_switched), and (user\_feedback\_received). Events are recorded only for published answers. If answers are removed, unpublished, or renamed, historical data isn’t affected. |
| Channel | The Zendesk channel where the interaction took place. In Sunshine Conversations terminology, a “channel” is referred to as “source.type”. |
| Time - Activity occurred | Includes several attributes that return the time and date when an activity (Conversation started, Engaged with bot, or Transferred to agent) happened. |
| Language | The standard name for a language (for example, Simplified Chinese). |
| Language code | The shorthand code for a language (for example, zh-CN). |
| User input type | The type of user input received by the bot. Possible values include **Option selected**, **Message sent**, **Form sent**, and **Unknown**. |
| Content type | This is effectively the same as user input type. User input type is the human friendly name, while content type is the raw value used by the system. |
| Content text | The text of the message sent to the bot. This includes only messages sent as a result of selecting a quick reply option (the **Option selected** value in the **User input type** attribute). Free text entered by end users is returned as blank values. |
| Answer ID | The ID of the answer. |
| Answer name | The name of the answer. This is referred to as “intent” when creating an answer in bot builder. |
| Answer type | The type of answer. Possible answer types are:   - **answer** - **initial**   (For the greeting   standard response, if enabled) - **fallback**   (For the fallback   standard response) - **unknown**   (For legacy and   unexpected values) |
| Option is resolution feedback | Indicates whether the type of option selected was a resolution feedback reply, as opposed to a standard option. Possible values are **true** or **false**. An attribute of the `user_input_received`event. |
| Resolution feedback reply | Indicates how the user replied to the resolution feedback prompt (when the bot asks for feedback via an “Ask if question resolved” step). Possible values are **Resolved** or **Unresolved**. An attribute of the `user_feedback_received`event. |