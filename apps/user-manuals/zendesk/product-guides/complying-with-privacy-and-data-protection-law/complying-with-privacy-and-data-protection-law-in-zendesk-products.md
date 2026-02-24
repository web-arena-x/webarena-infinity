# Complying with Privacy and Data Protection Law in Zendesk products

Source: https://support.zendesk.com/hc/en-us/articles/4408834005530-Complying-with-Privacy-and-Data-Protection-Law-in-Zendesk-products

---

This guide describes how certain features and functionality in Zendesk products can assist with your obligations under privacy law, for example, as a *data controller* under the General Data Protection Regulation (GDPR), or as a *business* under the California Consumer Privacy Act (CCPA). Zendesk is considered a third-party *data processor* under the GDPR, and a *service provider* under the CCPA, because it handles the personal data or personal information of its customers' end users on behalf of its customers (or subscribers).

Data controllers and businesses bear the primary responsibility for ensuring that their processing of personal data is compliant with relevant data protection law.

See the following articles in this guide:

- [Complying with Privacy and Data Protection Law in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408823195930)
- [Complying with Privacy and Data Protection Law in Zendesk Insights](https://support.zendesk.com/hc/en-us/articles/4408822109978)
- [Complying with Privacy and Data Protection Law in Zendesk Guide](https://support.zendesk.com/hc/en-us/articles/4408821644186)
- [Complying with Privacy and Data Protection Law in Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/4409148563098)
- [Complying with Privacy and Data Protection Law in standalone Chat accounts](https://support.zendesk.com/hc/en-us/articles/4409155522330)
- [Complying with Privacy and Data Protection Law in Zendesk Contact Center](https://support.zendesk.com/hc/en-us/articles/9878768380698)
- [Complying with Privacy and Data Protection Law in Zendesk Talk](https://support.zendesk.com/hc/en-us/articles/4408821829402)
- [Complying with Privacy and Data Protection Law in Zendesk Explore](https://support.zendesk.com/hc/en-us/articles/4409148577178)
- [Complying with Privacy and Data Protection Law in Zendesk Bime](https://support.zendesk.com/hc/en-us/articles/4409155627290)
- [Complying with Privacy and Data Protection Law in Zendesk Sell](https://support.zendesk.com/hc/en-us/articles/4408883081242)
- [Complying with Privacy and Data Protection Law in Zendesk Sunshine](https://support.zendesk.com/hc/en-us/articles/4409155569562)
- [Complying with Privacy and Data Protection Law in Zendesk Sunshine Conversations](https://support.zendesk.com/hc/en-us/articles/4409155590810)
- [Complying with Privacy and Data Protection Law in Zendesk WFM (Tymeshift)](https://support.zendesk.com/hc/en-us/articles/6636665226266)
- [Complying with Privacy and Data Protection Law in Zendesk QA (Klaus)](https://support.zendesk.com/hc/en-us/articles/7161366151194)
- [Complying with Privacy and Data Protection Law in AI agents - Advanced (Ultimate)](https://support.zendesk.com/hc/en-us/articles/7412310217370)

For instructions on deleting a user's personal data in Zendesk products, see [Forgetting a user in Zendesk](https://support.zendesk.com/hc/en-us/articles/4408845703194).

For more information on privacy law and Zendesk, see our [Privacy and Data Protection](https://www.zendesk.com/company/privacy-and-data-protection/)
website.

For instructions on providing legal notices, see [How to Provide Legal Notices to End-Users Using Zendesk.](how-to-provide-legal-notices-and-obtain-consent-in-zendesk.md)

## What is personal data

Personal data, or personal information, is any data that can be used to identify an individual.
Examples include an email address, a phone number, or a social security number.
Personal data may also include any data that could be used indirectly to identify an individual. For example, a person's nickname such as "Gerry" may not be personal data because many people may have the same nickname. However, if the nickname can be combined with other data such as a work address, the nickname could be considered personal data because it helps identify the individual.

Your organization needs to decide what personal data is. Is it simply an email address or phone number, or do you further disambiguate using a combination of identities or attributes? This decision is up to you.

If you’re unsure whether or not a piece of information is personal data, it’s best to err on the side of caution. Another option is to seek legal advice.

## Common terms

The following terms are sometimes used in this document:

**Soft delete**

*Soft deleting* an item deletes the item such that it is not visible to any users, including admins using either the product interface or the API. The item is still in the Zendesk database and accessible by Zendesk on a limited basis only to its employees with certain database privileges. Soft deleted tickets are automatically permanently deleted after 30 days.

**Hard delete, permanently delete, scrub**

*Hard deleting* or *scrubbing* an item permanently deletes the item. The item is completely removed from the Zendesk database. No one, including Zendesk employees with database privileges, can access the item any longer.