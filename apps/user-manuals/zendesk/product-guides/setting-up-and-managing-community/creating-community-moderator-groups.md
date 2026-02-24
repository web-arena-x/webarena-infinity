# Creating community moderator groups

Source: https://support.zendesk.com/hc/en-us/articles/4408882973338-Creating-community-moderator-groups

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

Knowledge admins can create moderator groups for the community so that designated agents and end users can manage community activity. Community moderators can be any users you choose to administer community content.

You can create multiple moderator groups, if you want to set different moderator permissions for each group. If you have multiple help centers, any moderator groups you create apply to all your help centers. Agent permissions are not governed by moderator settings.

Note: Moderator groups are based on user segments for signed-in users, which are built on tags and organizations. Make sure you've set up a user segment that contains all the users you want to include in the moderator group before you start (see [Creating user segments](https://support.zendesk.com/hc/en-us/articles/4408837707290)).

**To create a moderator group**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **User permissions** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_user_permissions.png)) in the sidebar.
2. Select **Community moderators**.

   You can see any moderator groups that you have already created.
3. Click **Add moderator group**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gather_admin_create_moderator.png)
4. Enter a moderator group name.

   For example, **approve\_only\_moderators** might be the name of the moderator group that has permission to approve posts and comments only.
5. Set the permissions by selecting the actions you want to enable for moderators in this group.
   - [Mark as answered](https://support.zendesk.com/hc/en-us/articles/4408823846170#topic_ycx_q3) indicates that a comment has been added to the post that answers the subject of a post.
   - [Pin to top](https://support.zendesk.com/hc/en-us/articles/4408823846170#topic_fm4_s1x_ds)
     moves to the top of the posts list within its topic and has a star beside it.
   - [Feature post](https://support.zendesk.com/hc/en-us/articles/4408823846170#topic_fm4_s1x_ds)
     labels the post as "featured" and displays it in the featured posts component, if it's in your theme.
   - [Move post](https://support.zendesk.com/hc/en-us/articles/4408823846170#topic_lwk_zst_st)
     changes the location of the post to another discussion topic.
   - [Hide for moderation](https://support.zendesk.com/hc/en-us/articles/4408823846170#topic_cvv_tt4_rrr) removes a live post from the community and sends it to the content moderation queue for review. If you want to enable this action for the moderator group, ensure that you have [content moderation enabled](https://support.zendesk.com/hc/en-us/articles/4408894193562#topic_bkn_y3n_qx). Otherwise, this action will not be available to moderators, even if you have selected it here.
   - [Approve pending content](https://support.zendesk.com/hc/en-us/articles/4408823846170#topic_jgf_mkw_2jb_2) makes the content visible in the community and removes it from the content moderation queue. This action is not available for content that is pending approval in the spam queue.
6. Under **Add moderators**, select a user segment for the moderator group.

   You can only choose user segments for *signed-in users*, not *staff* user segments. If you need to create a new user segment, select **Add new user segment**.

   Matching users appear below.

   Note: If your user segment includes agents, they will not appear in the matching list, even though they have the correct permissions (see [Creating user segments for user permissions](https://support.zendesk.com/hc/en-us/articles/4408837707290)).
7. Click **Create group**.

The moderator group is created.

When a user that has been added to the moderator group next signs in to the community, they will have additional user permissions that enable them to moderate content.