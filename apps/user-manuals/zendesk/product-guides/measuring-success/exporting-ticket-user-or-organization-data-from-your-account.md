# Exporting ticket, user, or organization data from your account

Source: https://support.zendesk.com/hc/en-us/articles/4408886165402-Exporting-ticket-user-or-organization-data-from-your-account

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

Location: Admin Center > Account > Tools > Reports

Important: To protect the data in your Zendesk account, data exports are not enabled by default in Zendesk accounts. The account owner must contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to enable data exports in the account.

You can export account data, such as tickets, users, or organizations, to a JSON, CSV, or XML file. If you want to export data about your team members (your agents and admins) only, see [Exporting team-member data](https://support.zendesk.com/hc/en-us/articles/5407034434842).

The exporting tools described in this article are not available on Team plans. However, customers on all Zendesk plans can use the Zendesk REST API to export data.

For security reasons, you can restrict who can export the data. You can also deactivate data exports in your account if Zendesk has enabled them. See [Restricting or deactivating account data exports](https://support.zendesk.com/hc/en-us/articles/5388932900250).

This article contains the following sections:

- [Exporting account data](#topic_lz3_mb5_hl)
- [Understanding the data export options](#topic_lnw_tfb_sfb)
- [Exporting account data with the Zendesk API](#topic_qd1_vgv_jwb)

## Exporting account data

Zendesk admins can export account data, such as tickets, users, or organizations, to JSON, CSV, or XML files. See [Understanding the data export options](#topic_lnw_tfb_sfb) to review which type of account data each file type can export.

Note: [AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346) cannot be exported.

When the export is complete, Zendesk sends you an email containing a download link.
Clicking the link downloads a zip file containing your JSON, CSV, or XML files. The larger the export, the more files you can expect the zip file to contain. The download link is valid for at least three days.

Note: Zendesk can't guarantee a specific order in which data appears in the exported file.

**To export ticket, user, or organization data from your account**

1. If not done already, get Zendesk to enable data exports in your account.

   The [account owner](https://support.zendesk.com/hc/en-us/articles/4408822084634#topic_xkh_3lm_ygb) must contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to enable data exports in your account. Make sure to include your Zendesk Support subdomain name in the request.

   Return here when data exports have been enabled in your account.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Tools > Reports**.

   If you don't see this option and data exports are enabled in your account, you may be restricted from exporting data. See [Restricting data exports to certain admins](https://support.zendesk.com/hc/en-us/articles/5388932900250#topic_bkl_nkw_jwb).

   If necessary, click the **Export** tab to display the data export options. Some legacy versions of Zendesk show the export options on a separate tab.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/export-reports-json-csv-xml.png)
3. Select an export option.
   - **JSON export**: Recommended for accounts with more than 200,000 tickets. Not available in [sandbox](https://support.zendesk.com/hc/en-us/articles/4408828617370) instances.

     To run a JSON export, select a date range, select tickets, users, or organizations, then click **Export**.

     For more information, see [Full JSON export](#topic_eqh_clm_c5b).
   - **CSV export**: Not available in [sandbox](https://support.zendesk.com/hc/en-us/articles/4408828617370) instances.

     To run a CSV export, select a date range and click **Export**.

     For more information, see [CSV export](#topic_ipx_clm_c5b).
   - **XML export**:

     To run an XML export, select **request file** next to each option. Setting a date range or selecting a data type is not available.

     For more information, see [Full XML export](#topic_szx_clm_c5b) and [User XML export](#topic_a3y_clm_c5b).

   Note: If you receive an error on the export, adjust the date range and try again.

When the export is complete, Zendesk sends you an email containing a download link to your data file. Click the link to download the zip file. The export files contained within the zip file are named using the following pattern:
`export_YYYY_MM_DD_uniqueID_X`, where:

- `YYYY` is the year
- `MM` is the month
- `DD` is the day
- `uniqueID` is automatically generated and unique to an export
- `X` is a numeric value related to the number of files in the zip. If there is only one file in the zip, it will end in `_1`; if there are two files, you'll have files ending in `_1` and `_2`; etc. The numbers at the end of the file aren't related to the order of the data within the files.

Depending on the requested export date range and your account's level of ticket activity, the export process can take anywhere from a few minutes to a day or more. If you have concerns about a particular export that you're waiting for, [contact Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).

If you haven't received the email notification, you can click **latest** beside **Full JSON export**, **CSV export**, **Full XML export**, or **User XML export** to download the most recently generated report. The latest report displays your account data from the file you last requested, not your current account data. See [Delays in receiving the email with the downloadable data export file](https://support.zendesk.com/hc/en-us/articles/4408821033754-Delays-in-receiving-an-email-with-the-downloadable-data-export-file-).

## Understanding the data export options

You have the following data export options:

- [Full JSON export](#topic_eqh_clm_c5b)
- [CSV export](#topic_ipx_clm_c5b)
- [Full XML export](#topic_szx_clm_c5b)
- [User XML export](#topic_a3y_clm_c5b)

### Full JSON export

Exports tickets, users, or organizations to JSON files. Accounts with more than one million tickets are downloaded in 31-day increments.

Note: Organization JSON exports include deleted organizations. Deleted organizations can be identified by two specific JSON objects: `name` and `deleted_at`.

Zendesk exports the data in "NDJSON" or Newline Delimited JSON format. This format enables systems to stream JSON objects one at a time rather than read the entire file at once. This is helpful for extremely large export files, which may be too much for traditional JSON readers.

If you want a single JSON file containing all of your information rather than a streaming version, you can wrap the ticket objects in a JSON array. For example, if Zendesk exports the following ticket objects:

```
{"ticket":{"id":....}}
{"ticket":{"id":....}}
{"ticket":{"id":....}}
```

You can create a valid JSON file by wrapping the objects into a "tickets" array as follows:

```
{
 "tickets": [ 
    {"ticket": {"id":....}}, 
    {"ticket": {"id":....}}, 
    {"ticket": {"id":....}}
 ]
}
```

The date ranges for these exports use a [system-generated timestamp](https://developer.zendesk.com/rest_api/docs/support/incremental_export#excluding-system-updates). Typically, these timestamps match the most-recent update recorded on the ticket, user, or organization (not the creation date). There are some cases where system updates don't generate ticket events. In these cases, you may see a few unexpected tickets in the output.

Note: JSON exports don't include items with a system-generated timestamp within 6 minutes of the export request. This prevents issues with trying to fetch items that are still being updated when the export starts.

If a single ticket has more than 1 MB of data, the comments are not included in the JSON file. In that event, the resulting downloadable zip file will include at least two JSON files:

- A JSON file that includes all the tickets you exported, including tickets that exceeded the 1 MB limit and were exported without comments
- A JSON file that includes the tickets that exceeded the 1 MB limit and an error message letting you know that the reason the comments were not included was because the ticket exceeded the 1 MB limit. Example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/export_tickets_json_error.png)

### CSV export

Exports ticket data to CSV files. The data does not include deleted tickets, ticket comments, or ticket descriptions.

If a single ticket has more than 1 MB of data, the ticket is excluded from the report.
However, this rarely happens because CSV exports don't include ticket comments, which are usually the largest data component in a ticket.

All date and time values are converted to the account’s default time zone (at the time of the export). The dates displayed in the CSV file may not match the dates in the JSON export (UTC) or in Explore, which displays the user’s time zone. For more information about an account's time zone, see [Setting time zone and format for Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408887059866#topic_dil_hnc_xe).

The date range for this export uses a [system-generated timestamp](https://developer.zendesk.com/rest_api/docs/support/incremental_export#excluding-system-updates).

Note: CSV exports don't include items with a system-generated timestamp within 6 minutes of the export request. This prevents issues with trying to fetch items that are still being updated when the export starts.

The ticket data in the report includes the data shown in the following table. Multi-line text and multi-select fields, as well as custom date fields, are excluded from CSV reports but can be included in JSON and XML reports.

| Data | Description |
| --- | --- |
| ID | The ticket number. |
| Requester | The name of the requester. |
| Requester ID | The requester's ID number. |
| Requester external id | The ID from an external system. Optional for accounts that have enabled Professional or Enterprise single sign-on using JWT or SAML. |
| Requester email | The requester's primary email address. If you want to export a list of users' secondary email addresses, you must use the [List Users API endpoint](https://developer.zendesk.com/api-reference/ticketing/users/users/#list-users) while [side-loading identities](https://developer.zendesk.com/documentation/ticketing/using-the-zendesk-api/side_loading/) (for example: `GET /api/v2/users.json?include=identities`). |
| Requester domain | The email domain of the requester's primary email address. |
| Submitter | The name of the initial submitter. The requester's name is displayed if the requester submitted the ticket. If an agent submitted the ticket on behalf of the requester, the agent's name is used. If the requester is changed, the submitter does not change. |
| Assignee | The assignee at the time of export. |
| Group | The group at the time of export. |
| Subject | The subject of the ticket. |
| Tags | The tags added to the ticket at time of export. |
| Status | The status at time of export |
| Priority | Priority at the time of export. |
| Via | The ticket channel from which the ticket originated. |
| Ticket type | The type at the time of export. |
| Created at | The original creation time and date. Displays in the account's time zone. |
| Updated at | The time and date of the most recent update. Displays in the account's time zone. |
| Assigned at | The time and date of the most recent agent assignment (i.e. the time it was assigned to the current assignee). Displays in the account's time zone. |
| Organization | The organization of the current requester (if any). |
| Due date | The due date at the time of export. Displays in the account's time zone. |
| Initially assigned at | The time and date of first assignment to an agent (not to a group). Displays in the account's time zone. |
| Solved at | The time and date of the final or most recent change to solved status. Displays in the account's time zone. |
| Resolution time | The final or most recent resolution time in hours, rounded to the nearest whole hour. |
| Satisfaction Score | The current satisfaction rating status (Not Offered, Offered, Good or Bad). |
| Group stations | The number of group assignment changes made. The initial assignment upon ticket creation also counts as a station. |
| Assignee stations | The number of agent assignment changes made. The initial assignment upon ticket creation also counts as a station. |
| Reopens | The number of times a ticket has been changed from Solved to Open (whether by agent or end user). |
| Replies | The number of public agent replies on a ticket to a comment from an agent or end user. |
| First reply time in minutes | The time between ticket creation time and the timestamp of the first public agent comment, displayed in minutes. |
| First reply time in minutes within business hours | Same as above, but only time that elapses during listed business hours is counted. |
| First resolution time in minutes | The time between ticket creation time and the timestamp of the first change of status to Solved, displayed in minutes. |
| First resolution time in minutes within business hours | Same as above, but only time that elapses during listed business hours is counted. |
| Full resolution time in minutes | The time between ticket creation time and the timestamp of the final or most recent change of status to Solved, displayed in minutes. |
| Full resolution time in minutes within business hours | Same as above, but only time that elapses during listed business hours is counted. |
| Agent wait time in minutes | The total time spent in the Pending status, displayed in minutes. |
| Agent wait time in minutes within business hours | Same as above, but only time that elapses during listed business hours is counted. |
| Requester wait time in minutes | The combined total time spent in the New and Open statuses. If the ticket is reopened after being solved, time spent in Solved status is counted as well. Time after final change to Solved status is not included. |
| Requester wait time in minutes within business hours | Same as above, but only time that elapses during listed business hours is counted. |
| On hold time in minutes | The total time spent in the On-hold status, displayed in minutes. |
| On hold time in minutes within business hours | Same as above, but only time that elapses during listed business hours is counted. |

### Full XML export

Exports data to an XML file. This export option is not available if your account has more than 200,000 tickets. In that case, use the JSON export option.

The data includes:

- **Accounts** - all the settings for your account
- **Groups** - detailed information about your groups
- **Organizations** - detailed information about your organizations
- **Tickets** - all the details (including comments) for all your tickets
- **Users** - a list of all your users (end users, agents, and admins)

### User XML export

Exports user data to an XML file. The data includes:

- **Groups** - detailed information about your groups
- **Organizations** - detailed information about your organizations
- **Users** - a list of all your users (end users, agents, and administrators).

For the user and organization data, tags are included but custom user fields and custom organization fields are not. To retrieve your custom user fields, you can use the [List User Fields](https://developer.zendesk.com/api-reference/ticketing/users/user_fields/#list-user-fields) endpoint in the Zendesk API. To retrieve your custom organization fields, you can use the [List Organization Fields](https://developer.zendesk.com/api-reference/ticketing/organizations/organization_fields/#list-organization-fields) endpoint in the Zendesk API.

## Exporting account data with the Zendesk API

You can also use the Zendesk API to export data from your account. For example, you can use the [List Users](https://developer.zendesk.com/api-reference/ticketing/users/users/#list-users) endpoint to export all the users in your account. To learn how, see [Exporting your users with the API](https://developer.zendesk.com/documentation/ticketing/using-the-zendesk-api/exporting-users/) in the Zendesk developer guide. The article shows you how to create a small script that exports all the users in your account to a CSV file. You can then import the CSV file into your favorite spreadsheet application.

For more information, see the following Zendesk API reference docs:

- [List Tickets](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#list-tickets)
- [List Users](https://developer.zendesk.com/api-reference/ticketing/users/users/#list-users)
- [List Organizations](https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/#list-organizations)
- [Incremental Exports](https://developer.zendesk.com/api-reference/ticketing/ticket-management/incremental_exports/)