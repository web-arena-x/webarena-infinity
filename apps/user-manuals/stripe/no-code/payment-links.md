# Create Payment Links

Source: https://docs.stripe.com/no-code/payment-links

---

Create Payment Links

[Create account](https://dashboard.stripe.com/register/payment_links) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Fpayment-links)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register/payment_links)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Fpayment-links)

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

Create Payment Links

[Create a buy button](/no-code/buy-button)

[Send invoices](/no-code/invoices)

[Create subscriptions](/no-code/subscriptions)

[Send quotes](/no-code/quotes)

[Accept in-person payments](/no-code/in-person)

[Pay out money](/no-code/payout)

[Set up customer portal](/no-code/customer-portal)

[Dashboard assistant](/assistant)

Migrate to Stripe

Common use cases

[Overview](/get-started/use-cases)[Accept simple payments as a startup](/get-started/use-cases/startup)[Sell subscriptions as a SaaS startup](/get-started/use-cases/saas-subscriptions)[Build a subscriptions solution with usage-based pricing](/get-started/use-cases/usage-based-billing)[Accept payments in person](/get-started/use-cases/in-person-payments)[Send invoices to collect payments](/get-started/use-cases/invoices)

United StatesEnglish (United States)

# Create Payment Links

## Quickly accept payments for goods, services, subscriptions, tips, or donations.

Ask about this page

Copy for LLMView as Markdown

[Payment Links](/payment-links) are a simple way for customers to pay you when you sell online. Create a single link that you can share with everyone.

Type

Sell a product or serviceSell a subscriptionCollect tips or donations

Name

Price

$

AEDAFNALLAMDANGAOAARSAUDAWGAZNBAMBBDBDTBGNBHDBIFBMDBNDBOBBRLBSDBWPBYNBZDCADCDFCHFCLPCNYCOPCRCCVECZKDJFDKKDOPDZDEEKEGPETBEURFJDFKPGBPGELGIPGMDGNFGTQGYDHKDHNLHTGHUFIDRILSINRISKJMDJODJPYKESKGSKHRKMFKRWKWDKYDKZTLAKLBPLKRLRDLSLLTLLVLMADMDLMGAMKDMMKMNTMOPMROMURMVRMWKMXNMYRMZNNADNGNNIONOKNPRNZDOMRPABPENPGKPHPPKRPLNPYGQARRONRSDRUBRWFSARSBDSCRSEKSGDSHPSLLSOSSRDSTDSVCSZLTHBTJSTNDTOPTRYTTDTWDTZSUAHUGXUSDUYUUZSVEFVNDVUVWSTXAFXCDXOFXPFYERZARZMW

Create your payment link

![](https://b.stripecdn.com/docs-statics-srv/assets/0bf124f94479ea72ead56c0aad4e7557.svg)

Your business name

Sunglasses

# $0.00

![](https://b.stripecdn.com/docs-statics-srv/assets/2fc0a8c0d6698e8ecd951d3c8137aa89.svg)

![](https://b.stripecdn.com/docs-statics-srv/assets/c63e01cc65f29058b5709a0b8bcabf8b.svg)

Payment Links supports over [30 languages](https://support.stripe.com/questions/supported-languages-for-stripe-checkout-and-payment-links) and over [40 payment methods](https://docs.stripe.com/payments/payment-methods/integration-options#payment-method-product-support).

## Create a payment link

Before you begin, decide what pricing model works best for you:

- **Products or subscriptions**: Best for e-commerce or SaaS where you’re selling products for a fixed price.
- **Customers choose what to pay**: Best for donations, tipping, or pay-what-you-want. This pricing model currently doesn’t support recurring payments or recurring donations. Learn more about the requirements for [accepting tips or donations](https://support.stripe.com/questions/requirements-for-accepting-tips-or-donations).

Products or subscriptions

Customers choose what to pay

To let your customers choose what to pay, create a payment link by completing the following steps:

1. In the Dashboard, open the [Payment Links](https://dashboard.stripe.com/payment-links/create/customer-chooses-pricing) page and click **New** (or click the plus sign () and select **Payment link**).
2. Select **Customers choose what to pay** and add a title, description, and image.
3. (Optional) Set a suggested preset amount.
4. (Optional) Set minimum and maximum payment amounts. By default, the maximum payment amount is 10,000.00 USD. Contact us using the form at [Stripe support](https://support.stripe.com/) to increase this limit.
5. Click **Create link**.

## Payment Links on mobile

If you’re creating a product or subscription, use the [Stripe Dashboard iOS app](https://apps.apple.com/app/apple-store/id978516833?pt=91215812&ct=stripe-mobile-app-docs-plinks&mt=8) to create a payment link on your mobile device. In the app, go to **Payments** > **Payment Links** to create a payment link (or click the create icon () and select **Payment link**). The iOS app doesn’t currently support creating links where your customers choose how much to pay.

## Share payment links

Use the Dashboard to copy your payment link, and share it online. Click the copy icon next to an existing link on the [Payment Links](https://dashboard.stripe.com/payment-links) page, or go to the payment link’s details page. You can share your payment link multiple times and anywhere online, including:

- Emails
- Text messages
- Social media platforms

### Generate a QR code

You can create a QR code for a payment link in the Dashboard. Choose an existing link from the **Payment Links** page, or [create a new link](https://dashboard.stripe.com/payment-links/create) and then click **QR code**. Copy or download a PNG image of the QR code.

The QR code doesn’t expire. If you deactivate the underlying payment link, the QR code redirects to an expiration page.

### Embed a button on your site

Turn your payment link into an embeddable buy button to sell a product or subscription from your website. Select an existing link from the **Payment Links** page or create a new link and then click **Buy button**. Copy the code and paste it into your website. To learn more on how to embed and customize a button, see [Create a buy button](/payment-links/buy-button).

### Deactivate a link

Dashboard

API

You can use the Dashboard to deactivate a payment link. For the selected payment link, click the overflow menu () > **Deactivate**. After you deactivate a link, customers can no longer use it to make a purchase. You can reactivate the payment link through the Payment Links API at any time.

## Configure payment methods

With [Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods), Stripe displays the most relevant and compatible payment methods to your customers, including Apple Pay and Google Pay. Stripe enables certain payment methods for you by default. We might also enable additional payment methods after notifying you. Use the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) to enable or disable payment methods at any time. Learn more about [supported payment methods](/payments/payment-methods/payment-method-support) and [different types of payment methods](https://stripe.com/guides/payment-methods-guide).

You can review what payment methods your customers see in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods/review) by entering a transaction ID or setting an order amount and currency.

To specify a different set of payment methods, set the [payment\_method\_types](/api/payment_links/payment_links/create#create_payment_link-payment_method_types) parameter when you create the payment link in the API:

Command Line

Select a language

cURL

Stripe CLI

Ruby

Python

PHP

Java

Node.js

Go

.NET

No results

```
curl https://api.stripe.com/v1/payment_links \
  -u "

sk_test_BQokikJOvBiI2HlWgH4olfQ2

:" \
  -d "line_items[0][price]"=

"{{PRICE_ID}}"

 \
  -d "line_items[0][quantity]"=1 \
  -d "payment_method_types[0]"=card \
  -d "payment_method_types[1]"=klarna
```

Some payment methods, such as bank debits or vouchers, might take between 2 and 14 days to confirm the payment. [Set up webhooks](/checkout/fulfillment#create-payment-event-handler) to send you notifications when the payment clears, so you can begin fulfillment.

Your customers will see Apple Pay or Google Pay options if they activated those methods on their device. The payment methods your customers see also depend on the browser they’re using.