# Import data from Inland Revenue

Source: https://central.xero.com/s/article/Import-data-from-Inland-Revenue

---

## Overview

- Import data from Inland Revenue into Practice Manager.
- Find out reasons why the import might have failed.

## What you need to know

You can import a client's Summary of Earnings (SOE) and other available income data from Inland Revenue (IR) directly into Practice Manager. You can then add this data to the client's tax return.

You can pre-populate SOE and available income data into your client's tax returns. The SOE data is the same data that was available before the switch to gateway services (GWS). Income types currently available include:

- Summary of Earnings (SOE)
- Wage subsidy
- Interest
- Dividends
- PIE Income

From 2025 onwards, relevant tax returns can also import the following IRD data:

- Losses
- Deductions
- Non-refundable research and development credits
- Excess imputation credits
- Excess residential rental deductions
- Opening balances for IR4J and IR8J

## Import income data

To import the available income data from IR:

1. In the **Tax** menu, select **Returns**.
2. Find the client and click their name to open the return.
3. Click **Options**, then select **Import IRD Data**.
4. Click **Confirm**.

You'll see a banner once the data has been imported. The data imported will be recorded in the **History**section.

The available income data will also import automatically when a tax return is created. This will be merged with any prior year rollover data in the return. Only data that matches will be merged. For example:

- BNZ won’t match and merge with Bank of New Zealand.
- Ltd won’t match and merge with Limited.

Practice Manager will ignore capitalisation differences, so BNZ would match and merge with bnz.

You can re-import data from IR by following the steps above again. Once you click **Confirm**, this will overwrite existing imported data in the return.

To view the imported SOE and available income data:

1. Click **Tax**.
2. Select **Statements**, then search for the client.
3. On the client's **Statement Summary**, under **Summary of Earnings**, click the relevant year.

The imported data will display in the income section of the tax return in the relevant boxes.

## Reasons the data might not import

If the data hasn't imported, it might be due to one of the following reasons:

- The client hasn't been [connected to a tax agent](Assign-a-tax-agent-to-a-client-in-Practice-Manager.md) or their IRD number is missing.
- Your practice's [START connection](Set-up-your-practice-s-START-connection-with-Inland-Revenue.md) hasn't been set up.

## What's next?

[Complete the tax return](Complete-a-tax-return.md) for the client.