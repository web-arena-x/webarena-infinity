# User Accounts Guide - Provider Level account vs. Staff Level account

Source: https://help.elationhealth.com/s/article/User-Accounts-Guide-Provider-vs-staff-level-account-privileges

---

# Contents

- [Overview](#overview)
 - [What are the two types of Elation accounts?](#account_types)
 - [Provider Level Accounts vs. Staff Level Account Overview](#provider_vs_staff)
 - [Standard Provider Level Account privileges](#provider)
 - [Staff Level Account privileges](#staff)
    - [Using Staff Level accounts for scribes](#staff_scribes)
 - [Licenses and seats (e.g. "scribe seats")](#licenses)
    - ["Scribe" the person vs. "scribe license" the product](#scribe_person_vs_license)
    - [Note Assist "scribe" subscriptions and reassignment](#scribe_license_reassignment)
- [Setup](#setup)
- [Sample Accounts View](#sample)
- [Frequently Asked Questions (FAQ)](#faq)

# Overview

## What are the two types of Elation accounts?

Elation EHR offers two types of accounts for users – Provider Level and Staff Level.

- Provider Level accounts
 - Usually used by physicians, non‑physician practitioners, or other medical providers who:
    - Have patients and visit notes assigned to them
    - Sign clinical documentation (visit notes, orders, referrals, prescriptions)
    - Are listed as the rendering and/or billing clinician on claims
 - **Paid user licenses** ("provider seats") and come with a fee as stated on your contract with Elation. Each provider seat is intended for a single named clinician.

- Staff Level accounts
 - Usually used for administrative or clinical staff who support clinicians with scheduling, documentation, and billing. Staff Level accounts are **free of charge** and are ideal for roles such as:
    - Front office and billing staff
    - Medical assistants and clinical support staff
    - Scribes and other documentation support roles
 - Do not replace a Provider Level account and do not sign visit notes or bill as rendering providers.

## Provider Level Accounts vs. Staff Level Account Overview

| Privileges vs. Account Type | Regular Provider | Non-Prescribing Provider | Limited Use Provider | On Call Provider | Staff |
| --- | --- | --- | --- | --- | --- |
| **Specific Calendar Schedule** | ✓ | ✓ | ✓ | ✓ | When Staff Level Users select a "Default Provider" in their Account Details settings, that provider calendar will be the default calendar shown. |
| **Telehealth Zoom Visits** | ✓ | ✓ | ✓ | **Not** able to activate the telehealth Zoom feature, but **can start virtual visits** from a Regular and Non-Prescribing Provider calendar. | **Can start virtual visits** from a Regular and Non-Prescribing Provider calendar. |
| **Document in a Visit Note** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Sign a Visit Note** | ✓ | ✓ | ✓ | ✓ | Can document in a visit note, but **cannot** complete the note by Signing Off. |
| **Enter/Edit Billing Information (Pre-Sign)** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Sign Bills** | ✓ | ✓ | ✓ | ✓ | **Cannot** sign bills on behalf of Providers. |
| **Enter/Edit Billing Information (Post-Sign)** | ✓ | ✓ | ✓ | ✓ | Must be a Billing Delegate of a Provider. |
| **Draft Prescriptions** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **ePrescribing Regular Substances** | ✓ | Must be a Prescription Delegate of a Regular Provider. | ✓ | ✓ | **Not** able to ePrescribe any substances. Can draft scripts and send on behalf of the Provider if the staff is a Prescription Delegate . |
| **ePrescribing Controlled Substances (EPCS)** | ✓ | **Not** able to ePrescribe any controlled substances. | ✓ | **Not** able to ePrescribe any controlled substances. | **Not** able to ePrescribe any controlled substances. |
| **Draft Electronic Lab Orders** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Sign and Send Electronic Lab Orders** | ✓ | ✓ | ✓ | ✓ | Must be an Order Delegate of a Provider. |
| **Draft Ancillary Orders (non-lab)** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Sign and Send Ancillary Orders (non-lab)** | ✓ | ✓ | ✓ | ✓ | Must be an Order Delegate of a Provider. |
| **Draft Referrals** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Sign and Send Referrals** | ✓ | ✓ | ✓ | ✓ | Must be a Referral Delegate of a Provider. |

## Standard Provider Level Account privileges

Provider Level accounts are usually used by physicians, non-physician practitioners or other medical providers. For these reasons, Provider Level accounts offer functionalities that Staff Level accounts do not. Here are some common examples:

- Providers can have patient charts assigned to them.
- Providers have a Calendar in Elation.
- Providers can sign all important clinical documentation such as:
 - visit notes
 - test orders
 - prescriptions
 - referrals
 - electronic test reports
- Providers can amend their own visit notes after the visit note is signed.
- Providers can edit the billing information of their own visit notes after a visit note is signed.
- Providers can sign office messages that Provider Level Users are part of.
- Administrative reports are catered towards Provider Level User data.
- Providers can append their signature to Reports when using the annotate feature.

## Staff Level Account privileges

Staff Level accounts are usually for administrative or clinical staff, including:

- Front office staff
- Billing staff
- Medical assistants and nurses
- Scribes and other documentation support roles

Staff Level users support clinicians with documentation and operations, but do **not** have the full set of Provider Level privileges above. For example, they do not sign visit notes as the billing/rendering clinician, and their credentials are not used as the treating provider on claims.

There is one important exception: Staff Level users can take certain clinical and billing actions **on behalf of a provider** when that provider explicitly designates them as an [authorized staff delegate](https://help.elationemr.com/s/article/staff-permissions--staff-delegates). In that case, a Staff Level user may:

- sign test orders on a provider's behalf
- sign prescriptions and/or send prescription medications to pharmacies (controlled substance medications cannot be e-Prescribed by staff delegates) on a provider's behalf
- sign referrals on a provider's behalf
- edit billing information of the provider's signed visit notes

This delegation pattern is how many practices configure **scribes** in Elation: as Staff Level users with the appropriate delegate relationships to the Provider Level clinicians they support.

### Using Staff Level accounts for scribes

In Elation, a "scribe" is not a separate account type. Instead, scribes are typically configured as Staff Level users who help one or more providers with visit documentation and billing workflows.

A Staff Level "scribe" can:

- Document in visit notes on behalf of a provider (for example, capturing the clinical story during or after the encounter)
- Enter or edit billing information before a visit note is signed
- Edit billing information for a provider's signed visit notes when designated as that provider's Billing Delegate

They do **not**:

- Replace a Provider Level account for the clinician
- Sign visit notes as the rendering provider
- Prescribe medications under their own credentials

For practices using Note Assist, Elation's AI‑powered ambient scribing tool, staff and scribes can also help review and edit the AI‑generated content before the provider signs the note.

## Licenses and seats (e.g. "scribe seats")

Elation's user accounts map directly to the licenses (or "seats") in your contract:

- Provider Level accounts are **limited** **seats** (based on your contract). Each seat is intended for one named clinician whose credentials are used to sign notes, orders, referrals, and prescriptions, and to appear as the rendering/billing provider on claims.
- Staff Level accounts are **unlimited**, **free seats** for administrative and clinical support staff, including front office, billing staff, medical assistants, and human scribes.

### "Scribe" the person vs. "scribe license" the product

It's important to distinguish between:

- A **scribe as a person** – a staff member who helps document visits and support billing workflows. In Elation, this person should always have their own Staff Level account and, when appropriate, be configured as an Authorized Staff Delegate / Billing Delegate for the providers they support.
- A **"scribe license" or Note Assist subscription** – a **product subscription** tied to a specific Provider Level account. This is distinct from the Staff Level user accounts that human scribes use.

Human scribes **do not share** a provider's login and do not "own" a Note Assist license themselves. Instead:

- The Provider Level user holds the Note Assist subscription.
- Any staff or scribes who help with documentation still log in as **themselves** on Staff Level accounts, following the normal delegation model.
- The provider remains the one who reviews and signs the visit note.

### Note Assist "scribe license" and reassignment

[Note Assist](https://help.elationemr.com/s/article/Note-Assist-Guide) is Elation's AI‑powered ambient scribing and note‑writing solution. Practices may purchase upgraded Note Assist subscriptions for specific providers.

Key points:

- A Note Assist subscription is **attached to a specific Provider Level account**, not to a Staff Level "scribe" account.
- When your practice wants to **reassign** a Note Assist subscription from one provider to another, Support or your Customer Success Manager must update the subscription assignment on your behalf.

#### How to reassign a Note Assist subscription between providers

If you need to move a Note Assist subscription from one provider to another, please **reach out to Elation Support or your Customer Success Manager** with all of the following information below. Support/CSM will make the changes as requested and then notify you once this is done.

- Name of the provider to turn Note Assist OFF
- Name of the provider to turn Note Assist ON
- The date you want the switch to take effect

This process ensures the Note Assist subscription follows the correct Provider Level user, while Staff Level scribes continue to work from their own accounts using the standard delegation model.

# **Setup**

[Click here for instructions on how to invite members of your practice to create an Elation account based on the account type you assign](https://help.elationemr.com/s/article/managing-user-accounts).

# Sample Accounts View

Here are examples of what the Provider versus Staff account privileges look like:

# Frequently Asked Questions

#### I have a Supervising Physician. Do they need their own Elation account?

Yes, if you have a Supervising Physician and you need to send their credentials along with any electronic prescriptions you create, then your Supervising Physician must have their own [authenticated](https://help.elationemr.com/s/article/how-to-complete-account-authentication) Provider Level User account with Elation. This is required even if your Supervising Physician does not need direct access to your patient data.

Once your Supervising Physician has activated and authenticated their Elation account, take the following actions to automatically send their credentials along with yours when e-Prescribing:

| | |
| --- | --- |
| 1 | Go to your Elation Settings. |
| 2 | Click "Edit Profile" under Account Details. |
| 3 | Select your Supervising Physician's name in the Supervising Provider field under the Credentials section. |

For more context on provider vs. staff seats and how licenses work in Elation, see the sections **"What are the two types of Elation accounts?"** and **"Licenses, seats, and 'scribe seats'"** above.

#### Which account type should I use for a scribe?

Use a Staff Level account for scribes.

Staff Level accounts are designed for administrative and clinical support roles, including scribes. They can:

- Document in visit notes
- Enter billing information before sign‑off
- Edit billing information for a provider's signed visit notes when configured as a Billing Delegate

The supervising clinician should keep a Provider Level account and remain the one who signs visit notes, prescriptions, orders, and referrals as the rendering/billing provider.

#### **How do I configure a Staff Level user as a scribe for a specific provider?**

To configure a Staff Level user as a scribe for a specific provider:

| | |
| --- | --- |
| 1 | Create a Staff Level account for the individual (do not share or reuse the provider's login). |
| 2 | Have an Admin‑level user review and manage the Staff Level user from Settings → Manage Accounts, as described in the Administrative privileges guide. |
| 3 | Have the Provider Level user add that Staff Level user as an Authorized Staff Delegate (and Billing Delegate, if desired) under their User Settings, so the scribe can sign specific items and edit billing information on the provider's behalf. |

#### Can my scribe use my provider login or my MFA device?

No. Shared or generic user accounts are **not permitted** in Elation.

Each individual must:

- Log in with their **own unique Elation user account**, and
- Use their **own multi‑factor authentication (MFA) factor(s)** when MFA is enabled.

Sharing a Provider Level login or sharing an MFA device with a scribe or staff member violates Elation's security policies and makes it harder to track who performed which clinical actions in the chart.

To give your scribe access:

| | |
| --- | --- |
| 1 | Create a Staff Level account for them. |
| 2 | Configure them as an Authorized Staff Delegate (and Billing Delegate, if desired) under your Provider User Settings, so they can take appropriate actions on your behalf while still logging in as themselves. |

# Related Articles

- [User Accounts Guide- Managing Elation accounts for providers and staff](https://help.elationemr.com/s/article/managing-user-accounts)
- [User Accounts Guide- Administrative privileges](https://help.elationemr.com/s/article/administrative-privileges)