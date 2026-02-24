# Importing Employer Contacts

Source: https://support.joinhandshake.com/hc/en-us/articles/115002887467-Importing-Employer-Contacts

---

Submitting a contacts file to the Importer is the most efficient way to upload information for new employer contacts (individuals at each company who recruit at your institution) into your Handshake system, as well as updating information for existing employer contacts. For existing contacts, we recommend updating them in a subsequent upload.

To start, download this [example CSV file](https://support.joinhandshake.com/hc/article_attachments/27613463522327) - it includes all of the fields you can upload, with example data. You'll notice that each field has its own column — *make sure that the headers match exactly*! If any of your headers differ from the formatting included below, the Importer's analyzer won't be able to identify it, and it will be ignored! We recommend copying and pasting the headers from the example file to ensure the formatting for each of your headers is correct.

### 

## **Available fields for importing an Employer Contacts file**

### **Download an** [**example Employer Contacts CSV file**](https://support.joinhandshake.com/hc/article_attachments/27613422769047)

The fields listed below should be formatted as shown and saved as a CSV. Column headers are case sensitive and should be in all lowercase. If any of your headers differ from the formatting included below, the Importer will not identify it and it will be skipped. We recommend reviewing the example file linked above to ensure correct header formatting.

**Required Fields:** The column headers marked as required are necessary in the file. The column values marked as 'can't be blank' must contain values. Column values that aren't required can be left blank - this will not erase any existing data in that field.

**Optional Fields:** You can leave out any headers or values that are not marked as required - this will not erase any existing data in that field.

| **Column header** | **Column value** |
| --- | --- |
| email\_address **\*Required** | This is the basic identifier for each user in Handshake. It must be unique for that user, meaning that the same email cannot be tied to two accounts. All duplicate emails in the file will fail. **\*Can't be blank** |
| first\_name **\*Required** | Contact's first name. 50 character limit. You cannot include numerical characters (0-9) in this field. If a student has a number in their name (i.e. John the 3rd), you can change the numbers to roman numerals (i.e. John III). **\*Can't be blank** |
| last\_name **\*Required** | Contact's last name. 50 character limit. You cannot include numerical characters (0-9) in this field. If a student has a number in their name (i.e. John the 3rd), you can change the numbers to roman numerals (i.e. John III). **\*Can't be blank** |
| title | Contact's title/position. |
| description | Description of the contact or employer. |
| employer\_id | This is the ID of the employer in Handshake. Do not include this unless it is the correct ID, found in that employer's Handshake URL. This can be used to directly associate the contact with a company profile in Handshake (not commonly utilized, but can be used for reporting purposes). |
| employer\_name | Name of the company. |
| archived | Set to TRUE to archive the contact or set to FALSE to unarchive the contact. |
| location\_attributes:name | Location of company or contact's office. **Note**: We recommend using the full physical address. When using only the street address, our system will use geocoding to autofill for a full physical address. |
| phone | Phone number for employer contact. This can include spaces and extensions. **Note**: a warning message will generate that the phone number needs to be valid. This warning can be ignored and the row will process without issue. |
| cell\_phone | Must be 10 or 11 digits (no special characters). |
| fax | Must be 10 or 11 digits (no special characters). |
| assigned\_to\_id | This is the user ID for the Career Services staff member who 'owns' this contact. To get the user ID for your Career Services staff: Add them as a Career Services Staff member at your school. Open the Career Services Staff member profile. Grab the digits at the end of the URL when you are on their profile. That is their ID:     You should pull this file out of your old system with your Career Services Staff Names or "account managers".  Then, you can use Excel to Find and replace each name with their newly generated Handshake ID! |

Example of how the optional headers in a contacts file may appear:

![](https://support.joinhandshake.com/hc/article_attachments/25998584456343)

### When your file is ready for import

1. Upload directly to the [Importer tool](http://importer.joinhandshake.com/) as a 'Contacts' job type:![](https://support.joinhandshake.com/hc/article_attachments/25998571335959)
2. Once your file is uploaded and analysis is complete, click "Submit and Request Run"

For information on troubleshooting file issues, refer to [Importer Errors: Common Message and Next Steps](https://support.joinhandshake.com/hc/en-us/articles/360001032108)

If you don't have access to Handshake's Importer tool, refer to [Importer: Gaining Access](https://support.joinhandshake.com/hc/en-us/articles/360016070934)

### Next Steps: Invite Your Employer Contacts

Once you've imported your Employer Contacts, follow the steps in this article for [Inviting Contacts to Become Users: Standard Employer Invite Process](https://support.joinhandshake.com/hc/en-us/articles/218692768)!