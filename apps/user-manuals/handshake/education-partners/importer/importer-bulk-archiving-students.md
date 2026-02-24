# Importer: Bulk Archiving Students

Source: https://support.joinhandshake.com/hc/en-us/articles/115001497067-Importer-Bulk-Archiving-Students

---

If you need to archive a set of student accounts that no longer attend your institution, you can do so via the [Importer](https://importer.joinhandshake.com/login).

*When an account is archived, the email address associated with the account remains in Handshake, preventing any other student account from being created with that same email*.

Click on the expandable headers to learn more about the process.

If you need to update graduating students to alumni, we recommend following the steps outlined in [Importer: Updating Graduating Students to Alumni](https://support.joinhandshake.com/hc/en-us/articles/227482608).

**Consider the following before archiving student accounts:**

- Students accounts should be archived upon student request or if absolutely necessary.
- Accounts can be unarchived - however, if other career services members at your school are unaware of a student’s account being archived, they may suggest that the student create a new account. At this time, accounts cannot be merged unless they meet the qualifications as listed in [Managing and Merging Duplicate Student Accounts](https://support.joinhandshake.com/hc/en-us/articles/115002657968). If they don't meet those qualifications, the data cannot be connected between two accounts.
- Data and information from an archived account may include: appointment history, fair participation, job applications, experiences, and more. These key points could help shape their career growth.
- Your school will be unable to view archived students on the Manage students page if the students log in to their account after being archived. Learn more about the student archive process in [What Happens When I Archive a Student?](https://support.joinhandshake.com/hc/en-us/articles/37658603402519)
- Alumni with archived accounts can still use Handshake post-graduation, they just won't be connected to your school.
- If your school currently runs automated jobs through Importer, the file will need to be updated to reflect students whose accounts have been archived. If a student requests reactivation, the file will need to be updated once more to reflect this change.

**Prerequisites**

To archive accounts via the Importer, one must have access to the Importer tool. If you don't currently have access to the Importer tool, refer to [Importer: Gaining Access](importer-gaining-access.md).

**Preparing the file**

To archive students, the file must contain headers for all of the *required fields* used in a standard upload. Additionally, you'll need to add a column for **disabled**, and set it to **TRUE**.

**Important**: while all of these headers are required to be present, only **email\_address**, **username** and **disabled** are required to have values in the columns under their headers. The rest of the columns can be left blank under the headers.

For an example, use the following specifications below, or refer to the example .csv file attached at the the bottom of the article.

|  |  |
| --- | --- |
| **Header** | **Description** |
| **email\_address** | Student's Handshake account email |
| **username** | Student's username (must match what's in Handshake) |
| **auth\_identifier** | Student's auth identifier for SSO (must match what's in Handshake) |
| **first\_name** | Student's first name (required only for new records) |
| **school\_year\_name** | The student's existing school year that is listed in Handshake. |
| **primary\_education:cumulative\_gpa** | The student's cumulative GPA listed in Handshake. Please [contact support](https://support.joinhandshake.com/hc/en-us) if you are not able to include this information in your file. |
| **primary\_education:major\_names** | The student's listed major(s) that are populated on their Handshake profile. |
| **primary\_education:education\_level\_name** | The student's education level that is populated on their Handshake profile. |
| **disabled** | Set to "TRUE" |

To learn more about the required fields in a standard upload, refer to [Importing Student Data.](https://support.joinhandshake.com/hc/en-us/articles/233086688-How-to-Import-Student-Data)

**Importing the file**

Use the process outlined in [Importing Student Data](https://support.joinhandshake.com/hc/en-us/articles/233086688#:~:text=Uploading%20Your%20Student%20File) to load your file into the Importer, and successfully run it.

If you need to reactivate a student account in Handshake, refer to [How to Reactivate an Archived Student](https://support.joinhandshake.com/hc/en-us/articles/230484588).