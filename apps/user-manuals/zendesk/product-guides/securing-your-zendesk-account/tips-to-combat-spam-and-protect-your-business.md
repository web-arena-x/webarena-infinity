# Tips to combat spam and protect your business

Source: https://support.zendesk.com/hc/en-us/articles/4408832828186-Tips-to-combat-spam-and-protect-your-business

---

Protecting your company from spam and abuse is inevitably a task all companies are confronted with. While there is no silver bullet to stop all spam, there are some commonly used options that can help.

To ensure your account is as spam-free as possible, applying active protections to forms, emails and API calls that send to your account should be maintained. This article describes some great methods for protecting your account.

This article contains the following sections:

- [Using CAPTCHA on forms](#h_57534470811539295291846)
- [Protecting your domain from email abuse, via SPF, DKIM and DMARC records](#h_99404083271539295299373)
- [Using Zendesk Support-specific features to combat spam](#h_667502120121539295305407)
- [Further Reading](#h_255541323221539295470946)

## Using CAPTCHA on forms

Using a *Completely Automated Public* *[Turing test](https://en.wikipedia.org/wiki/Turing_test)* *to tell Computers and Humans Apart* (CAPTCHA) is touted as one of the best ways to prevent incoming spam on any sort of public facing submission to your system. This presents a challenge to anyone submitting a ticket before they are able to successfully submit. In many cases, this will outright stop any attempts to abuse your system.

Support uses [Cloudflare's bot detection and management software](https://www.cloudflare.com/products/bot-management/). CAPTCHA is enabled by default, including on the Sign Up page, and can't be disabled. Only traffic that Cloudflare flags as suspicious will be served CAPTCHA challenges.

## Protecting your domain from email abuse via SPF, DKIM, and DMARC records

Most commonly, abusive email messages come from a forged or fake address which can be accomplished easily in many programs and scripts.  Using SPF, DKIM, and DMARC in tandem will help build your domain’s reputation, and avoid having your mail end up in your customer’s spam folder. We make it easy to use on your account, as we support all three records. Here's a quick recap of all records:

An SPF record is a policy which is set up within your DNS record that allows the email receiver's email client to validate if the server is allowed to send messages on its behalf. In layman's terms, SPF acts like an allowlist for email servers, dictating what can and cannot send on your domains behalf. This can cut down significantly on forged emails. You can read more about setting up records for Zendesk in our article, [Setting up SPF for Zendesk to send email on behalf of your email domain](https://support.zendesk.com/hc/en-us/articles/4408832543770-Setting-up-SPF-for-Zendesk-to-send-email-on-behalf-of-your-email-domain).

DKIM records are a protocol which validates a message’s cryptographic signature against a public key placed in the DNS record of sender’s domain. This helps ensure that there was no deviation within the path of the email, and shows if a message has been altered in anyway prior to the receiver getting the message. Due to this, servers tend to find any domain or email more reputable, and less likely to end up in a spam folder (or outright rejected). You can setup the DKIM records needed for Zendesk by following the article, [Digitally signing your emails with DKIM or DMARC](https://support.zendesk.com/hc/en-us/articles/4408822303386-Digitally-signing-your-email-with-DKIM-or-DMARC).

DMARC (Domain-based Message Authentication, Reporting and Conformance) is a policy which attempt to tie SPF and DKIM together, by telling servers how to handle an email if SPF and/or DKIM records aren't present within an email. It can also send email reports on failures, to help you gain insight into how your domain is being used and handling email. For more information on DMARC and how to set one up, see the overview on [Dmarc.org](https://dmarc.org/overview/).

## Using Zendesk Support-specific features to combat spam

While the previously-mentioned actions will help your domain in general, Zendesk Support offers a few additional tools at your disposal.

### Removing specific placeholders from first-reply triggers (only applies to open Zendesk Support instances)

If you have an [open Zendesk Support instance](https://support.zendesk.com/hc/en-us/articles/4408881989018#topic-1__ul_l2w_x13_4y) where anybody can submit tickets and no registration is required, first-reply triggers (that fire upon ticket creation) using any of the placeholders below can be targets for *relay spam*.

Relay spam occurs when mail is sent to a destination via a third party (in this case, Zendesk) to hide the source of the email address to impersonate the 3rd party. The following placeholders are targets for relay spam because they use an anonymous endpoint that allows anyone to enter any text or links they want.

- {{ticket.title}}
- {{ticket.requester.first\_name}}
- {{ticket.requester.last\_name}}
- {{ticket.requester.name}}

To avoid the risk of your account becoming a target for relay spam, consider configuring your instance to be closed or restricted, as discussed in [Configuring end user access](https://support.zendesk.com/hc/en-us/articles/4408887573274-Configuring-how-end-users-access-and-sign-in-to-Zendesk-Support#topic_dkn_nfk_v3). Otherwise, in an open Zendesk Support instance, do not use the placeholders listed above in the subject or body of your first-reply triggers; use static text instead. This ensures that the email notification that is sent when a ticket is created, for example, does not replace a salutation intended to say “Dear Amanda Smith” with “Dear www.spam.com.” Using these placeholders in other triggers (after the first reply) is acceptable because, at that point, you’ve established that the interaction is genuine.

### Sender Authentication (Inbound DMARC protection)

Sender Authentication is a relatively new feature which helps you control spoofed and illegitimate emails from reaching your account.  This feature looks to authenticate the senders DMARC, and sends to your suspended queue if it fails. You can find this feature on the Email admin page, at **Admin > Channels > Email**. For more information on the feature itself, see our support article, [Authenticating incoming email using DMARC](https://support.zendesk.com/hc/en-us/articles/4408821985818-Authenticating-incoming-email-using-DMARC) for further information.

### Blocking emails and domains

If you're past the point of proactively protecting your account and spam has been coming through email, you can outright block incoming emails from specific addresses or entire domains. This can be an efficient way to stop spam in its tracks. See our article, [Using the allowlist and blocklist to control access to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408886840986-Using-the-whitelist-and-blacklist-to-control-access-to-Zendesk-Support).

As spammers continue to get more creative and sophisticated with their methods, it is important to take advantage of all possible spam fighting tools at your disposal, as no one solution will be completely effective. With the combination of the methods listed here implemented for your business, spammers will be less likely to target your business.

### Requiring authentication for the requests and uploads APIs

You can require authentication for the requests API endpoint ([/api/v2/requests](https://developer.zendesk.com/rest_api/docs/support/requests)) and uploads API endpoint ([/api/v2/uploads](https://developer.zendesk.com/rest_api/docs/support/attachments#upload-files)). Although it's highly effective at preventing spam, requiring authentication makes it harder for end users to open tickets anonymously. Some methods of ticket creation, such as the Zendesk Web Widget Contact form, custom apps, and external web forms, rely on the unauthenticated anonymous ticket creation process to submit tickets.

Requiring authentication for the requests and uploads endpoints will prevent the creation of anonymous tickets from these sources. The **Require authentication for requests and uploads APIs** setting is turned off by default and can only be enabled in Admin Center.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_customer_settings_require_auth_apis.png)

## Further Reading

If you're looking for more documentation to combat spam, check out the following:

- [About Help Center Spam prevention](https://support.zendesk.com/hc/en-us/articles/4408883183770-About-Help-Center-spam-prevention)
- [How do I bulk delete spam tickets in Zendesk?](https://support.zendesk.com/hc/en-us/articles/4408884016410-How-can-I-bulk-delete-spam-tickets-in-Zendesk-)
- [Understanding and managing tickets and spam](https://support.zendesk.com/hc/en-us/articles/4408889141146-Understanding-and-managing-suspended-tickets-and-spam)