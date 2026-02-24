# Understanding WFM forecasting

Source: https://support.zendesk.com/hc/en-us/articles/9858048119194-Understanding-WFM-forecasting

---

This article helps you understand and interpret the Zendesk Workforce management (WFM) Forecast page.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Understand and interpret the Workforce Management (WFM) Forecast page to predict future contact volumes and staffing needs using historical data. The forecast provides inbound volume estimates and calculates Full-Time Equivalent (FTE) requirements, helping you optimize resources and meet service goals. Use the forecast to visualize expected inbound volume and required staffing across workstreams, adjusting for unique events like marketing campaigns.

This article helps you understand and interpret the Zendesk Workforce management (WFM)
Forecast page.

The forecast takes your historical data based on [workstream scenarios](https://support.zendesk.com/hc/en-us/articles/9940824842394) you've specified and creates inbound volume estimates for up to a year in the future. Full-Time Equivalent (FTE) calculations are also included, which show how many staff members are required to handle the estimated workload.

This article contains the following topics:

- [About WFM forecasting](#topic_ynn_bct_tfc)
- [Understanding inbound volume](#topic_qq1_cts_tfc)
- [Understanding required staffing](#topic_qrb_mgf_bhc)

Related articles:

- [Viewing and managing forecast scenarios](https://support.zendesk.com/hc/en-us/articles/9940824842394)
- [Viewing your active forecasts](https://support.zendesk.com/hc/en-us/articles/9940054229402)
- [Understanding WFM forecasting](https://support.zendesk.com/hc/en-us/articles/9858048119194)

## About WFM forecasting

Forecasting is the process of predicting future contact volumes and staffing needs using historical data and advanced algorithms to ensure that the right number of agents are scheduled at the right times. This helps you optimize resources and consistently meet service goals.

When you first activate Zendesk WFM, six months of your historical ticket data is migrated from Zendesk to the WFM system. This means that your initial forecast is based on the six month dataset. While the forecasting engine can use up to two years of data if it's available within WFM, longer historical data requires a manual data import [request to Zendesk support](https://support.zendesk.com/hc/en-us/articles/4408843597850).

Keep in mind that Zendesk WFM also includes spam tickets, which may be different from how you capture ticket volume in Zendesk Explore. See [Understanding suspended tickets and spam](https://support.zendesk.com/hc/en-us/articles/4408889141146).

You also have the option to import your own data into your workstream forecast. See [Importing historical volume](https://support.zendesk.com/hc/en-us/articles/6443365713946).

A minimum of one month of data is required for forecasting in Zendesk Workforce management (WFM). If you enter a date with less than one month of data, the forecast will not be generated. Additionally, the system limits the use of historical data to a maximum of two years. Any data exceeding this two-year threshold will not be factored into the forecast.

When you select a [workstream scenario](https://support.zendesk.com/hc/en-us/articles/9940824842394), Zendesk WFM begins calculating the future contact volumes and staffing needs.

Depending on the amount of historical ticket data available, it may take a moment to see the forecast for the selected workstream.

In some cases, there may not be enough collected data to display a complete forecast. In such instances, the forecast is repeated. For example, if only three months of data are available, Zendesk WFM replicates this pattern for the remainder of the year.

Use the information on the Forecast page to visualize, analyze, and manage [expected inbound volume](#topic_qq1_cts_tfc) and [required staffing](#topic_qrb_mgf_bhc) across workstreams.

## Understanding inbound volume

When your forecast is available, it's displayed on the Inbound volume chart. The inbound volume forecast is based on the [Prophet Forecasting Algorithm](https://support.zendesk.com/hc/en-us/articles/6443365725210#h_01HAQ998BYDGKY6DZQD4BGSX8B).

The Inbound volume chart indicates where the historical data ends and the forecast begins.
Each time you recalculate the forecast, the mark shifts accordingly. Each value on the line marked as a historical value represents the amount recorded until the last recalculation. If Zendesk WFM does not have the complete value for that time period (whether that is for a full day or a full week), the chart displays the values tracked to that point. This may appear as a sudden drop because the displayed values only reflect partial volumes.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_active_forecast.png)

Each workstream is represented by a color. You can view forecasts for up to 10 workstreams at a time.

Zendesk WFM calculates the inbound volume every time the ticket changes workstreams.

Use the date picker to select daily, weekly, monthly, or yearly views of the incoming workload.

Hovering over the chart intervals shows you the values of expected volumes for the selected workstreams.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_forecast_inbound_volume_hover.png)

You can also expand the chart to a table view, which can be exported. The table allows you to view the estimated incoming volumes and the values for each workstream based on the selected interval option. See [Viewing your active forecasts](https://support.zendesk.com/hc/en-us/articles/9940054229402).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_forecast_inboundvolume_expand_table.png)

Forecast allows you to adjust your expected volumes based on unique events, such as marketing campaigns or feature sunsets. See [Viewing and managing forecast scenarios](https://support.zendesk.com/hc/en-us/articles/9940824842394).

## Understanding required staffing

Based on the forecast scenario, Zendesk WFM calculates the staff count needed to handle the expected workload in the Required staffing chart. Colors represent the selected workstreams and you'll see the required staffing values when you hover over the chart.

The chart shows the projected required staffing count for upcoming dates.
Historical required staffing calculations aren't stored.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_forecast_required_staffing_chart.png)

Full-Time Equivalent (FTE) represents a standardized unit of measurement that reflects the number of hours worked by a typical full-time employee.

The baseline to qualify as 1.0 unit of FTE is defined by the amount of weekly working hours. Typically, this is set at 40 hours, so a part-time employee who works 20 hours is considered a 0.5 FTE.

The Required staffing table displays the calculated FTEs needed for each 15-minute interval based on a modified version of [Erlang C](https://www.callcentrehelper.com/erlang-c-formula-example-121281.htm). This is a mathematical model used in WFM to estimate the number of agents (FTEs) required to handle a given workload while maintaining a specific SLA. It's widely used in call centers and contact centers for staffing calculations.

Required staffing takes into account the following parameters:

- **[Channel](#topic_zrb_mgf_bhc)**: The volume of calls, emails, or chats.
- **[Occupancy](#topic_bsb_mgf_bhc)**: The time spent on work-related activities in seconds.
- **[Duration](https://support.zendesk.com/hc/en-us/articles/8203054518298#topic_ur1_w3b_ldc)**: The average duration of your chats.
- **[Concurrency](#topic_fsb_mgf_bhc)**: Max number of simultaneous active chats.
- **[Average Handling Time (AHT)](#topic_dsb_mgf_bhc)**:
 The average handle time for your tickets in seconds.
- **[First Response Time](#topic_hsb_mgf_bhc)**: How long it takes for your agents to give a first reply (SLA %).
- **[Wait time](https://support.zendesk.com/hc/en-us/articles/8203054518298#topic_kvb_w3b_ldc)**: The average waiting time for your chats
- **[Shrinkage](#topic_jsb_mgf_bhc)**: Time spent on non-work related activities.
- **[Minimum staffing](#topic_msb_mgf_bhc)**: Minimum number of people scheduled to work.
- **[Availability](#topic_nsb_mgf_bhc)**: Defines when your agents need to work on this workstream. It usually matches the operational hours of your locations.

Consider the following example:

- Volume = 38 emails/day
- In a period of minutes = 24h period = 24\*60s= 1440s
- Average Handling Time = 210s (3:30min)
- Required Service Level % = Target = 50%
- Target Answer Time = FRT = 5h30 = 19600s
- Maximum Occupancy = 90%
- Shrinkage = 30%

This leads to a value of 1.5 agents per day, considering an FTE is:

```
8h/day >> 1,5*8 = 12h of work
```

In general it can be defined as:

```
Total Hours Worked by Part-Time and Full-Time Employees ÷ Number of Available Full-Time Hours in Year
```

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/WFM_FTE.png)

You can also expand the chart to a table view which can be exported.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_forecast_requiredstaffing_table.png)

When Zendesk WFM calculates required staffing, Zendesk business hours aren't taken into account. Instead, the staffing requirements based on the historical times of incoming volumes are displayed so you can consider business hours adjustments if needed. For the day and week view, the staffing requirements value reflects the maximum FTE value attained on that time interval. For the month and year view, it's the sum of the required hours.

Values are calculated as follows:

- **Day View:** 15-minutes intervals.
- **Week View:** 1-hour intervals. The maximum number of people required in the four 15-minute intervals that fit into the hour in question.

 For example:

 - 3:00-3:15> 2 FTE
 - 3:15-3:30> 5 FTE
 - 3:30-3:45> 3 FTE
 - 3:45-4:00> 2 FTE
 - >> Total = 5 FTE between 3:00-4:00.
- **Month view:** 24-hours (1day). Hours of work instead of FTEs. This number is the result of a direct relation between the number of people set as available and hours in the day.

 For example:

 - From 3:00-4:00 >> 5 FTEs (working 1h each) >> 5h of work
 - Same calculation for all hours in the day
 - The sum of all 24 intervals provides the number displayed in the **Totals** row for each day.
- **Year view:** It’s the sum of the 7 days in the week, also expressed as “hours of work”. It's calculated in the same way as the total for 1 day.

You can modify your required staffing parameters. See [Setting up WFM forecasting](https://support.zendesk.com/hc/en-us/articles/6443407875354).

### Channel types

Zendesk WFM offers three channel types: Voice, Email and Chat.

The major difference between them relates to the redistribution of the inbound volume captured outside of business hours:

- **Voice and Chat**: Tickets outside of opening hours are not distributed in the first hours of availability since these are synchronous channels.
- **Email**: Tickets outside of opening hours are re-distributed in the first 15-minute interval, since this is an asynchronous channel. To avoid high requirements for just the first 15 minutes, we redistribute those values over the period of First Response Time. For example, if the First Response Time (FRT) is 4 hours, we redistribute the requirements over those 4 hours.

### Occupancy

Occupancy directly impacts how efficiently agents are utilized:

- **Higher Occupancy → Fewer FTEs**: This indicates that agents spend more time handling calls, emails, and chats, and less time idle. As a result, fewer FTEs are needed to manage the estimated inbound volume.
- **Lower Occupancy → More FTEs**: This indicates that agents have more idle time, necessitating a larger workforce to handle the same workload.

### Average Handling Time (AHT)

Determines how much time an agent spends per interaction:

- **Higher AHT → More FTEs**: Each agent handles fewer interactions per hour, resulting in a need for more FTEs.
- **Lower AHT → Fewer FTEs**: Each agent can handle more interactions per hour, leading to a requirement for fewer FTEs.

It's represented as follows:

```
hh:mm:ss
```

The value is then translated to total seconds to be used in the formula.

```
Total H.T will be equal to: Call Volume × AHT
```

### Concurrency

This parameter applies only to chat tickets and indicates how many simultaneous chats agents can handle. It directly impacts FTE calculation, as it increases agent productivity and reduces staffing needs:

- **Higher Concurrency → Fewer FTEs:** Agents handle multiple interactions simultaneously, which increases productivity and decreases the number of FTEs required.
- **Lower Concurrency → More FTEs:** Agents handle only one interaction at a time (as in voice calls). With the total workload unchanged, this leads to a requirement for more FTEs.

### Service Level Agreement (SLA)

[SLA](https://support.zendesk.com/hc/en-us/articles/5600997516058) is a key performance metric in contact centers that defines the percentage of tickets answered within a specific time threshold. It directly impacts FTE estimation because it determines how quickly tickets must be handled, which influences staffing needs:

- **Stricter SLA (Higher Target) → More FTEs:** When the SLA target increases (for example, from 70% in 30 seconds to 90% in 20 seconds), more agents are needed to ensure a higher percentage of calls are answered quickly. A stricter SLA reduces the allowable wait time, increasing the need for available agents at all times.
- **Relaxed SLA (Lower Target) → Fewer FTEs:** A relaxed SLA allows for better agent utilization (higher occupancy) and reduces staffing costs (for example, from 90% in 20 seconds to 70% in 30 seconds).

 In Zendesk WFM this is set by the following parameters:

 ```
 Speed of answer / First Response Time / Wait time
 ```

 Represented in:

 ```
 hh:mm:ss
 ```

### Shrinkage

Shrinkage accounts for the paid agent time that is not spent handling customer interactions. This parameter is included in the FTE calculation as the difference between Net and Gross FTE, where:

- **Net FTE**: The number of agents needed to handle interactions (Available Hours).
- **Gross FTE**: The number of agents scheduled after accounting for In and Out of Office Shrinkage.

Impact of Shrinkage on FTEs:

- **Lower Shrinkage → Fewer FTEs**: A higher percentage of scheduled agents actively handle interactions, reducing overall staffing needs.
- **Higher Shrinkage → More FTEs**: Fewer agents are available at any given time, necessitating more total agents to meet demand.

For example, if you need 100 productive agents and the shrinkage is 40%, you actually need 167 agents to account for the time lost due to auxiliary time and out-of-office shrinkage.

### Minimum Staffing

Minimum Staffing can be defined as the minimum number of people scheduled to work. The default value for Zendesk WFM is 1 FTE.

This parameter does not influence the formula for FTEs but affects their distribution throughout the available hours. This indicates to the system that you want to schedule at least one FTE for every hour of work.

### Availability

This parameter allows you to define the time period during which agents can work on the workstream. Tickets will be distributed according to the defined time periods. It's not the same as the working hours of the location but rather the time frame in which WFM projects agents will be scheduled to work on this workstream.

For example, if the location working hours are set to Monday through Friday, from 8:00 AM to 6:00 PM, where agents handle calls from region A from 8:00 AM to 1:00 PM and from region B from 1:00 PM to 6:00 PM.:

- Workstream A availability will be Monday through Friday, from 8:00 AM to 1:00 PM.
- Workstream B availability will be Monday through Friday, from 1:00 PM to 6:00 PM.

The timezone you select adjusts the hourly blocks based on your timezone. For example, if you are in GMT+1 and set availability for Monday to Friday from 8:00 AM to 6:00 PM in GMT+2, you'll see FTEs calculated from 7:00 AM to 5:00 PM. This is because when it's 8:00 AM in GMT+2, it's still 7:00 AM for you (one hour behind the set availability).

Availability is switched off by default in Zendesk WFM, which means that the distribution of tickets occurs over 24 hours, 7 days a week, based on the periods when tickets are received.