# Payment Plans

Source: https://help.clio.com/hc/en-us/articles/9285735777819-Payment-Plans

---

With payment plans, you can receive regular credit card payments toward a client’s outstanding balance until the balance or some set amount is paid, toward a client’s trust account, or for ongoing services. US customers using Clio Payments can accept either credit card or eCheck payments on a payment plan. Canadian customers using Clio Payments can accept credit card payments on a payment plan.

**Note:** Administrators and users with billing permissions can create, edit, or delete payment plans.

## Payment plan terms

- If your client has multiple outstanding bills, an active payment plan toward an outstanding balance will pay off the bill with the oldest due date before moving on to the subsequent bill. You cannot change the order in which bills are paid off.
- If two bills have the same due date, payment will be applied to the bill that was created first.
- If the remaining amount on an outstanding bill is less than the authorized payment plan amount, only the remaining bill amount will be charged.
- An active payment plan toward an outstanding balance will continue to debit payment until all due bills are fully paid, regardless of whether a payment fails or is voided, or until the plan is manually stopped.
- An active ongoing payment plan will continue until the plan is manually stopped.
- When payment is processed or fails, both you and the client will be notified via email.
  - If the payment plan is toward an outstanding balance, the payment confirmation email will include the remaining outstanding balance.

    **Note:** If a payment fails due to invalid card details, a canceled or expired card, or another reason, you can [stop the payment plan](payment-plans.md#h_01HBBPSK79W0GNSJ9Q1QFSKNXA) and [create a new one](payment-plans.md#h_01HBBPSK7864Y50SB770W0W8CV) with a valid payment method or you can [edit the existing payment plan](payment-plans.md#h_01HBBPSK78TJB1Q9WQ4MA88K0C) by requesting your client to save a new payment method.
- Payments on trust fund payment plans will remain on the client-level, not on the matter-level.
- Automated bill reminders are paused when a client has an active payment plan.

## Create payment plans

When you create the plan, the client will receive an email notification about their payment plan. Once the payment plan is active, payments will continue based on the information provided for the total payment amount and the repetition (repeat until) condition using the payment method provided. A payment plan can be towards outstanding amounts, ending once the owed amounts are paid, or it can be an ongoing payment plan. Payment can also be [manually stopped](payment-plans.md#h_01HBBPSK79W0GNSJ9Q1QFSKNXA) at any time.

**Note:** Clients cannot set up their own payment plans. Only firm users with the appropriate permissions can do this.

1. Go to **Online payments** > **New payment plan**.
2. Add the contact, bank account that funds will be deposited into, amount per payment, start date, payment frequency, and repetition (**Repeat until**) condition. For the **Repeat until** field:
   - Choose **Total payment amount reached** if you want the payment plan to end once the specified total payment amount is reached. Set a fixed amount or allow the plan to apply to the entire outstanding balance which continuously updates as amounts are paid or bills are added.

     **Note:** Any outstanding amounts from matters with [split billing enabled](https://help.clio.com/hc/en-us/articles/25704317136155) will not be included in the outstanding balance.
   - Choose **Ongoing** to continue the payment plan until you manually end it.
3. Click **Next step**.
4. Confirm the payment plan details and click **Create payment plan**.

## Edit payment plans

Once created, you can edit a payment plan's details, including the recurring payment amount, payment frequency, and payment method. When you make changes to the plan, your client will receive an email notification.

**Note:** Before changing the payment method, first [request a new payment method from your client](request-and-store-payment-methods.md#h_01HBVBVGTQGY358B95ECGXT2KP). Once they save a new payment method, you can edit the plan and choose their new payment method. The next payment will be processed using the new payment method[.](request-and-store-payment-methods.md#h_01HBVBVGTQGY358B95ECGXT2KP)

1. Go to **Online payments**.
2. Select the **Payment plans** subtab.
3. Find the payment plan that you want to change and then click **Edit**.
4. Make your changes.
5. Click **Save payment plan**.

## Stop payment plans

An active payment plan will automatically end and go into an inactive state when the entire overdue bill balance is paid. The client will not be notified by email. You can also stop a payment plan at any time. If you stop a payment plan, the client will receive a notification email. If automated bill reminders were previously enabled for this client, they will resume once the plan is stopped.

**Note:** Inactive payment plans will not reactivate when a new bill is generated. Once a payment plan ends, you will need to create a new one for a new bill.

1. Go to **Online payments**.
2. Select the **Payment plans** subtab.
3. Click the down arrow next to **Edit** and select **Stop**.
4. When the warning prompt appears, click **Stop**.