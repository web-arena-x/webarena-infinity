# Understanding discrepancies between the Talk Live calls dashboard and the Explore live dashboard

Source: https://support.zendesk.com/hc/en-us/articles/4408828509210-Understanding-discrepancies-between-the-Talk-Live-calls-dashboard-and-the-Explore-live-dashboard

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Professional or Enterprise |

Note: Talk customers who are not on a Suite plan must also have Explore Enterprise to use the
Explore live dashboard.

Both the Talk Live calls dashboard and the Explore live dashboard contain near real-time
information about calls in your Zendesk instance. Sometimes, the information in each
dashboard might not match. Use the information in this article to help understand when
discrepancies might occur.

- For more information about the Talk Live calls dashboard, see [Monitoring calls with the Live calls dashboard](https://support.zendesk.com/hc/en-us/articles/4408885902490).
- For more information about the Explore live dashboard, see [Overview of the Explore live dashboard](https://support.zendesk.com/hc/en-us/articles/4408843771546).

This article includes the following reasons why there might be discrepancies between the
Talk Live calls and the Explore live dashboard:

- [The Explore live dashboard is not yet ready](#topic_c5l_fms_znb)
- [KPI values in the Explore live dashboard don't match the Talk Live calls dashboard](#topic_wbw_kms_znb)

## The Explore live dashboard is not yet ready

When you first activate Explore Enterprise, it might take up to eight hours before
Talk live dashboard widgets begin to display information. While you wait, the
message "Your live data is almost ready. Check back soon." is displayed in the
widget as shown below:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_explore_dashboard_disc_1.png)

Once the data is available, the live widgets will start showing the correct
information.

## KPI values in the Explore live dashboard don't match the Talk Live calls dashboard

In this section, you'll learn some of the reasons why key performance indicators (or
*KPIs*) might show different values in the Explore live dashboard and the
Talk Live calls dashboard. An example is shown in the following screenshots:

**Talk live calls dashboard**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_explore_dashboard_disc_2.png)

**Explore live dashboard**

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_explore_dashboard_disc_3.png)

The reasons you might see discrepancies include:

- [Agents online differences](#topic_owx_dlm_14b)
- [Average wait time and longest wait time differences](#topic_qtn_2lm_14b)
- [Filtering discrepancies](#topic_ln4_2lm_14b)
- [Explore live dashboard refresh rate](#topic_ufp_2lm_14b)

### Agents online differences

In the Explore live dashboard, the **Agents online** KPI displays
only the agents who are in the Online status (either on a call or not).

In the Talk Live calls dashboard, the **agents online** KPI
additionally includes agents in the Away status.

### Average wait time and longest wait time differences

Talk wait times displayed in the Explore live dashboard are calculated
based on events sent from Talk about queued calls. When a call enters the queue,
and the event is received, Explore begins a timer to record how long calls are
waiting. When the call is answered by an agent, or leaves the queue, Explore
stops the timer. The average and longest wait time values are calculated from
these timers. Because of these calculations, there may be a slight delay in the
values when compared to the Talk Live calls dashboard which refreshes
approximately every five minutes.

### Filtering discrepancies

The Talk Live calls dashboard can be filtered by phone number (also
known as a *line*) while the Explore live dashboard can be filtered by
group. This might produce different values for KPIs depending on how the
customer account is configured.

### Explore live dashboard refresh rate

The Talk section of the Explore live dashboard refreshes every ten
seconds, while the dashboard tab is active in your browser. When the tab is not
active in the browser (for example if you're looking at a different web page)
the refresh rate is slowed to improve performance by not refreshing dashboards
that are not being viewed.

When you return to the tab displaying the dashboard, the refresh rate
returns to ten seconds.