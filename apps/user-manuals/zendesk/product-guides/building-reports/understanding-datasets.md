# Understanding datasets

Source: https://support.zendesk.com/hc/en-us/articles/4408839218842-Understanding-datasets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

Your Zendesk data is split into different *datasets*. Each dataset contains metrics and attributes that you can use to [create reports](https://support.zendesk.com/hc/en-us/articles/4408821589530). You must select a specific dataset before you can create a report.

Use this article to help choose the right dataset for your reports and to learn more advanced information about how datasets store your business information.

This article contains the following topics:

- [Understanding the available default datasets](#topic_hr1_tfk_jkb)
- [Understanding dataset structure](#topic_qgq_dmk_jkb)

Related articles:

- [Working with datasets](https://support.zendesk.com/hc/en-us/articles/4408846513050)
- [Setting dataset permissions](https://support.zendesk.com/hc/en-us/articles/4408831563802)

## Understanding the available default datasets

The table below describes the datasets that are available for each product.

Tip: Need help finding the right metrics and attributes to measure success and make smart business decisions? If so, check out [Top 18 customer service metrics to measure](https://www.zendesk.com/blog/customer-service-metrics-matter/).

Table 1. Explore default datasets

| Zendesk product area | Dataset name | What it contains |
| --- | --- | --- |
| Support | Tickets | Information about ticket details, like ticket ID and assignee. Does not include ticket update events. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4408827693594#topic_zlf_slp_4y) |
| Updates history | Information about updates made to tickets during their lifetime. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4408827693594#topic_as3_slp_4y) |
| Backlog history | Information about your unsolved tickets at the end of a given date. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4408827693594#topic_dfb_ydg_ndb) |
| SLAs | Information about your service level agreement (SLA) performance. Available only if you have tickets with SLA policies applied. See [Defining and using SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866). [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4408827693594#topic_cyq_fr4_l2b) |
| Group SLAs | Information about your group service level agreement (SLA) performance. Available only if you have tickets with SLA policies applied. See [Defining group SLA policies for internal teams](https://support.zendesk.com/hc/en-us/articles/5322445643802). [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4408827693594#topic_svt_cjx_kxb) |
| Knowledge | Knowledge Capture | Information to help you understand the efficiency of selecting articles to deflect support tickets. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4409155064090#topic_e45_ngh_bfb) |
| Team Publishing | Information to help you understand your team activity in Guide, including when articles are created, published, edited and more. Available only on Enterprise plans. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4409155064090#topic_aff_45y_jnb) |
| Knowledge Base | Information to help you understand how often your help center articles are being viewed, which articles are being voted up or down, and more. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4409155064090#topic_zwt_jht_cnb) |
| Search | Information about the searches that users performed and the terms they searched for in your knowledge base. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4409155064090#topic_anj_4gj_nrb) |
| Community | Information about the activity in your community forums, including the number of posts and comments, upvotes and downvotes, community members, and more. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4409155064090#topic_n5d_4dj_ktb) |
| User session | Information about user session activity from the help center to assess how effectively visitors are locating the answers they seek. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4409155064090#topic_cck_rlw_x2c) |
| Page efficiency | Information about help center page analytics to pinpoint self-service content that effectively provides answers, as well as content that may need enhancement. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4409155064090#topic_cz1_1lw_x2c) |
| Quick answers | Information to help you understand how your customers interact with your help center, including what they’re searching for and how successfully they find answers. [Full list of metrics and attributes](metrics-and-attributes-for-zendesk-knowledge.md#topic_jk2_x3n_13c) |
| Messaging and live chat | Messaging tickets | Information about all messaging channels, including web, mobile, and social messaging channels. Includes number of tickets, resolution times, satisfaction, and more. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4724624097818) |
| Engagement | Information about your customer engagement using Chat. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4409149177242#topic_r34_grl_mfb) |
| Chat Concurrency | Information about your agents' handling of concurrent chat engagements. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4409149177242#topic_ecm_gdp_mrb) |
| Voice | Calls | Information about your call center and agent activity. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4409156145434) |
| Answer Bot | Article Recommendations | Information about the performance of help center articles automatically recommended to customers. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4408824748698#topic_u23_1rs_crb) |
| Flow Builder | Information about bot performance across Zendesk channels. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4408824748698#topic_mxt_wqs_crb) |
| Omnichannel | Agent state | Information about how groups and agents spend their time across channels. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/5600290657434#topic_vyt_whf_2xb) |
| Agent state daily | Information about how groups and agents spend their time across channels, aggregated daily. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/5600290657434#topic_t4m_xhf_2xb) |
| Agent productivity | Information about work items offered and assigned to agents and how agents used their capacity. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/5600290657434#topic_v33_zw2_z1c) |
| Custom queues | Information about queue volume and efficiency over time. For example, the maximum, minimum, and average of queue wait time. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/9046662025498) |
| Engagement | Information about agent contributions in any given ticket. Includes metrics like engagement duration and assignment to first reply time. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/9204180217498) |
| AI | Generative AI agent tools | Information about agents’ usage of the following generative AI features: [summarize](https://support.zendesk.com/hc/en-us/articles/5608712782362#topic_ky3_wvc_3xb), [expand](https://support.zendesk.com/hc/en-us/articles/5608712782362#topic_r5d_xvc_3xb), and [make more friendly and make more formal](https://support.zendesk.com/hc/en-us/articles/5608712782362#topic_w25_xvc_3xb). [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/6961660060186) |
| Intelligent triage | Metrics and attributes that relate to tickets enriched with intent, language, and sentiment.[Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/6961660060186) |
| Copilot suggestions | Information about how agents engage with Zendesk AI copilot-powered suggestions, including similar tickets, merging suggestions, suggested macros, suggested replies, and quick answers. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/6961660060186#topic_jly_x2d_mfc) |
| Copilot auto assist | Information about how agents are using auto assist and checking procedure adoption, ticket volume, number of executed actions, and acceptance rate. [Full list of metrics and attributes](https://support.zendesk.com/hc/en-us/articles/6961660060186) |

## Understanding dataset structure

Explore datasets contain all of the available information for your product. To query your data efficiently and avoid duplicate or inconsistent data, Explore groups your data into multiple data tables. You can think of a data table as a kind of "box" in which your data is stored. Each data table is not isolated; instead, they're joined to one another by *connection points special attributes* that act as unique identifiers for each row of data in the table.

In the example diagram below, ticket data is stored in the **Tickets** data table and user data is stored in a separate **Users** data table. These data tables are joined in the datasets using connection points special attributes.

For example, **Ticket ID** is the connection point for the **Ticket** data table, but **Requester ID** is the connection point for the **Users** table.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Dataset_schemas__Online_Whiteboard_for_Visual_Collaboration.png)

When a user runs a report, Explore determines which tables contain the required metrics and attributes and whether the tables need to be joined. If the required metrics and attributes are located in one table, then no connections (or joins) are made. An example of this is a report that counts ticket IDs by status.

However, if the required metrics and attributes are in multiple data tables, then the tables will be joined. An example of this is a report that counts ticket updates by assignee name. In this case, the **Ticket updates**, **Tickets**, and **Users** tables are joined to generate the result.

Explore data tables are connected using the LEFT JOIN method. This means that when the tables are joined, the report returns all rows from the table on the left, even if there are no matches from the table on the right. In the example above, a count of ticket IDs by assignee name will return all tickets with or without an assignee.

In some cases, it's technically not possible to store data in multiple data tables due to the high volume of the data or high speed of the report execution required. An example of this is the Backlog dataset. This uses only one table for storing data.