# Prescription Form Guide - Viewing patient prescription benefits

Source: https://help.elationhealth.com/s/article/Prescription-Form-Guide-patient-prescription-benefits

---

## **Contents**

- [What is coverage, formulary, and cost estimate information and why is it valuable?](#description)
- [What information in Elation is used to retrieve coverage, formulary, and cost estimate information?](#data_for_benefits)
- [Retrieving coverage and formulary information](#coverage_and_formulary)
- [Retrieving cost estimate information](#cost_estimate)
- [Retrieving prescription benefits information for d](#discontinued_or_off_market_meds)[iscontinued and/or off-the-market medications](#discontinued_or_off_market_meds)
- [Frequently Asked Questions (FAQ)](#faq)

## **What is coverage, formulary, and cost estimate information and why is it valuable?**

The coverage information tells you whether a patient has prescription benefits coverage and which [Pharmacy Benefits Manager (PBM)](#PBM_role) covers the patient. Elation will show all prescription coverages available for the patient.

The formulary information serves as a guide for both healthcare providers and patients, outlining which medications are approved for coverage and the corresponding coverage limits and statuses. The formulary status tells you whether a medication is potentially reimbursable by the patient’s insurance and whether the medication is preferred and/or on- or off-formulary. Preferred medications are generally cheaper than non-preferred medications. Non-formulary medications may require prior authorization or have additional cost considerations compared to on-formulary medications.

The cost estimate information displayed is based on the patient’s prescription coverage benefits, and the medication, quantity, and pharmacy selected. Coverage, formulary and cost estimate information displayed is provided solely by the PBM and is not determined by Elation. Cost estimate information may include the estimated cost of the medication, cost breakdowns, coverage limits, prior authorization needs, and alternative options.

Overall, the medication coverage, formulary, and cost estimate information will tell you how much, and under what conditions the patient’s prescription benefits cover the cost of the medication you are about to prescribe to the selected pharmacy. If the patient has multiple coverages, then you may see coverage, formulary, and cost estimates for all coverages. Based on this information, you can make a well-informed decision regarding which variation of a medication is best suited for you to prescribe to the patient.

## **What information in Elation is used to retrieve coverage, formulary, and cost estimate information?**

The following chart outlines what information in the patient’s demographics or Prescription Form will be used to retrieve coverage, formulary, and cost estimate information:

| Patient Information | Coverage | Formulary | Cost Estimate |
| --- | --- | --- | --- |
| Required demographics: - Legal First Name - Legal Last Name - Date of birth - Sex at birth | ✔️ | | |
| Additional demographics: - Address (full address) - Primary phone number | ✔️ | | |
| Coverage | | ✔️ | ✔️ |
| Medication name | | ✔️ | ✔️ |
| Medication quantity | | | ✔️ |
| Days supply | | | ✔️ |
| Pharmacy | | | ✔️ |

**Important Note**: Medical insurance information saved in the patient’s demographics is not used for prescription coverage, formulary, and cost estimate queries.

## **Retrieving coverage and formulary information**

To retrieve coverage and formulary information:

1. Open the [Prescription Form (Rx/OTC/CS)](Prescriptions-Forms-Guide-ePrescribing-and-ordering-meds.md) in the patient’s chart
2. Select a medication
3. Look to the right of the Prescription Form to see the coverage of the medication and formulary information for that medication under 'COVERAGE'.
   - If the patient has multiple coverages, Elation will display the formulary information for all coverages listed. Use the scroll bar to scroll up and down to see all the coverage and formulary information.
   - If coverage or formulary information is unavailable you will see a note about this information being unavailable.

Elation will display all the formulary information that is shared by the Pharmacy Benefit Manager (PBM). Formulary information can include any of the details listed below but not all details are always available from the PBM.

- **User Tips**:
 - Hover your mouse cursor over information badges or details with an asterisk to see additional details as provided by the PBM.
 - Use the scroll bar to scroll up and down to see all the coverage and formulary information.

![]()

| Formulary Guidance Type | Details |
| --- | --- |
| Formulary status | Formulary status tells you whether a medication is potentially reimbursable by the patient’s insurance and whether the medication is preferred and/or on- or off-formulary.  View the Formulary Status Chart below for more details about the various formulary statuses. Hover your mouse cursor over any status to see its description. |
| Copay tier | The tier coverage is determined by the PBM and is organized from Tier 1 (more preferred) to lower tiers (less preferred). Tier 1 medications will generally be cheaper than Tier 2 medications and so forth. Tier coverage may also differ by pharmacy type (e.g. Retail vs Mail Order). Hover your mouse cursor over the ***copay details*** to see additional information about the copay tier. |
| Medication type | The formulary may categorize a medication by type (i.e. Prescription or Over-the-Counter) and note whether the medication is brand name or generic. Generic prescriptions are generally cheaper than their brand name counterparts. |
| Coverage factors and limits | Coverage factors and limits disclose the terms and conditions in which the coverage applies. These include: - quantity limits - age limits - prior authorization requirements - step medication protocols - drug-specific resource links |
| Therapeutic or payer-specified alternative medications | Any medications in the same drug group, class, and subclass as the medication selected are potentially therapeutic alternative medications. - If a PBM provides information about payer-specified alternative medications, then only payer-specified alternative medications and their details will be returned and disclosed under 'COVERAGE', even if other therapeutic alternative medications exist. Therapeutic alternative medications that are at a lower coverage status (less preferred) than the selected medication will never be displayed. - If payer-specified therapeutic alternative medications are not returned, Elation will display information about all therapeutic alternative medications that have an equal or higher coverage status (more preferred) returned by the PBM. Hover your mouse cursor over the name of any alternative therapeutic medication to see summarized copay and formulary status information. You can click on any alternative therapeutic medication to select that medication as a replacement for your script and see full formulary details. |

| **Formulary Status Chart** |
| --- |
| **Status** | **Description** |
| Preferred (On Formulary) | Medication is on the PBM formulary and is preferred. These medications will generally be cheaper than other medications that are not preferred or not on formulary. Generic medications will generally fall in this category. |
| On Formulary | Medication is on the PBM formulary but is not preferred. These medications will generally be cheaper than other medications that are not on formulary but more expensive than preferred medications. |
| Non-Formulary | Medication is not on the PBM formulary and may require prior authorization to be reimbursed by coverage. The insurance may also not offer prior authorization for reimbursement. These medications will generally be more expensive than preferred or on-formulary medications. |
| Non-Reimbursable | Medication is known to the PBM but is explicitly non-reimbursable. The patient must cover the cost of these medications without coverage contribution. These medications will generally be more expensive than preferred or on-formulary medications. |
| Formulary status unknown | Medication is not known to the formulary and the PBM has no additional coverage information to provide. |

## **Retrieving cost estimate information**

To retrieve cost estimate information:

1. Open the [Prescription Form (Rx/OTC/CS)](Prescriptions-Forms-Guide-ePrescribing-and-ordering-meds.md) in the patient’s chart
2. Select a medication and fill out the **Qty**
3. Select the pharmacy destination
4. Look to the right of the Prescription Form to see the cost estimate for that medication and pharmacy under 'COST ESTIMATE'. Elation will display all the cost estimate information that is shared by the Pharmacy Benefit Manager (PBM).
   - **Important Notes**:
     - If the patient has multiple coverages, Elation will by default display the cost estimate information for the first coverage listed. Select a different coverage to see the cost estimate information for that coverage.
     - By default, the cost estimate information is for a 30 day supply. Enter a different number in the **Days Supply** field if you would like the cost estimate to be for a different 'days supply'.
     - If cost estimate information is unavailable you will see a note about this information being unavailable.

Cost estimate information can include any of the details listed below but not all details are always available from the PBM.

- **User Tips**:
 - Hover your mouse over certain guidance types to see additional information as provided by the PBM.
 - Use the scroll bar to scroll up and down to see all the cost estimate information.

| Cost Estimate Guidance Type | Details |
| --- | --- |
| Cost | The cost of the medication as specified by the Payer. |
| Pharmacy Type | The type of pharmacy that can be used to retrieve the medication (e.g. Retail or Mail Order) will be listed if coverage is available for more than one pharmacy type. |
| Coverage Limits | Coverage limits disclose the terms and conditions in which the cost estimate applies. Hover your mouse cursor over the **Limits** tag to see the coverage factors and limits which can include: - quantity limits - age limits - usage recommendations & instructions |
| Prior Authorization Requirements | A  **PA**  tag will tell you whether prior authorization is required for the payer to reimburse the selected medication. The cost estimate you see is the cost estimate of the medication after prior authorization is acquired. Hover your mouse cursor over the  **PA**  tag to see any additional details that may be provided. |
| Estimate patient pay breakdown | Cost estimates may be broken down by the patient’s out-of-pocket responsibilities. Hover your mouse cursor over the cost to see any of the following details that may be disclosed: - Out-of-Pocket (OOP) applied - Out-of-Pocket (OOP) remaining - Deductible applied - Deductible remaining |
| Alternative medication options | The PBM may return specific medications deemed by the PBM to be therapeutic alternatives. If the PBM provides cost estimates for alternative medications then the cost estimate information for all alternatives will also be disclosed under 'COST ESTIMATE' in the 'Alternatives' section. |

## **Retrieving prescription benefits information for discontinued and/or off-the-market medications**

When a medication is discontinued by the manufacturer and/or taken off the market, its NDC code will be made obsolete and you will not be able to prescribe the medication or retrieve formulary or coverage information for that medication. Choose another active medication to continue with your prescription. If you'd like to continue prescribing the discontinued or off-the-market medication then you must [create a custom medication](https://help.elationemr.com/s/article/Prescriptions-Forms-Guide-ePrescribing-and-ordering-meds#add_med_to_database) and proceed without any prescription benefits information.

- **User Tip**: You may run into this situation when a medication in one of your Prescription Templates is discontinued by the manufacturer and/or taken off the market. Update or delete that template in your [Prescriptions Settings](https://help.elationemr.com/s/article/create-and-use-custom-rx-templates#managing_templates) to avoid running into this error.

## **Frequently Asked Questions**

- [Why is prescription coverage information not available for one of my patients?](#no_coverage)
- [Where does the coverage, formulary, and cost estimate information come from?](#source_of_data)
- [Why is the prescription coverage different from the medical insurance coverage saved in the patient chart?](#coverage_vs_insurance)
- [Can staff see prescription benefits information when drafting prescriptions?](#staff_delegates)
- [How does a Pharmacy Benefits Manager (PBM) contribute to the administration of prescription insurance benefits?](#PBM_role)
- [I selected a medication but I do not see any cost estimate information for the medication. Why?](#no_cost_estimate_data)
- [Will prescription insurance benefits be visible in the Elation Go mobile application?](#Elation_Go)
- [Do cost estimates include pricing with cash discount tools such as GoodRx?](#cash_pricing_programs)
- [Does Elation's prescription insurance benefits feature differ from other solutions like CoverMyMeds?](#CoverMyMeds)

#### **Why is prescription coverage information not available for one of my patients?**

Elation will query for patient prescription coverage every time the Prescription Form is opened. These are the most common reasons why prescription coverage may not be available:

- The patient does not have active prescription coverage.
- We could not find a patient match based on the demographics in the patient’s chart. Make sure the following information is in the patient’s demographics and then draft a prescription again or click “Re-check coverage”. Required fields are marked with an asterisk:
 - Legal First Name\*
 - Legal Last Name\*
 - Date of birth\*
 - Sex at birth\*
 - Address (full address)
 - Primary phone number
- The patient’s benefit plan is not part of the network of available information. Elation works with Surescripts, who works with 99% of plans in the United States, and the patient’s plan might be in the 1% that is not part of the Surescripts network.

#### **Where does the coverage, formulary, and cost estimate information come from?**

The formulary and cost information comes directly from the patient’s Pharmacy Benefit Manager (PBM). After you select the medication, quantity, and pharmacy the information is sent along with the patient’s coverage to the patient’s prescriptions benefit plan and then the patient’s out-of-pocket prescription cost and associated details is then returned and displayed on the right side of the Prescription Form along with alternative therapeutic medication options, if available.

#### **Why is the prescription coverage different from the medical insurance coverage saved in the patient chart?**

Formulary and prescription cost estimate information is based on the patient’s prescription coverage and not medical insurance. Elation works with Surescripts to determine coverage and Surescripts works with Pharmacy Benefit Managers (PBMs) to understand formulary and cost estimation information.

#### **Can staff see prescription benefits information when drafting prescriptions?**

Yes, anyone in the practice will be able to see prescription benefits information.

#### **How does a Pharmacy Benefits Manager (PBM) contribute to the administration of prescription insurance benefits?**

A Pharmacy Benefits Manager (PBM) is a third-party administrator that manages prescription drug benefits on behalf of health insurance plans, employers, and government programs. PBMs maintain a list of approved medications, known as a formulary. The formulary is designed to include cost-effective and clinically effective drugs. PBMs negotiate with pharmaceutical manufacturers to include specific drugs on the formulary and secure favorable pricing for medications included in the formulary to reduce overall drug costs for the insurer and patients.

#### **I selected a medication but I do not see any cost estimate information for the medication. Why?**

To see cost estimate information for a medication, the patient’s Legal First Name, Legal Last Name, Date of birth, and Sex at birth must be in their demographics and the medication, quantity, and pharmacy must be selected in the Prescription Form. Enter the quantity and select a pharmacy and then you will see cost estimate information if any is available. [Click here to understand the circumstances in which cost estimate information is not available](#no_coverage).

#### **Will prescription insurance benefits be visible in the Elation Go mobile application?**

Prescription insurance benefits information is not available in the [Elation Go](elation-go-the-mobile-app-for-practices.md) mobile application at this time. We will notify you when we support this in the future.

#### **Do cost estimates include pricing with cash discount tools such as GoodRx?**

GoodRx and other cash pricing programs are not currently included in the cost estimate feature. We will notify you when we support this in the future.

#### **Does Elation's prescription insurance benefits feature differ from other solutions like CoverMyMeds?**

Elation's prescription insurance benefits feature and CoverMyMeds are both platforms that offer prescription insurance benefits information and both pull information from Prescription Benefits Managers. For these reasons, the information you see in Elation and CoverMyMeds should be the same.

## **Related Articles**

- [Prescription Form Guide- ePrescribing and ordering medications using a single prescription form](Prescriptions-Forms-Guide-ePrescribing-and-ordering-meds.md)
- [Prescription (Rx) Templates Guide](create-and-use-custom-rx-templates.md)
- [Drug Decision Support Guide- Monitoring drug interactions](drug-decision-support.md)
- [EPCS (Electronic Prescribing of Controlled Substances) Introduction](introduction-to-electronic-prescribing-of-controlled-substances-epcs.md)
- [User Accounts Guide- Utilizing authorized staff delegates](staff-permissions--staff-delegates.md)
- [Prescriptions Guide- Frequently Asked Questions](Prescriptions-Guide-Frequently-Asked-Questions.md)