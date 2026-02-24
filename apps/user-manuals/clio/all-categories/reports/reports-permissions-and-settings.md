# Reports Permissions and Settings

Source: https://help.clio.com/hc/en-us/articles/9290095965211-Reports-Permissions-and-Settings

---

Access to reports in both Clio Grow and Clio Manage requires specific permissions on your user profile. Clio Manage users require reports permissions, and Clio Grow users require admin permissions to view reports. Additionally, Clio Manage administrators can change the payment allocation setting to determine how partial payments should be applied to certain reports.

**Note:** Only administrators can perform the actions listed in this article.

## Change reports permissions in Clio Grow

In Clio Grow, a user can either have admin or normal permissions. Only users with admin permissions can view reports and provide access to other users to view reports. If you are an administrator, follow the steps below to give another firm user reports permissions.

**Important:** All users with admin permissions can view reports, export contacts and matters to CSV, invite users, deactivate users, add or remove licenses, and update firm billing information.

1. Go to **Settings** > **Account**.
2. In the **User settings** section, select a user’s **Normal** permission.
3. Select **Admin** and then click **Assign permission**.

## Change reports permissions in Clio Manage

In Clio Manage, users need reports permissions to view and generate reports. Once a user has reports permissions, they can view all reports in Clio Manage. You cannot restrict reports. If you are an administrator, follow the steps below to give another firm user report permissions.

**Important:** Granting a user reports permissions will give them access to other firm users’ productivity, including activities and billing rates, when viewing reports even if the user does not have billing permissions.

For one user For multiple users in bulk

1. Go to **Settings** > **Manage Users**.
2. Click **Edit** below the user’s name.
3. Scroll down to **Permissions**.
4. Check the box for **Reports**.
5. Click **Save New Information**.

1. Go to **Settings** > **Groups, Permissions, and Job Titles** > **Permissions**.
2. Scroll down to **Reports**.
3. Check or uncheck the boxes next to users’ names.

## Change reports allocation setting in Clio Manage

Clio Manage reports help you quickly gauge how much of your client payments come from different line item categories. By default, partial payments and credit notes are applied to all line items proportionally. Administrators can also choose a different payment allocation method for how partial payments and credit notes are applied to line items in specific reports. Once a new method is selected, only reports generated after choosing the new method will be affected.

**Note:** This setting will affect the following reports: invoice payments report, fee allocation report, revenue report, and the originating attorney revenue report. This setting will also affect the collection rate in your Firm Dashboard.

1. Go to **Settings** > **Billing**.
2. Select **Reports allocation**.
3. Under **Payment allocation**, select the allocation method of your choice. There are four allocation methods to choose from. See below for an explanation of each and a table with examples of how a partial payment would be allocated across report line items depending on the selected method.
   - Option 1: Pay all line items proportionally
   - Option 2: Pay expenses oldest to newest first and then services oldest to newest
   - Option 3: Pay expenses oldest to newest first and then services proportionally
   - Option 4: Pay services oldest to newest first and then expenses oldest to newest
4. Click **Save setting**.

**Allocation method explanation:**

**Option 1: Pay all line items proportionally**

- This is the default setting. A partial payment will be applied to line items based on each line item's percentage of the total bill cost. For example, a $400 expense on a $1000 invoice is 40% of the invoice. If that invoice receives a payment of $800, 40% of that partial payment amount is $320, so the expense will receive a $320 payment.
- This method is also used by accounting systems like QuickBooks Online (QBO) and Xero. Use this method if you want your firm's reporting data in Clio Manage to match the reporting data in QBO or Xero.

**Option 2: Pay expenses oldest to newest first and then services oldest to newest**

- A partial payment will be first applied to expense line items from the oldest dated to newest dated, followed by services (time entries) from oldest dated to newest. If the payment is fully used before all line items are paid, the remaining line items will show $0 in reports.
- If you use reports to determine how to pay employees based on their recorded time, you may want to use the option 3 (pay expenses oldest to newest first and then services proportionally) since option 2 will result in employees who did work earlier on the invoice being compensated first.

**Option 3: Pay expenses oldest to newest first and then services proportionally**

- A partial payment will be first applied to expense line items from the oldest dated to newest dated. Services (time entries) will then be paid proportionally based on each service's percentage of the total of all services on the invoice, NOT the invoice total. This method can help pay all employees who did work on the invoice equally.
- For example, if, after paying all expenses, there is $100 of a partial payment remaining and a total of $300 in services, with service 1 for $200 (two-thirds of the total service amount) and service 2 for $100 (one-third of the total service amount), service 1 will receive $66.67 and service 2 will receive $33.33.

**Option 4: Pay services oldest to newest first and then expenses oldest to newest**

- If you select this option, a partial payment will be first applied to service line items from the oldest dated to newest dated, followed by expense line items from oldest dated to newest. If the payment is fully used before all line items are paid, the remaining line items will show $0 in reports.

**Example:**

In this example, you sent your client a $1000 invoice with two expense line items and two service line items. Your client paid a partial payment of $800 toward the invoice. When you generate a report containing invoice line items, the four line items will be allocated the paid $800 depending on the allocation setting you chose. The table below shows how much of the payment would go toward each line item depending on each allocation method option.

| Line item | Amount | Date | Option 1 | Option 2 | Option 3 | Option 4 |
| --- | --- | --- | --- | --- | --- | --- |
| Expense 1 | $400 | February 1, 2024 | $320 | $400 | $400 | $400 |
| Expense 2 | $300 | February 2, 2024 | $240 | $300 | $300 | $100 |
| Service 1 | $200 | February 29, 2024 | $160 | $100 | $66.67 | $200 |
| Service 2 | $100 | March 5, 2024 | $80 | $0 | $33.33 | $100 |

## Set originating and responsible attorney allocations in Clio Manage

The fee allocation report is designed give your firm a detailed view of the time and expenses each user has billed and collected for each matter. To help you easily determine your firm's compensation and bonus structures, administrators can also set how much of the collected time in the fee allocation report should be allocated to originating and responsible attorneys. Previously generated reports will not be affected by updated attorney allocations.

**Note:** This is a firm-wide setting that will affect all originating and responsible attorneys on the fee allocation report. Firm administrators can also override the firm-wide setting for any individual matter by changing the allocation percentages for that matter. Learn more about changing the percentages in the matter form [here](https://help.clio.com/hc/en-us/articles/9285959663131#h_01GEK791XBF1JJ0VYC8BQTG9MW).

1. Go to **Settings** > **Billing**.
2. Select **Reports allocation**.
3. Under **Attorney allocation**, enter percentage allocations for the originating attorney and responsible attorney. When you generate the fee allocation report, these percentages will help you determine how much of the collected time each originating and responsible attorney should earn.
4. Click **Save setting**.