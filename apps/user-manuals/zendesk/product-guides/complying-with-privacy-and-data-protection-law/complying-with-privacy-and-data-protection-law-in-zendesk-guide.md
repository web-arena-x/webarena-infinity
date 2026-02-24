# Complying with Privacy and Data Protection Law in Zendesk Guide

Source: https://support.zendesk.com/hc/en-us/articles/4408821644186-Complying-with-Privacy-and-Data-Protection-Law-in-Zendesk-Guide

---

This guide describes how certain features and functionality in Zendesk Guide can assist with your obligations under privacy law.

To learn more about meeting your obligations in other Zendesk products, see [Complying with Privacy and Data Protection Law in Zendesk products](https://support.zendesk.com/hc/en-us/articles/4408834005530).

In this guide, *users* can be End-Users or Agents as the terms are defined in the [Zendesk Customer Agreement](https://www.zendesk.com/company/agreements-and-terms/zendesk-customer-agreement/).

Knowledge users are managed in Zendesk Support.

Topics covered in this article:

- [Meeting an access obligation](#topic_qdm_yhk_gs)
- [Meeting a correction obligation](#topic_ezm_pcv_4v)
- [Meeting an erasure or deletion obligation](#topic_p3p_zhk_gs)
- [Meeting a data portability obligation](#topic_ekz_13k_gs)
- [Meeting an objection obligation](#topic_gcn_swl_ycb)
- [Disclaimer](#topic_mvj_lyf_gdb)

## Meeting an access obligation

Individuals from certain regions have a *right of access*. On request, you may have an obligation to inform an end user or agent where their personal data is being held and for what purposes.

If a user requests their personal data, you can export the data from Zendesk as described in [Meeting a data portability obligation](https://support.zendesk.com/hc/en-us/articles/4408823195930#topic_ekz_13k_gs) in the article for Zendesk Support.

## Meeting a correction obligation

Individuals from certain regions have a *right to rectification*, or the right to have inaccuracies in their personal data corrected. On request, you may have an obligation to provide the individual with their personal data and fix inaccuracies or add missing information.

See [Meeting a correction obligation](https://support.zendesk.com/hc/en-us/articles/4408823195930#topic_ezm_pcv_4v) in the article for Zendesk Support.

## Meeting an erasure or deletion obligation

Individuals from certain regions have a *right to erasure*, or the right to be forgotten or deleted. On request, you may have an obligation to delete the personal data of an individual.

See [Meeting an erasure or deletion obligation](https://support.zendesk.com/hc/en-us/articles/4408823195930#topic_p3p_zhk_gs) in the article for Zendesk Support.

Personal data may also be contained in Help Center articles, community posts, and comments. See the following topics:

- [Deleting personal data in content](#topic_fhk_pgt_ycb)
- [Searching and deleting personal data with the API](#topic_dyv_5c2_1db)

Article comments, community posts, and community comments are soft deleted. The inline images won't be accessible through the URL.

### Deleting personal data in content

You can remove personal data that appears in knowledge base articles, community posts, and comments, or delete the content item itself. Knowledge admins can edit or delete any item. Authors can edit or delete any item they created themselves, including articles, posts, and comments.

#### Knowledge base articles

Do one of the following to remove personal data from an article:

- Edit the article to remove the personal data.
 See [Editing articles in the knowledge base](https://support.zendesk.com/hc/en-us/articles/4408839258778#topic_1rt_tdq_cy).

 The data is deleted from the knowledge base but is maintained in the system to show [article revisions and history](https://support.zendesk.com/hc/en-us/articles/4408829321498) on the Zendesk Suite Growth plan or above and the Guide Professional or Enterprise plan.
- Archive the article. See [Archiving an article to remove it from your knowledge base](https://support.zendesk.com/hc/en-us/articles/4408838947738).

 The article is removed from the knowledge base, along with any attachments and translations associated with it, and added to a deleted articles list. Knowledge admins can view and restore articles in the list. Articles can't be deleted from the list.
- Delete the article. See [Deleting an article from your knowledge base](https://support.zendesk.com/hc/en-us/articles/4408832480154).

 The article is soft deleted from the knowledge base, making it unavailable for everyone including Knowledge admins in the UI or the API. The article will still be in the Zendesk database and accessible on a limited basis to employees with certain database privileges. Soft deleting the article will also soft delete any inline and block attachments..
- Delete an attachment from the article. See [Creating and editing articles in the knowledge base](https://support.zendesk.com/hc/en-us/articles/4408839258778).

 The attachment is removed from the article and is no longer available to anyone including Knowledge admins. However, due to caching, the attachment might still be visible for up to seven days after it is deleted.

#### Community posts

Edit or delete the community post to remove the personal data.

Deleting the post soft deletes it, meaning it's no longer accessible by anybody, including admins, in the Knowledge admin interface. Any comments and inline attachments associated with the post are soft deleted too. The attachments will no longer be accessible through the URL.

See [Editing and deleting community posts and comments](https://support.zendesk.com/hc/en-us/articles/4408823846170#topic_gzn_4hf_4k).

#### Article and post comments

Edit or delete the comment to remove the personal data.

Deleting a comment soft deletes it, meaning it's no longer accessible by anybody, including admins, in the Knowledge admin interface. Any inline attachments associated with the comment are soft deleted too. The attachments will no longer be accessible through the URL.

### Searching and deleting personal data with the API

You can use the [Help Center API](https://developer.zendesk.com/rest_api/docs/help_center/introduction) to find and remove content that contains a user's personal data.

**To search for personal data in articles**

- `GET /api/v2/help_center/articles/search.json?query={search_string}`

See [Search Articles](https://developer.zendesk.com/rest_api/docs/help_center/search#search-articles).

**To archive an article**

- `DELETE /api/v2/help_center/articles/{id}.json`

Note: Archived articles are still visible in the Knowledge admin interface. You can use the interface to soft delete articles archived with the API. A soft deleted article will still be in the Zendesk database and accessible on a limited basis to employees with certain database privileges. Soft deleting the article will also soft delete any inline and block attachments.

**To delete a community post**

- `DELETE /api/v2/community/posts/{post_id}.json`

See [Delete Post](https://developer.zendesk.com/rest_api/docs/help_center/posts#delete-post).

**To delete a comment**

- `DELETE /api/v2/help_center/articles/{id}/comments/{comment_id}.json`
- `DELETE /api/v2/community/posts/{post_id}/comments/{comment_id}.json`

See [Delete Article Comment](https://developer.zendesk.com/rest_api/docs/help_center/comments#delete-comment) and [Delete Post Comment](https://developer.zendesk.com/rest_api/docs/help_center/post_comments#delete-comment).

**To delete an article attachment**

- `DELETE /api/v2/help_center/articles/attachments/{attachment_id}.json`

See [Delete Article Attachment](https://developer.zendesk.com/rest_api/docs/help_center/article_attachments#delete-article-attachment).

## Meeting a data portability obligation

Individuals from certain regions have a *right to data portability*. On request, you may have an obligation to provide an individual with their personal data or to transmit the data to another organization.

To export an agent's or end user's personal data, see [Meeting a data portability obligation](https://support.zendesk.com/hc/en-us/articles/4408823195930#topic_ekz_13k_gs) in the article for Zendesk Support.

If an agent or user requests that everything be exported, you can export what the person posted or commented on in Help Center using the API.

**To get all articles for a user**

- GET /api/v2/help\_center/users/{id}/articles.json

See [List Articles](https://developer.zendesk.com/rest_api/docs/help_center/articles#list-articles).

**To get all article comments for a user**

- `GET /api/v2/help_center/users/{user_id}/comments.json`

See [List Comments](https://developer.zendesk.com/rest_api/docs/help_center/comments#list-comments).

**To get all community posts for a user**

- `GET /api/v2/community/users/{user_id}/posts.json`

See [List Posts](https://developer.zendesk.com/rest_api/docs/help_center/posts#list-posts).

**To get all community comments for a user**

- `GET /api/v2/community/users/{user_id}/comments.json`

See [List Post Comments](https://developer.zendesk.com/rest_api/docs/help_center/post_comments#list-comments).

## Meeting an objection obligation

Individuals from certain regions have a *right of objection*, or the right to object to direct marketing. You may have an obligation to stop processing personal data for direct marketing purposes when you receive an objection from an individual.

## Disclaimer

This document is for informational purposes only and does not constitute legal advice. Readers should always seek legal advice before taking any action with respect to the matters discussed herein.