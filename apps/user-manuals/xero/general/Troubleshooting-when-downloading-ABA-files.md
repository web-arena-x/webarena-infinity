# Fix issues when downloading ABA files for payroll

Source: https://central.xero.com/s/article/Troubleshooting-when-downloading-ABA-files

---

## Overview

- Resolve issues when you get an error when you download an ABA file for payroll.

If you get an error when you download an ABA file for payroll, check that your bank account is set up correctly. You need the [payroll admin permission](Payroll-Admin-access.md) to check and refresh your bank account details.

To check and refresh your bank account details:

1. In the **Accounting** menu, select **Bank accounts**.
2. Next to the bank account you want to check, click the menu icon , then click **Edit account details**.
3. Under **Bank Account Number**:
   - Remove any spaces or hyphens from the BSB and account number
   - Check that the BSB number is six digits and the account number is no more than nine digits
4. Under **Use the options below if you make batch payments**:
   - Check the DE user ID is correct. It's sometimes referred to as an APCA number
   - Select the **Include self-balancing transaction in the ABA file** checkbox if this option is required by your bank
5. Click **Save**.
6. In the **Payroll** menu, select **Payroll settings**.
7. In the **Organisation** tab, click **Save**. This refreshes the bank account settings for payroll.

## What's next?

After refreshing your bank account details, [download the ABA file](/s/article/Process-a-pay-run-and-pay-employees?userregion=true) again.