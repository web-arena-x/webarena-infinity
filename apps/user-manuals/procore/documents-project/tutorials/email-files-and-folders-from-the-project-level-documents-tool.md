# Email Files and Folders from the Project Level Documents Tool

Source: https://v2.support.procore.com/product-manuals/documents-project/tutorials/email-files-and-folders-from-the-project-level-documents-tool

---

## Things to Consider

- **Required User Permissions:**

 - 'Standard' or 'Admin' permissions on the Documents tool.
- **Additional Information:**

 - Files and folders that are emailed from Procore's Documents tool are sent to recipients using a designated company-specific email address. However, the name of the person sending the email will appear as the sender name.
 - Emails are marked as 'private' by default, which means that only 'Admin' users, designated email recipients, and the sender will be able to view a record of the email under a file or folder's Email Log Report.
 - 'Private' emails are ideal for documenting and saving sensitive email correspondences in Procore while maintaining privacy settings to ensure that the record of the sent files/folders remains hidden from other users on a project.
 - You can only email files or folders to contacts or distribution groups that exist in the Directory tool. At the Project level, you are restricted to users and groups that reside in your Project Directory. Files and folders can be emailed to any user in the Directory even if they have 'None' access on your project's Documents tool.
 - Email recipients can reply to the email directly from their inbox. Any attachments to the reply email will be included along with the body of the email message. Email replies will create new entries in the email's log.

## Steps

#### Send Documents in an Email

When sending files or folders by email from the Documents tool, the system uses a specific communication thread that automatically associates all outgoing correspondence and incoming replies with the file or folder. If you are the recipient of an email, you can use your email's Reply feature to send a response to the message. When you reply to an email, a copy of the message is kept in the Emails section of the file or folder in the Documents tool.

1. Navigate to the **Documents** tool.
2. Click the file or folder you want to email.
3. Click **Emails** located in the right side panel. 
   *Note*: You can also access actions by hovering over or selecting the file or folder.
4. This will open the 'Compose Email' window. Click **Compose Email.**
5. Fill out the following fields as necessary:

   - **To**: Select one or more users or groups to email the document to.
   - **CC**: Use the CC field to include other users and keep them informed. You (the sender) will automatically be CC'ed on the email to ensure that you will also receive an email if users reply to the email.
   - **BCC**: Use the BCC field to send a copy of an email to recipients without showing their email addresses to the other recipients.
   - **Subject**: This field will automatically be populated with 'FW: [Folder or File]: [Folder or file name]'. However, you can manually change the 'Subject' line accordingly.
   - **Attachments**: You can attach additional files from the project or files from your computer. The files in the folder or the file you selected will automatically be linked in the email. Preview thumbnails of attached files will not be shown.
   - **Message**: Enter a message in the body of the email.
6. Click **Send**.

ââââNote:

- If you were CC'd on the email, you should have received an email in your inbox with a link to download the file. Recipients can either download files using the hyperlink in the email or click the 'View online' text link to view the document in Procore's web application.
- After a file has been emailed from Procore, a record of the email is stored in the Emails section for that file. The Emails section automatically hides email correspondence records from users who were not on an email's distribution list for 'private' document transfers. However, 'Admin' users can see the email even if they were not included on the email's distribution list.

#### View and Export Emails Associated with a Document

For each file and folder that you upload to the Documents tool, the system keeps historical record of when the asset was sent to other users in your Company Directory. It also tracks any replies sent to the file or folder's communication thread. If the sender marked the email correspondence as private, the Emails Log is only visible to recipients and users with 'Admin' on the Documents tool.

To export an email from the Emails Log for a file or folder:

1. Navigate to the **Documents** tool.
2. Select the file or folder.
3. Click the **Info** icon to open the Information panel.
4. Scroll down and click **Emails**. 
   *Note*: Any emails that were sent are revealed in the Emails window.
5. Click the **Export** icon on the email you want to export.