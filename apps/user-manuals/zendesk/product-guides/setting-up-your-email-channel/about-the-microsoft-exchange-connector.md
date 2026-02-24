# About the Microsoft Exchange connector

Source: https://support.zendesk.com/hc/en-us/articles/8979947090586-About-the-Microsoft-Exchange-connector

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

The Microsoft Exchange connector lets you connect your Microsoft 365 or Exchange Online email servers directly, enabling secure email traffic with your domain's services. It uses the Microsoft Graph API and OAuth for secure communication and supports email conversion to tickets. Note limitations like email size and rate limits. Avoid altering critical email headers to maintain message integrity.

The Microsoft Exchange connector allows you to connect your non-Zendesk email servers,
based on Microsoft Exchange, directly to your Zendesk Support instance. This is ideal
for Microsoft customers looking to connect their online Microsoft 365 or Exchange
servers and leverage their Exchange and Outlook workflows.

The main advantage of this solution is that it allows you to send and receive email
traffic to and from your customers using your domain’s email services, while ensuring
encrypted and secure relays to and from Zendesk.

Microsoft Exchange is the server powering all Microsoft email products, including
Microsoft 365. Therefore, the Zendesk Microsoft Exchange connector is compatible with
the online version of all Microsoft email products. The connector is incompatible with
Exchange Server on-premises. If you're using on-premises servers, the [SMTP connector](https://support.zendesk.com/hc/en-us/articles/6740880198810) may be a better option.

See [Connecting your Microsoft Exchange account to
Zendesk](https://support.zendesk.com/hc/en-us/articles/8994395472922) for more information on establishing and managing your
connections.

This article includes the following topics:

- [Understanding how email is transmitted with the Exchange connector](#topic_ejc_fzy_m2c)
- [Technical details](#topic_xgz_thz_42c)
- [Requirements](#topic_v14_3xz_m2c)
- [Limitations](#topic_kys_1tc_42c)
- [Understanding the email labeling system](#topic_rqp_c4s_kfc)
- [Considerations regarding email headers](#topic_yfr_nxz_m2c)

## Understanding how email is transmitted with the Exchange connector

Using an Exchange API, the Microsoft Exchange connector allows you to fetch email
from an Exchange inbox and automatically convert email messages to tickets. The API
is also leveraged to deliver outbound email from Zendesk to your Exchange mailbox.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/exchange_connector_flow.png)

Zendesk Support frequently checks for new email in your Exchange inbox. Only new,
unread email messages in the inbox will be converted into tickets. Ticket
notifications will be sent from your Microsoft email address.

## Technical details

- The Exchange connector uses the [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/overview) for communication with
  Microsoft.
- All communication between Zendesk and the Exchange server is conducted through
  HTTPS calls.
- The Exchange connector uses [OAuth](https://support.zendesk.com/hc/en-us/articles/4408845965210) for authorization access.
- During authorization, you are granting access to Zendesk's verified Azure
  application.
- Credentials used to access your Exchange mailbox are securely stored and
  encrypted at rest.
- Zendesk will request only the essential permissions required for the operations
  of the Exchange connector:
  - `openid`
  - `offline_access`
  - `email`
  - `User.Read`
  - `Mail.Send`
  - `Mail.ReadWrite`

## Requirements

- The Zendesk Exchange connector is compatible with Microsoft Exchange Online
  only. Exchange Server on-premises versions are not supported.
- To connect your Exchange mailbox to Zendesk, you must be able to sign in
  (authenticate and authorize) as the account associated with that Exchange
  mailbox.
- The Microsoft email address cannot be used by any other connection method (such
  as email forwarding), agent, or end user in your Zendesk account.
- You must use [OAuth](https://support.zendesk.com/hc/en-us/articles/4408845965210) to authenticate all Exchange API
  requests to Zendesk.
- You must set [permissions](https://learn.microsoft.com/en-us/powershell/module/exchange/add-mailboxpermission?view=exchange-ps) on the Exchange mailbox to
  control who can access the mailbox and what actions they can perform.
- Your Exchange admin must have the ability to grant permissions to Zendesk during
  authorization.

## Limitations

- Due to Microsoft API limitations, [personalized email replies](https://support.zendesk.com/hc/en-us/articles/4408887209498) don't
  work with the Exchange connector. The Microsoft account configuration
  determines the sender name on outgoing emails sent from the Exchange
  server.
- [Side conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746) don't utilize
  the Exchange connector for communication. Instead, emails related to side
  conversations are sent directly from Zendesk hosts (it's important to set up
  SPF and DKIM records when using external support addresses). [Side conversation child tickets](https://support.zendesk.com/hc/en-us/articles/4408836521498)
  follow the same configuration as other tickets and use the Exchange
  connector for communication.
- Due to requirements imposed by the Microsoft API, traffic through the
  Exchange connector has the following limitations.
  - Limitations when sending email from Exchange:
    - 30 emails per minute per mailbox (with retries for up to two
      hours)
    - 50MB per 5 minutes per mailbox
    - 10,000 different email recipients in a 24-hour period per
      mailbox (shared across multiple applications connected to
      the mailbox)

      Microsoft [announced](https://techcommunity.microsoft.com/blog/exchange/exchange-online-to-introduce-external-recipient-rate-limit/4114733) that
      this limit will be reduced to 2,000 per 24-hour period
      for existing customers starting in October
      2026.
  - Limitations when fetching email from Exchange to Zendesk:
    - 25 emails per minute per mailbox
    - Max email size is 50MB (including attachments)

  If you have questions about Microsoft's rate limits, open a ticket
  with Microsoft directly. Zendesk doesn't have additional information or
  the ability to negotiate higher rate limits.

## Understanding the email labeling system

The Microsoft Exchange connector is designed to help you efficiently manage your
inbox by applying labels to inbound emails, allowing you to easily track their
processing status. When emails are processed in Microsoft Exchange, the following
labels are applied:

- `Zendesk`: This label appears on all emails that have been
  processed by Zendesk. When only the `Zendesk` label is present,
  it means the email has been successfully imported into your Zendesk
  account.

  Important: Don't delete the
  `Zendesk` label from the emails in your inbox. Deleting
  the label may cause issues with the integration, preventing it from
  importing new emails, as it will continuously attempt to re-import older
  emails without the label.
- `RejectedByZendesk`: This label appears in addition to the
  `Zendesk` label when Zendesk couldn't import the email
  successfully. Emails tagged with both labels were processed but not imported
  into your Zendesk account.

### When an email might be rejected

There are several common reasons why an email receives the
`RejectedByZendesk` label:

- **Email size limitations**: Emails exceeding 50 MB cannot be processed.
  If your email contains large attachments, consider compressing or sharing
  the files through a cloud storage link instead.
- **Email format issues**: Emails with improper formatting, corrupted
  content, or invalid structure might be rejected. Verify that all required
  fields, such as `From` and `To`, are filled
  in. Additionally, ensure that the email body and any attachments are intact
  and properly uploaded.

## Considerations regarding email headers

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