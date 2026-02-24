# How to Change System Labels to Normal Labels

Source: https://support.joinhandshake.com/hc/en-us/articles/115014929107-How-to-Change-System-Labels-to-Normal-Labels

---

To accomplish this goal, you will need to use the importer to first remove the system label, then you can upload the normal/public label. There is no method in Handshake to change a system label to a normal/public label.

**Note**: even if only a single student has this system label applied to their account (such as an Alumni or other students not in your sync), you will not be able to use it as a normal label until removed.

### Remove a System Label

1. Run a report through Analytics to identify all students that have the system label currently associated with their profile.

- **Tip**: You may need to pull a list of current system labels from your **Labels** page in Handshake. From your School Settings page, click **Labels** from the left sidebar. Next, use the filter to identify the system labels.

![](https://support.joinhandshake.com/hc/article_attachments/25998866701847)

You can access a pre-populated copy of this Analytics report [here](https://app.joinhandshake.com/analytics/explore_embed?insights_page=ZXhwbG9yZS9nZW5lcmF0ZWRfaGFuZHNoYWtlX3Byb2R1Y3Rpb24vc3R1ZGVudHM_cWlkPWlveEpXWUxtcm92dkdkY1p3NW1rdFEmZW1iZWRfZG9tYWluPWh0dHBzOiUyRiUyRmFwcC5qb2luaGFuZHNoYWtlLmNvbSZ0b2dnbGU9Zmls). In the report:

- ensure the below columns are the only results:
  - Students Username
  - Students Email
  - Students First Name
  - Institution Labels Name List
- create a filter for the "Institution Labels Name" column and add all system labels you would like to *keep*.
  - **Note**: Only enter the label names you want to *keep* in the filter box. This will ensure that the system labels that need to be removed are not included in your export (and thus "cleared" from Handshake when you submit that file).
  - **Example**: In the below image, the user is wanting to remove label3 so it is not included in the report. ![](https://support.joinhandshake.com/hc/article_attachments/25998877252759)

2. Download the results as a .csv file. You'll need to re-format the file to have the column headers defined in step 3.

3. Your file will need to have the below four columns:

- username
- email\_address
- first\_name
- system\_label\_names
  - If a student has multiple labels associated with their account, these will need to be separated by semicolons. *Any labels not listed in this file will be removed completely from Handshake.*

**Note**: the importer may require additional headers as described in [Importing Student Data](https://support.joinhandshake.com/hc/en-us/articles/233086688), but only the above headers will need to have data provided on each row. You may leave the other columns blank–this will not change the information in Handshake.

4. Save as a CSV UTF-8 and upload the file to the importer with a job type = Students. Once the job is complete, the system label will be deleted.

If you are unsure how to save in proper CSV UTF-8 formatted file, please review [Importer App: CSV Rules and File Requirements](https://support.joinhandshake.com/hc/en-us/articles/226346508).

### Adding a Normal/Public Label

Once the system label is removed from the system, you can re-use that name as a normal label.

1. Create a file to upload to the importer to add the normal label back to the student accounts. More information on creating this job type can be found in [Importing Labels](https://support.joinhandshake.com/hc/en-us/articles/229507687).

- Column Headers
  - identifier
  - identifiable\_type
  - user\_type
  - name
  - label\_type

2. Save as a UTF-8 and upload the file to the importer with the job type = labels. Once the job is complete, the the normal/public label will be added.