# Monitoring your account status with the Zendesk Status page

Source: https://support.zendesk.com/hc/en-us/articles/4408824499866-Monitoring-your-account-status-with-the-Zendesk-Status-page

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

The Zendesk Status page allows Zendesk users to monitor the status of their own Zendesk subdomain(s). You can also [subscribe](https://support.zendesk.com/hc/en-us/articles/4408821424666) to status notifications for your account.

This article focuses on the information related to your own subdomain's status, and discusses the following topics:

- [About the Zendesk Status page](#topic_fl5_ksb_kw__ul_wdj_z5b_kw)
- [Using the Zendesk Status page](#topic_m2c_yxb_kw)
- [Viewing Service incident information](#topic_yzk_jnc_kw)

To increase your understanding of service incidents, and the framework behind them, see the following:

- [Overview of incident management at Zendesk](https://support.zendesk.com/hc/en-us/articles/4408821685018)
- [Zendesk Support scalability and performance: Technical architecture](https://support.zendesk.com/hc/en-us/articles/4408832509338)

## About the Zendesk Status page

The Zendesk Status page displays status information related to your own Zendesk domain:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/status_page_new.png)

On the Zendesk Status page, you can view the following:

- Current active incidents
- A 90-day service history, organized by product and feature
- Basic information on each incident
- Detailed information on each incident

Once an incident is identified, an "investigating" banner appears on the Zendesk Status page. As soon as more specific information regarding the incident becomes available, it will replace this banner.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/investigating-banner.png)

In the sections below, we’ll discuss these elements in more detail.

You can view your information on the classic System Status page by clicking the **Switch to classic page** link. This is especially useful for customers who want to display their status on a TV screen, as TV mode is not currently available on the newer Zendesk Status page.

Note: Your Zendesk Status page and information is visible to anyone who knows your Zendesk subdomain.

**To view your Zendesk system status**

1. In your web browser, go to [https://status.zendesk.com](https://status.zendesk.com/). The Zendesk Status page opens:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/SysStatus1.png)
2. Enter your subdomain in the search box. For instance, if your Zendesk URL is *mycompany.zendesk.com*, enter the subdomain *mycompany*.
3. Click **Check**. Your subdomain’s status is displayed. Future visits to the site will remember this setting, so you don’t have to enter it each time.

Note: You can also use the Zendesk API to access system status. See [Zendesk Status API](https://developer.zendesk.com/rest_api/docs/status-api/status_api) for more information.

## Using the Zendesk Status page

The Zendesk Status page has two views:

- **Your Zendesk Subdomain**, which displays information specific to your subdomain.
- **All Data Centers**, which displays information about the Zendesk system-wide status.

If you experience any problems with your subdomain that do not appear on the Zendesk Status page, use the link at the bottom of the page to create a ticket for [Zendesk Customer Support.](https://support.zendesk.com/hc/en-us/articles/4408843597850)

When you enter your subdomain, as described above, the status page initially displays **Your Zendesk Subdomain** view:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/your_zendesk_subdomain_view.png)

This view is designed to be most relevant to users, and includes the following areas of information and functionality:

- The **Check status field**, where you can enter a new subdomain to view.
- The **Current active incidents box**, which shows all incidents currently affecting the subdomain.
- The **Services history list**, a list of the top-level Zendesk products, and a visual 90-day history of their status. Expanding a product box displays visual histories for any related subservices.

The **All Data Centers** view is similar to Your Zendesk Subdomain view, but displays the status of the Zendesk-wide system. You can display the All Data Centers view by clicking the x in the Check status field:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/all_data_centers_x.png)

### The Current active incidents box

The Current active incidents box displays all incidents currently impacting the subdomain.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/active_incidents_box.png)

The items in this list are not interactive, and are for informational purposes only.

### The Services history list

The Services history list allows you to interact with data related to service incidents, and display detailed information on those incidents. Here, you can view descriptions and updates on incidents in progress or historical incidents, and view incident reports and details from the past 90 days.

Note: Currently, the Services history list includes entries for all Zendesk products, even those you have not purchased

Each bar in a product service history represents a single day, from 90 days ago (on the far left) to today (on the far right):

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/service_history_support.png)

The color and size of each bar represents the most severe incident level that occurred on that date, in any of the related subservices:

- **Large Green bar:** No issues. The service is performing normally.
- **Medium Yellow bar:** Service degradation.
 There is intermittent or partial service interruption.
- **Small Red bar:** Service Outage. The service is currently unavailable.

#### Viewing the Subservice history list

Each product or service’s subservices are nested beneath it. For example, if you expand Support service, you’ll see line items for Ticketing, Views, SLAs, and so on, each with its own service history.

**To view the subservice history list**

- Click the chevron next to each product or service to expand and display that element’s subservices.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/subservice_history_list_expanded.png)

## Viewing service incident information

Any day with a Service degradation (yellow bar) or Service outage (red bar) includes an incident summary.

**To view an incident summary**

- Hover over the day’s bar. The incident summary appears.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/incident_summary.png)

An incident summary can include the following information:

- An overview description of the incident(s) (i.e., “Bubble Up test”)
- The date and time the incident(s) first reported
- The incident(s) resolution status
- A link to a more detailed incident description

**To view incident details**

- In the incident summary, click the **View details** link to open a window with more in-depth information on the incident:

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/incident_details.png)

If the incident has multiple updates, use the scroll bar to view earlier updates.

Incident details can include:

- Overview description of the incident.
- Beginning and end times/dates.
- Time and date of all updates to the incident, posted in real-time, beginning with the most recent.
- A link to the Incident Report, if available.

**To close the incident description**

- Click anywhere on the modal. The incident description closes.

To help you monitor your account status, admins and agents can choose to receive emails when a service incident affects your account by subscribing to incident email notifications. You can subscribe directly from the Zendesk status page or from your Support account.
[See Subscribing to status notifications](https://support.zendesk.com/hc/en-us/articles/4408821424666).