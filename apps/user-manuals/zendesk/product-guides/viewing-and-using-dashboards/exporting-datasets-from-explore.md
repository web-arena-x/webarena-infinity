# Exporting datasets from Explore

Source: https://support.zendesk.com/hc/en-us/articles/6037992005914-Exporting-datasets-from-Explore

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

You can export granular, unfiltered data from certain Explore datasets on a recurring or
one-time basis. The exported datasets are made available as CSV files that you can
download and integrate with third-party tools of your choice. Additionally, dataset
exports do not have the same [50,000-row limit that reports do](https://support.zendesk.com/hc/en-us/articles/5133326635162#topic_sh5_ljz_nvb).

Exporting datasets this way allows you to easily combine Zendesk data with other data
sources, giving you a fuller picture of your business operations.

Watch this video for a short introduction to exporting datasets.

*Exporting datasets with Zendesk Explore (1:41)*

Important: You must be an Explore admin to configure dataset exports. Admins have access
to all exports regardless of who created them.

This article contains the following topics:

- [Creating a one-time export](#topic_u32_mlt_lyb)
- [Creating a recurring export](#topic_rvq_nlt_lyb)
- [Viewing the results of an export](#topic_k1p_plt_lyb)
- [Canceling an in-progress export](#topic_pcc_rlt_lyb)
- [Deleting an export and its results](#topic_b3s_slt_lyb)

Tip: If you want to export a single report or
dashboard, see [Exporting dashboard tabs and reports](https://support.zendesk.com/hc/en-us/articles/4483481898266).

## Creating a one-time export

You can create an export that runs immediately and exports data for the dataset and
time period you select. The number of exports you can perform each month is equal to
the number of datasets you have access to.

The month is calculated based on a calendar month. If you use an export on March 15
for example, that slot will become available again on April 15.

**To create a one-time export**

1. In Explore, click the **Dataset exports** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dataset_exports_icon.png)) in the left sidebar.
2. Click **Create one-time export**.
3. In the **Dataset** field, select the dataset you want to export. The options
   are:
   - **Answer Bot: Flow Builder**
   - **Chat and Messaging - Engagement**
   - **Chat and Messaging - Messaging tickets**
   - **Guide - Knowledge Base**
   - **Support - Tickets**
   - **Support - SLAs**
   - **Support - Updates History**
   - **Talk - Calls**
4. In the **Time** field, select the time period the data should cover. The
   options are:
   - **Last 24 hours**
   - **Last 7 days**
   - **Last 30 days**
   - **Last 3 months**
   - **Last 6 months**
   - **Last 12 months**
5. Click **Create**. Your export begins processing.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dataset_exporter_one_time_export.png)

You’ll receive an email when the exported CSV file is ready to download. In the
meantime, you can [see the status of
your export](#topic_k1p_plt_lyb) on the **Dataset exports** page. You can download the CSV
file up to three times.

Only the admin who created the export and the account owner receive the email
notification. An admin cannot create an export on behalf of another user, but can
download any export regardless of who created it.

## Creating a recurring export

You can create an export that runs on a recurring basis and exports data for the
dataset and time period you select.

Recurring exports are always scheduled for a specified time in the future. The export
includes data from the previous day, week, or month, depending on the frequency you
select. For example, if you create a recurring weekly export that runs on Mondays at
9 AM, the export will begin processing at 9 AM on the next Monday and will return
data for the previous seven days. This process will repeat every week unless you
[delete the recurring
export](#topic_b3s_slt_lyb).

The first time the recurring export runs, it will return data from the past year,
regardless of your settings.

You can have up to 14 recurring exports at a time.

Tip: If you want to export data immediately, [create a one-time export](#topic_u32_mlt_lyb)
instead.

**To create a recurring export**

1. In Explore, click the **Dataset exports** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dataset_exports_icon.png)) in the left sidebar.
2. Click **Create recurring export**.
3. In the **Dataset** field, select the dataset you want to export.
4. In the **Frequency** field, select how often the export should run. The
   options are:
   - **Daily**
   - **Weekly**
   - **Monthly**
5. Depending on the frequency you selected, specify the **Hour**, **Day**, or
   **Day of the month** the export should run.

   Note: If the selected day of the month doesn’t exist
   for a given month (for example, the 31st of February), the export will
   run on the first day of the next month.
6. Click **Create**. Your export will begin processing on the day and time you
   specified.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dataset_exporter_recurring_export.png)

You’ll receive an email when the exported CSV file is ready to download. In the
meantime, you can [see the status of
your export](#topic_k1p_plt_lyb) on the **Dataset exports** page. You can download the CSV
file up to three times.

## Viewing the results of an export

On the **Dataset exports** page, you can see the details of all exports you’ve
created and download the results as a CSV file.

By default, the CSV files are automatically deleted from Explore seven days after the
export runs. To retain access to the exported data after seven days, download the
file and save it to a different location.

**To view the results of an export**

1. In Explore, click the **Dataset exports** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dataset_exports_icon.png)) in the left sidebar.
2. Select the **Recurring** or **One-time** tab, depending on which type of
   export you want to view. On the Recurring tab, you can see the following
   details:
   - **Dataset.** Which dataset is scheduled to be exported.
   - **Frequency.** How often the dataset is scheduled to be
     exported.
   - **Last run.** When the dataset was last exported.
   - **Next run.** When the dataset will next be exported.

   On the One-time tab, you can see the following details:

   - **Exported on.** When the export ran.
   - **Dataset.** Which dataset was exported.
   - **Time.** The relative time period the data covers (for example, the
     last 24 hours).
   - **Date range.** The specific dates the data covers.
   - **Size.** The size of the exported file.
   - **Expires in.** When the exported file will no longer be available to
     download.
   - **File.** A link to download the exported file. If the export is
     still processing, you’ll see **In progress** here.
3. Click **Download** to download the results of the export as a CSV file.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dataset_exporter_results.png)

## Canceling an in-progress export

You can cancel an in-progress export if you don’t want it to finish running.
Canceling a one-time export that’s currently processing still counts against the
limit of one export per 24 hours.

**To cancel an export**

1. In Explore, click the **Dataset exports** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dataset_exports_icon.png)) in the left sidebar.
2. Select the **Recurring** or **One-time** tab, depending on which type of
   export you want to cancel.
3. Hover your mouse over the export you want to cancel and click the options icon
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) on the right.
4. Click **Cancel**.
5. In the form that appears, click **Cancel export**.

## Deleting an export and its results

You can delete a recurring or completed one-time export that you no longer need. When
you delete an export, its associated results are also deleted. You’ll no longer see
the export results on the **Dataset exports** page.

Deleting a recurring export deletes any results associated with previous iterations
of that export and prevents future iterations from running. Deleting a one-time
export deletes the results associated with that export only.

**To delete an export and its results**

1. In Explore, click the **Dataset exports** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dataset_exports_icon.png)) in the left sidebar.
2. Select the **Recurring** or **One-time** tab, depending on which type of
   export you want to delete.
3. Hover your mouse over the export you want to delete and click the options icon
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) on the right.
4. Click **Delete**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dataset_exporter_delete_results.png)
5. In the form that appears, click **Delete export**.