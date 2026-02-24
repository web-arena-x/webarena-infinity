# Tracking customer actions with messaging goals

Source: https://support.zendesk.com/hc/en-us/articles/9435878261402-Tracking-customer-actions-with-messaging-goals

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Verified AI summary ◀▼

Track customer actions with messaging goals to monitor specific user activities and agent performance. Assign goals to agent groups, view goal conversions in Agent Workspace, and manage them via the Messaging goals page. Set conditions, attribution periods, and track up to 15 active goals. Export conversion data to CSV for detailed insights, helping you optimize support interactions and measure success.

You can create messaging goals to track specific customer actions. Goals can be assigned
to agent groups, allowing you to track which conversations lead to a completed goal (or
“goal conversion”), and see how often each agent is responsible for driving the action.
Additionally, agents can see goal conversion events in Agent Workspace.

This article includes the following topics:

- [About messaging goals](#topic_q5h_3wx_bgc)
- [The Messaging goals page](#topic_ncd_3wx_bgc)
- [Creating and editing goals](#topic_t2y_hwx_bgc)
- [Activating, deactivating, and deleting goals](#topic_ngs_hwx_bgc)
- [Viewing and monitoring goal conversions](#topic_u5j_hwx_bgc)
- [Viewing goal conversions in Agent Workspace](#topic_jkd_hwx_bgc)

## About messaging goals

Messaging goals are available on all accounts that use messaging and don’t need to be
turned on by an admin. You can track customer goals in the Web Widget, iOS SDK,
Android SDK, and social messaging channels. Currently, goals are not available for
third-party bot channels, Unity SDK, or AI agents.

This feature introduces terminology you may be unfamiliar with, including:

- **Goal**: A specific action you want an end user to perform during or
  after a messaging conversation with an agent. For example, an end user
  making a purchase.
- **Goal conversion**: The event when an end user meets a goal.
- **Attribution period**: The period during which an agent can earn credit
  for a goal conversion.
- **First touch** and **Last touch**: A [goal configuration option](#topic_t2y_hwx_bgc) used to determine which
  agent gets [credit for the goal
  conversion](#topic_jjb_qxx_bgc).

### Crediting agents for goal conversions

Agents are are credited for goal conversions based on several
factors, including whether the [conversation is active or
inactive](https://support.zendesk.com/hc/en-us/articles/7043034053658#topic_d1b_hpz_1bc) at the time of the conversion, conversation
assignment or interaction, and whether the interaction occurs within the
attribution period.

In **active conversations**:

- **First touch**: When goal conversion credit is set
  to First touch, the agent receives credit for a conversion
  simply by being the first agent assigned to the ticket.
- **Last touch**: When the goal conversion credit is
  set to Last touch, the agent receives credit for a conversion if
  they are the agent assigned to the ticket at the time of the
  conversion.
- **Attribution period**: Does not apply to active
  conversations.

  Note: This is a temporary limitation for goal
  conversions.

In **inactive conversations**:

- **First touch**: When goal conversion credit is set
  to First touch, the agent receives credit for a conversion if
  they are the first agent assigned to the ticket, *and* they
  have sent a message within the Attribution period. Only the
  first agent assigned to the ticket is eligible for conversion
  credit.
- **Last touch**: When the goal conversion credit is
  set to Last touch, the agent receives credit for a conversion if
  they are the agent assigned to the ticket at the time of the
  conversion, and they have sent a message within the Attribution
  period.
- **Attribution period**: Determined by the admin-defined setting
  in the [goal
  configuration](#topic_t2y_hwx_bgc), it is the period counting back from the goal
  conversion event. For both First and Last touch, the agent must send a
  message in the conversation during the attribution period to receive credit.
  For example, if the Attribution period is 7 days, the agent must have sent a
  message to the end user in the conversation in the seven days *before*
  the goal conversion event.

### Limitations

Currently, the following limitations apply to messaging
goals:

- An account can have a maximum of 15 active goals at a
  time. The number of inactive goals isn’t restricted. However,
  goals that have ended will remain active and count against your
  active goal limit until they are [deactivated or deleted](#topic_ngs_hwx_bgc).
- Each goal can include up to 100 URL conditions.
- The set attribution period does not apply to goal
  conversions that occur during [active messaging
  conversations](https://support.zendesk.com/hc/en-us/articles/7043034053658#topic_d1b_hpz_1bc), but does apply to goal conversions
  that occur during inactive messaging conversations.

## The Messaging goals page

The Messaging goals page in Admin Center is the hub for managing and
tracking goals.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/messaging_goals_page.png)

From here you can:

- Create and edit goals
- Activate, deactivate, and delete goals
- Email yourself a CSV of goal information

**To view the Messaging goals page**

- The goals list includes columns with the following information:

  - **Name**: The name of the goal.
  - **Groups**: The groups assigned to the goal.
  - **Status**: Whether the goal is Active, Inactive, Ended, or how many
    days (up to five) remain before the goal ends.
  - **Start date**: The date you’ll begin tracking the goal.
  - **End date**: The date you’ll stop tracking the goal.
  - **7 day conversion**: The number of goal conversions achieved in the
    most recent seven-day period.

## Creating and editing goals

On the Messaging goals page, you can create a goal to track end-user activity.

**To create a goal**

2. Click **Create goal**.
3. Fill out the following fields:

   - **Name** (required): A short, descriptive name
     for the goal.
   - **Description**: A slightly more detailed
     description of the goal’s purpose.
   - **Activate goal**: Click to activate the goal
     upon saving it. You can have up to 15 active goals at a
     time. A goal can be active outside of the start and end
     dates configured below. Note that an active goal will not be
     tracked until its start date.
   - **Start date** (required): Enter or select the
     date you want to start tracking the goal. This field only
     appears if you have activated the goal. You can’t edit the
     start date retroactively.
   - **End date**: Enter or select the date you want
     to stop tracking the goal. Leave this field blank if you
     want to track the goal indefinitely, or have not decided on
     an end date. This field only appears if you have activated
     the goal.
   - **Assign to agent groups** (required): Use the
     dropdown to select one or more [groups](https://support.zendesk.com/hc/en-us/articles/4408839035546) to
     track. Only groups selected here will have their
     interactions included in the count.
   - **Attribution** (required): Define when credit is given for
     the goal conversion.

     - **Last Touch** assigns credit for a goal
       conversion to the agent assigned to the ticket at
       the time of the conversion.
     - **First Touch** assigns credit for a goal
       conversion to the first agent assigned to the
       ticket.
   - **Attribution time period in days** (required): The number of
     days within which agent interactions are considered for
     attribution.
   - **Transaction value**: Transaction value of the goal
     conversion. For example, if the conversion has a monetary value,
     enter that value here.
   - **Conditions** (required): Define the conditions that must be
     met for a goal conversion to be counted:

     - Category: URL
     - Operator: Select *Contains* to
       define a partial URL, or *Is* for an exact
       match
     - Value: Enter a partial or complete URL
4. Click **Save**.

You can edit a goal if you need to update its configuration.

**To edit a goal**

2. Click the goal name.
3. On the goal’s configuration page, edit the settings as needed.
4. Click **Save**.

## Activating, deactivating, and deleting goals

You can activate, deactivate, and delete goals as needed to manage when and
if they’ll be tracked. Active goals are tracked between the configured start and end
dates. Inactive goals aren't tracked.

Note: All active goals are counted towards your
15-active-goal limit, including goals that have ended. You must deactivate or
delete a goal to exclude it from the active goal count.

**To activate a goal**

2. Click the goal’s **Options menu** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) and select **Activate
   goal**.

**To deactivate a goal**

2. Click the goal’s **Options menu** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) and select
   **Deactivate goal**

**To delete a goal**

2. Click the goal’s **Options menu** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) and select **Delete
   goal**. *This action can’t be undone.*

## Viewing and monitoring goal conversions

After you create your messaging goals, you can email a CSV to yourself with data
about goal conversions. Data is captured hourly, so the CSV may not include
information from the most recent 60-minute period.

**To email a CSV of goal conversion data**

2. Click the goal’s **Options menu** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) and select Email
   CSV.
3. Choose a date range for the data included in the CSV file.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/goals_date_range.png)
4. Click **Email CSV**.

   A link is sent to your email address, including a
   link to a downloadable .zip file containing the CSV. The link is valid
   for 14 days.
5. Download and open the .zip file, then open the CSV.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/goal_conversion_csv_ex.png)

The CSV includes the following information related to each goal conversion completed
in the selected date range:

- **Timestamp**: The time the event occurred
- **Goal ID**: The system-generated ID for the goal
- **Goal name**: The assigned name in the goal
  configuration
- **Agent ID**: The agent’s user ID.
- **Agent name**: The name of the agent assigned the goal at
  the time of the conversion
- **Agent email**: Email of the agent assigned the goal at the
  time of the conversion
- **Ticket ID**: ID number of the related Support ticket.
- **Total transaction value**: Transaction value included in
  the goal configuration.
- **Satisfaction score**: The [CSAT rating](https://support.zendesk.com/hc/en-us/articles/4408886173338) submitted by the end
  user. If you aren’t collecting CSAT ratings, or if the end user did not
  submit a rating, the value in this column will be “Unoffered.”
- **Contact duration to goal**: Period from the attributed
  agent’s ticket assignment and the goal conversion.

## Viewing goal conversions in Agent Workspace

When a customer completes a goal, the event is displayed in the conversation history
in Agent Workspace.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/goals_event_AW.png)