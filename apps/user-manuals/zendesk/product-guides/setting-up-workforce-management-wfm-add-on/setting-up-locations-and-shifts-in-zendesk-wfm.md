# Setting up locations and shifts in Zendesk WFM

Source: https://support.zendesk.com/hc/en-us/articles/6443345205402-Setting-up-locations-and-shifts-in-Zendesk-WFM

---

Locations are part of your organizational structure and are used to group agents who share the same geographic location. You can also use locations to split teams in the same physical location that have different shifts and scheduling rules. For example, you might create two San Francisco locations: one for part-time agents and one for full-time agents.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Set up locations and shifts to organize agents by geographic location and manage their schedules. Create automatic shifts based on forecasted needs or fixed shifts with specific start times. Use rotation periods to vary shift start times and organize shifts in folders for easy management. Manage locations by editing or deleting them as needed.

Locations are part of your organizational structure and are used to group agents who share
the same geographic location. You can also use locations to split teams in the same physical
location that have different shifts and scheduling rules. For example, you might create two
San Francisco locations: one for part-time agents and one for full-time agents.

You’ll define your operational hours and create shifts that apply to agents’ schedules in the
locations you add.

When setting up a location’s shifts, you can create either automatic shifts, where forecasted
requirements determine the shifts’ days and hours, or fixed shifts, where managers have more
control.

This article contains the following topics:

