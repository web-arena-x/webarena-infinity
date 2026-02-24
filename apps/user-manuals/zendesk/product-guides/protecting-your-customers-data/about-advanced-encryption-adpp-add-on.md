# About advanced encryption (ADPP add-on)

Source: https://support.zendesk.com/hc/en-us/articles/5043582015898-About-advanced-encryption-ADPP-add-on

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Advanced Data Privacy and Protection (ADPP) |

Verified AI summary ◀▼

The Advanced Encryption feature, part of the ADPP add-on, lets you secure data using your own Key Management Service (KMS). It encrypts sensitive data, ensuring control over access and compliance. While it supports various KMS providers and encrypts key user data fields, be aware of limitations like unsupported key rotation and potential feature degradation. Test in a sandbox environment before full implementation.

Location: Admin Center > Account > Security > Advanced encryption

The Advanced encryption feature, part of the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), enhances data security by allowing your company to encrypt service data using your own enterprise Key Management Service (KMS). This ensures that sensitive information stored in Zendesk remains secure and inaccessible to unauthorized parties. Maintaining your own encryption keys provides greater security and compliance while giving you complete control over access and usage.

You can turn on advanced encryption in your production or sandbox account. Zendesk recommends testing it on sandbox first. See [Setting up advanced encryption](https://support.zendesk.com/hc/en-us/articles/5517626234138) to learn more.

This article covers the following topics:

- [Understanding how advanced encryption works](#topic_ghv_224_b2c)
- [Data encrypted in Zendesk](#topic_tm1_1f4_b2c)
- [Advanced encryption vs. standard encryption](#topic_wbf_bf4_b2c)
- [Advanced encryption limitations](#topic_hc5_cf4_b2c)
- [Data storage limitations](#topic_i1q_st4_b2c)

## Understanding how advanced encryption works

When using advanced encryption, you manage your own encryption keys outside of Zendesk. You can use any of the following supported Key Management Systems: AWS KMS, Azure Key Vault, Google Cloud KMS, or Thales CipherTrust Manager, which is an EU-based KMS based in Europe and managed and hosted by European companies.

Advanced encryption relies on envelope encryption. On encryption, Zendesk generates a Data Encryption Key (DEK) for the data chunk and requests the KMS to encrypt this key. It then discards the plain key and keeps the encrypted key.

Whenever Zendesk needs to access encrypted data, it will request the KMS to decrypt the data key using the master key. This happens in transit; data is encrypted when it comes into Zendesk before our applications process it, and it stays encrypted until there's a use case that requires decryption.

Data encryption doesn't impact the agent experience. Agents can continue to search and access the data they are permitted to see based on their role. However, there are a few [limitations](#topic_hc5_cf4_b2c).

## Data encrypted in Zendesk

Advanced encryption supports backfilling and encrypting newly created and existing users in your Zendesk account.

Key rotation and revocation are not yet supported. If you rotate or revoke the keys, you might lose your encrypted data forever. You can add a new key, which will be used to encrypt newly created data.
The old keys will continue to encrypt and decrypt the old data.

Advanced encryption encrypts the following user fields and entities for end-user data in Support and the knowledge and voice areas of Zendesk:

- Name
- Alias
- Signature
- Details
- Notes
- Email address
- Social channel [user identities](https://developer.zendesk.com/api-reference/ticketing/users/user_identities/)

The fields listed above are encrypted in the following areas of Zendesk Support:

- End-user management
- Team-member management
- User data in the context of a ticket (requester, CC, followers, assignee)
- Group and organization memberships
- User placeholder resolution in ticket comments and emails
- User creation through single sign-on, Web Widget, and email
- Ticket views
- Support search
- Triggers and automations (business rules)
- Support users created through messaging conversations
- Side conversations

All knowledge- and voice-related features are covered, except @mentions in help center, which will be turned off if encryption is activated.

## Advanced encryption vs. standard encryption

Advanced encryption complements standard encryption used by all Zendesk accounts.

| State | Advanced encryption | Standard encryption |
| --- | --- | --- |
| **In transit** | Data is encrypted with customer-managed keys as soon as possible at the HTTP proxy layer or equivalent entry point. | All communications with the Zendesk UI and APIs are encrypted through industry standard HTTPS and Transport Layer Security (TLS 1.2 or higher) over public networks. This ensures that all traffic between you and Zendesk is secure during transit. For email, Zendesk leverages opportunistic TLS by default. TLS encrypts and delivers email securely, mitigating eavesdropping between mail servers where peer services support this protocol. Exceptions for encryption may include any use of in-product SMS functionality, any other third-party app, integration, or service subscribers that customers may choose to leverage at their discretion. |
| **At rest** | Data in the database remains encrypted. If a third party or foreign government attempts to get access to a running database, the data will be returned in ciphertext. | Service Data is encrypted at rest in AWS using AES-256 key encryption. |
| **In use** | The data remains encrypted while in use and is only decrypted if a use case requires it. Any decryption actions are logged and auditable when leveraging an external Security Information and Event Management (SIEM) integration. | Data fetched from the data stores is processed in plaintext. |

## Advanced encryption limitations

Advanced encryption comes with some trade-offs that you should be aware of. When data is encrypted, you may encounter functionality limitations and unavailable features.

**General limitations**

- Any functionality outside of the scope described in [Data encrypted in Zendesk](#topic_tm1_1f4_b2c), including but not limited to legacy Chat, QA, integrations, and mobile, might be broken or show encrypted data in the UI or API responses. For these reasons, Zendesk encourages you to activate and test advanced encryption in a sandbox account before activating it in production.
- Key rotation is not yet supported.

**Support limitations**

- Ticket sharing is not yet supported.
- Encrypted accounts will become ineligible for account region moves. If you wish to move your data to a different region, request the move before activating advanced encryption.
- [Sandbox environments](https://support.zendesk.com/hc/en-us/articles/6150628316058) can't be created after activating advanced encryption.
- Messaging triggers with conditions based on an end-user name won’t work.
- Only email addresses are encrypted. Email HTML source files, as well as the subject line email body, are not encrypted.

**Search-related degradation**

- Snippet highlighting, wildcard search, phrase search, and non-space delimited languages (such as Chinese and Japanese) won’t work.
- Search match and ranking might be different.
- Searching for side conversations by user name won’t work. Instead, search by the subject line of the side conversation or parent ticket.

**Views-related degradation**

- Support views sorting by user name (requester and assignee) will be turned off for accounts with encryption activated.
- Support views grouped by user name (requester and assignee) will display user names that are out of order.
- CSV exports will display placeholders instead of user names.

**Imports and exports degradation**

- User fields and identities imported through the [bulk actions importer](https://support.zendesk.com/hc/en-us/articles/4408893496218#topic_nly_lm1_5cc) will not be encrypted. User fields added through the [data importer](https://support.zendesk.com/hc/en-us/articles/4408893496218#topic_syb_lm1_5cc) will be encrypted, but user identities added through the data importer will not be encrypted.
- XML exports for users will not be supported, but CSV and JSON exports are supported.

**Help center degradation**

- @mentions will be turned off.

## Data storage limitations

Advanced encryption introduces a new way of encrypting sensitive data using Customer Managed Keys (CMK). To ensure Zendesk’s functionality is not compromised, Zendesk services decrypt sensitive data while processing requests originating from many channels, including browsers, REST APIs, and email. Zendesk guarantees that plaintext data is never stored in permanent storage and is only kept for the minimum amount of time necessary to fulfill the request.

The following items are current exceptions:

- Gateway (NGINX + Cloudflare) stores public help center pages, which might contain user profile data for up to three minutes.
- Outbound email temporarily stores email bodies before the email is delivered by Simple Mail Transfer Protocol (SMTP).
- The [original email body](https://support.zendesk.com/hc/en-us/articles/4408832876442) of inbound email is maintained after the ticket or comment is created and powers additional collaboration features.
- Explore user datasets are stored in plaintext.
- Bulk import and export files are temporarily stored in plaintext for 30 days.
 The files are deleted after 30 days.
- User data in Sunshine Conversations datastores is stored in plaintext. (Support datastores are covered.)
- User data in real-time services (for example, agent presence and the call console) is retained in plaintext for up to seven days to power the agent UI.
- Agent and admin user data will appear in plaintext for customer sales and support cases to assist customers.