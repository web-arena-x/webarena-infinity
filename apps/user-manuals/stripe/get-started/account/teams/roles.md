# User roles

Source: https://docs.stripe.com/get-started/account/teams/roles

---

User roles

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fteams%2Froles)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fteams%2Froles)

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

User roles

[Organizations](/get-started/account/orgs)

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

# User roles

## Give team members controlled access to your Stripe account.

#### Note

If you assign a user multiple roles, they’re assigned all the permissions of each individual role. Be cautious of conflicts and unintended authority.

Admin roles

##### Administrator

This role is for anyone who needs similar access as the account owner—they can see and manage almost everything.

They can't delete the default bank account, or change the account owner.

[SSO](/dashboard/sso) Role ID:

admin

Some of what this role can do:

- Create, view, refund payments
- Issue credit notes on invoices
- Create, view, edit, and delete products
- Create, view, edit, and delete customers
- Create, view, edit, and reject connected accounts
- [Receive email notifications](https://support.stripe.com/questions/set-up-account-email-notifications) for connected account rejections and risk requirements that are upcoming, due, or past due
- View balance
- Transfer balances to connected accounts and reverse transfers
- Payout balance to external bank account
- Invite, edit, and remove team members
- Create, view, edit, and delete API keys
- Add and edit bank account details
- Add and edit bank account details of connected accounts
- Edit payout schedule
- Edit account details (address and contact)
- Configure all product settings (for example, payment methods, Radar settings, or Connect settings)
- Connect account to [Connect](https://docs.stripe.com/connect) platforms
- Bulk exports of payments, customers, products, and connected accounts
- View support message history
- Manage support requests
- Change the default payout currency
- View your account in the mobile app
- View security history audit logs

Some of what this role can't do:

- Delete the default bank account
- Change the account owner (only the owner can transfer ownership)

##### IAM Administrator

The Identity and Access Management (IAM) Admin role is for people who need to invite team members and assign roles. They can also remove any user, including Administrators and Super Administrators.

They can't do anything beyond access management. They also can't assign a user to the Administrator or Super Administrator role.

[SSO](/dashboard/sso) Role ID:

iam\_admin

Some of what this role can do:

- Invite, edit, and remove team members
- Create and manage user groups
- View security history
- View security history audit logs

Some of what this role can't do:

- View and resolve disputes
- Create, view, refund payments
- Create, view, edit, and delete products
- Create, view, edit, and delete customers
- Create, view, edit, and reject connected accounts
- Edit connected account capabilities
- Edit connected account payout schedules
- View Radar rules and settings
- View balance
- View transfers
- Transfer balances to connected accounts and reverse transfers
- Payout balance to external bank account
- Create, view, and download financial reports
- Bulk exports of payments, customers, products, and connected accounts
- Create, view, edit, and delete API keys
- Add and edit bank account details
- Edit payout schedule
- Edit account details (address and contact)
- Change the account owner
- Configure all product settings (for example, payment methods, Radar settings, or Connect settings)
- Connect account to [Connect](https://docs.stripe.com/connect) platforms
- View events and logs
- View payouts
- View your account in the mobile app
- Assign the Super Administrator role to other users

##### Super Administrator

This role is assigned to the creator of a business account and should only be assigned to users who are allowed to perform all privileged actions. Only a Super Administrator can assign the Super Administrator role to other team members.

Change the account owner (only the owner can transfer ownership).

[SSO](/dashboard/sso) Role ID:

super\_admin

Some of what this role can do:

- Create, view, refund payments
- Issue credit notes on invoices
- Create, view, edit, and delete products
- Create, view, edit, and delete customers
- Create, view, edit, and reject connected accounts
- [Receive email notifications](https://support.stripe.com/questions/set-up-account-email-notifications) for connected account rejections and risk requirements that are upcoming, due, or past due
- View balance
- Transfer balances to connected accounts and reverse transfers
- Payout balance to external bank account
- Invite, edit, and remove team members
- Create, view, edit, and delete API keys
- Add and edit bank account details
- Add and edit bank account details of connected accounts
- Edit payout schedule
- Edit account details (address and contact)
- Configure all product settings (for example, payment methods, Radar settings, or Connect settings)
- Connect account to [Connect](https://docs.stripe.com/connect) platforms
- Bulk exports of payments, customers, products, and connected accounts
- View support message history
- Manage support requests
- Change the default payout currency
- View your account in the mobile app
- View security history audit logs
- Assign the Super Administrator role to other users
- Create, view, modify, and delete sandboxes
- Add accounts to an organization (the user must be a Super Administrator in the accounts and the organization)

Some of what this role can't do:

- Delete the default bank account
- Change the account owner (only the owner can transfer ownership)

Important

These roles can invite additional users to your account, and if compromised by an attacker would allow them to invite users under their control.

Account owner

An Account Owner is a special type of Administrator that can perform all actions, including closing the account.
There can only be one Owner for an account. To change the Account Owner, please refer to [this guide](https://support.stripe.com/questions/change-the-owner-of-a-stripe-account).

Connect roles

These roles are only available if you use [Connect](https://docs.stripe.com/connect)

##### Connect Onboarding Analyst

This role is for people who need to create connected accounts and edit their identity information.

They can't do anything on the platform account except view and edit connected accounts.

[SSO](/dashboard/sso) Role ID:

connect\_onboarding\_analyst

Some of what this role can do:

- Create, view, and edit connected accounts
- Edit connected account capabilities
- Add person to a connected account
- Bulk exports of connected accounts

Some of what this role can't do:

- View and resolve disputes (on the platform or connected accounts)
- Create, view, refund payments (on the platform or connected accounts)
- Create, view, edit, and delete products (on the platform or connected accounts)
- Create, view, edit, and delete customers (on the platform or connected accounts)
- Reject connected accounts
- Edit connected account payout schedules
- View transfers
- Transfer balances to connected accounts and reverse transfers
- Payout balance to external bank account
- Edit payout schedule
- Add and edit bank account details
- Create, view, edit, and delete API keys
- View events and logs
- Invite, edit, and remove team members
- Edit account details (address and contact)
- Change the account owner
- View Radar rules and settings
- Configure any product settings (for example, payment methods, Radar settings, or Connect settings)
- Connect account to [Connect](https://docs.stripe.com/connect) platforms
- Create, view, and download financial reports
- Bulk exports of payments, customers, and products
- View payouts
- View your account in the mobile app

##### Transfer Analyst

Your account must require [two-step authentication](https://support.stripe.com/questions/two-step-authentication-requirement) in order to allow non-Administrators with this role to transfer funds.

This role is for people who need to transfer funds to connected accounts and view the platform’s balance and historical payouts.

They can't pay out money to external bank accounts, add or edit bank accounts, or create new connected accounts.

[SSO](/dashboard/sso) Role ID:

transfer\_analyst

Some of what this role can do:

- Transfer balances to connected accounts and reverse transfers
- View transfers
- View connected accounts
- View balance
- View payouts

Some of what this role can't do:

- View and resolve disputes
- Create, view, refund payments
- Create, view, edit, and delete products
- Create, view, edit, and delete customers
- Create, edit, and reject connected accounts
- Edit connected account capabilities
- Edit connected account payout schedules
- Payout balance to external bank account
- Edit payout schedule
- Add and edit bank account details
- Create, view, edit, and delete API keys
- View events and logs
- Invite, edit, and remove team members
- Edit account details (address and contact)
- Change the account owner
- View Radar rules and settings
- Configure any product settings (for example, payment methods, Radar settings, or Connect settings)
- Connect account to [Connect](https://docs.stripe.com/connect) platforms
- Create, view, and download financial reports
- Bulk exports of payments, customers, products, and connected accounts
- View your account in the mobile app

Developer roles

##### Developer

This role is for developers who need to set up a Stripe integration. This role has access to the secret key, which grants access to almost all API resources.

They can't invite team members or change the account owner.

[SSO](/dashboard/sso) Role ID:

developer

Some of what this role can do:

- Create, view, edit, and delete API keys
- View events and logs
- View and resolve disputes
- Create, view, refund payments
- Issue credit notes on invoices
- Create, view, edit, and delete products
- Create, view, edit, and delete customers
- Create, view, edit, and reject connected accounts
- Edit connected account capabilities
- Edit connected account payout schedules
- Add and edit bank account details of connected accounts
- View balance
- View transfers
- Payout balance to external bank account
- Edit account details (address and contact)
- View and edit almost all product settings (for example, payment methods, Radar settings, or Connect settings) except Climate
- Connect account to [Connect](https://docs.stripe.com/connect) platforms
- Create, view, and download financial reports
- Bulk exports of payments, customers, products, and connected accounts
- View payouts
- View your account in the mobile app
- View security history audit logs

Some of what this role can't do:

- Transfer balances to connected accounts and reverse transfers
- Edit payout schedule
- Add and edit bank account details
- Invite, edit, and remove team members
- Change the account owner
- Edit Climate settings

Identity roles

These roles are only available if you use [Identity](https://docs.stripe.com/identity)

##### Identity Analyst

This role is for Identity users who need to create, review, cancel, or redact verifications.

This role can’t edit verifications for connected accounts.

[SSO](/dashboard/sso) Role ID:

identity\_analyst

Some of what this role can do:

- Create, view, and edit identity verifications.
- Manually review, cancel, and redact identity verifications.
- View events and logs

Some of what this role can't do:

- Create, view, and edit identity verifications for connected accounts.

##### Identity View Only

This role is for Identity users who need to view verification data.

This role can’t create, review, cancel, or redact verifications.

[SSO](/dashboard/sso) Role ID:

identity\_view\_only

Some of what this role can do:

- View identity verifications.
- View events and logs

Some of what this role can't do:

- Create and edit identity verifications.
- Manually review, cancel, and redact identity verifications.
- Create, view, and edit identity verifications for connected accounts.

Payment roles

##### Analyst

This role is for people who need to pay out money, refund payments, and export data.

They can't edit payout schedules or account settings.

[SSO](/dashboard/sso) Role ID:

analyst

Some of what this role can do:

- View and resolve disputes
- Create, view, refund payments
- Issue credit notes on invoices
- Create, view, edit, and delete products
- Create, view, edit, and delete customers
- View connected accounts
- View balance
- View transfers
- Payout balance to external bank account
- View Radar rules and settings
- View events and logs
- Create, view, and download financial reports
- Bulk exports of payments, customers, products, and connected accounts
- View payouts
- Edit account details (address and contact)
- Create, view, and edit identity verifications.
- Manually review, cancel, and redact identity verifications.
- View your account in the mobile app

Some of what this role can't do:

- Edit connected account payout schedules
- Edit payout schedule
- Add and edit bank account details
- Create, view, edit, and delete API keys
- Invite, edit, and remove team members
- Change the account owner
- Connect account to [Connect](https://docs.stripe.com/connect) platforms
- Create, view, and edit identity verifications for connected accounts.

##### Dispute Analyst

This role is for people who need need to view, submit evidence for, and accept disputes.

They can't do anything that's not related to disputes.

[SSO](/dashboard/sso) Role ID:

dispute\_analyst

Some of what this role can do:

- View and resolve disputes
- View payments
- View products
- View customers
- View invoices and subscriptions

Some of what this role can't do:

- Create or refund payments
- Create, edit, and delete products
- Create, edit, and delete customers
- Create, view, edit, and reject connected accounts
- Edit connected account capabilities
- Edit connected account payout schedules
- View balance
- View transfers
- Transfer balances to connected accounts and reverse transfers
- Payout balance to external bank account
- Edit payout schedule
- Add and edit bank account details
- Create, view, edit, and delete API keys
- View events and logs
- Invite, edit, and remove team members
- Edit account details (address and contact)
- Change the account owner
- View Radar rules and settings
- Configure any product settings (for example, payment methods, Radar settings, or Connect settings)
- Connect account to [Connect](https://docs.stripe.com/connect) platforms
- Create, view, and download financial reports
- Bulk exports of payments, customers, products, and connected accounts
- View payouts
- View your account in the mobile app

##### Refund Analyst

This role is for people who need to refund payments and issue credit notes on invoices.

They can’t create payments, view balance, or view connected accounts.

[SSO](/dashboard/sso) Role ID:

refund\_analyst

Some of what this role can do:

- View and refund payments
- View products
- View customers
- View disputes
- View invoices and subscriptions
- Issue credit notes on invoices
- View Radar rules and settings

Some of what this role can't do:

- Create payments
- Resolve disputes
- Create, edit, and delete products
- Create, edit, and delete customers
- Create, view, edit, and reject connected accounts
- Edit connected account capabilities
- Edit connected account payout schedules
- View balance
- View transfers
- Transfer balances to connected accounts and reverse transfers
- Payout balance to external bank account
- Edit payout schedule
- Add and edit bank account details
- Create, view, edit, and delete API keys
- View events and logs
- Invite, edit, and remove team members
- Edit account details (address and contact)
- Change the account owner
- Configure any product settings (for example, payment methods, Radar settings, or Connect settings)
- Connect account to [Connect](https://docs.stripe.com/connect) platforms
- Create, view, and download financial reports
- Bulk exports of payments, customers, products, and connected accounts
- View payouts
- View your account in the mobile app

Support roles

##### Data Migration Specialist

This role is for people who need to perform data migrations (copy, import, export) for their account.

They can't create connected accounts, transfer funds, payout money, or edit any account and product settings.

[SSO](/dashboard/sso) Role ID:

data\_migration\_specialist

Some of what this role can do:

- View connected accounts
- View, create, and edit customers
- Send and receive data copies
- Request data exports
- View security history audit logs

Some of what this role can't do:

- Create, view, or refund live payments
- Issue credit notes on invoices
- Edit connected account capabilities
- Create connected accounts
- Transfer balances to connected accounts and reverse transfers
- Add and edit bank account details
- Create, view, edit, and delete API keys
- Invite, edit, and remove team members
- Edit account details (address and contact)
- Change the account owner
- Configure any product settings (for example, payment methods, Radar settings, or Connect settings)

##### Support Associate

This role is for people who need to refund payments and resolve disputes, but should not have the ability to edit products. It has administration permissions for connected accounts, where it can edit the payout schedule, update the legal entity, update the bank account, and more.

They can't create connected accounts, transfer funds, payout money, or edit any account or product settings.

[SSO](/dashboard/sso) Role ID:

support\_associate

Some of what this role can do:

- View and resolve disputes
- Create, view, refund payments
- Issue credit notes on invoices
- View products
- Create, view, edit, and delete customers
- View, edit, and reject connected accounts
- Edit connected account capabilities
- Edit connected account payout schedules
- Add and edit bank account details of connected accounts
- View Radar rules and settings
- Add payment fingerprint to Radar allow lists
- View events and logs
- Bulk exports of payments, customers, products, and connected accounts

Some of what this role can't do:

- Create connected accounts
- Transfer balances to connected accounts and reverse transfers
- Payout balance to external bank account
- Edit payout schedule
- Create, view, edit, and delete API keys
- Invite, edit, and remove team members
- Edit account details (address and contact)
- Change the account owner
- Configure any product settings (for example, payment methods, Radar settings, or Connect settings)
- Create, edit, and delete products
- Connect account to [Connect](https://docs.stripe.com/connect) platforms
- Create, view, and download financial reports
- View your account in the mobile app

##### Support Communications

This role is for people who need to authenticate email support cases, use Support Center to view and respond to support cases, or share files securely with Stripe.

They can’t access financial information, transfer funds, access or edit connected accounts, or edit any account and product settings.

[SSO](/dashboard/sso) Role ID:

support\_communications

Some of what this role can do:

- View support message history
- Manage support requests

Some of what this role can't do:

- Edit account details (address and contact)
- Add and edit bank account details
- Configure any product settings (for example, payment methods, Radar settings, or Connect settings)
- Create, view, edit, and delete API keys
- Create, view, refund payments
- View payouts
- View and resolve disputes
- Create, view, edit, and delete products
- Create, view, edit, and delete customers
- Create, view, edit, and reject connected accounts
- View events and logs
- View your account in the mobile app
- Anything outside the scope of managing support requests

##### Support Specialist

This role is for people who need to refund payments, resolve disputes, and may need to update products. It has administration permissions for connected accounts, where it can edit the payout schedule, update the legal entity, and more. This role can add, edit, and delete products.

They can't create connected accounts, transfer funds, payout money, or edit any account settings.

[SSO](/dashboard/sso) Role ID:

support\_specialist

Some of what this role can do:

- View and resolve disputes
- Create, view, refund payments
- Issue credit notes on invoices
- Create, view, edit, and delete products
- Create, view, edit, and delete customers
- View, edit, and reject connected accounts
- Edit connected account capabilities
- Edit connected account payout schedules
- Add and edit bank account details of connected accounts
- View Radar rules and settings
- Add payment fingerprint to Radar allow lists
- View events and logs
- Bulk exports of connected accounts
- Perform self-service returns for hardware orders

Some of what this role can't do:

- Create connected accounts
- Transfer balances to connected accounts and reverse transfers
- Payout balance to external bank account
- Edit payout schedule
- Add and edit bank account details
- Create, view, edit, and delete API keys
- Invite, edit, and remove team members
- Edit account details (address and contact)
- Change the account owner
- Configure any product settings (for example, payment methods, Radar settings, or Connect settings)
- Connect account to [Connect](https://docs.stripe.com/connect) platforms
- Create, view, and download financial reports
- Bulk exports of payments, customers, and products
- View your account in the mobile app

##### Terminal Specialist

This role is for people who need to manage their Terminal fleet. They can register readers, manage locations, place hardware orders, and deploy software to Terminal devices.

They can't view or manage payments, products, or customers. They also can't configure payment methods or other product settings.

[SSO](/dashboard/sso) Role ID:

terminal\_specialist

Some of what this role can do:

- Manage Terminal locations, zones, and configurations
- Register and manage Terminal readers
- Place hardware orders and return hardware
- Manage Terminal software and deployments

Some of what this role can't do:

- Create, view, refund payments
- Create, view, edit, and delete products
- Create, view, edit, and delete customers
- Configure any product settings (for example, payment methods, Radar settings, or Connect settings)
- Create, view, edit, and delete API keys
- Invite, edit, and remove team members

Tax form roles

These roles are only available if you use [1099s](https://docs.stripe.com/connect/tax-reporting)

##### Tax Analyst

This role is for people who need to configure tax form settings, file tax forms for connected accounts, and export data.

They can't create connected accounts, transfer funds, payout money, or edit account and non-Tax product settings.

[SSO](/dashboard/sso) Role ID:

tax\_analyst

Some of what this role can do:

- Configure tax and tax form settings
- View, modify, and file tax forms for connected accounts
- Full access to the [tax forms](https://dashboard.stripe.com/connect/taxes/forms) view
- View disputes
- View payments
- View products
- View customers
- View connected accounts
- View balance
- View transfers
- View Radar rules and settings
- View events and logs
- Create, view, and download financial reports
- Bulk exports of payments, customers, and products
- View payouts
- View your account in the mobile app

Some of what this role can't do:

- Resolve disputes
- Create or refund payments
- Create, edit, and delete products
- Create, edit, and delete customers
- Create, edit, and reject connected accounts
- Transfer balances to connected accounts and reverse transfers
- Payout balance to external bank account
- Edit payout schedule
- Add and edit bank account details
- Create, view, edit, and delete API keys
- Invite, edit, and remove team members
- Edit account details (address and contact)
- Bulk exports of connected accounts
- Change the account owner
- Edit any non-Tax product settings (for example, payment methods, Radar settings, or Connect settings)
- Connect account to [Connect](https://docs.stripe.com/connect) platforms

View only roles

##### View Only

This role is for people who need to view payments, balance, and connected accounts, but can’t edit any of them. This role can also export data and download reports.

They can't create connected accounts, transfer funds, payout money, or edit any account and product settings.

[SSO](/dashboard/sso) Role ID:

view\_only

Some of what this role can do:

- View disputes
- View payments
- View products
- View customers
- View connected accounts
- View balance
- View transfers
- View Radar rules and settings
- View events and logs
- Create, view, and download financial reports
- Bulk exports of payments, customers, and products
- View payouts
- View your account in the mobile app
- View security history audit logs

Some of what this role can't do:

- Resolve disputes
- Create or refund payments
- Create, edit, and delete products
- Create, edit, and delete customers
- Create, edit, and reject connected accounts
- Transfer balances to connected accounts and reverse transfers
- Payout balance to external bank account
- Edit payout schedule
- Add and edit bank account details
- Create, view, edit, and delete API keys
- Invite, edit, and remove team members
- Edit account details (address and contact)
- Bulk exports of connected accounts
- Change the account owner
- Configure any product settings (for example, payment methods, Radar settings, or Connect settings)
- Connect account to [Connect](https://docs.stripe.com/connect) platforms

Other roles

##### Accountant

This role is for accountants who need to access Stripe Revenue Recognition and its features for monthly bookkeeping. The accountants can set up a custom chart of accounts, create accounting rules and modify revenue amortisation settings. They can also view payments, balance, invoices, customers, and connected accounts, etc., but can’t edit any of them.

They can't create connected accounts, transfer funds, payout money, choose pricing plans, or edit any account and other product settings including signing-up or canceling Stripe Revenue Recognition.

[SSO](/dashboard/sso) Role ID:

accountant

Some of what this role can do:

- Create, view, download accounting reports and statements
- Import external information into Stripe Revenue Recognition
- Create, view, modify accounting rules or chart of accounts
- View and modify Revenue Recognition settings such as amortization schedule and reopening accounting periods
- Signing-up for Stripe Revenue Recognition product betas
- Create, view, and download financial reports
- View disputes
- View payments
- View products
- View customers
- View connected accounts
- View balance
- View transfers
- View payouts
- View security history audit logs

Some of what this role can't do:

- Initiate or cancel Stripe Revenue Recognition membership
- Choose or modify pricing plan
- Invite, edit, and remove team members
- Resolve disputes
- Create or refund payments
- Create, edit, and delete products
- Create, edit, and delete customers
- Create, edit, and reject connected accounts
- Transfer balances to connected accounts and reverse transfers
- Payout balance to external bank account
- Edit payout schedule
- Add and edit bank account details
- Create, view, edit, and delete API keys
- Change the account owner
- Configure any other product settings (for example, payment methods, Radar settings, or Connect settings)

##### Top-up Specialist

This role gives access to the Top-ups feature, including creating, viewing, and updating top-ups, as well as viewing balance and payouts. Accountants or Financial employees may find this useful.

They can't access any other Stripe features.

[SSO](/dashboard/sso) Role ID:

topup\_specialist

Some of what this role can do:

- Load and view Top-ups
- Create new Top-ups
- Update existing Top-ups
- View payouts
- View balance

Some of what this role can't do:

- Anything outside the scope of the Top-ups feature

##### Financial Connections Specialist

This role gives access to Financial Connections operations, including viewing and editing Financial Connections settings, registration and objects, with limited customer read access.

They can't access any other Stripe features.

[SSO](/dashboard/sso) Role ID:

financial\_connections\_specialist

Some of what this role can do:

- Apply to activate the Financial Connections product and edit that application
- Edit the Financial Connections settings
- View Financial Connections accounts
- Disconnect Financial Connections accounts
- View Financial Connections sessions

Some of what this role can't do:

- Anything not related to the Financial Connections product

##### Data Engineer

This role is for Stripe Data Pipeline users who need to setup and manage data pipelines.

They will not have access to other parts of the Dashboard other than Stripe Data Pipeline.

[SSO](/dashboard/sso) Role ID:

data\_engineer

Some of what this role can do:

- Create data pipelines
- View data pipelines
- Edit data pipelines
- Offboard data pipelines
- View pricing and update plans

Some of what this role can't do:

- Anything not related to the Stripe Data Pipeline product