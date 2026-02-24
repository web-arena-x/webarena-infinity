# Setting up your public Facebook channel

Source: https://support.zendesk.com/hc/en-us/articles/4408819897242-Setting-up-your-public-Facebook-channel

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Set up your public Facebook channel to convert Facebook Page posts and comments into tickets, allowing agents to manage them like any other ticket. You can add multiple Facebook Pages based on your plan, and configure settings for public and private messaging. Use business rules to manage Facebook tickets.

Location:  Admin Center > Channels > Messaging and social > Facebook Pages

All Zendesk Suite and Zendesk Support customers can add at least one Facebook account so that public messages, such as Facebook Wall posts and comments, become tickets. Your agents will be able to see and respond to these tickets, just like any other ticket.

Additionally, Zendesk Suite customers can add multiple Facebook Pages and receive public *and* private messages from those accounts. The number of Facebook Pages you can add depends on which version of the integration you're using.

|  |  |
| --- | --- |
| **Zendesk Support plans** | One Facebook Page with public messages only. Private messages are not supported. |
| **Zendesk Suite plans** | V1 supports up to 15 Facebook Pages with public *and* private messages.  V2 supports up to 30 Facebook Pages with public *and* private messages. |

This article describes adding a Facebook channel for *public messaging* with your customers. You must be an administrator in both Zendesk and Facebook to set up your Facebook channel.

