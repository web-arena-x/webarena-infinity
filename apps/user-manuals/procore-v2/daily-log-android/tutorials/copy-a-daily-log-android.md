# Copy a Daily Log (Android)

Source: https://v2.support.procore.com/product-manuals/daily-log-android/tutorials/copy-a-daily-log-android

---

## Background

When you are building out a daily log report for a current day, you might want to copy or clone an entry from a previous day. For example, you can save time by copying the Manpower log, especially if the same construction vendors or workers are on site performing work.

## Things to Consider

- [Required User Permissions](/product-manuals/daily-log-project/permissions)
- **Additional Information:**

 - You can only copy a log entry from a single day to another day. If there are multiple entries for a single day, all entries will be copied to the new log. Copying data to/from a specified date range is currently not supported.
 - Attachments will only copy from Notes log entries. All other logs do not copy attachments.
 - You can copy one or more logs at the same time (e.g. Manpower, Timecard, etc.).
 - You can edit entries once they've been copied over.
 - You can use the copy feature on all active daily logs except the Weather log and Photos. Weather can't be copied over because the data is being pulled from the Dark Sky service for a specific day. Same with Photos, they are from certain point and time so they will not be copied over to a Daily Log entry for a new day.
 - The change history for the Daily Log tool will be updated to reflect these changes. The entry will also denote that the log entry was created by using the copy feature.
 - You can configure your Manpower log so that the 'Hours' and 'Workers' values on a copied manpower log entry are set to zero (0).   
    See [Configure Advanced Settings: Daily Log](/product-manuals/daily-log-project/tutorials/configure-advanced-settings-daily-log). 
    *Note*: If this setting is not enabled, the copied manpower log entry will include the number of hours and workers from the previous entry.

## Steps

1. Navigate to the **Daily Log** tool using the Procore app on an Android mobile device.
2. Tap the **Copy** icon.
3. Tap **From** to select the date you want to copy.
4. Tap **To** to select the date to which you want to add the copied log.
5. Tap the section(s) you want to copy.
6. Tap **Copy Logs**.