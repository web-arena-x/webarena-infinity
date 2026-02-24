# Membership Management- Frequently Asked Questions

Source: https://help.elationhealth.com/s/article/Membership-Management-Frequently-Asked-Questions

---

## **Recommended Reading**

See the [Membership Management Introduction](Introduction-to-Membership-Management-with-Elation.md) article to learn more about the Membership Management feature.

###

## **Contents**

- [Creating and Managing Membership Plans](#creating)
 - [What happens to patients currently enrolled in a plan if I delete that plan?](#a1)
 - [What information about a plan is patient-facing?](#a2)
 - [What happens to patients currently enrolled in a plan if I change the billing amount?](#a3)
 - [Is there a limit on the number of plans that can be created?](#a4)
 - [How can I create employer plans?](#a5)
 - [How can I create group/family plans?](#a6)
 - [How can I create memberships based on age?](#a7)
 - [How can I create a fixed-duration membership (ex: 6-month plan or set number of visits)?](#a8)
- [Enrollment](#enrollment)
 - [What does a patient see when an enrollment occurs?](#b1)
 - [How do I enroll a group of patients in a group/family membership?](#b2)
 - [Can we provide a way for patients to self-enroll in a membership?](#b3)
 - [Does Elation offer a free pre - enroll period where patients can sign up for our practice before we are live?](#b4)
 - [How do I move a patient from one plan to another?](#b5)
 - [How do I handle group plans that are based on number of members? Ex: if a group of 4 needs to be moved to a plan for 5, what needs to happen?](#b6)
 - [Can a patient be enrolled in multiple memberships?](#b7)
 - [Can I pause a patient’s subscription?](#b8)
 - [How do I enroll a patient who plans to pay using cash or check?](#b9)
 - [How do I remove one patient from a group?](#b10)
- [Payments, Fees, and Refunds](#payments)
 - [What are the options for billing frequency?](#c1)
 - [What methods can I use for collecting payments (credit card, cash, check, etc.)?](#c2)
 - [When will I receive my payments?](#c3)
 - [How do I manage enrollment fees?](#c4)
 - [How do I give a refund?](#c5)
 - [How can I find a list of patients who are past due?](#c6)
 - [How can discounts be given to specific patients or groups of patients?](#c7)
 - [How do I offer promotions for joining a practice?](#c8)
 - [How do I handle associating payments to a family’s head of household?](#c9)
 - [Am I alerted if a patient does not pay their membership?](#c10)
 - [What happens if a patient does not have a card on file?](#c11)
 - [How quickly do refunds appear on a patient’s credit card statement?](#c12)
 - [How quickly will refunds be visible to me?](#c13)
 - [How are membership fees labeled on the payment request sent to the patient?](#c14)
- [Communication](#communication)
 - [What actions trigger automated communications to patients?](#d1)
 - [Does Elation offer pre-drafted documents to send to patients when their card expires?](#d2)
 - [Does Elation offer pre-drafted documents to send to patients when they are due to renew?](#d3)
 - [When are payment reminders / notifications sent to patients? What if the patient continues to not pay their bill?](#d4)
 - [Will patients be notified if I change the details of a plan?](#d5)
 - [D](#d6)[oes Elation have the option to send a "Welcome Letter" once a patient enrolls to our practice?](#d6)
 - [Will a patient get a payment request even if they paid cash/check already?](#d7)

## **Creating and Managing Membership Plans**

###

#### **What happens to patients currently enrolled in a plan if I delete that plan?**

If a membership plan is deleted, all patients that were enrolled in that plan will become unenrolled immediately. No notification is sent to patients when they are unenrolled.

###

#### **What information about a plan is patient-facing?**

Patient communications may include the membership plan display name, as well as the billing amount, start date, and billing frequency. The membership plan description is not currently patient facing but it may be in the future.

###

#### **What happens to patients currently enrolled in a plan if I change the billing amount?**

If changes are made to the billing amount, all patients enrolled in that plan that do not have an override amount set to their subscription will automatically be charged the updated amount on their renewal date. A membership update message will be sent to the patient showing the new information associated with the plan.

###

#### **Is there a limit on the number of plans that can be created?**

There is no limit to the number of plans that can be created.

###

#### **How can I create employer plans?**

A unique plan can be created for each employer. As an example, you could create an “Acme Co. Plan” for the Acme Company. A chart could be created for the employer, which you could then used as the primary member when enrolling patients on the plan. As patients are added and removed from the plan, you can either modify the override amount for the primary member, or update the billing amount at the plan level. For example, if there are 9 members currently on a plan and you charge $50 per member per month, when a 10th member is added you can either…

1. change the primary members override amount from $450 to $500, or
2. update the billing amount at the plan level from $450 to $500

#### **How can I create group/family plans?**

Unique plans can be created for various combinations of patients. For example, you could create plans like:

- Individual
- 2 adults
- 2 adults 1 child
- 1 adult 1 child

When enrolling patients, you can add them into the appropriate group/family plan. If the dynamics of the group/family change, such as a new child being born, you can then unenroll the group/family from their current plan, and enroll them into an appropriate plan. Alternatively, you can keep the group on the same plan, but override the billing amount to reflect the new number of people on the plan.

###

#### **How can I create memberships based on age?**

Unique plans can be created for specific age ranges, such as:

- Under 18
- 18-29
- Over 65

At the time of enrollment, you can add patients into the appropriate age-based plan. As patients age, you can unenroll the patient in their current plan, and enroll them into the appropriate plan.

To ensure patients are on the right age-based plan, you can use the Memberships Report. By clicking the ‘Edit Columns’ button, you can choose to add a ‘Patient Age’ column to the report. You can then filter for a given age-based plan, and then review the values in the ‘Patient Age’ column to make sure all the patients are in the right plan. If any patients are nearing the upper bound of the age limitations for the plan, you can click the name of the patient in the Membership Report to open their chart in a new tab, and then create a post-dated message that prompts you to contact the patient about moving into the appropriate age-based plan at the right time.

###

#### **How can I create a fixed-duration membership (ex: 6-month plan or set number of visits)?**

A unique membership plan can be created that corresponds to the type of membership being offered. During enrollment, you can create a post-dated message to trigger the appropriate follow-up action. For example, if you are enrolling a patient on a 6-month plan on 01/01/2023, you can create a message post-dated for the end of June that prompts you to reach out to the patient to see if they want to re-enroll or let their membership expire. You can then take the appropriate action.

## **Enrollment**

###

#### **What does a patient see when an enrollment occurs?**

When a patient is enrolled in a membership plan, they will receive a message providing the details of the enrollment. This will include the plan name, start date, billing amount, billing frequency, and automatic payment information (if applicable).

###

#### **How do I enroll a group of patients in a group/family membership?**

To enroll patients in a group/family membership, follow the steps to [enroll a patient from Practice Home](Using-Elation-Membership-Management-to-Create-Membership-Plans-and-Manage-Enrollments.md#four) or [from Patient Demographics](Using-Elation-Membership-Management-to-Create-Membership-Plans-and-Manage-Enrollments.md#five) , and use the ‘Patient Name’ field to search for and add the additional members.

###

#### **Can we provide a way for patients to self-enroll in a membership?**

Yes, please follow the instructions on this [help center article](https://help.elationemr.com/s/article/Membership-Management-Patient-Self-Enrollment).

###

#### **Does Elation offer a free pre - enroll period where patients can sign up for our practice before we are live?**

Patients can be enrolled into memberships with start dates that are set for some point in the future. This will enable you to provide services to patients without charging them until a specific date.

###

#### **How do I move a patient from one plan to another?**

To move a patient from one plan to another, you can unenroll the patient from their current plan and then enroll them into the new plan. You can unenroll the patient from Patient Demographics, or by using the ‘Unenroll’ option in the actions menu in the Memberships Report

- [To unenroll using Patient Demographic](Using-Elation-Membership-Management-to-Create-Membership-Plans-and-Manage-Enrollments.md#nine)
- To unenroll using the Memberships Report
 1. Click the ‘Memberships Report’ option in the ‘Reports’ dropdown at the top of the Elation window
 2. Browse the report or use the filters to find the appropriate patient
 3. Click the ‘…' action menu and select 'Unenroll’
 4. Click ‘Unenroll & remove’ to confirm

###

#### **How do I handle group plans that are based on number of members? Ex: if a group of 4 needs to be moved to a plan for 5, what needs to happen?**

To move a group of patients from one plan to another, you can unenroll any of the patient from their current plan and then enroll them into the new plan (unenrolling one member will unenroll the entire group). You can unenroll the patient from Patient Demographics, or by using the ‘Unenroll’ option in the actions menu in the Memberships Report.

- [To unenroll using Patient Demographic](Using-Elation-Membership-Management-to-Create-Membership-Plans-and-Manage-Enrollments.md#nine)
- To unenroll using the Memberships Report
 1. Click the ‘Memberships Report’ option in the ‘Reports’ dropdown at the top of the Elation window
 2. Browse the report or use the filters to find the appropriate patient
 3. Click the ‘…' action menu and select 'Unenroll’
 4. Click ‘Unenroll & remove’ to confirm
- To enroll patients in a group/family membership
 - Follow the steps to [enroll a patient from Practice Home](Using-Elation-Membership-Management-to-Create-Membership-Plans-and-Manage-Enrollments.md#four) or from [Patient Demographics](Using-Elation-Membership-Management-to-Create-Membership-Plans-and-Manage-Enrollments.md#five) , and use the ‘Patient Name’ field to search for and add the additional members.

#### **Can a patient be enrolled in multiple memberships?**

Yes, a patient can be enrolled in an unlimited number of memberships simultaneously.

###

#### **Can I pause a patient’s subscription?**

Yes, a patient’s subscription can be paused at any time from either Patient Demographics or the Memberships Report

- [To pause a subscription using Patient Demographic](Using-Elation-Membership-Management-to-Create-Membership-Plans-and-Manage-Enrollments.md#seven)
- To pause a subscription using the Memberships Report
 1. Click the ‘Memberships Report’ option in the ‘Reports’ dropdown at the top of the Elation window
 2. Browse the report or use the filters to find the appropriate patient
 3. Click the ‘…' action menu and select 'Pause’
 4. Click ‘Pause billing’ to confirm

###

#### **How do I enroll a patient who plans to pay using cash or check?**

You can enroll your patient in a membership without planning to charge a card on file. The patient will continue to receive payment reminders on the billing date associated with their plan.

Each time the patient has a new charge for their membership fee (this charge will coincide with their billing date), there will be a new item listed in the Patient Payments Report. You can then access this information and mark that line item as paid.

###

#### **How do I remove one patient from a group?**

If you attempt to unenroll a member, you will be notified that you will be unerolling the group. To remove a single member, you can ‘Edit’ the group. Groups can be edited from Patient Demographics or from the Memberships Report.

- To remove a member from a group using Patient Demographics
 1. Open a patient’s chart
 2. Click on the patient’s name to open Patient Demographics
 3. Scroll to the Membership Information section
 4. Click ‘Edit’
 5. Click the ‘X' next to one or more group member’s names to remove them
 6. Click ‘Update Enrollment’
- To remove a member from a group using the Memberships Report
 1. Click the ‘Memberships Report’ option in the ‘Reports’ dropdown at the top of the Elation window
 2. Browse the report or use the filters to find the appropriate patient
 3. Click the ‘…' action menu and select ‘Edit’
 4. Click ‘Edit’
 5. Click the ‘X' next to one or more group member’s names to remove them
 6. Click ‘Update Enrollment’

##

## **Payments, Fees, and Refunds**

###

#### **What are the options for billing frequency?**

You can select from monthly, quarterly, semi-annually or annually.

###

#### **What methods can I use for collecting payments (credit card, cash, check, etc.)?**

Patients can pay by credit/debit card, ACH, cash, or check. Credit/debit card and ACH payments can be made automatically if a patient has details on file and the enrollment is configured to automatically charge the method on file. Payments made via cash or check will need to be done directly with your practice, and you can then update the payment record in Elation to show the charge was paid using the Patient Payments Report.

###

#### ****When will I receive my payments?****

Your practice is paid out weekly, every Monday on a two-day rolling basis. This means that your financial week runs from Friday to Thursday. The cut-off for weekly Monday payout is Thursday. If you process a payment on Friday, for example, that payment will be deposited on the following Monday (9 days later).

###

#### **How do I manage enrollment fees?**

You can charge enrollment fees by creating a payment request.

- From Practice Home, click ‘Payment’
- Search for the appropriate patient
- Enter the enrollment fee amount
- Select a Payment Reason (ex: “Membership fee- medical services”)
- Select a Payment Method and Payment Option
- Complete the request

###

#### **How do I give a refund?**

Refunds can be issued through the Patient Payment Report.

- Click the ‘Patient Payments Report’ option in the ‘Reports’ dropdown at the top of the Elation window
- Browse the report or use the filters to find the appropriate patient
- Click the ‘…' action menu and select ‘Refund’

**Note**: Individual line items in the Patient Payment Report can be refunded, but there is no option to issue a partial / pro-rated refund.

###

#### **How can I find a list of patients who are past due?**

The Memberships Report can be filtered to show all patients who are past due.

- Click the ‘Memberships Report’ option in the ‘Reports’ dropdown at the top of the Elation window
- Use the ‘Status’ filter and select ‘Past Due’

###

#### **How can discounts be given to specific patients or groups of patients?**

Discounts can be provided through a few different means:

1. Create a membership plan with a built-in discount
   - Follow the process for [adding a new plan](Using-Elation-Membership-Management-to-Create-Membership-Plans-and-Manage-Enrollments.md#one), but modify the billing amount so it reflects a discount
   - Enroll patients in this discounted plan
2. Override the billing amount for a specific plan when completing enrollment
   - Follow the steps to [enroll a patient from Practice Home](Using-Elation-Membership-Management-to-Create-Membership-Plans-and-Manage-Enrollments.md#four) or from [Patient Demographics](Using-Elation-Membership-Management-to-Create-Membership-Plans-and-Manage-Enrollments.md#five) , and use the ‘Override’ feature to enter a discounted billing amount
3. Provide a ‘free’ period during enrollment
   - Follow the steps to [enroll a patient from Practice Home](Using-Elation-Membership-Management-to-Create-Membership-Plans-and-Manage-Enrollments.md#four) or from [Patient Demographics](Using-Elation-Membership-Management-to-Create-Membership-Plans-and-Manage-Enrollments.md#five) , and set the Start date for a point in the future. The patient will receive notice of enrollment immediately, but they will not be charged until the Start date.

###

#### **How do I offer promotions for joining a practice?**

Promotional rates can be offered by enrolling a patient into a discounted plan, and then later enrolling them in another plan at the standard rate. After enrollment, you can create a post-dated message to trigger the appropriate follow-up action. For example, if you are offering a 3-month discount, you can create a message post-dated for the end of the 3-month period that prompts you to unenroll the patient from the discounted membership and enroll them in the standard membership.

###

#### **How do I handle associating payments to a family’s head of household?**

When enrolling multiple patients in a group/family plan, you will designate a primary member for that enrollment. The primary member will receive all membership notifications and charges for the group. Note: other charges manually sent to the patient using a Patient Payment Request will go directly to the selected patient, even if they are the secondary members on a plan.

###

#### **Am I alerted if a patient does not pay their membership?**

If a patient is past due, this information is visible in the Status column of the Memberships Report and in the Membership Information section of Patient Demographics.

###

#### **What happens if a patient does not have a card on file?**

If the patient does not have a card on file at the time of enrollment and you choose to automatically charge a card, Elation will send a payment request to the patient. Patients can choose to store a card-on-file for future payments through completing a payment request. They will need to keep the checkbox “Keep this card on file” checked when completing the payment.

###

#### **How quickly do refunds appear on a patient’s credit card statement?**

The patient will see the refund in ~5-10 business days. The refund request will be submitted to the appropriate card issuer immediately, but the time required to process the refund can vary based on the card issuer and underlying bank.

###

#### **How quickly will refunds be visible to me?**

When you issue a refund, the refund amount should be deducted from your Stripe account balance immediately, which means that the next transfer or two to your bank account would be smaller to reflect this.

###

#### **How are membership fees labeled on the payment request sent to the patient?**

The payment request will include a ‘Reason’ field, which will show ‘Membership fee- medical services.’

## **Communication**

###

#### **What actions trigger automated communications to patients?**

- Enrollment Confirmation
 - Upon enrollment, the patient will receive confirmation of plan name, frequency, billing amount, first payment date, card on file (if applicable), other members (if applicable)
- Payment Request
 - Payment request is sent automatically based on the frequency of the plan. The email is sent on the due date
 - If the patient is being charged automatically, they’ll be charged 24 hours after the notice is sent. The patient will be considered past due if payment hasn’t been processed 24 hours after the due date
- Modifying a Plan
 - If changes are made to the billing amount or billing frequency, patients will be updated about the change. Changes to plan name, display name or description will not automatically notify patients.

**Note**: No communication goes to patients who are secondary members on group/family plans

###

#### **Does Elation offer pre-drafted documents to send to patients when their card expires?**

Elation sends a notification if a card is declined, and will request that a new card be put on file. You can check the status of the payment on the Patient Payment Report, where you will see a declined charge. If the patient enters a new card and the payment succeeds, you will see a successful charge in addition to the previous declined charge (note: these will appear as two separate charges in the Patient Payment Report).

###

#### **Does Elation offer pre-drafted documents to send to patients when they are due to renew?**

Yes, a message is sent automatically on the payment due date based on the enrollment start date and corresponding billing frequency. These messages are not configurable.

###

#### **When are payment reminders / notifications sent to patients? What if the patient continues to not pay their bill?**

Patients will receive a payment request based on the billing date associated with their plan. If the patient does not take action on the request, you can send a reminder from the Patient Payment Report using the ‘Resend payment request’ option in the '…' Actions menu.

###

#### **Will patients be notified if I change the details of a plan?**

If changes are made to the plan name, display name, or description, no message will be sent to the patients enrolled on the plan. However, if the billing amount or billing frequency is changed, a membership update message will be sent to the patient showing the new information associated with the plan.

###

#### **Does Elation have the option to send a "Welcome Letter" once a patient enrolls to our practice?**

An enrollment confirmation will be sent to the patient immediately after enrollment is completed, but there currently is not an option to customize this content or to automatically send additional material. You can use the ‘Letter’ functionality in the patient’s chart to send a template letter to the patient at any time.

###

#### **Will a patient get a payment request even if they paid cash/check already?**

Yes, a payment request will be sent out even if the patient has prepaid their balance using a cash or check.

###

## **Related Articles**

- [Membership Management Introduction](Introduction-to-Membership-Management-with-Elation.md)
- [Membership Management- How to Manage Plans](Using-Elation-Membership-Management-to-Create-Membership-Plans-and-Manage-Enrollments.md)
- [Membership Management- How to Enroll Patients in Plans](Membership-Management-How-to-Enroll-Patients-in-Plans.md)
- [Membership Management - Patient Self-Enrollment](https://help.elationemr.com/s/article/Membership-Management-Patient-Self-Enrollment)
- [Membership Management- How Patients Receive Communications](Membership-Management-How-Patients-Receive-Communications.md)
- [Membership Management- How To Manage Payments](Membership-Management-How-To-Receive-Payments.md)
- [Patient Payments Guide- Securely collect payments digitally from patients](using-elation-to-securely-collect-patient-payments.md)