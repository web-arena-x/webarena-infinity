# Discounts

Source: https://help.clio.com/hc/en-us/articles/9285279237787-Discounts

---

In Clio Manage, you can apply a discount to an entire bill or to individual activities on a generated bill. You can apply discounts to bills in draft and bills pending approval.

**Tip:** You can apply discounts to approved bills if you have this setting turned on. See the "Edit bill activities" section of [this article](https://help.clio.com/hc/en-us/articles/9285222010395) to learn more.

## Apply discounts to bills

Discounts are applied before any taxes are calculated and after any credit notes. Additionally, if a bill has an interest charge, the discount is applied to the total outstanding balance first, followed by the principal amount, and then the interest.

**Note:** If you apply discount to the whole bill rather than individual line items, the discount is applied proportionally across all line items on the bill.

1. Go to the main **Billing** tab or the **Bills** subtab in a matter or contact
2. Select the **Draft** or **Pending approval** quick filters.
3. Click **Edit.** You can also click **Edit** when viewing the bill.
4. To apply a discount to the entire bill, add the **Discount amount** and percentage or dollar amount and add a **Discount note**. To apply discount to individual line items, click the value under the **Discount** column to change it. 

   **Note:** The **Discount note** is limited to 255 characters and will appear on the bill invoice.
5. Click **Save invoice.**

## Set up early payment discounts

If you offer a discount for early payment, you can apply the discount using the method above, but you can also create a payment profile and apply it to the contact. The generated bill will automatically show the discount and discounted amount that is due. If the bill is not paid in full before the early payment discount expires, the discount will automatically disappear from the bill. Follow the steps below to create a payment profile for early payment discount.

**Tip:** Once a bill with an early payment discount is paid within the discount period, you can view the discounted amount and percentage. Go to **Billing** or the **Bills** subtab in the contact or matter, click the bill **Id**, and then select the **Credit notes** subtab.

**Note:** You cannot apply a payment profile for early payment discount to a bill that has already been generated. If you want to apply discount using this method to a generated bill, you will need to void or delete the bill, apply the payment profile to the contact, and then generate the bill again.

1. Go to **Settings** > **Billing** > **Payment Profiles.**
2. Click **Create a payment profile**.
3. Name the profile and then select **Custom Payment Terms.**
4. *Optional:* In the first box, enter a grace period.
   - This is the number of days the client has to pay their bill in full before interest is charged.
5. In the next two boxes, enter the terms for the early payment discount. You can choose the amount of discount that will be applied if the bill is paid within a set number of days.
   - The discount period is inclusive of a bill's issue date. This means that the payment profile will use the bill's issue date as the first day of the discount period.
6. *Optional:* In the last three boxes, enter the interest amount if payment is not received within the specified grace period. Learn more about interest [here](interest.md).
7. Click **Create Profile.**
8. Edit the contact to change the payment profile. Learn more [here](https://help.clio.com/hc/en-us/articles/9285717159707).
9. Generate the bill. Learn more [here](https://help.clio.com/hc/en-us/articles/9285169278747).