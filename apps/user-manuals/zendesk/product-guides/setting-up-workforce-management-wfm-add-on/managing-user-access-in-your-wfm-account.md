# Managing user access in your WFM account

Source: https://support.zendesk.com/hc/en-us/articles/6443374452250-Managing-user-access-in-your-WFM-account

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Manage user access in your WFM account using allow and block lists. The allow list lets you specify who can access and have their activities tracked, while the block list restricts access. You can automatically add new team members to the allow list or manually manage entries. Remember, you can only use one list at a time to control access.

Users are automatically added to Zendesk Workforce management (WFM) when they’re added to your Zendesk account. See [Understanding WFM roles and permissions](https://support.zendesk.com/hc/en-us/articles/6443374440090).

As an admin, you can manage user access to WFM by using the allow and block lists.
These lists allow you to maintain a known list of users who either have access or are restricted from your WFM account.

This article contains the following sections:

- [Controlling user access with the allow list](#topic_fhg_2kk_1bc)
- [Restricting access with the block list](#topic_vjp_skk_1bc)

Related articles

- [Managing Zendesk WFM account settings](https://support.zendesk.com/hc/en-us/articles/6443329207834)

## Controlling user access with the allow list

When you turn on the allow list and add users to it, only the users you specify can access Zendesk WFM and have their [activities tracked](https://support.zendesk.com/hc/en-us/articles/6443347506970). New team members added to your Zendesk account with the [Staff member](https://support.zendesk.com/hc/en-us/articles/4944849237658) user type will be added to the allow list on the next sync or on the next [manual sync](https://support.zendesk.com/hc/en-us/articles/7052274669338#topic_ych_1zy_1bc), unless you deselect the option to automatically add new team members.

Even when you control user access to WFM with the allow list, you’re still billed for all agents in your Zendesk account. See [Buying Zendesk workforce management](https://support.zendesk.com/hc/en-us/articles/6851584037146).

**To control user access with the allow list**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Account settings**.
2. Click the **Access control** tab.
3. Turn the **Allow list** toggle to the on position.

   Note: You can use either the allow list or block list; both can’t be used at the same time.
4. Enter the email addresses of the users you want to grant access to Zendesk WFM, one per line. The emails you enter must exactly match those listed on the agents' profiles.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_allow_list.png)
5. (Optional) Select or deselect the **Automatically add new team members** option:
   - When selected, new users added to your Zendesk account with the [Staff member](https://support.zendesk.com/hc/en-us/articles/4944849237658) user type will be added to the allow list during the next sync, which occurs within 12 hours or on the next [manual sync](https://support.zendesk.com/hc/en-us/articles/7052274669338#topic_ych_1zy_1bc).
   - When deselected, new team members will not be added to the allow list during the next sync.

     Note: If you deselect and later select this option again, only users added to your Zendesk account from that point forward will be automatically added to the allow list during the next sync. Existing team members with the [Staff member](https://support.zendesk.com/hc/en-us/articles/4944849237658) user type who are not yet on the list must be added manually.
6. Click **Save**.

## Restricting access with the block list

Use the block list to restrict users from accessing Zendesk WFM and having their activities tracked.

When you [downgrade a user in Zendesk](https://support.zendesk.com/hc/en-us/articles/4408888690842), the user is also removed from your WFM account and you don’t need to add them to the block list.

**To restrict user access with the block list**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Account settings**.
2. Click the **Access control** tab.
3. Turn the **Block list** toggle to the on position.

   Note: You can use either the allow list or block list; both can’t be used at the same time.
4. Enter the email addresses of the users who you want to restrict from using Zendesk WFM.
   The emails you enter must exactly match those listed on the agents' profiles.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_settings_block_list.png)
5. Click **Save**.