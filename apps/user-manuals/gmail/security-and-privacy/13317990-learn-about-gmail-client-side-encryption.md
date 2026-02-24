# Learn about Gmail Client-side encryption

Source: https://support.google.com/mail/answer/13317990

---

Google Workspace uses the latest cryptographic standards to encrypt all data at rest and in transit between its facilities. In addition, Gmail uses [TLS (Transport Layer Security)](/mail/answer/6330403) for communication with other email service providers. With Gmail Client-side encryption (CSE), you can strengthen the confidentiality of your sensitive or regulated data content by having the encryption handled in your browser before any data is transmitted or stored in Google's cloud-based storage. This provides a uniform protection to your messages until it is received by the intended recipients.

## Before you start

You can add additional encryption to emails with these Google Workspace editions:

- Enterprise Plus
- Education Plus
- Education Standard
- Frontline Plus

If you have Assured Controls, you can also send end-to-end encrypted emails to anyone without setting up S/MIME. [Learn more about Assured Controls](/a/answer/13880647).

- **If you have Assured Controls:** You can send encrypted messages to both internal and external recipients, just like normal email.
  - Your admin can control how external recipients access encrypted messages. They can either:
    - Allow recipients to use an existing Google account (@gmail.com or Google Workspace account).
    - Force all external recipients to create a guest account.
- **If you don't have Assured Controls and you use S/MIME:** You need to exchange certificates.
  - External recipients can read messages in their own email app.

If you can't find CSE, [contact your administrator](/a/answer/6208960).

## About Client-side encryption

When CSE is turned on:

- The body of the email, including inline images and attachments, will have additional encryption.
- The header of the email, including subject, timestamps, and recipients, will not have additional encryption.

Your admin may have set your messages to default to having client side encryption turned on by default.

## Send end-to-end encrypted email to anyone

**Important:**

- If you use Gmail with Assured Controls and have access to the beta, you can send end-to-end encrypted emails to anyone without setting up S/MIME.
- Before you start drafting an email, decide if you want to add additional encryption. You can add additional encryption while drafting an email, but if you do so, your draft will be deleted and a new draft will be opened.
- After drafting an email, you can turn off additional encryption if it's no longer needed. Make sure the draft doesn't contain any sensitive information before removing the additional encryption.

