# About Mail Merge Fields

Source: https://support.joinhandshake.com/hc/en-us/articles/225749467-About-Mail-Merge-Fields

---

Handshake wants to enable you to reach your students and contacts in ways that are time efficient and effective! Mail merge fields enable you to create emails that are specifically tailored to students or contacts, adding that extra touch of personalization that will lead to higher open rates. Use the mail merge fields as detailed below–this automatically adds the student or contact information as shown on the profile or contact entry.

While composing the email text, you can use the **Insert Variables** dropdown to select a pre-formatted mail merge field. If using a mail merge field in the subject field, you will need to type in the variable you'd like to use.

For example, if you are emailing multiple recipients, and you want the subject to contain something like “Join our event, [first name]” such that the [first name] portion of the email autofills for each recipient, **you must use the exact text written below**.

|  |  |
| --- | --- |
| **Variable you are including in email** | **Exact text to copy into your email** |
| Recipient’s username | %recipient.username% |
| Recipient’s full name | %recipient.name% |
| Recipient’s first name | %recipient.first\_name% |
| Recipient’s calculated first name | %recipient.calculated\_first\_name% |
| Recipient’s last name | %recipient.last\_name% |
| Recipient’s email address | %recipient.email\_address% |
| Recipient’s Institution | %recipient.institution\_name% |

If a particular field isn't completed in Handshake, we will default to the following text:

|  |  |
| --- | --- |
| **Variable you are including in email** | **Default text** |
| Recipient’s full name | there (example: “Hi **there**”) |
| Recipient’s first name | there |
| Recipient’s calculated first name | there |
| Recipient’s email address | your email address |
| Recipient’s Institution | your institution |