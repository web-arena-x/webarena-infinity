# Click-time link protections in third-party email clients

Source: https://support.google.com/mail/answer/10173182

---

Because links to malicious websites can be sent in emails, Google adds link protection for all official Gmail clients (web, Android, and iPhone & iPad). Some of these protections are now available for some users that use a third-party email application (IMAP client).

For these users, clicking a link in a recent message starts a malicious link check. If nothing malicious is detected, the user is taken to the destination. For older messages, a window might appear, requiring a tap or click to open the link.

## FAQ

## Who will receive these protections?

We're currently running a small test to bring third-party email client users many of the same link protections that all users of official Gmail clients receive. This test includes all users in the Advanced Protection Program.

## Which third-party email applications have these new protections?

Apple Mail, Outlook, and some prevalent Android email clients have them.

## How can I tell if these protections are being applied in my account?

If you’re part of the test, you might see a proxied URL (e.g. [https://www.google.com/url?q=ORIGINAL\_URL](http://original_url)) when inspecting the links in your email client.

## How can I read the message in its original state?

Visit [Gmail](https://mail.google.com) and follow these steps:

1. Open the message.
2. At the top-right, click More ![More](//lh3.googleusercontent.com/oLoRPrHJd7m46sWijX6zBWnEnfslP62AxJSwt5Nj0bNbpaYHz2pyscExleiofsH2kQ=h36) .
3. Click **Show original**.

## How can I export all of my messages in their original state?

To download your Gmail messages, visit [Google Takeout](https://takeout.google.com). Messages exported through Takeout won’t include link protection URLs.

## What information does Google log about these rewritten links?

This security feature brings the experience for users using third-party clients in-line with users of official Gmail clients.

The only information logged in connection with this feature is what's needed to run and maintain the service, including the IP address and user agent of the request, as well as information about clicked URLs (such as the URL itself and whether Safe Browsing determined it was malicious). None of this information is associated with any logged-in user or any Google account identity. This data is only retained for a short period of time and is only used for security purposes.