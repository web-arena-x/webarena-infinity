# Email Security

Source: https://support.joinhandshake.com/hc/en-us/articles/360041290793-Email-Security

---

Handshake users interested in email security may want to know if we support using Sender Policy Framework (SPF) and/or DomainKeys Identified Mail (DKIM) to identify messages that are legitimately sent by Handshake.

All emails sent by Handshake (such as notifications, job digests, etc.) use SPF / DKIM and DMARC for enforcement to validate that they are legitimate Handshake emails.

- **Note**: DMARC records for Handshake emails are published under DNS records and can be confirmed for free using tools like [Valimail](https://domain-checker.valimail.com/dmarc/mail.joinhandshake.com "https://domain-checker.valimail.com/dmarc/mail.joinhandshake.com").

Our email sending domains are currently:

- joinhandshake.com
- mail.joinhandshake.com
- notifications.joinhandshake.com
- m.joinhandshake.com
- g.joinhandshake.com

These servers send emails using TLS encryption protocol. In the event that sendings fail with TLS it may attempt to send emails using other protocols such as SSL.