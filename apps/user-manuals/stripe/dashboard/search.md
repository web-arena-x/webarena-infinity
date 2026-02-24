# Perform searches in the Dashboard

Source: https://docs.stripe.com/dashboard/search

---

Search in the Dashboard

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdashboard%2Fsearch)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdashboard%2Fsearch)

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

[Mobile Dashboard](/dashboard/mobile)

Search in the Dashboard

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

# Perform searches in the Dashboard

## Use the Dashboard to search for payments, customers, and more.

Ask about this page

Copy for LLMView as Markdown

### Advanced searches

[Stripe Sigma](/stripe-data) makes all of your business data available as an interactive SQL environment in the Dashboard. You can use it to perform highly advanced searches and generate customized reports.

Use Dashboard’s search to find important resources, and navigate across different Stripe resources, like [connected accounts](/connect), [customers](/api/customers), [invoices](/api/invoices), [payouts](/payouts), and [products](/api/products).

When you perform a search, the top results appear immediately. View all of the matches by clicking **View all results** or pressing **Enter**. From the resulting groups of search results, click **View all** to see an expanded display with column headings, some of which provide sorting options.

## Get started

Use different pieces of information as search terms:

- The last four digits of a card or account number (**4242**).
- The payment method type (**iDEAL**).
- The business name of a connected Stripe account (**Rocketship**).
- The email receipt number (**1817-9523**).

For searches that require dates, you can use different formats, like **08/22**, **2020-07-12**, or **last week**. Use object identifiers (dispute ID) to take you directly to the object you’re looking for. No additional context is necessary for most searches. The Dashboard automatically looks for the most relevant information based on your search query. You can make use of search filters and operators for more granular control.

## Search filters and operators

By default, the Dashboard looks for values that match your search term in the most logical fields within objects. (For example, it’ll look for an email address in the `email` field or an object description.) You can use filters and operators to further refine your searches. The more terms you provide in your search query, the fewer the number of results.

Filters

Operators

Use filters to limit your search terms so that they only apply to specific fields within applicable objects. Preface a search term with one of these filters. If your search term must include a space, wrap it in quotation marks (`name:"John Doe"`). Many fields are shared across different objects. For instance, the `amount` field applies to payments, invoices, payouts, and so on.

| Filter | Description | Example |
| --- | --- | --- |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| `amount:` | The amount of an object. For decimal currencies, use a decimal point for both currency units (for example, dollars and cents). | **amount:149.99** |
| `brand:` | The brand of card associated with an object. | **brand:visa** |
| `country:` | The two-letter [ISO code](https://en.wikipedia.org/wiki/ISO_3166-1) representing the country associated with an object. | **country:GB** |
| `created:` | The date an object was created (identical to `date`). | **created:2020/07/12** |
| `currency:` | The three-letter [ISO code](https://en.wikipedia.org/wiki/ISO_4217) representing the currency of an object. | **currency:EUR** |
| `date:` | The date an object was created (identical to `created`). | **date:yesterday** |
| `email:` | The email (either full address or part of one) of an object. | **email:jenny.rosen@example.com** |
| `exp:` | The expiration date of the card associated with an object. | **exp:08/22** |
| `flow:` | The type of [flow for customer action](/sources#flow-for-customer-action) that applies to a [Sources](/sources) payment. | **flow:redirect** |
| `last4:` | The last four digits of the card or account number associated with an object. | **last4:4080** |
| `metadata:` | [Metadata](/api#metadata) value on a supported object. Additional [search options](#metadata-searches) for metadata are also available. | **metadata:555-5555** |
| `name:` | The cardholder or customer name associated with an object. | **name:jenny** |
| `number:` | The unique number identifying an invoice. | **number:06b2b1a642-0023** |
| `postal:` | The ZIP or postal code associated with an object. | **postal:12345** |
| `receipt:` | The receipt number used in a payment or refund email receipt. | **receipt:3330-2392** |
| `risk_level:` | The [risk level](/radar/risk-evaluation) of a payment determined by [Radar](/radar). | **risk\_level:elevated** |
| `status:` | The status of an object. | **status:canceled** |
| `type:` | The type of [PaymentMethod](/payments/payment-methods) or [Source](/sources) used to create a payment. | **type:ideal** |
| `usage:` | The [usage](/sources#single-use-or-reusable) availability of a [Sources](/sources) payment method. | **usage:single\_use** |
| `zip:` | The ZIP or postal code associated with an object. | **zip:12345** |

### Combine and negate search terms

Use more than one search term to narrow down your search. You can also negate any search filter with a hyphen (`-`) so that matches for it aren’t included.

| Example | Description |
| --- | --- |
| `type:card last4:4242 exp:08/22` | The last four digits of the card are `4242` and expiration date is `08/22`. |
| `type:card last4:4242 -exp:08/22` | The last four digits of the card are `4242` and expiration date is *not* `08/22`. |
| `type:ideal status:canceled` | iDEAL payments where the source has been canceled and not used to complete a payment. |

To search for an entire phrase, use quotation marks. For example, **“Stripe Shop”** provides matches for that full phrase, but **Stripe Shop** searches the words **Stripe** and **Shop** separately.

### Metadata searches

You can search for [metadata](/api#metadata) that you added to objects that support it. For example, you can find documents that have metadata key `order_id` with corresponding metadata value `xyn712` using any of the following search queries:

- `xyn712`
- `order_id:xyn712`
- `metadata:xyn712`
- `metadata:order_id=xyn712`

## Search across an organization

After you add multiple Stripe accounts to an [organization](/get-started/account/orgs), your team members can search across all of the accounts they have access to in it. By default, searches display results from all of these accounts. If a team member is viewing the Dashboard from in an account, there’s an option in the search dropdown to only search within that account.

## Best practices

Many searches can be performed with a single search term. Use something that would be fairly specific, such as a name or email address. If you’re seeing too few results, make the search term less specific. If there are too many results, include additional terms, one at a time.

Use a wider range of values when using dates or amounts as search terms. Currency conversions and time zone differences between you and your customer are a common source of confusion when looking up information about a payment. In these cases, additional search terms or even different ones altogether can help.

#### Bookmark searches

As search terms are included in the URL, you can bookmark the search or share it with other team members as you would any other web page.