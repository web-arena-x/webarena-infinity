# Web Dashboard

Source: https://docs.stripe.com/dashboard/basics

---

Web Dashboard

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdashboard%2Fbasics)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdashboard%2Fbasics)

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

Web Dashboard

[Mobile Dashboard](/dashboard/mobile)

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

# Web Dashboard

## Learn how to use the web version of the Stripe Dashboard.

Ask about this page

Copy for LLMView as Markdown

The [Stripe Dashboard](https://dashboard.stripe.com/) is the user interface where you manage and configure your account. You can use the Dashboard to navigate account resources, [search transactions](/dashboard/search), invite team members, monitor your integration, and more. On your keyboard, press the question mark key (`?`) for a list of available keyboard shortcuts for common actions.

The Dashboard officially supports the following web browsers:

- The last 20 major versions of Chrome, Firefox, and Edge.
- The last 4 major versions of Safari.

If you don’t have access to the Dashboard, [activate your account](/get-started/account/activate).

## Primary navigation

In the Dashboard, the first section of the sidebar is where you can access and act on information related to your balances, transactions, customers, and products.

### Home

The [Home](https://dashboard.stripe.com/dashboard) page provides analytics and charts about your business performance. It also surfaces important notifications, like unresolved disputes or identity verifications. To customize this page:

1. Click **Add** under **Your overview**.
2. Add or remove widgets by selecting or unselecting them.
3. Click **Apply** to save your changes. You can also click **Edit** to remove widgets.

### Balances

Use [Balances](https://dashboard.stripe.com/balances) to see your Stripe balance, including top-ups, payouts, and transaction history.

### Transactions

Use [Transactions](https://dashboard.stripe.com/payments) to view all your customer payments, including collected fees and transfers, and their status. You can filter your transactions or export them if you want to use the data outside of Stripe.

If you use [Organizations](/get-started/account/orgs), you can see a detailed list of payments across all of your accounts. You can also filter the list down by account.

### Customers

Use [Customers](https://dashboard.stripe.com/customers) to create and manage customer profiles. You can see information about your existing customers, including their accounting details, using filters to locate specific customers. Click a customer’s name to see more details, including subscriptions, payments, payment methods, invoices, and quotes. To learn more, see [Create customers](/invoicing/customer).

If you use [Organizations](/get-started/account/orgs), you can view a list of your shared and unshared customers across all your accounts. You can filter this list by email address, card status, creation date, account type, and delinquency status. When you click into a customer, there’s also a link to the customer’s details page within the account they belong to.

#### Note

You can only create, export or analyze customers from the **Customers** page at the account level.

### Product catalog

The [Product catalog](https://dashboard.stripe.com/products) lets you create and manage products and prices for your business. Click your product to see more details. To learn more, see [Manage products and prices](/products-prices/manage-prices).

## Shortcuts

Use the **Shortcuts** section to display your pinned and most recently visited pages. After you visit a page, it apperas under this section, where you can pin it.

## Products

Use the **Products** section to complete tasks, and view important product information.

### Connect

If your business is a platform or marketplace, and you have [connected accounts](https://dashboard.stripe.com/connect), the Stripe Dashboard allows you to also manage and support them. To learn more, see [Managing connected accounts](/connect/dashboard).

### Payments

Payments contains insights and tools for improving your payments performance, including card authorization rates, fraud prevention, and dispute management. Here, you can review insights and opportunities for improving your card authorization rates, address any disputes, and manage fraudulent payments with [Radar](https://dashboard.stripe.com/radar).

[Payment links](https://dashboard.stripe.com/payment-links) let you accept payments or sell subscriptions without building an additional standalone website or application. To learn more, see [Payment Links](/payment-links).

[Terminal readers](https://dashboard.stripe.com/setup/terminal/activate) are a selection of pre-certified readers that accept EMV, contactless, and swiped payments, encrypt sensitive card information, and return a token to your application for payment confirmation. To learn more, see [Terminal](/terminal).

### Billing

[Billing](https://dashboard.stripe.com/billing) lets you manage and configure your billing and subscription-related information, such as creating, customizing, and sending invoices to customers, and managing subscriptions, applying discounts, and generating revenue reports. To learn more, see [Billing](/billing).

### Reporting

[Reporting](https://dashboard.stripe.com/reports/hub) allows you to export historical transactions, payments, and payouts information from the Dashboard. You can customize the reports by filtering and adding custom columns, and access financial reports for an accounting-grade view. To learn more, see [Reports](/stripe-reports).

In addition to the general financial reporting available in the Dashboard, Billing, Tax, and Radar offer product-specific analytics for additional performance insights.

If you need more customized reporting, [Sigma](https://dashboard.stripe.com/sigma/queries) lets you access and analyze your data within an interactive SQL environment. While [Data management](https://dashboard.stripe.com/data-management), lets you import external data into Stripe. Learn more at [Stripe data](/stripe-data).

To automate your accrual accounting process, use [Revenue Recognition](https://dashboard.stripe.com/revenue-recognition). To learn more, see [Revenue Recognition](/revenue-recognition).

### Other Stripe products

To see additional Stripe products in the Dashboard, click **More**:

- [Workflows](https://dashboard.stripe.com/workflows): Automate tasks and create custom flows, without writing code. Workflows help you automate multi-step tasks and can span across multiple Stripe products. To learn more, see [Stripe Workflows](/workflows).
- [Tax](https://dashboard.stripe.com/tax/thresholds): Automate sales tax, VAT, and GST compliance on all your transactions. To learn more see, [Stripe Tax](/tax).
- [Connect](https://dashboard.stripe.com/connect) (if disabled): For platforms or marketplaces who want to route payments between multiple parties. To learn more, see [Connect](/connect).
- [Identity](https://dashboard.stripe.com/identity): Confirm the identity of global users to prevent fraud and streamline risk operations. To learn more, see [Identity](/identity).
- [Atlas](https://dashboard.stripe.com/setup/atlas/activate): Start a US company from anywhere in the world. To learn more, see [Atlas](/atlas).
- [Issuing](https://dashboard.stripe.com/issuing/overview): Create, manage, and distribute payment cards for your business. To learn more, see [Issuing](/issuing).
- [Financial connections](https://dashboard.stripe.com/settings/financial-connections): Allow users to securely share their financial data with your business. To learn more, see [Financial Connections](/financial-connections) to learn more.
- [Capital](https://dashboard.stripe.com/capital): Financing offers for eligible businesses processing payments through Stripe. To learn more, see [Capital](/capital/how-stripe-capital-works).
- [Climate](https://dashboard.stripe.com/climate): Remove carbon as you grow your business. To learn more, see [Climate](/climate).

## Dashboard settings

The Dashboard’s settings are broken into three categories: Personal, Account, and Product.

### Account settings

You can manage your [business settings](https://dashboard.stripe.com/settings) directly from the Dashboard. Business settings include:

- [Account details](https://dashboard.stripe.com/settings/account), account health, public information, payouts, legal entity, custom domains, and so on.
- [Personal details](https://dashboard.stripe.com/settings/user) settings, password, communication preferences, and your active sessions.
- [PCI compliance details](https://dashboard.stripe.com/settings/compliance) and Stripe’s Attestation of Compliance.
- [Viewing and uploading documents](https://dashboard.stripe.com/settings/documents), legacy exports, and PCI compliance.
- [Get early access](https://dashboard.stripe.com/settings/early_access) to new beta features.

Under **Team and security**, you can [invite team members](https://dashboard.stripe.com/settings/team?invite_shown=true) to access the Dashboard, and help manage your business. Each of them can have different levels of access. For example, you can let members of your customer service team access your Dashboard for the purpose of handling [refunds](/refunds) and [disputes](/disputes/responding). To learn more about team roles, see [User roles](/get-started/account/teams/roles).

You can customize your customer’s payment forms, emails, invoices, and quotes with the public details you set for your business. You can also upload your logo or icon and aelect colors in your [Branding](https://dashboard.stripe.com/settings/branding) settings. Learn more about [branding your Stripe configuration](/get-started/account/branding).

If you’re using Stripe Checkout, you can also [customize your policies and contact information](https://dashboard.stripe.com/settings/checkout) to display to your customers.

### Product settings

Manage the settings for individual Stripe products directly from the Dashboard. Product settings include:

- [Billing](https://dashboard.stripe.com/settings/billing/automatic): Manage subscriptions, invoices, quotes, and customer portal.
- [Financial connections](https://dashboard.stripe.com/settings/financial-connections): Manage appearance, featured institutions, optimizations and usage details.
- [Radar](https://dashboard.stripe.com/settings/radar): Manage fraud protection and customization capabilities for your account.
- [Card issuing](https://dashboard.stripe.com/settings/issuing/authorizations): Manage authorizations, balance notifications, card branding, and digital wallets.
- [Identity verification](https://dashboard.stripe.com/settings/identity): Use synthetic identity protection and the native mobile SDK.
- [Sigma custom reports](https://dashboard.stripe.com/settings/sigma): Manage your Sigma subscription.
- [Connect](https://dashboard.stripe.com/settings/connect): Manage your platform and connected accounts.
- [Payments](https://dashboard.stripe.com/settings/checkout): Manage user checkout, payment methods, currency conversion, and so on.
- [Tax](https://dashboard.stripe.com/settings/tax): Manage head office address, preset tax code, default tax behavior, and tax integrations.
- [Data pipeline](https://dashboard.stripe.com/settings/stripe-data-pipeline): Manage an external data warehouse.

## Monitor and test your integration

[Workbench](https://dashboard.stripe.com/workbench) gives you information about the performance and health of your integration. You can view your API and [webhook](/webhooks) usage, upgrade your API version, and review API errors that can be filtered by endpoint or type. To access Workbench, enable it under **Beta features** in the [Dashboard](https://dashboard.stripe.com/settings/early_access). To learn more, see [Workbench](/workbench).

Workbench also [logs](https://dashboard.stripe.com/workbench/logs) every successful or failed request made using your API keys. Each log contains details about the original request, whether it succeeded or failed, the response from Stripe, and a reference to any related API resources.

To test your integration, use [Sandboxes](/sandboxes) to simulate and test your integrations without impacting live transactions or affecting real data.

## Mobile Dashboard app

Like the web version of the Dashboard, you can use our [mobile app](/dashboard/mobile) to monitor your business metrics, create and manage payments, track and initiate payouts, get push notifications on business activity, and so on. The app is available on iOS and Android in 14 languages.

To download the mobile app, go to:

- [iOS on App Store](https://apps.apple.com/app/apple-store/id978516833?pt=91215812&ct=stripe-docs-dashboard-basics&mt=8)
- [Android on Google Play](https://play.google.com/store/apps/details?id=com.stripe.android.dashboard&pli=1)

The mobile app lets you create and accept payments [in-person](/no-code/get-started#in-person) or online. It only supports the following products:

| Payment capability | iOS | Android |
| --- | --- | --- |
| [Tap to pay](/no-code/in-person) |  |  |
| [Manual card entry](https://support.stripe.com/questions/b7bd8ea6-d20c-40f8-a273-4d6c4902957a) |  |  |
| [Invoices](/no-code/invoices) |  |  |
| [Payment Links](/no-code/payment-links) (including QR codes) |  |  |
| [Subscriptions](/no-code/subscriptions) |  |  |

## Stripe organizations

If you have multiple Stripe accounts for regulatory or financial requirements you can centralize reporting, operations, and team management across your enterprise by setting up [Stripe Organizations](/get-started/account/orgs) within the Stripe Dashboard.

[YouTube resources](https://www.youtube.com/stripe)Watch tutorials, discover new features, and hear customer stories.[![](https://b.stripecdn.com/docs-statics-srv/assets/stripe-yt-supportresources.f22b44b4b7adb7778ae6265a9a8bc1a4.png)](https://www.youtube.com/stripe)

- ### [Developer resources](/development)

  Sign up for the newsletter, follow Stripe on X, or chat with the community on the official Discord.
- ### [Partner directory](https://stripe.partners/?f_help-me-with=implementation-and-development-services)

  Get expert help from certified service partners or use prebuilt integrations from technology partners.
- ### [Stripe Apps](https://marketplace.stripe.com/)

  Connect your business tools, like customer management and accounting systems, to Stripe.
- ### [Support site](https://support.stripe.com/)

  Learn the answers to common account questions and get troubleshooting tips and tricks.

## See also

- [Activate your account](/get-started/account/activate)
- [Start a team](/get-started/account/teams)
- [Perform searches](/dashboard/search)