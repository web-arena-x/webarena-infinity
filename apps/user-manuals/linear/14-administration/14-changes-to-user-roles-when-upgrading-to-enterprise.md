# Changes to user roles when upgrading to Enterprise

If your existing workspace upgrades from any other plan to the Enterprise plan:

* All current admins are automatically upgraded to workspace owners
* The new, limited workspace admin role becomes available
* Regular members and guest users remain unchanged

Workspace owners can now assign users to the new admin role as needed.

## **Migrating from admins to owners with SCIM**

If your workspace has SCIM enabled and is currently managing permissions via `linear-admins`:

* The group will now control workspace owners, not admins
* All users in `linear-admins` will become owners
* The group name itself will not change automatically

If you want to start managing admins as well, you can do one of the following:

> [!NOTE]
> If you've renamed your admins management group to something other than `linear-admins`, these steps still apply. When following the steps, ensure that any renamed or newly created groups use the exact `linear-admins` and `linear-owners` identifiers.
> 
> Once the groups are properly syncing, their names can be changed.

### **Option 1: Rename the admins group**

> [!NOTE]
> Only use this option if your Identity Provider supports syncing group name changes, e.g., via Okta’s _“Rename app groups to match group name in Okta”_ setting.
> 
> If your IdP does _not_ support this—or you'd prefer not to enable this setting—skip ahead to the second option.

1. Rename the `linear-admins` group to `linear-owners` in your IdP
2. Create a new `linear-admins` group and push it to Linear
3. Move users who should be admins from `linear-owners` into the new `linear-admins` group

### **Option 2: Re-link the admins group**

> [!NOTE]
> Use this option if your IdP does _not_ support syncing group name updates

1. Create a new group called `linear-owners`
2. In the Linear [security settings](https://linear.app/settings/authentication), unlink the existing `linear-admins` group
3. Move intended owners from the old `linear-admins` group into the new `linear-owners` group
4. Push both `linear-admins` and `linear-owners` groups to Linear



<details>
<summary>What permission will a user get if they are in both admin and owner groups in SCIM?</summary>
If a user is in two groups, they will get the permission of the most recent group that was pushed.
</details>
