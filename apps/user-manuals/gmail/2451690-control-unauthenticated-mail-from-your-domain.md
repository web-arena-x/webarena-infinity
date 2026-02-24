# Control unauthenticated mail from your domain

Source: https://support.google.com/mail/answer/2451690

---

**Important:** To prevent emails from being blocked or sent to spam, you can find info about spam rates, reputation, and more through [Postmaster Tools](/mail/answer/6227174).

If you sent an email to a Gmail user and got an automatic bounce message that says, "Unauthenticated email from [email domain] is not accepted due to domain's DMARC policy,” see the options below for more information:

- **If you sent the email using Gmail**, learn how to [fix bounced or rejected emails](/mail/answer/6596).
- **If you sent the email using a different email application**, try looking for a setting in your email application that controls the server used to send messages (the “outgoing” server). Change this setting so that you’re using the server that matches the email address you want to send from. If that doesn’t work or you need more help, contact the email provider for your email address.

To help fight spam and abuse, Gmail uses [email authentication](/mail/answer/180707) to verify if a message was actually sent from the address it appears to be sent from. As part of the DMARC initiative, Google allows domain owners to help define how we handle unauthenticated messages that falsely claim to be from your domain.

## What you can do

Domain owners can publish a policy telling Gmail and other participating email providers how to handle messages that are sent from your domain but aren’t authenticated. By defining a policy, you can help combat [phishing](/mail/answer/8253) to protect users and your reputation.

Learn more about [setting up DMARC](/a/answer/2466580).

Here are some things to keep in mind:

- You'll receive a daily report from each participating email provider so you can see how often your emails are authenticated and how often invalid emails are identified.
- You might want to adjust your policy as you learn from the data in these reports. For example, you might adjust your actionable policies from “monitor” to “quarantine” to “reject” as you become more confident that your own messages will all be authenticated.
- Your policy can be strict or relaxed. For example, eBay and PayPal publish a policy requiring all of their mail to be authenticated in order to appear in someone's inbox. In accordance with their policy, Google rejects all messages from eBay or PayPal that aren’t authenticated.

## More about DMARC

[DMARC.org](https://dmarc.org) was formed to allow email senders to influence unauthenticated mail by publishing their preferences in a discoverable and flexible policy. It also enables participating email providers to provide reports so that senders can improve and monitor their authentication infrastructure.

Google is participating in DMARC along with other email domains like AOL, Comcast, Hotmail, and Yahoo! Mail. In addition, senders like Bank of America, Facebook, Fidelity, LinkedIn, and Paypal have already published policies for Google and other receivers to follow.

For more information, refer to [About authentication methods](/a/answer/10583557).

## Was this helpful?

How can we improve it?

YesNo

Submit