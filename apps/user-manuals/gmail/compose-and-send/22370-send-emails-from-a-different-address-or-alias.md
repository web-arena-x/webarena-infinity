# Send emails from a different address or alias

Source: https://support.google.com/mail/answer/22370

---

If you own another email address, you can send mail as that address. For example:

- Yahoo, Outlook, or other non-Gmail address
- Your work, school, or business domain or alias, like @yourschool.edu or youralias@gmail.com
- Another Gmail address

**Tip**: You can send emails from up to 99 different email addresses.

![An animation showing how to send emails from a different address or alias in Gmail](//storage.googleapis.com/support-kms-prod/DP39FEtIZcefksnInfCe917EEKW06dUmBzlQ)

## Step 1: Add an address you own

1. On your computer, open [Gmail](https://mail.google.com).
2. In the top right, click Settings ![Settings](//lh3.googleusercontent.com/p3J-ZSPOLtuBBR_ofWTFDfdgAYQgi8mR5c76ie8XQ2wjegk7-yyU5zdRVHKybQgUlQ=h36) ![and then](//lh3.googleusercontent.com/QbWcYKta5vh_4-OgUeFmK-JOB0YgLLoGh69P478nE6mKdfpWQniiBabjF7FVoCVXI0g=h36) **See all settings**.
3. Click the **Accounts and import** or **Accounts** tab.
4. In the "Send mail as" section, click **Add another email address**.
5. Enter your name and the address you want to send from.
6. Click **Next Step**![and then](//lh3.googleusercontent.com/QbWcYKta5vh_4-OgUeFmK-JOB0YgLLoGh69P478nE6mKdfpWQniiBabjF7FVoCVXI0g=h36)**Send verification**.
7. For school or work accounts, enter the SMTP server (for example, smtp.gmail.com or smtp.yourschool.edu) and the username and password on that account.
8. Click **Add Account**.

## Step 2: Confirm the address

1. Sign in to the account you added.
2. Open the confirmation message you got from Gmail.
3. Click the link.

## Step 3: Change the "From" address

1. In the message, click the "From" line.  
   (If you don't see this, click the space next to the recipient's email.)
2. Select the address to send from.

I can't find my confirmation email

- Check your Spam or Bulk Mail folders for a message from send-as-noreply@google.com.
- If you're trying to add your work or school account, ask your administrator to configure your [domain alias](https://support.google.com/a/answer/53295) and [email alias](https://support.google.com/a/answer/33327).

My recipients see my Gmail address

If your recipient uses Outlook or another mail service, they might see something like, "From yourname@gmail.com on behalf of othername@otherdomain.com."

Your recipients might also see your original @gmail.com address if you:

- Set up an [out of office reply](25922-send-an-automatic-reply-when-youre-out-of-office.md)
- Create a [filter](6579-create-rules-to-filter-your-emails.md) with automated response
- Have a full mailbox, and your recipient gets notified

Remove an email address or alias

If you don’t want to send emails from an alias or if the alias is invalid, you can remove the email or alias. If you send an email from an invalid alias, you get a bounce email.

1. On your computer, open [Gmail](https://mail.google.com/).
2. At the top right, click Settings ![Settings](//lh3.googleusercontent.com/p3J-ZSPOLtuBBR_ofWTFDfdgAYQgi8mR5c76ie8XQ2wjegk7-yyU5zdRVHKybQgUlQ=h36) ![and then](//lh3.googleusercontent.com/QbWcYKta5vh_4-OgUeFmK-JOB0YgLLoGh69P478nE6mKdfpWQniiBabjF7FVoCVXI0g=h36) **See all settings**.
3. Click the **Accounts and import** tabor **Accounts** tab.
4. In the "Send mail as" section, next to the email address you want to remove, click **Delete**.

**Tip:** If you get a bounce email from a valid email address and need to reverify it, you must delete the "Send mail as" email address then add it again.

## Always send from a different address

If you want to always send from your other address, you'll need to change both your default "From" and "reply-to" address. If you only change the "From" address, replies will go to your original Gmail address by default.

Change default "From" address

To always send email from a different address or alias:

1. On your computer, open [Gmail](https://mail.google.com).
2. In the top right, click Settings ![Settings](//lh3.googleusercontent.com/p3J-ZSPOLtuBBR_ofWTFDfdgAYQgi8mR5c76ie8XQ2wjegk7-yyU5zdRVHKybQgUlQ=h36) ![and then](//lh3.googleusercontent.com/QbWcYKta5vh_4-OgUeFmK-JOB0YgLLoGh69P478nE6mKdfpWQniiBabjF7FVoCVXI0g=h36) **See all settings**.
3. Click the **Accounts and import** or **Accounts** tab.
4. In the "Send mail as" section to the right of the address you want to use, click **Make default**.

Change default "reply-to" address

When you send a message, replies will go to your original Gmail address by default. To choose a different address, follow these steps.

1. On your computer, open [Gmail](https://mail.google.com).
2. In the top right, click Settings ![Settings](//lh3.googleusercontent.com/p3J-ZSPOLtuBBR_ofWTFDfdgAYQgi8mR5c76ie8XQ2wjegk7-yyU5zdRVHKybQgUlQ=h36) ![and then](//lh3.googleusercontent.com/QbWcYKta5vh_4-OgUeFmK-JOB0YgLLoGh69P478nE6mKdfpWQniiBabjF7FVoCVXI0g=h36) **See all settings**.
3. Click the **Accounts and Import** or **Accounts** tab.
4. In the "Send mail as" section, click **Edit info** next to your email address.
5. Click **Specify a different "reply to" address**.
6. Add a reply-to address.
7. If necessary, click **Next Step**.
8. Click **Save Changes**.

## "Couldn't reach server," "TLS Negotiation failed" error

If you see one of these error messages, you might need to select a different port number and authentication type. Make sure you have used the correct outgoing mail server for your provider. You might need to contact your third party email provider for the correct settings.

Select a secured connection

Check with your other mail service for their recommended port number, authentication type, or outgoing mail server. Make sure your third party provider supports SSL or TLS with a valid certificate.

Here are some common combinations:

- [SSL](https://support.google.com/a/answer/100181) with port 465
- [TLS](https://www.google.com/transparencyreport/saferemail/) with port 25 or 587

My other mail service doesn't support SSL or TLS

We recommend you send your email over a secure (encrypted) connection.

However, if your other mail service doesn't support these secured connections or doesn't use a valid certificate, you can choose port **25**, then select the **Unsecured connection** option that appears.

If you do this, your information won't be encrypted for your protection.

## Use Gmail aliases

Filter using your Gmail alias

An easy way to sort your email is to add categories after your username.

For example, messages sent to the following aliases will all go to **janedoe@gmail.com**:

- janedoe**+school**@gmail.com
- janedoe**+notes**@gmail.com
- janedoe**+important.emails**@gmail.com

### Step 1: Choose aliases

Think of how you want to sort your email, then choose an alias for each category. For example:

- Use yourname**+work**@gmail.com for work emails.
- Use yourname**+news**@gmail.com to sign up for newsletters.
- Use yourname**+shopping**@gmail.com to create an account with an online retailer.

### Step 2: Filter your messages

[Create filters](6579-create-rules-to-filter-your-emails.md) to take automatic actions, like:

- Adding a label or a star
- Forwarding to another account
- Archiving or deleting

Send from a work or school group alias

If you use Gmail with your work or school account, you can send from a group alias. To receive the verification email to send from a group alias, you need to give delegates access to the group.

**Important:** Aliases aren’t private and sometimes they’re visible to others. For example, if you search Gmail for messages from bill@school.edu, you might find messages from alias@school.edu.

You'll need access to the group's permissions to change access for other members.

1. Open [Google Groups](https://groups.google.com/).
2. Click **My groups**.
3. Under the group name you want to send from, click **Manage**.
4. On the left, click **Permissions** ![and then](//lh3.googleusercontent.com/QbWcYKta5vh_4-OgUeFmK-JOB0YgLLoGh69P478nE6mKdfpWQniiBabjF7FVoCVXI0g=h36) **Posting permissions**.
5. In the "Post" section, click the Down arrow ![Down arrow](//lh3.googleusercontent.com/7acH9pM1qZl0MEFmPRkOPeuNk48-E7Wbn08-h9yfGXbkMTKHY0kOPqurH20N2jHFwZY=w36-h36).
6. Select **Anyone on the web**.
7. Click **Save**.

**Tip**: If "Anyone on the web" is not available in the group's permissions, your administrator might need to enable "Group owners can allow incoming email from outside the organization for your domain."