- [Accessing the Locations page](#topic_slm_4k4_zzb)
- [Adding a location](#topic_wf4_yl4_zzb)
- [Creating automatic shifts](#topic_z3b_jff_b1c)
- [Creating fixed shifts](#topic_t1x_mff_b1c)
- [Organizing shifts](#topic_lkl_rff_b1c)
- [Managing locations](#topic_qzz_4z4_zzb)

Related articles:

- [About Zendesk WFM workstreams](https://support.zendesk.com/hc/en-us/articles/6443314489242)
- [Creating Zendesk WFM general tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330)
- [Using the WFM time zone switcher](https://support.zendesk.com/hc/en-us/articles/6443314319258)

## Accessing the Locations page

You must be an admin to access the Locations page.

**To access Locations**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Organization structure**.
2. Click **Locations**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_organization_structure_locations.png)

## Adding a location

Add locations to group agents that share the same geographic location, such as an office,
country, or region. Note that agents can be assigned to only one location.

**To add a location**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Organization structure**.
2. Select **Locations**, then click the add location (**+**) icon in the
   upper-left.
3. Enter a unique **Location name**.
4. Click the drop-down menu and select the **Time zone**.

   By default, the
   time zone selected in the [time zone switcher](https://support.zendesk.com/hc/en-us/articles/6443314319258) is used.
5. (Optional) If you plan to use [automatic shifts](#topic_z3b_jff_b1c), choose your Operational hours. Select either **Open
   24/7** or select **Specific hours** to choose certain days of the week and
   specific hours.
   If you select specific hours, it's recommended to set the same length of
   time for each day.

   Note: A location’s operational hours and automatic shift requirements only apply if
   you're using automatic shifts. [Fixed
   shift](#topic_t1x_mff_b1c) logic overrules these settings.
6. (Optional) If you plan to use automatic shifts, set the **Automatic shift
   requirements**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_org_add_locations.png)
7. Click **Save**.

   Next, you’ll create shifts for the location and assign agents.
   You can create both [automatic](#topic_z3b_jff_b1c) and
   [fixed](#topic_t1x_mff_b1c) shifts for each of your
   locations.

**Understanding a location's time zone**

Here are a few things you should keep in mind when setting up a location’s time
zone:

- The agent's Location time zone determines where time off and shifts are scheduled.
- The timezone set in the Location is also what determines whether or not daylight
  saving time (DST) applies for that shift or time off.
- The time zone in which agents see their shifts is controlled through the time zone
  selector in their [schedule](https://support.zendesk.com/hc/en-us/articles/6443374353434). For example, a location's time zone is in the United
  States during daylight saving time. Agents who have set their time zones in their agent
  schedule to a time zone that doesn't observe DST will see their shifts adjust when
  daylight saving time takes effect in the time zone to which their shifts are anchored
  within Locations.

## Creating automatic shifts

Automatic shifts are based on your forecasted requirements. These shifts allow Zendesk WFM
to automatically decide the best days and starting times for each agent. However, you do
have some control over the starting times for your automatic shifts.

You can also choose to [rotate shifts
automatically](#topic_ogy_xt5_xgc).

**To create an automatic
shift**

1. [On your Locations page](#topic_slm_4k4_zzb)
   select a location.
2. Click **Shifts** in the top-right corner.
3. Click the add shift (**+**) icon and select **Automatic shift**
   .
4. Enter a **Shift name**, then click **Add shift**.
5. Click the add **Intraday variants** (**+**) icon below the Actions
   menu.
6. In the **Settings** tab, configure the following:
   - Name
   - Shift length
   - Select either **Flexible shift start time** or **Specific shift start
     time**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_scheduling_auto_start.png)

     **Flexible shift start times**
     allow you to choose the **Max difference in shift start time** (such as +2
     hours). This is the window of time in which agents can be scheduled. For example, if
     your max difference is two hours, an agent scheduled to work at 9:00 am can only
     have their next shift start between 7:00 am and 11:00 am.

     For **Specific
     shift start time**, enter more than one starting time. The start times for each
     agent will be chosen to best satisfy the forecasted staffing needs.
7. Click the **Intraday** tab. This is when your agents' [general tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330) or [unified agent statuses](https://support.zendesk.com/hc/en-us/articles/10114746509978) should occur. You can set only one
   intraday variant per automatic shift.
8. Click the **Task** (+) icon, then select a task. This can be any task that your
   agents need to accomplish daily, such as a break, lunch, or a daily stand-up meeting. It
   can also include any [workstreams](https://support.zendesk.com/hc/en-us/articles/6443314489242) they're assigned to. If you don't select any
   workstreams, the workstream is auto-populated for you based on what's been
   forecasted.
9. Set the time interval in which the task can occur, counting from the start of the shift
   and the duration of the task.

   Overlapping tasks are highlighted in red. Make sure to correct
   these, as they can prevent shifts from being generated or result in shifts being
   generated with overlapping tasks, disrupting editing and tracking.

   You can also add a note to provide more context to agents when this task is
   selected.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_locations_shifts_intraday.png)

   The task displays
   a white corner and agents can see the note by hovering over it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/agent_schedule_task_note.png)
10. Click **Save**.
11. Select **Agents** on the top right to assign users to this shift and then click
    **Save**. By default, all users who are assigned to workstreams are displayed, but
    you can filter by your [teams](https://support.zendesk.com/hc/en-us/articles/6443329411994), [workstreams](https://support.zendesk.com/hc/en-us/articles/6443314489242), other [locations](https://support.zendesk.com/hc/en-us/articles/6443345205402), and your Zendesk groups.

### Rotating automatic shifts

When you create or edit automatic shifts, you can define a rotation period for these
shifts in either days or weeks. Rotation periods allow agents to rotate between shifts
with different starting times. For example, if you define a rotation period of one week,
then agents that start at 9:00 am can start at 11:00 am the following week, and so on.

By rotating agents' shift start times automatically, managers don't have to decide a
specific order in which to rotate shifts.

**To create a rotation period for an automatic shift**

1. [Create](#topic_z3b_jff_b1c) or edit an existing
   automatic shift.
2. Click the shift's **Intraday variant**.
3. Enter a **Rotation period**, then select if it's in either **day(s)** or
   **week(s)**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_auto_shift_rotate_period.png)

   If the
   intraday variant has a **Flexible shift start time**, the best starting time for
   each agent is calculated according to what's forecasted and is maintained for the
   defined rotation period. During the next rotation period, a new starting time may be
   selected for agents.

   If the intraday variant has a **Specific shift start time**,
   agents are randomly assigned to the different specified times and are rotated
   between the different starting times during each rotation period.
4. Click **Save**.

## Creating fixed shifts

Fixed shifts allow you to set specific days and times for shift start. The fixed shift
logic overrides the location's operational hours and automatic shift requirements.

Fixed shift intraday settings work similarly to the automatic shift intraday, but with the
following key differences:

- You can set up multiple intraday variants for each shift.
- Each variant can be assigned to one or more day of the week (each day can only have
  one intraday variant)
- The covered days for the shift are displayed at the top of the intraday variants
  screen.

**To create a fixed shift**

1. Click your [Location's](#topic_slm_4k4_zzb)
   **Shifts** section in the top-right corner.
2. Click the add shift or folder (**+**) icon and select **Fixed shift**
   from the menu.
3. Enter a **Shift name**. For example, *9am MWF*.
4. Click **Add shift**.
5. Click the add intraday variant (**+**) icon below the Actions menu.
6. In the **Settings** tab, configure the following:
   - Name
   - Start time
   - Length
   - Working days. The days your agents will work. The days that appear dimmed will be
     their days off.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_shift_intra_fixed.png)
7. Click the **Intraday** tab.

   This is when your agents' [general tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330) or [unified agent statuses](https://support.zendesk.com/hc/en-us/articles/10114746509978) should occur.
8. Click the add **Task**(+) icon, then select a task from the menu.

   This can be any
   task that your agents need to have or accomplish on a daily basis such as a break,
   lunch, or a daily stand-up meeting. It can also include any [workstreams](https://support.zendesk.com/hc/en-us/articles/6443314489242) they're assigned to.

   If you don't select
   any workstreams, the workstream is auto-populated for you based on what's been
   forecasted.
9. Set the time interval in which the task can occur, counting from the start of the shift
   and the duration of the task.

   Overlapping tasks are highlighted in red. Make sure to correct
   these, as they can prevent shifts from being generated or result in shifts being
   generated with overlapping tasks, disrupting editing and tracking.

   You can also add a note to provide more context to agents when this task is
   selected.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_locations_shifts_intraday.png)

   The task displays a white corner and agents can see the note by hovering over
   it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/agent_schedule_task_note.png)
10. Click **Save**.
11. Select **Agents** on the top right to assign users to this shift and then click
    **Save**. Make sure that agents are assigned to workstreams so they can be
    selected.

### Rotating fixed shifts

You can add your fixed shifts to a rotation folder so that your agents' shifts are
rotated. For example, you may want to rotate agents' shift start times every week so that
agents who start at 9:00 am one week, can start at 11:00 am the following week, and so on.

**To create a rotation
folder**

1. Click your [Location's](#topic_slm_4k4_zzb)
   **Shifts** section in the top-right corner.
2. Click the add shift or folder (**+**) icon and select **Folder**
   from the menu.
3. Enter a **Name** and then click **Add folder**.
4. Choose your **Rotation period**. For example, enter **1 week** to
   rotate agents' shifts every week.

   Note: All rotations start from Jan 01, 2022, and not
   from the day or week that your rotations are created. The order of the shifts will
   dictate the order of the rotation that week.
5. Click **Save**.
6. In the Shifts sidebar, select the shifts you want to rotate and drag them
   into the rotating folder.

After a shift has been added to the rotation folder, you can view the rotation period of
your agents by clicking the Rotation preview tab inside of the folder. If you'd like to
change the order of shifts, you can reassign agents to different shifts.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_location_shift_rotate_folder.png)

## Organizing shifts

Arranging shifts in folders can help you keep all your shifts organized and help you locate
shifts.

**To create a shift
folder**

1. Click your [Location's](#topic_slm_4k4_zzb)
   **Shifts** section in the top-right corner.
2. Click the add shift or folder (**+**) icon and select **Folder** from
   the menu.
3. Enter a **Name** and then click **Add Folder**.
4. Click **Save**.
5. In the **Shifts** sidebar, select the shifts you want to organize and drag them into
   the folder.

   A blue line indicates where the shift will be reorganized

## Managing locations

Manage locations by editing or deleting them.

**To edit a location**

1. [Access your Locations page](#topic_slm_4k4_zzb) and
   click the location you want to edit.
2. Edit the location settings and shifts as needed.
3. Click **Save**.

**To delete a
location**

1. [Access your Locations page](#topic_slm_4k4_zzb) and
   hover over the location you want to delete.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) that appears next to the location name.
3. Click **Delete**.
4. Confirm you want to delete the location by clicking **Delete location**.