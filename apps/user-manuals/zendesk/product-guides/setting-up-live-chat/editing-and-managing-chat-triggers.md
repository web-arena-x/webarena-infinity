# Editing and managing chat triggers

Source: https://support.zendesk.com/hc/en-us/articles/8554265015322-Editing-and-managing-chat-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Admins can create chat triggers to automate actions when certain conditions are met for
live chat interactions with end users. This article describes how to edit and manage
chat triggers after they've been [created](https://support.zendesk.com/hc/en-us/articles/4408884148762).

This article contains the following topics:

- [Editing chat triggers](#topic_f5j_pst_rdc)
- [Duplicating chat triggers](#topic_iff_wkh_3kb)
- [Testing chat triggers](#topic_mhh_xvd_tdc)
- [Deactivating chat triggers](#topic_tnp_czx_zhb)
- [Activating chat triggers](#topic_usf_bdp_sdc)
- [Deleting chat triggers](#topic_nf5_czx_zhb)

## Editing chat triggers

Chat triggers can be modified as needed to meet your business needs.

**To edit a chat trigger**

1. On your Chat dashboard, go to **Settings** > **Triggers**.
2. From the list, click the row of the trigger you want to edit.
3. Modify the values as needed.
4. Click **Save changes**.

## Duplicating chat triggers

If you want to duplicate an existing chat trigger to use as a template for creating
new triggers, you need to copy the trigger's developer code, then create a new
trigger using the copied code.

**To copy the developer code for a chat trigger**

1. On your Chat dashboard, go to **Settings** > **Triggers**.
2. From the list, click the trigger you want to copy.
3. Click the **Developer** button on the top right and copy the code you see
   on the box:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_trigger_developer_code.png)
4. Click **Cancel**.

**To create the new chat trigger using the copied code**

1. Return to the trigger list page and click **Add Trigger**.
2. Click the **Developer** button again.
3. Replace the code in the Customize trigger box with the code you copied.
4. Update the code as needed. Click the **Visual** button to see the changes
   before saving them.
5. Click **Save changes**.

## Testing chat triggers

Chat triggers depend on caching data, IP addresses, user data, and more. Therefore,
testing chat triggers isn't as simple as testing from a new tab in your browser.
Instead, to perform an accurate test, you must successfully imitate a visitor and
stage your account properly.

**To imitate a visitor in chat**

- Use the **Simulate visitor** option in the Visitors page in the Chat
  dashboard.

  ![](https://support.zendesk.com/hc/article_attachments/8567411011994)

  OR
- Manually imitate a visitor using the following best practices:
  - Use a private browsing window, such as an incognito window in Chrome
    to ensure caching data in your main browser doesn't interfere with
    your testing.
  - If your trigger includes a condition that checks for previous
    visits, [clearing your cache and
    cookies](https://support.zendesk.com/hc/en-us/articles/4408823836314) can also help.
  - If you're testing a trigger with location-based conditions, make
    sure you're testing from the correct location. Check that your
    browser matches the correct location so that the trigger can fire.
    See [How does Zendesk capture the
    location of the end user?](https://support.zendesk.com/hc/en-us/articles/4408827583898)

**To stage your account**

- Ensure your account, agents, and departments have the correct statuses to
  align with your trigger conditions. For example:
  - To test department routing, at least one agent from that department
    must be logged in to the Chat dashboard with a status of online. See
    [Creating agents and departments
    in Chat](https://support.zendesk.com/hc/en-us/articles/4408894143898).
  - To test triggers that fire when the account is offline, all agents
    must be logged out of the Chat dashboard or have a status of
    invisible.

## Deactivating chat triggers

If you want a chat trigger to stop running but do not want to delete it, you can
simply deactivate it. Deactivated triggers can be re-activated at any time.

**To deactivate a chat trigger**

1. From the Chat dashboard, click **Settings > Triggers**.
2. Click the row of the trigger you want to disable.
3. Next to **Trigger status**, select **Disable trigger**.
4. Click **Save changes**.

   On the Triggers settings page, the check mark
   is removed from the Enabled column.
5. To re-enable a disabled trigger, click the trigger you want to enable, then
   click **Enabled**.

## Activating chat triggers

Deactivated chat triggers can be re-activated at any time.

**To activate a chat trigger**

1. From the Chat dashboard, click **Settings > Triggers**.
2. Click the row of the trigger you want to disable.
3. Next to **Trigger status**, select **Enable trigger**.
4. Click **Save changes**.

## Deleting chat triggers

When a chat trigger is no longer needed, you can delete them from the Triggers
settings page. Deleted triggers cannot be recovered.

**To delete a chat trigger**

1. From the Chat dashboard, click **Settings > Triggers**.
2. Click the checkbox to the left of the trigger you want to delete. To select
   all triggers, click the checkbox to the left of the Name heading.
3. Click **Delete selected** at the top of the page.
4. Confirm that you want to delete the trigger. The trigger is removed from the
   Triggers list.