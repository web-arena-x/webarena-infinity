# Creating deletion schedules for custom object records

Source: https://support.zendesk.com/hc/en-us/articles/9948798181530-Creating-deletion-schedules-for-custom-object-records

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Verified AI summary ◀▼

Create deletion schedules for custom object records to manage data retention and comply with regulations. You can set up to 10 schedules per object, using conditions like last updated or custom fields to determine when records are deleted. Preview records before activating schedules to ensure accuracy. This feature helps maintain data privacy and organization by automatically removing outdated or unnecessary records.

Data retention policies are critical when [managing data storage](https://support.zendesk.com/hc/en-us/articles/4408835043994) in your account and complying with
industry regulations about the retention of certain data types. [Custom object](https://support.zendesk.com/hc/en-us/articles/5914453843994) record deletion schedules allow admins and
[agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) with permission to
create data retention policies for custom data in your Zendesk account.

For example, you can create custom object record deletion schedules such as the
following:

- Delete temporary order records 30 days after a ticket associated with the order
  is solved.
- Delete product registration records or service orders older than 3 years.
- Delete denied loan applications after 180 days.

This article contains the following topics:

- [Creating a deletion schedule for a custom object's records](#topic_rpj_2jw_ghc)
- [Building condition statements for custom object record deletion schedules](#topic_sxn_sfy_m1c)

Related articles:

- [Managing deletion schedules](https://support.zendesk.com/hc/en-us/articles/8301879320474)

## Creating a deletion schedule for a custom object's records

Admins and [agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) with permission can
create up to 10 deletion schedules per custom object, but only one of the deletion
schedules can be active at a time. If you have the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), you can
activate up to 10 custom object deletion schedules per object.

**To create a custom object record deletion schedule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Deletion schedules**.
2. Click **Create deletion schedule** and then select the name of your custom
   object that you want to create a deletion schedule for.

   If you already have 10
   deletion schedules created for that object, a message appears notifying you
   that you’ve reached your limit. You must delete a schedule before you can
   create a new one.
3. Enter the **Schedule name**.

   Use a consistent naming convention to help you
   recognize similar types of deletion schedules.
4. (Optional) Enter a **Description** for your deletion schedule.
5. For **Category**, indicate when to delete records based on when the record
   was **Last updated**.

   This field is required.
6. Click **Add condition** to add an additional *All* condition for
   deleting the records, based on other properties of the record.

   See [Building condition statements for custom object record deletion schedules](#topic_sxn_sfy_m1c).

   If you have the [Advanced Data Privacy and Protection
   add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), you can add deletion criteria that meet *All* or
   *Any* conditions. There is no limit to the number of conditions you
   can add.
7. Select a **Category**, **Operator**, and **Value** for each
   condition.

   The operator determines the relationship between the category
   and the value. For example, if you select the operator *Is*, your
   category must equal the value.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/deletion_schedule_conditions.png)
8. (Optional) After conditions are added, click **Preview** to preview an
   approximate number of records that match and will be deleted when the schedule
   is active.

   Note: Admins see a complete list of records that match and will be
   deleted. However, because of [custom object permissions](https://support.zendesk.com/hc/en-us/articles/6034260247066), the
   number of records to be deleted that is displayed to agents reflects only
   the records they have access to.
9. Click **Create**.

   Your new deletion schedule is added to the end of the
   list as an inactive schedule.
10. [Activate](https://support.zendesk.com/hc/en-us/articles/8301879320474#topic_nlj_q4y_fdc) the deletion schedule.

## Building condition statements for custom object record deletion schedules

Condition statements consist of categories, field operators, and condition values,
which vary depending on the category selected. Condition statements are essentially
"if" statements that delete custom object records meeting the specified
criteria.

The table below lists the categories available for building condition statements for
custom object record deletion schedules.

Table 1. Custom object record deletion schedule categories

| Category | Description |
| --- | --- |
| Last updated | Deletes records based on when they were last updated. At least one Last updated condition is required. |
| Created at | Deletes records based on when they were created. |
| Custom fields | Deletes records based on custom field values. |