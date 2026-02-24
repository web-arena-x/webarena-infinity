# Importer: What are Sensitive Fields and How Do I Change Them?

Source: https://support.joinhandshake.com/hc/en-us/articles/223411787-Importer-What-are-Sensitive-Fields-and-How-Do-I-Change-Them

---

**Sensitive fields are identifying fields in a student file (manually uploaded to the Importer or received in an automatic student sync).  The following are currently considered sensitive fields:**

- username
- auth\_identifier

**\*\*As of 10/3/18**

- **email\_address and card\_id are no longer considered sensitive fields in data imports!**
- **AWS/Automated upload will automatically update emails if <10% of total rows have email address changes.  If >10%, no emails will be updated during that sync.**
 1. ex: 1000 rows in your AWS upload/sync file, 100 rows have new emails: No emails will be updated during that import. (If only 99 rows have new emails, these will update!)
- **auth\_identifier and username can no longer be changed via automatic/AWS syncs**

If your AWS upload/automatic sync has enough email\_address updates to exceed the 10% limit, or you've changed username or auth\_identifier for any students, instead of processing these individual rows successfully and updating the email\_address/auth\_identifier/username in Handshake, these specific rows will be "failed" on your importer job and you will have to process this change by downloading these failures and manually uploading a file with 'This job changes identifier data' selected (Please see below for manual steps!).

**\*\*As of 10/3/18: You will no longer need to opt-in to update email\_address or card\_id via automatic syncs (username and auth\_identifier can no longer be updated via automatic syncs, and require manual import as seen below)!**

**Identifying Sensitive Fields Errors on the Importer**

In order to identify the rows in your student file upload that failed because of a sensitive field, follow these steps:

1. Go to your job on the importer. Click "View/Download Results" in the top right hand corner.

![](https://support.joinhandshake.com/hc/article_attachments/25997655794583)

2. Click "Download Failed Rows CSV":

![](https://support.joinhandshake.com/hc/article_attachments/25997655795223)

3. Scroll to the far right column on the download spreadsheet, you will see two additional columns, with the error message for the sensitive fields error in the last column.

![](https://support.joinhandshake.com/hc/article_attachments/25997636022807)

**I've received an error "attempted to change sensitive fields" - What do I do?**

- This occurs when any change is made to auth identifier or username
- Review the user/s that failed, determine if any sensitive field has been updated since the last sync
- Was this an intended change?

- If yes, see ***'How-To Change Sensitive Fields'***
- Otherwise, confirm that the values being sent through to Handshake are accurate

- If this change was not intended, these users do \*not\* have duplicate accounts (e.g. with a personal email), and there are no duplications being sent in the user file, please contact us to assist with the issue.

**How do I know if there are duplicate sensitive fields in my file?**

- When uploading to the Importer, you'll receive feedback from the analyzers indicating any duplicate sensitive field values found
- Use a personal program (such as Excel or Numbers) to compare possible duplicate records

**How do I know if this sensitive field is associated to another account within Handshake?**

- These fields should be unique to each user at your school.

- If these fields are not unique to the student, please contact your Handshake Relationship Manager immediately to go over alternatives for handling this situation

- If sensitive field is associated ("already taken") to another account, this is generally due to the user having multiple Handshake accounts
 - The undesired account is then archived

- e.g. User signed up with personal email address but associated their school username and auth\_identifier to their account
- When school attempts to sync this user with their school email, username, auth\_id, that user will fail due to this information being associated with another account
- This generally requires a deconfliction that happens at the Student and School level (to determine which account they want to retain)

**How do I change sensitive fields manually?**

1. Re-upload the failed rows spreadsheet that you downloaded from the original job. Prior to upload, delete the last two columns: "status" and "response".

2. When uploading the file to the Importer, make sure that the field for "This job changes identifier data" is selected, as shown below:

![](https://support.joinhandshake.com/hc/article_attachments/25997636025111)