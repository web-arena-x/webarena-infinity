# Custom email domain

Source: https://docs.stripe.com/get-started/account/email-domain

---

Custom email domain

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Femail-domain)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Femail-domain)

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

[Multiple separate accounts](/get-started/account/multiple-accounts)

[Linked external accounts](/get-started/account/linked-external-accounts)

Settings

[Profile](/get-started/account/profile)

[Branding](/get-started/account/branding)

[Statement descriptors](/get-started/account/statement-descriptors)

Custom email domain

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

# Custom email domain

## Set up your own custom domain to interact with your customers.

Ask about this page

Copy for LLMView as Markdown

By default, when Stripe sends invoices, receipts, and failed payment notifications to your customers, it sends them from the `stripe.com` domain. You can change this to a custom domain.

## Set up a custom email domain

To start sending emails from your own domain, complete the following steps:

1. [Add your domain](#adding_domain) in the Dashboard.
2. [Verify your domain](#verifying_domain) to allow sending.
3. [Set your sending domain](#setting_sending_domain) as your domain.

To modify the look and feel of your emails, go to your [Branding](https://dashboard.stripe.com/account/branding) settings.

[## Add your domain](#adding_domain)

Navigate to your [Customer email](https://dashboard.stripe.com/settings/emails) settings and add the domain that you want to send customer emails from.

[## Verify your domain](#verifying_domain)

To verify your domain, you must configure the Domain Name System (DNS) records provided in the Dashboard. These DNS records are necessary to verify your domain ownership and reliable email delivery.

The procedure for adding DNS records to the DNS server for your domain depends on who provides your DNS service. Consult the documentation for your DNS service for specific instructions.

### Instructions for popular providers

It can take up to 72 hours for DNS record changes to be confirmed. Stripe lets you know whether your domain has been verified.

### Troubleshoot DNS issues

If your domain hasn’t been verified after 72 hours, try the following:

- Correct any typos. You can check your domain records in the Dashboard’s [Customer emails](https://dashboard.stripe.com/settings/emails) settings by clicking **Verify domain** to filter issues.
- Make sure you don’t have any records that share the same name as the provided CNAME records. CNAME records must be the [only record present](https://tools.ietf.org/html/rfc2181#section-10.1) for a record name.
- Make sure the added record names don’t include your domain twice. Some providers automatically append DNS record names with the domain name. For example, to create a record with the name **bounce.example.com**, enter only `bounce` in the **Name** field.
- Check that the DNS records are published. You can verify this by using a [DNS lookup tool](https://dnschecker.org/all-dns-records-of-domain.php), which displays the published records for your domain.

If you’ve tried all of our troubleshooting recommendations and are still having trouble verifying your domain, contact your DNS provider.

### DNS records

Each category of record that needs to be configured has a purpose.

| Record Category | Type | Purpose |
| --- | --- | --- |
| Stripe proof-of-ownership | TXT | Before you can send email from a domain, we must confirm ownership of the domain you plan to use. |
| Mail From Domain | CNAME | This specifies the source of the message to the receiving email server and the [Sender Policy Framework (SPF)](https://tools.ietf.org/html/rfc7208) policy to allow sending. |
| [DomainKeys Identified Mail (DKIM)](http://dkim.org/) | CNAME | These allow a mail server to verify that a third party didn’t modify a message in transit. |

#### Caution

After we verify the domain, don’t delete the provided DNS records from your domain. Stripe frequently checks these records. If a record becomes invalid or goes missing, we notify you. Also, make sure to correct DNS records within 48 hours. If you don’t, we send customer emails from *stripe.com* until you resolve the problem.

### Sender authentication (DMARC)

To use a custom email domain, you need to set up a DMARC policy for your domain. [Domain-based Message Authentication, Reporting & Conformance (DMARC)](https://dmarc.org/) shields your domain from impersonation attacks, such as phishing. Notably, major email providers like Google and Yahoo now necessitate DMARC for those sending bulk emails.

You publish DMARC policy as a DNS TXT record. The record’s name is always `_dmarc`, and the value comprises tag-value pairs that symbolize your policy. Additionally, you can learn about all the [supported tags and their uses](https://dmarc.org/overview/), but let’s cover some of the most significant tags:

| Tag | Description | Sample value |
| --- | --- | --- |
| v required | The protocol version. This must always be DMARC1. | v=DMARC1 |
| p required | The policy for domain. The possible values are: none, quarantine, reject. | p=none |
| rua optional | Address(es) to receive aggregate reports | rua=mailto:report@example.com |

If you’re new to DMARC, we suggest beginning with a `p=none` policy for initial monitoring, then switch to either `quarantine` or `reject` in due course. After you’ve settled on the appropriate policy, you must incorporate the following DNS record into your domain:

| Type | Name | Value |
| --- | --- | --- |
| TXT | `_dmarc` | Your DMARC policy. For example: `v=DMARC1; p=none; rua=mailto:report@example.com` |

#### Caution

We don’t currently support strict SPF alignment. Make sure your DMARC policy doesn’t have `aspf=s`.

If you’re already using this domain to send email, use caution when adding DMARC to make sure that it doesn’t interfere with your existing configuration. Consult an email or IT professional before adding or modifying this record.

[## Set your sending domain](#setting_sending_domain)

If Stripe has verified your domain, you’ll see a **Verified** badge under the **Verification** column in your [Customer email](https://dashboard.stripe.com/settings/emails) settings. Customer emails are now sent from your domain. You can send a test email by clicking the overflow menu ().

Whenever a customer replies to your emails, their responses are sent to the support email address you specified in your [public business information](https://dashboard.stripe.com/settings/public).

### Supported address configurations

After you specify a custom domain, you can send emails to your customers from the following email usernames:

- `billing`
- `card-expiring`
- `failed-payments`
- `invoice`
- `invoice+statements`
- `receipts`
- `support`
- `support+express`
- `trial-ending`
- `upcoming-invoice`

[## OptionalChange email domains](#change-email-domains)

[## OptionalUse the same email domain on multiple Stripe accounts](#same-id-multiple-accounts)