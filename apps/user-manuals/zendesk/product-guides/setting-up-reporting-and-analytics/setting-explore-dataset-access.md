# Setting Explore dataset access

Source: https://support.zendesk.com/hc/en-us/articles/4408831563802-Setting-Explore-dataset-access

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

After you [give users access to Explore and define their role](https://support.zendesk.com/hc/en-us/articles/4408836002970), you can choose which datasets they can view and change. This helps you secure your company information from unauthorized views or changes.

This article contains the following topics:

- [Understanding dataset permissions](#topic_g4r_qsr_gtb)
- [Setting dataset permissions](#topic_mqw_lwf_n1b)

## Understanding dataset permissions

By default, most of the Explore [default datasets](https://support.zendesk.com/hc/en-us/articles/4408839218842#topic_hr1_tfk_jkb) have read-only access permissions for all Explore users. However, [custom datasets](https://support.zendesk.com/hc/en-us/articles/4408846513050#topic_hdd_2bc_v2b) require an admin to grant users permission to see or edit it.

If an admin doesn’t [grant a user permissions to a dataset](https://support.zendesk.com/hc/en-us/articles/4408831563802#topic_mqw_lwf_n1b), the user won't be able to create reports from it or see data from it in reports or dashboards, even when shared with them.

Admins can access and modify permissions for all datasets in an account.

## Setting dataset permissions

Explore admins can set dataset access permissions for most other users, except for users with [Limited viewer and Limited editor permissions](https://support.zendesk.com/hc/en-us/articles/4408836002970). Users with limited permissions have access to the [Support - Tickets](https://support.zendesk.com/hc/en-us/articles/4408827693594#topic_zlf_slp_4y) and [Support - Updates History](https://support.zendesk.com/hc/en-us/articles/4408827693594#topic_as3_slp_4y) datasets only, and this cannot be changed.

**To set dataset access for users**

1. In Explore, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_admin_icon.png)) in the left sidebar.
2. On the Dataset access tab, click the User drop-down field and select the user you want to set dataset permissions for.

   Important: If the user is newly created, you won't see them on the Dataset access tab until they've signed in to their Support account for the first time.
3. For each dataset, set the following dataset permissions for the selected user:
   - **Reports**: Choose what users can do with reports that use the dataset:
     - No access
     - View, create, export
     - View, create, export, save
   - **Create calculations**: Select the checkbox to allow the user to [create standard calculated metrics and attributes](https://support.zendesk.com/hc/en-us/articles/4408824243738). This option isn’t available for users with the [**No access** permission level](https://support.zendesk.com/hc/en-us/articles/4408836002970).
   - **Clone dataset**: Select the checkbox to allow the user to create a copy of the dataset. Default datasets and datasets owned by deleted users can’t be cloned.
     This option isn’t available for users with the [**No access** permission level](https://support.zendesk.com/hc/en-us/articles/4408836002970).
4. Click **Save**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_settings_dataset_access_example.png)