# Using email encryption and private email relay services with Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/4408823267738-Using-email-encryption-and-private-email-relay-services-with-Zendesk

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article examines the challenges of using email encryption and private relay services with Zendesk, highlighting issues with maintaining security and sender anonymity. It also discusses different email encryption types and the implications of private email relays for Zendesk's functionality.

This article contains the following sections:

- [Understanding the limitations when using email encryption and relay services with Zendesk](#h_01KC2VVHP29DQ8BMP5KV6NCTRS)
- [About email encryption](#h_01ERZ685CCPTBC61R1XQQ9P3CR)
- [About private email relays](#h_01ERZ68EHKVY2549VEGA0C3JJ0)

## Understanding the limitations when using email encryption and relay services with Zendesk

It's becoming increasingly common for organizations to send email using *email encryption* or through a *private email relay service* which masks the email identity and domain of the original sender.

While it is possible that either of these two systems *might* work with Zendesk, the result is largely dependent on the state of the email that is being sent or forwarded and what form its in for that part of the relay process. For private email services, the success depends on how they are maintaining the consistency of the conversation thread and adhering to the protocols that allow that to happen.

Where possible and making sure you are in accordance with all legal, security, and privacy agreements or requirements, it's best to send or forward Zendesk an unencrypted email when you can verify that you are doing so safely and securely.

Zendesk can't decrypt an email for you as if we were the intended recipient and we possess the necessary identity to act upon the email, or to provide you any useful information on who the sender was that emailed you using a private relay service. The purpose of encryption (which requires authentication for the decryption process) is to prevent the unwanted interception of information. Zendesk functions as a repository of information, but is often inhabiting the role of an intermediary relay in the overarching process. The purpose of private email relays is to obscure the identity of the sender and the sender's true domain.

While decrypting emails or determining the identity of a masked sender is a *near* mathematical impossibility,  it would be a violation of our own security and privacy policies and possibly a violation of state or federal privacy laws to attempt to decrypt them.

Zendesk is responsible for preserving the security of communications, which includes the sending services of encrypted or private emails.

## About email encryption

There are a few forms of [email encryption](https://en.wikipedia.org/wiki/Email_encryption) in use today. The two most popularly used are S/MIME and PGP/MIME.

- [S/MIME](https://en.wikipedia.org/wiki/S/MIME) (Secure/MIME) is the most widely used, as it is built into the infrastructure of several large email providers - OSX, iOS, Outlook, Gmail, etc.
- [PGP/MIME](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) (PrettyGoodPrivacy/MIME) relies on a decentralized model and a third-party encryption tool.

There are a variety of others including encryption protocols that are entirely proprietary. Some of these function only when the email is in-transit, so are invisible to the end-users viewing emails within their authenticated clients. Others require strict authentication from the user before the email can be readable by a human. When an email is forwarded to another service, as it often does when arriving at Zendesk's inbound processing servers, we are entirely reliant on the encryption state in which the email arrives.

Zendesk currently only supports opportunistic-TLS as an end-to-end email encryption protocol. This means that on both inbound and outbound email we will accept or send TLS-encrypted email if the sending or recipient server also supports that protocol. Here is the [overview article of our security features](https://www.zendesk.com/product/zendesk-security/).

### Zendesk features using TLS encryption

If you have email encryption needs then we offer three features that use TLS encryption: [Exchange Connector](../setting-up-your-email-channel/about-the-microsoft-exchange-connector.md), [Gmail Connector](https://support.zendesk.com/hc/en-us/articles/4408835030426-Turning-on-automatic-ticket-creation-for-your-Gmail-inbox), and the [Authenticated SMTP Connector](https://support.zendesk.com/hc/en-us/articles/6740880198810-About-the-Authenticated-SMTP-Connector).

The first two features retrieve and relay email to your provider using API calls, which are always SSL/TLS encrypted. The Authenticated SMTP Connector also uses TLS encryption over smtp as it requires a username and password, which must be encrypted before being sent or received. The outbound-only version of this feature is encrypted only for outbound traffic, but forced-TLS can be enabled at the sending/forwarding service to accomplish a similar goal, ensuring encryption in transit.

The Gmail Connector can fall back to sending from our infrastructure if rate limits are exceeded, where TLS encryption is always offered for outbound relays but not guaranteed, as it is dependent on the receiving server accepting the TLS connection.

## About private email relays

These services are designed to obscure the identity of the sender. Under the best circumstances we are interacting normally, though with a proxy email address.

Where issues generally arise is in the usage of tokenized Reply-To: addresses. These headers fields indicate to a recipient email service the address to which any response should be sent. It becomes the address in the To: field of your email client (MS Outlook, Mac Mail, Gmail, Yahoo, etc.) when you click Reply or Reply-all. Private email relays by necessity must populate this field with something other than the original sender's email address, otherwise the relay would not be private.

Often, these services rely on a tokenized address that can only be parsed and routed based on the tokenized string found in the local portion of the email address, as well as the domain portion of the email address reflecting the private email relay's resource instead of the original sender. These tokens are protected from conversion by a recipient as a foundational aspect of the service that they are providing. Because these services are designed for maximum user identity protection, the recipient service can stop delivery of any email attempts if the user chooses to end the email thread. This prohibitive behavior is entirely beyond a sending server's control to negotiate.

Zendesk understands that any communication from your customer to you is important, it is equally important that the senders of these types of emails want their information to be seen only by the recipient they have designated it for. If you are forwarding email to us then your own forwarding address very well might be the intended recipient. Navigating into the inbox of that forwarding support address might offer some insight and benefit into gaining more information about these types of email relays.