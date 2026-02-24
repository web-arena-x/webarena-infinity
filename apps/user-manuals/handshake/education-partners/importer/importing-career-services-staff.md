# Importing Career Services Staff

Source: https://support.joinhandshake.com/hc/en-us/articles/115002307227-Importing-Career-Services-Staff

---

Creating a staff file is the fastest way to upload and update your Career Services staff in your Handshake system. This article will go through all of the available fields that can be included in a staff upload file, which fields are required vs. recommended, and the formatting that must be used.

To start, download the [sample file](https://support.joinhandshake.com/hc/article_attachments/360062323074) linked in this article - it includes all of the different fields you can use. You'll notice that each field has its own column - make sure each header matches exactly! If a header isn't the same in your file as in our example, Handshake won't be able to identify it and it will be ignored! We recommend that you copy and paste from the example file into a blank excel sheet to ensure the formatting of your headers is correct.

You can always include these with a later file upload, enter them in manually, or have your staff update these fields themselves.  

## Available fields for importing a Career Services Staff file

**Download an [example Career Services Staff CSV file](https://support.joinhandshake.com/hc/article_attachments/360062323074).**

The fields listed below should be formatted as shown and saved as a CSV. Column headers are case sensitive and should be in all lowercase. If any of your headers differ from the formatting included below, the Importer will not identify it and it will be skipped. We recommend reviewing the example file linked above to ensure correct header formatting.

**Required Fields:** The column headers marked as required are necessary in the file. The column values marked as 'can't be blank' must contain values. Column values that aren't required can be left blank - this will not erase any existing data in that field.

**Optional Fields:** You can leave out any headers or values that are not marked as required - this will not erase any existing data in that field.

| **Column header** | **Column value** |
| --- | --- |
| email\_address **\*Required** | The user's email address for Handshake authentication. The email \*must\* be unique within Handshake - it cannot be duplicated. **\*Can't be blank** |
| username **\*Required** | This is the account identifier, or account 'anchor'. This should be unique identifier across your institution, that never changes. We recommend using a staff member's ID number, or any other identifier that will not be updated with a name or email change. **\*Can't be blank** |
| user\_type **\*Required** | This will always be "Career Services". Please note that this value must be capitalized and plural as listed below:   ``` Career Services ``` |
| first\_name **\*Required** | The staff member’s first name. This field is required for new Career Services profiles. 50 character limit.  You cannot include numerical characters (0-9) in this field. If a student has a number in their name (i.e. John the 3rd), you can change the numbers to roman numerals (i.e. John III). |
| auth\_identifier | The staff member's auth identifier, which is necessary for SSO login.  This is the attribute that is set up in your school's SSO settings. |
| last\_name | The staff member’s last name. 50 character limit.  You cannot include numerical characters (0-9) in this field. If a student has a number in their name (i.e. John the 3rd), you can change the numbers to roman numerals (i.e. John III). |
| preferred\_name | The staff member’s preferred name. Do NOT include last name - this field is for preferred first name only. 50 character limit.  You cannot include numerical characters (0-9) in this field. If a student has a number in their name (i.e. John the 3rd), you can change the numbers to roman numerals (i.e. John III). |
| middle\_name | The staff member’s middle name. |
| bio | The staff member’s biography. |
| mobile\_number | The staff member’s phone number. |
| disabled | This field can be used if you would like to archive staff member accounts. This can be used to update staff member accounts in bulk who are no longer working at your institution and who should no longer have staff access on the platform.  Must use boolean values (case sensitive):   ``` TRUE FALSE ``` |
| role\_names | The different roles (or permissions) you’d like to give to the Career Services user. The list of accepted role values is listed below. You can include as many of these roles as needed for each staff member, but if you are including multiple roles, they will need to be formatted as a *semi-colon separated list*. Learn more about how roles function in Handshake in [School Settings: Career Services Staff Roles and Permissions](https://support.joinhandshake.com/hc/en-us/articles/219132767). |

**Note**: *Roles can be added to staff member accounts in Handshake via the Importer, but they cannot be removed. Role removal must be done manually, under each staff member's user account settings.*

*Applications*: The “Applications” role allows staff members to utilize all features under the “Applications” tab; signing up students for interviews, accepting them for interviews, extending job offers, and downloading resumes.

*Articles*: The "Articles" role grants permission to create/update articles under the "Resources" tab.

*Career Fairs:* The “Career Fairs” role grants access to all the features of the “Career Fairs” tab. It allows users to register for career fairs, as well as pay invoices for attendance.

*Employer Approvals*: The "Employer Approvals" role allows staff members to manage employer approvals at your institution. Note that staff members will still be able to view employers without this role, but will not be able to modify approvals, or approve new employers.

*Events*: The “Events” role allows staff members to post, approve, delete, and edit events. All school staff users can view attendee lists for events and open check-in kiosks. Only users with the “Mass Emails” role can send mass emails to event attendees.

*Experiences*: The "Experiences" role provides staff members access to the "Experiences" tab. This includes access to view/approve all experience requests submitted by students at their institution.

*Explore Insights*: The "Explore Insights" role provides staff member access to the Insights Explore feature under the "Analytics" tab. This includes report creation/modification under any of the available Explorer reports.

*External Feeds*: The "External Feeds" role provides staff members access to the "External Feeds" tab under School Settings. This includes the ability to add/edit external feeds.

*First Destination Surveys*: The "First Destination Surveys" role provides staff members access to the "First Destination" tab, and includes the ability to add new First Destination Surveys and edit existing FDS data (recipients, responses, etc).

*Handshake Point of Contact*: The "Handshake Point of Contact" role lists the staff member as a public point of contact for their institution. This is visible to students and approved employers on Handshake.

*Interview Schedules*: The “Interview Schedules” role allows staff members to utilize all features under the “Interview Schedules” tab. This includes creating, editing, and approving interviews. They can also assign students to interviews and put both students and recruiters into interview time slots.

*Jobs*: The “Jobs” role allows staff members to use all available features under the “Jobs” tab. This includes the ability to approve, decline, edit, and post jobs. Note: Edits to a job only affect the version of the job posted at your school. Employers retain control over the original job, which can be posted at many schools.

*Launch Check-In Kiosk*: The "Launch Check-In Kiosk" role allows staff members to access the check-in kiosk - this will be available under career fairs, events, appointments, interview schedules, and first destination surveys.

*Manage All Appointments*: The "Manage All Appointments" role allows staff members to view/manage all appointments scheduled at their institution.

*Manage Feature Preferences*: The "Manage Feature Preferences" role provides staff member access to the "Feature Preferences" tab under school settings. This includes access to approving new feature releases, and activation email campaigns.

*Manage Labels*: The "Manage Labels" role allows staff members to create/edit labels for their institution.

*Manage Own Appointments*: The "Manage Own Appointments" role allows staff members to view/manage their own scheduled appointments. This *does not* provide access to any other staff member's appointments in Handshake.

*Manage Payment Preferences*: The "Manage Payment Preferences" role provides staff member access to the "Payment Preferences" tab under school settings. This includes access to add/change the vendor a school uses for their fair/event payments.

*Manage School Page*: The "Manage School Page" role provides staff member access to the "Details" tab under school settings. This also provides access to the school overview page, and editing/updating the school banner and logo.

*Manage SSO Settings*: The "Manage SSO Settings" role provides staff member access to the "SSO Preferences" tab under school settings. This includes access to configuring an institution's SSO integration, or making any necessary updates/migrations.

*Manage Staff*: The "Manage Staff" role allows staff members to change the roles of other staff members within their institution, and which permissions have been granted.

*Manage Students*: The "Manage Students" role allows users to view the "Manage Students" tab, and view individual student accounts. This also provides access to bulk add/remove labels on student accounts under the "Manage Students" tab.

*Mass Emails*: The "Mass Emails" role provides staff member access to the Mass Emails and Targeted Emails features under the "Emails" tab.

*Reports*: The "Reports" role provides staff member access to the "Analytics" tab. This provides access to basic reporting/dashboards, but does not include the Insights Explorer feature (this is a separate role, listed above).

*Rooms*: The "Rooms" role provides staff member access to the "Rooms" tab under school settings. This allows staff members to add/edit rooms used for appointments/interview schedules.

*Sensitive Student Data Privileges*: The "Sensitive Student Data Privileges" role provides staff member access to view/edit student identifier data (such as auth\_identifier and username values on a student's account).

*Surveys*: The "Surveys" role provides staff member access to all functionality within the "Surveys" tab in Handshake.

*Upload Attachments*: The "Upload Attachments" role provides staff member access to upload attachments to items in Handshake such as career fairs/events/etc.

*View as Student*: The "View as Student" role allows staff members to view as any student associated with their institution.

*View Shared Notes*: The "View Shared Notes" role provides staff member access to view all notes associated with student accounts that have the Institutional privacy setting (rather than the Individual privacy setting, which is viewable only by the note creator).

**How to Upload your Staff File:**

1. Once your file is prepared, click File > Save As > UTF-8 encoded CSV.
2. Login to the [Importer tool](https://importer.joinhandshake.com/) to upload.
3. Click "Upload New CSV" and choose Job Type "Career Services Staff":  
     
   ![](https://support.joinhandshake.com/hc/article_attachments/25287191247511)

**Inviting Staff to Handshake:**

Once you've uploaded your staff into Handshake, they'll be provisioned with Handshake accounts. However, we will *not* send any communications to your staff telling them that they have an account. This will allow you to upload all of your staff at once and then roll out access on your own schedule. When you're ready to have your staff log in, you can direct them to follow these steps to access their accounts:

1. Navigate to your Handshake login page
2. Enter your email address (do *not* use the SSO option)
3. You'll be prompted to set a password and then be given access to your account