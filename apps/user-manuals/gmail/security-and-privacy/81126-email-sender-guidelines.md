# Email sender guidelines

Source: https://support.google.com/mail/answer/81126

---

The guidelines in this article can help you successfully send and deliver email to personal Gmail accounts. Starting in 2024, email senders must meet the requirements described here to send email to Gmail personal accounts. A personal Gmail account is an account that ends in @gmail.com or @googlemail.com.

For the latest updates about sender requirements, visit the [Email sender guidelines FAQ](/a/answer/14229414).

**Google Workspace senders:** If you use Google Workspace to send large volumes of email, review the [Spam and abuse policy in Gmail](/a/answer/178266). The policy is part of the [Google Workspace Acceptable Use Policy](http://www.google.com/apps/intl/en/terms/use_policy.html).

## Sender requirements updates

This table lists our updates to the sender guidelines and requirements:

| Sender requirement | Date added |
| --- | --- |
| Use a TLS connection for transmitting email | Dec. 2023 |

## Sender requirements and guidelines

Follow these guidelines to help ensure messages are delivered to Gmail accounts as expected, and to help prevent Gmail from limiting sending rates, blocking messages, or marking messages as spam.

Requirements for all senders

Starting February 1, 2024, all email senders who send email to Gmail accounts must meet the requirements in this section. 
 
**Important:** If you send more than 5,000 messages per day to Gmail accounts, follow the [Requirements for sending 5,000 or more messages per day](#requirements-5k).

- Set up SPF or DKIM email authentication for your sending domains.
- Ensure that sending domains or IPs have valid forward and reverse DNS records, also referred to as PTR records. [Learn more](#ip)
- Use a TLS connection for transmitting email. For steps to set up TLS in Google Workspace, visit [Require a secure connection for email](/a/answer/2520500).
- Keep spam rates reported in [Postmaster Tools](https://gmail.com/postmaster) below 0.3%. [Learn more about spam rates](#spam-rate)
- Format messages according to the Internet Message Format standard, [RFC 5322](https://tools.ietf.org/html/rfc5322).
- Don’t impersonate Gmail From: headers. Gmail will begin using a DMARC quarantine [enforcement policy](/a/answer/10032169#policy-options), and impersonating Gmail From: headers might impact your email delivery.
- If you manage a forwarding service, including mailing lists or inbound gateways, add [ARC headers](#arc) to outgoing email. ARC headers indicate the message was forwarded and identify you as the forwarder. Mailing list senders should also add a List-id: header, which specifies the mailing list, to outgoing messages.

Requirements for sending 5,000 or more messages per day

Starting February 1, 2024, email senders who send more than 5,000 messages per day to Gmail accounts must meet the requirements in this section.

- Set up SPF and DKIM email authentication for your domain.
- Set up DMARC email authentication for your sending domain. Your DMARC [enforcement policy](/a/answer/10032169#policy-options) can be set to none. [Learn more](#dmarc)
- Ensure that sending domains or IPs have valid forward and reverse DNS records, also referred to as PTR records. [Learn more](#ip)
- Use a TLS connection for transmitting email. For steps to set up TLS in Google Workspace, visit [Require a secure connection for email](https://support.google.com/a/answer/2520500).
- Keep spam rates reported in [Postmaster Tools](https://gmail.com/postmaster) below 0.30%. [Learn more about spam rates](#spam-rate)
- Format messages according to the Internet Message Format standard, [RFC 5322](https://tools.ietf.org/html/rfc5322).
- Don’t impersonate Gmail From: headers. Gmail will begin using a DMARC quarantine [enforcement policy](/a/answer/10032169#policy-options), and impersonating Gmail From: headers might impact your email delivery.
- If you manage a forwarding service, including mailing lists or inbound gateways, add [ARC headers](#arc) to outgoing email. ARC headers indicate the message was forwarded and identify you as the forwarder. Mailing list senders should also add a List-id: header, which specifies the mailing list, to outgoing messages.
- For direct email, the domain in the sender's From: header must be aligned with either the SPF domain or the DKIM domain. This is required to pass [DMARC alignment](/a/answer/10032169#dmarc-alignment).
- Marketing messages and subscribed messages must support one-click unsubscribe, and include a clearly visible unsubscribe link in the message body. [Learn more](#subscriptions)

If you send more than 5,000 emails per day before February 1, 2024, follow the guidelines in this article as soon as possible. Meeting the sender requirements before the deadline may improve your email delivery. If you don’t meet the requirements described in this article, your email might not be delivered as expected, or might be marked as spam. To get help with email delivery issues, go to [Troubleshooting](#troubleshooting).

### Email authentication requirements & guidelines

We require that you set up these email authentication methods for your domain:

- All senders: SPF or DKIM
- Bulk senders: SPF, DKIM, and DMARC

Authenticated messages:

- Help protect recipients from malicious messages, such as spoofing and phishing messages.
- Help protect you and your organization from being impersonated.
- Are less likely to be rejected or marked as spam by Gmail.

Set up email authentication for each of your sending domains at your domain provider. You can use instructions Google provides and our domain provider's email authentication support information.

To verify messages are authenticated, Google performs checks on messages sent to Gmail accounts. To improve email delivery, we recommend that you always set up SPF, DKIM, and DMARC for your domains. Make sure you're meeting the minimum authentication requirements described on this page. Messages that aren’t authenticated with these methods might be marked as spam or rejected with a [5.7.26 error](/a/answer/3726730#5726).

If you use an email service provider, verify that they authenticate your domain’s email with SPF and DKIM.

If you regularly forward email or manage a forwarding service, help ensure forwarded messages are authenticated by following our [Best practices for forwarding email to Gmail](/mail/answer/175365).

We recommend you always set up email authentication for the domain that hosts your public website

#### SPF

SPF prevents spammers from sending unauthorized messages that appear to be from your domain. Set up SPF by publishing an SPF record at your domain. The SPF record for your domain should include all email senders for your domain. If your third-party senders aren't included in your SPF record, messages from these senders are more likely to be marked as spam. Learn how to [define your SPF record and add it to your domain](/a/answer/33786).

#### DKIM

Turn on DKIM for the domain that sends your email. Receiving servers use DKIM to verify that the domain owner actually sent the message. If you use Google Workspace to send email, learn how to [turn on DKIM for your domain](/a/answer/180504#dkim-turn-on-verify). If you don’t use Google Workspace to send email, you can use one of many available internet tools to create your DKIM keys, or check with your domain provider for help.

**Important:** Sending to personal Gmail accounts requires a DKIM key of 1024 bits or longer. For security reasons, we recommend using a 2048-bit key if your domain provider supports this. Learn more about [DKIM key length](/a/answer/180504#key).

#### DMARC

DMARC tells receiving servers what to do with your messages that don’t pass SPF or DKIM. Set up DMARC by publishing a DMARC record for your domain. To pass DMARC authentication, messages must be authenticated by SPF or DKIM, or both. The authenticating domain must be the same domain that appears in the message From: header. Learn how to [set up DMARC](/a/answer/2466580).

We recommend you set up DMARC reports so you can monitor email sent from your domain, or appears to have been sent from your domain. DMARC reports help you identify senders that may be impersonating your domain. Learn more about [DMARC reports](/a/answer/10032472).

#### ARC

ARC checks the previous authentication status of forwarded messages. If a forwarded message passes SPF or DKIM authentication, but ARC shows it previously failed authentication, Gmail treats the message as unauthenticated.

When ARC shows that a forwarded message previously passed authentication, Gmail doesn’t automatically authenticate the message. Instead, Gmail does its own authentication check on the message.

We recommend that senders use ARC authentication, especially if they regularly forward email. Learn more about [ARC authentication](/a/answer/13198639).

### Infrastructure configuration requirements and guidelines

#### IP addresses

**Important:** The sending IP address must match the IP address of the hostname specified in the Pointer (PTR) record.

The public IP address of a sending SMTP server must have a corresponding PTR record that resolves to a hostname. This is called a *reverse DNS lookup*. The same hostname must also have an A (for IPv4) or AAAA (for IPv6) record that resolves to the same public IP address used by the sending server. This is called a *forward DNS lookup*.

Set up valid [reverse DNS records](https://en.wikipedia.org/wiki/Reverse_DNS_lookup) of your sending server IP addresses that point to your domain. Check for a PTR record with the [Google Admin Toolbox Dig](https://toolbox.googleapps.com/apps/dig/#PTR/) tool.

**Important:** The sending IP address must match the IP address of the hostname specified in the Pointer (PTR) record.

#### Shared IP addresses

A shared IP address is an IP address used by more than one email sender. The activity of any senders using a shared IP address affects the reputation of all senders for that shared IP address. A negative reputation can impact your delivery rate.

If you use a shared IP address for sending email:

- Make sure the shared IP address isn’t on any internet blocklist. Messages sent from IP addresses on a blocklist are more likely to be marked as spam.
- If you use an email service provider for your shared IP, use [Postmaster Tools](/mail/answer/6227174) to check the reputation of the shared IP address.

### Subscription requirements and guidelines

If you manage mailing lists or other email subscriptions, you should send email only to people who want to get messages from you. These recipients are less likely to report your messages as spam. If messages from your domain are frequently reported as spam, future messages from you are more likely to be marked as spam. Over time, user spam reports can lower your domain’s reputation. Check your spam rate and your domain and IP address reputation with [Postmaster Tools](/mail/answer/6227174).

#### Make it easy to subscribe

To help ensure recipients are engaged:

- Make sure recipients opt in to get messages from you.
- Confirm each recipient's email address before subscribing them.
- Periodically send messages to confirm that recipients want to stay subscribed.
- Consider unsubscribing recipients who don’t open or read your messages.

#### Make it easy to unsubscribe

Always give recipients an easy way to unsubscribe from your messages. Letting people opt out of your messages can improve open rates, click-through rates, and sending efficiency.

**Important:** If you send more than 5,000 message per day, your [marketing and subscribed messages must support one-click unsubscribe](#requirements-5k).

To set up one-click unsubscribe for Gmail messages, include both of these headers in outgoing messages:

- List-Unsubscribe-Post: `List-Unsubscribe=One-Click`
- List-Unsubscribe: `<https://solarmora.com/unsubscribe/example>`

When a recipient unsubscribes using one-click, you receive this POST request:

"POST /unsubscribe/example HTTP/1.1 Host: solarmora.com Content-Type: application/x-www-form-urlencoded Content-Length: 26 List-Unsubscribe=One-Click"

Learn more about List-Unsubscribe: headers in [RFC 2369](https://tools.ietf.org/html/rfc2369) and [RFC 8058](https://tools.ietf.org/html/rfc8058).

These unsubscribe options can also be used but they should not replace one-click unsubscribe:

- Let recipients review the individual mailing lists they’re subscribed to. Let them unsubscribe from lists individually, or all lists at once.
- Automatically unsubscribe recipients who have multiple bounced messages.

### Message formatting requirements and guidelines

Follow these message formatting guidelines to help ensure messages are delivered as expected:

- If your messages are in HTML, format them according to [HTML standards](https://html.spec.whatwg.org/multipage/).
- Follow these message header guidelines:
 - From: headers should include only one email address. For example: 
    From: notifications@solarmora.com
 - Avoid excessively large message headers. To learn more, visit [Gmail message header limits](/a/answer/14016360).
- Format messages according to the Internet Format Standard ([RFC 5322](https://tools.ietf.org/html/rfc5322)).
 - Make sure every message includes a valid Message-ID.
 - Make sure single-instance message headers are included only once in a message. Examples of single-instance headers include From:, To:, Subject:, and Date:.
- Message headers and message content should be accurate, and not misleading or deceptive.
 - Email message subject, headers, display names, and other message elements should accurately represent the sender identity and message content, and shouldn’t be misleading. For example, don’t send messages with subject lines starting with Re: or Fwd: unless the messages are actual replies or forwards, and include only actual senders and recipients in From: and To: headers.
 - Don't use emojis or other non-standard characters to imitate graphic elements in messages, with the intent to deceive or influence recipients. For example, don’t use emojis or images next to display names or brand names to imply the name has been verified in some way.
 - Don’t use HTML and CSS to hide content in your messages. Hiding content might cause messages to be marked as spam.
 - Web links in the message body should be visible and easy to understand. Recipients should know what to expect when they click a link.
 - Sender information should be clear and visible.
- Format the following international domains according to [Section 5.2 of Unicode Technical Standard #39](http://www.unicode.org/reports/tr39/#Restriction_Level_Detection). An international domain is also called an ;*internationalized domain name (IDN*), and is a URL that is specific to a region or country.
 - Authenticating domain
 - Envelope from domain
 - Payload domain
 - Reply-to domain
 - Sender domain

### Guidelines for email display names

Misuse of display names can impact email deliverability when sending to personal Gmail accounts. When you send commercial or bulk email, it’s important to follow the [Email sender guidelines](/a/answer/81126) and to respect recipients’ inboxes. Follow the display name guidelines here to help ensure your messages are delivered as expected.

#### **Display name guidelines**

Sender display names should be used exclusively to identify the sender.

Display names should reflect a consistent, clear, and accurate statement of the sender's identity, name and/or organization.

Don’t include subject or message content in display names.

Display names should never be used to attempt to deceive the recipient of the email.

Avoid misleading or deceptive display names by following these guidelines:

- Identify the sender first and don’t include subject or message content in this display name. For example, don’t use display names like these:
 - Important Update ---------- From [Company Name]
 - TIME IS RUNNING OUT (SALE)
 - [Product/News] Alert
 - URGENT REQUEST
 - Last Chance
- The display name should not include the recipient’s name and should not imply a message reply or threaded conversation. For example, don’t use display names like these:
 - [recipient’s first name] <info@organization.com>
 - User (2)
- The display name should clearly identify the sender and shouldn't include emojis or other non-standard characters to imitate graphic elements. For example, don’t use display names like these:
 - ![](//storage.googleapis.com/support-kms-prod/vkw133ZXkbLgmrgXGJnhjgOjcT18wm4L6LOa) LATEST UPDATE
 - MAIL, ME ![](//storage.googleapis.com/support-kms-prod/2d2OWuojrmIaWtXUAcZw525P6w97ZTGzsG1S)
 - ![](//storage.googleapis.com/support-kms-prod/zsu6j9LDhrDwKnH5i2CmXyVClaxer1NqV6nd)
 - [1] New Message

#### **Spoofing and display names**

Avoid these types of spoofing, which are deceptive display name practices:

- Using an @gmail.com domain as the display name for bulk email
- Using characters that imply the mail is part of threaded conversation, for example: User (2)
- Using the name of the recipient in the display name

To manage an effective email campaign, your messages should connect you and your recipients in a meaningful way. Be sure to follow all [Email sender guidelines](/a/answer/81126) to improve your email delivery and effectiveness. Senders who fail to follow best practices may not be considered for deliverability mitigations.

### Sending practices requirements and guidelines

To reduce the chances that messages from your domain are sent to spam or blocked by Gmail, follow the best practices in this section.

- Authenticate email with SPF and DKIM that are aligned with each other at the organizational level. If you use an email provider, verify that your provider supports this.
- Ideally, send all messages from the same IP address. If you must send from multiple IP addresses, use a different IP address for each message type. For example, use one IP address for sending account notifications and a different IP address for sending promotional messages.
- Messages of the same category should have the same From: email address. For example, messages from a domain called **example.com** might have From: addresses like:

 - Sales receipt messages: **sales@example.com**
 - Promotional messages: **deals@example.com**
 - Account notification messages: **alert@example.com**
- Messages sent from an address in the recipient’s contacts are less likely to be marked as spam.

#### Sending practices to avoid

- Don't mix different types of content in the same message. For example, don't include promotions in sales receipt messages.
- Don't impersonate other domains or senders without permission. This practice is called *spoofing*, and Gmail might mark these messages as spam.
- Don't mark internal messages as spam. This can negatively affect your domain's reputation, and future messages might be marked as spam.
- Don't purchase email addresses from other companies.
- Don't send messages to people who didn't sign up to get messages from you. These recipients might mark your messages as spam, and future messages to these recipients will be marked as spam.
- Avoid opt-in forms that are checked by default and that automatically subscribe users. Some countries and regions restrict automatic opt-in. Before you opt-in users automatically, check the regulations in your region.

Some legitimate messages may be marked as spam. Recipients can mark valid messages as not spam, so future messages from the sender should be delivered to their inbox.

#### Increase sending volume slowly

When increasing sending volume, keep in mind:

- Increasing the sending volume too quickly can result in delivery problems. As you gradually increase your sending email volume, use [Postmaster Tools](/mail/answer/6227174) to monitor email delivery.
- For Google Workspace work and school accounts, sending limits apply even when recipients are in different Google Workspace domains. For example, you might send email to users with email addresses that have the domains **your-company.net** and **example.com***.* Although the domains are different, if both domains have **google.com** as their MX record, messages sent to these domains count toward your limit.
- If you use Google Workspace or Gmail for sending: When you reach the sending limit, the sending rate is limited for the sending IP address.

If you send large amounts of email, we recommend you:

- Send email at a consistent rate. Avoid sending email in bursts.
- Start with a low sending volume to engaged users, and slowly increase the volume over time.
- As you increase the sending volume, regularly monitor server responses, spam rate, and the sending domain's reputation. Regular monitoring will allow you to quickly adapt if your sending is rate limited, if the spam rate is increased, or when the sending domain's reputation drops.
- Avoid introducing sudden volume spikes if you do not have a history of sending large volumes. For example, immediately doubling previously sent volumes suddenly could result in rate limiting or reputation drops.
- If you change the format of your bulk emails, gradually increase the sending volume of messages with the new format.
- After making any significant changes to your sending infrastructure or email header structure, increase the modified segment of traffic separately.
- If messages start bouncing or start being deferred, reduce the sending volume until the SMTP error rate decreases. Then, increase slowly again. If bounces and deferrals continue at a low volume, review individual messages to identify problems. For example, you can try sending a blank test message and see if it experiences issues.
- Stay within the IP limits for sending:
 - Be aware of email sending limits when sending from domains that have a Google.com MX host.
 - Limit sending email from a single IP address based on the MX record domain, not the domain in the recipient email address.
 - Monitor responses so you can change sending rates as needed to stay within these limits.

These factors affect how quickly you can increase sending volume:

- Amount of email sent: The more email that you send, the more slowly you should increase sending volume.
- Frequency of sending email: You can increase the sending volume more quickly when you send daily instead of weekly.
- Recipient feedback about your messages: Make sure you send only to people who subscribe to your emails, and give recipients an option to unsubscribe.

In the event of a recent spike in email activity, we recommend following the requirements and guidelines on this page to resolve deliverability issues automatically during following sends.

## Additional guidelines

### Guidelines for using email service providers

Google and Gmail don’t accept allowlist requests from email providers. We can't guarantee messages sent by email providers will pass Gmail’s spam filters.

If you use a third-party email provider to send email for your domain:

- Verify that the provider follows the guidelines on this page. Large providers, such as Google, AOL, and Yahoo, typically follow these guidelines.
- Make sure the SPF record for your domain includes all email senders for your domain. If third-party senders aren't included in your SPF record, messages sent from these providers are more likely to be marked as spam. [Learn how to set up your SPF record](/a/answer/10685031#more-senders).

If you use a domain provider but you manage your own email, we recommend you:

- Review and follow the requirements and guidelines on this page.
- Use [Postmaster Tools](/mail/answer/6227174) to monitor information about messages sent from your domain to Gmail accounts.

### Guidelines for email service providers

When clients use your service to send email, you’re responsible for their sending practices. We recommend taking these steps to help manage your clients’ sending activity:

- Offer an email address for reporting email abuse, for example: **abuse@email-provider.com**.
- Make sure your contact information in your WHOIS record and on [abuse.net](https://abuse.net/) is current.
- Immediately remove any client who uses your service to send spam.

### Affiliate marketing

Affiliate marketing programs offer rewards to companies or individuals that send visitors to your website. However, spammers can abuse these programs. If your brand is associated with marketing spam, other messages sent by you might be marked as spam.

We recommend you regularly monitor affiliates, and remove any affiliates that send spam.

### Phishing exercises

Don’t send test phishing messages or test campaigns from your domain. Your domain’s reputation might be negatively affected, and your domain could be added to internet blocklists.

## Monitoring and troubleshooting

### Postmaster Tools

Use [Postmaster Tools](/mail/answer/9981691) to get information about the email you send to Gmail users, for example:

- When recipients mark your messages as spam
- Why messages might not be delivered as expected
- If messages are authenticated
- Your domain or IP reputation and the impact on message delivery rates

#### Spam rate

- #### Regularly monitor your domain's spam rate in [Postmaster Tools](/mail/answer/9981691).
- Keep spam rates reported in [Postmaster Tools](https://gmail.com/postmaster) below 0.10% and avoid ever reaching a spam rate of 0.30% or higher. [Learn more](#spam-rate)
- Maintaining a low spam rate helps senders be more resilient to occasional spikes in user feedback.
- Maintaining a high spam rate leads to increased spam classification. It can take time for improvements in spam rate to reflect positively on spam classification.

#### Open rate

- Google doesn't track open rates.
- Google can't verify the accuracy of open rates reported by third parties.
- Low open rates aren't necessarily an accurate indicator of deliverability or spam classification issues.

### Troubleshooting email delivery

If messages aren't being delivered as expected:

- Check regularly that your domain isn’t listed as unsafe with [Google Safe Browsing](https://transparencyreport.google.com/about).
- To check your domain status, enter your domain in the [Safe Browsing site status page](https://transparencyreport.google.com/safe-browsing/search).
- Regularly check the status of any domains that are linked to yours.

#### Sending with email service providers

If you’re having delivery issues with email sent by a service provider, verify the provider follows the requirements and guidelines on this page.

#### Use the Google Admin Toolbox to review domain settings

Use the [Google Admin Toolbox](https://toolbox.googleapps.com/apps/checkmx/) to check and fix settings for your domain.

#### Fix the source of rejected email

If your messages are rejected, you might get an error message. Learn more about the error so you can fix the problem. Common error messages are:

- **421, "4.7.0":**Messages are rejected because the sending server’s IP address is not on the allowed list for the recipient’s domain.
- **550, "5.7.1":** Messages are rejected because the sending server’s IP address is on an IP suspended list. You might get this error if you’re sending email using a shared IP with a poor reputation.

Learn more about email and SMTP error messages:

- [SMTP error reference](/a/answer/3726730)
- [Fix bounced or rejected emails](/mail/answer/6596)

#### Fix IPv6 authorization errors

An IPv6 authorization error could mean that the PTR record for the sending server isn’t using IPv6. If you use an email service provider, confirm they’re using an IPv6 PTR record.

Here's an example of an IPv6 authorization error:

**550-5.7.1:** Message does not meet IPv6 sending guidelines regarding PTR records and authentication.

#### Use the troubleshooting tool

If you’re still having email delivery problems after following the guidelines in this article, try [Troubleshooting for senders with email delivery issues](/mail/troubleshooter/2696779).

## Related topics

- [Email sender guidelines FAQ](/a/answer/14229414)
- [Fixed bounced emails](/mail/answer/6596)
- [Fix messages rejected by Google Groups](/a/answer/168383)

*Translations of our policies are provided for your convenience. If there is a conflict between the text of this policy in language other than English and the text of the English language version of the policy, the text of the English language version of the policy takes precedence.*

## Was this helpful?

How can we improve it?

YesNo

Submit