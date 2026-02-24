# Workspace Owner

The workspace owner role has full administrative access, while the Admin role becomes more restricted. Use the new Admin role to allow updating most routine settings without granting access to billing or security configurations.

## Basics

When switching to the Enterprise plan, all existing admins will automatically be switched to workspace owners. A new, limited admin role will be available for use. No changes will occur to Member or Guest roles.

Using the now limited admin role, workspace owners can allow a greater number of admins to handle routine tasks like managing public teams, without increasing the number of people with access to your workspace's most sensitive settings.

Workspace owners can manage which roles have access to workspace-level actions through _[Settings > Administration > Security](https://linear.app/settings/security)_ under the "Workspace restrictions" section.

![Workspace restrictions](https://webassets.linear.app/images/ornj730p/production/61a69e79dac9ced08c3e28a656c9cdd7a40585cb-1366x1080.png?q=95&auto=format&dpr=2)

## Permissions by role

Legend:

✅ Available

❌ Unavailable

🟨 Available by default, but can be restricted in security settings

🟣 Admins can only manage team settings for public teams or private teams they are a member of

**Action** | **Workspace Owner** | **Admin** --- | --- | --- **Workspace configuration** | | Change workspace name, icon, enable/disable features at workspace level | ✅ | ❌ Delete workspace | ✅ | ❌ Restrict workspace creation | ✅ | ❌ **Security & compliance** | | Manage security settings | ✅ | ❌ View audit log | ✅ | ❌ Manage OAuth app approvals | ✅ | ❌ **User & access management** | | Invite users | ✅ | 🟨 Promote or demote members to admin | ✅ | ✅ Promote or demote admins to owners | ✅ | ❌ **Team management** | | Create and delete teams | ✅ | ✅ Manage all public teams | ✅ | ✅ Manage all private teams | ✅ | 🟣 Manage Triage Rules | ✅ | 🟣 **Integrations and API** | | Enable and disconnect integrations | ✅ | ✅ Manage API settings | ✅ | 🟨 Create webhooks | ✅ | 🟨 Create OAuth apps | ✅ | 🟨 **Workflows** | | Manage Labels | ✅ | 🟨 Manage Project Statuses | ✅ | ✅ Manage SLA settings | ✅ | ✅ Manage AI settings | ✅ | ✅ Manage Customer Requests | ✅ | ✅ **Data & billing** | | Billing | ✅ | ❌ Workspace imports | ✅ | 🟨 Workspace exports | ✅ | ❌

## Managing admin and owner roles with SCIM

### Migrating from admins to owners

If your workspace has SCIM enabled and is currently managing permissions via `linear-admins`, your `linear-admins` group will automatically be updated to manage _owners_, not _admins._ This means that all users in `linear-admins` will become owners, however the name of the group will not change automatically.

If you now want to additionally start managing admins, you have two options:

#### Rename the admins group

To rename the `linear-admins` group, you'll first need to make sure your IdP supports syncing group name changes to connected apps. For example, in Okta, this can be configured using the "Rename app groups to match group name in Okta" setting.

If your IdP does _not_ support this—or you'd prefer not to enable this setting—skip ahead to [Re-link the admins group](https://linear.app/docs/workspace-owner#re-link-the-admins-group).

If syncing group name changes _is_ supported, follow these steps:

1. Rename the `linear-admins` group to `linear-owners`.
2. Create a new `linear-admins` group in your IdP and push it to Linear.
3. Move all desired admin users from the `linear-owners` group into the new `linear-admins` group.

#### Re-link the admins group

If your IdP does not support syncing group name changes, you can re-link groups instead:

1. Create a new group called `linear-owners`.
2. Unlink the existing `linear-admins` group from Linear in your IdP.
3. Move all desired owners from the old `linear-admins` group into the new `linear-owners` group.
4. Push the new `linear-admins` and `linear-owners` groups to Linear.



### Starting fresh

If you're starting fresh with SCIM, you'll need to create a `linear-owners` group to manage owners, in addition to the groups described [here](https://linear.app/docs/scim#provisioning-roles).

## FAQ

<details>
<summary>What permission will a user get if they are in both admin and owner groups in SCIM?</summary>
If a user is in two groups, they will get the permission of the most recent group that was pushed.
</details>
