# Managing data storage in your Zendesk account

Source: https://support.zendesk.com/hc/en-us/articles/4408835043994-Managing-data-storage-in-your-Zendesk-account

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

You can monitor the data storage usage in your account and manage data storage as needed. If you reach your storage limit or expect that you will, you can remove data to free up space or you can purchase more storage to increase your limit.

This article contains the following sections:

- [Default storage limits](#topic_izq_c22_hlb)
- [How Zendesk calculates your storage usage](#topic_qjz_h22_hlb)
- [Monitoring storage usage](#topic_zpg_txm_3xb)
- [Storage notifications](#topic_sgk_wr4_lzb)
- [Removing data to free up space](#topic_m4t_fdw_5lb)
- [Increasing your storage limits](#topic_xwl_ycw_5lb)
- [Buying more storage](#topic_pkw_qcz_tzb)

## **Default storage limits**

Over time, your company will accumulate a lot of data in your Zendesk account. This data is important to you for a lot of reasons.
That's why all customers have the ability to store a default amount of ticket data and files, along with custom objects and user data.
These storage limits exist to ensure the reliability and usability of Zendesk services. Most customers will never use all of their storage.

Note: Storage limits do not include call recordings (see [Recording storage](https://support.zendesk.com/hc/en-us/articles/4408828042010#topic_dcg_3ph_2db)).

Storage consists of these parts:

- **Tickets:** Total size of all ticket [storage objects](#topic_qjz_h22_hlb) in the Support ticketing system.
- **File storage:**Total size of all the files attached to storage objects in the Support ticketing system.
- **Custom objects**: Total size of all storage required to support custom objects, objects records, fields, permissions, and relationships added to the account.
- **Users**: Total size of all storage required to support users added to the account.
- **External content**: Total size of all [external content](https://support.zendesk.com/hc/en-us/articles/9822956298010)brought into Zendesk.

The default storage limits include a base storage amount for all plans and an additional per-seat allocation that varies per plan type:

| Plan | Base storage per account | | | Additional storage per agent | |
| --- | --- | --- | --- | --- | --- |
| Support or Suite | Data | File | External content | Data | File |
| Team | 10 GB | 10 GB | 100 MB | 50 MB per agent | 2 GB per agent |
| Growth | 10 GB | 10 GB | 500 MB | 100 MB per agent | 5 GB per agent |
| Professional | 10 GB | 10 GB | 500 MB | 100 MB per agent | 5 GB per agent |
| Enterprise, Enterprise Plus | 10 GB | 10 GB | 1 GB | 200 MB per agent | 10 GB per agent |

Note: If you exceed your limit, you can remove data to free up space. If you need help making that decision, Zendesk will work with you.
Ultimately, Zendesk always reserves the right to enforce product limits, including charging for additional usage or curtailing usage if the limits are surpassed.

## How Zendesk calculates your storage usage

Each ticket in your Zendesk account is composed of multiple data storage objects. For example, a ticket is composed of metadata, and then depending on what’s included in the ticket, a number of additional data storage objects such as attachments, events, tags, and so on.
[Archived tickets](https://support.zendesk.com/hc/en-us/articles/4408887617050) are included in the storage usage calculations, but [deleted tickets](https://support.zendesk.com/hc/en-us/articles/4408883872538) (via soft delete or permanent delete) are not. If you use [custom objects](https://support.zendesk.com/hc/en-us/articles/5914453843994), each custom object record is calculated as 2 KB of storage. [User](https://support.zendesk.com/hc/en-us/articles/4408893585178) storage is also included in the calculations. Storage requirements for [original email messages](https://support.zendesk.com/hc/en-us/articles/4408832876442#topic_lzq_5br_1bb) and [organizations](https://support.zendesk.com/hc/en-us/articles/4408882246298) are not included.

## Monitoring storage usage

To help you monitor storage usage on your account, Zendesk provides a storage usage dashboard. You can use this dashboard to view your current usage and compare it against your storage limits.

The storage usage dashboard is not available for customers with legacy Support and Support Suite [self-service accounts](https://support.zendesk.com/hc/en-us/articles/4408833931674).

Note: Customers who have accounts with Enterprise License Agreements (ELAs)
will see storage usage information on the dashboard, but they will not see usage limitations or usage notifications.

**To monitor storage usage**

1. In Admin Center, click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/admin_center_home_icon.png) Home in the sidebar.

   A summary of your storage usage appears on the Admin Center home page.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/admin_home_external_content.png)

   The summary shows your data storage, file storage, and external content storage as compared with the amount of storage you have remaining. If you are over your storage limit, you’ll see a warning symbol (!) in the summary.
2. To view more details about your storage usage, click **View details**.

   You can also follow these instructions to view storage usage details:

   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
     **Account** in the sidebar, then select **Usage > Storage**.

   The detailed storage dashboard includes a summary of your usage, along with charts for data storage, file storage, and external storage.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/storage_usage_external_content.png)

   The storage dashboard is refreshed every 24 hours, but it can take up to 72 hours for your current usage to be reflected in the dashboard.
   The graph shows your usage over time as compared with your storage limit.
   The chart line is blue until you use over 80% of your storage. At that point, it turns to orange. If you exceed your storage limit, the line changes to red.

   You can hover your mouse over each data point to get more information.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/storage_dashboard_tooltip.png)

   You can also use the drop-down menus to show the chart by time window and granularity.

   Time window options include:

   - Last 7 days
   - Last 30 days
   - Last 90 days
   - Last 365 days
   - Custom range

   Granularity options include:

   - Daily
   - Weekly
   - Monthly
   - Quarterly

Data collection for the storage usage dashboard started in May 2023, so your usage before that date isn't available and appears as zero on the chart.

## Storage notifications

When you’re approaching your storage limit by using more than 80% of your storage, you'll receive an in-product warning message. For example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_add_storage_button_warning.png)

If you go over your storage limit, you’ll receive an in-product error message. For example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_add_storage_button_short.png)

Admins who don't have permission to make billing changes will see similar storage notifications, but they must contact a billing admin to add more storage. For example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_add_storage_request_error.png)

To create more storage, you can do one of the following:

- [Remove data to free up space](#topic_sgk_wr4_lzb__ul_mw1_3s4_lzb)
- [Increase your storage limit](#topic_xwl_ycw_5lb). You must be an account owner or a billing admin to increase your storage limit.

## Removing data to free up space

If it looks like you're near your storage limit, there are few things you can do to remove data from your account to free up space.
Deletions can take up to 24 hours to show up on the storage dashboard.

For example, you might do any of the following:

- [Create a ticket deletion schedule](https://support.zendesk.com/hc/en-us/articles/6388012977306), an [end-user deletion schedule](https://support.zendesk.com/hc/en-us/articles/6062884435866), or buy the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6119316155930), which includes advanced data retention policies.

 With deletion schedules, which is a bundled feature, you can have only one ticket and end-user deletion schedule active at a time. With the add-on, you can have multiple active schedules and also segment by other criteria, such as brand.
- [Delete users](https://support.zendesk.com/hc/en-us/articles/4408821737498)
- [Manually delete tickets](https://support.zendesk.com/hc/en-us/articles/4408883872538)
- [Export data to a JSON, CSV, or XML file](https://support.zendesk.com/hc/en-us/articles/4408886165402) as a backup, then delete the data from your account.
- [Use the Incremental Exports API](https://developer.zendesk.com/rest_api/docs/support/incremental_export#incremental-exports) to export the data as a backup, then delete the data from your account.
- [Delete custom object records](https://support.zendesk.com/hc/en-us/articles/6093145333786)
- Remove external content from [Confluence connections](https://support.zendesk.com/hc/en-us/articles/9796584600218), [crawlers, or the federated search API](https://support.zendesk.com/hc/en-us/articles/4593564000410).
- You can free up file storage for attachments by deleting the tickets with attachments or using the [Ticket Comments API](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/#redact-ticket-comment-in-agent-workspace) to redact attachments from the ticket.
 For tickets that haven't been closed yet, you can also use the [Redact comment attachment endpoint](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/#redact-comment-attachment).
- Refer to [this Help and FAQs article](https://support.zendesk.com/hc/en-us/articles/4408830952474) for additional deletion tips.

Note: Zendesk cannot help you by automatically removing unwanted data from your account. There is no external, account-level setting to do this.

## Increasing your storage limits

[Account owners](https://support.zendesk.com/hc/en-us/articles/4408822084634) and [billing admins](https://support.zendesk.com/hc/en-us/articles/4408838125082#topic_db4_zcc_wnb) can purchase the More Storage add-on to increase your storage limits.
You can increase your account’s storage in the following increments:

| Plans | Data storage | File storage | External content |
| --- | --- | --- | --- |
| All Suite and Support plans | 500 MB | 25 GB | 500 MB |

You may want to increase your storage limit if:

- Your company is expanding. You anticipate accelerated growth within the next few months and higher ticket volumes.
- Historically, your company has needed more storage than other companies.
- Your company has a use case that creates an exceptional amount of customer service data.
- You're using custom objects with high record volume.
- Your company uses a lot of external content to power your generative search, help center search, and Agent Workspace results.

To buy more storage, see [Buying more storage](#topic_pkw_qcz_tzb).

## Buying more storage

If you have an [eligible sales-assisted or self-service account](https://support.zendesk.com/hc/en-us/articles/4408833931674), you can buy more storage directly from the Subscription page in Admin Center or directly from the storage usage dashboard. You must be an account owner or a billing admin to buy more storage.

If you have a managed account, or a legacy Support or Support Suite account, contact your account representative or click the **Request more storage** link and use the automated bot to request more storage.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ga_storage_usage_error4.png)

This topic describes three different situations for buying more storage:

- If you don't have the More Storage add-on for your account, you can purchase it directly from the shopping cart. See [Buying more storage for the first time](#topic_wwt_v3d_fbc).
- If you already have the More Storage add-on you can increase your storage by adding more units. You can use the shopping cart to increase your units. See [Buying additional storage units](#topic_yy2_jjd_fbc).
- If you are approaching or over your storage limit, you can instantly buy more storage directly from the storage usage dashboard in Admin Center. See [Instantly buying more storage](#topic_kdb_mjd_fbc).

### Buying more storage for the first time

If you don't already have the More Storage add-on, you can purchase it directly from the shopping cart.

**To buy more storage for the first time**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Billing > Subscription**.

   Alternatively, you can click the **Request more storage** link in the Admin Center notification.

   A summary of your current subscription appears.
2. Click **Manage**.
3. Click the **More products** tab on the Subscription page.

   A list of product additions appears, including the More Storage add-on.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/more_storage_cart.png)

   To learn more about the add-on, click **See how it works**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/more_storage_cart_details.png)
4. Enter the number of storage units you want to add.

   Each storage unit includes: Data 500 MB, File 25 GB. External content 500 MB
5. Click **Add to subscription**.

   Your subscription summary is updated to reflect the purchase price.
6. Click **Update subscription** to purchase the add-on.
7. Follow the payment instructions on the Payment page to complete your purchase.

   Within a reasonable amount of time (typically 24 hours), your storage dashboard will be updated to show the new limit.

### Buying additional storage units

If you already have the More Storage add-on you can increase your storage by adding more units. You can use the shopping cart to increase your units. To decrease your units, contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).

**To buy additional storage units**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Billing > Subscription**.

   Alternatively, you can click the **Request more storage** link in the Admin Center notification.

   A summary of your current plan appears. You’ll see the number of More Storage units your subscription already has.
2. Click **Manage** to make changes to your subscription.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/more_storage_add_units.png)
3. Enter the number of additional units to include in your subscription.

   Each storage unit includes: Data 500 MB, File 25 GB

   When you buy more storage units, enter the total number of units to include in your account, not the number you want to add.
4. Click **Add to subscription**.

   Your subscription summary is updated to reflect the purchase price.
5. Click **Update subscription** to purchase the additional units.
6. Follow the payment instructions on the Payment page to complete your purchase.

   Within a reasonable amount of time (typically 24 hours), your storage dashboard will be updated to show the new limit.

### Instantly buying more storage

If you are approaching or over your storage limit, you’ll see a notification on the storage usage dashboard to add more storage. For example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_add_storage_button_short.png)

In this case, you can instantly buy more storage directly from the storage usage dashboard.

**To instantly buy more storage from the dashboard**

1. When you see the storage limit notification, click **Add storage**.

   A mini shopping cart appears. This cart includes a recommendation for the number of storage units you need to add based on your past usage. It also shows you the amount of storage you will have after you purchase more units, the price for the additional units, and the total cost to your account after you add the new units.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_storage_mini_cart_version2.png)
2. Enter the number of units you want to **add** to your account, then click **Buy storage**.

   When you're buying more storage, make sure you enter only the number of **additional** units you want to add, not the total number of units you need in your account.
3. Follow the payment instructions on the Payment page to complete your purchase. Within a reasonable amount of time (typically 24 hours), your storage dashboard will be updated to show the new limit.