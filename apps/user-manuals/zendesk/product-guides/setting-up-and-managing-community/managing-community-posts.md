# Managing community posts

Source: https://support.zendesk.com/hc/en-us/articles/4408823846170-Managing-community-posts

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

You can edit, move, or delete community posts, as well as edit or delete comments on community posts. You can also take a number of actions on the post or comment.

Note: The user interface described in this article is based on the default Copenhagen theme.
If your theme is customized, options might appear differently or be missing.

Knowledge admins have full permissions to manage community posts. Users with moderator rights can perform a limited number of actions on posts depending on their moderator group permissions.
Regular agents, who are not part of a moderator group, don't have permissions to take any actions on community posts.

For information about managing the discussion topics that contain community posts, see [Managing help center community discussion topics](https://support.zendesk.com/hc/en-us/articles/4408833845786).

Topics covered in this article:

- [Editing and deleting community posts](#topic_csn_mgt_mgb)
- [Editing and deleting comments on community posts](#topic_gzn_4hf_4k)
- [Moving a post to another discussion topic](#topic_lwk_zst_st)
- [Adding content tags to community posts](#topic_glj_1sr_bvb)
- [Closing a post for comments](#topic_sjv_q1x_ds)
- [Marking a comment as the official comment for a post](#topic_ttm_l2t_mgb)
- [Promoting a post by pinning or featuring](#topic_fm4_s1x_ds)
- [Setting status on a post](#topic_bpy_t1x_ds)
- [Marking a post as answered](#topic_ycx_q3)
- [Approving pending content](#topic_jgf_mkw_2jb_2)
- [Moving a live community post to the moderation queue](#topic_cvv_tt4_rrr)
- [Creating a ticket from a community post or comment](#topic_4c4_ydn_c5)

## Editing and deleting community posts

You can edit or delete community posts as needed.

**To edit a post**

1. In the post you want to edit, click the **Post actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_post_actions_icon.png)), then select **Edit**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_comm_post_actions_edit.png)
2. Make your changes, then click **Update**.

**To delete a post**

1. In the post you want to delete, click the **Post actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_post_actions_icon.png)), then select **Delete**.
2. Click Ok to confirm the deletion.

   The post is removed from the topic and cannot be recovered.

## Editing and deleting comments on community posts

You can edit or delete comments on community posts as needed.

You can also mark a comment as official (see [Marking a comment as the official comment for a post](#topic_ttm_l2t_mgb)).

**To edit a comment**

1. Beside the comment you want to edit, click the options menu, then select **Edit**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_comm_post_edit_comment.png)
2. Make changes, then click **Update**.

**To delete a comment**

- Beside the comment you want to delete, click the **Comment actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_post_actions_icon.png)), then select **Delete**.

 The comment is removed from the post and cannot be recovered.

## Moving a post to another discussion topic

You can move a post from one discussion topic to another in your community. You cannot move a community post to the knowledge base.

**To move a post to another topic**

1. In the post you want to move, click the **Post actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_post_actions_icon.png)), then select **Edit**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_comm_post_actions_edit.png)
2. Click inside the **Topics** box and select another topic.
3. Click **Update**.

## Adding content tags to community posts

You can apply content tags to new or existing posts to group and display related content to end users. End users can click content tags displayed on community posts to open a search results page that displays links to all help center content (articles and posts) with the same content tag. See [About content tags](https://support.zendesk.com/hc/en-us/articles/4848925672730).

**To add content tags to community posts**

1. In the post you want to edit, click the **Post actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_post_actions_icon.png)), then select **Edit**.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/ew-gather-content-tag-edit-post.png)
2. In the **Related to** field, click the down arrow then select the content tag you want to apply to the post.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/ew-gather-content-tag-related-to.png)
3. Click **Update**.

## Promoting a post by pinning or featuring

You can promote community posts by *pinning* or *featuring*.

When you *pin* a post, it moves to the top of the posts list within its topic and has a star beside it. This enables you to draw attention to important posts in a topic, such as announcements or guidelines.

Pinned posts always appear at the top of the topic, regardless of any sorting option chosen. The most recently pinned post will be the top-most. You can manually add styling for pinned posts so that they appear different than other posts in the topic.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_pinned_to_top_example.png)

