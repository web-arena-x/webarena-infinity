# Split Billing

Source: https://help.clio.com/hc/en-us/articles/25704317136155-Split-Billing

---

With split billing in Clio Manage, you can split a bill for a matter between multiple payers, giving you the flexibility to bill based on your practice area needs. Split billing is a quick and efficient process that starts with adding all payers to a matter, generating a bill with time and expense activities, and then sending each payer their own bill showing their amount owing.

**Note:** This feature is available to firms with Advanced and Expand subscriptions. If you need to upgrade your firm’s plan, ask a firm administrator. [Learn more about your plan's features](https://www.clio.com/pricing/).

## Enable and arrange split billing bill theme columns

Before generating split bills, we recommend enabling and arranging the split bill columns on at least one bill theme. Once enabled, when you apply a bill theme to a split bill, each payer will see additional columns showing them the total amount of each activity line item on the bill along with the portion that each payer needs to pay. If you do not enable these columns and generate a split bill, your client and additional payers will not see the portion that they owe.

**Note:** If you enable the split bill columns on a bill theme but only generate a regular bill, not a split bill, the columns will not populate on the client's bill invoice. The columns will only appear on split bill invoices.

1. Go to **Settings** > **Billing** > **Bill themes**.
2. Select the bill theme that you want to edit. You can also click **New Theme** to create a new bill theme. Learn more about creating bill themes [here](https://help.clio.com/hc/en-us/articles/9285055886235).
3. Click **Matter** and then select **Services/Combined Orderings**.
4. Click and drag **Split Portion** and **Activity Total** from **Hidden Columns** to **Showing Columns**, and rearrange the order of the active columns as appropriate.

## Set up and generate split bills

Setting up and generating split bills is a simple process. You can start by adding multiple payers to a matter with the percentage portion of a bill that each would pay. Once this is done, add your time and expense entries as usual to the matter, generate the bill, and then send the bill to each payer to pay their portion. Split bills will show a **Split invoice** pill in the bills table to differentiate them from regular bills.

**Note:** You can only set up split billing for hourly and flat rate matters, not contingency matters.

**Tip:** If another contact is the primary payer on a matter rather than the main client (e.g. a young person is the client but their parent is paying any bills), you can set up the matter accordingly. Just add the other contact as a payer and set their invoice portion to 100% and the main client's portion to 0%.

#### Step 1: Add multiple payers to a matter:

1. Go to a matter and select **Edit matter** to view the matter form. You can also create a new hourly or flat rate matter. Learn more about creating matters [here](https://help.clio.com/hc/en-us/articles/9285959663131).
2. Scroll down to **Billing preference**.
3. Under **Split invoice**, check the box for **Split the invoices for this matter**.
4. Click **Add payer** to add an additional payer and then enter the amount the payer will be responsible for paying under **invoice portion**.
   - The matter's client will be added as a payer by default.
   - The total for all payers must add up to 100%.
   - If you want the payer's bill to be sent to all bill recipients, check the box for **Send invoice copy to all bill recipients**. By default, a payer will only receive their own bill, but if you check this box, all other bill recipients will receive a copy of this payer's bill.
5. Repeat step 4 to add additional payers. You can add up to 10 additional payers, not including the client, for a total of 11.
6. Click **Save matter** to finish.

#### Step 2: Add activities and generate a bill

**Note:** You can only generate a split bill using bulk billing.

1. As you complete work on the matter, record time and expense activities. Learn more about adding time entries [here](https://help.clio.com/hc/en-us/articles/9289741706779) and more about adding expense entries [here](https://help.clio.com/hc/en-us/articles/9289745356571).
2. To generate the bill, go to **Billing** and select **New bills**.
3. Select the bill and then click **Generate**. The split bill will show a **Split invoice** pill to help you find it more easily.
4. Complete the necessary details to generate the bill:
   - Under **Change bill theme**, select the bill theme where you enabled the split bill columns. If you did not previously enable the columns, see the steps under [Enable and arrange split billing bill theme columns](#h_01HXW5MD3G4RRQAKCFNVQTW4N2). Without these columns, your client and additional payers will not see the portion that they owe.
   - Under **Detail level**, select **All details**. You cannot select any other detail level.
   - Complete the remaining details. Learn more about the bill generation options [here](https://help.clio.com/hc/en-us/articles/9285169278747-Generate-Bills-for-Billing-in-Clio#h_01H5T70XAFX0Q5CE0ZGT0VP94D).
5. Click **Generate bills** to finish. Once generated, you can do the following:
   - Edit the split bill line items. Learn more [here](#h_01HXW5T5GCNFV9WC38TN1FTX34).
   - View the bill invoice that your client and payers will see. Learn more [here](#h_01HXW6HN5H1AYKN2VX51SZGK8Y).
   - Send copies of the bill to each payer. Learn more [here](https://help.clio.com/hc/en-us/articles/9285343645595).
   - Accept credit card, debit card, Apple Pay, Google Pay, or eCheck (US only) payment directly from payers via Clio Payments or manually record cash, check, or card payments. Learn more about accepting payments via Clio Payments [here](https://help.clio.com/hc/en-us/articles/12406718783131-Client-Payment-Actions) or more about manually recording payments [here](https://help.clio.com/hc/en-us/articles/9285641955355).
   - Apply matter-level or client-level trust funds to the primary client, and apply client-level trust funds to other payers (you cannot apply matter-level trust funds to bills issued to payers that are not the primary client).

## Edit split bills

If you need to make modifications to line items or add tax or discounts after generating split bills, you can edit each split bill as necessary.

1. Go to the main **Billing** tab or the **Bills** subtab in a contact or matter.
2. Select the **Draft**, **Pending approval**, or **Unpaid** quick filters, depending on whether you skipped the bill approval process when generating the split bills.
3. Find the split bill and then click **Edit** under the **Actions** column. Each split bill will show a **Split invoice** marker to differentiate it from regular bills and trust requests.
4. Make any necessary changes.
   - You can edit text fields (date and description) and the discount and tax fields.
   - You cannot edit numeric fields (quantity and rate) and the type field since these would impact other activities on other bills.
   - The **Activity category**, **Description**, and **Date fields** are linked to the other split bills, which means that changes to these fields will also be applied to the other linked split bills.
   - The tax and discount fields are independent of other split bills, which means that changes to these fields will only be applied to the bill that you are editing and not the other linked split bills. If you want to apply these changes to all of the split bills, you will need to edit them separately.
   - The **Update records** checkbox will be checked by default and cannot be unchecked.
5. Click **Save invoice** to finish.

## View split bills

After generating split bills, you can open the bill invoice to view what the client or each payer will see when viewing their bill. If you enabled the split bill columns in at least one bill theme and applied that bill theme when generating the split bills, each payer will also see additional columns:

- **Activity Total:** This column is the total of each activity line item across all of the split bills.
- **Your Portion:** This column is the percentage portion of the line item that the specific payer or client needs to pay.

To view split bills:

1. Go to the main **Billing** tab or the **Bills** subtab in a contact or matter.
2. Find the split bill. Each split bill will show a **Split bill** marker to differentiate it from regular bills and trust requests.
3. Under the **Id** column, click the bill id number. You can also click the down arrow under the **Actions** column and then select **View bill**.