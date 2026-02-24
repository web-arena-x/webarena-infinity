# Manage users in Workpapers

Source: https://central.xero.com/s/article/User-roles-in-Workpapers

---

## Overview

- Add a user to Workpapers and assign them a role.
- Update a user's details or change their Workpapers user role.

Tip

Workpapers is currently in beta and is available to selected practices. We’ve renamed our original solution classic Workpapers.

About user roles in Workpapers

Workpapers (beta) Classic Workpapers

When you set up Workpapers, the master administrator is the only user to have access by default. You can assign practice staff access to Workpapers during the set up process, or manage their access in Practice Manager from each staff member’s **Permissions** tab. You need [manage staff permissions](About-staff-privileges-in-Practice-Manager.md) to manage staff access to Workpapers.

You can assign users the following roles in Workpapers:

- **No access** – The user has no access to Workpapers.
- **Preparer** – The user can only create and prepare workpapers. They can't complete a pack or access workpaper settings.
- **Reviewer** – The user can create, prepare and review workpapers, and complete a workpaper pack. They can't access workpaper settings.
- **Admin** – The user can create, prepare and review workpapers, and control workpaper settings for the practice.

If you remove a user from Workpapers, they're still assigned to any workpapers they worked on, but they can’t access them or be assigned to any new ones.

You can assign users to the following roles:

- **None** – Use this role when you don't want a user to access classic Workpapers. Their name still appears against workpapers they’re assigned to.
- **Standard** – Standard users can only see workpaper packs they are assigned.
- **Manager** – Managers can only see and approve workpaper packs assigned to them. Managers can also assign users to a workpaper pack.
- **Partner** – Partners can see all workpaper packs and can approve workpaper packs they've been assigned to. They can assign users to a workpaper pack and delete workpaper packs.
- **Practice admin** – Practice admin users can see all workpaper packs and can approve and delete workpaper packs. They can assign users to a workpaper pack.

| **Role comparison** | **None** | **Standard** | **Manager** | **Partner** | **Practice Admin** |
| --- | --- | --- | --- | --- | --- |
| No access to workpaper packs | **✔** | - | - | - | - |
| Practice Settings | - | - | - | - | **✔** |
| Connect to Practice Manager | - | - | - | - | **✔** |
| Add and edit queries at Practice Level | - | - | - | - | **✔** |
| Add users | - | - | - | **✔** | **✔** |
| Partner review | - | - | - | **✔** | **✔** |
| Add and edit workpaper packs | - | **✔** | **✔** | **✔** | **✔** |
| Re-assign workpaper pack | - | - | **✔** | **✔** | **✔** |
| Unarchive workpaper pack | - | - | **✔** | **✔** | **✔** |
| Manager review | - | - | **✔** | **✔** | **✔** |
| Change materiality on workpapers | - | **✔** \* | **✔** | **✔** | **✔** |
| Add and edit queries within workpaper pack | - | **✔** | **✔** | **✔** | **✔** |
| Bulk send client queries | - | - | - | **✔** | **✔** |
| Send queries and management letter to client | - | **✔** | **✔** | **✔** | **✔** |
| Create journals | - | **✔** | **✔** | **✔** | **✔** |
| Link workpaper pack to Xero account for import | - | **✔** | **✔** | **✔** | **✔** |
| PDF and ZIP workpaper pack | - | **✔** | **✔** | **✔** | **✔** |
| Archive workpaper pack | - | **✔** | **✔** | **✔** | **✔** |

\* A standard user can only change the materiality settings if they are set as the manager or partner on the workpaper pack.

Add a user to Workpapers

Workpapers (beta) Classic Workpapers

To add a staff member to Workpapers, you need to add them as staff in Practice Manager, then assign them a Workpapers user role.

1. In Practice Manager, in the **Business** menu, select **Staff**.
2. Invite a new staff member, or click the name of the staff member you want to add to Workpapers.
3. Select the **Permissions** tab.
4. On the **General** tab, under **Workpapers role**, select the user role you want to assign them.
5. Click **Save**.

1. In classic Workpapers, select the **Settings** tab,
2. Under **General**, click **Users**.
3. Click **New User**, then enter the user's details and select their role.
4. Click **Send Invite**.
5. (Optional) Click **Choose File** in the **Attach Signature** screen to upload an image of the user's signature.
6. Click **Close**.

Until the user accepts the invitation, their status shows as **Pending**. To resend the invitation, click the pending user, then click **Resend Invite**.

Edit a user's details

Workpapers (beta) Classic Workpapers

To change the user role assigned to a staff member or edit their details, you need to edit the staff member’s record in Practice Manager.

1. In Practice Manager, in the **Business** menu, select **Staff**.
2. Click the name of the staff member you want to edit.
3. (Optional) Select the **Information** tab to update their contact details, financials and performance information or custom task or historic rates, or to enter a note.
4. Select the **Permissions** tab.
5. On the **General** tab, under **Workpapers role**, select the user role you want to assign them.
6. Click **Save**.

1. In classic Workpapers, select the **Settings** tab.
2. Under **General**, click **Users**.
3. Click the user's name, then update their details.
4. Click **Save**.

Delete a user

Workpapers (beta) Classic Workpapers

To remove a staff member from Workpapers, you need to change their Workpapers permission in Practice Manager to **No access**. When you do this, they no longer show up as an option to select as a preparer, reviewer or final reviewer in Workpapers.

To remove a user from Workpapers:

1. In Practice Manager, in the **Business** menu, select **Staff**.
2. Click the name of the staff member you want to remove Workpapers access for.
3. Select the **Permissions** tab.
4. On the **General** tab, under **Workpapers role**, select **No access**.
5. Click **Save**.

If a staff member has left your practice, you can [remove them from your practice](/s/article/Disable-and-delete-staff-accounts?userregion=true). This also removes their access to Workpapers.

1. In classic Workpapers, select the **Settings** tab
2. Under **General**, click **Users**.
3. Click the user's name.
4. Click **Delete**, then click **Delete** to confirm.

Deleting a user doesn’t affect any workpapers they’re assigned to.

## What's next?

In Workpapers, [assign the new user to a workpaper or workpaper pack](Assign-a-user-to-a-workpaper-or-pack.md).

In classic Workpapers, once a user has accepted their invitation, you can [set up email notifications](Email-notifications.md) for them.