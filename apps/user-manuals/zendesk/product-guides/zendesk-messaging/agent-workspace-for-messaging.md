# Agent Workspace for messaging

Source: https://support.zendesk.com/hc/en-us/articles/4408821905434-Agent-Workspace-for-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

If enabled by an admin, end users can send messages to agents through the [Web Widget](https://support.zendesk.com/hc/en-us/articles/4408828655514), and agents can manage these conversations in the Zendesk Agent Workspace. Similar to social messaging, it provides a native, persistent messaging channel you can use to talk to your customers. This article provides an overview of messaging in the agent workspace. For details on how to send and receive messages, see [Receiving and sending messages in the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408843683226).

This article contains these sections:

- [About Web Widget messages in the Agent Workspace](#topic_tvk_c3h_3nb)
- [Messaging flow](#topic_bt2_l3h_3nb)
- [Information at your fingertips](#topic_zgt_l3h_3nb)
- [Working with attachments](#topic_i32_zhh_3nb)

**Related articles**

- [About the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930)
- [Enabling messaging](https://support.zendesk.com/hc/en-us/articles/4408832031898)

## About Web Widget messages in the Agent Workspace

Messaging for the Web Widget lets you deliver rich, modern, and automated conversation experiences out-of-the-box on your website. It gives customers the unique flexibility to pop in and out of the conversation at their leisure so they can get help on their own terms.

With messaging in the Web Widget:

- Customers can start and pick up conversations anywhere, any time, without losing their history.
- Agents can take advantage of the automated flows and data capture that their admins have built into the messaging flow, so they can step in and answer a message at just the right time with all the relevant information they need to help a customer.
- Similar to social messaging in the agent workspace, agents can manage messages as part of a unified conversation experience.

## Messaging flow

Customers use the Web Widget to send messages, and agents use the Zendesk Agent Workspace to respond. These messages become tickets in the workspace. Also, if enabled by your admin, customers may interact with a bot first, before requesting to talk to an agent. Your Zendesk admin configures the types of messages you can receive and how these messages are routed to your queue.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_native_message_client2.png)

When you’re working [online](https://support.zendesk.com/hc/en-us/articles/4408824439194#topic_j53_h5h_bhb) in the agent interface, you’ll see an active **Accept** button at the top of the interface when a new messaging ticket comes in.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_native_message_accept.png)

This Accept button works for live chats, social messaging, and messages from the Web Widget.

When you accept a message, you’ll see the channel type (**via messaging**) in the conversation header. Just like live chats and social messages, you can use the [composer](https://support.zendesk.com/hc/en-us/articles/4408831849882) to reply on the messaging channel, add an internal note, send an email, or make a call. You can use Chat shortcuts in Zendesk messages, but [Chat shortcuts with options](https://support.zendesk.com/hc/en-us/articles/4408832184346#topic_kwr_mgd_h2b) or dynamic content are not supported. You cannot change from a messaging channel to a social messaging channel.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_native_message_switch3.png)

You will be able view the conversation (if any) that occurred between a bot and the customer before it was handed off to you. So, you’ll have the full context of what’s going on.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_native_message_abot3.png)

If the end-user and bot conversation included [carousels](https://support.zendesk.com/hc/en-us/articles/4408831142554#topic_uj4_mnn_pgb), lists, or other rich text messages, a fallback text-only version appears in the Agent Workspace.

## Information at your fingertips

While you’re working with Web Widget messages in the Agent Workspace:

- Customer information captured by a bot is visible in [customer context](https://support.zendesk.com/hc/en-us/articles/4408829170458) and other information captured from the customer is available in custom ticket fields.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_native_message_context3.png)
- Similar to [social messaging](https://support.zendesk.com/hc/en-us/articles/4408843683226), Web Widget conversations with your customers are enhanced by leveraging all the features available in the agent workspace. This includes:

  - Targeted, channel-based business rules and ticket tags to help admins route tickets quickly to the right agent at the right time.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_native_message_trigger2.png)
  - Views and macros to help you manage your tickets and reply quickly.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_native_message_views.png)
  - [Ticket tabs](https://support.zendesk.com/hc/en-us/articles/4408844108826) and a [notifications list](https://support.zendesk.com/hc/en-us/articles/4408829025690) to show you which conversations are active. Also, typing, sent, and received indicators to keep you up-to-date.

    |  |  |
    | --- | --- |
    |  |  |
  - Ticket assignments and changes to ticket assignments work the same as with [social messaging](https://support.zendesk.com/hc/en-us/articles/4408843683226#topic_cfx_gjk_2mb).
  - When the ticket is Closed, control is handed back to the bot which means that the customer will be greeted by that bot when they send a message.

## Working with attachments

Admins can determine whether customers can attach files and images to messaging conversations. See [Configuring the widget frame](https://support.zendesk.com/hc/en-us/articles/4500747797914-Configuring-the-appearance-of-the-Web-Widget#topic_ubc_nmd_btb) for more information.

Agents and, if allowed, customers can attach files and images to messaging conversations in the Agent Workspace or Web Widget, respectively. Files and images can be attached to conversations in two ways:

- Clicking the paper clip icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/paperclip_attach.png)) in the workspace or widget, then browsing to and selecting the file(s) they want to add to the conversation.
- Selecting the file(s) they want to add to the conversation, then dragging them into the workspace or messaging conversation window.

File attachments for both customers and agents have the following limitations:

- The file size limit is 50 megabytes.
- The [file sending options](https://support.zendesk.com/hc/en-us/articles/4408886202394) that admins manage from the Chat dashboard apply to live chats, but they do not apply to web, mobile, or social messaging.
- Messaging supports a fixed list of file types, including 3g2, 3gp, 7z, aac, amr, avi, bmp, csv, doc, docx, eml, gif, heic, heif, ics, jfif, jpeg, jpg, key, log, m4a, m4v, mov, mp3, mp4, mp4a, mpeg, mpg, mpga, neon, numbers, odt, oga, ogg, ogv, opus, pages, pdf, png, pps, ppsx, ppt, pptx, qt, svg, tif, tiff, txt, vcf, wav, webm, webp, wmv, xls, xlsx, xml, yaml, yml. Zip files (zip) that include other file types are also supported.
- [Private attachments](https://support.zendesk.com/hc/en-us/articles/4408832757146#topic_nrp_bnx_xdb) are currently not available in messaging.