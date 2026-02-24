# Inserting common phrases with shortcuts

Source: https://support.zendesk.com/hc/en-us/articles/4408832184346-Inserting-common-phrases-with-shortcuts

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

With shortcuts, you can save typing time by inserting common phrases with just a few keys.
For example, you might want to create a shortcut that says, "Hi there, how may I assist you
today?" You can also use placeholders to pull in visitor-specific and chat session–specific
information.

This article contains the following topics:

- [About shortcuts](#topic_ovw_mgd_h2b)
- [Creating shortcuts](#topic_kwr_mgd_h2b)
- [Editing and cloning shortcuts](#topic_wbb_rhd_h2b)
- [Reassigning shortcuts](#topic_ucj_dm5_p2b)
- [Using shortcuts in chats](#topic_wvj_mgd_h2b)

Related articles:

- [Setting up shortcuts and departments to optimize agent
  efficiency](https://support.zendesk.com/hc/en-us/articles/4408882959642)
- [Creating custom roles and assigning users](https://support.zendesk.com/hc/en-us/articles/4408893917338)

## About shortcuts

You can create up to 15,000 shortcuts in your account.

There are three types of shortcuts available: **Personal**, **shared global**, and
**shared department**:

- **Personal shortcuts**, which can be created by an agent or administrator for their
  own use.
- **Shared shortcuts**, which can be created only by an administrator, and can be
  shared among multiple users. There are two kinds of shared shortcuts:

  - **Department shortcuts**, available to agents in specific departments. A
    single department shortcut can be used by multiple departments. See [Creating shortcuts](#topic_kwr_mgd_h2b) for more
    information. **Department shortcuts are not available on all plans**.
  - **Global shortcuts**, available to all agents, regardless of their department
    affiliation..

You select the type of shortcut during its creation. Depending on your permissions, you can
change the shortcut type by reassigning it. See [Reassigning shortcuts](#topic_ucj_dm5_p2b) for more information.

Administrators can restrict the permissions available to agents:

- **All shortcuts:** Can add and edit personal, department, and global
  shortcuts.
- **Department**: Can add and edit personal and department shortcuts.
- **Personal**: Can add and edit personal shortcuts.
- **None**: Unable to add or edit any shortcuts.

These permissions are applied to a user via their Chat role, and are configured on each
role's edit page, in the Shortcuts section:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shortcut_roles.png)

For information on these and other permissions, see [Creating custom roles and assigning users](https://support.zendesk.com/hc/en-us/articles/4408893917338).

## Creating shortcuts

Shortcuts are created on the Shortcuts settings page, which is accesed from the Chat
dashboard.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shortcuts_settings.png)

**To create a shortcut**

1. From the Chat dashboard, select **Settings > Shortcuts**.
2. Click **Add Shortcut** to open the shortcut creation page:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shortcuts_add.png)
3. In the **Shortcut** field, enter the abbreviated text you want to use as your
   shortcut.

   Note: Shortcut names cannot contain the following characters: /, \ ,
   $.
4. Use the **Available for** drop-down to select the shortcut type you want to create.
   See [About shortcuts](#topic_ovw_mgd_h2b) for information
   on shortcut types:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_select_shortcut_type.png)

   - Select **All Agents** to create a shared global shortcut.
   - Select **Agents in Department(s)** to create a shared department shortcut.
   - Select **Me only** to create a personal shortcut.
5. If you selected **Agents in Departments** in the previous step, enter the names of
   the department(s) you want to share the shortcut with into the **Required**
   field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shortcut_select_dept.png)
6. In the **Message** field, enter the complete phrase or question the shortcut should
   insert.

   To pull in visitor-specific details, you can click the **Insert
   placeholder** link to display a list of available placeholders. Click on the
   placeholder you want to use to insert it into the message body.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shortcuts_placeholders.png)
7. (Optional) If your shortcut is for a question with a discrete list of answers, click
   **Add Option** to add one or more Options to enter answers visitors should select
   from, such as in the example below:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shortcuts_add.png)
8. (Optional) If needed, click in the **Tags** field to add a tag to a chat when this
   shortcut is used.
9. Click **Create Shortcut** to finish.

## Editing, deleting, and cloning shortcuts

You can edit existing shortcuts, delete unneeded shortcuts, or clone a shortcut to copy its
content and modify it.

**To edit an existing shortcut**

1. From the Chat dashboard, select **Settings > Shortcuts**.
2. Click on the row of any shortcut to edit it.
3. Update the information as needed, then click **Save Changes**.

**To delete an existing shortcut**

1. From the dashboard, select **Settings > Shortcuts**
2. Click on the row of any shortcut to select it.
3. Use the **Actions** drop-down menu at the top of the page to select **Delete**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shortcuts_clone.png)

   The shortcut is removed from the list.

**To clone an existing shortcut**

1. From the dashboard, select **Settings > Shortcuts**
2. Click on the row of any shortcut to select it.
3. Use the **Actions** drop-down menu at the top of the page to select
   **Clone**.
4. Update the information as needed, **making sure to give the shortcut a new name**.
5. Click **Create Shortcut**.

## Reassigning shortcuts

Admins and agents can change a shortcut’s type by reassigning them. Shortcuts can
be reassigned individually, or in bulk.

**To reassign shortcuts**

1. From the dashboard, select **Settings > Shortcuts**.
2. Select one or more shortcuts. You can select all shortcuts on the list by
   clicking the checkbox at the top of the list.
3. Click the **Actions** drop-down menu, then select **Reassign**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shortcuts_reassign.png)
4. Select the shortcut type you want to apply:
   - Select **All Agents** to create a shared global shortcut.
   - Select **Agents in Department(s)** to create a shared department
     shortcut, if available.
   - Select **Me only** to create a personal shortcut, if available.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shortcuts_reassign_select.png)
5. If you selected **Agents in Departments**, enter the names of the department(s) you
   want to share the shortcut with.
6. Click **Set** to save the new assigned type.

## Using shortcuts in chats

Note: If you are on a Chat + Support account with the Agent Workspace enabled, see [Serving chats in the Agent Workspace: Using shortcuts in
chats](https://support.zendesk.com/hc/en-us/articles/4408824439194#topic_kd5_klb_x3b) for information on applying shortcuts.

Shortcuts are entered into a chat by the agent, who either begins typing the abbreviated
shortcut text, or entering a slash. If the agent enters only a slash (/), the first 10
shortcuts appear. You can filter the displayed shortcuts by typing in more of the shortcut
name.

Agents and admins will see:

- Their personal shortcuts
- Department shortcuts shared with the departments they belong to
- Global shortcuts

**To use a shortcut in a chat**

1. In a chat, start typing a shortcut, or type a slash (/) to view all shortcuts. The
   matching shortcut options appear, like in the example below:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shortcuts_insert.png)

   Personal and department shortcuts are
   labeled as such.
2. Highlight the shortcut you want to insert either by clicking it or by pressing the down
   arrow and then **Enter**.
3. The complete shortcut appears. If your shortcut includes options, they appear with radio
   buttons when you send the chat.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zopim_shortcut3.png)