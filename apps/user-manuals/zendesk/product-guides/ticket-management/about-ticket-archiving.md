# About ticket archiving

Source: https://support.zendesk.com/hc/en-us/articles/4408887617050-About-ticket-archiving

---

Verified AI summary ◀▼

Archiving tickets helps speed up loading times for views by automatically archiving tickets 120 days after they close. You can search for archived tickets using specific criteria, but they won't appear in views or trigger rules. You can still access and manage archived tickets through direct links, searches, user profiles, and API endpoints, keeping your support operations streamlined.

Archiving tickets speeds up the loading time for [views](https://support.zendesk.com/hc/en-us/articles/4408888828570), especially those with multiple tickets that have been
closed for a long time. In most cases, Zendesk automatically archives tickets 120 days
after the [ticket status changes to Closed or the ticket is in
the Closed state](https://support.zendesk.com/hc/en-us/articles/8263915942938#topic_zxw_4yk_fdc).

This article covers the following topics:

- [Understanding
  ticket archiving](#topic_uky_q21_34b__section_cz3_vxm_syb)
- [Actions you
  can take on archived tickets](#topic_uky_q21_34b__section_abh_bgm_syb)

## Understanding ticket archiving

You can identify an archived ticket if the **This is an archived ticket** banner
is displayed at the top.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_archive_banner.png)

There isn't a view or specific search filter to show only archived tickets. However,
you can [search for tickets](https://support.zendesk.com/hc/en-us/articles/4408882086298) that meet archiving
criteria, which is typically that they're Closed or in a Closed state for at least
120 days. For example: `type:ticket status:closed
updated<2023-03-31`.

Considerations:

- For accounts with extremely high volumes of tickets, Zendesk may automatically
  archive tickets sooner than 120 days after they are closed.
- Tickets aren't automatically archived if either of the following are true:
  - The ticket includes more than 10,000 events.
  - The ticket's associated records (including ticket events, field entries,
    audits, and ticket metric events) exceed 2MB.
- Archived tickets aren't included in the [User Data app](https://www.zendesk.com/marketplace/apps/support/6536/user-data/).
- Archived tickets aren't included in lists of related records for lookup
  relationship fields.
- In Zendesk sandbox environments, closed tickets are automatically archived after
  three days.

## Actions you can take on archived tickets

Archived tickets are still accessible and actionable. The following table includes
actions you can take on an archived ticket.

| Function | Details | Available? |
| --- | --- | --- |
| Direct access | Access a ticket directly via URL (for example, https://*yoursubdomain*.zendesk.com/agent/#/tickets/37) | Yes |
| Search | [Searching for tickets](https://support.zendesk.com/hc/en-us/articles/4408882086298) and accessing from search results | Yes |
| User profiles | [Viewing a list of tickets associated with a user](https://support.zendesk.com/hc/en-us/articles/4408829574810) (e.g., assigned tickets, CC'd tickets) | Yes |
| Explore reporting | [Zendesk Explore resources](https://support.zendesk.com/hc/en-us/articles/4408846357018) | Yes |
| Group profiles | Viewing a list of tickets associated with a [Group](https://support.zendesk.com/hc/en-us/articles/4408894175130) | Yes |
| Organizational profiles | Viewing a list of tickets associated with an [Organization](https://support.zendesk.com/hc/en-us/articles/4408882246298) | Yes |
| Incremental export | Available  [API endpoint](https://developer.zendesk.com/rest_api/docs/support/incremental_export)  detailing which tickets have been recently updated | Yes |
| My activities | Viewing a list of tickets associated with your requests. Archived tickets will still be labeled as "solved" in My activities. | Yes |
| Views | [Used to create filtered lists of tickets](https://support.zendesk.com/hc/en-us/articles/4408888828570). Archived tickets are excluded from these lists. | No |
| Rules | [Triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) and [Automations](https://support.zendesk.com/hc/en-us/articles/4408883801626) allow you to automate actions on tickets. Rules cannot be executed on archived tickets. | No |
| API | All ticket API endpoints except [Bookmarks](https://developer.zendesk.com/api-reference/ticketing/ticket-management/bookmarks/), [Count Tickets](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#count-tickets), [Count Ticket Comments](https://url.us.m.mimecastprotect.com/s/L2NtC82XXjCwz1qAMH2i7sya5BR?domain=developer.zendesk.com), [Listing Tickets](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#list-tickets), [Listing Ticket Metrics](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_metrics/#list-ticket-metrics), [Ticket Skips](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_skips/), and [Listing Ticket Audits](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_audits/#list-all-ticket-audits) return archived tickets. | Yes |
| Customer context | [Used to gather information about the requester and their previous tickets](https://support.zendesk.com/hc/en-us/articles/4408829170458). Archived tickets do not show under **Interactions** in the customer context panel. See [Viewing customer context in a ticket](https://support.zendesk.com/hc/en-us/articles/4408829170458#topic_nq1_qnm_xsb). | No |
| Data export | Full export of your data. See [Exporting data to a JSON, CSV, or XML file](https://support.zendesk.com/hc/en-us/articles/4408886165402). | Yes |