# Importing Historical Events

Source: https://support.joinhandshake.com/hc/en-us/articles/115002420488-Importing-Historical-Events

---

Submitting an event job through the Importer is the fastest way to upload your Career Center's historical events into Handshake. This article will help you understand the event information that can be uploaded into Handshake, and how the data must be formatted.

To start uploading your events, download the [sample file](https://support.joinhandshake.com/hc/article_attachments/360053077974). This file is also attached at the end of the article. It includes the proper formatting and all of the different fields you can use.

Each field has its own column — make sure each header matches exactly! If any of the headers don't have the exact formatting that's listed below, all of the information in that field will not be uploaded. We recommend copying and pasting from the example file into a blank excel sheet to ensure the formatting of your headers is correct. 

## Available fields for importing a Historical Events file

### Download an [example Historical Events CSV file](https://support.joinhandshake.com/hc/article_attachments/25324946362135)

The fields listed below should be formatted as shown and saved as a CSV. Column headers are case sensitive and should be in all lowercase. If any of your headers differ from the formatting included below, the Importer will not identify it and it will be skipped. We recommend reviewing the example file linked above to ensure correct header formatting.

**Required Fields:** The column headers marked as required are necessary in the file. The column values marked as 'can't be blank' must contain values. Column values that aren't required can be left blank - this will not erase any existing data in that field.

**Optional Fields:** You can leave out any headers or values that are not marked as required - this will not erase any existing data in that field.

| **Column header** | **Column value** |
| --- | --- |
| student\_registration\_start **\*Required** | The date/time that student registration begins. The required formatting for all dates is yyyy-mm-dd**T**hh:mm:ss (example: *2016-11-01T12:00:00).*If you're having problems formatting any of the required dates/times, you can use this [date formatting guide](https://support.joinhandshake.com/hc/en-us/articles/231942648-Date-Formatting) as a reference. If you're still having trouble, feel free to reach out to our Support team. |
| student\_registration\_end **\*Required** | The date/time that students must complete their registration by. The required formatting for all dates is yyyy-mm-dd**T**hh:mm:ss (example: *2016-11-01T12:00:00).* |
| name **\*Required** | The name of the event (free text is accepted in this field). |
| start\_date **\*Required** | When the event starts. The required formatting for all dates is yyyy-mm-dd**T**hh:mm:ss (example: *2016-11-01T12:00:00).* |
| end\_date **\*Required** | When the event ends. The required formatting for all dates is yyyy-mm-dd**T**hh:mm:ss (example: *2016-11-01T12:00:00).* |
| event\_type\_name **\*Required** | The type of event. Must be one of the following (case-sensitive):   ``` Classroom Presentation Employer On-site Group Appointment Info Session Mock Interview Networking Speaker/Panel Virtual Session Workshop Other ```  **Important**: if the event was a Virtual Session, you must also include virtual\_link |
| virtual\_link **\*Required if event\_type = Virtual Session** | If the event\_type = Virtual Session. The value for virtual link must be only a single URL.   - If more than one link or any additional text are included in this field, the Importer job will display “Analyzed Failed”. - If the event type is Virtual Session and no virtual\_link is included, Importer will display an error: {"success":false,"errors":{"virtual\_link":["cannot be blank for a Virtual Event"]}} |
| import\_identifier **\*Required** | The unique identifier for each event. This identifier will be used if you import notes or labels attached to this event in the future. The **import\_identifier** can be anything and must be totally unique. We recommend an identifier such as:  *schoolhistoricalevent100* *schoolhistoricalevent101 schoolhistoricalevent102 schoolhistoricalevent103* |
| career\_center\_id | The Handshake ID of the Career Center hosting the event. The ID can be found in your School settings > Career Centers. |
| status | The status of the event.Must be one of the following (case-sensitive):   ``` pending in_progress approved declined ``` |
| description | A description of the event (free text is accepted in this field). |
| invite\_only | Was it invite only? Must be one of the following:   ``` Yes No  ``` |
| attendee\_limit | Limit for the number of attendees (must be a number). |

**Example file:**

![](https://support.joinhandshake.com/hc/en-us/article_attachments/115004825307/Screen_Shot_2017-02-01_at_1.20.09_PM.png)

### How to Upload the Events File

1. Once your file is prepared, select *File > Save As > UTF-8 encoded CSV* from Excel (or your preferred CSV file management tool).
2. Use the [Importer tool](https://support.joinhandshake.com/hc/en-us/articles/Every%20staff%20file%20you%20upload%20must%20have%20these%20four%20fields.%20Let's%20talk%20about%20each%20of%20them.) to upload/edit your institution's historical events.  
     
   **Note:** You'll need to set Job Type = **Events**

### Additional Resources

- [Importer: Gaining Access](importer-gaining-access.md)
- [Importer: Getting Started + Running Your First File](importer-getting-started-running-your-first-file.md)