# Read Gmail messages on other email clients using POP

Source: https://support.google.com/mail/answer/7104828

---

You can open your messages from Gmail in other mail clients that support POP, like Microsoft Outlook.

## Step 1: Make sure POP is the best way to read your emails

- IMAP and POP are both ways to read your Gmail messages in other email clients.
- IMAP can be used across multiple devices. Emails are synced in real time.
- POP can only be used for a single computer. Emails aren't synced in real time. Instead, they're downloaded and you decide how often you want to download new emails.

## Step 2: Set up POP

### First, set up POP in Gmail

**Important:** After you turn on POP in Gmail, it may take some time to download your messages to your email client.

1. On your computer, open [Gmail](https://mail.google.com/).
2. In the top right, click Settings ![Settings](//lh3.googleusercontent.com/p3J-ZSPOLtuBBR_ofWTFDfdgAYQgi8mR5c76ie8XQ2wjegk7-yyU5zdRVHKybQgUlQ=h36) ![and then](//lh3.googleusercontent.com/3_l97rr0GvhSP2XV5OoCkV2ZDTIisAOczrSdzNCBxhIKWrjXjHucxNwocghoUa39gw=h36) **See all settings.**
3. Click the **Forwarding and POP/IMAP** tab.
4. In the "POP download" section, select:
   - **Enable POP for all mail (even mail that’s already been downloaded)**
   - **Enable POP for mail that arrives from now on**
5. Under “When messages are accessed with POP,” select what happens to Gmail’s copy of the message:
   - **Keep Gmail’s copy in the Inbox**
   - **Mark Gmail’s copy as read**
   - **Archive Gmail’s copy**
   - **Delete Gmail’s copy**
6. At the bottom of the page, click **Save Changes**.

### Next, make changes on your email client

Go to your client, such as Microsoft Outlook, and check these settings.

| | |
| --- | --- |
| Incoming Mail (POP) Server | pop.gmail.com Requires SSL: Yes Port: 995 |
| Outgoing Mail (SMTP) Server | smtp.gmail.com Requires SSL: Yes Requires TLS: Yes (if available) Requires Authentication: Yes Port for TLS/STARTTLS: 587 **If you use Gmail with your work or school account**, check with your [administrator](/a/answer/6208960) for the correct SMTP configuration. |
| Server timeouts | Greater than 1 minute (5 is recommended) |
| Full name or display name | Your name |
| Account name, username, or email address | Your email address |
| Password | Your Gmail password |

## Troubleshoot problems

I can't sign in to my email client

If you can't sign in to your email client, you might see one of these errors:

- "Username and password not accepted"
- "Invalid credentials"
- You're asked to enter your username and password over and over

#### Step 1: Check your password

If you have these problems or can’t sign in, first check to make sure you’re using the right password.

#### Step 2: Try these troubleshooting steps

- Update your email client to the latest version.
- Use an App password: If you use 2-Step Verification, try signing in with an [App password](/accounts/answer/185833).
- Allow less secure apps: If you don't use 2-Step Verification, you might need to [allow less secure apps to access your account](/accounts/answer/6010255).
- If you recently changed your Gmail password, you might need to re-enter your Gmail account information or completely repeat your Gmail account setup on your other email client.
- If the tips above didn't help, visit <https://www.google.com/accounts/DisplayUnlockCaptcha> and follow the steps on the page. If you use Gmail through your work, school, or other organization, visit https://www.google.com/a/yourdomain.com/UnlockCaptcha In the web address, replace `yourdomain.com` with your domain name.

I want to download emails on multiple email clients

It's easiest to use Gmail on multiple email clients using IMAP. If you need to use POP instead of IMAP, set up "Recent mode." Recent mode shows your last 30 days of emails from Gmail.

#### Step 1: Turn on Recent mode

1. In your email client's POP settings page, find the "Email address" or "User name" field.
2. Add `recent:` in front of your email address. For example, `recent:example@gmail.com`.

#### Step 2: Change your POP settings

Change your POP settings so that your emails are left on the server.

- **Outlook**: Go to your Accounts, click **Advanced** ![and then](//lh3.googleusercontent.com/QbWcYKta5vh_4-OgUeFmK-JOB0YgLLoGh69P478nE6mKdfpWQniiBabjF7FVoCVXI0g=h36) **Leave a copy of messages on the server.**
- **Apple Mail**: On the "Advanced" tab, uncheck the box next to "Remove copy from server after retrieving a message," if available.
- **Thunderbird**: On the "Server Settings" tab, check the box next to "Leave messages on server."

"Account exceeded POP command or bandwidth limits" error

If you see the "Account exceeded POP command or bandwidth limits error," it's usually because your POP clients have been accessing your Gmail account too frequently.

To fix this, change your client's settings so it won't check for new messages too frequently.

I can't send emails

If emails you sent in your mail client are stuck in your outbox, try these fixes:

- If you're sending email through Apple Mail and you currently have 'smtp.gmail.com:username@gmail.com' in the 'Outgoing Mail Server:' field of your settings, try changing the field to 'smtp.gmail.com' instead.
- Make sure your SMTP settings don't have recent: on your email address.

My automatic replies aren't working

If you create automatic responses on your mail client, like an out of the office response, it might cause issues, including:

- If you're using your mail client on a computer and the computer goes offline, your automatic response won't be sent.
- When you receive emails that are sent to you indirectly, like through a mailing list, the automatic response might show your email address when it replies to the sender.

To avoid these problems, try using Gmail’s [out of office or vacation reply](/mail/answer/25922) instead of the one in your mail client.

My emails are deleted from Gmail

If the emails you read in your other email client are getting deleted from Gmail, check your POP settings.

1. Visit the [Forwarding and POP/IMAP settings page](https://mail.google.com/mail/u/0/#settings/fwdandpop).
2. In the "POP Download" section, make sure "Archive Gmail's copy" or "Delete Gmail's copy" aren't selected.
3. At the bottom of the page, click **Save changes**.

Emails aren't downloading correctly

After you set up POP in your Gmail settings, your emails become available in batches. It might take a while to see all your emails.

**Note:** Gmail downloads a copy of every email you send or receive, except for emails in Chats, Spam, and Trash. To avoid duplicates, Gmail doesn't download emails sent within your mail client, but you can still see them if you log in to Gmail.

If you continue to have problems downloading emails, try using recent mode:

1. In your email client's POP settings page, find the "Email address" or "User name" field.
2. Add `recent:` in front of your email address. For example, `recent:example@gmail.com`.

If that doesn't fix the problem, try deleting your Gmail address from your email client, then re-adding it.

Option to change the POP setting is unavailable

After you change your POP setting, the update needs to complete before you can change your settings again. When this happens, a status message displays in the Gmail POP settings menu.

“We are still working on enabling POP” error

If you attempt to download emails in windowed mode using POP while Gmail is still configuring POP for your account, this error message shows in your email client:

“We are still working on enabling pop for your account so windowed mode is not available. Try again later or consider using POP3 in recent mode.”

To use POP while the setup is still in process, you can:

- Change your email client to use recent mode.
- Wait until the process completes.
 - To check if the process is complete:
    1. On your computer, open [Gmail](https://mail.google.com/).
    2. At the top right, click Settings ![Settings](//lh3.googleusercontent.com/p3J-ZSPOLtuBBR_ofWTFDfdgAYQgi8mR5c76ie8XQ2wjegk7-yyU5zdRVHKybQgUlQ=h36) ![and then](//lh3.googleusercontent.com/3_l97rr0GvhSP2XV5OoCkV2ZDTIisAOczrSdzNCBxhIKWrjXjHucxNwocghoUa39gw=h36) **See all settings**.
    3. Select the **Forwarding and POP/IMAP** tab.
       - If the process is incomplete: In the "POP download" section, the option to enable POP is unavailable. You get a message that POP enablement is still in process.