# Creating end-user deletion schedules

Source: https://support.zendesk.com/hc/en-us/articles/6062884435866-Creating-end-user-deletion-schedules

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Data retention policies are critical for companies to ensure regulatory compliance, as many industries have laws mandating the retention of certain data types. For example, General Data Protection Regulation (GDPR) legislation requires EU companies not to retain personal data longer than necessary, and companies must be able to demonstrate compliance with this principle. Often, companies must comply with multiple data retention laws, depending on industry and location.

User deletion schedules allow admins and [agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) with permission to create data retention policies for end users in your Zendesk account, deleting end users that meet certain conditions. For example, you can create end-user deletion schedules like these:

- Delete end users that haven't been active in three years
- Delete end users whose organization is NOT Acme, Inc. that haven't been active in two years
- Delete end users without the tag *retain* that haven't been active in 18 months

When you [delete end users](https://support.zendesk.com/hc/en-us/articles/4408821737498) in Zendesk, they’re soft deleted and queued for permanent deletion after 30 days.

This article covers the following topics:

- [About end-user deletion schedules](#topic_ogb_ypk_pyb)
- [Creating end-user deletion schedules](#topic_cd2_zpk_pyb)
- [Building condition statements for end-user deletion schedules](#topic_rbk_rjd_kcc)

Related articles:

- [Creating ticket deletion schedules](https://support.zendesk.com/hc/en-us/articles/6388012977306)
- [Creating deletion schedules for bot-only conversations](https://support.zendesk.com/hc/en-us/articles/8499219792154)
- [About the Deletion schedules page](https://support.zendesk.com/hc/en-us/articles/8301879320474)

## About end-user deletion schedules

End-user deletion schedules continuously search for and delete end users who haven't been active for a specified period of time. For example, if you create a schedule that deletes an end user after one year of inactivity, but the end user comments on a ticket within that time, the end user is not deleted. The clock starts over, and the user will be deleted one year after they've been last active.

The last active date considers activities that were driven by the user:

- The end user's last activity on the help center, including the last time they searched for, viewed, or commented on an article.
- The end user's last comment on a ticket where they are requester or CC'd. This is the timestamp of the user's last comment on the ticket.

User activity is *not* activity driven by a team member or Zendesk, such as the time a ticket was closed.

After it's activated, a deletion schedule isn't a one-off event. Zendesk continuously searches for and deletes end users unless you deactivate the schedule. Deletion schedules start to delete eligible end users within 72 hours of meeting the defined criteria. For example, if a schedule deletes inactive end users after 3 years, it will start deleting them within 72 hours of reaching 3 years of inactivity. Zendesk can delete up to 24,000 end users per account per day.

Deletion schedules soft delete end users, meaning users are still in the Zendesk database and accessible on a limited basis to Zendesk employees with certain database privileges. You can then [permanently delete the user](https://support.zendesk.com/hc/en-us/articles/4408845703194#topic_ojp_mjj_hdb), or take no additional action, and Zendesk deletes the user permanently after 30 days.

You can track these changes in the [audit log](https://support.zendesk.com/hc/en-us/articles/4408828001434) by filtering by **Activity type: Updated**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user_deletion_audit_log.png)

## Creating end-user deletion schedules

You can create up to 10 end-user deletion schedules, but only one end-user deletion schedule can be active at a time. If you have the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), you can activate up to 10 end-user deletion schedules.

Tip: To give feedback on more conditions to add, complete this short [Google form](https://docs.google.com/forms/d/e/1FAIpQLSdjZXhMzcZ3IGl7-6GubfPKOGfHCkyGjJdKevLMPGfvQap7Ag/viewform).

**To create an end-user deletion schedule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png) **Account** in the sidebar, then select **Security > Deletion schedules**.
2. Click **Create deletion schedule** > **End users**.

   If you already created 10 end-user deletion schedules, a message appears notifying you that you’ve reached your limit. You must delete a schedule before you can create a new one.
3. Enter the **Schedule name**.

   Use a consistent naming convention to help you recognize similar types of deletion schedules.
4. (Optional) Enter a **Description** for your deletion schedule.
5. For **Last active**, indicate when to delete end users based on when they were last active in Zendesk. This field is required.

   Note: The earliest last active date is January 1, 2018. End users who were last active before that date are marked as last active on January 1, 2018. In addition, only ticket activity is considered between January 1, 2018 and March 1, 2021. Any help center activity during this period is ignored.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/deletion_schedule_users_conditions.png)
6. Click **Add condition** to add additional conditions for deleting end users, such as by organization or tags. You can configure the deletion schedule to delete end users that meet *All* or *Any* of the specified conditions. See [Building condition statements for end-user deletion schedules](#topic_rbk_rjd_kcc).

   You can add one additional condition for deleting end users. If you have the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), there's no limit to the number of conditions you can add.
7. Select a **Category**, **Operator**, and **Value** for each condition.

   The operator determines the relationship between the category and the value. For example, if you select the operator *Is*, your category must equal the value.
8. (Optional) After conditions are added, click **Preview** to preview an approximate number of end users that match and will be deleted when the schedule is active.
9. Click **Create**.
10. [Activate](https://support.zendesk.com/hc/en-us/articles/8301879320474#topic_nlj_q4y_fdc) the deletion schedule.

## Building condition statements for end-user deletion schedules

Condition statements consist of categories, field operators, and condition values (which vary depending on the category selected). Condition statements are essentially "if" statements that delete tickets meeting the specified criteria.

The table below lists the categories available for building condition statements for end-user deletion schedules.

Table 1. End-user deletion schedule categories

   | Category | Description |
| --- | --- |
| Last active | Deletes end users based on when they were last active in your Zendesk account. At least one Last active condition is required. Deletion schedules delete end users that have been *inactive* for the time period specified in the Last active field. For example, if Last active is set to 365 days, and the end user commented on an article within that time, the end user is not deleted. The clock starts over, and the end user will be deleted 365 days from the last active date.  Activities that count toward an end user's activity in the help center or community include:  - Viewing and searching for articles and posts - Commenting on articles and posts - Submitting or viewing a support request  Activities that count toward an end user's activity in Support include:   - Ticket comments made by the end user as the requester on a ticket - Ticket comments made by the end user as a CC on the ticket |
| Organization | Deletes end users based on organization, if you have multiple [organizations](https://support.zendesk.com/hc/en-us/articles/4408886146842). |
| Tags | Deletes end users with the selected [user tags](https://support.zendesk.com/hc/en-us/articles/4408881573658). |