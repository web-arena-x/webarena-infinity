# Patient List Report Guide- Searching your patient panel

Source: https://help.elationhealth.com/s/article/find-patients-with-elations-patient-list

---

# **Contents**

- [Overview](#overview)
 - [What is a Patient List Report?](#description)
 - [Why is the Patient List Report useful?](#benefits)
- [Workflow Instructions](#workflows)
 - [Generating a Patient List Report](#generate_report)
    - [Using Quick Views](#quick_views)
    - [Using filters](#filters)
      - [Available filters](#FilterOptions)
 - [Viewing Patient List Report contents](#view_reports)
    - [Viewing the report summary](#report_summary)
    - [Viewing the detailed report as a spreadsheet (CSV)](#spreadsheet)
 - [Exporting charts as C-CDA files](#export_CCDA)
- [Sample Reports](#SampleReports)
 - [Patients who are due for an annual wellness visit](#AWV)
 - [Patients who are due for a flu vaccine](#flu)
 - [Active patients with diabetes who need follow-up on their HbA1c levels](#diabetes)
- [Frequently Asked Questions (FAQ)](#FAQ)

# **Overview**

## **What is a Patient List Report?**

Use the Patient List Report to find patients who match specific criteria based on structured data in their charts. You can create detailed searches—for example, patients with certain diagnoses, medications, or lab results. Once you've generated a list, you can export it as an Excel-compatible spreadsheet for further analysis.

To access demographic information, you can also download a complete list of all your patients' addresses, phone numbers, insurance details, and more at any time.

## **Why is the Patient List Report useful?**

The Patient List Report is a great tool for tracking, outreach and analysis.

- **Patient outreach** - Generate contact lists for preventive care reminders or appointment recalls.
- **Population health management** - Identify patients due for screenings, immunizations, or chronic condition management (e.g., diabetic patients overdue for A1c tests).

See the [Sample Reports](#SampleReports) section to get a better idea of the kinds of reports you can run.

# **Workflow Instructions**

## **Generating a Patient List Report**

| | |
| --- | --- |
| **1** | Click the **Reports** button in the blue navigation bar. |
| **2** | Click **Patient List**. |
| **3** | Filter for patients using the [Quick Views](#quick_views) feature or individual filters (see below). |
| **4** | Click Generate List when you have selected all of your views or filters. |

The results of all the patients who match the criteria will appear in the report. The results page will only display a summarized list of patient details. See the [Patient List result contents](#view_reports) section for more information.

You can generate a report of your entire patient panel by leaving everything blank and clicking Generate List.

### **Using Quick Views**

The Quick Views feature allows you to apply preset filters to your report criteria, making it faster and easier to generate reports. Once a Quick View is selected, the report will generate automatically.

The Quick Views available are:

- **Initial Medicare AWV eligibility**
 - Identifies patients that turned 65 years old within the last 12 months who don't have any of the following CPT Codes in their chart:
    - G0402
    - G0438
    - G0439
    - G0468
    - G0498
- **Subsequent Medicare AWV eligibility**
 - Identifies patients who are 65 or older and have a CPT code G0438 documented in their chart, but do not have a G0439 CPT code.

Once you have identified the patients who are due for their Medicare Annual Wellness Visit, your staff can contact each patient to ask them to schedule an appointment. Apply additional filters on top of the Quick View filters for additional filtering as needed (e.g. **Patient Status**).

## **Using filters**

Each filter criteria has its own customization options. We recommended exploring each filter to understand the available options.

- General filters are based on specific characteristics.
- Demographics filters are based on data stored in the patient's demographics.
- The Clinical Data filters let you narrow down your patient list based on structured clinical data documented in the chart—such as diagnoses, medications, labs, and more.
 - The matches **all**/**any** filter lets you apply conditional logic across the Clinical Data filters.
 - Individual filters have their own options such **include**/**doesn’t include** a specific data point.

See the [Sample Reports](#SampleReports) below for live use-cases for the different filters.

#### **Available filters**

- **Provider** - patients of a specific provider in the practice, or patients of the entire practice
 - Patients are classified as 'belonging' to a given provider if that provider is listed as their Provider assigned in practice in their demographics.
- General Filters
 - **Last Seen (Last Signed Visit Note)** -
    - Search for patients with signed visit notes within a specific timeframe.
 - **Patient Passport** **Status**
    - *Registered user*=Patients who have an active [Elation Patient Passport](elation-patient-passport-an-introduction.md) account.
    - *Invited, not registered* = Patients who have been invited to Passport, but have not yet signed up.
    - *Not invited*=Patients who have not been invited to Passport.
 - **Order Status**
    - *Outstanding*
    - *Cancelled*
    - *Fulfilled*
 - **Order Hold Status**
    - *On hold*
      - Search for patients with [held lab orders](Order-Forms-Guide-Putting-lab-orders-on-hold-for-specimen-collection.md).
 - **Auto-Created Charts**
    - Search for charts that were automatically created via the Booking Site or third party integrations such as labs or refill requests.
- Demographics
 - **Age**
    - Search for patients older than, younger than or between certain ages.
    - Search for patients that turn a specific age within a certain number of months.
 - **Sex at Birth**
    - Search for patients of a specific gender.
 - **Race**
    - Search for patients of a specific race.
 - **Ethnicity**
    - Search for patients of a specific ethnicity.
 - **Preferred Language**
    - Search for patients based on a specific language preference.
 - **Preferred Contact Method​**
    - Search for patients based on a specific preferred contact method.
 - **Patient Status**
    - Search for patients based on their [chart status](Patient-Status.md).
 - **State**
    - Search for patients based on the State recorded in their address.
- Clinical Data
 - **Risk Score**
    - Search for patients with a [HCC Risk Score](how-to-use-elations-risk-assessment-feature.md) above, below, or between a certain number.
 - **Most Recent Lab Results**
    - Search for patients with/without a specific range of values for Hemoglobin A1c, Total Cholesterol, LDL-Cholesterol, HDL-Cholesterol, and Triglycerides
    - This filter only applies for patient charts that have structured lab values, that is, lab values imported electronically into the chart or recorded via the [Structured Labs](record-structured-data-from-in-house-or-faxed-lab-reports.md) or [Point-of-Care Labs](point-of-care-labs.md) features.
 - **Active Problems in Clinical Profile**
    - Search for patient with/without specific *Active* problems in their [Problem List](managing-your-problem-list.md).
    - Enter the name or ICD-10 code.
 - **Permanent Medications in Clinical Profile**
    - Search for patients with/without a specific medications listed in their active [Medication List](medication-history.md).
 - **Active Allergies in Clinical Profile**
    - Search for patients with/without specific active allergies.
 - **Vaccinations in Clinical Profile**
    - Search for patients with/without specific [Vaccinations](Vaccination-Form-Guide.md).
 - **Patient Tags**
    - Search for patients with/without specific [Patient Tags](adding-patient-tags.md) on their charts.
 - **Document Tags**
    - Search for patients with/without specific [tags for Visit Notes & Reports](tag-reports-and-notes-with-document-tags.md) in their chart records.
 - **CPT Codes**
    - Search for patients with/without [specific CPT Codes documented in their Visit Note Billing Information](billing.md) within a specific timeframe.

####

## **Viewing Patient List Report contents**

### **Viewing the report summary**

The results of all the patients who match the criteria will appear on the page. You will find the search criteria applied and the number of qualifying patients displayed as well.


Each patient that matches your search criteria will appear with the following information:

- Patient Name: Legal first name, Middle Name, Legal last name
- HCC Score
- Date of Birth / Age
- Gender
- Preferred Contact Method
- Contact (based on Preferred Contact Method)
- Last Appointment (last signed visit note)
- Next Appointment

You can sort the Patient List report by Name, HCC Score, Date of Birth / Age, Gender or Preferred Contact Method by clicking the column headers. Clicking the patient's name will open the patient's chart.

### **Viewing the detailed report as a spreadsheet (CSV)**

To view a more detailed report of your results, click **Download** -> **Download CSV** to save the list as an Excel-compatible file to your computer. From there, you can open the file in spreadsheet software like Excel to apply advanced sorting, filtering, or analysis as needed.

The spreadsheet that is exported contains the following information:

- First Name
- Middle Name
- Last Name
- Date of Birth
- Gender
- SSN
- Address information
- Phone Numbers
- Email
- Preferred Pharmacies
- Preferred Contact Method
- Provider assigned in practice
- Primary and Secondary Insurance Information
- Race. Ethnicity, and Language Preference
- Any Demographic Notes
- Last Appointment
- Next Appointment
- Passport Status
- Whether or not the Patient qualifies for a [Passport Invitation](https://help.elationemr.com/s/article/elation-patient-passport-an-introduction#HowToGetStarted)
- HCC Score

## **Exporting charts as C-CDA files**

You can export a list of patients as C-CDA (CCDA) files to securely share clinical data with other collaborating providers who are also using an electronic health record system. Read our [Patient Chart Guide- Sharing clinical care summaries with collaborating providers using C-CDA (CCDA) format](Supported-Elation-CCDA-types.md) article to learn more about this feature.

# **Sample Reports**

## **Patients who are due for an annual wellness visit**

You can use the [Quick Views](#quick_views) feature to search for patients who are due for their Medicare Annual Wellness Visit. Once you have identified the patients who are due for the exam, your staff can contact each patient to ask them to schedule an appointment.

The Quick Views available are:

- **Initial Medicare AWV eligibility**
 - Identifies patients that turned 65 years old within the last 12 months who don't have any of the following CPT Codes in their chart:
    - G0402
    - G0438
    - G0439
    - G0468
    - G0498
- **Subsequent Medicare AWV eligibility**
 - Identifies patients who are 65 or older and have a CPT code G0438 documented in their chart, but do not have a G0439 CPT code.

## **Patients who are due for a flu vaccine**

You can use the date of the patient's last encounter and clinical documentation in the patient's chart to identify a list of patients who have not received a flu vaccine during the current flu season by applying the following filters. Once you have identified the patients who need a flu vaccine, your staff can contact each patient to ask them to schedule an appointment to be vaccinated.

1. **Last Seen (Last Signed Visit Note)** *= Before* "10/1/2025"
2. **Vaccinations in Clinical Profile** *Doesn't include* "influenza"

####

## **Active patients with diabetes who need follow-up on their HbA1c levels**

You can use a combination of **Patient Status** and clinical documentation to identify a list of active patients who are diabetic and need to have their Hemoglobin A1c levels monitored by applying the following filters. Once you have identified the patients, you can send an order to the lab for each patient to get tested.

1. **Patient Status** *Active*
2. **Most Recent Lab Results** where *Hgb A1c >* "9"
3. **Active Problems in Clinical Profile** *includes* "diabetes"

# **Frequently Asked Questions**

#### **Can I add my own Quick Views?**

You cannot add your own Quick Views.

#### **Can I add my own filters?**

You cannot add your own filters.

#### **Can I apply conditional logic to my searches?**

The conditional logic options are limited to what you currently see in the Clinical Data criteria section.

**Next Step**

**Run a Patient List Report and start managing your patient panel today!**

# **Related Articles**

- [List of all Elation Administrative Reports](https://help.elationemr.com/s/topic/0TO1G000000LRD0WAO/practice-reports)
- [Bulk Letter Guide- Mass communication with Patients](introduction-to-bulk-letters.md)
- [Patient Chart Guide- Sharing clinical care summaries with collaborating providers using C-CDA (CCDA) format](Supported-Elation-CCDA-types.md)