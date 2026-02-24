# Importer Errors: Common Messages and Next Steps

Source: https://support.joinhandshake.com/hc/en-us/articles/360001032108-Importer-Errors-Common-Messages-and-Next-Steps

---

Below we've listed the most common Importer error messages, their meanings, and your next steps. Additional resources are linked (as relevant) within next steps for more information.

This is not a complete list of possible errors, so if you encounter an error not listed, feel free to reach out to Support!

Errors by file type:

- [Users File](#h_01F6QSPDCDHPEYJBQ1YYCYXF86)
- [Contacts File](#h_01F6QSQ7HB6QW158M0DEP7XE67)
- [Appointments File](#h_01F6QRCTRVHB9V97CRHT15G2QG)
- [Notes File](#h_01F6QRXM4JF7D22RYPW4637X33)
- [CSV Format Errors (and other misc. messages)](#h_01F6QRY0FV580CB5RXVX6A7723)

## **Users File**

| | | |
| --- | --- | --- |
| **Error** | **Meaning** | **Next Steps** |
| "Attempted to update auth\_identifier from \_\_\_\_\_ to \_\_\_\_\_"} | You attempted to update a sensitive field value but this option was not enabled on your import job. | **Manual Imports:** Select "This job changes identifier data" when creating the job. **AWS/Upload:** auth\_identifier and username can *no longer be changed* via automatic/AWS syncs. More info on sensitive fields can be found here, [Importer: What are Sensitive Fields and How do I Change Them?](https://support.joinhandshake.com/hc/en-us/articles/223411787). \*Please note that when a student self-registers for Handshake, their email\_address and username in-app are **both** populated withthe email address they entered during registration. |
| {"email\_address":["can't be blank"]} {"username":["can't be blank"]} {"first\_name":["can't be blank"]} | You attempted to update or create a user but did not include an email address, username, or first\_name value | Please review the required fields for student uploads here, [Importing Student Data](https://support.joinhandshake.com/hc/en-us/articles/233086688). To create or update a student, you must always include **email\_address**, **username**, and **first\_name** for that student. |
| {"auth\_identifier":["has already been taken"]}} {"card\_id":["has already been taken"]}} | You attempted to create a new user but auth\_identifier or card\_id has already been taken by another account. | Ensure that you actually intend to create a new user, rather than updating an existing one. **Note**: If you update email\_address and username for someone at the same time, it will attempt to create a new user with the information in that row. These two fields must be updated separately for existing users. This student may exist under a different user/email. Make sure to look up their record in Handshake to confirm. |
| {"email\_address":["is already in use"]}}: | You attempted to create a new user but the email\_address is already in use on an account with a different username. | **email\_address** must be unique to all of Handshake, so importer will reject when it is imported with a different username. To fix, resubmit the failed rows manually and switch the primary identifier column from "username" to "email\_address". This will search for accounts using the email address rather than the username. You will also need to toggle on "This job changes identifier data" so that importer has permission to update the username. Alternatively, search for the student's account in Handshake and manually update the username. |
| {"primary\_education.end\_date":["must be a date on or after primary\_education:start\_date"]}} | You attempted to set an end\_date that was before the student's current start\_date.   **Example:** You are only providing **primary\_education:end\_date** on the file and the student's profile has a start date after the end date included in the student upload. | **primary\_education:end\_date** should have a value of \*\*CLEAR\*\* (Every letter capitalized with two asterisks at the beginning and end of the word) rather than <blank> if you do not have a new end\_date for this student. When using \*\*CLEAR\*\* the analysis will say it is an invalid date value, but will accept it nonetheless when the job is processed. Alternatively, set a valid projected end\_date that is after the student's current start\_date. |
| "exclude\_from\_sync":true,"errors":["User is marked as excluded from sync and cannot be updated."]} | You attempted to update a user via import but they have an "Exclude from Syncs" option selected on their profile in-app. | Verify first that you do want to manage this specific user via syncs (rather than in-app). Go to this user's account in Handshake, then the "Account Tab". Uncheck "Exclude from Automatic Syncs" about halfway down the page. |
| {"mobile\_number":["is invalid"]}} | You used a mobile number that is more or less than 10 digits | Please only use valid domestic 10-digit phone numbers, or leave the field blank at this time.  This value is used for text message verification for the mobile application, and eventually newer features. |
| {email\_address":["has already been taken","conflicts with another primary account"]}} | There is another student account with the same email address on Handshake. | Add the student by email in the Manage Students tab on the Handshake app. If the error that student is connected to another institution shows, create an account with an alternate email address or contact Support for assistance on the connection request. |

## **Contacts File**

| | | |
| --- | --- | --- |
| **Error** | **Meaning** | **Next Steps** |
| {:status=>"invalid", :error\_code=>"email\_account\_invalid", :error=>"Email account invalid", :http\_status=>200, :request=>"email@email.com", :valid=>false} | This contact email failed validation (or test bounced/invalid email address) | All contacts are validated during import, and any emails that bounce or are flagged as invalid will result in this error. In these cases, you should update any addresses you can, and double-check for any typos in the address, then re-upload. |

## **Appointments File**

| | | |
| --- | --- | --- |
| **Error** | **Meaning** | **Next Steps** |
| "student":["can't be blank"]: | An existing student with this email address was not found in Handshake. | This student needs to be created in Handshake and associated with your institution prior to adding this appointment. |
| "staff\_member":["can't be blank"]: | An existing staff member with this email address was not found in Handshake | This career services user needs to be created in Handshake and associated with your institution prior to adding this appointment. |
| "time\_zone":["is not included in the list"]: | Erroneous Error Message.  Usually comes before student or staff\_member "Can't be blank" error, but does not actually indicate an issue. | Ignore this part of the error message. |
| " import\_identifier":["has already been taken"] | This import\_identifier was used for another appointment in the same import file, or was used in a previous 'appointments' import. | Import\_identifier has to be completely unique to a single appointment, and is later used to attach notes to the appointment (via 'Notes' file import) **Suggestions for unique identifier:** \* (school)(file type)(date)(number) \*\* jcuappointments06272016100  \*\* jcuappointments06272016101  \*\* " " " " " "102, 103, 104, etc |

## **Notes File**

| | | |
| --- | --- | --- |
| **Error** | **Meaning** | **Next Steps** |
| {"Could not find identifiable"} | The identifier or identifiable\_id used in this row could not be matched to any existing id in Handshake. | If using **identifiable\_id**, make sure this is the correct ID from the URL of the event or appointment in Handshake. If using **identifier** (for previously imported events or appointments), make sure this matches the respective **import\_identifier** from your previously imported Events or Appointments file. If using **identifier**(for users), make sure to include the **user\_type** field, and specify 'Students' or 'Career Services'.  For users or contacts, **identifier** is their email\_address value(user must already exist in Handshake prior to importing notes) Review [Importing Notes](https://support.joinhandshake.com/hc/en-us/articles/115002426128) for further detail. |

## **CSV Format Errors (and other misc. messages)**

| | | |
| --- | --- | --- |
| **Error** | **Meaning** | **Next Steps** |
| | A special character was found in your CSV file, but the file was not in UTF-8 format. | Special characters are supported in imports, but your file must be saved in CSV UTF-8 format before submitting to the importer. Please review [Importer App: CSV Rules and File Requirements](https://support.joinhandshake.com/hc/en-us/articles/226346508) for info on correcting this with manually generated files. |
| "This job has users with email addresses not associated with your school. These users will be skipped. If you feel this is an error and this domain belongs to your institution, please contact support." | You are attempting to import users with email\_address values containing domains not listed in your importer settings. | If the email domains listed in the warning (further down the import job page) should be associated with your school, please open a new support request to add these. If the email domain is associated with another institution, please find an alternate/personal email for these students.  These emails and domains should be managed by the respective institution (the student may have another existing account with their previous institution). More info about this here, [Handling Students with .edu Emails Associated with Other Institutions](https://support.joinhandshake.com/hc/en-us/articles/360001151208) |
| Maximum row allowed error message.png "The file you uploaded has (over 199,999) rows. The maximum number of rows allowed is 199,999." | You are attempting to import more than 199,999 rows through the importer, which exceeds the limit. | Only jobs with 199,999 and less rows can be imported. Exceeding this bandwidth can potentially cause slowdown and interruptions with transferring information between the Importer tool and Handshake.    If you need to import more than 199,999 rows, it is suggested that you import multiple files, each with less than 199,999 rows. |