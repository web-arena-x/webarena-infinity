# Manage access to your organization

Source: https://docs.stripe.com/get-started/account/orgs/team

---

Manage access to your organization

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Forgs%2Fteam)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Forgs%2Fteam)

[Get started](/get-started)

[Payments](/payments)

[Revenue](/revenue)

[Platforms and marketplaces](/connect)

[Money management](/money-management)

[Developer resources](/development)

APIs & SDKsHelp

[Overview](/get-started)[See all products](/products)

About the APIs

[Stripe glossary](/glossary)

Start building

Create an account

[Overview](/get-started/account)

[Activate your account](/get-started/account/activate)

[Add funds to your balance](/get-started/account/add-funds)

[Account checklist](/get-started/account/checklist)

[Acceptable verification documents](/acceptable-verification-documents)

Account structure

[Start a team](/get-started/account/teams)

[Organizations](/get-started/account/orgs)

[Build an organization](/get-started/account/orgs/build)

Manage access to your organization

[Manage SSO](/get-started/account/orgs/sso)

[Share customers and payment methods](/get-started/account/orgs/sharing/customers-payment-methods)

[Supported setups](/get-started/account/orgs/setup)

[Multiple separate accounts](/get-started/account/multiple-accounts)

[Linked external accounts](/get-started/account/linked-external-accounts)

Settings

[Profile](/get-started/account/profile)

[Branding](/get-started/account/branding)

[Statement descriptors](/get-started/account/statement-descriptors)

[Custom email domain](/get-started/account/email-domain)

[Custom domain](/payments/checkout/custom-domains)

[Single sign-on](/get-started/account/sso)

[Stripe Verified](/verified)

[Quickstarts](/quickstarts)

Start developing

[Build with an LLM](/building-with-llms)

Use Stripe without code

Migrate to Stripe

Common use cases

[Overview](/get-started/use-cases)[Accept simple payments as a startup](/get-started/use-cases/startup)[Sell subscriptions as a SaaS startup](/get-started/use-cases/saas-subscriptions)[Build a subscriptions solution with usage-based pricing](/get-started/use-cases/usage-based-billing)[Accept payments in person](/get-started/use-cases/in-person-payments)[Send invoices to collect payments](/get-started/use-cases/invoices)

United StatesEnglish (United States)

# Manage access to your organization

## Invite and manage access for team members in your organization.

Ask about this page

Copy for LLMView as Markdown

