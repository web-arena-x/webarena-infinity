# About the Advanced Data Privacy and Protection (ADPP) add-on

Source: https://support.zendesk.com/hc/en-us/articles/6561144266906-About-the-Advanced-Data-Privacy-and-Protection-ADPP-add-on

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Advanced Data Privacy and Protection (ADPP) |

Verified AI summary ◀▼

The Advanced Data Privacy and Protection add-on enhances security with features like access logs, advanced encryption, data retention policies, data masking, redaction suggestions, and automatic redaction. It helps you manage sensitive information, comply with data privacy regulations, and control data access. Available for Enterprise plans, it’s ideal for those with advanced data privacy needs.

Advanced Data Privacy and Protection is a set of features that expand on security
offerings already built into Zendesk Suite. It’s available as an add-on for Suite
Enterprise plans and above, as well as Support Enterprise plans.

This article answers the following questions about Advanced Data Privacy and Protection:

- [What is it?](#topic_myt_hvh_vzb)
- [How does it work?](#topic_tny_pvh_vzb)
- [Why should I use it?](#topic_gl3_xvh_vzb)
- [Who can use it?](#topic_hxt_yvh_vzb)
- [How do I get it?](#topic_shs_1wh_vzb)
- [Where can I learn more?](#topic_gf4_hxh_vzb)

## What is it?

The Advanced Data Privacy and Protection add-on is for customers with advanced data
privacy and security needs beyond the strong security Zendesk already provides for
every customer.

Watch the video below for more information about the Advanced Data Privacy and
Protection add-on.

Advanced Data Privacy and Protection 1:17

## How does it work?

Access logs, advanced data retention policies, redaction suggestions, and automatic
phone call transcription redaction are the first features available with this
add-on. Additional features are expected in future releases.

### Access log

The access log enhances data security and administrative control of your Zendesk
account. Use the access log to view or export access events for your account
related to tickets, user profiles, and searches. It provides insight into what
has been accessed based on the URLs that have been visited.

The access log is currently available as an [API](https://developer.zendesk.com/api-reference/ticketing/account-configuration/access_logs/) and from Admin Center.

**Access logs**:

- **Create a log of access events within 90 days** for your account related
  to tickets, user profiles, and searches.
- **Support data privacy compliance** by giving you visibility into whether
  the right agents are viewing the right data.
- **Help you proactively address security risks** by identifying suspicious
  behavior like repeated searches for personal or sensitive information.

For more information, see [Using the access log to monitor agent activity](https://support.zendesk.com/hc/en-us/articles/6066010357530).

### Advanced encryption

Advanced encryption allows your company to encrypt Service Data using your own
enterprise Key Management Service (KMS). This ensures that sensitive information
stored in Zendesk remains secure and inaccessible to unauthorized parties.

**Advanced encryption**:

- **Allows you to maintain your own encryption keys,** providing greater
  security and compliance while giving you complete control over access and
  usage.
- **Is compatible with industry-leading key management systems:** AWS KMS,
  Azure Key Vault, Google Cloud KMS, or Thales CipherTrust Manager, which is
  an EU-based KMS based in Europe and managed and hosted by European
  companies.
- **Supports backfilling and encrypting newly created and existing users**
  in your Zendesk account.

For more information, see [About advanced encryption](https://support.zendesk.com/hc/en-us/articles/5043582015898).

### Advanced data retention policies

Limit the data you keep with advanced data retention policies. Admins and agents
in custom roles with permission can create deletion schedules with conditions
for deleting tickets or end users. Once activated, deletion schedules
continuously search for and delete tickets or end users that meet the
conditions.

**Advanced data retention policies**:

- **Support compliance with data retention laws** by deleting the data your
  business doesn't need and keeping the data it does.
- **Enable you to define multiple deletion schedules** to fit different
  data types and compliance requirements.
- **Help you manage data storage in your account** by removing data to free
  up space.

For more information, see [Creating ticket deletion schedules](https://support.zendesk.com/hc/en-us/articles/6388012977306) and
[Creating end-user deletion
schedules](https://support.zendesk.com/hc/en-us/articles/6062884435866).

### Data masking

Data masking allows you to hide personally identifiable information (PII) from
agents in custom roles.

**Data masking**:

- **Allows certain roles to have end-user names, email addresses, and phone
  numbers obscured** based on custom role settings.
- **Helps reduce unnecessary exposure to sensitive information** by
  limiting the data agents can view.
- **Supports compliance with regulations such as the General Data Protection
  Regulation (GDPR)**, which emphasizes data minimization and controlled
  access

For more information, see [About data masking](https://support.zendesk.com/hc/en-us/articles/7713908123674).

### Redaction suggestions

Automatically highlight certain types of personally identifiable information
(PII) within a ticket for agents with appropriate permissions. Agents can then
click the highlighted PII and quickly redact it. This helps keep confidential
information out of Zendesk.

**Redaction suggestions**:

- **Give you control over which types of PII** should be automatically
  highlighted for agents within tickets.
- **Highlight identified PII** so that agents can quickly see what
  information might need to be redacted.
- **Allow agents to quickly redact** a single piece of identified PII or
  all identified PII within a ticket comment.

For more information, see [Automatically detecting sensitive information
for redaction](https://support.zendesk.com/hc/en-us/articles/6669399593882).

### Automatic redaction

When redaction suggestions are turned on, create triggers to remove detected
sensitive data from ticket comments automatically. This helps minimize or
eliminate the time spent identifying and redacting PII during ticket
handling.

**Automatic redaction**:

- **Automates the removal of large volumes of PII**.
- **Gives admins complete control over when and how PII is protected**
  within Zendesk.
- **Redacts PII automatically** based on trigger conditions, such as
  specific brands or ticket statuses.

For more information, see [Automatically redacting sensitive information in tickets using triggers](https://support.zendesk.com/hc/en-us/articles/9248330321050).

### Automatic phone call transcription redaction

Zendesk users can automatically redact PII and payment card industry (PCI)
information from transcribed call recordings.

- The PII redaction setting for call transcriptions automatically
  redacts PII data such as names, locations, and social security numbers.
- Using the PCI redaction setting, you can redact sensitive credit
  card information, including card numbers, expiration dates, and CVV codes
  from call transcriptions.

For more information, see [Zendesk call transcription and summarization
FAQ](https://support.zendesk.com/hc/en-us/articles/7470764710298).

## Why should I use it?

Zendesk is committed to a high level of security for every customer. The Advanced
Data Privacy and Protection add-on provides an additional level of security for
customers with higher data security and compliance requirements. It adapts to a wide
variety of security and compliance needs.

## Who can use it?

The table below summarizes the requirements for using the Advanced Data Privacy and
Protection add-on and its included features.

| What's available | Requirement type | Requirement details |
| --- | --- | --- |
| Access logs | Plan type | Suite Enterprise and above  Support Enterprise and above  (Legacy plans are not eligible) |
| Permissions | Admins Working with APIs generally requires some level of developer experience. You’ll need to work with a developer or other technical resource at your company to access, export, and format the data, as described in [Exporting access logs to a CSV file](https://developer.zendesk.com/documentation/ticketing/using-the-zendesk-api/exporting-access-logs/). |
| Advanced data retention policies | Plan type | Suite Enterprise and above  Support Enterprise and above  (Legacy plans are not eligible) |
| Permissions | Admins and [agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) |
| Data masking | Plan type | Suite Enterprise and above  Support Enterprise and above  (Legacy plans are not eligible) |
| Permissions | Admins |
| Advanced encryption | Plan type | Suite Enterprise and above  Support Enterprise and above  (Legacy plans are not eligible) |
| Permissions | Admins |
| Redaction suggestions | Plan type | Suite Enterprise and above Support Enterprise and above (Legacy plans are not eligible) |
| Permissions | Admins and [agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) with the Redact ticket content permission |
| Automatic redaction | Plan type | Suite Enterprise and above Support Enterprise and above (Legacy plans are not eligible) |
| Permissions | Admins and [agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) with permissions to manage triggers. |
| Automatic phone call transcription redaction | Plan type | Suite Enterprise and above Support Enterprise and above (Legacy plans are not eligible) |
| Permissions | Admins and team leads of Talk can turn on transcription redaction in the Settings page in Admin Center |

## How do I get it?

To get started with the Advanced Data Privacy and Protection add-on, see [Buying the Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6119316155930)
or contact your Zendesk account representative.

## Where can I learn more?

To learn more about the features available with the Advanced Data Privacy and
Protection add-on, see:

- [Using the access log to monitor agent activity](https://support.zendesk.com/hc/en-us/articles/6066010357530)
- [Creating ticket deletion
  schedules](https://support.zendesk.com/hc/en-us/articles/6388012977306)
- [Creating end-user deletion
  schedules](https://support.zendesk.com/hc/en-us/articles/6062884435866)
- [Automatically detecting sensitive
  information for redaction](https://support.zendesk.com/hc/en-us/articles/6669399593882)
- [Automatically redacting sensitive information in tickets using triggers](https://support.zendesk.com/hc/en-us/articles/9248330321050)
- [Zendesk call transcription and
  summarization FAQ](https://support.zendesk.com/hc/en-us/articles/7470764710298)

See [Advanced Data Privacy and Protection](https://www.zendesk.com/customer-data-privacy-protection/) on
the Zendesk website for more planned features.