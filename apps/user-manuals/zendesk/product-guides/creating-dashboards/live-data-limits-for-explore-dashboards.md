# Live data limits for Explore dashboards

Source: https://support.zendesk.com/hc/en-us/articles/4408846310810-Live-data-limits-for-Explore-dashboards

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Enterprise |

To optimize performance and give you the best experience possible, Explore includes some
limits on your use of live dashboards and widgets. Use this article to learn about these
limits and help you get the best from your live data.

Tip: Zendesk now offers [real-time monitoring](https://support.zendesk.com/hc/en-us/articles/9757124462234), which enhances your reporting by
focusing on use cases, offering immediate decision-making insights, and tracking
trends for up to seven days.

This article contains the following sections:

- [Limits for concurrent users](#topic_uvr_pjz_lnb)

## Limits for concurrent users

To ensure the best experience for all our users in your organization, Explore
dashboards containing live widgets have the following user limits:

- The maximum number of concurrent users (users who can view an individual
  dashboard at the same time) for a live dashboard (or a dashboard containing
  live widgets) is 100.
- If a user doesn't interact with a live dashboard for one minute and 30
  seconds, it will time out and stop updating. Once the user starts to
  interact with the dashboard again, it will continue to update as long as
  there less than 100 concurrent users viewing the dashboard.

The session timeout applies to the slots available in the for maximum concurrent
users. For example when a user's session times out, their concurrent user slot will
be released for another user to take. When a user times out and returns to their
live dashboard, if there is a concurrent user slot available, Explore will present
the page to the user without any interruption.