# Unable to save the details of a PayPal account

Source: https://central.xero.com/s/article/Unable-to-save-the-details-of-a-PayPal-account

---

## Overview

- Identify and work around a known issue with saving changes to a PayPal account when the BSB is blank.

## Scenario

New PayPal accounts are set up initially with no value for BSB. If you edit the account details but don’t update the default value from the initial set up, when you try to save the details you receive an error message, and the save fails.

## Steps to reproduce

Update the details for a newly create PayPal account:

1. In the **Accounting** menu, select **Bank accounts**.
2. Find the PayPal account in the list, click the menu icon  and select **Edit account details**.
3. Review and update the account details but leave the default blank value for **BSB**.
4. Click **Save**.

You’ll get an error telling you to enter a valid BSB number.

## How to resolve the issue

To resolve the issue, enter any six digits, such as 000000, in the **BSB** field. The value will be formatted automatically.

## What's next?

If you need further help, [contact Xero support](https://central.xero.com/s/contact-support).