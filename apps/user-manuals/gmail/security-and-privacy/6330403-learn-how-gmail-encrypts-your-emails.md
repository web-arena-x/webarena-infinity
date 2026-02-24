# Learn how Gmail encrypts your emails

Source: https://support.google.com/mail/answer/6330403

---

When you send a message, Gmail uses encryption to help keep your message private and secure until it reaches the right person.

## Transport Layer Security (TLS): Standard protection for your emails

![A static image that shows how TLS works in Gmail. In the image, two people send emails to each other. Each email has a TLS icon on it, which indicates that the emails can't be tampered with while they are in transit to the intended recipients.](//storage.googleapis.com/support-kms-prod/ZVv5Vr7Uxd5Yx6ir5IykvagiIQwcg3QEGEsv)

**Available for:** All Gmail accounts

All Gmail messages use TLS automatically. Think of TLS as a secure mail carrier for your messages.

- When you send a message in Gmail, it’s like you give a letter to a reliable mail carrier.
- If the recipient also uses this secure mail carrier, your message is protected.

Almost all major email services use TLS. When you send or receive a message in Gmail, your message is protected and marked with a gray lock icon ![](//lh3.googleusercontent.com/n7ov12gscRuYFMEmwNFr6tf5sgEOLO0wENZ6oeO2Cdz09rM7QyM8vq7Ea3wUR5LiTXk=w36), also known as standard encryption.

## Secure/Multipurpose Internet Mail Extensions (S/MIME): Extra protection for sensitive emails

![A static image that shows how S/MIME works in Gmail. In the image, two people send emails to each other. Each person has a key in their hands, which indicates that they can encrypt and decrypt the mesages.](//storage.googleapis.com/support-kms-prod/8tzIv2mertMY3plfIqyvK9CnJtUrN5bakDRe)

**Available for:** Work or school Gmail accounts

For a higher level of security, Gmail supports S/MIME. Imagine S/MIME as a locked briefcase and only you and your recipient have the keys so that:

- When you send a message, you put it inside the briefcase and lock it with a unique key.
- The secure mail carrier (S/MIME) transports the briefcase and can’t open it.
- Only the recipient can open the briefcase with their matching key.
- Even if someone intercepts the briefcase, they can’t open it without your key.

There are 2 key-management options for S/MIME:

- **Hosted S/MIME:** Google securely manages a copy of your key. These messages are marked with a green lock icon ![](//lh3.googleusercontent.com/WmzEOw364ngqLin-wCJv3HD08VRBhfjXKHy5QdOU0MHjvn_HFLocO85chSI3-9usUbU=w36), also known as enhanced encryption. [Learn about hosted S/MIME](/mail/answer/7023606).
- **Client-side encryption (CSE):** Your organization holds the only copy of the key. Not even Google can open your briefcase. These messages are marked with a blue shield icon ![](//storage.googleapis.com/support-kms-prod/MhXzlz8GjmXOT6qJSrSQ1tCcXQVGHtczrTJl), also known as additional encryption. [Learn about Gmail CSE](/mail/answer/13317990).

## Learn how to verify email security

There are two ways to verify email security:

- On your computer or Android device, when you compose a message, select Message security ![](//storage.googleapis.com/support-kms-prod/UTscb32S6vXRGWlBpKY8ZQlFTfKC5ub2Ne1e).
- When you receive a message, open the recipient details.
- If you get a message with a red open lock icon ![](//lh3.googleusercontent.com/Voo-KJStWSUpPumm-ex5WhBWnvWx5AgzgsX-vVC83hFsrOZFGu7B8wOpC11WeeMqUjA=w36), it means the message is unencrypted. You should:
 - Not send sensitive information.
 - Let the sender know their message is unencrypted.

[Learn how to check your email security](/mail/answer/7039474).

## Related resources

- [Check the security of your emails](/mail/answer/7039474)
- [Use hosted S/MIME to keep Gmail messages more secure](/mail/answer/7023606)
- [Learn about Gmail Client-side encryption](/mail/answer/13317990)
- [Email Encryption FAQs](/transparencyreport/answer/7381230)
- [Email encryption in transit](https://transparencyreport.google.com/safer-email/overview)