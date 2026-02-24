# Accept in-person payments without writing code

Source: https://docs.stripe.com/no-code/in-person

---

Accept in-person payments

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Fin-person)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Fin-person)

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

[Create subscriptions](/no-code/subscriptions)

[Send quotes](/no-code/quotes)

Accept in-person payments

[Pay out money](/no-code/payout)

[Set up customer portal](/no-code/customer-portal)

[Dashboard assistant](/assistant)

Migrate to Stripe

Common use cases

[Overview](/get-started/use-cases)[Accept simple payments as a startup](/get-started/use-cases/startup)[Sell subscriptions as a SaaS startup](/get-started/use-cases/saas-subscriptions)[Build a subscriptions solution with usage-based pricing](/get-started/use-cases/usage-based-billing)[Accept payments in person](/get-started/use-cases/in-person-payments)[Send invoices to collect payments](/get-started/use-cases/invoices)

United StatesEnglish (United States)

# Accept in-person payments without writing code

## Use the Stripe Dashboard mobile app or Stripe Terminal Reader to accept in-person payments.

Ask about this page

Copy for LLMView as Markdown

To accept in-person payments without writing any code, **Tap to Pay with Stripe Dashboard** allows you to process in-person, contactless payments using only your phone. To get started with Tap to Pay, download the Stripe Dashboard mobile app on [iOS](https://apps.apple.com/app/apple-store/id978516833?pt=91215812&ct=stripe-mobile-app-ttp-doc-page&mt=8) or [Android](https://play.google.com/store/apps/details?id=com.stripe.android.dashboard) and log in with your Stripe account.

## Before you begin

Before you start setting up, make sure that you meet the requirements below and operate in a supported country.

If you’re new to Stripe, [set up and activate a new account](https://dashboard.stripe.com/register/).

| | **Tap to Pay with Stripe Dashboard** | |
| **Good for** | In-person payments without your own app or terminal | |
| **Pricing** | [Pay-as-you-go for Terminal and Tap to Pay](https://stripe.com/pricing#terminal) | |
| **Compatible with** | - Contactless cards (Visa, MC, Amex, Discover) - NFC mobile wallets (Apple Pay, Google Pay, and Samsung Pay) | |
| **To get started** | Use the Stripe Dashboard app in the App Store and Google Play: - [Download the iOS app from the App Store](https://apps.apple.com/app/apple-store/id978516833) - [Download Android app on Google Play](https://play.google.com/store/apps/details?id=com.stripe.android.dashboard) | |
| **Requirements** | - [Stripe account](/get-started/account) - Stripe [iOS](https://apps.apple.com/app/apple-store/id978516833?pt=91215812&ct=stripe-mobile-app-ttp-doc-page&mt=8) or [Android](https://play.google.com/store/apps/details?id=com.stripe.android.dashboard) Dashboard app - Location permissions enabled - **iOS:** iPhone XS or later. The device must have a passcode set and be signed into iCloud. Apple’s [Business Register documentation](https://register.apple.com/login?returnTo=/docs-service-api/readme/redirect/tap-to-pay-on-iphone/docs/sdk-and-api-guide#ios-versions-and-deprecation-management) lists supported iOS versions. - **Android:** A [supported Android device](/terminal/payments/setup-reader/tap-to-pay?platform=android#supported-devices) | |
| **Supported countries** | The Stripe Dashboard app is available on iOS and Android in the following countries. Australia Austria Belgium Bulgaria Canada Croatia Cyprus Czech Republic Denmark Estonia Finland France Germany Gibraltar\* Hungary Ireland Italy Japan\* Latvia Liechtenstein Lithuania Luxembourg Malaysia\* Malta Netherlands New Zealand Norway Poland Portugal Puerto Rico\* Romania Singapore Slovakia Slovenia Spain Sweden Switzerland United Kingdom United States Note Tap to Pay on iOS isn’t available in Gibraltar, Malaysia, or Puerto Rico. Tap to Pay on Android isn’t available in Japan. | |

## Tap to Pay with Stripe Dashboard

#### Enable NFC

Before accepting Tap to Pay contactless payments, you must enable NFC on your mobile device.

1. Open your Stripe Dashboard mobile app.
2. Tap the add symbol () from any tab.
3. Select **Charge a card or send an invoice**.
4. Enter the amount to charge.
5. Select **Tap to Pay** as your payment acceptance option.
6. When the Tap to Pay symbol appears, prompt your customer to tap their card to the device by following the instructions on screen.
7. The payment confirmation page signals successful completion of the transaction.

If you’re unable to accept a Tap to Pay payment in the Dashboard app, you have other options:

- **Manually charge a card**: Open the Stripe Dashboard app, click the add symbol () from any tab, and select **Charge a card or send an invoice**. Then, enter your customer’s card information manually.
- **Generate a QR code**: Create a [payment link](/no-code/payment-links) and have your customer scan the QR code to pay. You can also [share a payment link](/payment-links/share) through text, email, and other channels.

#### For developers

If you want to build an in-person payment solution, see the [Terminal integration guide](/terminal/designing-integration).

## Payment considerations

### Charge limits

The same maximum and minimum charge amounts apply when accepting payments in-person as accepting payments online. For more information on limits, see [Minimum and maximum charge amounts](/currencies#minimum-and-maximum-charge-amounts).

### Strong Customer Authentication

Strong Customer Authentication (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is required for customer-initiated electronic payments within the [European Economic Area (EEA)](https://en.wikipedia.org/wiki/European_Economic_Area). See [Regional Considerations](/terminal/payments/regional?integration-country=BE#strong-customer-authentication) for more detail on how Terminal supports SCA requirements.

Related Guides

[Tap to Pay integration guide for app developers](/terminal/payments/setup-reader/tap-to-pay)