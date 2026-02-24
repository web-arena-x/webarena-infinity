# Preventing account suspension

Source: https://support.zendesk.com/hc/en-us/articles/4408846497434-Preventing-account-suspension

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article describes how to proceed if you receive an email or an in-product warning that your Zendesk payment has been declined. Payment may be declined if your credit card has expired or if your payment method is out-of-date.

This article contains the following topics:

- [Updating your account payment](#topic_l4v_pbq_zgb)
- [Notifications for past-due payments](#topic_udz_1yp_zgb)
- [Notifications for manual invoice customers](#topic_oj5_vfq_zgb)

## Updating your account payment

If you received an email or an in-product warning saying that your Zendesk payment has been declined, update your credit card details (or provide a different payment method) to prevent account suspension. Refer to [Managing payments](managing-payments.md) for more information. Only the [account owner](https://support.zendesk.com/hc/en-us/articles/4408822084634-Changing-account-ownership) can update a payment method for the account.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/payment_failed_second_owner.png)

Once your payment method is updated, the Zendesk payment gateway automatically tries to charge your account again. When payment succeeds, a confirmation email is sent to all billing contacts listed on your account.

Note: If you update your payment method and you still experience issues with your credit card, refer to the article [Resolving issues when your credit card fails](https://support.zendesk.com/hc/en-us/articles/4408832461210).

## Notifications for past-due payments

The following notification schedule applies for past-due payments:

- **First email (Renewal Date)**: If the Zendesk payment system attempts and fails to process a payment, an email is sent to all billing contacts.
- **Second email (Renewal Date +2 days)**: If the Zendesk payment system attempts and fails to process a payment, another email is sent to all billing contacts. The account owner and admins also see the first pop-up warning in the Zendesk account.
- **Third email (Renewal Date +4 days)**: If the Zendesk payment system attempts and fails to process a payment, another email is sent to all billing contacts. The account owner and admins also see a second pop-up warning in the Zendesk account.
- **Suspension warning (Renewal Date +21 days)**: If the Zendesk payment system attempts and fails to process a payment, an email is sent to all billing contacts warning of pending account suspension.
- **Account suspension (Renewal Date + 22 days)**: If the Zendesk payment system attempts and fails to process a payment, Zendesk account functions are restricted. The account owner, admins, and agents also see a final pop-up warning in the Zendesk account.

 Talk accounts are suspended, all Explore reports and dashboards are deleted, and any Zendesk-provisioned SSL certificates are removed. No tickets or emails will reach your Zendesk account, and you won't be able to respond to existing tickets until Zendesk has a successful payment.

 After three days, Zendesk phone numbers are permanently deleted from the account. Your payment method can still be updated by your account owner. Follow the prompts in the pop-up message or refer to [Managing payments](managing-payments.md).

 Once you restore payment, you need to contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to re-enable Talk, Explore, and SSL.
- **Account cancellation (Renewal Date + 29 days)**: Access to your Zendesk account is disabled. Explore reports and dashboards can no longer be recovered. Submit a request to [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) for temporary (limited access) account reactivation to allow your account owner to update the payment method.

Important: After 90 days from suspension date, all your Zendesk data is deleted and reactivation is not possible. Refer to the [Zendesk Service Data Deletion Policy](https://support.zendesk.com/hc/en-us/articles/4408883628954).

## Notifications for manual invoice customers

Notifications differ slightly for customers who aren't set up for automatic payments. These customers are considered *manual invoice customers*.

- Email reminders are sent to the primary billing contact when invoices are 15, 30, 45, 60, and 65 days past due.
- When an invoice reaches 30 days past due, the Zendesk Financial Operations sends emails to all billing contacts, the account owner, the sales representative, and the AR team.
- If no payment is received after 65 days, the account is suspended.