# Using the Time Tracking app

Source: https://support.zendesk.com/hc/en-us/articles/4408822487450-Using-the-Time-Tracking-app

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

The Time Tracking app enables you to monitor how much time you spend on tickets.
You might see all or just some of the following options, depending on how your administrator has set up time tracking.

Every agent must do a one-time browser refresh to see the Time Tracking app after it's installed.

The app must be installed and set up by an admin. See [Setting up the Time Tracking app](https://support.zendesk.com/hc/en-us/articles/4408828227098).

This article covers the following topics:

- [Making the Time Tracking app appear after installation](#topic_csv_zcs_s4)
- [Tracking your time spent on tickets](#topic_bc2_wcs_s4)
- [Reporting on time tracking in Explore](#topic_mcq_bds_s4)

## Making the Time Tracking app appear after installation

The first time you use the Time Tracking app, do a hard refresh on your browser for it to appear.
You will only need to do this once.

**To make the Time Tracking app visible**

- Press Command + Shift + R (Mac) or Control + F5 (Windows) to refresh your browser cache.

## Tracking your time spent on tickets

**To pause and resume the timer**

- Click pause and play to pause and resume the timer as needed, such as if you still have a ticket open but are taking a break to answer an unrelated phone call.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/time-tracking-timer-controls.png)

**To reset the timer**

- Click the refresh button to reset the timer to 0.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/time-tracking-reset-current-time.png)

**To review timelogs**

- Click **Show timelogs** to review how long different agents have spent on that ticket.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/time-tracking-timelogs.png)

**To review all time tracking events on a ticket**

- In [ticket events](https://support.zendesk.com/hc/en-us/articles/4408829602970), check the Total time spent (sec)
 and Time spent last update (sec) fields for updates.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/time-tracking-app-ticket-events.png)

 If an agent submits time that matches the previously recorded time, a change event is not recorded for the Time spent last update (sec) field because the value is unchanged. Only the Total time spent (sec) field is updated to reflect the cumulative time.

**To edit the total time spent on a ticket**

- When you submit a ticket, you might see a window like the following, which allows you to edit or confirm your time:

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/time-tracking-edit-time-submission.png)

When the window appears, the timer begins counting down from 15. If you don't click **Cancel** or **Submit time** before the 15 seconds are up, it closes, and you are returned to the ticket.

## Reporting on time tracking in Explore

The Time Tracking app tracks the time spent on each ticket update and stores this with the ticket. With Explore, you can create calculated metrics that contain this information and use them to produce reports. To learn how to set up custom time tracking metrics and produce reports, see [Time Tracking app: metrics you need to be measuring](https://support.zendesk.com/hc/en-us/articles/4408825230490).

Note: When a [ticket is shared](https://support.zendesk.com/hc/en-us/articles/4408886265370-Sharing-tickets) with another account, agent updates from the receiving account still contribute to the **Total time spent** field, but won't appear in the ticket’s Events view from within the sending account. This results in a higher **Total time spent** value in Explore and API reports than what appears in the sending account’s Events view.