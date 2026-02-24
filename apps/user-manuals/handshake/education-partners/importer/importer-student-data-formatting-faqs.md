# Importer: Student Data Formatting FAQs

Source: https://support.joinhandshake.com/hc/en-us/articles/360008607874-Importer-Student-Data-Formatting-FAQs

---

We’ve sourced a variety of FAQs from across the Handshake network to help you consider your student data formatting. Use this to navigate a few edge cases and specific workflows. A few things to keep in mind:

- **Keep this**[**additional article**](https://support.joinhandshake.com/hc/en-us/articles/233086688)**handy** for the exact specs, example CSV download and contextual descriptions on each of headers/fields for the student data import
- **Leverage our**[**Handshake Community**](https://support.joinhandshake.com/hc/en-us/community/topics) for additional insights from over 600+ university partners
- **It's ok to have a different formatting approach - just** **test**, test, test your functionality to ensure you’re comfortable with any workflow tradeoffs.

## **Importer Functionality FAQs:**

**Q: If I import user data, will it automatically send an invite or notification?  Will they have to confirm their accounts?**

No, the importer will never send a notification to any students or contacts imported in the data file. Accounts will already be marked as confirmed (so they will not receive a confirmation email).

Keep in mind, when students do log in they will be prompted to "activate" their profiles by agreeing to the ToS and Privacy Policy. Learn more about that process in this article about [student onboarding](https://support.joinhandshake.com/hc/en-us/articles/360007508853) and and this article about [student privacy](https://support.joinhandshake.com/hc/en-us/articles/360000951508)

**Q: If I import a blank field, will it clear out the data?**

The importer will not override or clear out data if you leave that blank. You have to explicitly enter **\*\*CLEAR\*\*** (Every letter capitalized with two asterisks at the beginning and end of the word) in any non-True/False fields to clear out what's been entered into Handshake. Leaving the information blank on each sync will just skip that field for that row/user as it is unchanged.

***\*\*Please Note***: The one exception to this is the field **system\_label\_names** -- if you have uploaded system labels to a student's account, these must be listed *each time* this field is included in a student sync file, otherwise all system labels on the student's account will be cleared out.

**Q: There are duplicate students in my file - will they import successfully?**

No, the importer will skip any rows with duplicates in any of the sensitive fields (email, username, card\_id, and auth\_id). We recommend removing all duplicate records, and ensuring that you are only importing the most accurate student record.

**Q: How can I learn more about the using the Importer?**

Explore these resources if you’re just getting started:

- [Importer overview](https://support.joinhandshake.com/hc/en-us/articles/222574167)
- [Common Importer errors](https://support.joinhandshake.com/hc/en-us/articles/360001032108)
- [How to re-upload failed rows](https://support.joinhandshake.com/hc/en-us/articles/360006715173)
- [What are sensitive fields and how do I change them?](https://support.joinhandshake.com/hc/en-us/articles/223411787)

**Q: I am currently uploading student data via AWS and have scheduled recurring student syncs. I am receiving emails informing me that these jobs have been processed, but when I log into my Importer account, I don't see any of them. What happened to these jobs?**

Each time a job is uploaded and processed *without any errors* (either through AWS or a manual upload to the Importer), it will be automatically archived. This is so that the list of jobs you will view when you are logged into your Importer account will only be jobs that need your attention (due to failed rows, or a file analysis failure).

If you would still like to view any of these jobs, you can do so by following the link provided in the email notifications that are sent out each time one of your jobs is processed. If you are not receiving these emails, contact Support to request to be added to the email recipient list for your institution's Importer account.

## **Student Data Formatting FAQs:**

**Q: If a student has completed their undergraduate degree at our school and is still attending, but now pursuing a graduate or advanced degree, how should we format their import record?**

 You’ll only import **one** education record for each student -- choose the most recent or most relevant degree/program. Students will always be able to add in the additional education history for employers to review on their profile, but you’ll want the qualifications that you’re importing to reflect their current program. These imported details are what will connect to employer job, interview, and event qualifications.

**Q: Our GPA is not on a 4.0 scale - can we import a different value?**

This must be a value between 0 and 4 with no more than 2 hundredths (example: 3.75). Employers can use GPA as a qualification on job postings - so this must be a value that translates to student profiles across the entire network.

**Q: How do we format students with dual majors?**

In Handshake, you can import multiple options for **primary\_education:major\_names** as long as they are separated by a semicolon. All imported majors will be displayed on the student's profile and tied to qualifications on for job postings.

**\*\*Please Note**: The field for **primary\_major\_name** (singular) *is different* - this is only used for Analytics and the First Destination Survey to show primary program of study. This field is not displayed on the student's profile.

**Q: We have a specialty certificate program - how should we create the student records?**

 This will greatly depend on how you aim to organize and report on this student data. Additionally, you should consider if - and how - this information should display to employers who review student applications and public profiles.

Outline your functionality requirements **(in addition to the core student data fields)**, and use this table to determine your formatting.

 

|  |  |  |
| --- | --- | --- |
| **Fields to consider:** | **Example content:** | **Why:** |
| **primary\_education:education\_level\_name** | “Certificate” | Employers use education level, major groups, and school year as qualification fields on job postings. Standardizing this helps ensure your students are qualified for relevant positions |
| **school\_year\_name** | Leave this field blank OR  select a standard year such as “Junior” or “Senior” |
| **primary\_education:primary\_major\_name** | “Certificate Program Name” | This field will **not** show up on a student's profile, and is primarily used for FDS.  This is the student's primary major. Only 1 major can be supported in this field. The major name *must already be added* to the **primary\_education:major\_names**field in order for the primary major to be backfilled into Handshake. |
| **system\_label\_names:** | “certificate-program-name” | This will not display externally, but can be help for tracking, filtering, and reporting by the Career Services team |

**Q: We have a residential college and/or manage another satellite campus that doesn't need another formal "career center" created -- how should we format our student data?**

This likely depends on how both you and employers need to see and manage these students. [Career Centers](https://support.joinhandshake.com/hc/en-us/articles/360000700747) can help you for manage distributed campuses, but keep in mind students are not attached to a Career Center - the filtering is dependent on the formatting from your student data upload.

Consider using the following data fields, and leverage [saved searches](https://support.joinhandshake.com/hc/en-us/articles/219132657)to segment and filter your student population.

- **campus\_name:**Typically used for schools with multiple campuses. This is not tied to any requirements/functions or employer visibility in Handshake, but you can add and filter on it in the Insights reporting tools
- **system\_label\_names:** Use this field to import any custom tags or labels from your SIS. You can import multiple system labels for each student by separating with a semi-colon. Keep in mind system labels can be tricky for a few reasons:

- Leaving this field blank in your import will clear all system labels in Handshake for that respective student.  System labels are added or removed in every student sync that includes this column, based on exactly what you have in this field.
- It's difficult to remove a system label once created, but you can [remove and add as a normal label](https://support.joinhandshake.com/hc/en-us/articles/115014929107).
- We first recommend exploring the [different types of labels and how they are used in Handshake](https://support.joinhandshake.com/hc/en-us/articles/360006639854)

- **primary\_education:college\_names:** This is usually used for a student's academic college(s) and will be visible to both students and employers. Career Services can filter on this and use as a qualification. Please refer to [Importer: Uploading Your First Student File](https://support.joinhandshake.com/hc/en-us/articles/360012405373) for more information.

**Q: Our institution majors won’t directly map to Handshake major groups, can we add options to your major groups? Or customize the industry list pick list?**

No, these major groups and pick lists are standardized across the platform. Major groups represent broader fields of study and enable employers to easily evaluate and identify student qualifications across the entire Handshake network.

The major names that you import should reflect the **full title** of the students degree at your institution. After the student file is imported, this will populate your majors in Handshake and  you will map these major names to major groups to ensure students are qualified for postings.

However, Employers (and the individual student) will always see your custom (imported) major name on the students profile when reviewing their application or profile details - which is why the major full name (not a code) is important. [Learn more about major mapping here](https://support.joinhandshake.com/hc/en-us/articles/218692828)

**Q: If a student has a profile at another school, can we import that email or connect to that existing account in Handshake?**

You **cannot** import or update students with .edu email domains that are not associated with your school. We only enable 1 student account for every 1 email address.

This is because email address is currently the only identifying value that must be unique in Handshake. If a student were to transfer or will attend a grad program at another institution or transfer, we need to ensure they have a separate, accurate record at that school.

Additionally, if students have an active account (typically as an alumni) at another school, they are not able to connect that existing account to the account created at your school. To access the different school instances, they would need to log in with the two separate sets of credentials (i.e. 2 different emails and passwords).

Explore this article to learn more about the [Importer restrictions for other .edu emails](https://support.joinhandshake.com/hc/en-us/articles/360001151208)

**Q: Can we format a custom gender for students who do not identify with the binary male/female options in the file specifications?**

Yes - any custom values will be imported as they appear in your file. Some schools will leave this field**blank** in the data file and allow the student to self-identify their custom gender on their profile:

![Screen_Shot_2018-08-30_at_7.38.15_AM.png](https://support.joinhandshake.com/hc/article_attachments/26001429014935)