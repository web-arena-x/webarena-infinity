# Account checklist

Source: https://docs.stripe.com/get-started/account/checklist

---

Account checklist

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fchecklist)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fchecklist)

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

Account checklist

[Acceptable verification documents](/acceptable-verification-documents)

Account structure

[Start a team](/get-started/account/teams)

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

# Account checklist

## Complete this checklist before taking your Stripe account live.

Ask about this page

Copy for LLMView as Markdown

### Checklist progress

As you complete each item and check it off, the state of each checkbox is stored within your browser’s cache. You can refer back to this page at any time to see what you’ve completed so far.

You can [log in](https://dashboard.stripe.com/) to see some of your current settings.

The items in this checklist apply to all Stripe accounts, regardless of how or where you signed up for Stripe. We also have checklists for [taking your integration live](/get-started/checklist/go-live) and adhering to [website payment best practices](/get-started/checklist/website). For the safety and security of your Stripe account, follow these steps before going live:

- Enable two-step authentication

  For security purposes, [enable two-factor authentication (2FA)](https://support.stripe.com/questions/how-do-i-enable-two-step-verification) on your Stripe account. Two-factor authentication requires that you log in with both your username and password, and enter a code sent to your mobile device. Using 2FA makes it harder for someone else to access your Stripe account.
- Confirm your statement descriptor and public information

  The [statement descriptor](/get-started/account/activate#public-business-information) appears on customer statements when you charge their card. Missing or incorrect information can result in confused customers creating disputes, so make sure to review your statement descriptor in the [Dashboard](https://dashboard.stripe.com/settings/public). Statement descriptors are limited to between 5 and 22 characters. They must contain at least 5 letters and can’t use the following special characters: `<`, `>`, `\`, `'`, or `"`. Stripe also recommends that you add text to your site that tells your users what they’ll see on their statements.

  The card issuer can automatically include other account information—for example, business name, address, email, or phone number—to show on your customer’s statements. Check that all of this information in your Stripe account is acceptable for your customers to see.
- Set up email notifications

  Stripe can notify you of account activity by email. You can choose events to be notified of in your [Communication preferences](https://dashboard.stripe.com/settings/communication-preferences). If multiple [team members](/get-started/account/teams) have access to your account, each one can set their own notification preferences. At a minimum, we recommend turning on emails for successful charges and disputes.
- Set up SMS from Stripe for critical account health updates

  Choose the events to receive notification of in your [Communication preferences](https://dashboard.stripe.com/settings/communication-preferences). Any [team member](/get-started/account/teams) with account access can set their own notification preferences.
- Prevent and manage fraud and disputes

  [Fraud and disputes](/disputes/prevention) are unfortunate realities in all commerce. While Stripe is constantly improving its tools to help reduce these incidents, we recommend that you’re set up to:

  - Regularly review [payments in the Dashboard](https://dashboard.stripe.com/test/payments).
  - [Report charges](/radar/risk-evaluation) that appear suspicious using the Dashboard or API.
  - Have [evidence](/disputes/responding#respond) at the ready for disputes.
  - Prevent and mitigate [card testing](/disputes/prevention/card-testing).
- Review your bank account information

  Incorrect bank information is a common cause of [payout delays](/payouts#payout-failures). Before accepting live charges, confirm [your bank details](https://dashboard.stripe.com/settings/payouts) are correct. If you process charges in [multiple currencies](/currencies) and have multiple bank accounts, also confirm you’ve established the correct default currency. Multiple bank accounts for additional currencies are optional as Stripe can convert any payments into your default currency.

  When reviewing your bank information, set your preferred [payout schedule](/payouts#payout-schedule). The recommended and default option is daily—as funds become available—but you can change this to best suit your business and reporting needs.
- Give your team members access to your Stripe account

  You can give your [team members](/get-started/account/teams) access to your Stripe account. Stripe even lets you give different team members different permissions depending on their [roles](/get-started/account/teams/roles).

  Whenever you give a team member access to your Stripe account, don’t give them your login credentials. We also recommend that you ask your team members to enable 2FA.

  If a team member no longer needs access to your Stripe account, remove them from your account.
- Understand industry-specific restrictions

  Review our [Prohibited & Restricted businesses list](https://stripe.com/legal/restricted-businesses) to determine if your business operates in an industry that Stripe restricts or prohibits.

  If your business operates in a restricted industry, you might need to provide additional documentation before you can use Stripe as your payment processor. If your business operates in a prohibited industry, you won’t be able to use Stripe.

  If you have any questions about onboarding requirements or restrictions applicable to your business, [contact us](https://stripe.com/contact).

## See also

- [Multiple accounts](/get-started/account/multiple-accounts)
- [Start a team](/get-started/account/teams)
- [Custom email domain](/get-started/account/email-domain)