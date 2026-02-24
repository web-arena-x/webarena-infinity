# Importing Appointment Types

Source: https://support.joinhandshake.com/hc/en-us/articles/115003653787-Importing-Appointment-Types

---

Manually creating appointment types in Handshake can take a while, so we've made it easier by also allowing you to bulk upload appointment types via our Importer tool!

For more information on creating manual appointment types, refer to [School Settings: Appointment Types](https://support.joinhandshake.com/hc/en-us/articles/224601047).

**Getting started:**

1. While logged into your Handshake account, use [Analytics](https://app.joinhandshake.com/analytics/explore) to create a report of appointment types you'd like to bulk add.  It's also useful to explore majors, colleges, labels, and school year names and even add them to your report so that you can be sure you're working with the exact names you'll need when uploading the data. 
   **Note**: All data that is uploaded must be exactly the same in the upload file as it looks in Handshake.  Here is an [example report](https://app.joinhandshake.com/analytics/explore_embed?insights_page=ZXhwbG9yZS9nZW5lcmF0ZWRfaGFuZHNoYWtlX3Byb2R1Y3Rpb24vYXBwb2ludG1lbnRzP2VtYmVkX2RvbWFpbj1odHRwczolMkYlMkZhcHAuam9pbmhhbmRzaGFrZS5jb20mc2hvdz1kYXRhLGZpZWxkcyZxdWVyeT1NRHh0V0tCJnZpcz0lN0IlN0Q=) you can use in Analytics.
2. After creating the report in Analytics, download it in CSV formatting.
3. Open the download file in Excel, and update the column headers to the correct format as listed below. Refer to the list below of all available fields and formatting.

## Available fields for importing an Appointment Types file

**Download an [example Appointment Types CSV file](https://support.joinhandshake.com/hc/article_attachments/360050996693)**

The fields listed below should be formatted as shown and saved as a CSV. Column headers are case sensitive and should be in all lowercase. If any of your headers differ from the formatting included below, the Importer will not identify it and it will be skipped. We recommend reviewing the example file linked above to ensure correct header formatting.

**Required Fields:** The column headers marked as required are necessary in the file. The column values marked as 'can't be blank' must contain values. Column values that aren't required can be left blank - this will not erase any existing data in that field.

**Optional Fields:** You can leave out any headers or values that are not marked as required - this will not erase any existing data in that field.

| **Column header** | **Column value** |
| --- | --- |
| name **\*Required** | The name of the appointment type. **\*Can't be blank** |
| length **\*Required** | The length of the appointment type in minutes (Integer). **\*Can't be blank** |
| id | The ID of the appointment to update. Note this is optional and only required if you're updating appointments and know the Handshake ID. Normally you can get this through Handshake Insights. |
| description | A description of the appointment type |
| pre\_survey\_id | The ID of a Handshake survey that the student will fill out as part of their appointment request |
| post\_survey\_id | The ID of a Handshake survey that will be sent to the student following their appointment |
| advisor\_survey\_id | The ID of a Handshake survey that the staff member may fill out once the appointment has started |
| pre\_message | A message that will be sent to the student prior to their appointment |
| post\_message | A message that will be sent to the student following their appointment |
| drop\_in\_enabled | Whether or not you would like students to be able to select this appointment type when checking into Drop In appointments (Boolean) |
| appointment\_category\_names | Names of appointment categories that this appointment type should be used for |
| student\_screen\_attributes:department\_gpa\_required | Whether or not a minimum department GPA is required to schedule this appointment type (Boolean) |
| student\_screen\_attributes:department\_gpa | The minimum department GPA that a student must have to schedule this appointment type (Decimal) |
| student\_screen\_attributes:cumulative\_gpa\_required | Whether or not a minimum cumulative GPA is required to schedule this appointment type (Boolean) |
| student\_screen\_attributes:cumulative\_gpa | The minimum cumulative GPA that a student must have to schedule this appointment type (Decimal) |
| student\_screen\_attributes:major\_names | Names of majors that a student must be a part of to schedule this appointment type |
| student\_screen\_attributes:major\_group\_names | Names of major groups that a student must be a part of to schedule this appointment type |
| student\_screen\_attributes:school\_year\_names | Names of school years that a student must be a part of to schedule this appointment type(separated by semi-colons) |
| student\_screen\_attributes:institution\_label\_names | Names of labels that a student must have to schedule this appointment type |
| student\_screen\_attributes:college\_names | Names of colleges that a student must be a part of to schedule this appointment types |

**Finally, upload it to the [Importer App](https://importer.joinhandshake.com/):**

When you've successfully uploaded your file with no analysis errors, click "Submit and Request Run" and one of our technical support members will process it within 24 hours.