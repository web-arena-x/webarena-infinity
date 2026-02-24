# Complying with Privacy and Data Protection Law in Zendesk Sunshine 

Source: https://support.zendesk.com/hc/en-us/articles/4409155569562-Complying-with-Privacy-and-Data-Protection-Law-in-Zendesk-Sunshine

---

This guide describes how certain features and functionality in Zendesk Sunshine can
assist with your obligations under privacy law. Zendesk Sunshine includes profiles, events,
custom objects, and the Sunshine UI.

To learn more about meeting your obligations in other Zendesk products, see [Complying with Privacy and Data Protection Law in Zendesk
products](https://support.zendesk.com/hc/en-us/articles/4408834005530).

In this guide, users can be End-Users or Agents as the terms are defined in the [Zendesk Customer Agreement](https://www.zendesk.com/company/agreements-and-terms/zendesk-customer-agreement/).

Topics covered in this article:

- [Meeting an access obligation](#topic_pqm_544_5jb)
- [Meeting a correction obligation](#topic_iny_gp4_5jb)
- [Meeting an erasure obligation](#topic_fgb_br4_5jb)
- [Meeting a data portability obligation](#topic_rlh_gr4_5jb)
- [Meeting an objection obligation](#topic_bq4_ks4_5jb)
- [Disclaimer](#topic_ihs_syf_gdb)

## Meeting an access obligation

Individuals from certain regions have a *right of access*. On request, you
may have an obligation to inform an end user or agent where their personal data is being
held and for what purposes.

Sunshine profiles, events, and custom objects authenticates callers to its API
using either basic authentication with your email address and password, with your email
address and an API token, or with an OAuth access token.

Access to Sunshine profiles and events data using APIs can be limited to access
to a single business account.

With respect to audits and logs, all generated logs are transferred and stored in
a secured and encrypted location. In the event of suspected or confirmed unauthorized data
access, Sunshine profiles, events, and custom objects can provide audit logs to help you
investigate, respond to, and remediate the issue.

To export the data from profiles and events, please follow the steps described in [Meeting a data portability obligation](#topic_rlh_gr4_5jb).

## Meeting a correction obligation

Individuals from certain regions have a right to rectification, or the right to
have inaccuracies in their personal data corrected. On request, you may have an obligation
to provide the individual with their personal data and fix inaccuracies or add missing
information.

To meet a correction obligation:

- Sunshine profiles allows you to delete the existing information and re-create
  the personal data with the necessary fixes, or [update or partially update an existing profile](https://developer.zendesk.com/rest_api/docs/sunshine/profiles_ap)
- Custom objects allows you to delete the existing information and re-create
  the personal data with the necessary fixes, [update an existing object type](https://developer.zendesk.com/rest_api/docs/sunshine/resource_types#update-object-type), or [update an existing object record](https://developer.zendesk.com/rest_api/docs/sunshine/resources#update-object-record)
- The Sunshine UI in the Admin Center allows you to [delete an existing object type or relationship
  type](https://support.zendesk.com/hc/en-us/articles/4408834725402#topic_gqp_yk5_dlb). You can then re-create the object type or relationship type.

See [Meeting an erasure obligation](#topic_fgb_br4_5jb) for more detail.

## Meeting an erasure obligation

Individuals from certain regions have a right to erasure, or the right to be
forgotten or deleted. On request, you may have an obligation to delete the personal data of
an individual.

Using the Sunshine Profiles API, you can [delete a profile](https://developer.zendesk.com/rest_api/docs/sunshine/profiles_api#delete-profile-by-profile-id) to delete a customer’s details and
all events associated with the profile.

Using Custom Objects API, you can [delete an object type](https://developer.zendesk.com/rest_api/docs/sunshine/resource_types#delete-object-type), [delete an object record](https://developer.zendesk.com/rest_api/docs/sunshine/resources#delete-object-record), [delete a relationship type](https://developer.zendesk.com/rest_api/docs/sunshine/relationship_types), [delete a relationship record](https://developer.zendesk.com/rest_api/docs/sunshine/relationships#delete-relationship-record). You can also run [custom object jobs](https://developer.zendesk.com/rest_api/docs/sunshine/jobs#jobs-to-delete-object-records-or-relationship-records) to batch delete object records
and relationship records.

## Meeting a data portability obligation

Individuals from certain regions have a right to data portability. On request,
you may have an obligation to provide an individual with their personal data or to transmit
the data to another organization.

Businesses can export data about users including metadata to another system as
required by privacy and data protection law. The feature exports data in a commonly used
machine readable format (JSON), which can then be imported into another system. The [Get profile by identifier API](https://developer.zendesk.com/rest_api/docs/sunshine/profiles_api#get-profile-by-identifier) and [Get profile by profile ID API](https://developer.zendesk.com/rest_api/docs/sunshine/profiles_api#get-profile-by-profile-id) allows you to retrieve
all of the personal data stored on a user.

The [Get events by Sunshine profile API](https://developer.zendesk.com/rest_api/docs/sunshine/events_api#get-events-by-user-profile) and [Get events by Sunshine profile ID API](https://developer.zendesk.com/rest_api/docs/sunshine/events_api#get-events-by-user-profile-id) retrieves all
the events associated with a user.

## Meeting an objection obligation

Individuals from certain regions have a right of objection, or the right to
object to direct marketing. You may have an obligation to stop processing personal data for
direct marketing purposes when you receive an objection from an individual.

Since Sunshine profiles, events, custom objects, and the Sunshine UI do not actively offer
direct marketing as a feature, it's up to the business to be aware of how the end user
information is being used. With that, if the business wishes to meet this objection
obligation within the platform, Sunshine profiles, events, and custom objects allows you to
delete the existing information and re-create the personal data with the necessary fixes.
See [Meeting an erasure obligation](#topic_fgb_br4_5jb) for more detail.

## Disclaimer

This document is for informational purposes only and does not constitute legal advice.
Readers should always seek legal advice before taking any action with respect to the matters
discussed herein.