# Activate your account

Source: https://docs.stripe.com/get-started/account/activate

---

Activate your account

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Factivate)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Factivate)

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

Activate your account

[Add funds to your balance](/get-started/account/add-funds)

[Account checklist](/get-started/account/checklist)

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

# Activate your account

## Learn how to activate and secure your Stripe account.

Ask about this page

Copy for LLMView as Markdown

### Account checklist

For the safety and security of your Stripe account, complete our [account checklist](/get-started/account/checklist) before going live.

Immediately after you create a Stripe account, you can use your account in testing environments. In a [sandbox](/sandboxes), simulate transactions and use all of Stripe’s features without moving any money. To accept real payments, you must activate your account to use live mode. If you haven’t already, [create a Stripe account](https://dashboard.stripe.com/register).

## Activate your account

To activate your account, fill out the [account application](https://dashboard.stripe.com/account/onboarding) requesting some basic information about your business, product, and your personal relationship to your business. After activating your account, you can immediately start accepting live payments.

Stripe’s “Know Your Customer” (KYC) obligations require that we collect and maintain this information on all Stripe users. These requirements come from our regulators and financial partners, and are intended to prevent abuse of the financial system. We review the information you provide internally to make sure that it complies with [our services agreement](https://stripe.com/legal/ssa). We’ll contact you if we need any further information.

After you activate your Stripe account, you can’t change its country. If you need to use Stripe in a different country that we support, you must create a new account.

#### Caution

Privacy and security are priorities for Stripe. Our [privacy policy](https://stripe.com/privacy) explains how and for what purposes we collect, use, retain, disclose, and safeguard any personal data you provide to us.

## Public business information

### Close your account

You can [close your account](https://support.stripe.com/questions/how-can-i-close-my-stripe-account) any time you want. We recommend you leave it dormant, however, in case you need to access any financial data or take action to resolve a dispute.

Your customers see the following details on either their card statements or in [email receipts](/receipts) sent by Stripe.

- Business name and website URL
- Business email address, phone number, and address
- Support site URL
- Statement descriptor text

You provide this information when you activate your account, and can update it any time in your [Account settings](https://dashboard.stripe.com/settings/public). Make sure that your statement descriptor text and business information are clearly associated with you. If your customer can’t recognize one of your payments, they might [dispute](/disputes) it.

Statement descriptors are limited to between 5 and 22 characters. They must contain at least 5 letters and can’t use the special characters `<`, `>`, `\`, `'`, `"`, or `*`.

You can also use dynamic statement descriptors when creating a charge so that each payment has a custom statement descriptor. This dynamic text is appended to the [shortened descriptor](https://dashboard.stripe.com/settings/public) set in the Stripe Dashboard. Statement descriptor prefixes are limited to between 2 and 10 characters. For detailed information, see the documentation on [statement descriptors](/get-started/account/statement-descriptors).

## Keep your account safe

After you set up your account, you’ll want to keep it safe. Here are our recommendations:

- **Keep private information private**: Don’t share your password and keep your secret [API keys](/keys) confidential on your own servers. As a reminder, Stripe employees will never ask you for your keys.
- **Don’t reuse your Stripe password**: Use a password that’s unique to Stripe. If you use your password on another site and that site is compromised, an attacker could use those stolen credentials to take over your account. If you need to reset your password, click **Edit** > **Change password** in your [Personal details](https://dashboard.stripe.com/settings/user) settings, and enter a new password.
- **Use team members to provide others with access to your account**: You can [invite others](/get-started/account/teams) (with limited access) to your Stripe account so that they can log in and take certain actions.
- **Update your computer and browser regularly**: We recommend configuring your computer to automatically download and install updates (for example, [macOS](https://support.apple.com/en-us/HT201541) or [Windows](https://support.microsoft.com/en-us/kb/306525)). This helps protect your system against automated attacks and malware.
- **Beware of phishing**: All [genuine Stripe sites](https://support.stripe.com/questions/verify-you-are-on-an-official-stripe-webpage) use the `stripe.com` domain and HTTPS. If you get an email from us that you don’t expect, go directly to our site to log in. Don’t enter your password after clicking a link in an email. If you’re ever not sure it’s really us, review [Verified Stripe domains](https://support.stripe.com/questions/verified-stripe-domains) on Stripe Support.
- **Enable two-factor verification**: When you enable two-factor authentication, you’ll need to provide an additional unique code from your mobile device to complete the login process—either received as a text message or generated through an app like Google Authenticator. This means that even if someone steals your username and password, they won’t be able to log in. To enable this feature, go to your [user settings](https://dashboard.stripe.com/settings/user).

## See also

- [Account checklist](/get-started/account/checklist)
- [Multiple accounts](/get-started/account/multiple-accounts)