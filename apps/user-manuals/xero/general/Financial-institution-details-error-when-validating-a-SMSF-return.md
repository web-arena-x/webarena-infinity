# Financial institution details error when validating a SMSF return

Source: https://central.xero.com/s/article/Financial-institution-details-error-when-validating-a-SMSF-return

---

## Overview

- Identify and work around a known issue with a validation error on self-managed super fund (SMSF) returns related to the financial institution details for tax refunds.

## Scenario

When you validate a SMSF return, it generates a form error that references the financial institution details for tax refunds. This happens when you provide bank account information for both the fund's financial institution account (7A) and the account for tax refunds (7B), but then select the option to have refunds paid into the account in 7A.

The error reads in full:

Financial institution account details for tax refund must not be provided if answer to question 'I would like my tax refunds made to this account' is 'yes' (true).
(CMN.ATO.SMSFAR.437189)

Financial institution account details for tax refund must not be supplied if 'I would like my tax refunds made to this account' is 'yes' (true) to use the same account for both super contribution and rollover and tax refund purposes for the SMSF.

## Steps to reproduce

In the **Cover** section of a SMSF return:

1. In item **7 Electronic Funds Transfer (EFT)**, complete the bank account details for **B. Financial institution account details for tax refunds**.
2. Under **A. Fund's financial institution account details**, select **Yes** in response to **I would like my tax refunds made to this account**. The details in 7B are hidden but not removed.
3. Click **Validate**.

You receive a form error CMN.ATO.SMSFAR.437189 that reads in part, “Financial institution account details for tax refunds must not be provided if…”.

Clicking **Complete** also runs validation checks on the return and generates the same form error.

## How to resolve the issue

To use the account from 7A for refunds, the account details in 7B must be left blank. You’ll need to make the bank account details in 7B visible again, then delete them.

In the **Cover** section of a SMSF return:

1. In item **7 Electronic Funds Transfer (EFT)**, under **A. Fund's financial institution account details**, select **No** in response to **I would like my tax refunds made to this account**. The details in 7B are visible again.
2. Under **B. Financial institution account details for tax refunds**, select **Manual**, then delete the account details. If **Manual** doesn’t appear, you need to [edit the tax agent details](Set-up-a-tax-agent-and-connect-to-the-ATO.md) to remove the **Prevent manual bank details to be entered in tax return** option.
3. Re-select **Yes** in response to **I would like my tax refunds made to this account**.
4. Click **Validate**.

Clicking **Complete** also runs validation checks on the return but no longer generates the form error.

Alternatively, you can select **No** in response to **I would like my tax refunds made to this account** and leave the details in 7B as they are. However, if you choose this option, the accounts used in 7A and 7B must be different.

## What's next?

If you need further help, contact Xero support.