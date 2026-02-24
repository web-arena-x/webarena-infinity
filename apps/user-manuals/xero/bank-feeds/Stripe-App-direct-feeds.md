# Stripe app direct feeds

Source: https://central.xero.com/s/article/Stripe-App-direct-feeds

---

## Overview

- Get transactions from Stripe automatically imported into Xero.
- Transactions import when a payout occurs in Stripe.

## What you need to know

If you have a Stripe account, connect it to your Xero organisation to automatically import your transactions.

You can set up a Stripe feed for each settlement currency you have in Stripe. The currency will be the account name and the bank account number will be the same for each bank account in Xero.

Your Stripe account automatically connects to an existing bank account in your Xero organisation if the account was created by the Stripe integration. If your Stripe account isn't already set up in Xero, a new bank account is automatically created.

Payment transactions display as two statement lines, one line shows the gross amount and the other line shows the Stripe fee.

To distinguish between local and international transactions, the country associated with the charge displays in the description of the transaction.

For any Stripe accounts you have in another currency, you need multicurrency. See our [pricing plans](https://www.xero.com/pricing/) (Xero website) for more information.

## Set up your feed

Warning

If you’ve already set up a [Stripe direct feed](Stripe-direct-feeds.md) within Xero, you’ll need to deactivate the feed before you can set up the Stripe App bank feed.

Set up the bank feed in Stripe during the onboarding of the Stripe app. Alternatively, in the Xero app settings page in Stripe, click **Add bank feed** and follow the prompts to connect the bank feed. If you need more help setting up your feeds, [contact Stripe directly](https://support.stripe.com/contact/email?topic=stripe_apps&app=xero) (Stripe website).

Once the feed is set up, transactions appear in Xero depending on your Stripe [payout schedule and region](https://stripe.com/docs/payouts#payout-schedule) (Stripe website).

Transactions before your feed was activated aren't imported into Xero automatically. You need to [import these manually](Manually-import-Stripe-transactions.md).

You can stop this feed within the Stripe app. Click **Disconnect** next to the relevant account in your Stripe app settings.

## What's next?

When the direct feed starts, check you don’t have any missing or duplicate transactions. If you do, [manually import any missing transactions](About-manually-importing-bank-statements.md) or [delete any duplicates](Delete-or-restore-a-bank-statement-line.md).