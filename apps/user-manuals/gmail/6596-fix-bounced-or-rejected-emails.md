# Fix bounced or rejected emails

Source: https://support.google.com/mail/answer/6596

---

When you send an email and it fails to reach your recipient, you get an automated bounceback email with an error message. To understand why your email doesn’t reach your recipient, review the details in the bounceback email and the troubleshooting guidance in this article.

## Before you begin

- If you can't sign in to Gmail,[learn how to recover your Google Account or Gmail](/accounts/answer/7682439).
- If you're a business or organization that sends email to personal Gmail accounts (@gmail.com or @googlemail.com), [learn about the email sender guidelines](/mail/answer/81126).

## Step 1: Find the error message

When your message bounces, Gmail automatically sends you an email that explains what happened.

1. On your device, open [Gmail](https://gmail.google.com/).
2. Go to your:
   - Inbox
   - Spam
3. Check for an email from "Mail Delivery Subsystem (mailer-daemon@googlemail.com)."
   - The subject line is often "Delivery Status Notification (Failure)."
4. Open the email.
5. Review the error message that explains why Gmail can’t deliver your email.

## Step 2: Review the error & find your solution

To troubleshoot your problem, review the error message in the bounceback email. Check for phrases that match the errors below:

- [The recipient's email address doesn’t exist](/a/answer/6596#email_noexist)
- [Your email is flagged as spam or temporarily rejected](/a/answer/6596#spam)
- [You reached the limit for sending email](/a/answer/6596#limit)
- [There’s a temporary problem with the recipient’s inbox](/a/answer/6596#temporary)
- [The recipient’s inbox is out of storage space](/a/answer/6596#storage)
- [You get a "HELO/EHLO" error message](/a/answer/6596#helo)

### The recipient's email address doesn't exist

#### Why it happens

- The email address doesn't exist.
- The email address has a typo or another error in it, either before or after the "@" symbol.

#### What you can do

- Check for common errors like:
  - **Spelling errors:** john.doe@gmal.con
  - **Quotation marks:** john**"**doe@gmail.com
  - **Dots at the end of the address:** john.doe@gmail.com**….**
  - **Spaces before or after an address:** john. doe@gmail.com
- Review your contact's information:
  - Make sure you have the person's current email address, as their email address may have changed.
  - If possible, ask the person for their email address.
  - To check your contact information, go to [Google Contacts](https://contacts.google.com/).

### Your email is flagged as spam or temporarily rejected

#### Why it happens

- Something in your message, like links, attachments, or text, triggers the recipient's spam filters.
- This can also happen when you send a message to a large group of recipients at once.

#### What you can do

- Remove links to websites or text that ask for personal information.
- If you email a large number of people, put all recipients in a Google Group. Send the message to that single group address. [Learn about Google Groups](/groups/answer/46601).
- If you forward your email, [learn about best practices for forwarding email to Gmail](/mail/answer/175365).

### You reached the limit for sending email

#### Why it happens

- To prevent spam, personal Gmail (@gmail.com) accounts have a limit on the number of emails you can send per day.
- You specifically get this error message when you send:
  - More than 500 emails in a day
  - One email to more than 500 recipients

#### What you can do

- This error is temporary. You can send emails again within 24 hours. [Learn more about limits for sending and getting email](/mail/answer/22839).
- If you use your Gmail through your work, school, or other organization, there are different limits when you send an email. [Learn about Gmail sending limits in Google Workspace](/a/answer/166852).

### There's a temporary problem with the recipient's inbox

#### Why it happens

- The recipient's email server is busy, offline, or experiences a temporary technical issue.

#### What you can do

- Send the message again at a later time.
- If you still can't reach the recipient:
  - Check if there are any mistakes with their email address.
  - Reach out to your recipient's email provider for support.

### The recipient's inbox is out of storage space

#### Why it happens

- Your recipient is out of Google storage and can’t receive new messages.

#### What you can do

- The recipient must clear space in their account storage before they can receive new email.
  - Storage is shared across Google Drive, Gmail, and Google Photos. In addition to emails, your recipient may also need to delete older files or photos.
- You can let them know how they can [manage their storage in Drive, Gmail, and Photos](/mail/answer/6374270).

### You get a "HELO/EHLO" error message

When the mail server that responds to Google identifies itself with an invalid value, you get a "HELO/EHLO argument invalid" error message. For example:

`501 5.5.4 Empty HELO/EHLO argument not allowed, closing connection.  
501 5.5.4 https://support.google.com/mail/?p=helo`

`501 5.5.4 HELO/EHLO argument “...” invalid, closing connection.  
501 5.5.4 https://support.google.com/mail/?p=helo`

When mail servers talk to each other, they're required to identify themselves to the receiving server with a HELO or EHLO command. This identification should be the sending machine's fully-qualified IP address or domain name (like mail.example.com). Any other value is considered invalid and can reject your email.

This error usually occurs with devices like printers, scanners, and fax machines that also send mail.

#### What you can do

- Contact your email provider.
  - If you use Gmail for work or school, ask your administrator to send the fully-qualified domain name or IP address of the sending server when they contact Gmail servers.
- For more information about the HELO/EHLO error message, [go to RFC 5321, section 4.1.1.1](https://datatracker.ietf.org/doc/html/rfc5321#section-4.1.1.1).

## Related resources

- [Limits for sending & getting mail](/mail/answer/22839)
- [Why has Gmail blocked my messages?](/mail/answer/188131)