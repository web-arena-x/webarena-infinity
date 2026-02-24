# Email Delivery: Unblocking Handshake Email

Source: https://support.joinhandshake.com/hc/en-us/articles/360012324954-Email-Delivery-Unblocking-Handshake-Email

---

Handshake maintains highly reputable emailing domains to ensure that emails are delivered. However, email delivery can sometimes fail due to the various systems in between Handshake and students which are designed to prevent email abuse. In order to maintain high deliverability, Handshake monitors and acts on spam scores, domain blocking, IP throttling and more.

In addition to unblocking IPs and domains, please identify any **internal limitations** you may have with receiving email and surface them to your Handshake Relationship Manager. 
*(e.g. 5k rate limit for recipients every hour)*

# Unblock by IP

We send email from a dedicated set of IP addresses; please allow access to all of these:

```
192.237.159.131
161.38.192.196
192.237.159.132
159.112.247.178
192.237.158.52
161.38.199.254
159.112.247.179
69.72.46.73
104.130.123.85
192.237.159.133
159.112.247.180
159.135.237.56
159.112.247.182 
159.112.247.181 
69.72.44.24
69.72.46.79 
69.72.40.228
159.135.226.83 
159.112.241.1
159.112.242.178 
159.112.252.237 
161.38.197.221 
161.38.198.110 
161.38.199.254
```

**Note:** All *italicized IP addresses*were added to this list as of February 8, 2023.

# Unblock by Domain (Optional)

We only send email from these domains:

```
joinhandshake.com
notifications.joinhandshake.com
mail.joinhandshake.com
m.joinhandshake.com 
g.joinhandshake.com
cm.joinhandshake.com
```

Additionally, please ensure that you are allowing traffic *from* smtp.sendgrid.net on port 587.

# How to Unblock if you use Google Apps

You'll need to have a [paid subscription for G Suite](https://support.google.com/a/answer/60217) in order to unblock email domains/IP addresses. With G Suite Basic or above, you can use [this guide](https://support.google.com/a/answer/60751?hl=en) to unblock email by domain and IP address. For more help, use the [general guidelines for bulk emailing](https://support.google.com/mail/answer/81126), recommended by Google (if you are emailing using Handshake).

# How to Unblock if you use Microsoft Office 365

For Office 365 admin portals - unblocking the above IPs/domains can be accomplished by following [these instructions](https://technet.microsoft.com/en-us/library/jj200718(v=exchg.150).aspx).

*Note*: Messages may also be automatically routed to the new 'Clutter' folder. Please refer to this [Microsoft guide](https://support.microsoft.com/en-us/office/use-clutter-to-sort-low-priority-messages-in-outlook-7b50c5db-7704-4e55-8a1b-dfc7bf1eafa0) for more information on how to manage your Clutter preferences. This guide will also walk you through enabling/disabling this feature if mail is being sent there that you should be receiving in your general inbox.