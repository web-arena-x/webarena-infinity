# About the forecast vs actual report (EAP)

Source: https://support.zendesk.com/hc/en-us/articles/6443331729306-About-the-forecast-vs-actual-report-EAP

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

This feature is currently in an Early Access Program (EAP). You can [sign up for the EAP here](https://docs.google.com/forms/d/e/1FAIpQLSdG7v4i3bXiIuvXPndOIV9vyzhPXwl5d5kokF8qRWis41u_sw/viewform).

The forecast vs actual report displays the forecasted data compared to the actual data for Inbound Volume, Staffing, Average Handle Time, and Service Levels.

In the forecast vs actual report, you can also navigate to the past and future dates. However, note that future dates don't display actuals, average handle time, and service level data.

This article contains the following topics:

- [Accessing the report](#h_01HCD9KCCV7V2VNC9VYS80NXJV)
- [Understanding the forecast vs actual report](#h_01HCDEKD4R2FSR4Z534B8CE7AS)

## Accessing the report

**To access the forecast vs actual report**

- Hover over the agent activity folder icon in the navigation bar, then click **Forecast vs Actual**.  
  Alternatively, you can press **cmd** (or **ctrl**)+**K** and then enter **forecast vs actual** in the window that opens.

### Sorting, filtering, and exporting the report

By default, the forecast vs actual report displays comparison data for all workstreams by the hour. You can filter the report by workstreams by clicking the sort icon in the upper-left.

When you've selected the workstreams you want to see, you can then sort the data by the hour down to every 15 minutes.

You can also generate a CSV export of this report. Click **Export CSV** to generate an export of the selected date.

## Understanding the forecast vs actual report

The forecast vs actual report contains four sections:

- Inbound Volume
- Staffing
- Average Handle Time
- Service Level

### Inbound Volume

Forecast shows historical data which was used to generate the forecast. This volume is based on the current workstream parameters. Unlike Forecast, the Actual column in the S vs A shows the historical volume of the workstream based on parameters of workstream at that point in time (called "as was").

For example, if you change a workstream's tags, Actuals displays the inbound volume associated with the original tags up to the point of change. However, the Forecast page for the same previous month shows the volume using the new set of tags. This results in different values. If you don't change the workstream after its creation, the historical volume in Forecast matches the Actuals on S vs A.

- **Forecast** - The forecast column calculates the volume based on the entirety of the available forecast data depending on how much available data you have in your account. This means it can be a minimum of 30 days or a maximum of 2 years.
- **Short Term Forecast** - The short term forecast re-calculates the volume based on the actuals of the last 24 hours of data only to give a close up "short term" updated view of the forecast.
- **Actual** - This shows the actual volume received on each workstream. We count each time a ticket matches a workstream, meaning that the same ticket might be counted more than once if it changes workstreams. Example:   
  - Ticket #111 is assigned to workstream Tier 1 is counted as 1 inbound ticket for workstream Tier 1.
  - Ticket #111 conditions are changed and now matches workstream Tier 2 is counted as 1 inbound ticket for workstream Tier 2.
  - Ticket #111 is updated again and the condition matches workstream Tier 1, it is counted 1 again as inbound ticket for workstream Tier 1.
- **SvA Net** - This shows the difference from the actual volume and the short term forecasted volume.

### Staffing

- **Required** - This is the required number of FTEs to meet the forecasted volume. This is generated based off the staffing parameters set.
- **Scheduled** - This shows how many FTEs are scheduled.
- **Actual** - This shows how many scheduled were actually in attendance.
- **RvA Net** - This shows the difference in the actual vs required FTEs.

### Average Handle Time

- **Forecasted** - The forecasted AHT for the specified interval.
- **Actual** - The actual AHT that happened for that interval.

### Service Level

The Service Level data is taken directly from Zendesk and depends on the SLA policies set in your account.

- **Actual** - This is the actual Service Level for each interval.
- **Met** -This is the # of tickets that met SLA.
- **Missed** - This is the # of tickets that missed SLA.

**Note:**  SLA data doesn't appear for Voice workstreams.