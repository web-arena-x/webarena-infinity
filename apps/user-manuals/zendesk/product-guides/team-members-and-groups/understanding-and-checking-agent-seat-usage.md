# Understanding and checking agent seat usage

Source: https://support.zendesk.com/hc/en-us/articles/4408834934554-Understanding-and-checking-agent-seat-usage

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

When you purchase Zendesk Suite or Support, you purchase a number of agent *seats*, or allocated user licenses, that are consumed by the team members you add to your account. Most roles consume one of the purchased and counted seats, but there are a few exceptions. If you’re having trouble adding or managing agents, you may have reached your seat limit.

This article explains how these seats are counted and used.

- [About roles and seat provisioning](#topic_vtq_zsq_l4b)
- [Checking how many seats you’re using](#topic_b12_c5q_l4b)
- [Fixing an over-provisioned account](#topic_an4_fwq_l4b)

## About roles and seat counts

Support has a variety of user roles, most of which are counted against the available agent seats and others that aren’t counted. For example, the Contributor and Light Agent roles in Support don’t consume a seat.

However, the roles counted against the seat count change when the account has other Zendesk functionality like [live chat and messaging](https://support.zendesk.com/hc/en-us/articles/4408828690074-Buying-The-Zendesk-Support-Suite#topic_y5l_hlz_rdb) or analytics and users are assigned roles for both Support and other functionality.

- Most roles on other products require a Support seat that is counted against the available agent seats.
- If a user fills a role for another product that requires a counted Support seat, that user is counted against the Support seat count even if their Support role typically wouldn’t be counted.

For information about other product roles and requirements, see [About team member product roles and access](https://support.zendesk.com/hc/en-us/articles/4408832171034).

### Zendesk roles included in the Support seat count

| Products | Role | Requires counted Support Seat |
| --- | --- | --- |
| [Support](https://support.zendesk.com/hc/en-us/articles/4408883763866) | [Account owner](https://support.zendesk.com/hc/en-us/articles/4408846746778) | Yes |
| Admin | Yes |
| Agent | Yes |
| Contributor | No |
| Light agent | No |
| [Guide](https://support.zendesk.com/hc/en-us/articles/4408827842458) | Admin | Yes |
| Agent | Yes |
| Viewer | No |
| [Talk](https://support.zendesk.com/hc/en-us/articles/4408882966170) | Admin | Yes |
| Agent | Yes |
| Team lead | Yes |
| [Chat](https://support.zendesk.com/hc/en-us/articles/4408882929946) | Admin | Yes |
| Agent | Yes |
| Custom role | Yes |
| [Explore](https://support.zendesk.com/hc/en-us/articles/4408836002970) | Admin | Yes |
| Editor | Yes |
| Viewer | No |

## Checking how many seats you're using

As part of managing your subscription, you can use the Team members page to monitor the number of agent seats (paid licenses) you have remaining in your account. This count provides you with advance warning when you're about to run out of licenses and need to buy more.

Note: You might also want to generate an export of all your team members' data from the Team members page. This export includes information about your team members, including their assigned product roles. See [Exporting team-member data](https://support.zendesk.com/hc/en-us/articles/5407034434842).

**To monitor remaining seats**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.

   The Team members page appears with a list of all agents, admins, and the account owner in your account. See [About the team members page](https://support.zendesk.com/hc/en-us/articles/4408843830938).
2. Review the **Seats remaining** description on the upper right of the page.

   **Seats remaining** displays information about how many of your agent seats you’ve used for each product and how many seats you have remaining. It includes a link to add additional seats.

   | Seats remaining, Zendesk Suite | Seats remaining, multiple products |
   | --- | --- |
   | | |
3. To add more seats, click **Add more seats** to open the Subscription page in your account.

   Self-service and eligible sales-assisted accounts can add more seats from the Subscription page. You must be the [account owner](https://support.zendesk.com/hc/en-us/articles/4408881860378-How-do-I-find-out-who-the-Support-account-owner-is-) or a [billing admin](https://support.zendesk.com/hc/en-us/articles/4408838125082) to add the seats.
   Admins who don’t have billing permission can [request subscription changes](https://support.zendesk.com/hc/en-us/articles/4408828513434).

   For details, see [Adding agent seats to your subscription](https://support.zendesk.com/hc/en-us/articles/4408881540506) and [Managing agent seats](https://support.zendesk.com/hc/en-us/articles/4408834934554).

Tip: If you find you're using more seats than expected, check the roles you have set for light agents and contributors. See [Discovering light agents and contributors that also take up paid agent seats](https://support.zendesk.com/hc/en-us/articles/4844001120410).

## Fixing an over-provisioned account

Due to an issue in the way agent seats were counted for Zendesk Support Suite and Zendesk Support accounts with multiple products, it was briefly possible for some accounts to add more team members than they purchased. This inconsistency with the seat count was fixed with the release of the [team member profile in Admin Center.](https://support.zendesk.com/hc/en-us/articles/4408832485914)

Because it was our error, we aren’t taking those additional users away automatically. Instead, we’ve updated the **seats used** value in Support to reflect the actual number of team members you’ve added.

However, you won’t be able to add new users or manage existing roles and permissions in the team member profile until you reduce the number of team members on your account to the number of seats purchased. To do this, you must either [downgrade permissions](https://support.zendesk.com/hc/en-us/articles/4408888690842#2) or [remove the role](https://support.zendesk.com/hc/en-us/articles/4408824375450#topic_ppd_dky_lkb) that requires a Support seat. Alternatively, you can [purchase additional seats](https://support.zendesk.com/hc/en-us/articles/4408881540506) for the team members. After you bring your account back into alignment with the number of agent seats purchased, your ability to add and manage users and roles will be re-enabled.