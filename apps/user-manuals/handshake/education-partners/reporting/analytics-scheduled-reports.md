# Analytics: Scheduled Reports

Source: https://support.joinhandshake.com/hc/en-us/articles/360000979627-Analytics-Scheduled-Reports

---

Scheduled Reports enable Career Services users to more easily share data with campus stakeholders and external platforms. Reports can be sent to your email address or a secure cloud file storage on the frequency of your choosing. Reports can be in a number of formats –– image, PDF, CSV –– to minimize the need for post-processing. *This means you can create a report and then “set and forget”—Handshake will deliver the report for you.*

We know that many of our partners have expressed an interest in ways to connect Handshake data with platforms like Salesforce, Tableau, and more. This update represents a significant step toward fully automating that process by automating and standardizing the delivery of Handshake data to be imported into another platform.

*Note: you will need both* Analytics: Access*and*Manage *permissions in order to schedule reports to an email. To select SFTP or S3 as a destination for reports, you will need a new role called* Schedule Reports to File Storage*. If you do not have these roles, please reach out to your team's Handshake administrator to request access.*

Topics:

- [Creating a new Reports schedule](#h_01ES49SX6YCN15HRR0DQ2MYAAA)
- [Editing or deleting a schedule](#h_01F6G7A4NTGFBXPKVZESNQV800)
- [Scheduled Dashboards](#h_01F24G2PGJKW2YT2WDR1D3XWZ8)
- [Reviewing Scheduled Reports](#h_01ES49T2M18W93CD5JQYPYRH5V)
- [FAQs](#h_01ES49T8H80YRWVYX9SBAGYYDE)

## Creating a new Reports schedule

Reports can be scheduled via the Analytics overview page or while viewing a specific report:

- On the Analytics overview page, click the three dots to the far right of the saved report name, then click **Schedule**. ![Schedule_from_overview_page.png](https://support.joinhandshake.com/hc/article_attachments/26001302457751)
- When reviewing a saved report or creating a new custom report, click **Options** in the upper-right corner, then click **Schedule**. ![options_-_schedule.png](https://support.joinhandshake.com/hc/article_attachments/26001342005783)

In the popup window that loads, fill out the following information:

### Basic Information

- **Name of schedule**(the name will default to the name of the saved report)
 - The Scheduled Report cannot work if there is a "/" in the name. Please remove any slashes from the schedule name before saving.
- **Where should this data go?** (Select One: **Email** / **SFTP** / **Amazon S3**)
 - **Email**: For security reasons, only the creator of the scheduled report can be the recipient. This email address will default to the email address on your Handshake account.
 - **SFTP**: Enter your **URL** or **IP Address**, **Username**, and **Password**.
 - **Amazon S3**: Enter your **Bucket**, **Path** (optional), **Access Key**, and **Secret Key**.
- **What format should your data be delivered?**
 - **Email**: (Select one: **CSV ZIP File** / **XLSX** / **JSON** / **HTML** / **Text**)
 - **SFTP**: (Select one: **CSV ZIP File** / **JSON**)
 - **Amazon S3**: (Select one: **CSV ZIP File** / **JSON**)
- **At this time, Row Totals and Calculations are not support for Scheduled Reports.**

### Delivery timing

- **How often would you like the report to be delivered?** (Select One: **Daily** / **Weekly** / **Monthly**)
 - **Daily**: Select one from the dropdown: **Every day** / **Weekdays only** / **Specific day**
    - - Specific day will allow for multiple days to be selected.
 - **Weekly**: Select one day of the week from the dropdown.
 - **Monthly**: Select one from the dropdown: **Every month** / **Specific month**and select what day of the month.
    - - Specific month will allow for multiple months to be selected.
 - **At what time?** Select from the dropdown, the time you would like to receive the report. Times are available on a 24-hour time format, in 15 minute increments. The time you select will reflect your own timezone.

### Summary

- Confirmation of selections –– click **Send test email** to test delivery.

**Note**: For reports scheduled to SFTP or Amazon S3, your credentials are not validated upon entry in Handshake. Sending a test email will validate the credentials entered immediately. *If you choose not to send a test email, your credentials will be validated on the first scheduled send date.*

If the credentials were not entered correctly:

- **SFTP**: an error will appear in the lower-right corner that states either "Validation Failed. Check your credentials." or "Connection failed. Upload failed due to error."
- **Amazon S3**: an email will be sent to the address on your account.
 - Subject: "Error with scheduled job *SCHEDULE NAME*"
 - Content: "The scheduled job "*SCHEDULE NAME*" failed for *REASON*. Please visit your content (link) to view and resolve the error, or contact your Looker administrator if you need further assistance. Error: (may vary) 
    - Example email below: ![amazon_s3_credentials_incorrect_email_example_.png](https://support.joinhandshake.com/hc/article_attachments/26001302458903)

## Editing or deleting a schedule

To edit or delete a schedule:

1. From the left navigation bar, click **Analytics**, then click the **Schedules** tab.

2. Locate the desired schedule name, then click the ellipses (three dots) to the far right in the schedule row.

3. Click either **Edit Schedule** or **Delete Schedule** from the dropdown menu.

![edit_schedule.png](https://support.joinhandshake.com/hc/article_attachments/26001302460823)

- **Edit Schedule**: The same fields from creating a schedule (for Basic Information, Delivery timing, and Summary) are available on the **Edit Schedule** popup as well.
 - An example of the **Edit Schedule** popup:

![Edit schedule pop up.png](https://support.joinhandshake.com/hc/article_attachments/26001342020887)

- **Delete Schedule**: if you choose to delete the schedule, a confirmation popup will appear that reads "Delete this schedule? This change cannot be undone. All future sends of this report will cease. You may create a new schedule from the report page." To proceed, click **Delete**.![delete_schedule_confirmation.png](https://support.joinhandshake.com/hc/article_attachments/26001302464407)

## Scheduled Dashboards

To schedule a Dashboard, click the **Schedule** button on the individual dashboard page, in the upper-right corner of the page.

The fields to enter will match those of Scheduled Reports. Fill in the **Basic Information**, select the **Delivery timing**, and **Send test email**, then click **Confirm** to save the schedule.

Click **Confirm** in the lower-right corner of the popup to create the schedule.

![Create schedule pop up for dashboards.png](https://support.joinhandshake.com/hc/article_attachments/26001342022551)

## Reviewing Scheduled Reports

To review a list of your currently scheduled reports, click **Analytics** from the left navigation bar in Handshake, then click the **Schedules** tab.

A table will display all reports you've scheduled with the following columns:

- Name (the name of the saved report or Dashboard scheduled)
- Created Date
- Type
- Delivery Method
- Format
- Frequency

Click the three dots menu to the far right in each row to **Edit Schedule** or **Delete Schedule**.

![List of scheduled reports.png](https://support.joinhandshake.com/hc/article_attachments/26001342024855)

**Note**: Scheduled Reports to an SFTP or Amazon S3 will *only* be visible to the schedule creator.

## FAQs

**Q: What is SFTP and why would I use it? Can HS set it up for me?**

A: SFTP stands for Secure File Transfer Protocol –– it's essentially a secure location that can receive files from Handshake. Because the data may likely contain PII (Personally Identifiable Information), Handshake ensures the options for export remain private and secure. Your IT contact should be able to set up an SFTP location with access permissions. Handshake will not set up the SFTP server on behalf of our partners due to the inherent security considerations. To learn more about set up, refer to the [Looker Documentation](https://docs.looker.com/sharing-and-publishing/scheduling-and-sharing/scheduling-ftp). To receive SFTP deliveries from Handshake, be sure your network admin has added [Looker’s IP addresses](https://docs.looker.com/setup-and-management/enabling-secure-db#option_1:_ip_address_whitelist) to your SFTP server’s IP allowlist or inbound traffic rules. The necessary Public IP addresses to unblock are as follows: 

- 34.200.64.243
- 54.157.231.76
- 18.206.32.254

**Q: What time of day do reports arrive? Can it be changed?**

A: You can select the time that you would like to receive the report! You can learn more about this under the [Edit Schedule](#h_01F6G7A4NTGFBXPKVZESNQV800) section of this article.

 

**Q: Why can’t I email a report to someone else?**

A: At this time, scheduled reports can only be sent to your own email address. Handshake may consider opening this up at a later date. The intent is to ensure data is not inadvertently sent to people who should not have access to it, so we are taking a conservative approach at this time.

 

**Q: Is there a row limit on data pushed?**

A: Handshake’s analytics service is backed by Looker (Google), which has placed some limits on the data that may be delivered to email / SFTP / Amazon S3 –– [Read the details in Looker's scheduling and sharing article](https://docs.looker.com/sharing-and-publishing/scheduling-and-sharing/scheduling). The summary is: 

- Email 
 - CSV or JSON formats do not have row limits, but have a file size maximum of 15MB so your email client doesn’t reject it.
- SFTP
 - CSV or JSON - No row limit

 

**Q: What about other destinations like Dropbox?**

A: There are numerous locations that can serve as intermediary ‘destinations’ for exported data. Handshake started with SFTPs because of their low-cost and ubiquity. If there are specific destinations you’d like added, we plan on releasing more options in the future, so please let us know what serves you best. 

 

**Q: Who’s allowed to send reports to Email, SFTP, or Amazon S3?**

A: Any user with *Access* and *Manage* *Analytics* permissions can schedule reports to be sent to their email address. There is a permission “Schedule Reports to File Storage” that needs to be granted for users to send reports to an SFTP or Amazon S3 destination.

 

**Q: Would you recommend I use my own Handshake account to send reports, or should I set up a separate ‘system user’ account to manage the process?**

A: This is up to you. The benefit of a system user is that it can remain untouched and a dedicated user account on which to run your automated exports. If your personal account becomes deactivated (if you leave the school, for example), having a separate account can be useful. However, be sure to control password and lock down permissions to ensure this doesn’t become a risk for improper access to student data. 

 

**Q: What happens to the scheduled report if the saved report changes?**

A: If the original report is edited and changes saved, the scheduled report will reflect those changes. Therefore, be careful not to disrupt automated reporting. It is recommended that SFTP and 3rd-party system integrations use a saved report that is a dedicated ‘integration’ export report.

**Tip**: if you'd like to use another user's saved report, we recommend to duplicate that report and save the duplicate as a dedicated schedule version, as described in [Analytics: Using Saved Reports](https://support.joinhandshake.com/hc/en-us/articles/222752707). 

**Q: Can we use AZURE SFTP to receive Scheduled Reports?**

A: At this time our data partner, Looker, does not support the host\_key algorithm used by Azure SFTP. Any attempts to send reports to Azure SFTP will result in this error: 
*“Connection failed. Upload to SFTP host ‘**\_\_\_\_\_\_\_\_\_\_\_\_\_\_**’ failed due to error: Net::SSH::Exception. Error: could not settle on host\_key algorithm. Please check your credentials.”*