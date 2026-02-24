# Complying with Privacy and Data Protection Law in Zendesk Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408883081242-Complying-with-Privacy-and-Data-Protection-Law-in-Zendesk-Sell

---

This article describes how certain features and functionality in Zendesk Sell can assist with your obligations under privacy law.

To learn more about meeting your obligations in other Zendesk products, see [Complying with Privacy and Data Protection Law in Zendesk products](https://support.zendesk.com/hc/en-us/articles/4408834005530).

Topics covered in this article:

- [Meeting an access obligation](#topic_qdm_yhk_gs)
- [Meeting a correction obligation](#topic_ezm_pcv_4v)
- [Meeting an erasure or deletion obligation](#topic_p3p_zhk_gs)
- [Meeting a data portability obligation](#topic_ekz_13k_gs)
- [Meeting an objection obligation](#topic_gcn_swl_ycb)
- [Disclaimer](#topic_mvj_lyf_gdb)

## Meeting an access obligation

Individuals from certain regions have a *right of access*. On request, you may have an obligation to inform a user where their personal data is being held and for what purposes.

Sell provides a platform for businesses to collect information on contacts and leads, for example, through calls, notes, text messages, documents, and tasks, that they can analyze to help sell their products to new and existing clients.

If an individual requests a copy of their personal data, you can export the data from Sell as described in [Meeting a data portability obligation](gdpr_guide.html#topic_ekz_13k_gs).

## Meeting a correction obligation

Individuals from certain regions have a *right to rectification*, or the right to have inaccuracies in their personal data corrected. On request, you may have an obligation to provide the individual with their personal data and fix inaccuracies or add missing information.

To meet the correction obligation Sell allows you to export the existing information and edit the personal data with the necessary fixes. To apply fixes to the user data, follow the steps described in [Editing lead, contact, and deal data using Table view](https://support.zendesk.com/hc/en-us/articles/4408822104858).

To export user data, follow the steps described in [Exporting data from Sell](https://support.zendesk.com/hc/en-us/articles/4408828443674), and extract the information pertaining to the individual, or use the Sell [Contacts API](https://developers.getbase.com/docs/rest/reference/contacts) or Sell [Leads API](https://developers.getbase.com/docs/rest/reference/leads) to extract details for an individual.

## Meeting an erasure or deletion obligation

Individuals from certain regions have a *right to erasure*, or the right to be forgotten or deleted. On request, you may have an obligation to delete the personal data of an individual.

To delete an active user’s data, follow the steps described in [Deleting a contact,](https://support.zendesk.com/hc/en-us/articles/4408832226842)
and raise a [support ticket](https://support.getbase.com/hc/en-us/requests/new) to have the user’s data removed permanently from the database.

## Meeting a data portability obligation

Individuals from certain regions have a *right to data portability*. On request, you may have an obligation to provide an individual with their personal data or to transmit the data to another organization.

The Sell API provides the capability to export an individual’s data in a commonly used machine readable format (JSON), which can then be imported into another system. Use the Sell API to export account data for an individual (a [contact](https://developers.getbase.com/docs/rest/reference/contacts) or [lead](https://developers.getbase.com/docs/rest/reference/leads)), including any [calls](https://developers.getbase.com/docs/rest/reference/calls), [documents](https://developers.getbase.com/docs/rest/reference/documents), [notes](https://developers.getbase.com/docs/rest/reference/notes), [tasks](https://developers.getbase.com/docs/rest/reference/tasks), or [text messages](https://developers.getbase.com/docs/rest/reference/text_messages)
associated with the individual.

Additionally, use [Smart Lists](https://support.zendesk.com/hc/en-us/articles/4408827735066) to export data about a specific person.

Integration data that is present in Sell, including email, calendar entries, and data associated with any other third party integrations, cannot be exported through Sell as this data is owned by the integration provider. Your data controller needs to contact your integration provider to export this data at source.

## Meeting an objection obligation

Individuals from certain regions have a *right of objection*, or the right to object to direct marketing. You may have an obligation to stop processing personal data for direct marketing purposes when you receive an objection from an individual.

Sell does not actively offer direct marketing as a feature, therefore it is up to the business to be aware of how the end user information is being used. With that, if the business wishes to meet this objection obligation within the platform, Sell allows you to [delete user details](https://support.getbase.com/hc/en-us/articles/203478509-Deleting-a-Contact).

See [Meeting an erasure or deletion obligation](#topic_p3p_zhk_gs) for more detail.

## Disclaimer

This document is for informational purposes only and does not constitute legal advice. Readers should always seek legal advice before taking any action with respect to the matters discussed herein.