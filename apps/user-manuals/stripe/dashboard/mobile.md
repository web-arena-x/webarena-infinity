# Stripe Dashboard mobile app

Source: https://docs.stripe.com/dashboard/mobile

---

Mobile Dashboard

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdashboard%2Fmobile)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdashboard%2Fmobile)

[Get started](/get-started)

[Payments](/payments)

[Revenue](/revenue)

[Platforms and marketplaces](/connect)

[Money management](/money-management)

[Developer resources](/development)

APIs & SDKsHelp

[Overview](/development)

Versioning

Changelog

[Upgrade your API version](/upgrades)

Upgrade your SDK version

Essentials

SDKs

API

Testing

Stripe CLI

Sample projects

Tools

Stripe Dashboard

[Web Dashboard](/dashboard/basics)

Mobile Dashboard

[Search in the Dashboard](/dashboard/search)

Workbench

Developers Dashboard

[Stripe for Visual Studio Code](/stripe-vscode)

Terraform

Features

Workflows

Event destinations

[Stripe health alerts](/health-alerts)[File uploads](/file-upload)

AI solutions

Agent toolkit

[Model Context Protocol](/mcp)[Build agentic AI SaaS Billing workflows](/agents-billing-workflows)

Security and privacy

Security

[Stripebot web crawler](/stripebot-crawler)

Privacy

Extend Stripe

Build Stripe apps

Use apps from Stripe

Partners

Partner ecosystem

[Partner certification](/partners/training-and-certification)

United StatesEnglish (United States)

# Stripe Dashboard mobile app

## Learn how to use the mobile app version of the Stripe Dashboard.

Ask about this page

Copy for LLMView as Markdown

Stripe offers a mobile application to access the Dashboard for both iOS and Android devices. Use the app to view business metrics, track and manage payments and customers, and initiate payouts. You can also accept in-person payments (such as Tap to Pay) and create payment links, basic invoices, and subscriptions.

## Download the mobile app

Download the appropriate app for your device:

