# Working with Chat tags in the Zendesk Agent Workspace

Source: https://support.zendesk.com/hc/en-us/articles/4408822099738-Working-with-Chat-tags-in-the-Zendesk-Agent-Workspace

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article describes how Chat tags are supported in the [Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930). If [enabled](https://support.zendesk.com/hc/en-us/articles/4408844177050) by an admin, Chat tags are labels you add to chat sessions to help you categorize and sort your website's chat sessions so you can better understand your traffic and support needs.

Topics in this article include:

- [About Chat tags](#topic_u1g_jsc_jjb)
- [Using Chat tags in the Zendesk Agent Workspace](#topic_bpk_stc_zmb)
- [Adding tags manually](#topic_obj_4jd_zmb)
- [Using shortcuts to add tags](#topic_fvr_jwc_zmb)
- [Using macros to add tags](#topic_vqg_rjd_zmb)

**Related topics**

- [About the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930)
- [Serving chats in the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408824439194)

## About Chat tags

Zendesk Chat offers two different types of tags to categorize your visitors and chat sessions:

- **Chat tags** contain information about the specific content of a chat session.
- **Javascript API and trigger tags** contain more general information about the visitor.

You can use either or both types of tags to better understand your chat traffic. There are important differences in how these types of tags are added, stored, and displayed. For more information, see [Understanding different types of tags in Chat](https://support.zendesk.com/hc/en-us/articles/4408888643866) and [Setting up Chat tags](https://support.zendesk.com/hc/en-us/articles/4408844177050).

## Using Chat tags in the Zendesk Agent Workspace

In the Zendesk Agent Workspace, tags from all sources appear in one place.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_chat_tags.png)

- When a ticket is created, tags applied by the Javascript API and triggers are pre-populated in the tags field. Tags added through the Javascript API and Chat triggers during a conversation appear in the tags field when the chat has ended.
- During a conversation, agents can add tags manually in the Tags field or automatically through shortcuts or macros. These tags aren't saved until the ticket is updated via the **Submit** button.
- When the conversation ends, agents can continue to add tags until the ticket is closed.
- If an agent transfers the chat to another online agent or group, tags remain in the Tags field.
- Ticket fields, including new tags, are saved when the chat is transferred. If a change in a ticket field activates a business rule, the business rule takes precedence over the transfer.
- Tags that agents add manually in the Tags field of the ticket interface do not show up on the [Chat dashboard](https://support.zendesk.com/hc/en-us/articles/4408830603674). Tags added through APIs and tags added by triggers do appear on the dashboard.

## Adding tags manually

Agents can manually add tags to tickets during or after a Chat conversation. Depending on your support workflow, you might want to add tags to provide more context for the request so that tickets can be viewed and tracked, or processed by your account's business rules.

- **To add tags manually**
- In a ticket, enter new tags into the **Tags** field as needed. Enter a space after each tag.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_chat_tags_manual.png)

For more information, see [Adding tags to tickets](https://support.zendesk.com/hc/en-us/articles/4408835059482#topic_vwg_ola_vb).

## Using shortcuts to add tags

Admins can add tags to shortcuts so that when agents use the shortcut, the tags are applied to the chat. For details about adding tags to shortcuts, see [Adding tags to shortcuts](https://support.zendesk.com/hc/en-us/articles/4408844177050#topic_b4f_qcp_nt).

**To use shortcuts to add tags**

1. Start typing a shortcut or a slash (/) to view all shortcuts.
2. Insert a shortcut by clicking it or selecting it and pressing Enter.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_chat_tags_shortcuts.png)

   When you select the shortcut, the tags appear in the **Tags** field of the ticket.
3. You can delete tags by clicking the X next to the tag.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_chat_tags_delete.png)

## Using macros to add tags

Agents and admins can also use the **Set tags** action statement in macros to include tags in tickets and apply them to a Chat. Agents can add them in personal macros and admins can add them in shared marcos and personal macros.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_chat_tags_macro.png)

For more information, see [Creating macros for tickets](https://support.zendesk.com/hc/en-us/articles/4408844187034) and [Building macro action statements](https://support.zendesk.com/hc/en-us/articles/4408832783642).