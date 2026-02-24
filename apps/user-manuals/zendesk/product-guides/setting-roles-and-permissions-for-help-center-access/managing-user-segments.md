# Managing user segments

Source: https://support.zendesk.com/hc/en-us/articles/4408831908634-Managing-user-segments

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

A [*user segment*](https://support.zendesk.com/hc/en-us/articles/4408837707290) is a collection of end users and/or agents,
defined by a specific set of attributes, used to determine access to help center content.

All of your user segments appear on the User Segments management page. After you create user
segments, you can edit, or delete those user segments as needed. You must be a Knowledge admin to
manage user segments.

This article contains the following sections:

- [Accessing your user segments](#topic_vbh_rdw_gfb)
- [Editing user segments](#topic_dj4_d2w_52b)
- [Deleting user segments](#topic_itb_h2w_52b)

Related articles:

- [Create management permissions to define agent editing and publishing
  rights](https://support.zendesk.com/hc/en-us/articles/4408827952538)
- [Setting view permissions on articles with user segments](https://support.zendesk.com/hc/en-us/articles/4408824005914)

## Accessing your user segments

All of your [user segments](https://support.zendesk.com/hc/en-us/articles/4408837707290) appear on the User Segments management
page. User segments are presented in a table format that includes three columns that provide
the name of the user segment, the User type, and Last edited date. There are two different
types of user segments:

- Staff members
- Signed-in users

User segments appear in the order in which they were created, from newest to oldest. You
cannot rearrange user segments in the list.

**To access your user segments**

- In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **User permissions**
  (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_user_permissions.png)) in the sidebar.

  ![Guide User segments management page](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_user_segments_management_page.png)

## Editing user segments

You can [create user segments](https://support.zendesk.com/hc/en-us/articles/4408837707290) to define access to articles
and topics in your help center. You can also edit a user segment at any time to update the
tags, groups, organizations, or individual users that define the user segment. However, you
cannot change the User type.

**To edit a user segment**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **User permissions**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_user_permissions.png)) in the sidebar.
2. Click the user segment you want to edit.

   Alternatively, you can click the options
   menu at the end of the user segment, then select **Edit**. You cannot edit the
   built-in user segments.
3. Make any changes that you want to apply.

   On the right, you can preview a list of
   matching users. If there are more than 30 users, click **View all matching
   users.**

   You cannot edit where a user segment is applied in the user segment
   itself, but you can click **View articles that are only visible to this segment**
   to see a list of articles where the user segment is applied.
4. Click **Save segment**.

## Deleting user segments

You can [create user segments](https://support.zendesk.com/hc/en-us/articles/4408837707290) to define access to articles
and topics in your help center. When you no longer need a user segment, you can delete
it.

**To delete a user segment**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **User permissions**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_user_permissions.png)) in the sidebar.
2. Click the options menu at the end of the user segment you want to delete, then select
   **Delete**.

   ![Guide User segments delete](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_user_segments_delete.png)

   Note the following:

   - Deletion of a user segment affects related articles and moderator groups, topic
     visibility, and management permissions.
   - If the user segment is [currently applied to an article](https://support.zendesk.com/hc/en-us/articles/4408838243354), visibility permissions
     will be set to Everyone.
   - If the user segment is applied to a help center, the help center will be
     restricted to Admins.
   - If the user segment is currently applied to a topic, the user segment will be
     set to Everyone. See [Restricting access to community content](https://support.zendesk.com/hc/en-us/articles/4408845814170).