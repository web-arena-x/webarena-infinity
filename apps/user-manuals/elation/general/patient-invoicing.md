# Billing Guide - Patient Invoicing - Generating invoices to patients for services rendered

Source: https://help.elationhealth.com/s/article/patient-invoicing

---

# Contents

- [Overview](#overview)
 - [What is Patient Invoicing?](#WhatIsPatientInvoicing)
 - [What do the different invoices look like?](#InvoiceViews)
- [Setup](#setup)
 - [Turning on Patient Invoicing](#TurnOn)
 - [Assigning charges to Popular CPT (procedure) codes](#AssignCharge)
- [Workflow Instructions](#workflows)
 - [Entering charges in a visit note](#VisitNote)
 - [Generating an invoice](#GenerateInvoice)
 - [Recording payment in invoices](#record_payment)
 - [Collecting payments directly from your invoices](#CollectPayment)

# Overview

## What is Patient Invoicing?

Patient invoicing is a feature that allows you to print invoices for patients to collect payment for services rendered for the patient responsibility portions of claims or any services that are not billed to insurance companies. If patients pay you directly but have insurance, you can also share the invoice with patients to send to their insurance companies for reimbursement.

ℹ️   **IMPORTANT NOTE** Patient invoicing is independent of Elation's Patient Payment feature. Generating and sending invoices through Patient Invoicing does not incur processing fees. Elation's percentage-based fee applies only when patients pay electronically via Patient Payments.

Learn more about the [Patient Payments feature and how to securely collect payments digitally from patients here](https://help.elationemr.com/s/article/using-elation-to-securely-collect-patient-payments).

## What do the different invoices look like?

### Simple Invoice

Contains Procedures, descriptions, charges, and the total balance and no diagnosis codes. Use the Simple Invoice when your patient is not submitting information to insurance and only needs a concise summary of their bill.

### **Claims Invoice (detailed information for Insurance claims)**

Contains procedures, descriptions, diagnosis codes, charges, total balance, and all of the patient and provider identifying information necessary for insurance claims. Provide the detailed invoice to your patient when they need to submit a receipt to insurance for reimbursement.

# Setup

## Turning on Patient Invoicing

Patient Invoicing is a practice-wide setting that can be turned on or off inside **Billing Settings**. Turn it on and new functions will become available for all providers and staff in your practice.

To enable patient invoicing, make sure the toggle to **Turn on patient invoicing** is set to **Yes**:

## Assigning charges to Popular CPT (procedure) codes

Once you turn patient invoicing on, you can add default charges to each CPT (procedure) code in your *Popular CPT Code* list in Billing settings. This is useful for any procedure or service commonly rendered by your practice.

Simply click **Edit** and enter the charge amount. When you add a CPT code with a default charge to your bill, the **Charge** field will automatically fill in the default charge value you entered. Charges will then print on invoices when you generate an invoice for a patient.

**USER TIP**

You can create your own custom code to use as a Popular CPT Code to charge patients for services that do not have standard CPT Codes. Here are some common use cases:

- You can create a code called *FORMS* and associate a charge of $10 to it if you charge patients $10 for completing medical paperwork.
- You can create a code called *RCOPY* and associate a charge of $25 to it if you charge patients $25 for a copy of their medical records.
- You can create a code called *VMB12* and associate a charge of $35 to it if you charge patients $35 for Vitamin B12 injections.

ℹ️   **IMPORTANT NOTE** For customers using a Practice Management System (PMS) integration with Elation, the **Amt ($)**, **Qty** and **Subtotal ($)** fields do not sync with any PMS. Best practice is to store claim charges in your Fee Schedule in your PMS.

# **Workflow Instructions**

## Entering charges in a visit note

| | |
| --- | --- |
| 1 | Go to the **Billing Information** section of the visit note. |
| 2 | For any billing line item, enter a dollar amount in the **Amt ($)** field, a quantity in the **Qty**, and your line item **Subtotal ($)** will be automatically calculated. |

**USER TIPS**

- If you enter a charge amount but leave the **Qty** field blank, Elation will automatically assume a quantity of "1" for the total.
- Use the minus (-) sign to enter a negative charge value (for discounts).
- When you add a CPT code with a default charge to your bill, the **Amt ($)** field in your bill will be automatically filled in with your default charge, saving you time. However, you will always be able to alter the charge amount directly from the bill.
- If you added or edited any default charges from the [Billing Settings](https://help.elationemr.com/s/article/billing-settings---service-locations--procedure-codes), remember to refresh your patient charts that are open for your new changes to appear.

## Generating an invoice

There are 4 ways to print [an invoices](#InvoiceViews):

| | |
| --- | --- |
| 1 | From the **Billing Information** window of the Visit Note, click **Save & Print...** to print an invoice. |
| 2 | From the **Billing Information** section at the bottom of your visit note, click **Print Invoice** and select an option to print. |
| 3 | After your visit note is signed off, find the visit note in the chart and click **Actions** → **Print** and select one of our invoices. |
| 4 | From [Billing Home](https://help.elationemr.com/s/article/Billing-Home), click on the **Actions Menu** and click **Open Bill.** Then use one of the **Save & Print...** options to print an invoice. |

## Recording payment in invoices

The **Patient Payment ($)** field in the **Billing Information** window will allow you to record information about payments that were already collected from the patient.

- E.g. The patient's charge for today's visit is $100. The patient paid your office $25 in cash prior to their visit. You can enter '25' in the **Patient Payment ($)** field. When an invoice is generated for the patient, the $25 payment will be listed so that they patient knows they only owe $75.

**USER TIP** The **Patient Payment ($)** field can be used to indicate to insurance companies that the patient paid you the total charge amount so that insurance companies know to reimburse the patient directly.

## Collecting payments directly from your invoices

Using Elation's patient payments solution, your practice's personalized Payment Site will automatically be included on your patient invoices, providing your patients with an easy way to submit payments to your practice in a secure, electronic manner.

Patients can simply point their phone camera at the QR code (see below) and they will be automatically directed to your practice's Payment Site to submit payment. Alternatively, they can visit your Payment Site by typing in your Payment Site URL into their browser. Logging into Patient Passport is not required. Learn more about the [Patient Payments feature here](https://help.elationemr.com/s/article/using-elation-to-securely-collect-patient-payments).

**Next Step

Start collecting payments from patients today!**

**CPT c***opyright 1995 - 2023 American Medical Association. All rights reserved.*

# **Related Articles**

- [Billing Guide- Navigating Billing Settings](billing-settings---service-locations--procedure-codes.md)
- [Billing Guide- Frequently Asked Questions](Billing-Guide-Frequently-Asked-Questions.md)
- [Patient Payments Guide- Securely collect payments digitally from patients](using-elation-to-securely-collect-patient-payments.md)
- [Billing Home Guide- A dashboard for managing your bills](Billing-Home.md)
- [Patient Demographics Guide- Managing patient insurance](Managing-Insurance.md)