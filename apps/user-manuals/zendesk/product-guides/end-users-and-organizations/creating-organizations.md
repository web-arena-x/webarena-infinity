# Creating organizations

Source: https://support.zendesk.com/hc/en-us/articles/4408882246298-Creating-organizations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Create and manage organizations to group users and streamline support operations. You can set up user mapping based on email domains, assign tickets to specific groups, and establish shared organizations for ticket visibility. This feature allows you to organize users effectively, automate ticket assignments, and control access to tickets, enhancing your team's workflow and customer support capabilities.

Location: 
In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Organizations** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/organizations_icon.png)) in the sidebar.

Organizations are typically collections of your end users, but they can also include agents.
Your account starts with a single, default organization that has the same name as your account and contains all your users.

Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can create and edit organizations. How you set up your organizations depends on how you want to define your workflow and organize your users. See [About organizations and groups](https://support.zendesk.com/hc/en-us/articles/4408886146842).

On Team plans, users can belong to only one organization. On all other plans, users can belong to up to 300 organizations. However, a user does not have to belong to any organization.

Topics covered in this article:

- [Creating organizations](#topic_1yx_452_ck)
- [Automatically adding users to organizations based on their email domain](#topic_nxl_vdt_bc)
- [Mapping a group to an organization](#topic_cfj_gfn_bc)
- [Setting up a shared organization for end users](#topic_nat_vgn_bc)

## Creating organizations

Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882-Creating-custom-roles-and-assigning-agents-Enterprise-) can create organizations.

The following video gives you an overview of how to create an organization:

Creating organizations [1:01]

**To create an organization**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Organizations** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/organizations_icon.png)) in the sidebar.
2. Click **Add organization**. Alternatively, hover over the **+Add** tab in the top toolbar, then select **Organization**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_buttons_support_3.png)
3. Enter a unique **Name** for the organization.

   Note: Don't include a pipe (|) character in the organization name. If you do, the organization won't be created.
4. If you want to set up user mapping, in **Domains**, enter one or more email domains, separated with spaces (for example, organization1.com organization2.com).

   With user mapping, users from the specified email domains are automatically added to this org when they submit a request for the first time or register. If you add a domain that is already mapped to another org, users are mapped to the first organization alphabetically.
5. Click **Save**.

   You can add additional information after clicking **Save**.
6. Optionally, enter **Tags**.

   See [Adding tags to users and organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658).
7. If you want to set up group mapping, select a **Group**.

   When you set up group mapping, an organization's tickets are automatically assigned to the specified group.
8. For **Users**, determine ticket access for tickets in the help center customer portal.

   Important: There are organization access settings in the user profile and in the org itself. If the settings are in conflict, the more permissive setting overrides the less permissive setting.

   Ticket access options include:

   - **Can view own tickets only**: users in this org can view and edit their own tickets only.

     Note: If you chose this setting, but the access setting in the user's profile or custom role gives the user access to all org tickets, this org setting *will be overridden* by the user setting.
   - **Can view all org tickets**: users in this org can view all org tickets. This is referred to as a *shared organization* For this setting, determine whether users can also comment on org tickets.

     Note: If you chose this setting, and the access setting in the user's profile or custom role restricts access for users in the org to their own tickets only, this org setting *will override* the user setting.
9. Enter any **Details** or **Notes** you want.

   The new organization is saved automatically.

If you want to add further information to your organization than the default fields contain, see [Adding custom fields to organizations](https://support.zendesk.com/hc/en-us/articles/4408842677786).

## Automatically adding users to organizations based on their email domain

Users can be automatically added to an organization based on their email domain when they submit a request for the first time or register. This is referred to as *user mapping*.
An administrator can set this up by editing an organization's settings.

Generally, a user must verify their email address before they are automatically added to an organization. However, an unverified user can be mapped to an organization *if* their profile is created at the same time as their first ticket and the ticket is created either via email or chat.

**Important considerations:**

- If a user with an unverified email address from the specified domain submitted a ticket before user mapping was configured, you must manually add them to the organization. They won't be added automatically. Users with verified email addresses will be added automatically to the organization when the user mapping is created.
- If you add a domain to an organization that is already mapped to another organization:
 - New users are automatically mapped to the first organization (sorted alphabetically by name) only. This is true even if you [allow users to belong to multiple organizations](https://support.zendesk.com/hc/en-us/articles/4408838140314).
 - If you allow users to belong to multiple organizations, existing users will be added to the new organization with the shared domain (this change may not be visible immediately). They will not lose their existing organizations.
 - The email domain is automatically included in the allowlist.

    If you've added email domains to the allowlist (see [Setting your allowlist and blocklist to control email support requests](https://support.zendesk.com/hc/en-us/articles/4408886840986)), these domains will be automatically included in the list.
    Although allowed domains are included, they are not shown on this organization settings page.
- Removing the domain mapping from the organization also removes the organization from all users who were mapped to the domain.

**To set up user mapping for an organization**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Organizations** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/organizations_icon.png)) in the sidebar.
2. Find the organization you want to edit and click on the organization's name.
3. On the organization's detailed view, enter the email domain(s) (separated by a space)
   in the **Domains** field to set up user mapping.

   Your update is saved automatically, so when you are finished you can simply navigate away. A user must then verify the email address for it to be added.

## Mapping a group to an organization

An organization's tickets can be automatically assigned to a group. This is referred to as *group mapping* and can be set up by an administrator.

**To set up group mapping for an organization**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Organizations** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/organizations_icon.png)) in the sidebar.
2. Find the organization you want to edit and click on the organization's name.
3. On the organization's detailed view, select a **Group** from the drop-down list to set up group mapping.

   Your update is saved automatically, so when you are finished you can simply navigate away.

New tickets will now automatically be assigned to the selected group; however, business rules and agents may override this default group setting.

## Setting up a shared organization for end users

You have the option of allowing all of the end users in an organization to see each other's tickets. This is referred to as a *shared organization*. This can be set up by an administrator.

**To set up a shared organization**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Organizations** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/organizations_icon.png)) in the sidebar.
2. Find the organization you want and click the organization's name.
3. On the organization's detailed view, select **Can view all org tickets** in the **Users** field. Then, if you want to allow users to add comments to shared organization tickets, select **and add comments**.

   Important: This organization-wide setting overrides the user access setting in the user profile. Meaning that, even if you restrict a user in this org to view their own tickets only, they will be able to see all org tickets if the org access is set to view all org tickets.

   Your update is saved automatically, so when you are finished you can simply navigate away.

Alternatively, instead of allowing *all* end users in an organization to see an organization's tickets, you can grant this privilege to select end users. To do so, set the org to **Can view own tickets only**, then set individual users to **Can view all org tickets** in their user profiles. The user permission in that case overrides the organization-wide setting.