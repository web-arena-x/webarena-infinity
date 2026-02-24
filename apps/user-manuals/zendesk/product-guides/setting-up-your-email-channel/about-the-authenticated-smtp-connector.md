# About the authenticated SMTP connector

Source: https://support.zendesk.com/hc/en-us/articles/6740880198810-About-the-authenticated-SMTP-connector

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

The authenticated SMTP connector lets you connect your email server to your support instance, ideal for organizations with strict data policies. Choose between two-way or outbound-only relay to control email flow. Two-way relay offers enhanced tracking and security, while outbound-only relay provides flexibility with cloud services. Ensure compliance by reviewing security requirements and customer agreements before implementation.

Location:  Admin Center > Channels > Talk and email > Email

Note: Due to Microsoft Exchange Online retiring Basic
authentication for SMTP at the end of December, 2026, customers using Microsoft
Exchange should use the Zendesk [Exchange connector](https://support.zendesk.com/hc/en-us/articles/8979947090586) instead of the SMTP connector. See
the [announcement](https://support.zendesk.com/hc/en-us/articles/10203154603546) for details.

The authenticated SMTP connector lets you connect a non-Zendesk email server to your
Zendesk Support instance. It is specifically designed for organizations that prefer to
use their own email servers or cannot use third-party email servers due to internal
corporate policies, data regulations, or encryption needs.

There are two different ways you can use the connector to meet the needs of your company:
*two-way authenticated relay* or *outbound-only authenticated relay*. Each
use case has a distinctive way of relaying email and is set up differently, so it is
important to understand how you intend to use it.

Note: Before implementing this feature, familiarize yourself with
Zendesk’s [Security Configuration Requirements for HIPAA or HDS
Enabled Accounts on Zendesk](https://support.zendesk.com/hc/en-us/articles/4408828395802) and the terms and conditions of the [Zendesk Customer Agreement](https://www.zendesk.com/company/agreements-and-terms/zendesk-customer-agreement/), particularly those
related with Non-Zendesk Services. While this feature does ensure TLS encryption during
use, that alone does not change HIPAA compliance responsibilities.

This article includes the following topics:

- [Using the connector for two-way authenticated email relay](#zug_SMTP_connector_about__section_mcz_m3v_zcc)
- [Using the connector for outbound-only authenticated email relay](#zug_SMTP_connector_about__section_h43_hjv_zcc)

## Using the connector for two-way authenticated email relay

Use two-way authenticated relay to establish a secure and authenticated two-way
connection between your email domain or service and Zendesk's servers. While this
requires more setup and configuration, it is ideal for on-premise servers or domains
with added security layers, such as Mimecast. Organizations with strict data
compliance and security requirements may prefer this setup, as it keeps all email
data within their controlled environment, reducing the risk of data breaches and
non-compliance.

Figure 1. Email flow for two-way authenticated email relay
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_SMTPAuth_flow.png)

Other advantages of two-way authenticated relay include:

- **Improved tracking and management.** You can better track interactions
  and manage email threads. This ensures all communications are logged and
  organized within your support system, improving the overall customer support
  experience. In addition, tags are added to tickets created by
  unauthenticated or authenticated email, allowing you to [use ticket triggers to help track
  unauthenticated email](https://support.zendesk.com/hc/en-us/articles/8156703046298).
- **Better control over email policies.** Organizations can implement their
  own email policies and controls when using their email servers to send and
  receive emails. This allows for greater flexibility in managing spam
  filters, security protocols, and other email-related settings.
- **Simplified troubleshooting.** When both sending and receiving are
  handled by the same system, troubleshooting can be simplified. Email
  delivery or reception issues can be diagnosed more efficiently when both
  processes are managed within the same environment.

For more information, see [Setting up the authenticated SMTP connector for two-way email
relay](https://support.zendesk.com/hc/en-us/articles/7189260823194).

## Using the connector for outbound-only authenticated email relay

Use outbound-only authenticated relay to allow for standard auto-forwarding of
inbound email traffic to Zendesk, but an authenticated outbound connection with your
email domain or service so all outbound sending for the connected addresses occurs
through your domain or email service.

Although this option uses standard auto-forwarding, it requires a different setup
that can't leverage existing addresses using standard auto-forwarding. Each support
address must be newly added using the authenticated workflow.

Figure 2. Email flow for outbound-only authenticated email relay
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_SMTPAuth_flow_outbound.png)

Organizations may choose outbound-only authenticated relay for the following
reasons:

- **Email service limitations.** Setting up the connector this way allows
  for cloud-based email services that don’t offer authenticated outbound
  relays to other systems, like Exchange Online, Office365 Cloud, and
  G-Suite.
- **Flexibility and scalability.** Forwarding inbound email traffic allows
  organizations to use external email services to receive emails. This can
  provide greater flexibility and scalability, especially as the organization
  grows.
- **Simplified Management.** Using a third-party service for inbound emails
  can simplify management, as these services typically handle updates,
  security, and maintenance, allowing organizations to focus on other
  priorities.

For more information, see [Setting up the authenticated SMTP connector for outbound-only
email relay](https://support.zendesk.com/hc/en-us/articles/8043218178842).