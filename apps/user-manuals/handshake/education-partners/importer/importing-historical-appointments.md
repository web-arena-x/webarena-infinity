# Importing Historical Appointments

Source: https://support.joinhandshake.com/hc/en-us/articles/115003651627-Importing-Historical-Appointments

---

If you have historical appointment information outside of Handshake, you can import this information to keep your records in one place! This article will provide you with tips and steps to import your school's historical appointments.

**Important Notes:**

- Appointments can only be created, they **cannot be updated or deleted** through the Importer so please be sure that your appointments are formatted correctly prior to submitting a file for processing.
- Dates can be very finicky, so be sure to check out our help article on [**Date and Time Formatting**](https://support.joinhandshake.com/hc/en-us/articles/231942648-Date-Formatting).
- The description is a field viewable by the student, so do not input private notes here.
- If you'd like to upload [**Appointment Notes**](https://support.joinhandshake.com/hc/en-us/articles/115002426128), these can be connected to your historical appointments by using the unique **import\_identifier** field. The **import\_identifier** can be anything but it has to be totally unique across all of Handshake, and you will create these identifier values yourself.

**Note**: If you receive an error via the Importer *{"success":false,"errors":{"import\_identifier":["has already been taken"]}}*this indicates you need to create unique identifiers for the appointment.

We recommend an identifier such as YOURSCHOOLNAMEhistoricalappt100, YOURSCHOOLNAMEhistoricalappt101, YOURSCHOOLNAMEhistoricalappt102, YOURSCHOOLNAMEhistoricalappt103 (with YOURSCHOOLNAME being set to your institution's name or abbreviation)

If your location participates in Daylight Savings Time, double-check the dates for historical imports: if it's during standard time, proceed as normal, and if the date is during Daylight Savings Time, you'll need to account for the difference. For example, this historical appointment was (2016-11-01T12:00:00-04:00), but due to DST, it should have actually been (2016-11-01T12:00:00-05:00).

## **Available fields for importing a Historical Appointments file**

### **Download an** [**example Historical Appointments CSV file**](https://support.joinhandshake.com/hc/article_attachments/25348557359127)

The fields listed below should be formatted as shown and saved as a CSV. Column headers are case sensitive and should be in all lowercase. If any of your headers differ from the formatting included below, the Importer will not identify it and it will be skipped. We recommend reviewing the example file linked above to ensure correct header formatting.

**Required Fields:** The column headers marked as required are necessary in the file. The column values marked as 'can't be blank' must contain values. Column values that aren't required can be left blank - this will not erase any existing data in that field.

**Optional Fields:** You can leave out any headers or values that are not marked as required - this will not erase any existing data in that field.

| **Column header** | **Column value** |
| --- | --- |
| appointment\_medium\_name **\*Required** | The name of the appointment medium (location). Case sensitive, must be one of the configurable appointment mediums on your school. **\*Can't be blank** |
| appointment\_type\_name **\*Required** | The name of the appointment type. Case sensitive, must be one of the configurable appointment types on your school. **\*Can't be blank** |
| staff\_member\_email **\*Required** | The email of the staff member involved. Must be an existing staff member in Handshake, and their account must be confirmed. **\*Can't be blank** |
| student\_email **\*Required** | The email of the student involved. *Must be a student in the system.* |
| start\_date **\*Required** | The start date and time, must be formatted as:   - yyyy-mm-dd**T**hh:mm:ss   **Warning:** This defaults to UTC. \*Please see: [Date and Time Formatting](https://support.joinhandshake.com/hc/en-us/articles/231942648-Date-Formatting) |
| end\_date **\*Required** | The end date and time, must be formatted as:   - yyyy-mm-dd**T**hh:mm:ss   **Warning:** This defaults to UTC. \*Please see: [Date and Time Formatting](https://support.joinhandshake.com/hc/en-us/articles/231942648-Date-Formatting) |
| description **\*Required** | A description of the appointment **Warning:** This is viewable by the student. Cannot be left blank. |
| status **\*Required** | Must be one of the following (case sensitive): ``` approved cancelled completed no_show declined requested started ``` |
| import\_identifier **\*Required** | This required identifier must be completely unique. This is used as the main identifier for the appointment by the Importer. If you are importing notes or labels onto this appointment, the two import identifiers for the matching appointment and note/label must match. The import\_identifier can be anything but it must be totally unique across all of Handshake. We would recommend identifiers such as: YOURSCHOOLNAMEhistoricalappt100 YOURSCHOOLNAMEhistoricalappt101 YOURSCHOOLNAMEhistoricalappt102 YOURSCHOOLNAMEhistoricalappt103 |
| walkin | Must use boolean values: ``` TRUE FALSE ``` |

**Example File:**

![](https://support.joinhandshake.com/hc/article_attachments/26001215633559)

**Once you've submitted your file...**

And the file has passed all analyzers with no errors, click the **Submit and Request Run** button. One of our technical support team members will process this file within 24 hours of submission.