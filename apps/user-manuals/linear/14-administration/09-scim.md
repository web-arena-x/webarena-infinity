# SCIM

SCIM, or _System for Cross-domain Identity Management_ allows for the automation of user provisioning for your Linear workspace. 

> [!NOTE]
> Available to workspaces on our [Enterprise](https://linear.app/pricing) plan

![Security Settings page for SCIM in the Linear app](https://webassets.linear.app/images/ornj730p/production/de09045809402f74f116b880078a1b7b4b774bb4-2160x1326.png?q=95&auto=format&dpr=2)

## Overview

With SCIM enabled, user accounts can be automatically created, updated, and suspended based on your IDP settings—eliminating the need for manual account management in Linear. This integration helps ensure that your team's access stays in sync with your organization’s directory.

## Configure

### Enable and test

1. Navigate to [Settings > Administration > Security](https://linear.app/settings/security)_._
2. Under the "Authentication" section, click **Configure** next to "SAML & SCIM".
3. Toggle the option to enable SCIM
4. Click _"View configuration"_ to get your **SCIM base connector URL** and **Bearer Auth token.** Keep these values at hand as you will need them to configure SCIM in your Identity provider.

> [!NOTE]
> Once enabled, Admins will **not** be able to manage users from within Linear as they will be kept up to date through your identity provider.  
> If necessary, you can temporarily enable a manual override to allow user suspension. This may be useful if you need to remove members or Guests that were added to Linear before you enabled SCIM.

#### OneLogin

* In OneLogin's Admin panel > Applications, click _Add App_
* Search for the "SCIM Provisioner with SAML (SCIM v2 Enterprise, full SAML)" app and add
* Click on the _Configuration_ tab and add your SCIM base URL and Bearer token
* Click on the _Provisioning_ tab and Enable Provisioning
* Save your App

#### Okta

* In the Okta admin pages, open the Linear application you have for SAML 2.0
* In the _General_ tab, click _Edit_ and choose _SCIM_ in the Provisioning section and _Save_
* In the _Provisioning_ tab, enter the SCIM Base connector URL you generated from Linear
* For the _Unique identifier_ field for users section enter **email**
* For _Supported provisioning actions_ you can enable "Import New Users and Profile Updates", "Push New Users" and "Push Profile Updates". Also select "Push Groups" if you are planning to sync selected Okta groups with Linear teams. "Import Groups" is optional, but can be selected to import existing Linear teams to be later linked to Okta groups.
* For _Authentication mode_ field, choose HTTP Header and enter your Bearer token generated from Linear. You can now test the configuration and save
* Lastly, return to the Provisioning tab in Okta and edit your settings under "To App" to enable the SCIM functionality needed for your Linear application (Create, Update and Deactivate users)

![Okta settings with provisioning options checked for Linear app](https://webassets.linear.app/images/ornj730p/production/d5c19b976eca09f26ecea5eea1d19c63c0b67a82-1076x902.png?q=95&auto=format&dpr=2)

## Group push

Linear's SCIM integration also supports group push. From your side all you have to do is start pushing groups from your Identity provider to Linear. These will then map 1:1 with teams in Linear.

  
To link an existing team to a Group, you first need to import teams from Linear. These teams will be recognized as groups by your Identity provider. Once imported, you can then select the appropriate team when configuring group push.  


Once a team is linked to a Group, this team's membership is solely managed through your identity provider and not in Linear directly.

If you choose to disconnect the Push group from Linear in the future, you may see different options offered by your IDP:

* Opting to delete the group on Linear's side will remove all members from the Linear team and convert the team to private. Issues will remain unchanged.
* Disconnecting the group without sending a delete request will leave the team unchanged and not sync any changes to the team on Linear's side. From the team **Settings > Danger Zone** you can then unlink SCIM manually to resume managing the team as normal. 

![Unlink from SCIM option in Linear team settings](https://webassets.linear.app/images/ornj730p/production/3c82a6bf3de2d2fdf814e9f9c721cb6c0f229d28-915x274.png?q=95&auto=format&dpr=2)

## Provisioning Roles

By default, all accounts created via SCIM via individual assignment or group push are provisioned as Members. You can also choose to provision specific users into Owner (if on an Enterprise plan), Admin and Guest roles directly from your IDP.

To do this, you need to create `linear-owners` (only if on an Enterprise plan), `linear-admins` and `linear-guests` as push groups on the IDP side and sync their members with Linear. 

Once these have been connected to Linear, any users added to the group will be given the corresponding role in Linear. 

* These particular groups do not create Teams in Linear or sync membership with existing teams.
* You can rename these groups from your IDP after you've pushed them at first as `linear-owners` (if applicable), `linear-admins` and `linear-guests`
* You will not be able to assign or edit admin or guest roles manually when this link is in place.

If your workspace already uses SCIM and is now migrating to an Enterprise plan for the first time, follow [this migration guide](https://linear.app/docs/changes-to-user-roles-when-upgrading-to-enterprise) to make sure both Owner and Admin roles get provisioned correctly going forward.

> [!NOTE]
> **Guest Exceptions**
> You may prefer to invite external Guests to your workspace manually, without adding them through your IDP.
> 
> The Invite menu in _Settings > Members_ will allow you to invite Guests only, even with SCIM enabled.
> 
> For Guests added before this was an option, you can use the ... menu on the Members page to unlink their account from your identity provider and manage them in Linear.

## SCIM Sync

Linear keeps the following user and team properties in Linear up to date in near real time when we receive SCIM updates from your IDP. 

**Users**

* **Email (`userName`):** primary identifier; must be a valid email. SCIM updates are accepted when the email domains are claimed by your workspace. 
* **Full Name:** resolved in order: `name.formatted` → `name.givenName + name.familyName` → `displayName`
* **Username/Nickname:** updated from `displayName`. Linear ensures uniqueness by appending a number when needed.
* **Active:**  `active: false` suspends the user; `active: true` unsuspends.
* **Avatar:** updated from `avatarUrl` or `photos[].value` 

**Teams**

* **Name (`displayName`):** updates the team name; uniqueness enforced with a suffix if needed (e.g., “Engineering (2)”).
* **Members (`members`):** add/replace/remove members to SCIM-managed teams via user references (`value` = user ID).

## Disabling SCIM

Once SCIM is disabled on Linear side:

* SCIM requests coming from your Identity provider will be rejected on Linear side.
* Any team that was linked to a Group will be unlinked.
* All SCIM restrictions will stop being enforced.

This does mean that if SCIM is re-enabled on Linear side, any changes or member removals that happened on your Identity provider will have to be pushed again to Linear. Refer to your Identity provider documentation for more information on accomplishing this.

If you need to remove some Linear accounts that are not part of your IDP, we recommend enabling the temporary override from your Linear SCIM settings, rather than disabling SCIM.   
  
You'll find the option for this at the bottom of your SCIM settings page and it will allow the Admin or Owner who toggles the setting to manually suspend users temporarily.  

![SCIM Manual overrides button with "Enable override" option](https://webassets.linear.app/images/ornj730p/production/e48d8a73d4a1ede5965682104bc1f5581966a1b4-2058x562.png?q=95&auto=format&dpr=2)

## FAQ

<details>
<summary>Can you set default public teams for users created through SCIM?</summary>
Yes, we support setting default public teams for SCIM provisioned users.
</details>

<details>
<summary>What identity providers do you support?</summary>
SCIM should work with most identity providers though we have only tested with Okta and OneLogin.
</details>

<details>
<summary>What version of SCIM do you use?</summary>
We support SCIM 2.0 (not SCIM 1.1.)
</details>

<details>
<summary>When do SCIM created users become billable seats?</summary>
As of August 14th 2025, SCIM-created users are billable only after they've logged on for the first time, not at time of creation.
</details>
