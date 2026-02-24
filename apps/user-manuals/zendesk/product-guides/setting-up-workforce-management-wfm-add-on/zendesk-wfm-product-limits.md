# Zendesk WFM product limits

Source: https://support.zendesk.com/hc/en-us/articles/7697409906842-Zendesk-WFM-product-limits

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

This article outlines the product limits for Workforce Management (WFM), detailing maximum thresholds for monitoring, reporting, scheduling, and administration. Understanding these limits helps you manage data effectively, anticipate occasional inconsistencies, and ensure optimal system performance. Key limits include dashboard and widget counts, file sizes, and scheduling intervals. Regular updates may introduce new limits based on usage patterns.

[The Workforce Management (WFM) system](../../getting-started/getting-started-with-zendesk-workforce-management/getting-started-with-zendesk-wfm-manager-guide.md) processes large volumes of data in near real-time, balancing speed, scalability, and accuracy. This article outlines the maximum product limits that are in place for Zendesk WFM.

Because Zendesk WFM operates in a distributed, real-time environment, you may occasionally notice slight differences or inconsistencies in the data. Minor data differences are a normal part of real-time, distributed systems. Such differences are typically small in relation to the overall data and rarely impact your day-to-day decisions. It's helpful to share this information with your team to help them understand the reasons for [occasional small inconsistencies](https://support.zendesk.com/hc/en-us/articles/9513135487514).

This article contains the following topics:

- [Limits for WFM Monitoring and Reporting](#topic_vl4_khk_1bc)
- [Limits for WFM Scheduling](#topic_l1c_kwp_fcc)
- [Limits for WFM Administration](#topic_aj5_xbq_fcc)

Note: This article will continue to be updated, as we may introduce additional limits in the future based on usage.

## Limits for WFM monitoring and reporting

The following table shows the maximum limits for Zendesk WFM monitoring and reporting.

| | | |
| --- | --- | --- |
| **Page** | **Feature** | **Limits** |
| Dashboard | Maximum number of dashboards | 10 |
| Maximum number of widgets per dashboard | 12 |
| Reports | File size | < 15 MB |
| UI response timeout | < 15 sec |
| Daterange picker future max (the maximum number of days that can be selected in the future) | -1 (we currently don't allow a current day selection) |
| Data granularity per time frame selected | - 1 day or less: data is displayed in 15m or 30m intervals - 7 days or less: data is displayed daily and hourly - 31 days or less: data is displayed weekly and daily - 13 weeks or less: data is displayed weekly, monthly and   quarterly - Up to 58 weeks (or the equivalent of 13 months): data is displayed   monthly and quarterly |
| Agent Activity | Date picker future max (max number of days displayed in future) | 0 (we currently only allow up to the current day selection; it’s not possible to select future dates) |
| Agent Attendance | Date picker future max (max number of days displayed in future) | 0 (we currently only allow up to the current day selection; it’s not possible to select future dates) |
| Public API | Rate limit (number of requests per second) | 100 requests |
| Pagination limit per page | 100 items |

## Limits for WFM scheduling

The following table shows the maximum limits for Zendesk WFM scheduling.

| **Page** | **Feature** | **Limits** |
| --- | --- | --- |
| Agent Schedule Time Off | Maximum number of requested days displayed in advance in the sidebar | One year |
| Maximum number of requested days displayed in the past in the sidebar | 30 days |
| Agent schedule shift trades | Maximum number of requested days displayed in the past in the sidebar | 30 days |
| Agent schedule notes | Maximum number of notes | 1 per task |
| Schedule | Maximum scheduling interval | 90 days |
| Maximum publishing interval in the past | 30 days |
| Maximum publishing interval | 90 days |
| Import schedule CSV file size | 25Mb |
| Maximum exporting interval | 30 days at once |
| Maximum bulk add shifts interval | 90 days |
| Maximum scheduling recurring tasks repeat interval | 12 weeks |
| Maximum task "Recurrence ends on" interval | 90 days |
| Minimum task size | 5 min |

## Limits for WFM Administration

The following table shows the maximum limits currently in place for Zendesk WFM Administration.

| **Page** | **Feature** | **Limits** |
| --- | --- | --- |
| Roles and permissions | Number of roles per user | 1 |
| Account settings | Block and allow lists maximum number of characters | 4B characters |
| Locations | Location shifts: maximum rotation period (rotation folder) | 12 weeks, 90 days |
| Location shifts: maximum duration of a task | 24 hours |
| Location shifts: minimum duration of a task | 5 minutes |
| Location shifts: maximum number of start time options for automatic shift intraday | 10 items |
| Location shifts: maximum shift length | 24 hours |
| Location shifts: minimum shift length | 5 minutes |
| Location shifts: maximum difference in shifts start time for automatic shifts | ±24 hours |
| Location shifts: maximum rotation period (automatic shifts) | 12 weeks, 90 days |
| Workstreams | Maximum number of workstreams inside a combined workstream | 10 |
| Forecast | Maximum number of visible workstreams on chart | 10 |
| Use Zendesk data (available in WFM database) | 2 years |
| AHT (Average handle time) | 24 hours |
| Duration | 24 hours |
| Concurrency | 100 |
| First response time | 48 hours |
| Speed of answer | 48 hours |
| Wait time | 48 hours |
| Shrinkage | 99 |
| Minimum staffing | 1000 |
| Import historical volume period | Cannot be future dates |