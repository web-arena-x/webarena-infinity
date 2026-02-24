# Managing deletion schedules

Source: https://support.zendesk.com/hc/en-us/articles/8301879320474-Managing-deletion-schedules

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Deletion schedules help you manage data retention by automatically removing data to comply with privacy laws and manage storage. You can set up schedules for deleting inactive users, archived tickets, attachments, bot-only conversations, and custom object records. Activate, edit, clone, deactivate, or delete schedules as needed to maintain control over your data management processes.

Deletion schedules allow admins and [agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) with permission to create data retention policies by automatically deleting data in Zendesk. Deletion schedules help comply with privacy laws and are beneficial when [managing data storage](https://support.zendesk.com/hc/en-us/articles/4408835043994) in your account.

There are several types of deletion schedules:

- [End-user deletion schedules](https://support.zendesk.com/hc/en-us/articles/6062884435866) delete inactive end users that meet certain conditions, such as those belonging to specific organizations or containing a specific tag on their profile.
- [Ticket deletion schedules](https://support.zendesk.com/hc/en-us/articles/6388012977306) delete archived tickets after a specified period and can be configured to delete tickets by criteria such as brand, group, and custom fields.
- [Attachment deletion schedules](https://support.zendesk.com/hc/en-us/articles/9783945525658)
 automatically delete attachments from archived tickets that meet specific criteria, ensuring that documents are deleted once they have served their purpose.
- [Deletion schedules for bot-only conversations](https://support.zendesk.com/hc/en-us/articles/8499219792154) allow you to delete conversations that take place only between an end user and your bot.
- [Deletion schedules for custom object records](https://support.zendesk.com/hc/en-us/articles/9948798181530) allow you to automatically delete records that meet specific criteria, helping you comply with data retention regulations.

The Deletion schedules page in Admin Center provides a central place to manage deletion schedules.

This article covers the following topics:

- [Accessing the Deletion schedules page](#topic_egz_f4y_fdc)
- [Activating deletion schedules](#topic_nlj_q4y_fdc)
- [Editing and cloning deletion schedules](#topic_zzt_r4y_fdc)
- [Deactivating and deleting deletion schedules](#topic_sbq_w3s_mdc)

## Accessing the Deletion schedules page

You'll find the Deletion schedules page in Admin Center.

**To access the Deletion schedules page**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
 **Account** in the sidebar, then select **Security > Deletion schedules**.

 The Deletion schedules page opens.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/deletion_schedule_page.png)

## Activating deletion schedules

Deletion schedules are inactive when you initially create them. You must activate deletion schedules for them to start deleting data.

One deletion schedule per type can be active at a time. If you have the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), up to 10 deletion schedules per type can be active.

**To activate a deletion schedule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Deletion schedules**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) for the schedule, then click **Activate**.
3. In the confirmation dialog, select the checkboxes to confirm you understand what data will be deleted immediately and as scheduled moving forward.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/deletion_schedule_activate.png)
4. Click **Activate deletion schedule**.

## Editing and cloning deletion schedules

You can edit and clone deletion schedules. Cloning a deletion schedule creates a copy you can modify and use for other purposes.

**To edit a deletion schedule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Deletion schedules**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) for the schedule, then click **Edit**.
3. Modify the schedule name, description, and conditions as needed.
4. Click **Save**.

**To clone a deletion schedule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Deletion schedules**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) for the schedule, then click **Clone**.

   A copy of the deletion schedule is created and automatically opened for editing.
3. Modify the schedule name, description, and conditions as needed.
4. Click **Save**.

## Deactivating and deleting deletion schedules

If you no longer need a deletion schedule, you can deactivate or delete it.

If you want to use a deletion schedule again in the future but don't currently need it, then deactivate it. You can reactivate it at any time. Deleting a deletion schedule means that it's gone and can't be retrieved. Deletion schedules must be deactivated before they can be deleted.

**To deactivate a deletion schedule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Deletion schedules**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) for the schedule, then click **Deactivate**.
3. Click **Deactivate deletion schedule**.

   The status of the deletion schedule changes to Inactive.

**To delete a deletion schedule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Deletion schedules**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) for the schedule, then click **Delete**.
3. Click **Delete schedule**.