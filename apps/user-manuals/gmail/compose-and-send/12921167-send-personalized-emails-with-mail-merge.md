# Send personalized emails with mail merge

Source: https://support.google.com/mail/answer/12921167

---

You can use mail merge in Gmail to send personalized email campaigns, newsletters, and announcements to a wide audience.

**Important:** Mail merge replaces multi-send mode in Gmail. When composing a message, next to the "To:" line, click Use mail merge ![](//storage.googleapis.com/support-kms-prod/rrMPZldvZmbNxXVwlo54CFFX33zsXwOHrMbN).

## Learn how mail merge works

[Mail merge in Gmail](//www.youtube.com/watch?v=tIXhg9fBEUY)

- Mail merge lets you personalize messages with merge tags, such as @firstname and @lastname. When you send a message, each recipient gets a unique copy of the email in which the merge tags are replaced with your details.
- Recipients can’t check who else you sent the message to. To easily manage conversations, you'll get the recipient’s replies in separate threads.
- If you have a large number of recipients, you can [link a spreadsheet that contains their contact information](/mail/answer/12921167#link_spreadsheet). Any column in the spreadsheet can be used as a merge tag in your message. It includes custom details for each recipient to personalize your message.

## Check your eligibility for mail merge

To use mail merge, sign in to an account with an eligible Google Workspace plan:

- Workspace Individual
- Business Standard
- Business Plus
- Enterprise Standard
- Enterprise Plus
- Education Standard
- Education Plus

## Add recipients directly to your message

1. On your computer, [open Gmail](https://mail.google.com/).
2. At the top left, click **Compose**.
   - You can also open an existing draft.
3. In the "To:" line, add recipients.
4. On the right of the "To:" line, click Use mail merge ![](//storage.googleapis.com/support-kms-prod/rrMPZldvZmbNxXVwlo54CFFX33zsXwOHrMbN).
5. Turn on **Mail Merge**.
6. In your message, enter **@**.
7. Select a merge tag:
   - **@firstname**
   - **@lastname**
   - **@fullname**
   - **@email**
8. To insert the merge tag, press **Enter**.

**Tips:**

- To ensure your message uses the correct recipient name, [check their name in Google Contacts](https://contacts.google.com/).
- To add multiple recipients, create a label in Google Contacts and group recipients. When you add the label in the "To:" line in Gmail, the grouped recipients populate automatically. [Learn how to organize contacts with labels](/contacts/answer/30970).
- If the recipient isn’t in Google Contacts, mail merge populates the first and last name based on what you enter in the "To:" line.
 - For example, if you enter "Lisa Rodriguez <lisa@example.com>" as a recipient, Gmail uses "Lisa" as @firstname and "Rodriguez" as @lastname.

## Add recipients from a spreadsheet to your message

**Important:** Contact information must be in the first tab of your spreadsheet and can only contain text.

1. On your computer, [open Gmail](https://mail.google.com).
2. At the top left, click **Compose**.
   - You can also open an existing draft.
3. On the right of the "To:" line, click Use mail merge ![](//storage.googleapis.com/support-kms-prod/rrMPZldvZmbNxXVwlo54CFFX33zsXwOHrMbN).
4. Turn on **Mail Merge**.
5. Click **Add from a spreadsheet**.
6. Select a spreadsheet.
7. Click **Insert**.
8. In the window, select the columns from your spreadsheet that have recipient info:
   - Email
   - First name
   - Last name (optional)
9. Click **Finish**.
   - Your spreadsheet is added to the "To:" line in the message.
10. In your message, enter **@**.
11. Select a merge tag.
    - Merge tags are determined by the column headers in your spreadsheet.
12. To insert the merge tag, press **Enter**.

**Tip:** When you use a spreadsheet for recipient information, check the text characters used in your column headers and email addresses.

- If a column name contains special characters other than letters or numbers, you can identify the corresponding merge tag in Gmail by its position. For example, the first column would be called "@A."
- Email addresses that contain special characters are considered invalid.

## Learn about default values for merge tags

If you have a recipient with missing information for a merge tag, you get an error message. For example, you get an error if you try to email "Sam <sam@example.com>" and use either the @firstname or @lastname merge tag. This is because Gmail can’t be sure whether "Sam" is this person’s first name or last name.

In this situation, you can:

- Enter a default value in the error message.
 - For example, for recipients who don’t have a first name, "Hi @firstname" can be "Hi friend."
- Go back to the draft and:
 - Add the missing value in the "To:" line, in Google Contacts, or in the spreadsheet you linked.
 - Remove any recipient with missing values from the "To:" line or the spreadsheet you linked.

## Find your sent messages

To find your sent messages, open the "Sent" folder in Gmail. In the message, you find a "Sent with mail merge" banner.

Understand send limits

- Standard Gmail accounts have a daily send limit of [500 outgoing messages](/mail/answer/22839).
- Work, school, and Workspace Individual accounts have a daily send limit of [2,000 outgoing messages](/a/answer/166852).

With mail merge, you can:

- Add up to 1,500 recipients in the "To" line per message
- Send to a maximum of 1,500 recipients per day
 - With mail merge on, you can send one message to 1,000 recipients and another message to 500 recipients.

To ensure you can always send regular emails, mail merge has a daily limit that works within your account's total sending capacity. For most work, school, and Workspace Individual accounts, the total daily sending limit is 2,000 emails.

Here’s how the mail merge limit is applied:

- Once you send a combined total of 1,500 emails in a day that includes both your regular and mail merge emails, you can't send any more mail merge messages until your daily quota resets.
- The remaining 500 sends in your daily limit are reserved for regular emails only.

There’s no limit to the number of unique recipients you can contact per month with mail merge.

Understand Cc and Bcc recipient limits

You can only have one recipient in the "Cc" or "Bcc" field in each message with mail merge. Any recipient added to the "Cc" or "Bcc" field is copied on each outgoing email.

- For example, if you send a message to 500 recipients with "support@company.com" in "Bcc," the "support@company.com" receives 500 copies of the message. This message would use up 1,000 of your daily send limit because recipients in the "Cc" or "Bcc" field also count toward your daily send limit.

**Important:** If you added recipients using a spreadsheet, you can’t include "Cc" or "Bcc" recipients with your message.

Unsubscribed recipients

When you turn on mail merge, a unique unsubscribe link is automatically added to the bottom of each email. Recipients can use this link to unsubscribe or resubscribe to your emails.

You get an email notification whenever a recipient unsubscribes or resubscribes to your emails. You can’t get a list of all unsubscribed recipients.

After you send a message, in the confirmation box that appears, you find the total recipients who unsubscribed and won’t receive the email.

**Important:** Recipients who unsubscribe can still receive messages sent from you without mail merge turned on or with mail merge from other accounts in the same domain. For example, if they unsubscribe from "support@company.com," they can still receive emails from "marketing@company.com."

If you use a work or school account:

- We won't discard unsubscribe data when a user account is deleted.
- Recipients can't unsubscribe from senders within their organization.

How to avoid your messages being marked as spam

When you send messages in bulk, it’s important to follow best practices that respect your recipient's inbox. Follow your local regulations and [Gmail policies](https://www.google.com/gmail/about/policy/).

To run an effective email campaign, messages you send should connect you and your recipients in a meaningful way. [Learn more about bulk email best practices](/mail/answer/10979322).

Understand mail merge limitations

Mail merge can’t be used with the following types of messages:

- Reply
- Forward
- Schedule send
- Confidential mode

You can't use mail merge to send emails from a different domain. This includes secondary domains and domain aliases that you own.

If you add an attachment, the attachment will be included in each recipient’s copy of the message. This can use a large amount of storage.

- For example, if you send a message to 500 recipients with a 10MB attachment, you would use about 5GB of your storage.

**Tip:** To save storage space, upload, rather than attach, the file to Google Drive and link to it in your message. [Learn how to share files from Google Drive](/drive/answer/2494822).

You can’t use merge tags in:

- Subject lines
- Hyperlinked text

## Related resources

- [Learn about bulk email best practices](/mail/answer/10979322)
- [Create branded emails with customized layouts](/mail/answer/10960345)