When you *feature* a post, it is labeled as "featured" and appears in the featured posts component, which you can add to any page in your theme.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_featured_post_component_example.png)

**To pin a post**

- In the post you want to pin, click the **Post actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_post_actions_icon.png)), then select **Pin to top**.

 If you don't want the post to be pinned to the top of the topic anymore, select **Unpin from top**.

**To add styling for pinned posts to your theme**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. In the Theme panel, click **Edit theme**.
3. Select the **Community post page** in the template drop-down in the upper-left.
4. Click **Post actions**.
5. Click **Pin to top**.
6. Click the **CSS** tab, then add the following CSS to style pinned posts or modify it to fit your design:

   *.post-pinned .**question-title:before {*

   *content: "\2605";*

   *margin-right:
   5px;*

   *color: $color\_5;*

   *}*
7. Click **Save**, then **Publish changes**.

**To feature a community post**

- In the post you want to feature, click the **Post actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_post_actions_icon.png)), then select **Feature post**.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_comm_post_actions_feature.png)

 You must have added the featured posts component to your theme for the post to be featured. Otherwise, selecting the feature post option does nothing.

 If you don't want the post featured in the Featured Posts component anymore, select **Unfeature post**.

**To add featured posts to your theme**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. In the Theme panel, click **Edit theme**.
3. Select a template from the template drop-down in the upper-left, then paste the following snippet of code where you want featured posts to appear (on your Home page, for example).

   ```
   <div class="featured-posts">
       <h2>{{t 'featured_posts'}}</h2>

      {{#if featured_posts}}

         <ul class="featured-post-list">

           {{#each featured_posts}}

             <li><a href="{{url}}">{{title}}</a></li>

           {{/each}}

         </ul>

       {{else}}

         <p>{{t 'no_featured_posts'}}</p>

       {{/if}}

     </div>
   ```
4. Click **Preview** at the top to ensure it looks as intended. To preview a featured post, use the preview window to the right of the theme editor, locate a post, click **Post actions** and click **Feature post**.
5. Click **Save**, then **Publish changes**.

## Setting status for a community post

You can set a status of Planned, Not planned, or Completed on any community post. This can be especially useful if you have feature requests in your community and want to communicate status.

When you set status, the status appears in the list of posts within the topic and on the post itself. You can filter by any status to see all posts in a topic with the selected status.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_comm_status_example.png)

**To set status on a community post**

- In the post where you want to set status, click the **Post actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_post_actions_icon.png)), then select one of the statuses: **Planned**, **Not planned**, **Completed**, and **Answered**.

**To filter community posts by status**

- In a community topic, click **Show all**, then select one of the status options.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_comm_filter_by_status.png)

## Closing a post for comments

If you don't want to allow comments on a community post, you can close the post for comments.

**To close a community post for comments**

- In the post you want to close for comments, click the **Post actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_post_actions_icon.png)), then select **Close for comments**.

## Marking a comment as the official comment for a post

You can mark a comment as the official comment for a community post. You can make either a new comment or an existing comment the official comment. Make sure that you mark only one comment as the official comment for a post. You cannot mark an official comment on a knowledge base article.

When you mark an official comment, it appears as the first comment on the post and is indicated as the official comment. That means that if you edit an existing comment and mark it as official, that comment moves from its current place in the order and timeline of comments, and appears at the beginning, ahead of any older comments.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/official_comment_label.png)

If a comment is marked as the official comment and the user who made the comment is downgraded to end user, the comment remains the official comment.

**To mark a comment as the official comment**

