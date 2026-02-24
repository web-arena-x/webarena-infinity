# Medication List Management Guide - Managing a patient's medication history

Source: https://help.elationhealth.com/s/article/medication-history

---

# **Contents**

- [Overview](#overview)
 - [What is the medication history?](#description)
 - [Anatomy of the Medication History list](#medication_list_anatomy)
 - [Anatomy of a medication thread](#medication_thread_anatomy)
- [Workflows](#workflows)
 - [Viewing active, permanent medications in the Clinical Profile](#Clinical_Profile)
 - [Viewing the full medication history](#full_medication_history)
 - [Adding medications to the medication history](#adding_medications)
    - [Prescribing medications](#prescribing)
    - [Documenting medications a patient is already taking](#documenting)
 - [Managing the Permanent vs. Temporary classification of medications](#permanent_vs_temporary)
 - [Merging and un-merging medication threads](#merging_and_unmerging)
    - [Merging medication threads](#merging_meds)
    - [Unmerging medication threads](#unmerge_meds)
 - [Reconciling medications](#reconciling_medications)
 - [Discontinuing medications](#discontinuing_medications)
 - [Deleting a medication](#deleting_a_medication)

# **Overview**

## **What is the medication history?**

The medication history contains a list of all medications ever prescribed or documented for a patient. Medications are organized in alphabetical order by medication name and divided into the following statuses:

- Permanent Rx
- Permanent OTC
- Temporary
- Discontinued
- Script(s) Canceled

## **Anatomy of the Medication History list**

| | |
| --- | --- |
| **A** | Medication search bar - used for searching for medications in the medication history. |
| **B** | Shortcuts for taking action on medications in the medication history. These include:   - Reconcile Active Medications - Check PMP - Print Medication History - Bulk Refill |
| **C** | Medication section heading. |
| **D** | The order of the medications within that section of the medication history. |
| **E** | The link to the [medication thread](#medication_thread_anatomy) - created from the name, dosage and Sig of the **most recent** prescription or record in the medication thread. |
| **F** | The month and year of the **first** prescription or record in the [medication thread](#medication_thread_anatomy). |
| **G** | The date and time the medication was last modified. |
| **H** | References to any medications that were merged into the [medication thread](#medication_thread_anatomy). |

## **Anatomy of a medication thread**

| | |
| --- | --- |
| **A** | Medication search bar - used for searching for medications in the medication history. |
| **B** | Shortcut for returning to the full medication history. |
| **C** | Medication section heading. |
| **D** | The month and year of the **first** prescription or record in the medication thread. |
| **E** | The title of the medication thread - created from the name, dosage and Sig of the **most recent** prescription or record in the medication thread. |
| **F** | All the prescriptions and records in the medication thread. View a prescription in detail by clicking on the blue text. |
| **G** | The date of the **first** prescription or record in the medication thread. |

# **Workflows**

## **Viewing active, permanent medications in the Clinical Profile**

A quick view of a patient’s permanent, active medications can be found in the Clinical Profile (left column of the patient chart), grouped into two separate drug classifications:

- Permanent Rx Meds
- Permanent OTC Meds

Each list is sorted chronologically, with the most recent medication at the top. The date at the beginning of each medication entry is when the medication was first prescribed or recorded in the patient's chart.

## **Viewing the full medication history**

There are two ways to pull up the full medication history which includes permanent, temporary and discontinued medications:

1. Go to any of the permanent, active medication list headers in the Clinical Profile and click **Actions** -> **View All Meds**.
2. Click **Meds Hx** -> **Medication History** at the top of the patient's chart.

###

## **Adding medications to the medication history**

Medications are automatically added to the Medication List when the medication is prescribed or documented in the patient's chart. Reference the workflows below for more details.

### **Prescribing medications**

[Click here for instructions on how to prescribe medications](https://help.elationemr.com/s/article/Prescriptions-Forms-Guide-ePrescribing-and-ordering-meds).

### **Documenting medications a patient is already taking**

New patients joining your practice may already be taking medications prescribed by other providers. To document a medication that a patient is actively taking (not prescribe new medications):

| | |
| --- | --- |
| **1** | Open the Document Medication form using one of the following workflows:   - Click **+ Document Med Pt is On** in the **Permanent Rx Meds** or **Permanent OTC Meds** section of the Clinical Profile. - Go to the header of the **Permanent Rx Meds** or **Permanent OTC Meds** section of the Clinical Profile and click **Actions** -> **Document Med**. - Click **Rx** -> **Document Med Pt is On** at the top of the patient's chart. |
| **2** | Select the type of medication you are documenting from the **Type** dropdown. |
| **3** | Enter the date the patient started the medication in the **Date** field.   - If the patient does not remember the exact month and date they started the medication, type in the year and then press the **Tab** key on your keyboard. Elation will automatically set the date as January 1st of that year. |
| **4** | Enter the medication name in the **Med** field by typing in the drug name and selecting it from the medication database. |
| **5** | Fill in the rest of the medication details as needed. Click more... to expose additional fields.   - The more details you fill in, the easier your workflows will be when you refill medications. |
| **6** | Save the medication by clicking one of the save options. |

## **Managing the Permanent vs. Temporary classification of medications**

When you prescribe or document medications, they're automatically classified as 'Permanent' unless you change the classification to 'Temporary' in the form. For [downloaded medications](https://help.elationemr.com/s/article/retrieving-previous-medication-history-for-your-patients), Elation automatically classifies each medication as 'Permanent' or 'Temporary' based on whether the medication is typically used to treat chronic or acute conditions.

- You can find temporary medications in the [full medication history](#full_medication_history).

You can change a medication's classification by clicking **Actions** next to the medication in the medication list and selecting **Set as Temporary Med** or **Set as Permanent Med** from the dropdown.

## **Merging and un-merging medication threads**

### **Merging medication threads**

To consolidate multiple [medication threads](#medication_thread_anatomy) for the same medication:

| | |
| --- | --- |
| **1** | Locate the medication thread from the Clinical Profile or Medication History list. |
| **2** | Click **Actions** -> **Merge with other Med**. |
| **3** | Select the medication you want to merge with in the **Choose Med(s) to Merge with** box. |
| **4** | Click **Merge with Selected Med(s)**. |
| **5** | A yellow banner will appear at the top of the chart that says **Meds merge complete** to indicate the action has been completed. |

ℹ️   **NOTES**

- Do not click the **Actions** button next to a specific prescription because you can only merge medications from the medication thread.
- When you merge two medication threads, the new thread will be named after the most recent prescription's or record's name, dosage, and Sig.

### **Unmerging medication threads**

To unmerge medication threads:

| | |
| --- | --- |
| **1** | Locate the medication thread from the Clinical Profile or Medication History list. |
| **2** | Click **Actions** -> **Move to other Med (un-merge)**. |
| **3** | Select **Set as Its Own Med** in the respective section you want it to be in OR select a new medication you want to merge it with in the **Choose Med(s) to Merge with** box. |
| **4** | Click **Merge Order into Selected Med**. |
| **5** | A yellow banner will appear at the top of the chart that says **Order has been moved** to indicate the action has been completed. |

**Reconciling medications**

Use the Medication Reconciliation feature to review and update a patient's active medication list. When you complete medication reconciliation, all changes—including sig edits, additions, and discontinuations—are saved immediately.

Discontinued medications move to the **Discontinued** section of the Medication History with the reason you selected, and the **Last Reconciled** date updates at the top of the Medication History section.

[Click here for step by step instructions on how to use the Medication Reconciliation feature](https://help.elationemr.com/s/article/Reconciling-active-medications).

## **Discontinuing medications**

[Click here for step by step instructions on how to discontinue medications](https://help.elationemr.com/s/article/Prescriptions-Guide-Discontinuing-medications).

####

## **Deleting a medication**

Best practice is to only delete medications if they were inaccurately documented. To discontinue a medication the patient is no longer taking, follow the discontinue medication instructions instead.

To delete a medication:

| | |
| --- | --- |
| **1** | Locate the medication thread from the Clinical Profile or Medication History list. |
| **2** | Click **Actions** -> **Remove Medication**. |
| **3** | Click **Yes, Delete** to confirm deletion. |

**💡**  **USER TIP** The Audit Log feature can be used to track actions taken on a medication, such as deletion. [Click here for more information about Audit Logs](Patient-Chart-Guide-Audit-Logs.md).

####

**Related Articles**

- [Medication List Management Guide - Reconciling active medications](https://help.elationemr.com/s/article/Reconciling-active-medications)
- [Medication History Download Introduction](retrieving-previous-medication-history-for-your-patients.md)
- [Prescription Form Guide- ePrescribing and ordering medications](https://help.elationemr.com/s/article/Prescriptions-Forms-Guide-ePrescribing-and-ordering-meds)
- [Prescriptions Guide - Discontinuing medications](https://help.elationemr.com/s/article/Prescriptions-Guide-Discontinuing-medications)