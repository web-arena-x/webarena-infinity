# Importer: Updating Graduating Students to Alumni

Source: https://support.joinhandshake.com/hc/en-us/articles/227482608-Importer-Updating-Graduating-Students-to-Alumni

---

When handling the transition from Senior to Alumni, a lot can vary based on your school’s procedures for handling student access and data updates. See below for the most common workflows used by other schools.

### Handling Graduated Students That Retain Their .edu Email

1.) Update their data through a student sync by [Importing Student Data](https://support.joinhandshake.com/hc/en-us/articles/233086688)**.**The relevant fields you'll be updating are:

- **school\_year\_name** changed to **Alumni**
- **primary\_education:end\_date** should be updated to the correct graduation date, if it’s not     already.
- **primary\_education:currently\_attending** should be set to FALSE (unless they are returning for a graduate degree/additional education at your institution) 
    
 **Note**: This student should drop from your sync over time, since they will have no further information to update.
 - *This will not disable their account.*

2.)  If the student returns later, they can return to the sync with their new information (school year, majors, education dates, etc.):

- **If an alumni returns**, their new **primary\_education:end\_date** and **start\_date** must be provided in your upload file or manually updated on their profile.  Otherwise, this will error during future uploads.
 - This import error typically shows as *{"primary\_education.end\_date":["must be a date on or after primary\_education:start\_date"]}}*
 - If you are providing an updated **start\_date** in your import, but not **end\_date**, you should pass \*\*CLEAR\*\* (Every letter capitalized with two asterisks at the beginning and end of the word) in the **end\_date** field to wipe out the old date and prevent errors. Leaving the **end\_date** field blank in imports will not clear the old **end\_date** value.
    - **Note:** Some users reported receiving a warning from the Importer that \*\*CLEAR\*\* is an "invalid value" for **primary\_education:end\_date** or **start\_date**. This is not accurate, and you may proceed with running the job because it will still recognize it as clearing the field. We are looking into updating the Importer to no longer suggest this as a warning.
- If they were disabled previously, you will need to either:
 - Manually unarchive the user from their student profile **OR**
 - Manually upload a file, including the **disabled** field and set it to FALSE
 - For automatic syncs: Add the **disabled** field to your upload and set it to FALSE

**Note**: This is a student upload, and thus all standard required fields for any student upload file **must** be present in order for your file to process successfully. These fields can be found [here](importing-student-data.md) for your reference. The listed fields above are **in addition to** the standard required fields for student uploads.

### Handling Graduated Students That DO NOT Retain Their .edu Email

1.) Update their data through a student sync by [Importing Student Data](https://support.joinhandshake.com/hc/en-us/articles/233086688)**.** The relevant fields you'll be updating are:

- **school\_year\_name** to change to **Alumni**
- **primary\_education:end\_date** should be updated to the correct graduation date, if it’s not     already.
- **email\_address**:
 - You **cannot** update a student email to an address that is associated with another institution/.edu, as those institutions would create separate accounts for these users.
 - You **can** change these email addresses to personal accounts, such as @gmail, etc.
 - If they keep their .edu email from your institution active for an extended period (1 year+), you will not need to change this address yet.
 - If they do *not* keep their .edu email after graduation, you will need to gather their preferred alternate email to continue using Handshake.
    - We recommend sending a targeted email out requesting their alternate email.
      - If you need the information before a certain date, you may choose to use the verbiage "*we will archive your Handshake account on [insert date] if you do not respond with an alternate email*" or something similar.
- **primary\_education:currently\_attending** should be set to FALSE (unless they are returning for a graduate degree/additional education at your institution)

**Note**: This is a student upload, and thus all standard required fields for any student upload file *must* be present in order for your file to process successfully. These fields can be found in [Importing Student Data](importing-student-data.md). The listed fields above are *in addition to* the standard required fields for student uploads.

### Disabling Graduated Students (Not Recommended)

**Consider the following before archiving student accounts:**

- Students accounts should be archived upon student request or if absolutely necessary.
- Accounts can be unarchived - however, if other career services members at your school are unaware of a student’s account being archived, they may suggest that the student create a new account. At this time, accounts cannot be merged unless they meet the qualifications as listed in [Managing and Merging Duplicate Student Accounts](https://support.joinhandshake.com/hc/en-us/articles/115002657968). If they don't meet those qualifications, the data cannot be connected between two accounts.
- Data and information from an archived account may include: appointment history, fair participation, job applications, experiences, and more. These key points could help shape their career growth.
- Your school will be unable to view archived students on the Manage students page if the students log in to their account after being archived. Learn more about the student archive process in [What Happens When I Archive a Student?](https://support.joinhandshake.com/hc/en-us/articles/37658603402519)
- Alumni with archived accounts can still use Handshake post-graduation, they just won't be connected to your school.
- If your school currently runs automated jobs through Importer, the file will need to be updated to reflect students whose accounts have been archived. If a student requests reactivation, the file will need to be updated once more to reflect this change.

If you wish to disable Alumni Handshake accounts after X number of months you can include the **disabled** column in your student sync, and set this to **TRUE** for anyone no longer needing access. Refer to [Importer: Bulk Archiving Students](https://support.joinhandshake.com/hc/en-us/articles/115001497067) for detailed information on bulk-archiving users.

**Note:** If the student returns at a later point, you can just do the opposite of the above to unarchive/re-enable the user: Include the **disabled** column in your sync and set this to **FALSE**.

### Alternative Option - Manual Import to Update Alumni Information

If you do not use automatic syncs to manage students, or Alumni are removed from your sync right after graduation, you can use the following steps to manually import an Alumni Update file.

Generate a new CSV file containing these users and the include following fields:

- - username - Current Handshake Username
 - email\_address - Existing Handshake E-mail, or new email if updating
 - school\_year\_name - Set to **Alumni**
 - primary\_education:end\_date - Set to recent graduation date if not already updated
 - disabled - (optional) Include if you need to archive Alumni.  See **Disabling Graduated Students** above for details.

**Note**: This is a student upload, and thus all standard required fields for any student upload file *must* be present in order for your file to process successfully. These fields can be found [here](importing-student-data.md) for your reference. The listed fields above are *in addition to* the standard required fields for student uploads.

### SSO Access for Alumni

Alumni can continue to use SSO if the following are true:

- The student’s account in Handshake is not disabled/archived after graduation.
- You continue to allow access to SSO at the school for this user (SSO access is managed by your institution locally).  Please check with your IT team if you are unsure about this.

\* **If Alumni lose access to SSO**, we recommend sending out an email to let students know that they'll need to set a new Handshake-specific password to access the system.  Alumni can always login with email\_address and Handshake password if they lose SSO access.

### What About Students That Go On to Other Institutions After Graduation?

Many students may go on to other institutions for Graduate programs. In this case, those institutions will create a new, separate account for the student with their **new school-issued email**.  You should still maintain their local account with your institution, and update their Alumni status and other information based on the steps above.

For more information on how an existing Alumni connects to your school, refer to [How Students & Alumni Can Request to Access Handshake](../student-account-management/how-students-alumni-can-request-to-access-handshake.md).