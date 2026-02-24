# Creating custom WFM roles and assigning users

Source: https://support.zendesk.com/hc/en-us/articles/6443314455834-Creating-custom-WFM-roles-and-assigning-users

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Create custom workforce management roles to align with your organization's structure by defining specific permissions and access for agents, team leads, and managers. Assign users to these roles to ensure they have the appropriate access to teams, locations, and workstreams. Note that users can only have one role at a time, and role changes are effective immediately upon assignment.

Admins can create custom workforce management (WFM) agent roles that reflect the unique
positions in your organization.

You can allow or restrict access in a way that reflects your organization's structure and
access management system. Create roles and specify different permissions for your agents, team
leads, admins, managers, or other roles.

This article contains the following topics:

- [Accessing the Roles and permissions
  page](#topic_bpy_wcc_1bc)
- [Creating custom WFM roles](#topic_pjj_tdc_1bc)
- [Assigning users to custom WFM
  roles](#topic_whf_52c_1bc)

Related articles

- [Understanding WFM roles and permissions](https://support.zendesk.com/hc/en-us/articles/6443374440090)
- [Managing WFM roles and permissions](https://support.zendesk.com/hc/en-us/articles/7037879703322)

## Accessing the Roles and permissions page

WFM admins can access the Roles and permissions page.

**To access the Roles and permissions page**

- In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
  **Settings** in the top bar, then select  **Roles and permissions**.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_roles_page_acess.png)

## Creating custom WFM roles

Before creating roles, you may want to align with other stakeholders in your organization
on what roles you’ll need. To learn more, see [Who uses Zendesk Workforce management and when](https://support.zendesk.com/hc/en-us/articles/6514644101914#topic_lml_wbx_c1c).

**To create custom WFM roles**

1. [Access](#topic_bpy_wcc_1bc) the Roles and permissions
   page.
2. Click the **Add Role** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_plus_icon.png)).
3. Enter a **Role name**, then click **Add role**.

   The new role appears in the All
   roles panel.
4. Define permissions by toggling them to the on position.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_roles_custom_define.png)

   Use the search box to quickly search for a
   permission.

   See [WFM permissions](https://support.zendesk.com/hc/en-us/articles/6443374440090#topic_zcx_t1c_1bc) for more information.
5. Click the **Scopes** tab.
6. Define the **Teams**, **Locations**, and **Worksteams** that users assigned to
   this role will have access to.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_roles_define_scopes.png)
7. Click **Save**.

   Next, [assign](#topic_whf_52c_1bc)
   users to the role.

## Assigning users to custom WFM roles

Users can be assigned to only one WFM role at a time. By default, all users are
automatically assigned to either the standard WFM admin or agent role depending on their
role in your Zendesk account. See [Standard WFM roles](https://support.zendesk.com/hc/en-us/articles/6443374440090#topic_ngj_b1c_1bc).

When you assign users to a new WFM role, the change takes effect immediately. Users will
see the change when they refresh their browsers or navigate to another page.

[Teams](https://support.zendesk.com/hc/en-us/articles/6443329411994), [Locations](https://support.zendesk.com/hc/en-us/articles/6443345205402) and [Workstreams](about-zendesk-wfm-workstreams.md#topic_br5_tjz_11c) created by users assigned to a custom
WFM role are automatically added to the scope of that role. This means that all users with
this custom role can also see and edit the new teams, locations, and workstreams.

For example, if a user with the "Manager" custom role creates the location "London", all
users with the "Manager" role will be able to see and edit that same “London” location.

Note: You cannot change your own role. To do so, you need to request assistance from another
user with admin permissions. This policy is in place to prevent the accidental loss of admin
privileges.

**To assign users to a custom
WFM role**

1. [Access](#topic_bpy_wcc_1bc) the Roles and permissions
   page.
2. Select the role to which you want to assign users.
3. Click the **Agents** tab.
4. Find the users you want to assign to the selected role.

   You can filter the list of
   agents by group, team, location, role, or view all users in your account. Or, use the
   search bar to find a specific agent.
5. Hover over the user’s default role and click **Reassign**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_roles_assign_user.png)
6. Continue to assign users to the role, then click **Save**.