You can manage your organization’s team member permission levels from your [Team and security](https://dashboard.stripe.com/org/settings/team) settings. Administrators can:

- Add members to or remove them from an organization or its accounts.
- View all members across an organization or account.
- Change the [user roles](/get-started/account/teams/roles) assigned to any member.
- Invite up to ten users to a given role.
- Manage two-factor (2FA) authentication settings for a member or the entire account.
- View the security history of all members.

## Organization versus account roles

You can assign users access to your entire organization or individual accounts within your organization. Organization-level roles grant users access to all accounts within the organization, including the organization itself. Account-level roles let users access a specific account with the assigned role.

A user can have roles at both the organization and account levels. However, organization-level roles are automatically inherited at the account level. For example, you can’t give someone admin rights for the organization but view-only access for an account within that organization. Conversely, you can assign admin rights for a specific account without granting organization-level admin access.

- **Manage your organization’s team members**: Manage user access and roles for specific accounts under the organization’s [Team](https://dashboard.stripe.com/org/settings/team) tab. You can also manage team members by granting access to multiple accounts simultaneously or providing access to the entire organization. You can only access this page if you have an organization-level role.
- **Manage an account’s team members**: Add, remove, and edit team members of an account, and update the roles of users associated with that account under the account’s [Team](https://dashboard.stripe.com/settings/team) tab.

For example, assume you have three accounts: Banking, Finance, and Consulting. In this case, organization- and account-level roles work as follows:

- **Organization-level role**: Assign a user the IAM Administrator role to grant that role in all three accounts and the organization itself. This provides access to team management for all three accounts and organization-level team management.
- **Account-level role**: Assign a user the IAM Administrator role in the Banking account to limit their access to the IAM role within that account. They can manage account-level teams only within the Banking account. This role doesn’t grant access to other accounts or organization-level team management.

## Create API keys

Configure [organization API keys](/keys#organization-api-keys) so your team members can make API requests for any account within the organization.

## Update your organization

You can view all of your organization’s team members under the [Team](https://dashboard.stripe.com/org/settings/team) tab. Additionally, you can:

- Invite new members.
- Edit members.
- Grant members access to one or more additional accounts.
- Remove members from your organization.

You add, remove, and edit team members using the following processes from either the organization or account Dashboard. The only difference is that the account Dashboard only shows actions available for that specific account.

### Add a team member

To add new team members:

1. Navigate to the [Team](https://dashboard.stripe.com/org/settings/team) tab.
2. Click **Add member**.
3. Add one or more email addresses, separated by space or comma. Adding users together allows you to assign them all the same roles and access simultaneously.
4. Select which roles to assign. Users can hold multiple roles within the same account.
5. Select which accounts to apply the selected roles to.

   - Select one or more accounts to grant the role permissions only in those accounts.
   - Select the organization to grant the role permissions for the organization and all accounts within the organization. Grant the lowest permission required by the user because you can still grant different roles at the individual account level.
6. Click **Assign additional roles** to choose different roles to assign for other accounts.
7. After completing the role assignment for all the accounts, review the configuration, and click **Send invites** to email the specified users with the steps to accept the invitation.

### Remove a team member

To remove an existing team member:

1. Navigate to the [Team](https://dashboard.stripe.com/org/settings/team) tab.
2. Click the overflow menu () in the user’s row to remove them. You can also click **Remove member** in the user’s profile.
3. After you remove a user, they immediately lose access to the organization.

### Edit a team member’s access

To edit an existing team member’s access:

1. Navigate to the [Team](https://dashboard.stripe.com/org/settings/team) tab.
2. Click the user’s profile from the list of team members.
3. Click **Manage roles**.
4. In the overflow menu () next to the user’s role, click **Edit**. In the **Manage roles** drawer, you can also remove or add user roles.
5. Select the accounts where you want this user to have these new roles. You can add new accounts, remove accounts, or grant organization-level access.

### View all team members

To view all team members within an organization, go to the [Team](https://dashboard.stripe.com/org/settings/team) tab. From here, you can also export the entire user table as a **CSV** file, and filter by:

- Account
- Roles
- Status
- Name
- Email

## Authenticate team members

Stripe supports 2FA through TouchID, security key, SMS, and authenticator apps, such as Google Authenticator. As an additional security measure, Stripe recommends that all users register for 2FA.

### Require 2FA for all users

Only an organization Administrator or Super Administrator can require 2FA for all team members.

1. Navigate to the [User authentication](https://dashboard.stripe.com/org/settings/security/authentication) tab.
2. Enable **Require two-step authentication for all team members**.

After you enable this option, all users must register a 2FA device during their next login. This requires them to complete a 2FA challenge during subsequent login attempts.

### Reset 2FA for a single user

If a single user loses access to their 2FA devices, an Administrator or Super Administrator must reset the compromised user’s 2FA settings from the account level:

1. Navigate to the account’s [Team](https://dashboard.stripe.com/settings/team) tab.
2. Click the compromised user’s profile.
3. Click **Reset two-factor authentication**.

Stripe sends an email to the compromised user’s registered email address with instructions on how they can reset their 2FA devices. You can’t do this by going to the user’s profile at the organization level.

## View your security history

To view your organization’s security history, go to the [Security history](https://dashboard.stripe.com/settings/org/security/history) tab. Here, you can filter your security history by date or action. The **Action** filter includes hundreds of actions across different categories, including **User security**, **Team**, **API**, and a number of Stripe products. You can also export your entire security history as a **CSV** file.