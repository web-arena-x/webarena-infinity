# Importer Errors Related to Manually Created Student Accounts

Source: https://support.joinhandshake.com/hc/en-us/articles/360048144814-Importer-Errors-Related-to-Manually-Created-Student-Accounts

---

In any student upload that is importing new student accounts into Handshake, you may receive the following error messages:

- **{"success":false,"errors":{ "Attempted to update username from CURRENT USERNAME to NEW USERNAME"}**
- **{"success":false,"errors":{ "Attempted to update auth\_identifier from CURRENT AUTH\_IDENTIFIER to NEW AUTH\_IDENTIFIER "}**

## Why are these errors occurring?

These errors are caused by a combination of:

1. the student creating their account prior to being imported by your institution
2. the importer job settings

When a student creates their own account, the *username* field auto-populates to the student's *email\_address* value, and the *auth\_identifier* field is left blank.

Typically, the student's username is something other than their full email address, so when Importer attempts to create the new student account, it recognizes an existing account with the email address but lacks the permission to overwrite the username.

**Note**: If you attempt to search Handshake for students that haven't yet connected with your institution, their account will not be discoverable. For more information, check out [Managing Students Already in Handshake but not Connected to Your Institution](https://support.joinhandshake.com/hc/en-us/articles/115013134948-Managing-Students-Already-in-Handshake-but-not-Connected-to-Your-School).

## How can these errors be resolved?

To resolve the failed rows, you will need to re-upload the new student file with both settings below:

- the *This job changes identifier data* option enabled
  - When a student's **username** and/or **auth\_identifier** needs to be updated on their account, this must be selected for the change to be processed.
- the **Identifier Column** set to *email\_address*
  - With this set to *email\_address*, you are directing Importer to locate the accounts in Handshake by the email address.

![Sensitive_Data_Enabled_Image.png](https://support.joinhandshake.com/hc/article_attachments/25992976373911)

Once your file is resubmitted and processed, the student's information will be updated in the system and they will be connected to your institution, if they weren't already.

## Additional Resources

- If a student has an account that is connected to a different institution, check out [Managing Students Already in Handshake but not Connected to Your School](https://support.joinhandshake.com/hc/en-us/articles/115013134948-Managing-Students-Already-in-Handshake-but-not-Connected-to-Your-School)for next steps.
- If you are receiving the error message **{"success":false,"errors":{"email\_address":["has already been taken"]}**, refer to [Importer Error: Email Address Has Already Been Taken](https://support.joinhandshake.com/hc/en-us/articles/4421092998295) to learn more about the error and how to resolve.