# Complying with Privacy and Data Protection Law in Zendesk Sunshine Conversations

Source: https://support.zendesk.com/hc/en-us/articles/4409155590810-Complying-with-Privacy-and-Data-Protection-Law-in-Zendesk-Sunshine-Conversations

---

This guide describes how certain features and functionality in Zendesk Sunshine Conversations can assist with your obligations under privacy law.

To learn about meeting your obligations in other Zendesk products, see [Complying with Privacy and Data Protection Law in Zendesk products](https://support.zendesk.com/hc/en-us/articles/4408834005530).

Topics covered in this article:

- [Meeting an access obligation](#topic_pqm_544_5jb)
- [Meeting a correction obligation](#topic_iny_gp4_5jb)
- [Meeting an erasure obligation](#topic_fgb_br4_5jb)
- [Meeting a data portability obligation](#topic_rlh_gr4_5jb)
- [Meeting an objection obligation](#topic_bq4_ks4_5jb)
- [Disclaimer](#topic_ihs_syf_gdb)

## Meeting an access obligation

Individuals from certain regions have a *right of access*. On request, you may have an obligation to inform an end user or agent where their personal data is being held and for what purposes.

Sunshine Conversations authenticates callers to its API using JSON Web Tokens (JWTs) that allow access to be scoped to several different levels and can be set to expire at a specific date and time. Access to Sunshine Conversations data through JWTs can be limited to access to an individual user's conversation history and metadata, access to a single business account (app) and all of the user data contained within it, access to a group of business accounts (such as parent company and divisions) as well as global access for all business accounts provisioned on the software provider’s system.

With respect to audits and logs, all generated logs are transferred and stored in a secured and encrypted location. In the event of suspected or confirmed unauthorized data access, Sunshine Conversations can provide audit logs to help you investigate, respond to, and remediate the issue.

To export the data from Sunshine Conversations, please follow the steps described in [Meeting a data portability obligation](#topic_rlh_gr4_5jb).

## Meeting a correction obligation

Individuals from certain regions have a *right to rectification*, or the right to have inaccuracies in their personal data corrected. On request, you may have an obligation to provide the individual with their personal data and fix inaccuracies or add missing information.

To meet a correction obligation, Sunshine Conversations allows you to delete the existing information and re-create the personal data with the necessary fixes.

See [Meeting an erasure obligation](#topic_fgb_br4_5jb) for more detail.

## Meeting an erasure obligation

Individuals from certain regions have a *right to erasure*, or the right to be forgotten or deleted. On request, you may have an obligation to delete the personal data of an individual.

To delete a user's personal data, Sunshine Conversations gives you full control over app, user, and message deletion. You can easily [delete a single user profile](https://docs.smooch.io/rest/#delete-app-user-profile) along with the [conversation history](https://docs.smooch.io/rest/#delete-all-messages) attached to it. You can also [delete single messages](https://docs.smooch.io/rest/#delete-single-message). Sunshine Conversations also supports [deleting an app](https://docs.smooch.io/rest/#delete-app). This means you can delete a customer (a business) and immediately delete all associated data of the users of that business.

## Meeting a data portability obligation

Individuals from certain regions have a *right to data portability*. On request, you may have an obligation to provide an individual with their personal data or to transmit the data to another organization.

Businesses can easily export data about users, including metadata and conversation history, to another system as required by privacy and data protection law. The feature exports data in a commonly used machine readable format (JSON), which can then be imported into another system. The [Get App User API](https://docs.smooch.io/rest/#get-app-user) allows you to retrieve all of the metadata (including channel-specific metadata) Sunshine Conversations stores on a user. The [Get Messages API](https://docs.smooch.io/rest/#get-messages) retrieves all the messages exchanged between your software and a user, across any channel the user has used to communicate. If your software takes advantage of Sunshine Conversations’s built-in business system integrations, you can use the [Get App User Business System IDs](https://docs.smooch.io/rest/#get-app-user-business-system-ids) to find the business system entity (such as a ticket ID or Slack channel) associated with the user.

## Meeting an objection obligation

Individuals from certain regions have a *right of objection*, or the right to object to direct marketing. You may have an obligation to stop processing personal data for direct marketing purposes when you receive an objection from an individual.

Since Sunshine Conversations as a platform does not actively offer direct marketing as a feature, it's up to the business to be aware of how the end user information is being used. With that, if the business wishes to meet this objection obligation within the platform, Sunshine Conversations allows you to delete the existing information and re-create the personal data with the necessary fixes. See [Meeting an erasure obligation](#topic_fgb_br4_5jb) for more detail.

## Disclaimer

This document is for informational purposes only and does not constitute legal advice. Readers should always seek legal advice before taking any action with respect to the matters discussed herein.