# EPCS Guide - Managing EPCS Access Controls

Source: https://help.elationhealth.com/s/article/how-to-set-up-epcs-access-controls

---

# Contents

- [Overview](#overview)
 - [What are EPCS Access Controls?](#what_is)
 - [Why are Access Controls important?](#why_important)
 - [Prerequisites](#prereq)
- [Workflow Instructions](#workflow)
 - [Setting up Access Control permissions for the first time as the first provider](#first_time)
    - [Multi-Provider Practice](#multi_provider_practice)
    - [Single Provider Practice](#single_provider_practice)
 - [Setting up Access Control permissions for additional providers](#additional_providers)
 - [Adjusting Access Control permissions](#adjust_permission)
 - [EPCS and account deactivation](#epcs_deactivation)

# Overview

## What are EPCS Access Controls?

EPCS Access Controls are DEA-required security settings that determine which providers in your practice can electronically prescribe controlled substances. These controls ensure that only authorized, properly credentialed providers can e-prescribe Schedule II-V medications.

## Why are Access Controls important?

The DEA requires a two-person verification system for enabling EPCS within any EHR system. This "checks and balances" approach ensures:

- Only providers legally authorized to prescribe controlled substances can do so.
- A second authorized user verifies each provider's EPCS permissions.
- Your practice maintains proper compliance with DEA regulations.

## Prerequisites

Review the [EPCS Sign Up Process Guide](https://help.elationemr.com/s/article/how-to-complete-the-epcs-sign-up-process) first before proceeding with this article. You must complete the initial EPCS sign-up steps before you can configure Access Control Permissions.

ℹ️   **IMPORTANT NOTE** The DEA requires that two users—the Provider Level User needing to prescribe controlled substances, and a second Provider Level User or an Admin Level Staff User—are present to enable EPCS within Elation. Multi-provider practices and single provider practices have different workflows, detailed below.

# Workflow Instructions

## Setting up Access Control permissions for the first time as the first provider

ℹ️   **IMPORTANT NOTE** The DEA requires that two users, a Provider Level User and a second Provider Level User or an Admin Level Staff User, are present in order to enable EPCS within Elation. This is a checks and balances system to ensure that any provider who is given EPCS permissions can legally prescribe controlled substance medications.

The steps in this section apply to you (the provider) if your entire practice is new to Elation and this is the first time a provider in the practice is signing up for EPCS. Each provider should **always complete steps 1 to 3 in the**[EPCS Sign Up Process Guide](how-to-complete-the-epcs-sign-up-process.md) first before setting up their Access Control Permissions.

### Multi-Provider Practice

ℹ️   **IMPORTANT NOTE** Please note the user definitions for the workflow detailed in this section.

- First user = Provider signing up for EPCS
- Second user = Provider Level User who is assisting with sign up
 - Must be an Admin Level User at the practice.
 - Will become an Access Control Manager by assisting with sign up.

| | |
| --- | --- |
| 1 | Assign "Admin" level privileges to the second user (Provider Level User assisting with sign up) in your practice if they do not already have this permission.   1. Go to Manage Accounts and then click **Make Admin** next to the second user's name. |
| 2 | Ask the second user to login to their Elation account. |
| 3 | Ask the second user to click on their email at the top of their Elation account & click Settings. |
| 4 | Ask the second user to click into the **ePrescribing Controlled Substance (EPCS)** settings section and click on **Access Controls**. |
| 5 | The second user will then be brought to a page called "EPCS Permissions- Logical Access Control Setup". |
| 6 | Under **Grant Permissions**, ask the second user to check off all of the following boxes next to your name:   - Access Control Manager - Authorization Verifier - Can Approve EPCS - Can Sign & Send |
| 7 | Under **Grant Permissions**, ask the second user to check off the following boxes next to their name:   - Access Control Manager - Authorization Verifier |
| 8 | **(Optional)** If the second user plans on signing up for EPCS at a later time, have them check off the following next to their own name as well:   - Can Approve EPCS - Can Sign & Send |
| 9 | Under **Signoff & Save Permissions** ask the second user to take the following 2 actions:   1. Select your name in the dropdown for the **First User (Prescriber w/ Token)** field. 2. Verify the second user's name is already selected in the **Second User (Prescriber or Admin)** field. |
| 10 | Have the second user click Save. A new box will appear prompting the second user to enter their email address. |
| 11 | Have the second user enter their email address & click Save. A box will pop up with a message that says "Second User approval code has been sent to their email...." |
| 12 | Have the second user check their email inbox for an email with the subject line "EPCS Permission Request" from "[noreply@mdnotification.net](mailto:noreply@mdnotification.net)". The body of the email will contain a 7-digit approval code. |
| 13 | Have the second user enter the 7-digit code in the **Approval Code** box that now appears under the **Second User (Prescriber or Admin)** field. |
| 14 | Have the second user click Save to save the approval code. |
| 15 | A box will pop up asking you (First User/the provider completing EPCS Sign Up) to enter your EPCS Token Password and Security Code. Enter this information and click **Sign and Authorize** to complete the final step of this process. |

Congratulations on completing EPCS Sign Up! You can now close the MDToolbox tab in your web browser.

[Click here to view our how to e-Prescribe controlled substance guide](http://help.elationemr.com/customer/portal/articles/2746249-how-to-e-prescribe-controlled-substances).

### Single Provider Practice

| | |
| --- | --- |
| 1 | If you have a staff member with a Staff Level Elation account, assign them "Admin" level privileges if they do not already have this permission   1. Go to Manage Accounts and then click **Make Admin** next to the second user's name. |
| 2 | If you do not have any staff, ask a trusted friend or family member to assist you    1. Invite them to Elation by going to **Manage Accounts** -> **+ Invite Staff**. 2. Enter their name and email and then click **Invite**. 3. Ask them to find the invitation in their email inbox and click **Click here to complete your Registration**.    1. The invitation email will come from "[support@elationemr.com](mailto:support@elationemr.com)" and will have the subject line "Your Elation Account is Ready!". 4. Supply them with your practice's fax number to complete registration. |
| 3 | Ask the Staff Level User to click on their email at to top of their account and click **Settings**. |
| 4 | Ask the Staff Level User to click into the **ePrescribing Controlled Substance (EPCS)** settings section and click on **Access Controls**. |
| 5 | The Staff Level User will then be brought to a page called "EPCS Permissions- Logical Access Control Setup". |
| 6 | Under **Grant Permissions**, ask the Staff Level User to check off all of the following boxes next to your name:   - Access Control Manager - Authorization Verifier - Can Approve EPCS - Can Sign & Send |
| 7 | Under **Grant Permissions**, ask the Staff Level User to check off the following boxes next to their name:   - Access Control Manager - Authorization Verifier |
| 8 | Under **Signoff & Save Permissions** ask the Staff Level User to take the following 2 actions:   1. Select your name in the dropdown for the **First User (Prescriber w/ Token)** field. 2. Verify the Staff Level User's name is already selected in the **Second User (Prescriber or Admin)** field. |
| 9 | Have the Staff Level User click Save. A new box will appear prompting the second user to enter their email address. |
| 10 | Have the Staff Level User enter their email address & click Save. A box will pop up with a message that says "Second User approval code has been sent to their email...." |
| 11 | Have the Staff Level User check their email inbox for an email with the subject line "EPCS Permission Request" from "[noreply@mdnotification.net](mailto:noreply@mdnotification.net)". The body of the email will contain a 7-digit approval code. |
| 12 | Have the Staff Level User enter the 7-digit code in the **Approval Code** box that now appears under the **Second User (Prescriber or Admin)** field. |
| 13 | Have the Staff Level User click Save to save the approval code. |
| 14 | A box will pop up asking you (First User/the provider completing EPCS Sign Up) to enter your EPCS Token Password and Security Code. Enter this information and click **Sign and Authorize** to complete the final step of this process. |

Congratulations on completing EPCS Sign Up! You can now close the MDToolbox tab in your web browser.

[Click here to view our how to e-Prescribe controlled substance guide](http://help.elationemr.com/customer/portal/articles/2746249-how-to-e-prescribe-controlled-substances).

## Setting up Access Control permissions for additional providers

The steps in this section apply to you (the provider) if another Provider Lever User in the practice has already completed EPCS Sign Up. Each provider should **always complete steps 1 to 3 in the**[EPCS Sign Up Process Guide](how-to-complete-the-epcs-sign-up-process.md) first before setting up their Access Control Permissions.

There are three options available for necessary users present when setting up Access Controls when there are already two established Access Control Managers at a practice (one being a Provider Level User):

| | | |
| --- | --- | --- |
| **Option 1** | **Option 2** | **Option 3** |
| - One Provider Level User/established Access Control Manager - One Staff Level User/established Access Control Manager | - Two Provider Level Users/established Access Control Managers | - Provider Level User signing up for EPCS - Provider or Staff Level User/established Access Control Manager |
| \*Please utilize the steps detailed below. | \*Please utilize the steps detailed below. | \*Please utilize the [steps detailed for setting up a Provider Level User for the first time in a multi-provider practice](#multi) if only these users are present. |

| | |
| --- | --- |
| 1 | Ask any established Access Control Manager to login to their Elation account. |
| 2 | Ask the Access Control Manager to click on their email at the top of their Elation account & click **Settings**. |
| 3 | Ask the Access Control Manager to click into the **ePrescribing Controlled Substance (EPCS)** settings section and click on **Access Controls**. |
| 4 | The Access Control Manager will then be brought to a page called "EPCS Permissions- Logical Access Control Setup". |
| 5 | Under **Grant Permissions**, ask the Access Control Manager to check off the boxes next to your name (the Provider Level User requiring EPCS) for the all the fields that apply (**at a minimum, Provider Level Users must have 'Can Approve EPCS?' and ‘Can Sign & Send' checked off** in order to send electronic controlled substance medications via Elation):    - Access Control Manager - Authorization Verifier - Can Approve EPCS - Can Sign & Send |
| 6 | Under Signoff & Save Permissions:    - For the **First User (Prescriber w/ Token)** field, ask the Access Control Manager to select the name of the other Access Control Manager (must be a Provider Level User, usually already signed up for EPCS). - For the **Second User (Prescriber or Admin)** field, the original Access Control Manager's own name should already be filled in. |
| 7 | Have the Access Control Manager click **Save** and a prompt will appear asking the Access Control Manager to approve their own changes. Have the Access Control Manager click **OK** to continue. |
| 8 | A box will pop up for the First User (the other Access Control Manager/Provider Level User) to enter their EPCS Token Password and Security Code. Have the First User enter this information and click **Sign and Authorize** to complete the final step of this process. |

Congratulations on completing EPCS Sign Up! You and the Access Control Manager can now close the MDToolbox tab in your web browser.

[Click here to view our how to e-Prescribe controlled substance guide](http://help.elationemr.com/customer/portal/articles/2746249-how-to-e-prescribe-controlled-substances).

## Adjusting Access Control permissions

The steps in this section are outlined for anyone who needs their existing Access Control Permissions updated. Each person needs to have two established Access Control Managers available to assist with updating their permissions.

There are two options available for necessary users present for Access Controls adjustment:

| | |
| --- | --- |
| **Option 1** | **Option 2** |
| - One Provider Level User/established Access Control Manager - One Staff Level User/established Access Control Manager | Two Provider Level Users/established Access Control Managers |

| | |
| --- | --- |
| 1 | Ask any established Access Control Manager to login to their Elation account. |
| 2 | Ask the Access Control Manager to click on their email at the top of their Elation account & click **Settings**. |
| 3 | Ask the Access Control Manager to click into the **ePrescribing Controlled Substance (EPCS)** settings section and click on **Access Controls**. |
| 4 | The Access Control Manager will then be brought to a page called "EPCS Permissions- Logical Access Control Setup". |
| 5 | Under **Grant Permissions**, ask the Access Control Manager to adjust the boxes next to the name of the person requiring a permission change. (**If the user is a Provider Level User then, at a minimum, they must have 'Can Approve EPCS?' and ‘Can Sign & Send' checked off** in order to send electronic controlled substance medications via Elation):    - Access Control Manager - Authorization Verifier - Can Approve EPCS - Can Sign & Send |
| 6 | Under Signoff & Save Permissions:    - For the **First User (Prescriber w/ Token)** field, ask the Access Control Manager to select the name of the other Access Control Manager (must be a Provider Level User, usually already signed up for EPCS). - For the **Second User (Prescriber or Admin)** field, the original Access Control Manager's own name should already be filled in. |
| 7 | Have the Access Control Manager click **Save** and a prompt will appear asking the Access Control Manager to approve their own changes. Have the Access Control Manager click **OK** to continue. |
| 8 | A box will pop up for the First User (the other Access Control Manager/Provider Level User) to enter their EPCS Token Password and Security Code. Have the First User enter this information and click **Sign and Authorize** to complete the final step of this process. |

## EPCS and account deactivation

When a provider with EPCS permissions leaves your practice or their account is disabled, their EPCS access is **automatically revoked**. Before disabling a provider account:

| | |
| --- | --- |
| 1 | **Review pending controlled substance prescriptions** – Ensure any prescriptions requiring their signature are completed or reassigned. |
| 2 | **Update Access Control permissions** – If the departing provider is an Access Control Manager, assign those permissions to another eligible user before disabling the account as needed. Each practice needs at least 2 Access Control Managers. |
| 3 | **Plan for re-enablement** – If the provider's account is later re-enabled, their EPCS permissions must be **re-granted** by existing Access Control Managers. EPCS access is not automatically restored. |

ℹ️   **IMPORTANT NOTE** For a complete checklist of actions to take before disabling any user account (including Requiring Action queue, post-dated messages, and appointments), see [Best practices for disabling accounts](https://help.elationemr.com/s/article/User-Accounts-Guide-Best-practices-for-deactivating-accounts).

**Next Step**

Send a controlled substance prescription electronically using the Controlled Substance Form in your Patient's chart! Learn **[How to e-Prescribe Controlled Substances](https://elation.lightning.force.com/articles/Knowledge/how-to-e-prescribe-controlled-substances).**

# **Related Articles**

- [EPCS Guide - ePrescribing controlled substance medications & troubleshooting](how-to-e-prescribe-controlled-substances.md)
- [EPCS (Electronic Prescribing of Controlled Substances) Introduction](introduction-to-electronic-prescribing-of-controlled-substances-epcs.md)
- [EPCS Guide - Signing up for EPCS](how-to-complete-the-epcs-sign-up-process.md)
- [EPCS Guide - Updating your EPCS Token or password](how-to-update-your-epcs-token.md)
- [EPCS Guide - Frequently Asked Questions](epcs-faq-page.md)
- [How to Complete Identity Proofing with Elation](how-to-complete-identity-proofing.md)

##