# Creating a schedule with operating hours

Source: https://support.zendesk.com/hc/en-us/articles/4408822398106-Creating-a-schedule-with-operating-hours

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Professional or Enterprise |

You can set an availability schedule for your chat agents by enabling operating hours on your account. If you are also using offline forms, you can display this schedule to customers during your offline hours.

Note: Any schedules you create in Zendesk Support will not transfer over to Zendesk Chat.

This article contains the following sections:

- [Understanding operating hours](#topic_brn_1w4_p3b)
- [Setting up operating hours](#topic_dgz_nv5_z1b)
- [Displaying operating hours on the widget](#topic_cfq_fw5_z1b)
- [Reviewing operating hours](#topic_lxg_3w5_z1b)

## Understanding operating hours

When you enable operating hours, any agents signed in to Chat outside of the scheduled hours have their availability status set to **Invisible**. Agents cannot manually change their availability status during offline hours.

You can apply a single offline hours schedule across your entire account, or, if you have multiple [departments](https://support.zendesk.com/hc/en-us/articles/4408881953434) enabled, you can apply customized schedules to each department. However, the operating hours applied to the entire account override the operating hours applied to departments.

Note: You can also choose to display a set schedule (or schedules, if you have separate operating hours for each department) in the Chat widget.

By default, when operating hours are set, agents cannot receive messages from end users outside of the scheduled work hours.

However, in some cases, your end users may be able to use custom Javascript to override your operating hours, and send messages to your agents' accounts, even if they are Invisible. Contact Zendesk's customer support for more information.

## Setting up operating hours

Note: If you enable operating hours, your widget can only be online during the operating hours you've set. If an agent logs in outside of operating hours, their status is Invisible by default. If the agent tries to manually change it to Online, it's automatically set back to Invisible.

**To set up operating hours**

1. From the dashboard, select **Settings** > **Account** > **Operating Hours** tab.
2. In the upper-right corner of the page, click **On**.
3. Select the type of schedule you want to set up for your account.
   - **Account schedule** is a single schedule that applies to your entire account.
   - **Department schedules** lets you apply multiple schedules to a department or apply multiple departments to a single schedule.
4. Select a type of schedule from the **Online Schedule** drop-down menu:
   - **Daily:** Allows you to set separate hours for each day of the week.
   - **Weekday/Weekend**: Allows you to set the same hours for every weekday (Monday to Friday) and both weekend days (Saturday and Sunday).
5. Ensure the check box is selected next to each day of the week that has operating hours. If a day has no operating hours at all, clear the check box next to it.
6. Adjust the sliders next to the days to select the hours agents are available to chat. Note that operating hours must be at least one hour and can be scheduled in 15-minute increments.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopimoperatinghours2.png)
7. If you're using department schedules, click the link to also add departments to the schedule. Note that you must add at least one department to each schedule for department schedules to work.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopimoperatinghours2_departments.png)
8. If you want to show your operating hours on to visitors on the chat widget when the widget is offline, select the **Display Operating Hours** check box. For details, see [Displaying operating hours on the widget](https://support.zendesk.com/hc/en-us/articles/4408822398106#displaying).
9. Click **Save Changes**.
10. For changes to take effect, make all agents log out, click your profile icon in the upper-right, thenn select **Leave session**, and log in again.

## Displaying operating hours on the widget

If you've configured the Offline Form to appear (**Settings** > **Widgets** > **Forms** > **Offline Form**), you can also show operating hours show on your offline widget.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_oh3.png)

**To display operating hours on the widget**

1. From the dashboard, select **Settings** > **Account** > **Operating Hours** tab.
2. Select the **Display Operating Hours** check box.
3. Click **Save Changes**.

## Reviewing operating hours

Where you review your schedules after you've set them up depends on whether you're using account schedules or department schedules.

**To review account schedule hours**

- Go to **Settings** > **Account** > **Operating Hours** tab.

**To review department schedule hours**

- Go to **Settings** > **Departments** and click on the department with the schedule you want to review. The schedules appear in the **Operating Hours** section. The hours that appear here take into account all of the schedules applied to this apartment.