# Accessing and viewing the WFM User management page

Source: https://support.zendesk.com/hc/en-us/articles/7052274669338-Accessing-and-viewing-the-WFM-User-management-page

---

The User management page in Zendesk Workforce management (WFM) provides a central place for admins to view their team members’ information, such as their role, teams, assigned workstreams, and so on.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

The User management page lets you view and manage team member details like roles, teams, and workstreams. You can search, filter, and sort team members by name or status, and manually sync updates to reflect changes faster. This feature helps you efficiently organize and access team member information, ensuring your support operations run smoothly.

The User management page in Zendesk Workforce management (WFM) provides a central place for admins to view their team members’ information, such as their role, teams, assigned workstreams, and so on.

A WFM user profile is different from a [Zendesk user profile](https://support.zendesk.com/hc/en-us/articles/4408835022490). In a WFM user profile, you can [view team member information](#topic_twr_4xy_1bc) such as their name, email address, time zone and current WFM account access status (active or inactive).
Specifically, from the WFM User management page, you can [search for team members](#topic_gb2_kcr_tbc), [export the list](https://support.zendesk.com/hc/en-us/articles/7446311222042), and [refresh your list of team members](#topic_ych_1zy_1bc). You can also [add and remove users from teams](https://support.zendesk.com/hc/en-us/articles/9226702189082), [add and remove users from workstreams](https://support.zendesk.com/hc/en-us/articles/9822760145818), and [edit team members' tracking settings](https://support.zendesk.com/hc/en-us/articles/7446325512730) individually or in bulk.

You can control access to Zendesk WFM through an allow or block list.
See [Managing user access in your WFM account](https://support.zendesk.com/hc/en-us/articles/6443374452250).

This article contains the following topics:

- [Viewing team member WFM information](#topic_twr_4xy_1bc)
- [Finding WFM team members](#topic_gb2_kcr_tbc)
- [Refreshing the team members list](#topic_ych_1zy_1bc)

## Viewing team member WFM information

From the User management page in Zendesk WFM, you can view details about all the team members in your account and search for specific team members.

**To access the User management page**

- In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
 **Settings** in the navigation bar, then select **User management**.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_usermgmt_access.png)

### Team member information

The following table describes the information you can view about users in your account.

Information on this page can be viewed only, not edited. To edit a team member's information, such as their Zendesk user profile or their WFM role, refer to the corresponding column in the table below for more information. To edit a team member's WFM profile, see [Editing WFM team member profiles](https://support.zendesk.com/hc/en-us/articles/7446325512730).

| Column | Description |
| --- | --- |
| Team member | The team member’s full name and primary email address. See [Editing team member user profiles](https://support.zendesk.com/hc/en-us/articles/4408832485914). |
| Role | The user’s WFM role. For example, Admin, Agent, or any custom role created in your account. See [Understanding WFM roles and permissions](https://support.zendesk.com/hc/en-us/articles/6443374440090). |
| Zendesk default group | The user’s default group. A user’s default group is different from your Zendesk account’s default group. See [About default groups](https://support.zendesk.com/hc/en-us/articles/4408828237722). |
| Teams | The WFM teams to which the user is assigned. Users can belong to more than one team. See [Setting up teams in Zendesk WFM](https://support.zendesk.com/hc/en-us/articles/6443329411994). |
| Workstreams | The workstreams to which the user is assigned. Users can be assigned to multiple workstreams. See [About Zendesk WFM workstreams](https://support.zendesk.com/hc/en-us/articles/6443314489242). |
| Location | The user’s assigned location. A user can only be assigned to one location. See [Setting up locations and shifts](https://support.zendesk.com/hc/en-us/articles/6443345205402). |
| Shift | The shift the agent is assigned to. See [Setting up locations and shifts](https://support.zendesk.com/hc/en-us/articles/6443345205402). |
| Status | The user’s status in your WFM account can be either active or inactive. This status is controlled by your allow and block lists. The inactive status reflects users who are still [active in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408843830938) but not in WFM, based on the allow and block lists. See [Managing user access](https://support.zendesk.com/hc/en-us/articles/6443374452250). [Suspended agents in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408888690842#topic_zfr_vq5_w2b) aren't visible on the WFM team members page. |

## Finding WFM team members

You can [search](#topic_a2w_qdr_tbc) the list of WFM team members by name or email address. You can also [filter](#topic_i41_zdr_tbc) the list, such as by role or workstream, and [sort](#topic_qfx_kgr_tbc) by name and status to quickly find a team member.

### Searching for WFM team members

Searching by name or email address is the quickest way to find a team member. You can search the whole list, or you can filter the list and search only the filtered results.

**To search for team members**

1. [Access](#topic_twr_4xy_1bc) the User management page.
2. Enter a team member’s name, partial name, or email address in the search bar.

### Filtering the list of WFM team members

You can filter the list by any of the columns, except for the team member column.

1. [Access](#topic_twr_4xy_1bc) the User management page.
2. Click **Filter**.
3. In the Filter menu, click a column you want to filter by and then select options for the column. Note that you can filter by more than one column at a time.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_user_mgmt_filter.png)

   For example, you may want to filter the list by your Tickets and Chats workstreams for all team members with an Active status.

### Sorting the list of WFM team members

Filtering doesn't change the order of the list. You can sort the list by team member name and status in both ascending and descending order.

**To sort the list of team members**

1. [Access](#topic_twr_4xy_1bc) the User management page.
2. To sort the list by name, click the **Team member** column to sort the list alphabetically in ascending (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon-sort-path-up.png)) or descending order (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon-sort-path-down.png)).
3. To sort the list by status, click the **Status** column to sort the list by active (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon-sort-path-up.png)) or inactive (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon-sort-path-down.png)) status.

## Refreshing the team members list

When you [add new agents and admins](https://support.zendesk.com/hc/en-us/articles/4408886939930) to your Zendesk account, they’re automatically synced to your WFM account every 12 hours. Any changes you make to existing team members in your Zendesk account are also synced to your WFM account in 12 hours.

If you’d like your new team members and changes to appear in your WFM account sooner, you can manually sync them.

**To manually sync team members**

1. [Access](#topic_twr_4xy_1bc) the User management page.
2. In the upper-right corner, click the **Resync Agent List** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_user_mgmt_resync_icon.png)).

   The process may take a few moments.