# Importing Student Data

Source: https://support.joinhandshake.com/hc/en-us/articles/233086688-Importing-Student-Data

---

Importing student data is a vital step in implementing Handshake. It's the most efficient way to ensure you're populating accurate student information. Imported accounts are automatically confirmed in Handshake and won't require verification from the student.

Data in Handshake helps Career Services users with outreach, filtering, analytics, and populating necessary student job qualifications.

Use this article to upload your initial student data file into Handshake.

Topics:

- [Getting Started](#01H7ZVWRXHFS6EFP4FDSXJ61N7)
- [Uploading Your Student File](#01H7ZVWRXHG7MQ8A54VTFXH35A)
- [Iterating on Your Feedback](#01H7ZVWRXHTCG6BHFN4KV4AWBN)
- [Exploring Additional Resources](#01H7ZVWRXHM6FN34J7SERF1135)
- [Available fields for importing a Students file](#h_01J3KEAP0F65YWNTEGZXHG9RX0)

## Getting Started

**1. Review the list of available student data fields, listed below -** Explore the basic formatting requirements and example content to understand the type of data you'll be bringing in.

**2. Outline your workflow requirements and identify any questions -** [Importer: Student Data Formatting FAQs](https://support.joinhandshake.com/hc/en-us/articles/360008607874) Work as a team (both Career Services and IT) to identify the key fields to support the Career Services team's workflows. Explore the linked doc to determine how you'll handle edge-cases and formatting for particular populations.

**3. Download the Student CSV Example (located at the bottom of this article) -** Each field has its own column, and the headers must match exactly. Copy and paste from the example file to ensure your headers are correctly formatted.

**4. Access the Importer to upload -** Anyone who uploads data into Handshake will need access to the Importer, refer to [Importer: Gaining Access](https://support.joinhandshake.com/hc/en-us/articles/360016070934). If you don't have access yet, review the brief training, then contact Support to request access!

## Uploading Your Student File

1. Once your file is prepared, delete any instructions so that the header fields are in the top row.
2. Click File -> Save As -> UTF-8 encoded CSV.
   - More information on how to properly save your file in the correct formatting can be found [Importer App: CSV Rules and File Requirements](importer-app-csv-rules-and-file-requirements.md).
3. Use the Importer to upload your file:
   - You will want to use Job Type = students
   - The identifier column should be username
   - Review this article for an in-depth walk-through of the upload process - [Importer: Uploading Your First Student File](https://support.joinhandshake.com/hc/en-us/articles/360012405373)

## Iterating on Your Feedback

The Importer should give you detailed automated feedback on the formatting of your file. It can take a few uploads to perfect the formatting, so **if you're encountering warnings or errors, there are a few things to check:**

- **File Type**: make sure you have a valid file type (we require a **UTF-8 encoded .csv file**)
- **Headers**: confirm all headers and fields match the exact formatting requirements (The Importer will notify you if it finds data that we don't map).
- **Missing Fields**: determine if values in your file aren't registering. If they don't register, they'll fail to import.
- **Gut Check**: conduct a quick gut check on the data you are importing:
  - How many students are you bringing in? How many are you archiving? Etc.
  - Are you planning to create new accounts or update existing accounts?
  - What new majors, minors, colleges, and/or campuses were found? Should this create new ones or could these be duplicates/typos?

## Available fields for importing a Students file

Download an [example Students CSV file](https://support.joinhandshake.com/hc/article_attachments/34818629995159)

The fields listed below should be formatted as shown and saved as a CSV. Column headers are case sensitive and should be in all lowercase. If any of your headers differ from the formatting included below, the Importer will not identify it and it will be skipped. We recommend reviewing the example file linked above to ensure correct header formatting.

**Required Fields:** The column headers marked as required are necessary in the file. The column values marked as 'can't be blank' must contain values. Column values that aren't required can be left blank - this will not erase any existing data in that field.

**Options fields:** You can leave out any headers or values that are not marked as required - this will not erase any existing data in that field ***except for system\_label\_names*****.** If you include the system\_label\_names column header in the file and leave the column values blank, this will clear all system labels in Handshake for that respective student.  

| Column header | Column value |
| --- | --- |
| email\_address  ***\*Required***  ***\*Can't be blank*** | The basic identifier for each user in Handshake. This must be unique for each user — meaning that the same email cannot be tied to two student accounts. As a security measure, the .edu domain must belong to your institution. If your students do not use .edu emails, you can use a generic (.gmail.com, etc) address. |
| username  ***\*Required***  ***\*Can't be blank*** | This MUST be unique and should never change for each student. This serves as the “anchor” in imports so that other sensitive fields (such as email) can be updated around this value. Most schools will use a student’s school ID number. This should NOT match any part of a student’s email\_address, or their cardID, as both fields are subject to change (due to last name changes, lost ID cards, etc.). |
| auth\_identifier ***\*Required*** | Required if using SSO. This will be used to check against the returned attribute from SSO systems to authenticate students. Students will **not** enter this value on login; this is a background identifier attribute. This value CAN match their email\_address value, or part of it, if necessary.  Learn more about [Setting up SSO in Handshake](https://support.joinhandshake.com/hc/en-us/articles/360012363913) |
| first\_name  ***\*Required***  ***\*Can't be blank*** | Student's first name. 50 character limit.  You cannot include numerical characters (0-9) in this field. If a student has a number in their name (i.e. John the 3rd), you can change the numbers to roman numerals (i.e. John III). |
| school\_year\_name ***\*Required*** | This field is where you can enter the exact school year that a student is currently in. Here are the different values you can include in this field. Please note the capitalization and spelling must match exactly.   ``` Freshman Sophomore Junior Senior First Year Community / Technical College Second Year Community / Technical College Certificate Program Masters Masters of Business Administration Accelerated Masters Doctorate  Postdoctoral Studies  Alumni ```   Learn more about [School Year Options in Handshake](../operations-platform-management/school-year-options-in-handshake.md) |
| primary\_education:cumulative\_gpa ***\*Required*** | This is the student's cumulative GPA at your school. This has to be a value between 0 and 4 with no more than 2 hundredths (example: 2.75). |
| primary\_education:major\_names  ***\*Required*** | This is the name of the major(s) that this student has declared, **and will populate the "majors" field on a student's profile** (note: there's a limit of 255 characters per major). The formatting for these majors *must* be capital case, with all caps used *only* for abbreviated program designations (i.e., BS Physics; BA Art History). You can upload more than one major for a student by separating each major with a semicolon (i.e. Biology;Chemistry). This is the only field that can be used to populate majors in Handshake via the Importer. |
| primary\_education:education\_level\_name ***\*Required*** | This will describe the degree/education level of a student. It appears on student profiles to tell people what level of education they're currently pursuing.  Here are the different values you can include in this field. Please note the capitalization and spelling must match exactly.   ``` Associates Certificate Advanced Certificate Bachelors Masters Doctorate Postdoctoral Studies Non-Degree Seeking Technical Diploma ``` |
| middle\_name | Student's middle name. 50 character limit.  You cannot include numerical characters (0-9) in this field. If a student has a number in their name (i.e. John the 3rd), you can change the numbers to roman numerals (i.e. John III). |
| last\_name | Student's last name. 50 character limit.  You cannot include numerical characters (0-9) in this field. If a student has a number in their name (i.e. John the 3rd), you can change the numbers to roman numerals (i.e. John III). |
| preferred\_name | Student's preferred name. 50 character limit. Any value added in this field will show up first on the student's profile. If this field is left blank, we'll display the student's First Name. This field needs to be updated in your student system. If not, then any changes made in Handshake manually will be overwritten on the next import.  You cannot include numerical characters (0-9) in this field. If a student has a number in their name (i.e. John the 3rd), you can change the numbers to roman numerals (i.e. John III).  Learn more about [Preferred Student Names](https://support.joinhandshake.com/hc/en-us/articles/224900247) |
| additional\_email\_addresses | Any additional email addresses that your students have been assigned that are not their main email\_address. You can upload more than one additional email address by separating each email address with a semicolon. These emails can be associated with your school email domain and end with .edu or they can be personal email addresses (.gmail.com, etc).  **Note:** Personal email addresses added via the additional\_email\_addresses column will be connected to the account immediately to prevent other accounts from using it, but the student will be required to perform email verification. The link in the email expires after 7 days, so if the student is not receiving the email, or if the link has expired, contact support for next steps.  Learn more about [Additional Email Addresses for Students](https://support.joinhandshake.com/hc/en-us/articles/4409136398615) |
| primary\_education:department\_gpa | The student's departmental GPA at your school (i.e. what a student has earned in their main field of study). This also has to be a value between 0 and 4 with no more than 2 hundredths (example: 3.47). |
| primary\_education:primary\_major\_name | The Primary Major field will not show up on a student's profile and is primarily used for FDS. It is the student's primary major, if they have multiple majors. Only 1 major can be uploaded in this field. The major name must be included in the primary\_education:major\_names field for the primary major to upload to the student's account. |
| primary\_education:minor\_names | The name of the minor that this student has declared in Handshake (note: there's a limit of 255 characters per minor). The formatting for these minors must be capital case (i.e., Math;Art History). You can upload more than one minor for a student by separating each minor with a semicolon (i.e. Math;Art History). |
| primary\_education:primary\_college\_name | This is the student's primary college, if they have multiple colleges. The primary college field will not show up on a student's profile and is primarily used for FDS. Only 1 college can be uploaded in this field. The college name must be included in the primary\_education:college\_name field for the primary major to be updated to the student's account. |
| primary\_education:college\_names | The college that a student is connected to. This field supports multiple entries for students that have multiple colleges (i.e. "Ross School of Business" at the University of Michigan and "College of Engineering"). You can upload multiple colleges by separating each college with a semicolon, i.e. "Ross School of Business;College of Engineering". Note: Due to the nature of CSV files, you cannot include multiple college names for one student if one of those college names contains a comma. |
| primary\_education:start\_date | The date when a student started their current education at the school. It must be in the format "yyyy-mm-dd" for automated Student data syncs. For Manual student data uploads, you can format a Students file in mm/dd/yyyy and can check the box *"Use mm/dd/yyyy format"* in the importer job settings when uploading a new Students CSV. This is incredibly useful when it comes to searching students, qualifications for jobs, and knowing when to shift students to alumni. |
| primary\_education:end\_date | The date when a student is expected to graduate. Please note that it has to be included in the format yyyy-mm-dd, unless otherwise specified in the job! This is incredibly useful when it comes to searching students, qualifications for jobs, and knowing when to shift students to be alumni. There is now an option on the importer to use a mm/dd/yyyy format. If you choose this option for formatting, please make sure you check the box next to "use mm/dd/yyyy format' when loading your file to the importer. **Note:** Student accounts won't automatically update to "Alumni" after the given primary\_education:end\_date.  Learn more about [Updating Graduating Students to Alumni](https://support.joinhandshake.com/hc/en-us/articles/227482608) |
| primary\_education:currently\_attending | This denotes whether the student is currently enrolled or has graduated. It's used for reporting to differentiate between students who are currently active on campus and those who might be on some sort of official absence from school. By assigning TRUE, this will set the user to attending, while FALSE will set them to not attending. Must use boolean values (case sensitive):   ``` TRUE FALSE ``` |
| card\_id | This field is where you can include student ID numbers that correlate with student card IDs. This string must be contained in a card swipe output. If you want to use a card swipe to check students into events, career fairs, or other kiosks, make sure you include this field.  Learn more on [How to Enable Card Swipe Check-in for Students](https://support.joinhandshake.com/hc/en-us/articles/218693498) |
| campus\_name | Schools that have multiple campuses as part of their Handshake setup can use this to designate a specific campus for students. (i.e., 'Main') |
| ethnicity | The ethnicity of the student. This is a custom field that can include any text you wish to upload.  **Note:** The ethnicity and gender field is for internal reporting purposes only. This information won't be available to employers or used by employers for outreach. The information that's imported by your institution is different from the ethnicity and gender data that students can voluntarily share.  For best reporting results, we suggest using one of the US Census designations outlined below.   ``` Native American/Alaskan Native Black or African American Asian/Asian American Native Hawaiian/Pacific Islander Latino(a) White/Caucasian Middle Eastern ```   Learn more on [Interpreting Gender and Ethnicity in Handshake](https://support.joinhandshake.com/hc/en-us/articles/1500008852522) |
| gender | The gender of the student. The field is custom where you can include any text that you wish to upload.  **Note:** The ethnicity and gender field is for internal reporting purposes only. This information won't be available to employers or used by employers for outreach. The information that's imported by your institution is different from the ethnicity and gender data that students can voluntarily share.  Learn more on [Interpreting Gender and Ethnicity in Handshake](https://support.joinhandshake.com/hc/en-us/articles/1500008852522) |
| work\_study\_eligible | If a student is work study eligible. This field determines whether students can view and apply to jobs posted as work study. By assigning TRUE, this will set the student to eligible, while FALSE will remove their eligibility. Only students with TRUE will be able to view and apply to work study jobs. Must use boolean values (case sensitive):   ``` TRUE FALSE ```   Learn more on [How to Manage Work Study in Handshake](https://support.joinhandshake.com/hc/en-us/articles/360003935494) |
| disabled | Used to archive or reactivate student accounts. By assigning TRUE, this will archive the student, while FALSE will unarchive the student. Must use boolean values (case sensitive):   ``` TRUE FALSE ```   Learn more about [Bulk Archiving Students](https://support.joinhandshake.com/hc/en-us/articles/115001497067) |
| system\_label\_names | This section can be used to import any outside information that you would like to sync from your SIS that might provide more nuanced information about your students in a **semi-colon separated** list of label names. Some example values that we see imported here are things like Honors Student or Attending Part Time (here's a formatting example: Honors Student;Attending Part Time). Basically, this could be any type of additional information that you might want to use to organize, categorize, or parse out your students.  **Note:** leaving this field blank in your import will clear all system labels in Handshake for that respective student. This is not a required column header and we recommend using the field primarily in automated student data uploads.  System labels are added or removed in every student sync that includes this column, based on exactly what you have in this field.  Learn more on [How to Change System Labels to Normal Labels](https://support.joinhandshake.com/hc/en-us/articles/115014929107) |
| mobile\_number | The student's mobile number. We can accept any numerical string in this field without special characters such as () or - (but you can include an optional '+' at the beginning of the string). |
| assigned\_to\_email\_address | Email address of the Career Services user that the student is assigned to. |
| hometown\_location\_attributes:name | The address or location of a student's hometown. Ex: "San Francisco, California, USA" or "Phoenix, Arizona". Additional formatting can be found by searching an address here using [mapbox](https://www.mapbox.com/geocoder-feedback/). For maximum accuracy, please use full state names instead of abbreviations. |
| athlete | If the student an athlete. Must use boolean values (case sensitive):   ``` TRUE FALSE ``` |
| first\_generation | If the first generation student. Must use boolean values (case sensitive):   ``` TRUE FALSE ``` |
| veteran | If the student is a veteran. Must use boolean values (case sensitive):   ``` TRUE FALSE ``` |
| eu\_gdpr\_subject | If the student is a GDPR Subject. Must use boolean values (case sensitive):   ``` TRUE FALSE ```   Passing TRUE indicates this student is a GDPR Subject. This field is required if you want to be GDPR compliant.  For more information, review our article on [GDPR](https://support.joinhandshake.com/hc/en-us/articles/360003819213). |

## Exploring Additional Resources

Check out these links to learn more about the student data import:

- [Importer: Student Data Formatting FAQs](https://support.joinhandshake.com/hc/en-us/articles/360008607874)
- [Importer: Uploading Your First Student File](https://support.joinhandshake.com/hc/en-us/articles/360012405373)
- [Importer Errors: Common Messages and Next Steps](https://support.joinhandshake.com/hc/en-us/articles/360001032108)
- [Importer: Re-Uploading Failed Rows](https://support.joinhandshake.com/hc/en-us/articles/360006715173)
- [Importer App: CSV Rules and File Requirements](https://support.joinhandshake.com/hc/en-us/articles/226346508)
- [Importer: Student Card IDs and Leading Zeros](https://support.joinhandshake.com/hc/en-us/articles/115001027207)
- [Importer: Date Formatting](https://support.joinhandshake.com/hc/en-us/articles/231942648)
- [Importer Help Center](https://support.joinhandshake.com/hc/en-us/sections/205492607-Importer)