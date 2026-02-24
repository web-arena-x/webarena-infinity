# Invite members

Invite and manage members of your workspace.

![Linear app settings page showing the Manage members settings](https://webassets.linear.app/images/ornj730p/production/24df0e4ada358c601233c729518f9d91c04b5663-2160x1327.png?q=95&auto=format&dpr=2)

## Send an invitation

To send an invitation:

1. Go to the [Settings > Administration > Members](https://linear.app/settings/members)
2. Click the **Invite** button.
3. Enter the invitee(s) email address. To add multiple invitees, separate each email by commas.
4. Under **Invite as...**, select the role you want the invitee(s) to have when joining the workspace (_paid plans_)
5. You can select the team(s) you want your invitee(s) to automatically join.
6. Click **Send invites**. New members will receive an invite link via email along with steps to join the workspace.

> [!NOTE]
> In case an email server is filtering out invitation emails, we recommend adding notifications@linear.app and/or pm_bounces@pm-bounces.linear.app to your allowlist as trusted senders in email settings.

### Email Options by Plan

#### Free plan

All members of a workspace on the Free plan are considered an Admin, thus anyone can send invitations to new members.

#### Paid plans

By default, only Admins can invite members on paid plans. Admins can allow all users to invite members by toggling on **Allow users to send invites** within [Settings > Workspace > Security](https://linear.app/settings/security).

#### Enterprise (SAML & SCIM)

For [SAML-enabled workspaces](https://linear.app/docs/saml-and-access-control), ensure that members are given access in your identity provider (IdP) before inviting them, depending on your login requirements.

Users who have access to Linear through your IdP may login to the workspace without needing an invitation. If no account existed for this user before, one will be created through Just-In-Time (JIT) provisioning. The user will show up as a member in Linear from this point on.

Reach out to [support@linear.app](mailto:support@linear.app) if a new user's email does not match other emails in your workspace, as it will have to be added to the SAML configuration as an approved domain.

When [SCIM](https://linear.app/docs/scim) is enabled for your workspace, you can no longer manually invite users from the Linear members page.

> [!NOTE]
> Learn how [adding](https://linear.app/docs/billing-and-plans?collapsible=b6d516b44aa5) or [removing](https://linear.app/docs/billing-and-plans?collapsible=24c14a946d42) users affects billing.

## Approved email domains

![Approved email domains](https://webassets.linear.app/images/ornj730p/production/68acab16d4f74f4a6c694d2f6f934fe544c41699-1392x296.png?q=95&auto=format&dpr=2)

To save time from manually inviting new members, Admins can navigate to [ Settings > Administration > Security](https://linear.app/settings/security) and add allowed email domains. Once set up, anyone with the matching email domain can join the workspace without an invitation or approval. This is only designed to streamline the joining process and does not prevent users from creating new workspaces with that domain email.

Users who are creating new accounts will see a prompt to join the workspace during the onboarding flow.

For members with existing accounts, click on your current workspace icon, hover over **Switch workspace**, select **Create or join a workspace**. The workspace with the allowed email domain should show up under available workspaces.

> [!NOTE]
> Please review this list regularly to ensure it is up to date. 
>   
> If you ever cancel your domain or transfer control of a domain to another organization, you'll need to remove this domain from your approved email domains in Linear to prevent unwanted access to the workspace.

## Invite links

Navigate to [Settings > Administration > Security](https://linear.app/settings/security) to generate a unique link that allows for anyone with the URL to join your workspace. If enabled, please ensure this link is only shared internally with your organization.

Invite links are persistent and reusable. They can be set to a new unique value with the "_Reset invite link_" button.

## Invite & Assign

Invited users can be assigned issues or marked as project leads before they accept their invitation.

* On any issue or project, open the assignee selection menu and choose _"Invite and assign…"._ After inviting them, search for them in assignee/lead menus to continue to allocate work.
* Or, when sending an invite from the workspace settings members page, click on the invited user and create new issues from their user page. These will automatically be assigned to them.

## FAQ

<details>
<summary>What happens to API tokens when a user is suspended or converted to a guest?</summary>
The API tokens will be revoked and invalidated.
</details>
