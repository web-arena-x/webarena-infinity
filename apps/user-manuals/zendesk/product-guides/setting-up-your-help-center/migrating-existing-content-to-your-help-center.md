# Migrating existing content to your help center

Source: https://support.zendesk.com/hc/en-us/articles/4408828053146-Migrating-existing-content-to-your-help-center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

There are many ways to migrate content from one help center to another. This article primarily focuses on using your help center API to programmatically import content, and gives a high-level overview of the process of migrating existing content to your new help center. You can also migrate content using the following approaches:

- **Copying and pasting**: If you are only migrating a few articles, then the fastest and easiest way is to simply copy and paste content from your previous help center into a new article.
- **Professional services**: If you have large or complex migrations, you can [hire Zendesk to help](https://www.zendesk.com/customer-experience/professional-services/) you with your migration.
- **Partner apps**: You can explore the Zendesk [apps marketplace](https://www.zendesk.com/apps/) to find partner apps such as [Help Desk Migration](https://www.zendesk.com/apps/support/help-desk-migration/).

This article covers the following topics:

- [Migrating content to your knowledge base](#topic_rtq_kdh_bpb)
 - [Importing your authors as Zendesk users](#topic_rtq_kdh_bpb__section_gzl_t2h_bpb)
 - [Creating categories in your knowledge base](#topic_rtq_kdh_bpb__section_wfq_s2h_bpb)
 - [Creating user segments (optional)](#topic_rtq_kdh_bpb__section_gtz_r2h_bpb)
 - [Creating sections in your categories](#topic_rtq_kdh_bpb__section_cxv_r2h_bpb)
 - [Creating articles in your sections](#topic_rtq_kdh_bpb__section_t5q_r2h_bpb)
 - [Uploading attachments (if necessary)](#topic_rtq_kdh_bpb__section_hzl_r2h_bpb)
 - [Importing article comments](#topic_rtq_kdh_bpb__section_wbh_r2h_bpb)
- [Migrating content to your community](#topic_uvz_kdh_bpb)
 - [Creating user segments (optional)](#topic_rtq_kdh_bpb__section_gtz_r2h_bpb)
 - [Importing topics in your community](#topic_uvz_kdh_bpb__section_pwh_tdh_bpb)
 - [Importing posts in topics](#topic_uvz_kdh_bpb__section_qfv_xdh_bpb)
 - [Importing comments in posts](#topic_uvz_kdh_bpb__section_y41_tdh_bpb)

## Migrating content to your knowledge base

Migrating content from an external system into your help center is a multi-step process where data from one step is required for subsequent steps.

Planning is critical. You'll need to map the structure of your legacy content to your help center's three-layer structure:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_knowledge_base.png)

### Importing your authors as Zendesk users

First, you must import the authors of all your articles as Zendesk users with the role of "agent" (an agent in Zendesk is not necessarily someone who solves tickets (see [Understanding Zendesk Support user roles](https://support.zendesk.com/hc/en-us/articles/4408883763866)).

To create Zendesk users with the API (see [Create user](https://developer.zendesk.com/api-reference/ticketing/users/users/#create-user)). Ensure you set the `role` attribute to "agent" in each POST request.

After you have successfully created a user, Zendesk returns the details of the user in the JSON response, including the user's new ID:

```
{
 "user": {
    "id":   9873843,
    "name": "Roger Wilco",
    ...
 }
}
```

Record the ID of each user as you'll need the IDs to set the `author_id` attribute of each article you create in your help center.

Tip: You might want to create a map of each author ID and their legacy articles.

If you plan on using [organizations](https://support.zendesk.com/hc/en-us/articles/4408886146842) in [user segments](https://support.zendesk.com/hc/en-us/articles/4408837707290) to segregate sections, you must create the organizations *before* you create any users. You can then assign the organization ID to the user when you are creating the user (see [Create organization](https://developer.zendesk.com/rest_api/docs/core/organizations#create-organization)). If your users will belong to multiple organizations, then use [organization memberships](https://developer.zendesk.com/rest_api/docs/core/organization_memberships) to add organizations to the user record.

### **Creating categories in your knowledge base**

Categories are collections of sections (see [Create category](https://developer.zendesk.com/rest_api/docs/help_center/categories#create-category)). After you have created a category, Zendesk returns a JSON response with the category's new ID:

```
{
 "category": {
    "id":          37486578,
    "name":        "Super Hero Tricks",
    "description": "This category contains a collection of Super Hero tricks",
    "locale":      "en-us",
    "position":    2,
    ...
 }
}
```

Record the ID of each category, because when you create sections later, you'll need the IDs to assign sections to specific categories.

### **Creating user segments (optional)**

If you want to restrict access to certain sections in your help center, you can assign [user segments](https://support.zendesk.com/hc/en-us/articles/4408837707290) to your sections (see [Create user segment](https://developer.zendesk.com/rest_api/docs/help_center/user_segments#create-user-segment)).

After you have created a user segment, Zendesk returns a JSON response with the user segment's new ID:

```
{
 "user_segment": {
    "id": 7284
    "name": "VIP agents",
    "user_type": "staff",
    "group_ids": [12, ...],
    "organization_ids": [42, ...],
    "tags": ["vip"],
    "created_at": "2017-05-21T20:01:12Z",
    "updated_at": "2017-05-21T20:01:12Z",
    "built_in": false
 }
}
```

Record the ID of each user segment because when you are creating sections later, you'll need the segment ID to assign access restrictions to the sections.

### **Creating sections in your categories**

Sections are collections of articles (see [Create section](https://developer.zendesk.com/rest_api/docs/help_center/sections#create-section)). Ensure you set the `category_id` and `user_segment_id` (if any), in each POST request. Zendesk returns a JSON response with the section's new ID:

```
{
 "section": {
    "id":          3457836,
    "name":        "Avionics",
    "description": "This section contains articles on flight instruments",
    "locale":      "en-us",
    "category_id": 3465,
    ...
 }
}
```

Record the ID of each section because when you create articles later, you'll need the section IDs to assign articles to specific sections.

### **Creating articles in your sections**

When you have all the section IDs and user IDs from the previous steps, you can create articles (see [Create article](https://developer.zendesk.com/rest_api/docs/help_center/articles#create-article)). In addition to the `title` and `body`, make sure you set the `author_id` and `section_id` in each POST request.

Note: All authors are automatically subscribed to their articles. If your help center has been activated, then the authors will receive an email notification when the article is created.

Zendesk returns a JSON response that looks as follows:

```
{
 "article": {
    "id":                37486578,
    "author_id":         3465,
    "promoted":          false,
    "position":          42,
    "comments_disabled": true,
    "section_id":        98838,
    ...
 }
}
```

### **Uploading attachments (if necessary)**

If an article has inline images that aren't hosted on a public file server, such as Amazon S3, then upload the images to your help center (see [Create unassociated attachment](https://developer.zendesk.com/rest_api/docs/help_center/article_attachments#create-unassociated-attachment)).
Ensure you set the `inline` parameter to `true`.

Zendesk returns a JSON response with a URL (`content_url`) for the attachment:

```
{
 "article_attachment": {
    "id":           1428,
    "article_id":   null,
    "file_name":    "icon.jpg",
    "content_url": "https://company.zendesk.com/hc/article_attachments/1428/icon.jpg",
    "content_type": "application/image",
    "size":         58298,
    "inline":       true
 }
}
```

Use the `content_url` to update the image URL in the HTML of the article (see [Associate attachments in bulk to article](https://developer.zendesk.com/rest_api/docs/help_center/articles#associate-attachments-in-bulk-to-article)).

### **Importing article comments**

To import comments, you'll need an author ID and the article's ID. Both agents and end users can be authors of comments (see [Create comment](https://developer.zendesk.com/rest_api/docs/help_center/comments#create-comment)).

Note: A comment author is automatically subscribed to the article. If your help center has been activated, then they'll get an email notification when their comment is created.

## Migrating content to your community

Importing community content has many of the same considerations as importing a knowledge base. You'll need to [import users](https://developer.zendesk.com/rest_api/docs/core/users#create-user) to assign authors to posts.
You'll also need to map the structure of your legacy community content to the two-layer structure of your help center community:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_community.png)

### **Creating user segments (optional)**

If you want to restrict access to certain topics, you'll need user segment IDs (see [Create a user segment](https://developer.zendesk.com/rest_api/docs/help_center/user_segments#create-user-segment)). When creating the topics later, you'll need the user segment IDs to assign access restrictions to topics.

### **Importing topics in your community**

If applicable, ensure you set the `user_segment_id` in the POST request (see [Create topic](https://developer.zendesk.com/rest_api/docs/help_center/topics#create-topic)).

Zendesk returns a JSON response with the topic ID:

```
{
 "topic": {
    "id":   115000553548,
    "name": "Help Center-Tricks",
    ...
 }
}
```

Record the ID of each topic because when you create topics later, you'll need the topic IDs to assign posts to specific topics.

### Importing posts in topics

In addition to the `title` and `details`, make sure you set the `author_id` and `topic_id` in each POST request (see [Create post](https://developer.zendesk.com/rest_api/docs/help_center/posts#create-post)).

Unlike KB articles, authors of community posts can be agents or end users.

When creating a post, the author is automatically subscribed to all updates to that topic, and will be notified when a new post is created or updated.

All subscribers of the same topic receive an email notification when the post is created. To prevent subscribers from being overwhelmed by notifications when bulk importing posts, include a `notify_subscribers` parameter with a value of `false` in your POST requests.

```
{
 "post": {
    "id":        35467,
    "author_id": 89567,
    "title":     "Help!",
    "details":   "My printer is on fire!",
    "notify_subscribers": false,
    ...
 }
}
```

### **Importing comments in posts**

After creating the posts and getting their IDs, you can now add their associated comments (see [Create comment](https://developer.zendesk.com/rest_api/docs/help_center/post_comments#create-comment)).

You can only create one comment at a time. When creating a post comment, the author of the comment is automatically subscribed to all updates to that topic and are notified when a new post is created or updated.

All subscribers of the same topic receive an email notification when the comment is created. To prevent subscribers from being overwhelmed by notifications, include a `notify_subscribers` parameter with a value of `false` in your POST requests.