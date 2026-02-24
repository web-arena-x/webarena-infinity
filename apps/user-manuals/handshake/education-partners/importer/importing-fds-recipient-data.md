# Importing FDS Recipient Data

Source: https://support.joinhandshake.com/hc/en-us/articles/360045860254-Importing-FDS-Recipient-Data

---

First Destination Recipient data can be uploaded for historical FDS data that you'd like to import from a previous system, or for students whose FDS recipient data needs to be adjusted/updated.  
  
For all staff members who have the 'Explore Insights' role on their Handshake account, [this report](https://app.joinhandshake.com/analytics/explore_embed?insights_page=ZXhwbG9yZS9nZW5lcmF0ZWRfaGFuZHNoYWtlX3Byb2R1Y3Rpb24vc3R1ZGVudHM_cWlkPUpJVml3YUI3OVg1OWJBdDlrakxDMnImZW1iZWRfZG9tYWluPWh0dHBzOiUyRiUyRmFwcC5qb2luaGFuZHNoYWtlLmNvbSZ0b2dnbGU9Zmls) can be used to pull the required fields for this file, if you have a list of student emails for your recipients. These students **must** have existing Handshake accounts in order to be included in this report! Note that you need to be logged in to your Career Services account in Handshake (with the 'Explore Insights' role enabled) in order to view/download this report.

Below are all of the fields that can be included in this job type, along with the required formatting. Note that your formatting needs to *match exactly* with what is included below! You can reach out to Support if you need assistance with your file formatting, or are having trouble uploading your file.

## **Available fields for importing a FDS Recipient file**

### **Download an** [**example FDS Recipient CSV file**](https://support.joinhandshake.com/hc/article_attachments/360065678553)

The fields listed below should be formatted as shown and saved as a CSV. Column headers are case sensitive and should be in all lowercase. If any of your headers differ from the formatting included below, the Importer will not identify it and it will be skipped. We recommend reviewing the example file linked above to ensure correct header formatting.

**Required Fields:** The column headers marked as required are necessary in the file. The column values marked as 'can't be blank' must contain values. Column values that aren't required can be left blank - this will not erase any existing data in that field.

**Optional Fields:** You can leave out any headers or values that are not marked as required - this will not erase any existing data in that field.

| **Column header** | **Column value** |
| --- | --- |
| user\_id **\*Required** | The student's Handshake account ID. This is the string of numbers at the end of their account URL. You can use the Insights report linked above to obtain this value for the list of students you'd like to include in your file. |
| first\_destination\_survey\_id **\*Required** | ID number of the survey you will be importing recipients onto (which can be found at the end of the URL of the survey's main page). If you haven't created this survey yet, please follow the instructions outlined [here](https://support.joinhandshake.com/hc/en-us/articles/219133387-How-to-Create-a-New-First-Destination-Survey). |
| internal\_status **\*Required** | Each recipient's account status. Must be one of the following (case sensitive):  ``` normal archived ``` |
| import\_identifier **\*Required** | This is an identifier (of your creation) and is unique to each recipient. The import\_identifier can be anything, but it *must be unique*. Examples of recommended identifiers are as follows:  school2020FDSrecipient100  school2020FDSrecipient101  school2020FDSrecipient102  school2020FDSrecipient103  *(Similar to what you would do when importing Appointments or Notes)* |
| education\_level\_name | The student's education level. Must be one of the following (case sensitive):  ``` Associates Certificate Advanced Certificate Bachelors Masters Doctorate Postdoctoral Studies Non-Degree Seeking ``` |
| primary\_college\_name | This is the college that the student belongs to (i.e. the 'Ross School of Business' at the University of Michigan). Only 1 college can be supported in this field. |
| campus\_name | This field is only used for schools that have multiple campuses as part of their Handshake setup (i.e. 'Main', 'East'). If you have multiple campuses on your Handshake system, you can use these here. |
| primary\_major\_name | This is the student's *primary* major. Only 1 major can be supported in this field.  **Note**: The formatting for this major **must** be capital case, with all caps used **only** for abbreviated program designations (i.e. BS Physics). |
| graduation\_date | This is the date when a student is expected to graduate. Please note that it has to be included in the format yyyy-mm-dd, unless otherwise specified in the job! **Note**: There is now an option on the Importer to use a mm/dd/yyyy format. If you choose this option for formatting, please make sure you check the box next to 'use mm/dd/yyyy format' when loading your file to the Importer. |
| major\_names | This is the name of the major(s) that this student has declared. You can upload more than one major for a student by separating each major with a semicolon (i.e. Biology; Chemistry).  **Note**: The formatting for these majors **must** be capital case, with all caps used **only** for abbreviated program designations (i.e. BS Physics; BA Art History). |
| gender | The gender of the student. This is a custom field that can include any text you wish to upload. |
| ethnicity | The ethnicity of the student. This is a custom field that can include any text you wish to upload. For best reporting results we suggest using one of the US Census designations outlined below:   ``` Native American/Alaskan Native Black or African American Asian/Asian American Native Hawaiian/Pacific Islander Latino(a) White/Caucasian Middle Eastern ``` |