# Add funds to your Stripe balance

Source: https://docs.stripe.com/get-started/account/add-funds

---

Add funds to your balance

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fadd-funds)

[The Stripe Docs logo](/)

Search

`/`Ask AI

[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fadd-funds)

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

Add funds to your balance

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

# Add funds to your Stripe balance

## Cover increased refunds and chargebacks by adding funds to your balance.

Ask about this page

Copy for LLMView as Markdown

### Connect accounts

To add funds to pay out to connected accounts, [add funds to your platform balance](/connect/top-ups).

To maintain stability in your business when your account has a negative balance or when you expect an increase in customer refunds or disputes, you can add funds directly to your Stripe balance using a wire or bank transfer.

For businesses using automatic payouts, we recommend that you set a [minimum balance](/payouts/minimum-balances-for-automatic-payouts) to ensure timely processing of refunds.

## Payment method availability

In several markets, funds are added to a Stripe VBAN (which helps reconciliation speed) using a local bank credit transfer. These include: AMER (United States), EMEA (United Kingdom, EUR Currency markets) and APAC (Japan).

In other markets, funds are added using a wire transfer, which follows slightly different times and processes. Only wire transfers are available in the following regions and countries: AMER (Canada), EMEA (Non-EUR Currency markets: BG, CZ, HU, LI, GI, RO), APAC (AU, NZ, SG, HK, IN, TH, MY), and LatAm (BR, MX). Stripe VBAN isn’t available in these regions and countries.

## Payments balance

In the US, UK, and JP, you can add funds directly to the payments balance. We recommend this option for most businesses because it avoids transiting funds through a separate balance.

For businesses using automatic payouts, funds added to the payments balance in excess of the [minimum balance](/payouts/minimum-balances-for-automatic-payouts) are paid out in the next payout. You can configure your payout schedule and minimum balance settings in your [Payout settings](https://dashboard.stripe.com/settings/payouts).

## Refunds and disputes balance

You can also add funds to the **Future refunds or disputes balance** ([refund\_and\_dispute\_prefunding](/api/balance/balance_object#balance_object-refund_and_dispute_prefunding)), which is a separate balance. These funds are never included in an automatic payout, but you can initiate a manual payout at any time.

Stripe first attempts to process refunds and disputes from your available payments balance. If your payments balance is insufficient, Stripe uses these reserved funds. If these reserved funds are also insufficient, then your payments balance might go negative.

#### Payouts reconciliation

For businesses using automatic payouts, balance transactions for refunds and disputes funded from the **Future refunds or disputes balance** aren’t included in [payouts reconciliation reports](/payouts/reconciliation).

## Financial account

In the US and UK, you can add funds to a [financial account](/financial-accounts) in the Stripe Dashboard. A financial account lets you store funds, send and receive money, convert currencies, and create spend cards.

## Add funds

This section outlines the steps to send funds from your bank using the Dashboard to add them to your Stripe balance.

### Before you send funds

You can send funds from an external bank account to fund your financial account. In the US, you can send funds with an ACH transfer or wire. With ACH, funds are available in about 3 days after you initiate the transfer from your bank. With wire transfers, funds are available within the day. Additional charges apply if funding with a wire.

1. On the [Balances](https://dashboard.stripe.com/balance/overview) page, click **Add funds**.
2. Select the balance to add money to.
3. Enter the amount and click **Next**.
4. Verify the account details to send money through ACH, RTP, a wire, or other local payment from your bank. Click **Done**.

### After you send funds

1. After your bank has sent the funds, navigate back to the Balances page, and click **Add to balance**.
2. If the modal prompts you for a receipt, upload a screenshot or document that confirms your bank transferred the funds. To fund your Stripe balance faster, you might need to provide a screenshot or PDF of your bank’s transfer or wire confirmation.
3. Click **Confirm transfer**.

## View your funds

After Stripe receives the funds, we show the added funds in the [Balances](https://dashboard.stripe.com/balance/overview) page.

You also receive a [balance.available](/api/events/types#event_types-balance.available) webhook. The following example event shows a balance snapshot with details of `refund_and_dispute_prefunding` balances:

```
{
  "id": "{{EVENT_ID}}",
  "object": "event",
  "type": "balance.available",
  "data": {
    "object": {
      "object": "balance",
      //...
      "available": [
        {
          "amount": 1000,
          "currency": "usd",
          "source_types" : {
            "bank_account": 100,
            "card": 900,
          },
        },
        {
          "amount": 0,
          "currency": "eur",
          "source_types" : {
            "bank_account": 0,
            "card": 0,
          },
        }
      ],
      "pending": [
        //...
      ],
      "refund_and_dispute_prefunding": {
        "available": [
          {
            "amount": 1000,
            "currency": "usd",
          },
          {
            "amount": 0,
            "currency": "eur",
          }
        ],
        "pending": [
          {
            "amount": 1000,
            "currency": "usd",
          },
          {
            "amount": 0,
            "currency": "eur",
          }
        ],
      }
      // ...
    }
  }
}
```

## Settlement timing

This table provides the expected timing for fund settlement based on the region and payment transfer method, and can help you understand how long it typically takes for payments to process.

| Region and currency | Payment transfer method | Estimated speed |
| --- | --- | --- |
| USA (USD) | Wire transfer | 1-5 days |
| USA (USD) | ACH Credit Transfer | 1-3 days |
| USA (USD) | ACH Debit Transfer | 5 days |
| EU (EUR) | SEPA Credit Transfer | 1-2 days |
| UK (GBP) | FPS | 2 hours - 1 day |
| UK (GBP) | BACS | 2-3 days |
| Other currencies | Wire transfer | 1-7 days (if you provide the correct wire information to Stripe) |

Depending on your account configuration, you might not have access to all the methods mentioned above immediately after launching.

If you’re a new user and haven’t completed a substantial amount of top-ups to Stripe, the timing for fund availability might initially be delayed longer than indicated; however, your initial speed will eventually align with the outlined speeds.

## See also

- [Add funds to your platform balance](/connect/top-ups)
- [Manage prorations for modified subscriptions](/billing/subscriptions/prorations)