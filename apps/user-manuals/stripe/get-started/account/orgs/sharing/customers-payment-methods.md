# Share customers and payment methods across accounts in an organizationPublic preview

Source: https://docs.stripe.com/get-started/account/orgs/sharing/customers-payment-methods

---

Share customers and payment methods

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Forgs%2Fsharing%2Fcustomers-payment-methods)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Forgs%2Fsharing%2Fcustomers-payment-methods)

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

[Manage access to your organization](/get-started/account/orgs/team)

[Manage SSO](/get-started/account/orgs/sso)

Share customers and payment methods

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

# Share customers and payment methods across accounts in an organizationPublic preview

## Avoid recollecting customer and payment method information from existing customers in multiple accounts.

Ask about this page

Copy for LLMView as Markdown

Many growing businesses expand to multiple Stripe accounts to keep finances from different business lines separate, or because the business operates in multiple regions with different legal entities. As a multi-entity business, you can share customers and payment methods across accounts in an organization to avoid:

- Recollecting payment methods or contact information multiple times from the same customer
- Introducing inconsistencies in a customer’s contact and payment details between accounts
- Maintaining and updating duplicate records

## Limitations

Customer and payment method sharing is currently in [public preview](/release-phases) with the following restrictions:

- You can only share payment methods if the [type](/api/payment_methods/object#payment_method_object-type) is `card`. This includes cards that originate from a [wallet](/payments/wallets), including Apple Pay, Google Pay, and Link.
- You can attach other payment methods (such as ACH or Klarna) to a shared customer in one account, but they won’t be shared to other accounts in your organization.
- You can’t disable sharing after enabling the feature.
- You can’t share customers or payment methods between connected accounts, unless the connected accounts directly belong to an organization.
- You can’t selectively share individual customers or payment methods. When you turn on sharing, all customers and payment methods are shared.
- You can’t charge shared cards issued from India off session.

## Before you begin

1. [Create an organization](/get-started/account/orgs/build#create-org) across your [multiple standalone accounts](/get-started/account/orgs/setup#standalone-accounts).
2. [Create a sandbox environment](/get-started/account/orgs/build#create-organization-sandboxes) for your organization and its accounts so you can test your integration before putting it in production.

#### Get customer consent

Your customers must consent to share customer data and payment methods before you enable sharing across your accounts and legal entities. Consent collection is the responsibility of merchants, not Stripe.

## Enable sharing for accounts within your organization

You can enable sharing for a specific group of accounts in your organization or for all accounts.

1. From your [organization settings](https://dashboard.stripe.com/org/settings) in the Dashboard, click **Customer and payment method sharing** to get started.
2. Select the accounts to enable sharing for, and click **Share**. You must select at least two.
3. Name your sharing group. Accounts can only belong to one group.
4. Check the box to confirm that you obtained consent from your customers to share contact and payment method information across accounts in your organization.
5. Click **Enable**.

#### Sharing is irreversible

You can enable sharing for unshared accounts at any time, but you can’t revert sharing for enabled accounts. You must contact Stripe if you want to disable sharing.

## How sharing works

After one account in the sharing group creates a customer, Stripe automatically creates that customer in all other accounts in the group. Each account in the sharing group maintains its own instance of the shared customer, but all instances have the same customer ID.

Any account in the sharing group can update the customer through the Dashboard or the API. Updates to the following fields of the `Customer` object sync across all account instances in the sharing group:

- [name](/api/customers/object#customer_object-name)
- [email](/api/customers/object#customer_object-email)
- [address](/api/customers/object#customer_object-address)
- [phone](/api/customers/object#customer_object-phone)
- [description](/api/customers/object#customer_object-description)
- [tax\_id](/api/customers/object#customer_object-tax-ids)
- [preferred\_locales](/api/customers/object#customer_object-preferred_locales)

Updates to other fields within an account save to the `Customer` instance of the account making the update, but don’t sync to other accounts in the sharing group. It’s possible for the same customer to have different values for the same unshared field across different account instances. This protects the integrity of customer data that might be proprietary, sensitive, or only relevant to one account.

### Payment methods

Unlike Customer instances, Stripe creates the payment method only in the originating account. However, any account in the sharing group can charge, update, and even delete this single payment method instance. Updating a shared payment method (including removal) affects its attached customers on all accounts in the sharing group. However, the following activity only applies to the originating account:

- Stripe generates `payment_method.<action>` events only for the originating account.
- Stripe charges [Card Account Updater (CAU)](/get-started/data-migrations/payment-method-imports#cau) fees only to the originating account.

### Event behavior

If an account updates any of the shared fields for a customer, Stripe generates separate `customer.updated` events for each account in the sharing group. If an account updates an unshared field for the customer, Stripe sends the `customer.updated` event to only that account.

If an account attaches a payment method to a customer, Stripe generates a single `payment_method.attached` event for only the originating account.

We recommend all accounts in a sharing group listen for events using an [organization-level webhook](/webhooks#webhook-endpoint-def) so you’re aware of shared payment method activity.

## Sample integration use cases Server-side

The following sections provide code samples that illustrate how accounts in an organization sharing group might retrieve and use shared data. These examples reflect an organization with the following setup:

### Create a Customer during checkout

A customer makes a payment to one of the accounts in a sharing group (Rocket Rides). The [CheckoutSession](/api/checkout/sessions/create) enables `customer_creation` and `payment_method_save`.

server.js

```
const stripe = require('stripe')('{{SECRET_KEY_ROCKET_RIDES}}');

const session = await stripe.checkout.sessions.create({
  customer_creation: 'always',
  line_items: [
    {
      price_data: {
        currency: 'usd',
        product_data: {
          name: 'ride_service',
        },
        unit_amount: 2000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  ui_mode: 'embedded',
  return_url: 'https://checkout.rocket-rides.com/checkout/return?session_id={CHECKOUT_SESSION_ID}',
  saved_payment_method_options: {
    payment_method_save: 'enabled',
  },
});
```

After payment completion, Stripe shares the new customer and payment method to the other accounts in the sharing group. Stripe triggers the following events:

- `customer.created` for each account’s instance of the customer
- `payment_method.attached` event for only the originating account

### Update shared customer data from another account

Rocket Deliveries updates the shared customer originally saved by Rocket Rides.

server.js

```
const stripe = require('stripe')('{{SECRET_KEY_ROCKET_DELIVERIES}}');

const customer = await stripe.customers.update(

'{{CUSTOMER_ID}}'

,
  {
    email: 'jenny@example.com',
    metadata: {
      door: "front"
    },
  }
);
```

Stripe triggers the `customer.updated` event for each account in the sharing group:

- Each account’s instance of the customer gets the `email` update.
- Only Rocket Delivery’s account gets the `metadata_door` update, because it’s not a shared field.

### Retrieve a customer’s shared payment methods

All accounts in a sharing group can list a customer’s saved card type payment methods to use or update them.

If a customer has multiple payment methods saved across many accounts in a sharing group, Stripe limits the retrieval accounts to prioritize performance. We retrieve payment methods from only the requesting account and the four accounts with the most recently attached payment methods.

server.js

```
const stripe = require('stripe')('{{SECRET_KEY_ROCKET_REPAIRS}}');

const paymentMethods = await stripe.customers.listPaymentMethods(

'{{CUSTOMER_ID}}'

);
```

### Update a customer’s shared payment methods

Updates to a shared payment method (including removal) sync to all accounts in the sharing group and trigger the `payment_method.updated` or `payment_method.detached` event.

server.js

```
const stripe = require('stripe')('{{SECRET_KEY_ROCKET_REPAIRS}}');

const paymentMethod = await stripe.paymentMethods.update(

'{{PAYMENT_METHOD_ID}}'

,
  {
    "billing_details": {
      "address": {
        "city": "South San Francisco",
        "country": "us",
        "line1": "354 Oyster Point Boulevard",
        "line2": null,
        "postal_code": "94080",
        "state": "CA"
      },
    },
  }
);
```

#### Consider recurring payments

Changes to payment methods can affect ongoing subscriptions using that payment method, so exercise caution.

### Accept a payment using a shared payment method Server-side

You can charge a payment method saved in one account (for example, Rocket Rides) for a payment created by another account in the sharing group (for example, Rocket Repairs).

server.js

```
const stripe = require('stripe')('{{SECRET_KEY_ROCKET_REPAIRS}}');

const session = await stripe.checkout.sessions.create({
  customer:

'{{CUSTOMER_ID}}'

,
  line_items: [
    {
      price_data: {
        currency: 'usd',
        product_data: {
          name: 'tow_service',
        },
        unit_amount: 5000,
      },
      quantity: 1,
    },
  ],
  mode: 'payment',
  ui_mode: 'embedded',
  return_url: 'https://checkout.rocket-repairs.com/checkout/return?session_id={CHECKOUT_SESSION_ID}',
  saved_payment_method_options: {
    payment_method_save: 'enabled',
  },
});
```

Payments appear on the **Transactions** page for the corresponding account and the organization. Accounts can’t see each other’s payments, even when they’re part of the sharing group.

### Create a subscription using a shared payment method Server-side

You can also create a subscription for a customer originally saved by another account in the sharing group.

server.js

```
const stripe = require('stripe')('{{SECRET_KEY_ROCKET_REPAIRS}}');

const session = await stripe.checkout.sessions.create({
  customer:

'{{CUSTOMER_ID}}'

,
  line_items: [
    {
      price_data: {
        currency: 'usd',
        product_data: {
          name: 'basic-roadside-service',
        },
        unit_amount: 2500,
      },
      quantity: 1,
    },
  ],
  mode: 'subscription',
  ui_mode: 'embedded',
  return_url: 'https://checkout.rocket-repairs.com/checkout/return?session_id={CHECKOUT_SESSION_ID}',
  saved_payment_method_options: {
    payment_method_save: 'enabled',
  },
});
```