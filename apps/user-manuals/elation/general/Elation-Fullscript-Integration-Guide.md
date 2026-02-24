# Elation-Fullscript Integration Guide - Using Fullscript to manage supplement dispensing

Source: https://help.elationhealth.com/s/article/Elation-Fullscript-Integration-Guide

---

# **Contents**

- [Overview](#overview)
 - [What is Fullscript?](#Fullscript_overview)
 - [What is the Elation-Fullscript Integration?](#integration_overview)
 - [What are the benefits of the Elation-Fullscript Integration?](#integration_benefits)
 - [What information is synchronized?](#sync_details)
    - [Overall](#overall_sync)
    - [Patient Charts](#patient_sync)
    - [Medications](#medications_sync)
- [Set-up](#set_up)
 - [1. Obtaining a Fullscript account](#obtain_Fullscript_account)
    - [Multi-provider practices](#multiprovider_practices)
 - [2. Authorizing the Elation-Fullscript integration](#authorize_integration)
 - [3. Connecting your Elation account to Fullscript & signing a Business Associate Agreement (BAA) for the integration](#connect_to_integration)
- [Workflow Instructions](#workflow_instructions)
 - [Pushing supplement plan information from Fullscript to Elation](#sync_supplements)
- [Frequently Asked Questions](#FAQ)
 - [Set Up](#faq_set_up)
 - [Account Management](#faq_account_management)
 - [Workflows](#faq_workflows)

# **Overview**

## **What is Fullscript?**

Fullscript is a supplement dispensing platform that empowers practitioners to dispense personalized treatment plans and high-quality supplements directly to patients.

## **What is the Elation-Fullscript Integration?**

The Elation-Fullscript Integration enables you to create treatment plans in Fullscript and store data on dispensed supplements within Elation.

## **What are the benefits of the Elation-Fullscript Integration?**

The Elation-Fullscript Integration demonstrates Elation’s commitment to supporting holistic patient care while empowering practitioners to deliver personalized treatment plans. You can see all of a patient’s medications and supplements in their Medication History in Elation.

## **What information is synchronized?**

### **Overall**

| **Data** | **Sync Direction** |
| --- | --- |
| Patient Chart Creation | Elation → Fullscript |
| Patient Demographics | Elation → Fullscript |
| Medications (Supplements) | Fullscript → Elation |

### **Patient Charts**

The synchronization of patient demographics information is uni-direction from Elation to Fullscript. Only charts created in Elation will be synchronized with Fullscript.

| **Elation Field Name** | **Fullscript Field Name** |
| --- | --- |
| Legal First Name | First name |
| Legal last name | Last name |
| Date of birth | Date of birth |
| Email | Email |
| Provider Assigned in Practice | Practitioner |

### **Medications**

The synchronization of medications is uni-directional from Fullscript to Elation. Supplement plans will push to Elation as a Documented Medication.

| **Fullscript Field Name** | **Elation Field Name** |
| --- | --- |
| Ingredient | Med |
| Dosage | Dosage |
| Plan Date | Documented date |
| Practitioner | Documented by |

# **Set-up**

## **1. Obtaining a Fullscript account**

To use the Elation-Fullscript integration each Provider must first have a Fullscript account and sign a consent with Fullscript.

- To register for a Fullscript account [click here](https://us.fullscript.com/practitioner-signup/elation-health).
- If you already have a Fullscript account move on to the next step.

### **Multi-provider practices**

To use the Elation-Fullscript integration each Provider must first have a Fullscript account and sign a consent with Fullscript.

- If you own a Fullscript account and you want other providers in your practice to work under your account:
 1. Add the other Providers as sub-practioners under your Fullscript store.
 2. [Connect your Fullscript account to Elation](#connect_to_integration).
 3. [Sign the BAA](#connect_to_integration) as the Fullscript account owner.
- If each Provider in your practice has their own Fullscript account, each Provider must:
 1. [Connect your Fullscript account to Elation](#connect_to_integration).
 2. [Sign the BAA](#connect_to_integration) in their Fullscript account.

## **2. Authorizing the Elation-Fullscript integration**

1. Sign in to your Fullscript account.
2. Click on your name at the bottom left corner of your account to open the practitioner menu & then click **Integrations**.
3. Select **Elation**.
4. Click **Get Started Now**.
5. Sign your **Authorization and Consent (A&C) form** and click **Send**.

After the **Authorization and Consent (A&C) form** is received by Fullscript, Fullscript will acknowledge receipt of the form, provide you with a copy, and inform Elation to authorize the application on your Elation account. Please allow 3-5 business days to process your request. Fullscript will send you an email once Elation has informed us the interface has been authorized.

## **3. Connecting your Elation account to Fullscript & signing a Business Associate Agreement (BAA) for the integration**

After the integration is turned on, you must connect your Elation account to Fullscript. Afterwards, you must sign a BAA before using the integration. To do this:

1. Navigate to a patient’s chart in Elation.
2. Click **Fullscript** in the upper-left corner of the patient’s Clinical Profile.
3. Log in with your existing Fullscript credentials.
4. Select the Elation Provider Level User account you want connected to your Fullscript account.

ℹ️   **CAUTION** Once you select the Elation Provider Level User account you want connected to your Fullscript account, it cannot be changed.

1. If there is no Business Associate Agreement (BAA) on file for your account, you will be asked to sign a BAA document. Click **Start Signing** to begin.
2. After signing the BAA you can begin using the Elation-Fullscript integration.

# **Workflow Instructions**

## **Pushing supplement plan information from Fullscript to Elation**

1. Navigate to a patient’s chart in Elation.
2. Click **Fullscript** in the upper-left corner of the patient’s Clinical Profile.
3. Log in with your existing Fullscript credentials.
4. If Fullscript is able to find the patient’s Fullscript profile based on the email address in their Elation chart, then you will see that patient’s profile open in Fullscript.
   - If Fullscript is unable to find a matching patient:
     - Verify the patient’s email matches between Elation and Fullscript and then click **Fullscript** in the upper-left corner of the patient’s Elation Clinical Profile again.
     - If the patient does not have a Fullscript profile yet, click **Create patient** in Fullscript.
5. [Create a plan](https://support.fullscript.com/articles/the-plan-building-tool/) for the patient.
6. When you are ready, click **Send to patient** to send the plan to the patient.
7. Once you return the patient chart in Elation, any recommended supplements that were in the plan will be listed under the **Chronological Record** and **Permanent OTC Meds**.

# **Frequently Asked Questions**

## **Set Up**

#### **Is there a cost to use the Elation-Fullscript integration?**

No, Elation’s integration with Fullscript is available to all Elation members at no additional cost, and a Fullscript account is free.

#### **Is there a cost to use Fullscript as an Elation member?**

No, your Fullscript account is free if you are using the Elation-Fullscript integration.

####

#### **What is the Elation Authorization & Consent (A&C) form and how do I submit it?**

The Authorization and Consent form is a requirement from Elation to enable a 3rd-party integration such as Fullscript. Simply review and complete it here, then wait for the Fullscript team to let you know that the integration is enabled. The Fullscript team will send an email confirming receipt and a follow-up email once approved and the integration is enabled on the Elation end.

Once enabled, the Fullscript app will be available under patient information in the patient chart in Elation. You’ll need to have a Fullscript account and execute a Business Associate Agreement (BAA) in order to use the integration, if you don’t already have one on file under your account.

#### **Why do I need a Business Associate Agreement (BAA) with Fullscript to enable the Elation-Fullscript integration?**

All Elation marketplace partners are required to execute BAA with accounts wanting to access their integrations. We have a standard BAA that you’ll sign when redirected to Fullscript via the Elation integration for the first time.

#### **I’m a practitioner who shares an Elation account with other providers but we don’t all operate under the same Fullscript store. Can we still utilize this integration?**

Yes! This integration allows one Elation account to be connect with multiple Fullscript stores. Please note the account owner of each Fullscript account must initiate the integration process within their account. If you’re an account owner, you can begin this process by clicking here.

## **Account Management**

#### **Can I change the Elation practitioner that I assigned to my Fullscript account when I first signed in?**

You cannot change the Elation practitioner account that was initially selected. Please contact [elationintegration@fullscript.com](mailto:elationintegration@fullscript.com) for additional assistance.

#### **I’m trying to sign in to Fullscript after clicking the Fullscript button from Elation, but it says “Account not found”. Why?**

This could mean one of two things:

- You’re signed in to Fullscript with a different account than the account you’re trying to access through the integration. Please go to Fullscript and make sure you are signed in to the correct account.
- You’re trying to log in with an account that’s not registered under this integration. Please make sure you are logging in with the correct account.

## **Workflows**

#### **Can I sync plans created prior to the Elation-Fullscript integration being active?**

Plans created before the integration will not automatically be synced to Elation. However, after the integration is enabled, you can go into Fullscript and edit a historic plan, and the products will sync back to Elation as a new plan.

ℹ️   **CAUTION** The medications will display as newly documented medication in Elation and Fullscript will send an email to your patient to notify them that their plan has been updated.

#### **Can I edit a plan that’s already been sent to the patient?**

No, you can’t. A brand new plan will be written.

#### **If I delete or cancel a plan in Fullscript, will that update the medications in Elation?**

Deleting or canceling a plan in Fullscript will not delete or cancel the medication in Elation and vice versa. You must manually update the information in both systems separately.

#### **I’m trying to write a plan for a patient that I know is in Fullscript, but it says “No email found”. Why?**

Fullscript treats the patient email as the unique identifier, therefore an email needs to be added to Elation to be able to match it to a patient in Fullscript. Please add an email to the patient’s Elation demographics and then proceed with writing a plan.

#### **Can I sync lab orders from Fullscript to Elation?**

No. Although labs can be added to plans, at this time, only supplements and personal care items will be synced back to Elation.

# **Related Articles**

- [Fullscript Resource](https://support.fullscript.com/articles/elation-integration/)