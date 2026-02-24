# Setting up the authenticated SMTP connector for two-way email relay

Source: https://support.zendesk.com/hc/en-us/articles/7189260823194-Setting-up-the-authenticated-SMTP-connector-for-two-way-email-relay

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

The authenticated SMTP connector enables secure, two-way email relay using your own email server, meeting security and regulatory needs. It's ideal for industries with strict protocols, offering visibility into email flow and preventing unauthorized use. Ensure email headers remain unchanged, test in a sandbox, and manage credentials carefully. Avoid using with cloud-based services like Google or Microsoft.

Location:  Admin Center > Channels > Talk and email > Email

Note: Due to Microsoft Exchange Online retiring Basic
authentication for SMTP at the end of December, 2026, customers using Microsoft
Exchange should use the Zendesk [Exchange connector](https://support.zendesk.com/hc/en-us/articles/8979947090586) instead of the SMTP connector. See
the [announcement](https://support.zendesk.com/hc/en-us/articles/10203154603546) for details.

The authenticated SMTP connector lets you connect a non-Zendesk email server to your
Zendesk Support instance. It is specifically designed for organizations that prefer to
use their own email servers or cannot use third-party email servers due to internal
corporate policies, data regulations, or encryption needs.

By establishing a secure connection using authenticated and TLS-encrypted SMTP for both
inbound and outbound traffic (each using their own credentials), the connector allows
you to run your business in ways that meet both your internal and external security and
regulatory requirements. It also gives you more visibility into the flow of your email
traffic. This flexibility is essential for industries like healthcare, financial
services, and government agencies, which often must adhere to strict security protocols.
It also helps to prevent unauthorized use of the email service for spam or other
malicious activities.

This article includes the following topics:

- [Understanding how email is transmitted with two-way authentication](#topic_x3w_kqw_xcc)
- [Considerations](#topic_ukf_g1w_zcc)
- [Important information about email headers](#topic_gqs_g1w_zcc)
- [Configuring the connector for two-way authenticated email relay](#topic_jxl_g5w_xcc)
- [Signing your outbound email traffic with your DKIM signature](#topic_ttd_zcx_xcc)
- [Rotating or changing credentials](#topic_spx_x2x_xcc)
- [Disconnecting the connector](#topic_wd2_nfx_xcc)

Related articles:

- [Using ticket triggers to create workflows for unauthenticated email](https://support.zendesk.com/hc/en-us/articles/8156703046298)
- [Email resources](https://support.zendesk.com/hc/en-us/articles/4408846000410)

## Understanding how email is transmitted with two-way authentication

SMTP is not new to Zendesk; Zendesk currently uses an SMTP relay for all inbound and
outbound emails (except the Gmail and Exchange connectors).

The authenticated SMTP connector functions like the current SMTP process for email
traffic, except that it relays email to and from your business mail server to
Zendesk and passes secure credentials (username and password) as part of those
inbound and outbound relays.

Figure 1. Email flow with the authenticated SMTP connector
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_SMTPAuth_flow.png)

The main advantage of this solution is that it allows you to send and receive email
traffic to and from your customers using your domain’s email services while ensuring
encrypted and secure relays to and from Zendesk.

Once [configured](#topic_jxl_g5w_xcc), here’s how the
authenticated SMTP connector works in a typical email workflow:

1. **End user submits support request**: When an end user emails a support
   request to your domain’s support address, the user’s email client establishes a
   standard SMTP connection to your business mail server.
2. **Authentication via your mail server**: Your business mail server then
   establishes an authenticated SMTP connection to Zendesk’s email infrastructure,
   ensuring that only authorized services can be validated through that
   workflow.
3. **Email sent to Zendesk via SMTP**: Once the service is authenticated, your
   business mail server relays the encrypted email to Zendesk.
4. **SMTP Connector**: The connector verifies the secure credentials for the
   incoming traffic (domain, username, and password) and passes it to the inbound
   Zendesk mail server.
5. **Ticket created**: The email is received, and a ticket is created in Zendesk
   with a tag indicating the relay was secure.
6. **Ticket notifications**: Notifications are sent back using your designated
   and authenticated SMTP-ready domain for outbound sending to the intended
   recipients.

## Considerations

- The SMTP connector for two-way email relay is not supported when using
  cloud-based email services such as Google or Microsoft, as these services don't
  allow outbound authenticated SMTP connections. However, you can use the
  connector for [outbound-only authenticated email
  relay](https://support.zendesk.com/hc/en-us/articles/8043218178842) and standard auto-forwarding of inbound email traffic to
  Zendesk.
- [CCs and followers](https://support.zendesk.com/hc/en-us/articles/5179445630234) must be turned on in
  your account.
- It's very important that you *do not* make a newly added address the default
  support address until you've verified that it is functioning correctly. You risk
  locking yourself out of your account if you can't receive password reset and
  access emails.
- Because the connector relies on two-way authenticated relays to occur, we
  recommend testing this feature in your [Zendesk sandbox environment](https://support.zendesk.com/hc/en-us/articles/6150628316058) before
  using it in production. This is to give your domain admin, IT team, or email
  provider time to understand the workflow and relationship between the two
  resources fully.
- Do not add the same support address in your sandbox and production accounts.
  This may result in inconsistent behavior with Zendesk or your email server. Use
  your sandbox environment to test, then delete all the test domains and support
  addresses before adding them to your production account.
- Email must be sent and received from the same domain. You cannot receive
  incoming authenticated emails from one domain and send outgoing authenticated
  emails from a different domain.
- The authenticated SMTP connector doesn't allow you to send email on behalf of
  your Zendesk system support addresses (for example,
  support@*yoursubdomain*.zendesk.com).
- During initial setup, email sent through your existing support addresses for the
  account or brand will not be interrupted and continue to function normally.
- After you add a support address for outbound sending through the authenticated
  SMTP connector and the address is verified, Zendesk will begin sending email
  through the authenticated domain.
- Up to 50 support addresses can be added to Zendesk for outbound sending through
  a single SMTP domain. You can add up to 10 domains for a total of 500 addresses,
  but only 50 support addresses can be added for each domain.
- [Graylisting](https://www.mail.com/blog/posts/what-is-greylisting/33/) for this traffic is not
  recommended, particularly for verification emails. These emails complete the
  forwarding circuit and confirm that traffic is relayed successfully.
- You should add the Zendesk IPs to your network allowlist to ensure a reliable
  connection.
- If you disconnect the connector and continue to forward traffic to Zendesk, it
  will create and update tickets, though those updates will not be
  authenticated.

## Important information about email headers

Email headers (such as `To`, `From`,
`CC`, and `Reply-To`) contain important data and
metadata about an email message.

Your administrator may want to change email headers for several reasons. However,
it’s important to note that some header fields should *never* be altered since
they are critical for ensuring the correct delivery and integrity of the message.
Changing standard headers at the account's email domain before outbound sending is
not supported. Any issues that emerge as a result of this should be investigated and
corrected at the external domain.

The below headers should persist throughout the outbound relay process:

```
Auto-Submitted: auto-generated
X-Auto-Response-Suppress: All
X-Mailer: Zendesk Mailer
X-Zendesk-From-Account-Id: ******
X-Zendesk-Email-Id: ************************
```

Changing your email header fields doesn’t change how Zendesk works; it only changes
how you send your outbound messages and how you might receive responses. The
relationships between the requester, agents, and CCs in the email and subsequent
ticket should not change.

## Configuring the connector for two-way authenticated email relay

Share these configuration steps with your domain admin or IT team, as they involve
obtaining and providing credentials that must be securely transferred and added to
your business email servers and Zendesk account.

There are two steps to configuring the connector:

1. [Adding an authenticated domain
   to Zendesk](#topic_oby_zvw_xcc)
2. [Adding a support address for
   outbound sending](#topic_ppz_yyw_xcc)

### Adding an authenticated domain to Zendesk

Begin by adding the domains for which all inbound and outbound traffic should be
authenticated through your business mail server. You should have no existing
support addresses currently using the domain, as the connector requires that
support addresses be added after the domain has been configured. All incoming
traffic should arrive through the authenticated connection.

At the end of this step, Zendesk provides you with credentials to share with your
domain administrator or IT team so they can properly configure your business
email servers.

**To add an authenticated domain to Zendesk**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. Click **Edit Authenticated SMTP Connectors**.
3. Click **Add domain**.

   The Add domain page
   appears.
4. Add a name for the connection. This can be a purpose-specific name or one
   that correlates directly to the domain being connected.
5. In the Domain field, enter the inbound domain from which you would like to
   allow Zendesk to receive incoming email.
6. Click **Add domain**.

   A page appears with your inbound
   credentials.
7. Copy the credentials to a secured location or document and provide them to
   your domain administrator or IT team. Because these credentials allow
   secured connections, they must be treated as sensitive and protected
   information. The credentials will not be displayed again.
8. (Optional) If your email service requires an email address for the username,
   you can use *yoursubdomain@yoursubdomain*.zendesk.com (replace
   *yoursubdomain* with your Zendesk subdomain). You should also
   create this exact same address
   (*yoursubdomain@yoursubdomain*.zendesk.com) in your account so that if
   your email provider sends any emails to the address, they will be received
   in your Zendesk account.

   Important: These
   credentials are only displayed once to your Zendesk admin. You must
   start over or rotate the credentials if they are lost. Zendesk cannot
   obtain them for you.
9. Click **Done**.

The connection appears in the authenticated SMTP connectors list with the status
"Connection required." To finish setting up the connection, continue to [Adding a support address for
outbound sending](#topic_ppz_yyw_xcc).

### Adding a support address for outbound sending

You must add an outbound support address to finish setting up your connection.
This means configuring Zendesk with your SMTP server settings, including the
domain username and password.

This step is critical, as the authenticated SMTP connector requires inbound and
outbound connections.

Before beginning this step, note the following:

- You will need to obtain the secured credentials for your domain (host,
  username, and password) from your domain administrator, IT team, or service
  provider.
- You will need the intended support address, with the above credentials, at
  your email service. The address must exist before Zendesk can interact with
  it. Aliases and distribution groups are not supported.
- Adding unique credentials is recommended for each address or brand so you
  can track traffic with greater specificity. Although this requires more work
  and credentials to manage, it can be helpful when rotating credentials or
  mitigating a possible security issue in which a set of credentials may have
  become compromised.
- You will want to verify that your email service is signing your outbound
  traffic with your [DKIM
  signature](#topic_ttd_zcx_xcc).
- You cannot use the API to add support addresses for this feature.

**To add a support address for outbound sending**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. Click **Manage support addresses**.
3. Click **Add address** > **Connect external address**.
4. If you have multiple brands, select the brand for the email address from the
   drop-down menu.
5. Select **Authenticated SMTP connector**, then click **Next**.
6. Select the domain associated with the address you wish to add, then enter
   the support address you want to connect. Click **Next**.
7. Add the domain credentials provided to you by your domain administrator or
   IT team. These credentials must be handled in the most secure manner
   possible.
8. Click **Save**.

## Signing your outbound email traffic with your DKIM signature

As described in [Digitally signing your email with DKIM](https://support.zendesk.com/hc/en-us/articles/4408822303386), Zendesk Support
allows DKIM authentication. DKIM provides a way to authenticate that an email was
sent from the domain it claims to be from. This is done by attaching a digital
signature to the outgoing emails, which can be verified against a public
cryptographic key published in the domain's DNS records.

When using the authenticated SMTP connector, Zendesk will *not* sign outbound
traffic with our `d=zendesk.com` DKIM tag within the header. If you
have enabled digital signatures in Zendesk after adding the required CNAME records
to your domain, Zendesk will sign the outbound traffic on your behalf and add the
`d=yourdomain.com` DKIM tag to the outbound
header.

Your domain can re-sign with your DKIM signature, if you choose. If you opt not to do
this, test and ensure you’re not inadvertently overwriting the signature we’ve added
for your domain before sending outbound production traffic.

Your domain may need to ignore SPF authority when we relay outbound traffic from
Zendesk to your email service (through this connection), as we will be creating a
“trusted sender” relationship with your email service, and you will be doing the
final authoritative outbound sending (SPF and/or DKIM) to your users.

Zendesk strongly recommends testing in a sandbox environment with test end users to
validate that the SPF/DKIM/DMARC checks are all passing.

## Rotating or changing credentials

Rotating allows for the temporary existence of two sets of credentials.

- You can use two sets of inbound credentials to achieve seamless credential
  rotation. Zendesk does not recommend using two sets in perpetuity, as this will
  limit what you can do if a sudden need to rotate credentials emerges.
- It's possible to cancel existing credentials immediately. This might be
  necessary if a security concern arises and your team wants to stop all
  authorization from the previous credentials.
- It's important to have valid Zendesk admin email addresses associated with your
  account and not to block traffic from Zendesk default native support addresses.
  These addresses are where Zendesk will send security and educational or
  confirmation emails from, so it's essential that key stakeholders can receive
  them.

## Disconnecting the connector

If you want to discontinue use of the connector, consider doing so during a
low-traffic time. This is because the process takes a few minutes, and you may need
to coordinate with your domain administrator to re-send traffic that had been
attempted to be relayed during that time.

Depending on how many connected support addresses you have, you may want to leverage
the API’s [support addresses endpoint](https://developer.zendesk.com/api-reference/ticketing/account-configuration/support_addresses/) for faster
results. Only one address can be deleted at a time, but once you have the list of
[SMTP-connected address IDs](https://developer.zendesk.com/api-reference/ticketing/account-configuration/support_addresses/#list-support-addresses), the calls can
be made rapidly. Authenticated SMTP connector support addresses cannot be added
through the API. Credentials must be added in Admin Center to create the necessary
connection.