# Copy a Daily Log - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/copy-a-daily-log

---

## Objective

To replicate data for a specific daily log (e.g. Manpower Log) by copying entries from a previous day.

## Background

When you are building out a daily log report for a current day, you might want to copy or clone an entry from a previous day. For example, you can save time by copying the Manpower log, especially if the same construction vendors or workers are on site performing work.

## Things to Consider

- [Required User Permissions](https://support.procore.com/products/online/user-guide/project-level/daily-log/permissions "Daily Log - User Permissions")
- **Additional Information:**
 - You can only copy a log entry from a single day to another day. If there are multiple entries for a single day, all entries will be copied to the new log. Copying data to/from a specified date range is currently not supported.
 - Attachments will only copy from Notes log entries. All other logs do not copy attachments.
 - You can copy one or more logs at the same time (e.g. Manpower, Timecard, etc.).
 - You can edit entries once they've been copied over.
 - You can use the copy feature on all active daily logs except the Weather log and Photos. Weather can't be copied over because the data is being pulled from the Dark Sky service for a specific day. Same with Photos, they are from certain point and time so they will not be copied over to a Daily Log entry for a new day.
 - The change history for the Daily Log tool will be updated to reflect these changes. The entry will also denote that the log entry was created by using the copy feature.
 - You can configure your Manpower log so that the 'Hours' and 'Workers' values on a copied manpower log entry are set to zero (0). See [Configure Advanced Settings: Daily Log](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/configure-advanced-settings-daily-log "Configure Advanced Settings: Daily Log"). 
    *Note*: If this setting is not enabled, the copied manpower log entry will include the number of hours and workers from the previous entry.

## Steps

1. Navigate to your project's **Daily Log** tool.
2. Use the date filters to navigate to the date you want to copy entries to. 
   *Note:* If you want to copy entries to a date that has already been marked complete, you will need to re-open the day. See [Re-Open a Daily Log](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/re-open-a-daily-log "Re-Open a Daily Log").
3. Click **Copy**. 
   ![copy-daily-log.png](https://support.procore.com/@api/deki/files/78587/copy-daily-log.png?revision=2)
4. In the 'Copy Records From' field, select a date in the past that you want to copy daily log entries from.
5. Mark the checkbox(es) next to the logs you want to copy, or mark the top checkbox next to 'Log Name' to select all.
6. Click **Copy**.  
   *Note:* The logs are automatically copied over to the specified day. You can modify the entries on this day as needed.

## See Also

- [Configure Advanced Settings: Daily Log](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/configure-advanced-settings-daily-log "Configure Advanced Settings: Daily Log")

## 

If you would like to learn more about Procore's daily log management software and how it can help your business, please visit our [construction daily log reporting software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/quality-safety/daily-log "https://www.procore.com/quality-safety/daily-log").