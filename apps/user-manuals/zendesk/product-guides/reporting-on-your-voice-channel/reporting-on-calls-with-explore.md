# Reporting on calls with Explore

Source: https://support.zendesk.com/hc/en-us/articles/4408885612314-Reporting-on-calls-with-Explore

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Professional or Enterprise |

When you run a call center using Zendesk, useful call information is recorded about your efficiency and productivity. Zendesk Explore helps you surface this important business information in easy-to-read reports and dashboards.

In this article, you'll learn the basics of what makes up a call, how to access your call information in Explore, and some of the most common metrics you can measure.

If you're new to Explore and want more help, see [Getting started with Explore](https://support.zendesk.com/hc/en-us/articles/4408831710618).

This article contains the following topics:

- [Understanding the flow of a call](#topic_bcq_rd5_yjb)
- [Understanding call legs](#topic_utw_qd5_yjb)
- [Understanding key Explore metrics for Talk](#topic_l3j_cy5_yjb)
- [Creating an Explore report](#topic_zpl_1y5_yjb)

## Understanding the flow of a call

To produce effective reports, it helps to understand the high-level flow of a call. A simple incoming call might look like this:

![Call diagram](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_call_diagram.png)

In addition to the basic flow, the following applies:

- If the agent declines or doesn't pick up the call, their call leg time ends.
- If the agent calls a second agent to consult, a new call leg starts for the second agent.
- Once the first agent transfers the call to another agent, then the first agent call leg ends.
- An agent's call leg is not complete until they complete their wrap-up time (if configured).

## Understanding call legs

A common term you'll hear is *call leg*. A call leg is defined as an interaction between a person and the call.

Call legs fall into one of two types:

- **Agent:** Begins when an available agent is found and the agent's phone (or browser) starts to ring. The call leg ends after one of the following events:
  - The agent declines the call.
  - The agent completes the call. The leg ends after any configured wrap-up time for the call.
  - The agent transfers the call to a second agent. As soon as the first agent calls the second agent, then the second agent's call leg begins. The first agent's call leg ends after the call is transferred. When calls have more than one agent leg, it's because more than one agent was a participant.
- **End user:** Begins after the call is answered and the end user hears the welcome message. The call leg ends when the call is disconnected because either the end user or the agent hung up. There can be more than one call leg for the end user (for example, a [callback request](https://support.zendesk.com/hc/en-us/articles/4408884087706) creates a second end-user call leg).

## Understanding key Explore metrics for Talk

You can access a range of prebuilt reports that display information about your calls, efficiency, and agent activity. If you need to customize these reports or create your own reports, Explore features a large number of metrics and attributes you can use.

In this section, you'll learn how to access the prebuilt reports, and discover some of the key metrics and attributes you can use to create your own reports.

### Prebuilt reports for Talk

There is a range of useful reports in prebuilt dashboards to analyze your call activity. Before creating custom reports, check to see if the report you want is already available.

**To access the Talk dashboard**

1. In Explore, click the **Dashboard** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) icon in the left sidebar.
2. From the list of dashboards, select the **Zendesk Talk** dashboard.

![A section of the Talk prebuilt dashboard](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk-dashboard.png)

For information about all of the reports on the dashboard, see [Analyzing your Talk activity](https://support.zendesk.com/hc/en-us/articles/4408836253338).

### Key metrics and attributes for creating your own Talk reports

If you need a report that doesn't exist in the prebuilt dashboard and you're using on a Professional or Enterprise plan, you can often create your reports. You create reports by adding metrics, which are *quantitative* values like the number of tickets, and attributes, which are *qualitative* values like ticket assignee. See [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530).

In this topic, you'll learn about some of the most common metrics and attributes you can use to analyze your call center. The following tables detail some of the key metrics and attributes you can use, and where to find the details.

- [Key call metrics](#topic_odz_rxj_jkb)
- [Key call attributes](#topic_gdh_sxj_jkb)
- [Key call leg metrics](#topic_xxh_sxj_jkb)
- [Key call leg attributes](#topic_xm3_sxj_jkb)

Tip: Don't use call-level metrics or attributes together with leg-level metrics or attributes within the same report. If you do, the call-level metrics are multiplied by the number of legs in the call, skewing your results.

### Key call metrics

The table below defines the key metrics for calls.

| Call metric | Definition |
| --- | --- |
| **Call wait time** | The time a customer waited to talk to an agent after being routed to where they want. |
| **Call answer time** | The time between the customer first connecting to the system and the first conference with an agent. Repetition, such as waiting after a transfer occurs, is not included. Voicemails are also excluded from this number. |
| **Call IVR time** | The time spent in an IVR. |
| **Call consultation time** | The total consultation time. Sums the value of any number of agent-to-agent consultations. |
| **IVR transitions** | The number of steps taken through the IVR menu. |
| **Call billed time** | The time that the call was billed for. |
| **Call on-hold time** | The time a call was on-hold from the customer’s perspective |
| **Call talk time** | The time spent talking from the customer’s perspective or the time spent in a conference with an agent. If the call was transferred this will include all agent conferences with the customer. |

### Key call attributes

The table below defines the available call attributes.

| Call attribute | Definition |
| --- | --- |
| **Call ID** | The ID number associated with the call. |
| **Call type** | The type of call. Values are **Callback, Forwarded, Overflow, Regular, Text back,** and **Voicemail**. |
| **Call completion status** | The completion status of the call. Shows whether a call was completed by an agent or to voicemail or whether it was abandoned before that could happen. |
| **Call direction** | Whether the call was inbound or outbound. |
| **Call exceeded queue wait time** | Indicates if the customer exceeded the set time limit waiting for the agent in the queue. |
| **Call outside business hours** | Indicates if call was outside of business hours (true/false). Business hours might vary depending on what schedule(s) have been set. For more information on setting up schedules, see [Setting your business hours and holidays](https://support.zendesk.com/hc/en-us/articles/4408842938522-Setting-your-business-hours-and-holidays-Plus-and-Enterprise-). |
| **Call Talk number** | The Zendesk phone number the call came in through. |
| **Call IVR destination group** | The destination group for calls coming out of an IVR. |
| **Caller with requested voicemail** | Indicates if the caller requested to be put through to voicemail. |
| **Call IVR action** | The last IVR action the end-user selected. Values are **Group, Invalid keypress, IVR menu, Phone number, Text back,** and **Voicemail.** |

### Key call leg metrics

The table below defines the available call leg facts.

| Call leg metric | Definition |
| --- | --- |
| **Leg duration** | The duration of the call from beginning to end of that call leg. |
| **Leg wrap-up time** | The total wrap-up time in seconds associated with the agent’s call leg. Customer legs will default to 0 seconds. |
| **Leg talk time** | The time spent talking, specific to call legs. |

### Key call leg attributes

The table below defines the available call leg attributes.

| Call leg attribute | Definition |
| --- | --- |
| **Leg type** | Indicates for which user the call leg was generated. Values are **Agent, End-user,** and **External.** |
| **Leg agent name** | The agent name associated with a specified call leg. If looking at an entire call, this attribute will include all agents that had legs associated with the call. An empty value indicates the call leg is a customer call leg. |
| **Leg ID** | The call leg ID. |
| **Leg agent available via** | Whether the agent answered via browser or phone. |
| **Leg completion status** | Displays whether an agent declined an incoming call, if an agent missed the prompt to accept the incoming call, or if the agent accepted it. |
| **Leg agent forwarding number** | The number a call was routed to if a call leg is associated with call forwarding. |
| **Leg instance** | The order the call leg began in reference to the overall call. Customer legs come first, so each call begins with a value of one. Each additional agent leg that occurs on the call increments this value by one. |
| **Leg user type** | The type of call leg, either agent or customer. |

To read about the metrics and attributes you can use to create reports, see [Metrics and attributes for Zendesk Talk](https://support.zendesk.com/hc/en-us/articles/4409156145434).

## Creating an Explore report

In this example, you'll use some of the metrics you learned above to create a basic report that, for each of your agents, shows the number of calls they made or received, the end-user name, and the completion status of the call. The report is filtered to show only calls from the current week.

**To create the report**

1. In Explore, click the Reports icon ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)).
2. In the Reports library, click **New report**.
3. On the **Select a dataset** page, choose **Talk** > **Talk - Calls** and then click **Start report**. The report builder opens.
4. In the **Metrics** panel, click **Add**.
5. From the list of metrics, choose **Calls**, then click **Apply**. Explore displays the total number of calls made or received.
6. In the **Filters** panel, click **Add**.
7. From the list of attributes, choose **Call - Date**, and then click **Apply**.
8. Click the **Call - date** filter you just added.
9. On the **Call - Date** page, click **Edit date ranges**.
10. On the **Date range** page, choose **This week**, and then click **Apply**. Explore displays the total number of calls made or received this week.

    ![Reporting example](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_reporting_example_1.png)
11. In the **Rows** panel, click **Add**.
12. From the list of attributes, choose the following:
    - **Call agent name**
    - **Call direction**
    - **End-user name**
13. When you are finished, click **Apply**. Explore displays the completed table.

    ![Report example](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_reporting_example_2.png)