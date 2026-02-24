# About bank feeds

Source: https://central.xero.com/s/article/Bank-feeds

---

## Overview

- Use bank feeds to automatically import transactions from your bank or financial institution into your Xero organisation.
- Xero follows industry-leading approaches to ensure your bank data is secure.

Bank feed types

### What you need to know

Bank feeds automatically import transactions from your bank or financial institution directly into your Xero organisation, eliminating the need to import transactions manually.

Different options are available as per the technical capabilities and preference of the banks and financial institutions we import data for.

Once you’ve connected a bank feed, your transactions will automatically import into your bank account in Xero ready for you to reconcile. You don’t need to manually refresh your bank feed for your transactions to import.

Xero relies on banks to make recent transactions available for import. We can’t guarantee transactions will be available as soon as they show in your online banking.

### Direct feeds

Where we have an agreement with your bank or financial institution, direct feeds automatically send transactions into your Xero organisation on a regular basis. Direct feeds offer a high level of reliability and transaction reference detail. Some direct feeds are also known as OAuth feeds.

The banks only provide one direct feed per bank account, so the feed can only be connected to one bank account in Xero.

Once your direct feed is connected, statement lines will appear in your bank account in Xero ready for you to reconcile.

### Aggregator supplied direct bank feeds

Aggregator supplied direct bank feeds (sometimes known as OAuth feeds) are a type of direct feed a third party aggregator offers for some banks or financial institutions. An aggregator is a third party that allows Xero to connect to a variety of banks.

Xero uses Yodlee to provide aggregator supplied direct bank feeds.

Aggregator supplied direct bank feeds automatically send transactions into your Xero organisation on a regular basis. Once your feed is connected, statement lines appear in your bank account in Xero ready for you to reconcile.

### Yodlee credential shared feeds

As a third party, Yodlee offers credential shared feeds for banks and financial institutions that don't have direct feeds available.

Yodlee retrieves transactions from your bank account by using your credentials, and imports them into Xero on your behalf. Most Yodlee feeds need to be manually refreshed in order for the transactions to import.

### PayPal feeds

If you have [PayPal set up as a payment service in Xero](PayPal.md), or you use PayPal as a payment provider for your online store, you can set up a [PayPal direct feed](/s/article/PayPal-direct-feeds?userregion=true) to get your transactions sent into Xero automatically.

Transactions will appear in your bank account in Xero every 12 hours, or you can manually refresh your feed to import the latest transactions.

### Stripe feeds

You can [set up a feed](Stripe-direct-feeds.md) to automatically import transactions from your Stripe account into Xero. Once the feed is set up, you can [reconcile your Xero transactions](Reconcile-Stripe-payments.md) with the imported Stripe statement lines.

You can set up a Stripe feed without having Stripe as a payment service in Xero.

Stripe transactions will appear in Xero depending on your [payout schedule and region](https://stripe.com/docs/payouts#payout-schedule) (Stripe website), which you can view on your Stripe dashboard.

Bank feed security

Xero takes the [security of our customers’ data seriously](https://www.xero.com/security/) (Xero website) and we follow industry-leading approaches to securing that data.

When you set up a bank feed, you access your bank through Xero. To ensure the connection with your bank is secure, Xero uses industry-leading standard encryption and data security techniques.

Your bank transactions import into Xero through a secure and encrypted connection.

Xero provides [security assurance](Security-assurance-at-Xero.md) for every mechanism used to import your bank transactions.

Xero is certified as compliant with ISO/IEC 27001:2022, which is globally recognised as the premier information security management system standard. Xero has produced a Service Organization Control (SOC 2 Type II) report since 2016. These credentials are audited on an annual basis to ensure we’re handling your data securely.

Sometimes, we partner with third-party providers such as aggregator entities like Yodlee. We assess these partnerships carefully and ensure that any third-party providers we work with have the right certifications and commitments to handling your data.

When you connect a bank feed in Xero, you’ll see if a third-party provider is involved during the setup process.

Check for available bank feeds

To see if a bank feed is available for your bank account:

1. In the **Accounting** menu, select **Bank accounts**.
2. Click **Add bank account**.
3. Start typing your bank's name. If your bank or financial institution appears in the search results, bank feeds are available.

You can also see the relevant [support article for your bank](/s/topic/0TO1N0000017kmwWAA/direct-bank-feeds-for-your-region#business) to check if your account is eligible for a direct feed.

If your account isn't eligible for a direct feed, see if a [Yodlee feed](Yodlee-feeds-overview.md) is available and connect this while you're logged into Xero.

If there aren't any feeds available for your bank account, [manually import your bank statements](About-manually-importing-bank-statements.md).

Resolve issues with your feed

- If you’re having connection issues with your bank, try these [suggestions to fix the bank connection](Fix-issues-when-connecting-your-bank-to-Xero.md) issues.
- If you’re having trouble connecting a bank feed using a paper application form, check these [common problems with uploading bank application forms](Common-Problems-for-uploading-bank-forms.md) or [fix common problems with a rejected bank feeds application](Fix-common-problems-with-rejected-bank-feeds-application.md).
- Learn how to [identify and fix missing bank transactions](/s/article/Transactions-don-t-match-my-bank-account?userregion=true).
- If you have an active bank feed but a statement hasn’t been imported as expected, [check if your bank feed is late](Check-if-your-bank-feed-is-late.md).

## What's next?

If you have an active bank feed but a statement hasn't been imported as expected, check [disruptions to bank feeds](Disruptions-to-bank-feeds.md) to see if there's a known delay.