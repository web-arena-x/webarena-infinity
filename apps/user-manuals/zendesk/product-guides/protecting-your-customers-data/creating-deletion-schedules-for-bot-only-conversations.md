# Creating deletion schedules for bot-only conversations

Source: https://support.zendesk.com/hc/en-us/articles/8499219792154-Creating-deletion-schedules-for-bot-only-conversations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

If you use AI agents or third-party bots with Zendesk messaging, you can create deletion
schedules to delete bot-only conversations.

Bot-only conversations are conversations that take place solely between an end user and
your bot. Because these conversations are never escalated to an agent, a ticket is never
created unless the [AI agent tickets feature is turned on](https://support.zendesk.com/hc/en-us/articles/9204149016346#topic_myq_2r1_2gc). To
ensure compliance with the rules outlined in the General Data Protection Regulation
(GDPR), [admins and agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) can use
deletion schedules to delete inactive bot-only conversations based on the schedule they
set in Admin Center. It is recommended that one deletion schedule be activated to delete
bot-only conversations after 30 days.

If the conversation has escalated to an agent at any point, admins can follow the process
outlined in [Deleting end users](https://support.zendesk.com/hc/en-us/articles/4408821737498).

Important: Deleted bot-only conversations cannot be
restored. Exercise caution when activating a deletion schedule.

This article covers the following topics:

- [Creating deletion schedules for bot conversations](#topic_z3h_gg5_pdc)
- [Activating deletion schedules for bot conversations](#topic_prt_q35_pdc)

## Creating deletion schedules for bot conversations

You can create up to ten deletion schedules, but only one schedule can be active.

**To create a deletion schedule for bot conversations**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Deletion schedules**.
2. Click **Create deletion schedule** > **Bot conversations**.
3. Enter the **Schedule name**.

   Use a consistent naming convention to help you
   recognize similar types of deletion schedules.
4. (Optional) Enter a **Description** for your deletion schedule.
5. For **Last active**, specify when the schedule should delete bot
   conversations based on when the conversation was last active. For example, to
   delete bot conversations that haven't had activity in 30 days, type **30**
   for **Value** and select **Days** in the **Unit** drop-down
   field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/deletion_schedule_bot_conversation.png)
6. Click **Create**.
7. [Activate](#topic_prt_q35_pdc) the deletion
   schedule.

## Activating deletion schedules for bot conversations

Deletion schedules are inactive when you create them. You must activate a deletion
schedule for it to start deleting bot conversations. Only one deletion schedule can
be active at a time.

When you activate a new deletion schedule, there may be historical bot conversations
to delete, so the schedule may take longer to run.

**To activate a deletion schedule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Deletion schedules**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) for the inactive schedule, then click
   **Activate**.
3. In the confirmation dialog, select the checkboxes to confirm you understand that
   bot conversations will be deleted immediately and as scheduled moving
   forward.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/deletion_schedule_bot_activate.png)
4. Click **Activate deletion schedule**.