# Importer Error: Email Address Has Already Been Taken

Source: https://support.joinhandshake.com/hc/en-us/articles/4421092998295-Importer-Error-Email-Address-Has-Already-Been-Taken

---

The error message **{"success":false,"errors":{"email\_address":["has already been taken"]}**appears on the failed rows file when the email address being imported is already in use in Handshake.

This may happen because:

- the student is connected to your institution, but has a different username
- the student is in Handshake, but not connected to your institution
- the student is in Handshake, but connected to different institution

## Why is this error occurring?

When a student creates their own account in Handshake, before being imported by your institution,  their username is automatically assigned as the email address used during the account creation. To learn more about students creating their own account, refer to [How Students & Alumni Can Request to Access Handshake](https://support.joinhandshake.com/hc/en-us/articles/360006170614).

If your institution uses a different username, other than the student's email address, and you upload a file into Importer, the row will likely fail due to the**Identifier Column** setting within your institution's file.

The **Identifier Column** is a setting that directs Importer to create or update an account in Handshake.

**Note**: the**Identifier Column** does not change any information on the file that is being imported, it only directs Importer to the specific column to identify the users in Handshake.

![Identifier_Column_Image.png](https://support.joinhandshake.com/hc/article_attachments/25995122862231)

For example, if your**Identifier Column** is set to *username*, Importer will use the *username* column to search accounts in Handshake.

- If the username listed on the import file *is* found, the system will begin to *update* the information to match what is on the file.
- If the username listed on the import file is *not* found, the system will begin to *create* an account for that username.
 - If the email address is found in Handshake, the row will fail. This is what causes the error message **{"success":false,"errors":{"email\_address":["has already been taken"]}**.

## How do I resolve this error?

One thing to consider when addressing this error message is, how many students on the import file received this error message?

- If less than 5, these students can be manually updated in Handshake.
 - Before taking action to fix this error, you will need to first confirm whether or not the student is connected to your institution already. For more information on this, skip to [Confirm a students connection](#h_01FVJKXZWJM3NYG44DK5AC0QR4).
- If more than 5, follow the steps below for re-uploading your file.

#### 

#### Re-uploading your file

1. Prior to upload, delete the last two columns: "status" and "response".

*Make sure that your file download did not remove any leading zeros (usually within usernames, card, auth ID fields). Learn more about* [Importer: Student Card IDs and Leading Zeros](https://support.joinhandshake.com/hc/en-us/articles/115001027207)*.*

2. When uploading the file to the Importer, select**This job changes identifier data**, and change **the identifier to email\_address**.

![Change_Indentifier_Column_Image.png](https://support.joinhandshake.com/hc/article_attachments/25995104332951)

3. Click **Save Job**.

Once your upload has been submitted and processed, the students information will be updated with what is in the file, and they'll be connected with your institution if they weren't already.  This includes students that are in "Waiting" or "Successful" status on the user approval page - but excludes students that are in "Rejected" or "Failed" status.

For students with a "Rejected" or "Failed" status, skip to [Student is in Handshake, but not connected to your institution](#h_01FTVG1NGX0N09KYW75C3A3BTS) below.

### Confirm a students connection

As a career services user, you can only manually update accounts that are connected to your institution.

To check this, go to the Manage Students overview page in Handshake and search the student by their email address, name, or username within the search box. If the student is connected to your institution, they will appear as a result from your search.

![Manage_Student_Search_Bar_image.png](https://support.joinhandshake.com/hc/article_attachments/25995122864407)

- If the student is connected to your institution, follow the steps for [Student is connected to your institution, but has a different username](#h_01FTVG1NGX0N09KYW75C3A3BTS).
- If you are unable to locate the student in Handshake, follow the steps for [Student is in Handshake, but not connected to your institution](#h_01FTVG1NGX0N09KYW75C3A3BTS).

### Student is connected to your institution, but has a different username

If a student has an account in the system with a different username than presented on the import file, you can manually update the accounts username in Handshake.

1. Locate the students profile in Handshake, and then click the account tab in the upper-right corner of the page.

![Student_Account_Tab_Image.png](https://support.joinhandshake.com/hc/article_attachments/25995104330903)

2. Scroll to the **Username** field and manually update it to the correct username for your institution.

3. Click the green **Update** button, located in the lower-right corner to save.

![Username_Field_Image.png](https://support.joinhandshake.com/hc/article_attachments/25995122869271)

On the next upload, Importer will recognize the username and update the relevant account information, instead of attempting to create a new account.

### Student is in Handshake, but not connected to your institution

If a student is not connected to your institution, or was previously "Rejected", you can *not* manually update their account.

To connect a student to your institution, follow the steps outlined in [Add an Existing Student Account to Your Institution](https://support.joinhandshake.com/hc/en-us/articles/360009480274-Student-Login-Update).

Once the student is added, you will need to either:

- Update the username on the profile manually
 - For more information, go to the [update students username manually](#h_01FTVHG9K1N9374AYFNQEF7F16) section in this article.
- Re-upload the file into Importer

### Student is in Handshake, but connected to different institution

If a student has an account connected to a different institution, you will not have the option to access or update their information in Handshake. Refer to [Managing Students Already in Handshake but not Connected to Your Institution](https://support.joinhandshake.com/hc/en-us/articles/115013134948) for more information.