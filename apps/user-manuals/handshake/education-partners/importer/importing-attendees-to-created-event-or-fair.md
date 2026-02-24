# Importing Attendees to Created Event or Fair

Source: https://support.joinhandshake.com/hc/en-us/articles/228463888-Importing-Attendees-to-Created-Event-or-Fair

---

**To upload a list of attendees, you will need:**

1. Event ID (Events attendees) or Career Fair Session ID (Career Fair attendees) 
     
   1. Event ID can be found at the end of the event URL: 
      ![](https://support.joinhandshake.com/hc/en-us/article_attachments/213158147/Screen_Shot_2016-09-29_at_2.29.52_PM.png)
   2. CareerFairSession ID can be found by going to the Career Fair and selecting 'View Registered Students':  
      ![](https://support.joinhandshake.com/hc/article_attachments/25283198339607) 
      Then select which Session the attendees should be associated with. 
      ![](https://support.joinhandshake.com/hc/article_attachments/25283169799575) 
      **Note:** You will need to select a session even if the Career Fair has only one session. 
        
      The Session ID is provided in the URL: 
      ![](https://support.joinhandshake.com/hc/article_attachments/25997308462359)
2. Student email address

- - The email address *must* be associated to an existing, confirmed student account within Handshake, and their account needs to be confirmed (if it was manually created).

**IMPORTANT**: You will only be able to import attendees on school hosted events.

## **Available fields for importing an Attendees file**

**Download an** [**example Attendees CSV file**](https://support.joinhandshake.com/hc/article_attachments/360067741093)

The fields listed below should be formatted as shown and saved as a CSV. Column headers are case sensitive and should be in all lowercase. If any of your headers differ from the formatting included below, the Importer will not identify it and it will be skipped. We recommend reviewing the example file linked above to ensure correct header formatting.

**Required Fields:** The column headers marked as required are necessary in the file. The column values marked as 'can't be blank' must contain values. Column values that aren't required can be left blank - this will not erase any existing data in that field.

**Optional Fields:** You can leave out any headers or values that are not marked as required - this will not erase any existing data in that field.

| **Column header** | **Column value** |
| --- | --- |
| student\_email\_address **\*Required** | The email address of the student attendee. **\*Can't be blank** |
| registered **\*Required** | Must use boolean values (case sensitive):   ``` TRUE FALSE ``` |
| checked\_in **\*Required** | Must use boolean values (case sensitive):   ``` TRUE FALSE ``` |
| identifiable\_type **\*Required** | Must be one of the following (case sensitive):   ``` Event CareerFairSession ```   (no space between words) **\*Can't be blank** |
| identifiable\_id **\*Required** | The Event or Career Fair Session ID (found in URL) **\*Can't be blank** |
| identifier **\*Required** | This is the import\_identifier from your Events import **ONLY** if your historical events were imported. **Note:** This is not typically used in Attendee uploads and can be left blank. Please include the header name in your file and provide an identifier *if* these Events were created through importer. |

**Additional Notes:**

- The **identifiable\_type** is dependent on it being an Event or CareerFairSession (found in URL - "events" or "career\_fair\_sessions")
- **identifier** will need to be included in the file, but please do not put anything in this field
- If you do not include **registered** or **checked\_in**, the attendee record will default to **FALSE** for both of these. The attendees file supports bulk uploads of students who have registered and/or checked in.
 - If the **registered** and **checked\_in** fieldsare listed as **FALSE** for existing attendees, the Importer will remove the attendees from the Career Fair Session or Event
- Importer will only default the values to **FALSE** for blank fields when creating new attendee records for those rows. If an attendee record already existed prior to an import (for example, a student that already registered for a fair/event on their own), a blank **registered** or **checked\_in** field will *not* make any changes to whatever values already exist for those particular attributes (a blank **registered** field will not suddenly unregister an existing attendee record).
- We do not currently support bulk inviting students to events/fairs through the Importer.

**Example of how a formatted file looks:**

- - ![](https://support.joinhandshake.com/hc/article_attachments/25997308470679)

**When your file is ready for upload:**

- Upload directly to the [Importer App](http://importer.joinhandshake.com/)
- Select job type "Attendees"![](https://support.joinhandshake.com/hc/en-us/article_attachments/213000488/Screen_Shot_2016-09-29_at_2.23.28_PM.png)
- Once the file has been successfully analyzed with no errors, click "Submit and Request Run".
 - Someone from our technical support team will process the file within 24 hours of submission.

**If you do not have access to Handshake's Importer App:**

After completing the Importer training material, contact our Support team to request Importer access. Our Support team will need the name and email address of your institution's point of contact for approval.

**\*\*\*Note for Consortia:** A school can only check-in students that are from their university (if public) or students from other universities that pre-registered.