1. In Gmail, click **Compose**.
2. On the right corner of the message, click Message security ![](//storage.googleapis.com/support-kms-prod/gTATV4I3xlOpNF9oS1phijJEUJMf91FEOa6A).
3. Under "Additional encryption," click **Turn on**.
4. Add your recipients, subject, and message content.
5. Click **Send**.
6. If prompted, sign in to your identity provider.

## If you're using S/MIME: Send emails with CSE to an external domain

Before you can send emails with CSE to a recipient outside your domain, exchange digital signatures first.

**Important:**

- Emails with a digital signature include your certificate and public key, which the recipient can use to encrypt the emails that they send to you.
- Make sure the recipient sends a signed email in return when you exchange digital signatures. When a recipient sends a signed email, the key is automatically stored, and additional encryption is now available when communicating with the recipient.
- You only have to exchange digital signatures once for each contact.
- If you or your contact update the certificates, you’ll need to exchange digital signatures again.

If you receive a Digitally signed message ![](//storage.googleapis.com/support-kms-prod/zunnTwTy6Y9hzB6gXps7QmEsWdyAmwSb694h) in the email, the sender has provided additional identification that they are the sender. If you want to confirm if a message is digitally signed, find the icon in the conversation view.

1. In Gmail, click **Compose**.
2. On the right corner of the message, click Message security ![](//storage.googleapis.com/support-kms-prod/gTATV4I3xlOpNF9oS1phijJEUJMf91FEOa6A).
   - Make sure that additional encryption is not turned on yet.
3. Click **Digital signature** ![and then](//lh3.googleusercontent.com/3_l97rr0GvhSP2XV5OoCkV2ZDTIisAOczrSdzNCBxhIKWrjXjHucxNwocghoUa39gw=h36) **Sign message**.
   - To view and download the certificate, click **View signature**.
4. Send your signed message to the recipient.
5. To confirm that the recipient received the email with the digital signature, ask them to send a signed message in return.

After you exchange digital signatures, CSE is available, and you can add additional encryption when communicating with the contact.

### Sign in to read an encrypted message

If you receive an invitation to read a Gmail encrypted message, you may be required to create a Google Guest Account and log in to a third-party service to read the message.

1. On your device, open your email client.
2. Click the email that contains the encrypted message notification ![and then](//lh3.googleusercontent.com/3_l97rr0GvhSP2XV5OoCkV2ZDTIisAOczrSdzNCBxhIKWrjXjHucxNwocghoUa39gw=h36) **View message**.
   - For mobile clients not on Gmail, this will open a browser instance of Gmail web.
3. Verify your email address.
   - To receive the verification code, click **Send code**.
4. Check your email for the code.
5. Enter the code.
6. Click **Verify**.
7. Follow the on-screen instructions.
8. Once your guest account is created, sign in to the account.
9. To agree to the terms of service, click **I understand**.

## Read a CSE encrypted email

When you receive a CSE encrypted message, you'll see "Encrypted message" below the sender's name. To read the message:

1. In Gmail, open the email.
2. If prompted, sign in to your identity provider.
3. The message will be automatically decrypted in your Gmail browser window.

## Use hardware keys for encryption

### Add certificates from a hardware key

**Important:** To add certificates from your hardware key, make sure you or your administrator have [installed the Workspace Hardware Keys application](/a/answer/14153163).

1. On your computer, open [Gmail](https://mail.google.com/).
2. At the top right, click Settings ![Settings](//lh3.googleusercontent.com/p3J-ZSPOLtuBBR_ofWTFDfdgAYQgi8mR5c76ie8XQ2wjegk7-yyU5zdRVHKybQgUlQ=h36) ![and then](//lh3.googleusercontent.com/3_l97rr0GvhSP2XV5OoCkV2ZDTIisAOczrSdzNCBxhIKWrjXjHucxNwocghoUa39gw=h36) **See all settings**.
3. In the “Accounts” tab, next to “Encryption certificates,” click **Manage certificates**.
4. Insert your hardware key into your device.
5. Click **Add certificates**.
   1. Select the certificates you want to upload to Gmail.
   2. Click **Add**.
6. In the “Active” tab, check that your certificates are included on the list, click **Done**.
7. Make sure you set the default certificates for your:
   - Digital signature
   - Encryption signature
8. Click **Save defaults** ![and then](//lh3.googleusercontent.com/3_l97rr0GvhSP2XV5OoCkV2ZDTIisAOczrSdzNCBxhIKWrjXjHucxNwocghoUa39gw=h36) **Add** ![and then](//lh3.googleusercontent.com/3_l97rr0GvhSP2XV5OoCkV2ZDTIisAOczrSdzNCBxhIKWrjXjHucxNwocghoUa39gw=h36) **Done**.

### Set your default certificates

**Important:** You can add a new certificate when your current one expires.

1. On your computer, open [Gmail](https://mail.google.com/).
2. At the top right, click Settings ![Settings](//lh3.googleusercontent.com/p3J-ZSPOLtuBBR_ofWTFDfdgAYQgi8mR5c76ie8XQ2wjegk7-yyU5zdRVHKybQgUlQ=h36) ![and then](//lh3.googleusercontent.com/3_l97rr0GvhSP2XV5OoCkV2ZDTIisAOczrSdzNCBxhIKWrjXjHucxNwocghoUa39gw=h36) **See all settings**.
3. In the “Accounts” tab, next to “Encryption certificates,” click **Manage certificates** ![and then](//lh3.googleusercontent.com/3_l97rr0GvhSP2XV5OoCkV2ZDTIisAOczrSdzNCBxhIKWrjXjHucxNwocghoUa39gw=h36) **Upload certificate**.
4. Make sure you set the default certificates for your:
   - Digital signature
   - Encryption signature
5. Click **Save defaults** ![and then](//lh3.googleusercontent.com/3_l97rr0GvhSP2XV5OoCkV2ZDTIisAOczrSdzNCBxhIKWrjXjHucxNwocghoUa39gw=h36) **Add** ![and then](//lh3.googleusercontent.com/3_l97rr0GvhSP2XV5OoCkV2ZDTIisAOczrSdzNCBxhIKWrjXjHucxNwocghoUa39gw=h36) **Done**.

## Verify your digital signature

1. On your computer, open [Gmail](https://mail.google.com/).
2. To open a new draft, click **Compose**.
3. On the right of the “To:” line, click Message security ![](//storage.googleapis.com/support-kms-prod/gTATV4I3xlOpNF9oS1phijJEUJMf91FEOa6A).
4. Click **Digital Signature** ![and then](//lh3.googleusercontent.com/3_l97rr0GvhSP2XV5OoCkV2ZDTIisAOczrSdzNCBxhIKWrjXjHucxNwocghoUa39gw=h36) **View Signature**.

## Attachment size limit

When additional encryption is turned on, there is a 5 MB upload limit for attachments and inline images.

## Blocked file types

When you turn on CSE and you receive an email with an attachment, you'll find a warning message that encrypted emails can’t be scanned for viruses. Unless you're sure that the email is safe, be careful with attachments. Attachments with certain file types are automatically blocked.

These file types are blocked by Gmail:

`.ade, .adp, .apk, .appx, .appxbundle, .bat, .cab, .chm, .cmd, .com, .cpl, .diagcab, .diagcfg, .diagpack, .dll, .dmg, .ex, .ex_, .exe, .hta, .img, .ins, .iso, .isp, .jar, .jnlp, .js, .jse, .lib, .lnk, .mde, .msc, .msi, .msix, .msixbundle, .msp, .mst, .nsh, .pif, .ps1, .scr, .sct, .shb, .sys, .vb, .vbe, .vbs, .vhd, .vxd, .wsc, .wsf, .wsh, .xll`

## Feature restrictions

When additional encryption is turned on, these features are not available:

- Confidential mode
- Delegated accounts
- Email layouts
- Multi-send mode
- Proposing meeting times
- Pop-out and full-screen compose
- Sending to Groups as recipients
- Email signatures
- Emojis
- Print
- Google AI products
- Smart features for Gmail
- Screen recording on mobile devices
- Screenshots on Android mobile devices

## S/MIME encryption protocol

Additional encryption relies on the [S/MIME 3.2 IETF standard](https://www.rfc-editor.org/rfc/rfc5751) to send and receive secure MIME data. S/MIME requires email senders and recipients to have their X.509 certificates [trusted by Gmail](/a/answer/7448393). S/MIME encryption is used in coordination with S/MIME digital signatures ensuring email integrity.