# Data Migration Guide- Transferring your data from your legacy EHR into Elation

Source: https://help.elationhealth.com/s/article/Transferring-your-data-from-your-legacy-EHR-into-Elation

---

# **Contents**

- [Overview](#Overview)
 - [What is data migration ?](#description)
 - [What are the benefits of transferring data from your legacy EHR into Elation?](#value)
 - [How do you transfer data from your legacy EHR into Elation?](#transfer_options)
- [Migration Details & Instructions](#instructions)
 - [Elation’s complimentary data migration](#complimentary_migration)
    - [Step 1: Inquire how to export data from your legacy EHR](#export_for_complimentary_migration)
    - [Step 2: Export and share data from your legacy EHR with Elation](#share_data_with_Elation)
    - [Step 3: Request a full data export from your legacy EHR](#request_full_export)
 - [‘Just-in-time’ manual migration](#manual_migration)
    - [Step 1: Inquire how to export data from your legacy EHR](#export_for_manual_migration)
    - [Step 2: Import records on a rolling basis](#import_records_manually)

# **Overview**

## **What is data migration?**

Data migration is the process of transferring patient data from one EHR system to another EHR system.


## **What are the benefits of transferring data from your legacy EHR into Elation?**

Transferring your patient data from your legacy EHR into Elation has the following benefits:

- You can use historical data to build your Elation patient charts.
- You will not need to reference patient data in multiple locations because all your patient’s data will be available in your patient’s chart in Elation.

## **How do you transfer data from your legacy EHR into Elation?**

There are two options for transferring your data from your legacy EHR into Elation. Practices are encouraged to pursue both options if possible to maximize the amount of data that can be moved into Elation.

1. Elation’s complimentary data migration - Elation performs one import of each of the following data types as long as as the data meets our specifications:
   - Demographics
   - Appointments
   - CCDAs
2. ‘Just-in-time’ manual migration - you manually move your data into Elation as patients are about to be seen in the office

# **Migration Details & Instructions**

## **Elation’s complimentary data migration**

Elation can perform one complimentary import of each of the following data types if the data meets our specifications.

- Demographics
- Appointments
- CCDAs


These bulk imports can save you time and ensure you have the historical data you need by go-live to start seeing patients. If you would like Elation to perform a bulk import of any of the below data types, please follow the instructions below to request your data from your legacy EHR and send it to Elation.

Reference the table below for more details about each data type.

| Data Type | Supported Formats | What kind of data does this import add to Elation? | What is required of the customer? | When is the data imported? |
| --- | --- | --- | --- | --- |
| Demographics | .csv, .xls, .xlsx, .txt | Patient demographics and Insurance | Send data in the supported format to Elation | 5 days prior to your ‘go-live’ (i.e your first day charting on Elation |
| Appointments | .csv, .xls, .xlsx, .txt | Appointment Date & Time,  Duration, Provider Scheduled, Description, Appointment Status |
| CCDAs | .xml | Discrete elements: Basic Demographics, Allergies, Problems, Immunizations, Medications    All other data from the CCDA is stored as a read-only file in the patient’s chart. |




### **Step 1: Inquire how to export data from your legacy EHR**

1. Ask your legacy EHR the following questions to understand what options they offer for requesting your data in bulk.
   - How do I obtain demographics for all of my patients into a spreadsheet file?  Can I generate this file from the EHR myself?
   - How do I obtain CCDA files for all of my patients? Will I be able to export CCDA files in bulk or will I need to export for one patient at a time?
   - How do I obtain future appointments into a spreadsheet file? Can I generate this file from the EHR myself?
   - How do I export a copy of all of my patient charts? What type of records are included in this export and what format(s) do they come in? Can I export patient charts in bulk or will I need to export for one patient at a time?
   - How long does it take to perform each of the 4 exports mentioned above?
2. Once you have and understand the answer to the questions above, share the details with your Elation Engagement Advisor.

### **Step 2: Export and share data from your legacy EHR with Elation**

5 days prior to your Elation ‘go live’:

1. Export the **demographics**, **CCDAs** and **appointments** data from your legacy EHR.
2. Send the files to Elation through a secure URL that is provided by your Elation Engagement Advisor.


Elation’s team will review the data and, barring any issues, will import into your account by your ‘go live’.

- **Important Note**: If we find quality issues with your legacy EHR data, your migration timeline and ‘go live’ date may be affected.

### **Step 3: Request a full data export from your legacy EHR**

Besides exporting your demographics, CCDA, and appointment exports, you will need to request a **full data export** from your legacy EHR for record-keeping purposes. Wait until you ‘go-live’ and start seeing patients using Elation to make this request.

- **Important Note**: Data that you receive through this full export will not be imported into Elation by Elation’s team. If you wish to bring any additional data into Elation, you’ll need to use the [‘just-in-time’ manual migration process](#manual_migration).

## **‘Just-in-time’ manual migration**

With the ‘Just-in-time’ migration method, you or a member of your practice manually adds data into Elation as patients are about to be seen. This method gives you complete control over the timing and outcome of your data import and allows you to exclude data for inactive patients.


### **Step 1: Inquire how to export data from your legacy EHR**

Ask your legacy EHR the following questions to understand what options they offer for exporting your data in bulk. This helps expedite your data transfer workflows.

- How do I export a copy of all of my patient charts? What type of records are included in this export and what format(s) do they come in?
- How long does it take to perform a chart export?
- Can I export patient charts in bulk or will I need to export this data for one patient at a time?

### **Step 2: Import records on a rolling basis**

Prior to a patient’s appointment, [follow these linked instructions to manually upload data to your patient’s chart](https://help.elationemr.com/s/article/filing-documents-to-a-patient-chart) in Elation.

We typically see practices upload the following records but you can transfer as much data as you deem fit:

- Last visit note
- Most recent lab results

# **Related Articles**

- [Patient Chart Guide- Uploading documents directly within the patient's chart](https://help.elationemr.com/s/article/filing-documents-to-a-patient-chart)
- [Patient Chart Guide- Importing patient information from another EHR (CCD/CCDA Format)](https://help.elationemr.com/s/article/import-patient-information-from-another-ehr-c-cda-format)