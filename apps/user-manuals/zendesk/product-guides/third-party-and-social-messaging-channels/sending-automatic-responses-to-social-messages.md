# Sending automatic responses to social messages

Source: https://support.zendesk.com/hc/en-us/articles/4408838007578-Sending-automatic-responses-to-social-messages

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Social Messaging add-on |

Customers without Zendesk Suite must have Support and Chat with the Social Messaging add-on to use this feature.

If you have added Facebook Messenger, X (formerly Twitter) DM, WhatsApp, LINE, or
WeChat channels, you may want to set up the auto-responder for those
channels. The auto-responder sends messages automatically to an end user
when you receive their messages.

This article contains the following sections:

- [About the auto-responder](#topic_ufs_cb3_n3b)
- [Setting up the auto-responder](#topic_sdv_zkk_zlb)
- [Adding user properties to automatic responses](#topic_dbg_t2r_gmb)

## About the auto-responder

You need to set up the auto-responder for each of the social messaging
accounts you have added to Zendesk. You can do this once for each
channel. You must be an admin to set up the auto-responder.

Here's how the auto-responder works:

- There’s no character limit for the automatic
  response.
- The auto-responder does not support dynamic content. See [Using dynamic content
  to translate your ticket fields (Professional and
  Enterprise)](https://support.zendesk.com/hc/en-us/articles/4408883892762-Using-dynamic-content-to-translate-your-ticket-fields-Professional-and-Enterprise-).
- The automatic response is sent once a day, not every time
  the end user sends a message.
- Automatic responses do not show up in ticket events. See [Viewing all events of
  a ticket](https://support.zendesk.com/hc/en-us/articles/4408829602970).
- If you have automatic responses set up via chat triggers for
  live chats, they may also apply to social messaging tickets.
  Triggers created with the following conditions and actions
  apply to social messaging tickets:
  - Chat trigger conditions: Visitor department,
    Account status, Department status, or Chat-related
    information (all types).
  - Chat trigger actions: Send message to
    visitor.
- Chat triggers created with other conditions and actions will not
  work for social messaging.

## Setting up the auto-responder

If you set up the auto-responder for your social messaging channels, the
auto-responder will send messages automatically to an end user when
you receive their messages.

**To set up the auto-responder for WhatsApp, LINE, or WeChat**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Open a channel for editing.

   The **Edit** screen
   displays.
3. Click **Auto-responder**.
4. Activate the auto-responder.
5. Edit the default auto-responder message.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/social_auto_responder.png)
6. Click **Save**.

## Adding user properties to automatic responses

You can add user properties to the automatic response, such as the user’s
first and last name, if desired.

For example, if your automatic response is configured like this:

```
Hi, {{firstName}}, Thanks for reaching out. An agent will be with you soon.
```

The message sent to a user named Martin Smithson looks like
this:

```
Hi Martin, Thanks for reaching out. An agent will be with you soon.
```

If the user's first name can't be resolved, the message looks like
this:

```
Hi, Thanks for reaching out. An agent will be with you soon.
```

Also, you can include a default value in the placeholder. This value is
used if the user's first name can't be resolved.

For example, if your automatic response is configured like this:

```
Hi, {{firstName || there}}, Thanks for reaching out. An agent will be with you soon.
```

The message sent looks like this when the user's first name can't be
resolved:

```
Hi there, Thanks for reaching out. An agent will be with you soon.
```

For more information about what properties you can use and how to
correctly format them, see [Managing user
information](https://docs.smooch.io/guide/managing-user-information/#structured-fields) in the Sunshine Conversations help
center. The user properties used in the automatic response aren’t
the same as [user property keywords](../../agent-guide/ticket-basics/zendesk-support-search-reference.md#topic_rvz_afv_uc)
used in other parts of Zendesk Support.