[iOS on App Store](https://apps.apple.com/app/apple-store/id978516833?pt=91215812&ct=stripe-docs-mobile&mt=8) [Android on Google Play](https://play.google.com/store/apps/details?id=com.stripe.android.dashboard&pli=1)

## Use the mobile app

When you’re ready to use the mobile app, you must [create a Stripe account](https://dashboard.stripe.com/register) or log into your existing account. If you’re using the iOS version, you can create a Stripe account from the mobile app.

Then, enable [two-factor authentication](https://support.stripe.com/questions/update-the-phone-number-for-two-step-authentication) and [verify your phone number](https://dashboard.stripe.com/settings/user) in the Dashboard.

## App capabilities

The app is available in 14 languages, and automatically defaults to the device language set in your system preferences. If you manage a [Connect](/connect) business, the app is also available to connected accounts that have full access to the Stripe Dashboard.

| [Monitor your business](/dashboard/mobile#monitor-business-metrics) | - Dashboard charts - Payment and customer list, and detail screens - Push notifications for new payments, alerts, and daily summary - Search across your entire business - iOS lock screen widgets - Android home screen widgets |
| [Accept online or in-person payments](/dashboard/mobile#accept-payments-on-mobile) | - Tap to pay - Payment links (iOS only) - Invoices (basic creation only) - Subscriptions (iOS only) - Manual card entry |
| [Manage payments](/dashboard/mobile#manage-payments) | - Issue refunds - Activate, deactivate, or share payment links (iOS only) - Cancel a subscription (iOS only) - Send and view receipts |
| [Create payouts](/dashboard/mobile#create-and-manage-payouts) | - View balances - Initiate an instant or standard payout - Track the status of bank transfers |
| [Create and manage customers](/dashboard/mobile#create-and-manage-customers) | - Create or edit a customer - Add a card on file (iOS only) - Send an email |

### Limitations

The app only displays live mode data. Stripe users with the **View only** role can’t create payments, refunds, or payouts in the app. Inactive Stripe accounts and users with the **Support specialist** role can’t log in to the app. For more information, see [User roles](/get-started/account/teams/roles).

## Monitor business metrics

The app’s home page has various charts providing account information. You can customize this page to stay informed about your financial data.

The Dashboard displays data in your default currency. If you receive payments in multiple currencies, Stripe home charts convert these to your default currency using sample exchange rates. These conversions are estimates and won’t exactly match with settled amounts because of fluctuating exchange rates.

To explore and manage available charts for iOS:

1. Tap **Edit** next to the **Reports overview** title.
2. Add, remove, or reorder charts as needed.

To explore and manage available charts for Android:

1. On the **Home** tab, scroll down to the bottom, and click **Add or edit charts**.
2. Add, remove, or reorder charts as needed.

### Push notifications

Push notifications are messages sent directly to a user’s device from a mobile app. To [enable push notifications from the app](https://support.stripe.com/questions/enabling-notifications-on-the-stripe-dashboard-mobile-app), you must allow notifications from Stripe in the settings of your phone.

Types of notifications include:

- Daily summary
- New payments
- New customers
- Disputed payments
- Deposited transfers

### Widgets

Widgets are available on [iOS](https://support.apple.com/guide/iphone/add-edit-and-remove-widgets-iphb8f1bf206/17.0/ios/17.0) and [Android](https://developer.android.com/develop/ui/views/appwidgets/overview) to provide a faster way to manage your business metrics.

To add widgets to your iOS lock screen:

1. Touch and hold the **Lock Screen** until **Customize** button appears at the bottom of the screen
2. Tap **Customize**, then tap **Lock Screen**.
3. Select any of the 17+ metrics, and set the time range and account you want.
4. Tap **Add** or **Done**.

| Widget type | iOS | Android |
| --- | --- | --- |
| Home | | 4 metric widgets, such as: - Daily gross volume - Daily new payments - Daily new customers - Daily net volume |
| Lock screen | 17 metric widgets, such as: - Monthly recurring revenue - Net volume from new sales - High risk payments - Dispute activity | |

## Accept payments on mobile

You can accept and manage in-person or online payments from the Stripe Dashboard mobile app, such as:

| Payment capability | Description | iOS | Android |
| --- | --- | --- | --- |
| [Tap to pay](/no-code/in-person) | Accept in-person payments through a contactless card without needing a hardware reader | | |
| [Manual card entry](https://support.stripe.com/questions/b7bd8ea6-d20c-40f8-a273-4d6c4902957a) | A transaction where you enter a customer’s card details and process it in the Stripe Dashboard | | |
| [Invoices](/no-code/invoices) | Use invoices to collect one-time or recurring payments from a specific customer. | | |
| [Payment links](/no-code/payment-links) (including QR codes) | Reusable links that take your customers to a prebuilt checkout page | | |
| [Subscriptions](/no-code/subscriptions) | Recurring payments for your products or services | | |

To accept payments on mobile:

1. Verify you meet the following requirements:
   - Confirm if your [user role](/get-started/account/teams/roles) can accept payments. Users with the **Support specialist** and **View-only** roles can’t accept payments.
   - For contactless payments (such as Tap to pay), confirm if your country [accepts in-person payment features](/terminal/payments/collect-card-payment/supported-card-brands).
   - If you haven’t already, enable [2FA](https://support.stripe.com/questions/update-the-phone-number-for-two-step-authentication), and [verify your phone number](https://dashboard.stripe.com/settings/user).
2. Open the Stripe Dashboard mobile app, and tap the plus symbol ().
3. Select either:
   - **Charge a card or send an invoice**: To accept **[Tap to pay](/no-code/in-person)**, **Hosted Invoice**, or **Manually Charge Card**.
   - **Create a payment link**: To share a link or a QR code to a customer

#### Create subscriptions on iOS

Go to the **Customers** tab, select a customer, and then tap the **create icon (+)** icon in the subscription row. Alternatively, tap the overflow menu (), and select **Create subscription**. You can only select existing products with a recurring price.

Loading video content...

## Manage payments

You can manage payments from your app:

### Issue a refund

1. Tap the **Payments** tab.
2. Select a successful payment.
3. Go to the action bar at the bottom, and tap **Refund**.
4. Enter the amount you want to refund, and select if you want to make a partial refund.

### Send and view receipts

1. Tap the **Payments** tab.
2. Select a successful payment.
3. Go to the action bar at the bottom, tap the overflow menu (), and select **View receipt** or **Send receipt**. You can also send a receipt directly after accepting a Tap to Pay payment from the success screen. After you complete the payment, tap **Send receipt**.

### Activate, deactivate, or share payment links (iOS only)

1. Tap the **Payments** tab.
2. Tap **Payment Links**, and select the active payment link you want to change.
3. You can copy the link, generate a QR code, or open the payment link in the web Dashboard. If you deactivate a payment link, it immediately deactivates without a confirmation prompt. If you deactivate a payment link by accident, reactivate it by tapping **Activate** in the action bar at the bottom of the screen.

### Cancel a subscription (iOS only)

1. Tap the **Payments** tab.
2. Tap **Subscriptions**, and select an active subscription.
3. Go to the action bar at the bottom, and tap **Cancel subscription**.
4. Confirm if you want to cancel the subscription immediately or at the end of the billing period.

## Create and manage payouts

1. Verify you have a [debit card or external account linked to your Stripe account](/get-started/account/linked-external-accounts#link-financial-account).
   - Currently, you can only link these accounts through the [web version](https://dashboard.stripe.com/settings/payouts) of the Stripe Dashboard.
   - If you want to use instant payouts, use a debit card or bank account that [supports instant payouts](/payouts/instant-payouts-banks).
2. Open the Stripe Dashboard mobile app on your device and log in.
3. Go to the **Balances** tab at the bottom of the screen. Alternatively, you can tap the plus symbol () at the top right of any tab and select **Pay out funds**.
4. Check your balance:
   - **Standard payouts**: If you have a positive balance, you can start the payout process by entering the amount you want to pay out. For more information, see [Receive payouts](/payouts).
   - **Instant payouts**: Funds acquired from card payments are available as soon as the charge is complete. ACH or bank debits are only available after the payment has settled in the Stripe account. For more information, see [Instant payouts for Stripe Dashboard users](/payouts/instant-payouts).
5. Complete your payout. The time it takes for funds to settle in the bank account depends on several factors, including whether you select a standard or instant payout:
   - **Standard payouts**: The time it takes for funds to appear in your account depends on your industry, country, and whether it’s your first payout. It takes around 7 days for funds to settle in the applicable bank account for your first payout.
   - **Instant payouts**: After Stripe verifies your account is eligible to send instant payouts, funds typically settle in the applicable bank account within 30 minutes.

## Create and manage customers

To create a new customer:

1. Tap the plus icon () at the top right of any tab, and select **Create a customer**.
2. Enter the customer’s name, email address, and a description.

To manage existing customers:

1. Tap the **Customer** icon () from the app’s navigation bar, and select a customer. You can view their past payments, subscriptions, invoices, and payment cards saved on file.
2. Go to the action bar at the bottom to:
   - Add a card on file
   - Send customers an email
   - Edit their details, or open the customer details in the web Dashboard