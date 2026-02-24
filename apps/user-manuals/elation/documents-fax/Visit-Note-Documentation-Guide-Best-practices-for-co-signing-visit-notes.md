# Visit Note Documentation Guide- Best practices for co-signing visit notes

Source: https://help.elationhealth.com/s/article/Visit-Note-Documentation-Guide-Best-practices-for-co-signing-visit-notes

---

## **Contents**

- [Who needs to co-sign visit notes?](#reason)
- [Co-signing under the non-physician practitioners' (NPP's) name](#npp)
 - [Identifying visit notes for review](#identify)
    - [NPP flags specific visit notes](#NPP_flags)
    - [The supervising physician selects visit notes](#SP_selects)
- [Co-signing under the practitioner's name](#practitioner)
 - [Creating the Visit Note Template for attestation](#creating_templates)
 - [Completing the encounter](#complete_encounter)
- [Using Templating software to facilitate co-signing](#templating_software)





## **Who needs to co-sign visit notes?**

If your practice employs non-physician practitioners (NPPs), a supervising physician is responsible for reviewing the work, records, and practice of the NPP to ensure that appropriate treatment is rendered and appropriate directions are given and understood as applicable to the law. Supervising physicians are required to note that they reviewed an NPP's work or include their name/signature in the clinical documentation for proper legal documentation purposes. Each state has different co-signature requirements that need to be followed.

Elation currently allows one provider-level user to sign each visit note which then captures one signature in a 'structured' manner in the visit note. The physician/practitioner that signs the visit note is typically the provider you are billing the encounter under. Then, to capture a co-signature, there are subsequent workflows that can be completed depending on how you plan to bill:

1. For ‘Direct Billing’
   - The NPP performs the visit, and the visit is billed under the NPP's NPI number. There must be documentation that the supervising physician reviewed a certain percentage of encounters.
2. For ‘Incident-To Billing’
   - The NPP performs the visit, and the visit is billed under the supervising physician's NPI number. There must be documentation of which NPP saw the patient and who rendered the encounter.






## **Direct Billing**

For Direct Billing, the NPP is billing under their own NPI number. Different states require a different percentage of a NPP's encounter documentation to be reviewed by their supervising physician for clinical appropriateness. The co-sign workflow in Elation can be divided into two main steps:

1. Identifying the visit notes that a supervising physician needs to review
2. Documenting that a review was completed

### **Identifying visit notes for review**

After the NPP signs off on the visit note documentation, there are two options for identifying visit notes for supervising physician review and/or sign off:

1. The NPP can flag specific visit notes for the supervising physician
2. The supervising physician can randomly select visit notes themselves

#### **NPP flags specific visit notes**

The NPP can identify and route visit note(s) to the supervising physician for review and/or sign off using the office message feature in Elation. To do so:

1. The NPP locates a signed visit note in the patient's chart
2. The NPP clicks "Actions" >> "Send: Office Message" at the top of the visit note
3. The NPP enters the supervising physician's name in the "To" field and enters a short message in the "Body" (ex. 'Please review' or 'Please review & sign')
4. The NPP clicks "Send"
5. The supervising physician then checks their "Office Messages" inbox daily for messages from the NPP
6. The supervising physician clicks on the patient's name to open the chart to view the visit note and review the documentation
7. The supervising physician then replies to the office message to close the loop (ex. 'Review complete' or 'Approved') and clicks "Send and Sign Off".
8. There is now documentation in the patient's chart that states the supervising physician reviewed a specific visit note signed by the NPP.

#### **The supervising physician selects visit notes**

The supervising physician can log in to Elation and use the *Billing Report* to select visit notes for review and then they can use the *Office Message* or *Non-Visit Note* features to document their review and/or sign off.

- **Note**: This workflow requires the NPP to enter billing information for each visit note prior to the NPP signing off on the visit note.


To use this workflow:

1. The supervising physician opens the *Billing Report*using one of the following options:
   1. Click on the "Billing" button at the top of the Practice Home
   2. Click "Reports" >> "Billing Report" at the top of any page in Elation
2. The supervising randomly selects signed visit notes completed by the NPP by clicking on a patient under one these sections
   1. the "Signed Visit Notes Not Yet Billed" section for customers who do not have a Practice Management System (PMS) integration with Elation
   2. the "Visit Notes with Bills Pending Sync to PMS" section for customers who have a Practice Management System (PMS) integration with Elation
3. The supervising physician reviews the visit note documentation for that date of service
   - **User Tip**: If the supervising physician needs additional clarification from the NPP about any contents of the encounter, they can send an *Office Message* to the NPP for additional clarification before signing off on the visit note draft.
4. After the supervising physician reviews the visit note documentation, the supervising can use one of the following features to make note of their review and/or sign off:
   1. Office Message:
      1. Click "Actions" >> "Send: Office Message" at the top of the visit note they reviewed
      2. Enter the NPP's name or their own name (depending on preference) in the "To:" field
      3. Enter a short message in the "Body" (ex. 'Review complete' or 'Approved')
      4. Click "Send"
      5. Locate the message in the *Requiring Action* section of the patient's chart & click "Sign" at the top of the message
   2. Non-Visit Note:
      1. Click "Notes" >> "Non-Visit Note" at the top of the patient's chart after reviewing the NPP's visit note
      2. Enter a short message in the body of the *Non-Visit Note* (ex. 'I reviewed the visit note for Date of Service 04/01/2022' or 'I reviewed the visit note for Date of Service 04/01/2022 and sign off on the work.')
      3. Click "Sign Note"

## **Incident-To Billing**

Incident-To Billing means the non-physician practitioner (NPP) sees the patient and documents the encounter and is billing under their supervising physician's NPI number. The documentation must capture the NPP's name in order to meet a requirement about documenting who saw the patient and who rendered the encounter.

We recommend the NPP uses a Visit Note Template to capture their name and statement in regards to seeing the patient and rendering the encounter. For example, the statement can be 'Visit was rendered and documented by Jane Doe, NP and completed under supervising physician James Hibbert, MD'.

####

#### **Creating the Visit Note Template for attestation**

1. Open the Visit Note Templates management window using one of the following methods:
   1. Click the "Visit Note Templates" button at the top of any visit note draft
   2. Click "Templates" >> "Visit Note Templates" at the top of any patient's chart
2. Click the "+New Template" button at the top of the Visit Note Templates management window
3. Enter a name for the template in the "Template Name" field (ex. 'Visit Attestation')
4. Select a section for storing your attestation. We recommend the *Procedure* section because it usually stores actions taken during the encounter.
5. Enter your attestation language in the *Procedure* section of the Visit Note Template. (ex. 'Visit Attestation: Visit was rendered and documented by Jane Doe, NP and completed under supervising physician James Hibbert, MD'.)
6. Click "Save Template"

#### **Completing the encounter**

After the NPP completes the encounter documentation in the Visit Note draft, the NPP will enter the visit attestation and then re-assign the visit note draft to their supervising physician for final review and sign off:

1. The NPP completes documentation of the encounter in the visit note draft
2. The NPP clicks the "Visit Note Templates" button at the top of any visit note draft
3. The NPP clicks the "Export to Note" button next to the visit attestation template to export the visit attestation template into the visit note draft
4. The NPP changes the provider at the top of the visit note draft to the supervising physician's name
5. The NPP clicks "Save as Draft & Close" to drop the visit note draft in the supervising physicians's "Draft Notes" inbox
6. The supervising physician then checks their Practice Home "Draft Notes" inbox daily for visit notes to review
7. The supervising physician clicks on the patient's name to open the chart and clicks on the 'In Progress...' visit note
8. The supervising physician reviews the visit note draft and then clicks the "Sign Visit Note" button once they have approved the contents of the encounter.
   - **User Tip**: If the supervising physician needs additional clarification from the NPP about any contents of the encounter, they can send an *Office Message* to the NPP for additional clarification before signing off on the visit note draft.

####

## **Using Templating software to facilitate co-signing**

Using a [templating software](using-templating-softwares-with-elation.md) will allow the NPP or supervising physician to drop text on-demand into records in Elation. The text can dictate:

1. that the NPP rendered a visit
2. that the NPP is requesting their supervising physician to review a visit note they signed
3. that the supervising physician reviewed the encounter and is co-signing a visit note





## **Related Articles**

- [Office Message Feature Guide](How-to-use-Office-Messages.md)
- [Practice Home Guide- Checking for requiring action items](check-for-your-offices-daily-to-do-list.md)
- [Templates Guide- Using templating softwares with Elation](using-templating-softwares-with-elation.md)