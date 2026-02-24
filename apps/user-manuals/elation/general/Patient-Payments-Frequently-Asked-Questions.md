# Patient Payments Guide - Frequently Asked Questions

Source: https://help.elationhealth.com/s/article/Patient-Payments-Frequently-Asked-Questions

---

# **Contents**

- [General questions](#general)
- [Sending and receiving payment requests](#sending_and_receiving)
- [Tips & tricks to increase collection rate](#collection_rate)
- [Managing your account](#managing_account)

# **General Questions**

| | |
| --- | --- |
| How do we submit our questions and feedback to the Elation team? | Please use the **I need help** -> **Contact Elation Support** option from your Elation account or fill out our [Contact Form](https://help.elationemr.com/s/contactsupport). |
| Is the Payment feature secure? | Elation Patient Payments is powered by Stripe. Stripe is a secure, digital, payment processing platform that is Payment Card Industry (PCI) compliant and utilizes best-in-class security tools to maintain a high level of security. Any information you enter during the payment process is securely encrypted. For more information in regards to Stripe’s Security and Privacy Policy, please see:   - Security info: <https://stripe.com/docs/security/stripe> - Privacy Policy- <https://stripe.com/privacy> |

# **Sending and receiving payment requests**

| | |
| --- | --- |
| Can I accept HSA and FSA payments using the Patient Payment feature? | Yes, patients can pay with their HSA or FSA cards when paying a balance through Elation Patient Payments.   If you are running into issues receiving FSA or HSA payments, follow these steps to verify you have the correct 'Industry' selection in your Stripe settings: 1. In your **Patient Payments** settings page in Elation EHR, click on **Go to Stripe account**. 2. Click **Edit** (pencil icon). 3. Update your **Industry** to 'Doctors and Physicians'. |
| What does this look like to my patients? | Our patient guide on how to complete payment requests is available [here](https://docsend.com/view/ke9fikv3nvga3ykr). Feel free to download and send this to your patients directly! |
| How can I resend, refund or void a payment request? | Take action on any transaction in the Elation Patient Payments Report. Resend or void outstanding requests, refund paid requests, mark any payment as paid via cash/check and more. Click the “**...**” icon in the **Actions** column within the report to take action on a specific transaction. |
| How can I print a receipt for my patient? | The option to print a receipt is available from the **Patient Payment** payment window after a charge has been completed. The patient will also automatically receive an electronic receipt via text or email depending on their preferred contact method. |
| What do the different statuses in the Patient Payment Report mean? | - **Paid:** The payment request was completed and paid, either via cash/check or credit card and a receipt has been sent to the patient’s preferred contact method. - **Card declined:**The attempt to charge a manually entered card number failed (not a saved card-on-file). - **Charge pending:** A credit card on file was charged and will be automatically charged within 24hrs. The charge is still in the 24hr window. - **Payment requested:** A payment request was sent via email or text and has not yet been paid by the patient. - **Payment declined:** The attempt to charge a card-on-file failed (likely due to an expiration or insufficient funds). Patients will be automatically notified when a payment is declined and are prompted to update card information to resubmit payment. - **Refunded:** The payment was refunded to the original payment method - **Void:** The payment request was voided, meaning the patient will no longer be able to complete/submit payment for this specific transaction. |
| Can I track when a Payment was requested or paid? | Track payment requests and payments through the **Patient Payment Report**. From the blue navigation bar, go to **Reports** -> **Patient Payment Report**. The **Patient Payment Report** will update the status of each transaction in real-time. |
| Does the Payment feature allow for partial payments? | The Payment feature currently does not allow for partial payments. The requested amount is the amount that the patient must pay when inputting payment information. You can break up payment requests for a single service by sending multiple payment requests for that service (E.g. Deductible for Date of Service July 1, 2020, payment 1 of 3). Or you can have the patient pay partial payments through your Payment Site, as they are able to choose the amount they pay through the site. |
| Can I send a payment request from the Patient’s chart or appointment? | To initiate a payment request, charge payment information on file, or log a cash/check payment, go to the **Practice Home** or the patient's chartand click on **Payment** or go the the **Patient Payments Report** and click **Send payment request.** |

# **Tips & tricks to increase your collection rate**

| | |
| --- | --- |
| Resend outstanding payment requests to remind payments to submit payment | From the blue navigation bar, go to **Reports** -> **Patient Payment Report**. Within the **Patient Payment Report**, you can take action on any transaction in real-time. Filter the report for outstanding payments where status is 'Payment requested' and choose **Resend request** in the **Actions** column. |
| Collect and charge your patients' cards-on-file. This will help guarantee your practice payment, but also make it easier on your patients as they won't have to enter payment details multiple times. | Patients can choose to store a card-on-file for future payments through completing a payment request. They will need to keep the checkbox **Keep this card on file** checked when completing the payment.   Once you have charged a card on file, the patient will be notified of the pending charge. The charge will automatically be collected within 24hrs. This gives the patient time to update their card-on-file or contact your office with any questions. Once the charge is completed, the patient will receive a receipt via text or email. |
| Select a Payment Reason relevant to the services that the patient is being charged for so that they have an idea of why they are paying. | Select one or more **Payment Reasons** in the payment request window before submitting the payment request or charge to your patients. These reasons will be displayed to the patient within the emailed or text request they receive. |

# **Managing your account**

| | |
| --- | --- |
| I received an email from Stripe saying I needed prior authorization to accept Telehealth payments via Stripe. What should I do? | Share a copy of the contents of your email with the [Support Team](https://help.elationemr.com/s/contactsupport) and we will work with Stripe to get your account cleared. |
| How do I update the phone number and email that display in my patient payment requests? | To update the phone number and email displayed on your payment requests, go to your Settings page in Elation and update the information associated with your primary practice location. Navigate to **Settings** -> **Practice Locations**, and click **Edit** next to the location tagged as your 'Primary Location'. |
| Do my staff have access to my Stripe Dashboard? | Anyone can view & manage the **Patient Payments** Settings section in Elation. To limit access, toggle to **Admin Only** to only allow Admin users. Only a Stripe Team Member (managed in the **Team Member** section in the Stripe account screen) can edit Stripe account information. And all changes will be verified by a two-factor authentication text that will be sent to the mobile number the account was activated with. |
| How can I add more Team members to my Stripe account? | 1. Go to the **Patient Payment** Settings page in Elation. 2. Click **Go to Stripe Account**. 3. Click **Account**. 4. Click **Manage** under Settings. 5. The existing Account Representative will need to enter a 6 digit verification code (sent to their mobile phone on file) into the form and the form will automatically proceed to the next page. 6. Click **+ Add team member**. 7. Enter the team member's email address and click **Invite**. 8. The new team member will go to their email and click the **Accept Invite** button in their invitation email. 9. The new team member enter their mobile number for account verification. 10. The new team member will enter the 6 digit verification code (sent to their mobile phone) into the form and the form will automatically proceed to the next page. 11. A message that says "You have successfully joined your practice's account." will appear on the Elation Health Stripe Account page for confirmation. |
| How much does Elation Patient Payments cost my practice? | Elation charges a flat rate for each transaction you collect (there is no fee associated with logging a cash/check payment). There are no startup costs, minimums, or termination fees. Elation will not charge you for refunding a transaction. However, the flat rate we charge for processing the transaction will not be refunded. |
| Where can I find my practice's processing rate? | If you have any questions about your processing rate, use **I need help** → **Contact Elation Support** and our Support Team will be able to assist you. |
| Does Stripe charge my practice additional fees? | No. Stripe and card networks do not charge fees beyond Elation's processing fee. Elation's fee covers all payment processing costs. |
| Can I pass processing fees onto patients? | Elation does not support automatically adding a surcharge or convenience fee to patient payments within the product. Consult your legal counsel if you are considering surcharging practices. |
| Does Patient Invoicing incur processing fees? | No. Generating invoices through [Patient Invoicing](https://help.elationemr.com/s/article/patient-invoicing) does not incur processing fees. Elation's percentage-based fee applies only to payments processed via Patient Payments. |
| How do I see how much transaction fee was deducted for each payment? | Download the Patient Payment Report to see a breakdown of the payments collected and the transaction fees deducted for each collected payment.   1. From the blue navigation bar click **Reports** -> **Patient Payment Report**. 2. Filter the report as needed. 3. Click **Download CSV**. |
| How do I obtain an 1099 Tax Form for tax reporting purposes? | [Click here to learn more about obtaining a 1099 Tax Form for your Stripe account](Patient-Payments-Guide-Obtaining-a-1099-Tax-Form-for-your-Stripe-account.md). |

# **Related Articles**

- [Patient Payments Guide - Securely collect payments digitally from patients](https://help.elationemr.com/s/article/using-elation-to-securely-collect-patient-payments)
- [Patient Payments Guide - Obtaining a 1099 Tax Form for your Stripe account](Patient-Payments-Guide-Obtaining-a-1099-Tax-Form-for-your-Stripe-account.md)