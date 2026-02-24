# Importing Notes

Source: https://support.joinhandshake.com/hc/en-us/articles/115002426128-Importing-Notes

---

Creating a notes file is the fastest way to upload your Career Services historical notes data in your Handshake system. This article will help you understand the available fields that can be uploaded to Handshake, and how the entries must be formatted. Notes can be attached to users, contacts, events, employers, or appointments. Please keep in mind that they can **only be created** through the Importer, they *cannot* be changed or deleted.

Before uploading this file, you should make sure that the following steps have already been completed:

1. [S](https://support.joinhandshake.com/hc/en-us/articles/115002307227-Creating-a-Staff-File-for-Upload-into-Handshake)[tudent File](https://support.joinhandshake.com/hc/en-us/articles/233086688-Creating-a-Student-File-for-Upload-into-Handshake)has been uploaded
2. [Historical Events](https://support.joinhandshake.com/hc/en-us/articles/115002420488) file has been uploaded
3. [Historical Appointments](https://support.joinhandshake.com/hc/en-us/articles/115003651627) file has been uploaded

Essentially, we want to make sure that the objects you are attaching notes to currently exist in the system.

## **Available fields for importing a Notes file**

### **Download an** [**example Notes CSV file**](https://support.joinhandshake.com/hc/article_attachments/360053134874)

The fields listed below should be formatted as shown and saved as a CSV. Column headers are case sensitive and should be in all lowercase. If any of your headers differ from the formatting included below, the Importer will not identify it and it will be skipped. We recommend reviewing the example file linked above to ensure correct header formatting.

**Required Fields:** The column headers marked as required are necessary in the file. The column values marked as 'can't be blank' must contain values. Column values that aren't required can be left blank - this will not erase any existing data in that field.

**Optional Fields:** You can leave out any headers or values that are not marked as required - this will not erase any existing data in that field.

**Unique Identifiers**: You must include values in either **identifiable\_id** *or* **identifier** within this file. 

| **Column header** | **Column value** |
| --- | --- |
| identifiable\_type **\*Required** | This field is sensitive and must be one of the following values.  This is the object you'd like to attach the note to:   ``` User Contact Event Job Employer Appointment ```   **\*Can't be blank** |
| identifiable\_id  **\*Required if identifiable\_type is Event, Employer, Job, or Appointment**  **Note: Do not include this header if identifiable\_type is User or Contact** | The ID found in the URL of the Event, Employer, Job, or Appointment.  Example 1:   - - **identifiable\_type** is *Event*   - **identifiable\_id** is *00001*   *Events_URL_Image_.png*  Example 2:   - - **identifiable\_type** is *Employer*   - **identifiable\_id** is *1*   *Employer_URL_Image.png* |
| identifier  **\*Required if identifiable\_type is Contact or User** | For importing to Appointment or Event, this is a unique identifier you created yourself and attached to an Appointment or Event.  For importing notes to Contacts or Users, this value should be the **email address.** |
| user\_type ***\******Required** | If the **identifiable\_type** is a user, then **user\_type** must be specified.  Potential user\_type values below (case sensitive):   ``` Students ``` |
| content **\*Required** | The actual text of the note.  **\*Can't be blank** |
| privacy\_preference **\*Required** | One of two values (listed below). Personal indicates a private note, viewable only to the creator.  Institution indicates it can be seen by all staff (case sensitive):   ``` personal institution ```   **\*Can't be blank** |
| reminder date | If there should be a reminder associated with the note. The best format is yyyy-mm-ddThh:mm:ss (example: 2016-11-01T12:00:00). If you're having problems formatting these dates and times, you can use this Help Center article as a formatting reference guide. |
| written\_at | The date the note was written at. The best format for all dates is yyyy-mm-ddThh:mm:ss (example: *2016-11-01T12:00:00).* If left blank, this field defaults to the date you submit your Notes file. |
| created\_by\_email | The email address of the author of the note. This must correspond to an existing career services user in Handshake.  Ensure you have uploaded your [career services staff](https://support.joinhandshake.com/hc/en-us/articles/115002307227-Creating-a-Staff-File-for-Upload-into-Handshake) file prior to uploading notes with this field included.If left blank, this field defaults to your institution's first Handshake point of contact. |

**Example CSV File**:

![Importer_Example_Image.png](https://support.joinhandshake.com/hc/article_attachments/26001282848407)

**How to Upload your Notes File:**

1. Once your file is prepared, select *File > Save As > UTF-8 encoded CSV* from Excel (or your preferred CSV file management tool).
2. Use the [Importer tool](https://importer.joinhandshake.com/) to upload/edit your institution's historical notes.
3. You will need to select Job Type = **Notes**