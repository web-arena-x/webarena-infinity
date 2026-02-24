# Create subscriptions

Source: https://docs.stripe.com/no-code/subscriptions

---

Create subscriptions

[Create account](https://dashboard.stripe.com/register/billing) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Fsubscriptions)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Fsubscriptions)

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

[Quickstarts](/quickstarts)

Start developing

[Build with an LLM](/building-with-llms)

Use Stripe without code

[Overview](/no-code)

[Find your use case](/no-code/get-started)

[Create Payment Links](/no-code/payment-links)

[Create a buy button](/no-code/buy-button)

[Send invoices](/no-code/invoices)

Create subscriptions

[Send quotes](/no-code/quotes)

[Accept in-person payments](/no-code/in-person)

[Pay out money](/no-code/payout)

[Set up customer portal](/no-code/customer-portal)

[Dashboard assistant](/assistant)

Migrate to Stripe

Common use cases

[Overview](/get-started/use-cases)[Accept simple payments as a startup](/get-started/use-cases/startup)[Sell subscriptions as a SaaS startup](/get-started/use-cases/saas-subscriptions)[Build a subscriptions solution with usage-based pricing](/get-started/use-cases/usage-based-billing)[Accept payments in person](/get-started/use-cases/in-person-payments)[Send invoices to collect payments](/get-started/use-cases/invoices)

United StatesEnglish (United States)

# Create subscriptions

## Set up recurring payments by offering subscriptions to your service.

Ask about this page

Copy for LLMView as Markdown

- **Stripe compatibility:** Payment Links, customer portal
- **Requires:** Stripe account
- **Good for:** SaaS businesses, individual creators, e-commerce businesses
- **Pricing:** [Stripe Billing pricing](https://stripe.com/billing/pricing) for recurring payments

Subscriptions represent what your customer is paying for and how much and how often you’re charging them for the product. You can subscribe customers manually through the Dashboard. You can also let them sign up through your website or a [Payment Link](/payment-links/create?pricing-model=standard).

This page shows you how to manually create and edit a subscription in your Stripe Dashboard.

## Create a subscription

To create a subscription:

1. In the Stripe Dashboard, go to the [subscriptions](https://dashboard.stripe.com/test/subscriptions) page.
2. Click **+Create subscription**.
3. Find or add a customer.
4. Enter the pricing and product information. You can add multiple products.
5. Set the start and end date of the subscription.
6. Set the starting date for the billing cycle. This defines when the next invoice is generated. Depending on your settings, the saved payment method on file might also be charged automatically on the billing cycle date. Learn more about the [billing cycle date](/billing/subscriptions/billing-cycle).
7. (Recommended) [Configure email reminders and notifications](/invoicing/send-email#email-configuration) for subscribers.
8. (Optional) Add the default tax behavior, a coupon, a free trial, or metadata.
9. (Optional) Enable [revenue recovery](/billing/revenue-recovery) features in the Dashboard, which can help you reduce and recover failed subscription payments. You can automatically retry failed payments, build custom automations, configure customer emails, and so on.

### Advanced options

## Edit a subscription

To edit a subscription:

1. Go to the [subscriptions](https://dashboard.stripe.com/test/subscriptions) page.
2. Find the subscription you want to modify, click the overflow menu (), then click **Update subscription**. You can also click the pencil icon () next to the subscription name. From this menu, you can also:

   - **Cancel the subscription**: Select a date to cancel the subscription immediately, at the end of the current period, or on a custom date. You can also select the option to refund the last payment for this subscription and create a [credit note](/invoicing/dashboard/credit-notes) for your records.
   - **Pause payment collection**: Select the duration of the pause (indefinite or ending on a custom date) and how invoices should behave during the pause.
   - **Share payment update link**: Generate a link the customer can use to [update the subscription payment method](/billing/subscriptions/payment-methods-setting#update-payment-method).
3. Make your changes to the subscription.
4. Click **Update subscription**.

## Delete a subscription

You can’t delete a subscription. But you can cancel it or pause payment collection. See [editing a subscription](#edit-susbscription) for those details.

## Subscriptions on mobile

Use the [Stripe Dashboard mobile app](/dashboard/mobile) to create or manage subscriptions on your mobile device. (Currently only available on [iOS](https://apps.apple.com/app/apple-store/id978516833?pt=91215812&ct=stripe-docs-subscriptions-nc&mt=8) only.)

1. Go to the **Customers** tab.
2. Select a customer.
3. Tap the plus sign (**+**) in the subscription row. Alternatively, tap the overflow menu (), and select **Create subscription**.

You can only select existing products with a recurring price.

### Cancel a subscription from the mobile app

1. Go to **Payments > Subscriptions**.
2. Select an active subscription.
3. Tap **Cancel Subscription** in the action bar.

You can’t pause subscriptions using the app.