# Creating macros for repetitive ticket responses and actions

Source: https://support.zendesk.com/hc/en-us/articles/4408844187034-Creating-macros-for-repetitive-ticket-responses-and-actions

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Workspaces > Agent tools > Macros

You can simply and effectively streamline your workflow by creating macros for support
requests that can be solved with a single, standard response or action. This saves agents the
time and effort of manually responding to multiple customers with the same issue.

This article contains the following topics:

- [About macros](#topic_zlk_nf1_dsb)
- [Creating personal macros for tickets
  (agents)](#topic_zdw_nnw_4y)
- [Creating personal or shared macros for
  tickets (administrators)](#topic_zh2_4nw_4y)
- [Adding formatting and inline images to
  macro comments](#topic_fn3_4nw_4y)
- [Adding attachments to macro
  comments](#topic_xb4_4nw_4y)
- [Adding an alternate plain text version of a rich content macro comment](#topic_o1b_myd_yy)
- [Using placeholders in macros](#topic_h4w_1dx_5lb)

Related articles:

- [Using macros to update tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602)
- [Organizing and managing your macros](https://support.zendesk.com/hc/en-us/articles/4408884166554)
- [Using macros to start side conversations](https://support.zendesk.com/hc/en-us/articles/4408829558938)

## About macros

A macro is a prepared response or action that an agent can manually apply when they are creating or updating tickets. Macros contain actions that can update ticket properties.

Unlike triggers and automations, macros *only* contain actions, not conditions. Conditions aren't used because nothing is automatically evaluating tickets to determine if a macro should be applied. Agents evaluate tickets and apply macros manually as needed.

Macros can perform tasks. For example

- Add comment text
- Update ticket fields
- Add or remove ticket tags
- Add followers
- Change the assignee
- Set the ticket subject
- Add attachments to ticket comments
- Start side conversations

There are two types of macros: personal macros (created by an agent or administrator for their own use) and shared macros (created by an administrator for multiple users).

## Creating personal macros for tickets (agents)

Although only administrators can create the macros that are shared by
all Zendesk Support agents, agents can create personal macros for their own use. A personal
macro can only be used by the creator but is visible to admins in Admin Center. If you have
the Copilot add-on, you can [use generative AI writing tools to help create macros](https://support.zendesk.com/hc/en-us/articles/9882403344410).

You can create macros from scratch, as described here, or you can create macros [based on existing tickets](https://support.zendesk.com/hc/en-us/articles/4408886850586).

The following video gives you an overview of how to use macros to respond to tickets faster:

Use quick responses with macros [1:40]

**To create a personal macro for tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Macros**.
2. Click **Create macro**.
3. Enter the macro name, and add actions for your macro as described in [Building macro action statements](https://support.zendesk.com/hc/en-us/articles/4408832783642).
4. Click **Create**.

Your personal macros are added to the list of available macros.

## Creating personal or shared macros (admins)

A macro is a prepared response or action that an agent can apply to a ticket. Macros
contain actions that can update ticket properties.

Admins, and agents in custom roles with permission, can create *shared* macros to be
used by all agents or groups of agents. The maximum number of shared macros per account is
5,000. Admins and all agents can create *personal* macros for their own use.

A personal macro can only be used or modified by the creator but is
visible to and can be cloned by admins. For example, if an agent creates a personal macro
that could be useful to other team members, then an admin may want to clone it and recreate
it as a shared macro.

Admins can create shared macros, and can modify all shared macros,
regardless of who created them.

You can create macros from scratch, as described here, or you can
create macros [based on existing tickets](https://support.zendesk.com/hc/en-us/articles/4408886850586). If you have the Copilot
add-on, you can [use generative AI writing tools to help create
macros](https://support.zendesk.com/hc/en-us/articles/9882403344410).

Tip: **Fine Tuning:** Learn how to improve your agents' productivity in
Sylviana Ho's [Fine Tuning: Agent Productivity](https://support.zendesk.com/hc/en-us/articles/4408822423450).

**To create a personal or shared macro for tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Macros**.
2. Click **Create macro**.
3. Enter a **Macro name**.
4. (Optional) Enter a macro **Description**.
5. Select who can use the macro from **Available for**:

   - **All agents**, all agents
   - **Agents in group**, specified groups

     (Suite Growth and up or Support
     Professional and up only)
   - **Me only**, the macro creator

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macro_availability_menu.png)
6. Click **Add action**, then select an action and complete the additional field. See
   [Building macro action statements](https://support.zendesk.com/hc/en-us/articles/4408832783642).

   For
   the Comment/description macro action, you can [add formatting, images](https://support.zendesk.com/hc/en-us/articles/4408844187034-Creating-macros-for-tickets#topic_fn3_4nw_4y), and [attachments](https://support.zendesk.com/hc/en-us/articles/4408844187034-Creating-macros-for-tickets#topic_xb4_4nw_4y).
7. Click **Add action** again to add another action.
8. Click **Create**.

   The macro is created.

## Adding formatting and inline images to macro comments

You can add styling, formatting, and inline images to the **Comment/description** macro
action.

**To add formatting to your comment**

1. In the text field, enter the content you want to appear in the macro.
2. Use the formatting options in the toolbar to format your content.

   |  |  |
   | --- | --- |
   | **Toolbar button** | **Formatting** |
   |  | Heading |
   |  | Bold |
   |  | Italics |
   |  | Underline |
   |  | Text color |
   |  | Background color |
   |  | Bulleted list |
   |  | Numbered list |
   |  | Decrease indent |
   |  | Increase indent |
   |  | Link |
   |  | Block quote |
   |  | Code |
   |  | Code block |
   |  | Horizontal line |

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_macros_text_editor_options.png)

Tip: If you created a macro with the
Comment/description action before the rich text formatting editor was introduced, you can
update your macro by clicking the **Use rich content** link. This copies your existing
comment action, loads in the rich content editor, and places your comment back into the
editor. You can then apply formatting and images or attachments as needed.

Now you can [add a plain
text version of your rich content macro comment](#topic_o1b_myd_yy), if you want. The plain text
version will be intelligently applied in channels that don't support rich text
formatting.

**To add inline images to your comment**

- Drag and drop an image from your computer into the comment window, or paste a copied
  image into the window by right-clicking and selecting **Paste** or by pressing
  **Ctrl** or **⌘ + V**.

## Adding attachments to macro comments

Comments in your macros can also contain up to five file attachments.

The maximum file size for a single linked attachment is 50 MB. For more information, see [Attachment size limitations](https://support.zendesk.com/hc/en-us/articles/4408832757146#topic_lv2_cnx_xdb).

**To attach one or more files to a comment**

1. Under the text field, click **Attach files**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_macros_attach_files.png)
2. Browse to the file you want to attach.
3. Select the file, and click **Open**.

   The file is added to the ticket.

Note: If you use macros to [bulk update tickets](https://support.zendesk.com/hc/en-us/articles/4408886890906#topic_oth_lkp_gk), attachments will not be
included in the comments.

## Adding an alternate plain text version of a rich content macro comment

If you added styling, formatting, or inline images to the
**Comment/description** macro action, you can add an alternate plain text version, if
you want.

The plain text version will be intelligently applied in channels that
don't support rich text formatting. These include the Zendesk mobile app, Zendesk SMS,
messaging channels in the Zendesk Agent Workspace and in the standard agent interface, and
any app installed from the Zendesk Marketplace.

**To add a plain text version of your rich content macro comment**

1. In the macro, under the rich content version of the comment, select **Include plain
   text fallback**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macro_comment1.png)
2. In the pre-populated version that appears, make any modifications needed to create the
   plain text version of the macro comment.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macro_2.png)

## Using placeholders in macros

The macros you create for tickets can include [placeholders](https://support.zendesk.com/hc/en-us/articles/4408886858138) to help personalize your ticket responses.

Be aware of the following when applying macros with placeholders:

- When you apply a macro with placeholders to a Problem ticket, the placeholder is
  rendered when the macro is applied, not when the ticket is submitted. This can produce
  unexpected results. For example, if you send an email response to a Problem ticket using a
  macro that contains the {{ticket.requester.name}} placeholder, the ticket requester's name
  is sent to all linked tickets, not just the ticket associated with the requester. To
  prevent this from happening, add an escape character (\) in front of the placeholder. For
  example, \ {{ticket.requester.name}}. In this case, the placeholder is not rendered until
  the ticket is submitted, which will show the correct name to each user who submitted a
  ticket linked to the problem.
- When you apply a macro that has a placeholder with multi-line content, the line breaks
  are removed in the comment. This is visible in the composer before the comment is
  submitted.