# Data Sharing Guide - Sharing data outside Elation via CCDA, Carequality, Direct messaging, Connect and Patient Passport

Source: https://help.elationhealth.com/s/article/Sharing-data-outside-Elation

---

# Contents

- [Overview](#overview)
 - [What is external data sharing?](#description)
 - [Why is understanding external data sharing important?](#value)
 - [Quick comparison: external data channels](#comparison)
- [Workflow Instructions](#workflow-instructions)
 - [CCDA exports/imports](#ccda)
    - [What leaves Elation in CCDA exports](#CCDA_export)
    - [What you can import from inbound CCD/CCDA files](#CCDA_import)
    - ["View only" vs import for CCDA](#CCDA_view_or_import)
 - [Carequality (Outside Care)](#carequality)
    - [What Carequality is doing with your data](#Carequality_share)
    - [What you see when you query Carequality](#Carequality_query)
    - [Viewing vs importing Carequality documents into the chart](#Carequality_view_or_import)
 - [Direct messaging & Elation Connect](#direct)
    - [What's in an outbound Direct message](#Direct_message_send)
    - [What you see for inbound Direct messages](#Direct_message_receive)
    - [What Elation Connect recipients can see](#Connect_share)
 - [Elation Patient Passport (patient portal)](#passport)
    - [Default patient-visible data](#Passport_default)
    - [What is not automatically shared with patients](#Passport_not_share_automatically)
    - [Messaging and attachments from patients](#Patient_messages)
- [Where to verify "what was sent"](#verification)

# Overview

## What is external data sharing?

External data sharing refers to how patient data flows out of and into Elation across four main channels:

- C-CDA (CCDA) exports/imports
- Carequality (Outside Care)
- Direct messaging & Elation Connect (secure provider portal)
- Elation Patient Passport (patient portal)

## Why is understanding external data sharing important?

Clinicians and admins frequently ask two key questions:

- What exactly leaves my chart, and who can see it?
- When I "view" outside records vs import them, where do those records live in Elation?

Understanding these data flows helps you maintain patient privacy, ensure continuity of care, and properly manage incoming records.

## Quick comparison: external data channels

| Data channel | Primary audience | Direction | What they can see | View vs import in Elation | Who initiates? |
| --- | --- | --- | --- | --- | --- |
| **CCDA export/import** | Other EHRs, registries, HIEs, patients | Outbound & inbound | Standard clinical summary (problems, medications, allergies, encounters, labs, care plan, etc.), optionally scoped to a specific use case (referral, complete record, care plan only). | [Inbound CCD/CCDA files](https://help.elationemr.com/s/article/import-patient-information-from-another-ehr-c-cda-format) always create a **Patient Summary** report. Only demographics, allergies, problems, immunizations, and medications can be imported as structured data; all other sections remain view-only in the **Patient Summary** unless manually transcribed. | You initiate [CCDA exports](https://help.elationemr.com/s/article/Supported-Elation-CCDA-types) from the chart or **Patient List** report; outside organizations initiate inbound CCD/CCDA sends. |
| **[Carequality](https://help.elationemr.com/s/article/Carequality-Integration-Introduction) (Outside Care)** | Carequality-enabled clinicians, HIEs, and EHRs | Bi-directional (outbound and inbound) | Outbound: a CCDA summary for matched, consented patients. Inbound: CCDs plus other document types (e.g., PDFs, images) depending on the trading partner. | Inbound CCDs appear in the **Outside Care** viewer and can be filed and (optionally) imported into structured sections. Other document types are view-only in the viewer; to retain them you must download and upload them as Reports. | You initiate queries via the **Outside Care** button; external organizations initiate pulls of your CCDA data when they query Carequality and a match is found. |
| **Direct messaging & Elation Connect** | External clinicians, facilities, and organizations | Outbound and inbound for Direct messaging; mainly outbound for Connect | [Direct messages](https://help.elationemr.com/s/article/how-to-use-direct-messaging): the Letter/Referral body, attachments you choose, plus an automatically attached CCDA file for the patient when supported. Elation [Connect](https://help.elationemr.com/s/article/secure-Provider-Portal): a secure, read-only snapshot of the exact documents you attached—never a live copy of your chart. | Inbound Direct CCD/CCDA attachments become **Patient Summary** reports. For new auto-created charts, compatible sections can auto-populate; for existing charts, you choose what to import, exactly like other CCD/CCDA imports. | You initiate outbound messages via **Provider Letters** and **Referrals**; external systems initiate inbound Direct messages to your Direct address. Connect invitations are triggered when you address a Letter/Referral to a non-Elation contact with fax or email. |
| [**Patient Passport**](https://help.elationemr.com/s/article/elation-patient-passport-an-introduction) | Patients and patient-authorized delegates | Mainly outbound from Elation to patients | By default: Clinical Profile (except records marked confidential), visit summaries for signed visit notes, **Patient Letters**, and any attachments you choose to send (e.g., labs, imaging, handouts). | Patient-visible data is read-only from the patient's perspective and **does** **not** change your internal structured chart. You control additional sharing (e.g., lab reports, orders) by attaching records to **Patient Letters**. | You invite patients and send messages/records from within the chart or via [**Bulk Letters**](https://help.elationemr.com/s/article/introduction-to-bulk-letters); patients and delegates can message or reply if you allow messaging. |

# External data channels

## CCDA exports/imports

### What leaves Elation in CCDA exports

When you export a CCDA for a single patient or a cohort, Elation generates a structured clinical summary that can include (depending on the export type):

- Reason for referral
- Allergies, adverse reactions, alerts
- Medication history
- Problem list
- Encounters
- Immunizations
- Vital signs
- Social history
- History of procedures and implantable devices
- Relevant diagnostic tests and/or laboratory data (all structured values from signed lab results)
- Functional and mental status
- Assessments, plan of care, goals, and health concerns

You can control the scope by choosing:

- Complete Record (all available data, excluding confidential records)
- Customized Record (manually pick sections such as labs only, or medications & problems)
- Referral Record (referral-oriented subset)
- Progress Notes or Care Plan exports for more focused use cases

### What you can import from inbound CCD/CCDA files

When another EHR, registry, or HIE sends you a CCD/CCDA file (whether via Direct, Carequality, or manual upload):

- Elation converts the file into a **Patient Summary** report in the patient's chart.
- From that **Patient Summary**, you can import **only** the following sections as structured data into the Clinical Profile:
 - Demographics
 - Allergies
 - Problems
 - Immunizations
 - Medications

Other sections—such as lab results, imaging reports, visit notes, and discharge summaries—remain part of the read-only **Patient Summary**. You can reference them any time but they **are** **not** merged into Elation's structured fields automatically.

### "View only" vs import for CCDA

- View only: If you simply open and sign off a **Patient Summary** without importing any sections, the CCD/CCDA stays as an attachment in the chart. It **does** **not** alter the Clinical Profile or other structured areas of the chart.
- View & import: If you choose **Import All** or **Import & Reconcile** for specific sections, Elation pulls demographics, allergies, problems, immunizations, and medications into the appropriate structured sections. All other sections remain view-only inside the **Patient Summary**.

This is true whether the CCD/CCDA arrived as a bulk migration file, a Direct message attachment, or through Carequality.

## Carequality (Outside Care)

### What Carequality is doing with your data

When your practice enables **Patient Data Sharing with Outside Care** and records patient consent, Elation participates in the national Carequality framework:

- Other Carequality-enabled organizations can query for your mutual patients.
- When there is a qualified match and consent, Carequality pulls a CCDA file of your patient's data from Elation and shares it with the querying organization.
- Elation **does** **not** share images or other non-CCDA document types through Carequality; we share CCDA-formatted data only.

The CCDA content we expose via Carequality matches the CCDA sections listed in the CCDA export guide (problems, medications, allergies, encounters, labs, care plan, goals, etc.).

### What you see when you query Carequality

When you click **Outside Care** in the Clinical Profile and the patient has granted consent:

- Elation queries the Carequality network using the patient's demographics.
- Any matched outside records appear in the **Outside Care** document viewer.
- You may see multiple document types:
 - CCDs/CCDAs – structured clinical summaries.
 - PDFs, images (PNG, TIFF, etc.) – scanned notes, results, or other unstructured content.

ℹ️  **NOTE** Labs and notes may be available as documents depending on trading partner capabilities. Elation can only return what other Carequality-enabled organizations choose to share and what their patients have consented to share.

### Viewing vs importing Carequality documents into the chart

Carequality documents **do not** automatically merge into your chart:

- For CCDs/CCDAs in the **Outside Care** viewer:
 - **Sign Off**: files the document into the patient's chart as a report, without importing discrete data.
 - **Sign Off & Import**: files the document and allows you to select and import discrete data (demographics, allergies, problems, immunizations, medications) into the Clinical Profile, just like other CCD/CCDA imports.
- For PDFs and images in the **Outside Care** viewer:
 - These are view-only in the viewer.
 - To retain them in the chart, you must download the file and drag-and-drop it into the chart to file it as a **Report**.

Elation has no control over gaps or omissions in what other organizations share.

## Direct messaging & Elation Connect

### What's in an outbound Direct message

When you send a Provider Letter or Referral and the yellow banner indicates Direct messaging, Elation transmits a secure Direct message that typically includes:

- The **Letter**/**Referral** body text.
- Any attached chart records that are supported for Direct (e.g., visit notes, reports, labs, summaries).
- An automatically attached CCDA file for the patient's data, when supported by the recipient.

The receiving EHR decides:

- Whether to show the message body as a note, inbox item, or both.
- Whether to store attachments as scanned documents.
- Whether and how to parse the CCDA into their structured chart.

### What you see for inbound Direct messages

When you receive a Direct message in Elation:

- Incoming messages appear in:
 - **Provider Letters inbox** on Practice Home; and/or
 - **Requiring Action** in the patient's chart.
- Any attached CCD/CCDA file appears as a **Patient Summary** above the Direct message.
- Behavior differs by chart status:
 - No existing chart – Elation creates a new chart and can automatically populate the Clinical Profile from the CCD/CCDA.
 - Existing chart – Elation keeps the CCD/CCDA as a **Patient Summary**; you choose whether to import structured sections.

You can always:

- Open the Direct message to see exactly what text and attachments were received.
- Open the associated **Patient Summary** to see what was shared in the CCD/CCDA, and optionally import sections.

### What Elation Connect recipients can see

When you address a Provider Letter or Referral to a non-Elation contact with fax and/or email, Elation can invite that contact to Elation Connect, our secure provider portal:

- Connect is a read-only portal: it stores patient charts that contain only the records you sent from Elation, not your full internal chart.
- A Connect user can:
 - View the **Letter**/**Referral** and its attachments.
 - Download those records to transfer into their own system.
 - Reply back to you; replies come into your **Provider Letters inbox** and the patient's chart.

ℹ️   **NOTE** Connect users never receive live access to your Elation chart. They only see the specific snapshot (Letter & attachments) that you chose to send for that patient.

## Elation Patient Passport (patient portal)

### Default patient-visible data

Once a patient registers for Elation Patient Passport, they see:

- Practice contact information.
- Last and next appointment dates.
- Key demographics and contact preferences.
- The Clinical Profile (problems, allergies, medications, immunizations, history, etc.), excluding items marked as confidential.
- A visit summary for every signed visit note, which includes vitals, procedures, tests/treatments (including referrals, medications, and diagnostic test orders), care plan/instructions, and follow-up details.
- Any **Patient Letters** and attachments you send them (e.g., lab reports, imaging reports, handouts).

Visit summaries and Clinical Profile content are shared automatically once Passport is enabled for the patient; you **do** **not** need to attach them manually each time.

### What is not automatically shared with patients

Patients **are** **not** automatically granted access to every record in the chart. For example:

- Individual lab reports, imaging reports, and other Reports **are** **not** visible by default.
- Specific visit note sections or chart items tagged as **Confidential** are never exported in CCDA files and are not surfaced via Patient Passport sharing.

To share those items, your practice must intentionally:

- Attach reports or notes to a **Patient Letter**, or
- Include them in a CCDA export you share directly with the patient.

### Messaging and attachments from patients

If you allow two-way messaging:

- Patients can send new messages from Passport and attach files (e.g., outside records or photos).
- Replies and attachments arrive as **Patient Letters** in your Practice Home; you can file attachments directly into the chart as **Reports**.

You can also configure Passport as one-way (you push information out but do not allow patients to initiate messages) via the **Patient Passport Messages** settings.

# Where to verify "what was sent"

Here's where clinicians and staff can double-check outbound and inbound data:

- CCDA exports
 - Single-patient exports: downloaded .zip file on your workstation, plus a record in the patient's Chronological Record indicating the type of export (Complete Record, Customized, Referral, etc.).
 - Bulk exports: password-protected .zip file on your workstation.
- Carequality (Outside Care)
 - Use the **Outside Care** button in the Clinical Profile to re-open the viewer and see exactly which documents are available and what you previously filed or imported.
- Direct messages & Elation Connect
 - The signed **Provider Letter**/**Referral** in the patient's Chronological Record shows the final message body, attachments, and delivery method (Direct, fax, Elation, Connect).
 - Sent faxes and Connect invitations show status such as "Fax Sent" or "Letter and its attachments will be faxed," with error details for failures.
- Patient Passport
 - The **Patient Letters** and visit summaries in the patient's chart mirror what the patient can see; if a record is not attached to a **Patient Letter** or included in a visit summary, it is not automatically visible in Passport.

Use these locations to answer patient or partner questions about "what you sent" vs what their system or portal is currently showing.

# Related Articles

- [Patient Chart Guide- Sharing clinical care summaries with collaborating providers using C-CDA (CCDA) format](https://help.elationemr.com/s/article/Supported-Elation-CCDA-types)
- [Patient Chart Guide - Importing patient information from another EHR (CCD/CCDA Format)](https://help.elationemr.com/s/article/import-patient-information-from-another-ehr-c-cda-format)
- [Elation-Carequality Integration Introduction](https://help.elationemr.com/s/article/Carequality-Integration-Introduction)
- [Letter & Referral Guide - Sending and receiving Direct messages](https://help.elationemr.com/s/article/how-to-use-direct-messaging)
- [Letter & Referral Guide - Sending a fax](https://help.elationemr.com/s/article/how-to-send-a-fax)
- [Elation Patient Passport Guide](https://help.elationemr.com/s/article/elation-patient-passport-an-introduction)
- [Letter & Referral Guide - Accessing patient information sent by an Elation EHR user](https://help.elationemr.com/s/article/access-patient-information-securely-shared-by-an-Elation-EHR-user)
- [Promoting Interoperability (MIPS) - Provider to Patient Exchange](https://help.elationemr.com/s/article/Promoting-Interoperability-MIPS-Provider-to-Patient-Exchange)
- [Patient Chart Guide- Managing confidential records](https://help.elationemr.com/s/article/confidential-items-in-your-patient-chart)
- [Patient List Report Guide- Searching your patient panel](https://help.elationemr.com/s/article/find-patients-with-elations-patient-list)
- [Letter & Referral Introduction](https://help.elationemr.com/s/article/letter-and-referral-introduction)