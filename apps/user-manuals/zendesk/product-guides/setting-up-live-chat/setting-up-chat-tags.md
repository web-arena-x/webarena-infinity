# Setting up chat tags

Source: https://support.zendesk.com/hc/en-us/articles/4408844177050-Setting-up-chat-tags

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Chat tags are labels you add to chat sessions to help you categorize and sort your website's chat sessions. Agents select tags from an administrator-defined list and add them to chat sessions they're serving. They can add tags individually or by using a shortcut with tags. For details about adding tags to chat sessions, see [Adding tags to chat sessions](https://support.zendesk.com/hc/en-us/articles/4408834844698).

Note: Chat tags apply to specific chat conversations, not to the visitor in general. Chat tags are separate from API and trigger tags. For details, see [Understanding different types of tags in Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/4408888643866).

This article contains the following sections:

- [Determining how tags are created](#topic_erx_lr4_nt)
- [Editing available tags in the Predefined Tags List](#topic_lpp_4w4_nt)
- [Adding tags to shortcuts](#topic_b4f_qcp_nt)
- [Creating tags in shortcuts and during chats](#topic_f1h_jz4_nt)
- [Creating and editing tags in History](#topic_xr1_blz_dv)

## Determining how tags are created

Only administrators can create tags. Agents must select from existing tags that have been created by administrators. Depending on your settings, there are three possible places administrators can create new chat tags:

- Regardless of your settings, all administrators can create and delete tags in the Predefined Tags List ( Settings > Account > Chat Tags tab). For details, see [Editing available tags in the Predefined Tags List](#topic_lpp_4w4_nt).
- If the Allow Tag Creation setting is enabled, they can also create new chat tags in these two places:
 - While setting up a shortcut
 - During a chat session in the chat panel

Note that this setting is enabled by default.

**To allow administrators to create tags in shortcuts or during chats**

1. Under **Settings** > **Account**, select the **Chat Tags** tab.
2. In the **General Preferences** section, check the **Allow Tag Creation** check box.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_allow_tag_creation.png)
3. Click **Save Changes**.

## Editing available tags in the Predefined Tags List

The Predefined Tags List, available under **Settings** > **Account** > **Chat Tags** tab, contains all chat tags for your account.

If a tag is removed from the Predefined Tags list, it can no longer be added to new chats or shortcuts. However, if a removed tag is already included in a shortcut, it will remain available to agents through that shortcut until it is manually removed. See Editing, deleting, and cloning shortcuts for more information.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settingup_tags2.png)

Updates to the Predefined Tags List take affect in real-time: logged-in agents see them automatically without having to log out and back in. If you remove a tag from the list, it stops being available to agents but isn't deleted from past chats.

If the **Allow Tag Creation** setting described above is enabled, new tags that administrators create in shortcuts and during chat sessions are added to the predefined list. Tags created in History are also added.

**To edit the Predefined Tags List**

1. Add a new tag by typing it in the empty field. To add more than one tag at once, click **+**. ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settingup_tags3.png)
2. Click an existing tag from the list to select it for deletion.![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settingup_tags4.png)
3. Click **Save Changes**.

## Adding tags to shortcuts

You can add tags to shortcuts so that when an agent uses the shortcut, the tags are applied to the chat. For details about using shortcuts with tags, see [Adding tags with shortcuts](https://support.zendesk.com/hc/en-us/articles/4408834844698#topic_wdz_jtm_nt).

1. Create or edit a shortcut following the steps in [Inserting common phrases with shortcuts](https://support.zendesk.com/hc/en-us/articles/4408832184346).
2. In the **Tags** field, enter tags you want to add to the shortcut.![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settingup_tags4.png)Depending on your settings, you might have the option of creating a new tag. For details, see [Creating tags in shortcuts and during chats](#topic_f1h_jz4_nt).
3. Click **Save Changes**.

## Creating tags in shortcuts and during chats

This section applies only if you've enabled the **Allow Tag Creation** setting. For details, see [Determining how tags are created](#topic_erx_lr4_nt).

**To create a tag while editing a shortcut**

1. Create or edit a shortcut following the steps in [Inserting common phrases with shortcuts](https://support.zendesk.com/hc/en-us/articles/4408832184346).
2. In the **Tags** field, start typing the new tag. The **Create new tag** option appears.![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_shortcuts_createtag.png)
3. Click on **Create new tag**.
4. Click **Save Changes**.

**To create a tag in the chat panel**

1. Click on “click to add tags” in Tags field
2. Start typing the new tag. The **Create new tag** option appears.![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settingup_tags7.png)
3. Click on **Create new tag**.
4. Click **Save Changes**.

## Creating and editing tags in History

Administrators can delete tags, add tags, and create new tags for past chat and offline messages in History. When you create a new tag here, it's automatically added to the predefined list. It's not synced to any related Zendesk Support tickets.

Most agents do not have access to modify tags in History.

**To edit tags in History**

1. From the dashboard, select **History**.
2. Click on the chat you want to edit tags for.
3. Click the pencil icon next to Tags.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_zopim_tags_history_click.png)
4. Click the **X** next to any tag to remove it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_tags_history_delete.png)
5. Start typing a tag to add it. Select a matching tag from the list or click Create new tag.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_tags_edit_history.png)
6. Click **Save Changes**.