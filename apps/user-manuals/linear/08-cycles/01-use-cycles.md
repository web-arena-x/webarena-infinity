# Cycles

Cycles are a practice to keep up your team's momentum, similar to commonly used agile flavored sprints.

![Image showcasing Cycle Details including percentage success, total effort, number of days ago and a chart showing effort and scope over time.](https://webassets.linear.app/images/ornj730p/production/d9c776ab4f3b38a56b22df4974c8719edc5557fb-1052x584.png?q=95&auto=format&dpr=2)

Cycles are time-boxed periods where a team works on completing a pre-defined set of work. When enabled, Linear automatically creates upcoming cycles for your team. Unlike sprints, cycles are not tied to releases. 

## Configure

Configure cycles under **Team Settings > Cycles.** Turn on the toggle for **Enable cycles**. Required settings will show up in the cycle setting flow with defaults. You can always edit cycle configurations in the future.

---

## Cycle settings

![Cycle settings](https://webassets.linear.app/images/ornj730p/production/2b6e55ce2413893807c7aef369f2a42a151deddd-1446x958.png?q=95&auto=format&dpr=2)

### Cycle duration

In the **Each cycle lasts** field, select the number of weeks you want each cycle to last. Cycles can last anywhere from 1-8 weeks. It is not possible to create cycles with different durations or to start or end on specific dates. The goal of cycles having repeated intervals is to help you avoid the busywork associated with optimizing cycle timing and instead focus on shipping.

### Cooldowns after each cycle

Including a cooldown period after each cycle to give your team a break and bandwidth to work through technical debt and other planning functions. Issues cannot be assigned to a cooldown.

### Starting day of the week

Since cycles occur in regular intervals, you'll choose a specific day of the week for your cycles to start. Cycles begin at 12:01 AM on the chosen day based on the timezone configured in **Team Settings > General**.

### Upcoming cycles

Select the number of future cycles to create so your team can assign issues to future cycles. The maximum number of futures that can be created is 15.

### Disable cycles

When disabling the Cycles feature, the current cycle will be marked as completed and upcoming cycles will be removed. Any completed cycle data will be preserved for reference. You can choose to reenable cycles at any stage in the future.

---

## Adjust cycles

### Move start and end dates

In cases where a future cycle should deviate from the schedule, its start and end dates may be moved through the overflow menu on that cycle.

![Adjust cycle dates](https://webassets.linear.app/images/ornj730p/production/a2fa4432d04b938961fb56cb83004878a0ecc904-1840x358.png?q=95&auto=format&dpr=2)

Past cycle dates cannot be changed, but you can end your current cycle at the end of the current day if needed.

### Start a cycle today

In some cases your team may wish to start a future cycle today instead of waiting for a future date. Take this action through the upcoming cycle's overflow menu.

* This action starts the upcoming cycle at 00:00 on the current day, per your team's timezone setting. Only the upcoming cycle can be started today.
* If the current cycle is active when we execute this action, we immediately complete it and roll issues over to the newly started cycle. If there is no currently active cycle, we act like cooldown has now ended for the previous cycle. If your current cycle also started today, you may not start the upcoming cycle today as well.

## Cycle automations

### Issues rollover

Cycles run on an automated schedule to reduce unnecessary date math and help create routine. Any unfinished work rolls over to the next cycle automatically. There is no way to keep unfinished issues in a closed cycle. If you forget to update an issue before the cycle ends, completed issues can still be moved over to the previous cycle.

### Auto-add active issues to current cycle

![Cycle automations](https://webassets.linear.app/images/ornj730p/production/225303175bf39059797fec985a1a0115553992de-1412x570.png?q=95&auto=format&dpr=2)

Auto-adding issues to a cycle helps to ensure all your work is captured by a cycle. You have the option to auto-add any _Active_, _Started_, or _Completed_ issues that do not have a cycle assigned into the current cycle. If the current cycle is in cooldown, the issues will be added to the following cycle.

When toggling on **Active issues** option, an option will appear allowing you to

* Move existing active issues that are not assigned to a cycle to **Move to Backlog** (change it's status), or
* **Keep in Active** and put it into the current or next cycle (depending on cooldown settings).

An active status is a status in the "Unstarted" and "Started" category.

## Cycle calendars

Keep up with your Linear cycles in your preferred calendar application by visiting your team's Cycles page, click on the overflow menu on a cycle, and hover over **Subscribe to cycle calendar**_._ Choose to add to Google Calendar, copy a feed URL, or download the calendar as an .ics file.

## Cycle capacity

On the Cycles view, cycles that have not yet started will display a capacity dial that shows an estimate on whether your team will be likely to complete all the issues added to the cycle. 
 
Capacity is calculated from the velocity of the previous three completed cycles, i.e. the number of issues or estimate points completed in these cycles. If the team has not completed any cycles previously, capacity will be roughly estimated from the number of members in the team. 

## FAQ

<details>
<summary>How do I start using Cycles now when my team is mid-cycle already?</summary>
We recommend creating a cycle starting today, and then setting further cycles to your regular cadence.

To do so, turn on Cycles in Settings > Team > Cycles. Choose today as your start date, which will create your current cycle. Then, edit the date field again to choose when your _next_ cycle should start. This way, you'll create a cycle to reflect your work for the rest of the current cycle, but have your desired cycle cadence reflected moving forwards.
</details>

<details>
<summary>Can I align cycles between multiple teams?</summary>
Yes, [sub-teams](https://linear.app/docs/sub-teams) inherit the cycle schedule of their parent team. When you designate an existing team as a sub-team, its past cycles remain untouched but future cycles update to match the closest parent cycles.
</details>
