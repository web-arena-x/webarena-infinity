# Start a team

Source: https://docs.stripe.com/get-started/account/teams

---

Start a team

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fteams)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fteams)

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

Start a team

[User roles](/get-started/account/teams/roles)

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

# Start a team

## Learn how to invite and interact with team members.

Ask about this page

Copy for LLMView as Markdown

### Security history

Stripe logs the account activity of team members during the past 180 days. To review account activity information, go to [Security history](https://dashboard.stripe.com/settings/security_history) in the Dashboard.

To invite new team members:

1. Go to the [Team](https://dashboard.stripe.com/settings/team) tab in the Dashboard.
2. Click **Add member**.
3. Add one or more email addresses, separated by a space or comma. Adding users together allows you to assign them all the same roles and access simultaneously.
4. Select which roles to assign. Users can hold multiple roles within the same account. Review the [list of actions](/get-started/account/teams/roles) that each role can and can’t perform before assigning the role to a team member. Grant the lowest permission required by the user to perform their job.
5. After completing the role assignment for all the accounts, review the configuration, and click **Send invites** to email the specified users with the steps to accept the invitation.

Invites to your Stripe account expire after 10 days.

After a team member accepts their invite, you can edit their role at any time from your [Team](https://dashboard.stripe.com/settings/team) settings. To edit a team member’s role, click the overflow menu (), then click **Edit**.

## Mention team members

You can mention team members when you add a note to a payment. If you mention a team member, they receive an email notification with the note and a link to the associated payment.

## Receive email notifications

You can configure email notifications under **Communication preferences** in your [Personal details](https://dashboard.stripe.com/settings/user) settings, and apply them on a per-user basis. If your team members also want to receive notifications, they must customize their own settings. Stripe sends email notifications to you when any of the following events occur:

- A successful payment is received.
- An [application fee](/connect/direct-charges#collect-fees) is collected from a connected account.
- A payment is [disputed](/disputes) by a customer.
- A payment is marked as [elevated risk](/radar/risk-evaluation#elevated-risk) by Stripe or a custom [Stripe Radar](/radar) rule.
- You’re mentioned in a note.
- A customer sends an incorrect amount to pay their [invoice](/invoicing).
- A [webhook](/webhooks) delivery fails.

For a full list of notification events, go to your **Communication preferences** under **Profile**.

### Automate email notifications

Use [Stripe Workflows](/workflows) to automate sending emails to your team. Workflows allows you to use a visual builder in the Stripe Dashboard to automate tasks that require multi-step processes that depend on conditional logic.

Workflows is also compatible with most Stripe products such as, but not limited to:

- [Online payments](/payments/online-payments)
- [Disputes](/disputes)
- [Invoicing](/invoicing)
- [Billing](/billing)
- [Radar](/radar)

To learn how it works, [set up a test workflow](/workflows/set-up) and review our [example use cases](/workflows/use-cases).

## See also

- [User roles](/get-started/account/teams/roles)