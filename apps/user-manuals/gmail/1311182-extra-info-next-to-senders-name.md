# Extra info next to sender’s name

Source: https://support.google.com/mail/answer/1311182

---

You may find extra information next to someone's name when they send you a message. For example, you could get an email from your bank, but the sender's email address is from a different site.

## I can find extra info next to the sender's name

I can find an email address next to the sender's name

You'll find the sender's email address next to their name if it's someone you haven't emailed in the past.

If you add this sender to your address book or reply to one of their emails, you won't find their email address next to their name on future messages.

I can find "via" and a website name next to the sender's name

You'll find "via" and a website name next to the sender's name if:

- The domain it was sent from doesn't match the domain in the "From:" address. For example, you got an email from john.smith@gmail.com, but it could've been sent through a social networking site and not Gmail.
- The email was sent to a Google Group from a domain that has a "p=reject or p=quarantine" [DMARC policy](https://www.dmarc.org/).

You can't remove the "via" next to someone's name. Gmail shows this information so you're aware of where your messages are coming from.

If an email was sent to a Google Group from a domain that has 'p=quarantine' or 'p=reject' policy as its [DMARC policy](https://dmarc.org/) you'll find "'Sender Name' via Group-Name" <YourGroup@Yourdomain.com> (the recipient's group) as the sender. This behavior is displayed so the Groups delivery system does not trigger the sender's domain DMARC policy and is correctly delivered.

If you notice that an email was sent via a program you don't recognize, the message might be spam.

## Remove "via" information from emails not sent through Gmail

Gmail checks whether the messages you send are [authenticated](/mail/answer/180707).

- If you send messages with a bulk mailing vendor or third party affiliates, [prevent your emails from being blocked by Gmail](/mail/answer/81126).
- Publish an SPF record that includes the IPs of the vendor or affiliates which send your messages.
- Sign your messages with a DKIM signature that is associated with your domain.
- Make sure the domain in the "From:" address matches the domain you're using to authenticate your emails.