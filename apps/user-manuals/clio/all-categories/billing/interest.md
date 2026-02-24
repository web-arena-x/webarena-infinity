# Interest

Source: https://help.clio.com/hc/en-us/articles/9285277478171-Interest

---

In Clio Manage, you can create payment profiles that automatically calculate when interest is charged on an overdue bill after the grace period passes. Any generated bill that is unpaid can collect interest if a payment profile is applied to the contact. This includes closed matters.

**Note**: Interest will only accrue on unpaid bills that are not fully paid.

## Charge interest on bills

Before interest can be charged on an overdue bill, you need to create a payment profile that specifies the grace period and the amount of interest that will be charged on a recurrent basis after the grace period passes and until the bill is paid fully. Once this payment profile is created, you can add it to the contact and generate the bill.

**Note**: If you want to charge interest to an overdue bill that has already been generated, you need to void the bill first. Then, you can follow the steps below.

**Step 1: Create a payment profile**

1. Go to **Settings** > **Billing** > **Payment Profiles.**
2. Click **Create a payment profile**.
3. Name the profile and then select **Custom Payment Terms.**
4. Select a grace period, and interest amount if payment is not received beyond the grace period.
5. *Optional:* Select the amount of discount if the bill is paid within a set number of days.
6. Click **Create Profile.**

**Step 2: Add the payment profile to the contact card**

1. Go to the contact and click **Edit** **contact**.
2. Scroll down to **Billing preferences.**
3. Under **Payment profile**, select the payment profile created in step 1.
4. Click **Save contact.**

**Step 3: Generate the bill**

Learn more about generating bills [here](https://help.clio.com/hc/en-us/articles/9285169278747).

## 

## Accrued interest terms

Once a generated bill’s grace period passes, the unpaid bill will accrue its first interest charge the day after the grace period ends, at midnight PST. The bill will continue to accrue interest depending on the interval specified in the payment profile.

Interest is applied to the entire bill, not individual activities on the bill. Additionally, each accrued interest will appear on the client’s bill invoice as a separate line item.

**Important:** Interest will continue to accrue on a bill until the bill is paid or voided. If you need to stop interest accrual on a bill, you need to remove any payments on the bill, void the bill, and then generate a new bill.