To set up Facebook Messenger for *private messaging* with your customers, see [Adding Facebook Messenger channels](https://support.zendesk.com/hc/en-us/articles/4408835753370).

Note: Aside from the conversations occurring directly through your Facebook account within Zendesk, no other data from your Zendesk account, such as ticket data, is shared with Meta in connection with using the Facebook channel integration. Only conversations occurring directly through your Facebook account will be accessible by Meta.

This article includes the following sections:

- [How the public Facebook channel works](#topic_xrv_cj5_tl)
- [Setting up the public Facebook channel](#topic_yy3_fp3_zl)
- [Updating settings for your public Facebook channel](#topic_ejk_hp3_zl)
- [Adding another Facebook Page](#topic_aym_jp3_zl)
- [Managing Facebook tickets with business rules](#topic_jmw_ckp_hx)
- [Migrating to the Facebook channel V2](#topic_j5v_lwr_hdc)

## How the public Facebook channel works

The public Facebook channel supports Facebook Pages, which are different from personal timelines. Facebook Pages help businesses, organizations, and brands share their stories and connect with people.

After adding a Facebook account to Support, Support monitors messaging activity on the Facebook account. Each new Wall post (a public message) on the Facebook account becomes a ticket in Support. On Zendesk Suite plans, private messages sent to the Facebook account through Facebook Messenger will also become tickets.

Facebook limits how Pages can communicate publicly and privately with users. For example, if you receive a ticket from a Wall post, when you reply in the ticket, your response is added as a comment to that Wall post. If you receive a ticket from a private message, when you reply in the ticket, your response is a private message. You cannot respond to a Wall post with a private message in the ticket. Likewise, you cannot respond to a private message with a Wall post in the ticket.

Currently, the following Facebook features are not supported:

- **Reel comments**: Unsupported by [Facebook's webhooks](https://developers.facebook.com/docs/graph-api/webhooks/reference).
- **Stickers in comments**: Unsupported due to limitations in Meta’s API.
- **Video comments**: Unupported by [Facebook's webhooks](https://developers.facebook.com/docs/graph-api/webhooks/reference); however, video posts are supported.
- **Live video posts and comments**: Unsupported by [Facebook's webhooks](https://developers.facebook.com/docs/graph-api/webhooks/reference).

When a user posts to your wall, a ticket is created, and the following happens:

- For standard Wall posts, only comments received in the first week after the post will be added to the ticket. If you would like comments to create new tickets, you can [turn on that setting](#topic_ejk_hp3_zl).
- Comments received after the first week are not added to the ticket, and no new ticket is created.
- If you post to your wall and the **Include Wall posts authored by the Page** setting is turned on, a ticket is created. Comments are recorded in the ticket for one year after the posting. However, if you close the ticket, comments will no longer be recorded.

  The first time you post to your wall with the setting turned on, an end-user account is created for the Facebook Page. For example, if your Facebook Page is named Mondocam Enterprises, an end-user account is created with the name Mondocam Enterprises. This account is tied to the Facebook Page, and the role cannot be changed.

If the posting user is not already a user in your account, they become a new user in your account. If your channel has multiple Facebook Pages and a new user posts on more than one Page, a separate user account is created for each Page on which that user posts.

An agent can respond to a Wall post by adding a public comment to the ticket in Support. The agent's response is added as a comment to the Facebook post. In the following Wall post, for example, an agent answered the user's question in the Support agent interface.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/facebook_wallpost.png)

Here's the corresponding ticket in Support:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/facebook_ticket.png)

## Setting up the public Facebook channel

You can connect a Facebook account to Zendesk so that Facebook comments become tickets, and your agents can see and respond to these tickets, just like any other ticket. The number of Facebook accounts and the type of messaging supported by your account depend on your plan type.

You must be an administrator in both Zendesk and Facebook to set up your Facebook channel.

**To set up your Facebook channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png) **Channels** in the sidebar, then select **Messaging and social > Facebook Pages**.
2. Click the **Add your first Facebook Page** link. If you already have a Facebook Page, click **add new Page**.
3. Enter your Facebook credentials if you are not already logged in.
4. When asked, be sure to grant Zendesk access to your account.
5. In the **Add Facebook Pages to your account** window, locate the Page you want to add, and choose the default permissions that Zendesk has to your Facebook Page. Select **Import recent activity** to create tickets from existing messages or posts. Zendesk will import the last week of activity, up to 100 posts and 500 comments per post. If you change any of these permissions, the connection between Facebook and Zendesk might not work properly.
6. Click **Add** for the Facebook Page you'd like to link to your Zendesk account.
7. If your plan supports multiple Facebook Pages, click **Add** beside another Page if you want to add it. Otherwise, you can close the window.

   You'll want to edit the account's settings to control how messages to this account are handled. If you need help troubleshooting your Facebook channel, see [Troubleshooting issues with your Facebook channel](https://support.zendesk.com/hc/en-us/articles/4408887381914).

## Updating settings for your public Facebook channel

After you've set up your Facebook channel, you'll need to edit and confirm settings for any Facebook Page you've added. You won't see all of the settings listed in this section if your account does not support private messaging.

**To edit your Facebook channel settings**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png) **Channels** in the sidebar, then select **Messaging and social > Facebook Pages**.
2. Click **Edit** beside the Facebook Page you'd like to edit settings for.
3. Change any of the following settings:
   - **Brand** lets you choose the brand for tickets created from Facebook posts and messages. See [Setting brand for your Facebook channel](https://support.zendesk.com/hc/en-us/articles/4408824394138).
   - Select **Yes** for **Include Wall posts** to convert Wall posts to tickets automatically.
     - **Comments on a Post are added to the same ticket** adds responses on Wall posts as replies to the Wall post's ticket.
     - **Comments on a post create new tickets** adds responses on Wall posts as new tickets.
     - **Include hidden posts** allows you to review posts that haven't been approved by the Page as tickets.
     - **Include Wall posts authored by the Page** converts posts by the Facebook Page owner to tickets, and also converts user comments on the posts to tickets. If this setting turned off, Support won't create a ticket when an end user comments on a Page owner's Wall post.

       **Include unpublished posts** lets you review unpublished posts (also known as dark posts) as tickets. This will also allow Facebook ads to convert to tickets.
   - For **Include private messages**, if you want to convert private messages to tickets, [set up the Facebook Messenger channel](https://support.zendesk.com/hc/en-us/articles/4408835753370) instead of selecting this option.
4. Click **Update Page settings**.

If you don't see the Message button on your Facebook Page, you need to turn it on. In your Facebook Page, select **Manage > Edit Page**, then select **Show Message button** and click **Save Changes**.

## Adding another Facebook Page (Zendesk Suite plans only)

On Zendesk Suite plans, you can monitor up to 30 Facebook Pages (V2) or 15 Facebook Pages (V1) from your Support account. You can add additional Pages, up to the limit, at any time.

Keep in mind that Facebook still limits traffic from external sources, so it is possible that your account might make too many requests. This has more to do with how many posts and messages you retrieve than how many Pages you add.

Also, keep in mind that if a new user posts on more than one Page, a separate user account is created for each Page on which that user posts.

**To add another Facebook Page to your Facebook channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png) **Channels** in the sidebar, then select **Messaging and social > Facebook Pages**.
2. Click **add new Page**.
3. Enter your Facebook credentials if you are not already logged in.
4. In the Add Facebook Pages window, select **Import recent activity** to create tickets from existing messages or posts. Zendesk will import the last week of activity, up to 100 posts and 500 comments per post.
5. Click **Add** beside the Page you'd like to add.

   The Facebook Page appears in the **Facebook Channel** page.

## Managing Facebook tickets with business rules

Just like with tickets from other Zendesk channels, you can set up business rules, like views, automations, and triggers, to manage your Facebook tickets. In addition to the actions and conditions available for all tickets, there are a few Facebook-specific options you can use:

- **Ticket: Channel** values:
  - **Facebook Post** returns tickets created from posts.
  - **Facebook Private Message** returns tickets created from private messages.
- **Ticket: Integration account** lets you pick a specific Facebook account if you’ve added more than one. This condition also has options for X (formerly Twitter) and channel integrations like Google Play.

For general information about setting up business rules, see these articles:

- [Creating triggers for automatic ticket updates and notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466)
- [Creating automations for time-based events](https://support.zendesk.com/hc/en-us/articles/4408883801626)
- [Creating views to build customized lists of tickets](https://support.zendesk.com/hc/en-us/articles/4408888828570-Using-views-to-manage-ticket-workflow)

## Migrating to the Facebook channel V2

Facebook channel V2 was released in November 2024 and offers several enhancements that remove some limitations, reduce latency, and improve stability.

Note: Migrating to V2 requires unlinking your existing Facebook Pages and re-adding them. If you manage six or more Pages, it is recommended to wait for the automated migration process planned for 2025. If you wish to access the new features sooner, complete [this form](https://forms.gle/8NL8pQnRDMN8ZBWA9), and a member of our product team will contact you.

The upgraded V2 channel includes the following features:

- **Increased channel support**: The number of supported Facebook Pages has been increased to 30 (from 15).
- **Lower latency**: Processes have been streamlined to reduce latency and improve the overall responsiveness of the platform.
- **Removal of the 7-day limit for older posts**: Users can access and capture comments on posts older than 7 days, enhancing archival and retrieval capabilities.
- **Enhanced ad support**: More ad types are supported, including boosted ads, flexible ad formats, and standard ads. (Dynamic ads are not supported because Meta is replacing them with [flexible ads](https://www.facebook.com/business/help/835561738423867).)
- **Improved stability**: There is greater platform stability, minimizing downtime and disruptions to provide a more reliable experience.

**To migrate to Facebook channel V2**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png) **Channels** in the sidebar, then select **Messaging and social > Facebook Pages**.
2. Unlink each of your existing Facebook Pages by moving the cursor over the name of the Facebook Page and clicking **Unlink**.
   - Make sure all Pages are unlinked and removed.
   - If you have any deactivated Pages, remove them so your screen is blank.
   - Open tickets will still send and receive messages after the migration.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/facebook_page_unlink.png)
3. After all Pages are unlinked, re-add them by clicking **add new Page**. Follow the prompts to sign in, select your Pages, and adjust permissions as necessary, as described in [Setting up the public Facebook channel](#topic_yy3_fp3_zl) and [Updating settings for your public Facebook channel](#topic_ejk_hp3_zl).
4. When [updating settings](#topic_ejk_hp3_zl), select **Yes** for **Include Wall Posts** and **Include private messages**.