1. In the post where you want an official comment, either enter a new comment or [edit an existing comment](#topic_gzn_4hf_4k).
2. Click **Official comment** under the comment.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/official_comment_checkbox.png)
3. Click **Submit** or **Update**, depending on whether you are making a new comment or editing an existing comment.

   The comment becomes the first comment on the post and is indicated as the official comment. The official comment checkbox is then hidden for all other comments related to the post.

## Marking a post as answered

If a comment has been added that answers the subject of a post, you can mark the post as answered.

**To mark a post as answered**

- In the post you want to mark as answered, click the **Post actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_post_actions_icon.png)), then select **Answered**.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gather_status_answered.png)

 If you have the correct moderator permissions, you can set the status as **Answered** only if a status has not previously been set.

 If you are a Knowledge admin, you can change the status to **Answered** from any other state.

## Approving pending content

If a post or comment is marked as pending approval, you can mark it as approved.

**To mark a post as approved**

- In the post you want to mark as approved, click the **Post actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_post_actions_icon.png)), then select **Approve**.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gather_approve_pending_content.png)

 Note: This action is not available for content that is pending approval in the spam queue.

## Moving a live community post to the moderation queue

You can send a live post to the content moderation queue if it contains content that you want to review. The post is then hidden from the community and appears in the content moderation queue for Knowledge admins.

**To move a live post for moderation**

- In the post you want to moderate, click the **Post actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_post_actions_icon.png)), then select **Hide for moderation**.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_hide_for_moderation.png)

 The post is no longer visible to the community. However, Knowledge admins can see the post in the content moderation queue. From there, a Knowledge admin can review the post and decide which action to take. See [Moderating end-user content](https://support.zendesk.com/hc/en-us/articles/4408894193562).

## Creating a ticket from a community post or comment

You can create a ticket from a community post or comment. When you do, a ticket is created in your instance of Zendesk Support with the body text from the post or comment and a link to the post or comment.

In the community post, the ticket number link appears at the top of the post so you can easily access the ticket from the post. In a community comment, the ticket number link appears beside the comment. If you click the link, you can access the ticket directly.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gather_ticket_number.png)

**To create a ticket from a community post**

1. In the post you want to convert to a ticket, click the **Post actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_post_actions_icon.png)), then select **Create a ticket**.
2. A Create a ticket window appears with the following fields prefilled with information from the post:
   - Subject:

     Request created from: <*community post title*>
   - Description:

     This request was created from a contribution made by <*post creator name*> on <*date and time*>.

     There is a link to the post itself, followed by the post contents.
   - Who should be the requester of the ticket?:

     The default ticket requester is the person who created the post, but you can change this to be yourself. The person specified in this field receives an email notification when the support ticket is created.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gather_create_a_ticket.png)Make any changes to the subject or description as needed, then select yourself or
   the poster as the requester of the ticket.

   The person specified in this field receives an email notification.
3. Click **Create ticket**.
4. In Support, the ticket is created, and is triaged by your support team.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gather_ticket_in_support.png)

**To create a ticket from a comment on a community post**

1. Beside the comment you want to convert to a ticket, click the **Comment actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_post_actions_icon.png)), then select **Create a ticket**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_comm_post_comment_create_ticket.png)
2. A Create a ticket window appears with the following fields prefilled with information from the comment:
   - Subject:

     Request created from: <*community post title*>
   - Description:

     This request was created from a contribution made by <*comment creator name*> on <*date and time*>.

     There is a link to the comment itself, followed by the comment contents.
   - Who should be the requester of the ticket?:

     The default ticket requester is the person who created the comment, but you can change this to be yourself. The person specified in this field receives an email notification when the support ticket is created.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gather_create_ticket_comment.png)Make any changes to the subject or description as needed, then select yourself or
   the poster as the requester of the ticket.

   The person specified in this field receives an email notification.
3. Click **Create ticket**.
4. In Support, the ticket is created, and is triaged by your support team.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gather_ticket_in_support.png)