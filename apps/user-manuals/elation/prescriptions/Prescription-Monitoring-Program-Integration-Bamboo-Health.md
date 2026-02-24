# Prescription Monitoring Program (PMP/PDMP) Integration- Bamboo Health

Source: https://help.elationhealth.com/s/article/Prescription-Monitoring-Program-Integration-Bamboo-Health

---

**Recommended Reading**: [Prescription Monitoring Program (PMP/PDMP) Integration Introduction](Integrating-with-your-state-s-Prescription-Monitoring-Program-PMP-PDMP.md)

## **Contents**

- [What is the Bamboo Health PMP Integration?](#overview)
- [Which states can utilize the Bamboo Health PMP Integration?](#supported_states)
- [How much does the integration cost?](#cost)
- [How do I activate my Bamboo Health integration?](#activate_integration)
- [Viewing Bamboo Health’s Prescription Monitoring Program (PMP) reporting](#view_PMP_report)
- [What data is available via Bamboo Health’s Prescription Monitoring Program (PMP) reporting?](#PMP_report_data)
- [Viewing Bamboo Health’s Narxcare reporting](#view_NarxCare_report)
- [What data is available via Bamboo Health’s NarxCare reporting?](#NarxCare_data)
- [Frequently Asked Questions (FAQ)](#faq)

## **What is the Bamboo Health PMP Integration?**

Elation works with Bamboo Health, a third-party healthcare technology solutions company, to provide a seamless EHR to Prescription Monitoring Program (PMP) integration in supported states (see the table below for a full list of the supported states and what features are offered in each state).
Once integrated, two features will be made available to you in the EHR depending on the selected state PMP:

1. Prescription Monitoring Program (PMP) reporting of detailed controlled substance prescription dispense history for patients
2. NarxCare data which can contain the following details based on a patient’s controlled substance prescription dispense history:
   - Overdose risk score
   - Graphs or charts of the prescription dispense history over time

## **Which states can utilize the Bamboo Health PMP Integration?**

Bamboo Health supports PMP integrations in the following states: Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Mississippi, Missouri, Montana, Nevada, New Hampshire, New Jersey, New Mexico, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Puerto Rico, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, Washington, DC, West Virginia, and Wyoming. See the table below for a full list of the supported states and their offerings.

The Bamboo Health PMP integration is *not available* in Guam, Illinois, Nebraska, New York, or Wisconsin.

**Important Notes**:

1. PMP data surrounding detailed controlled substance prescription dispensing history for patients may be either a free feature or a paid feature depending on whether or not your state funds your access. Payment will be made directly to Bamboo Health. Find your state in the table below for full details.
2. NarxCare data for patients may be either a free feature or a paid feature depending on whether or not your state funds your access. Payment will be made directly to Bamboo Health. Find your state in the table below for full details.
   - Practices in Utah who want access to PMP data must pay Bamboo Health for access to PMP data and NarxCare data as required by the state.
   - The state of Tennessee does not allow for access to NarxCare data.
   - Only NarxCare graphs and charts are available in the states of Massachusetts and New Jersey. The overdose risk score is not available.

| State | Do you need to pay for access to PMP data? | is NarxCare data available or required? | What Narxcare data is available? | Do you need to pay for access to NarxCare data? |
| --- | --- | --- | --- | --- |
| Alabama (AL) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Alaska (AK) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Arizona (AZ) | No (state-funded) | Not available | None | N/A |
| Arkansas (AR) | Yes | Available but not required | NarxCare score, charts, & graphs | Yes |
| California (CA) | Yes | Available but not required | NarxCare score, charts, & graphs | Yes |
| Colorado (CO) | Yes | Available but not required | NarxCare score, charts, & graphs | Yes |
| Connecticut (CT) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Delaware (DE) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Florida (FL) | Yes | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Georgia (GA) | No (state-funded) | Not available | None | N/A |
| Hawaii (HI) | Yes | Available but not required | NarxCare score, charts, & graphs | Yes |
| Idaho (ID) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Indiana (IN) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Iowa (IA) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Kansas (KS) | No (state-funded) | Not available | None | N/A |
| Kentucky (KY) | Yes | Available but not required | NarxCare score, charts, & graphs | Yes |
| Louisiana (LA) | No (state-funded) | Not available | None | N/A |
| Maine (ME) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Maryland (MD) | Yes | Available but not required | NarxCare score, charts, & graphs | Yes |
| Massachusetts (MA) | No (state-funded) | Available and required | NarxCare charts & graphs only | No (state-funded) |
| Michigan (MI) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Minnesota (MN) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Mississippi (MS) | Yes | Available but not required | NarxCare score, charts, & graphs | Yes |
| Missouri (MO) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Montana (MT) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Nevada (NV) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| New Hampshire (NH) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| New Jersey (NJ) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| New Mexico (NM) | No (state-funded) | Not available | None | N/A |
| North Carolina (NC) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| North Dakota (ND) | Yes | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Ohio (OH) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Oklahoma (OK) | No (state-funded) | Not available | None | N/A |
| Oregon (OR) | No (state-funded) | Not available | None | N/A |
| Pennsylvania (PA) | Yes | Available but not required | NarxCare score, charts, & graphs | Yes |
| Puerto Rico (PR) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Rhode Island (RI) | Yes | Available but not required | NarxCare score, charts, & graphs | Yes |
| South Carolina (SC) | Yes | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| South Dakota (SD) | Yes | Available but not required | NarxCare score, charts, & graphs | Yes |
| Tennessee (TN) | No (state-funded) | Not allowed | None | N/A |
| Texas (TX) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded |
| Utah (UT) | Yes | Available and required | NarxCare score, charts, & graphs | Yes |
| Vermont (VT) | Yes | Available but not required | NarxCare score, charts, & graphs | Yes |
| Virginia (VA) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Washington (WA) | Yes | Available but not required | NarxCare score, charts, & graphs | Yes |
| Washington, DC (DC) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| West Virginia (WV) | No (state-funded) | Available and required | NarxCare score, charts, & graphs | No (state-funded) |
| Wyoming (WY) | Yes | Available but not required | NarxCare score, charts, & graphs | Yes |

\* The Bamboo Health PMP integration is *not available* in Guam, Illinois, Nebraska, New York, or Wisconsin.

## **How much does the integration cost?**

The cost of the integration depends on whether or not the PMP data or NarxCare data is funded by your state. If it says ‘state-funded’ in the *'Do you need to pay for access to PMP data?'* or *'Do you need to pay for access to NarxCare data?'* columns above, that means the state pays for your access to that data. For states not funded, the cost can depend on a variety of factors and Bamboo Health will be able to assist you with a cost estimate. [Click here to reach out to Bamboo Health](https://go.bamboohealth.com/ehrrequest.html).

## **How do I activate my Bamboo Health integration?**

You will work directly with Bamboo Health on creating your Bamboo Health account, contracting, and getting state PMP approval to go live with the integration. Once complete, Bamboo Health will send your organization’s credentials to Elation to activate the integration. Below is the step-by-step breakdown of the entire integration process.

| Step | Task | Owner |
| --- | --- | --- |
| 1 | Send Bamboo Health a PMP integration request by filling out this form: <https://go.bamboohealth.com/ehrrequest> - If in Tennessee, use this request form instead: <https://go.bamboohealth.com/tngatewayintegrationrequest> - If in Kentucky, Kentucky has a special Bamboo-specific set of credentials that will preclude the practice from having more than one Bamboo PMP connection.   - If a practice is only going to be practicing in Kentucky or Kentucky is the only Bamboo PMP requested, the practice may use either Bamboo or LogiCoy for PMP integration.   - If the practice is practicing in at least one other state beyond Kentucky, the practice will need to ensure the only Bamboo integration is Kentucky or the practice can choose to use LogiCoy’s Kentucky integration with other state integrations. | Customer |
| 2 | Click “Create an Account” in the top right-hand corner after filling out the request form. | Customer |
| 3 | Login and follow the on-screen prompts to provide the needed information for your integration request. | Customer |
| 4 | Sign all necessary agreements within the Bamboo Health portal and complete your application. | Customer  Bamboo Health |
| 5 | Upon receipt of your completed application, Bamboo Health will submit your request to the state for final approval. | Bamboo Health → State |
| 6 | Upon state approval, Bamboo Health will send credentials to your organization’s primary contact and Elation. This is when Elation will begin working with you to complete your integration. A confirmation email will be sent to your organization’s primary point of contact. | Bamboo Health → Customer & Elation |
| 7 | Elation receives credentials from Bamboo Health. | Bamboo Health → Elation |
| 8 | Elation stores your organization’s credentials from Bamboo Health | Elation |
| 9 | Elation may contact your practice to verify minimum identifiers required for each state such as NPI, DEA and/or state license. - Alaska = DEA & License # - Alabama = DEA - California = NPI - Indiana = DEA - Michigan = DEA, NPI & License # - Minnesota = DEA - New Hampshire = DEA - Ohio = DEA & License # - All other states: Not required but need at least one identifier is needed for the integration to work, NPI is acceptable. | Elation → Customer |
| 10 | Elation enables the “Check PMP” button. Once enabled, it will be available in every patient chart. Integration is considered live. | Elation |
| 11 | Once the integration is live, a confirmation email will be sent to your organization’s primary contact. | Elation → Customer |

**Important Note**: The Bamboo Health integration will be gradually implemented for interested customers. The length of time it takes to activate the integration will also depend on how many requests are being managed by Bamboo Health and how quickly your state approves the integration.

## **Viewing Bamboo Health’s Prescription Monitoring Program (PMP) reporting**

To view the Prescription Monitoring Program reporting, connected Providers can click the “Check PMP” button from one of the following 4 (four) locations in the patient’s chart:

- At the bottom of the ‘Permanent Rx Meds’ list in the Clinical Profile
- In the dropdown when you click the “Meds Hx” button at the top of the patient’s chart
- At the top of the Medication History window
- In the Prescription Form next to the **NDC with Packaging** field

![]()

Once the “Check PMP” button is clicked, a query to the PMP is initiated and, if successful, a new browser tab will be opened with the patient’s PMP report. [Reference the data below to see what is available in the PMP report](#PMP_report_data).


A note will be documented in the patient chart after a successful PMP check for reporting purposes. This note can be exported to a visit note or to an office message.
![]()

## **What data is available via Bamboo Health’s Prescription Monitoring Program (PMP) reporting?**

Bamboo Health’s Prescription Monitoring Program (PMP) reporting displays the patient’s past 2 years of controlled substance refill history broken down into the following:

- A summary of the medication history information broken out by
 - Payment type
 - Prescribers
 - Pharmacies
 - Narcotics vs Buprenorphine
- Prescription history detail including the written dates and filled dates

## **Viewing Bamboo Health’s Narxcare reporting**

If you have access to Bamboo Health’s NarxCare data, you will see the ‘Overdose Risk Score’ at the bottom of the Permanent Rx Meds list in the Clinical Profile.

- Place your mouse cursor over the score to see the overall risk level of the score.

**Important Note**: Narxcare data is made available by Elation Health for informational purposes only and is not an endorsement by Elation: NarxCare is a commercial opioid overdose risk scoring platform proprietary to Bamboo Health. NarxCare has not been clinically validated for use on patients. [Click here for more information](https://academic.oup.com/jamia/article/30/10/1741/7222347).

## **What data is available via Bamboo Health’s NarxCare reporting?**

Bamboo Health’s NarxCare data can contain the following details based on a patient’s controlled substance prescription dispense history:

1. Overdose risk score
2. Graphs or charts of the prescription history over time

## **Frequently Asked Questions**

#### **Can Staff Level Users and non-prescribing Provider Level Users use the integration?**

Staff Level Users and non-prescribing Provider Level Users cannot use this integration. When Staff Level Users and non-prescribing Provider Level Users who are not set up for the integration click the “Check PMP” button, the state PMP login page will be opened in a new browser tab instead. Anyone can use their state PMP login credentials to log in to the state PMP directly to access PMP data.

#### **Why is the state’s PMP login page opening when I click the “Check PMP” button?**

If your state’s PMP login page is opening instead of directly accessing PMP data through Bamboo Health, this means your account is not set up for the integration. Only prescribing Providers can use the integration at this time. Staff Level Users and non-prescribing Providers cannot use the integration.

If you believe your account should be set up with the integration, contact Elation using the "I need help" -> "Contact Elation Support" button to let Elation know.

#### **What happens if the patient is not found in the PMP?**

If there is no record of the patient in the PMP, a new browser tab will still open with a confirmation that no match was found. This is still considered a successful PMP check and a note will be recorded in the patient record that a PMP check was performed.

#### **Why is the Bamboo Health integration not available for my state?**

Bamboo Health only support PMP integrations in the states of Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Mississippi, Missouri, Montana, Nevada, New Hampshire, New Jersey, New Mexico, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Puerto Rico, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, Washington, DC, West Virginia, and Wyoming.

If you are in the state of Illinois you can consider using the LogiCoy PMP Integration. [Click here to learn more about the LogiCoy PMP integration](Prescription-Monitoring-Program-Integration-LogiCoy.md).

If you are in Guam or the states Nebraska, New York, or Wisconsin, you will not be able to use any of Elation’s PMP integrations at this time. We will notify you if a PMP integration becomes available for these states.

## **Related Articles**

- [Prescription Monitoring Program (PMP/PDMP) Integration Introduction](Integrating-with-your-state-s-Prescription-Monitoring-Program-PMP-PDMP.md)
- [Prescription Monitoring Program (PMP/PDMP) Integration- LogiCoy](Prescription-Monitoring-Program-Integration-LogiCoy.md)
- [Prescription Form Guide- ePrescribing and ordering medications](Prescriptions-Forms-Guide-ePrescribing-and-ordering-meds.md)