# Lab Orders & Results - Managing electronic lab results

Source: https://help.elationhealth.com/s/article/Viewing-results-from-lab-interfaces

---

# **Contents**

- [Overview](#Overview)
 - [What are electronic lab results in Elation?](#description)
 - [What are the benefits of receiving structured lab results in Elation?](#benefits)
 - [How can I receive electronic lab results in Elation?](#how_to_receive)
- [Set-up](#Set-up)
- [Workflow Instructions](#Workflow_Instructions)
 - [Receiving electronic lab results](#receive_results)
 - [Viewing electronic lab results in Elation](#view_results)
    - [Viewing electronic lab results on the Practice Home](#view_in_Practice_Home)
    - [Viewing electronic lab results in the patient’s chart](#view_in_patient_chart)
 - [Signing electronic lab results](#sign)
 - [Moving an electronic lab result to a different patient chart](#refile)
 - [Reassigning electronic lab results to a different Provider or Delegate](#reassign)
 - [Exporting lab results to visit notes](#export_to_note)
 - [Managing duplicate charts created when receiving electronic lab results](#duplicate_charts)
 - [Sharing electronic lab results with patients](#share)
- [Frequently Asked Questions (FAQ)](#FAQ)

# **Overview**

## **What are electronic lab results in Elation?**

Electronic lab results are test results that are formatted as individual data points, known as structured data. This structured test data is sent directly from the lab vendor to your patient charts in Elation through an interface.

## **What are the benefits of receiving structured lab results in Elation?**

Structured lab results:

- **Improve data accuracy** - Uses standardized vocabularies to eliminate transcription errors.
- **Enhance data organization** - Stores results in a standardized format, making it easier to review and trend over time.
- **Reduce paperwork** - Minimizes the need for faxed or printed reports, streamlining workflow efficiency.

## **How can I receive electronic lab results in Elation?**

Electronic lab results can be transmitted to Elation once a lab interface is activated for a lab vendor. Follow the [set-up steps below](#Set-up) to set up this type of interface for each of your lab vendors.

# **Set-up**

1. [Set up lab vendors (mandatory)](https://help.elationemr.com/s/article/Managing-lab-vendors)

# **Workflow Instructions**

## **Receiving electronic lab results**

Once an interface between your practice and a lab vendor is live, the lab vendor will automatically send lab results electronically to the patient’s chart.

Electronic lab results are routed to patient charts by matching first name, last name, date of birth, and sex at birth and assigned to the Ordering Provider for review and sign off. If the interface is unable to find an exact patient match, then it will automatically create a new patient chart in Elation to house the lab results.

By default, lab vendors will send the electronic report once all tests are finalized across a single lab panel or lab order, but you can ask a lab to send partial results if preferred.

##

## **Viewing electronic lab results in Elation**

View electronic lab results in any of the following places:

- In the Practice Home **Reports** inbox of the Ordering Provider if the report is unsigned.
- In the patient’s chart under **Requiring Action** if the report is unsigned.
- In the patient’s chart under the **Reports** -> **Lab** tab regardless of whether it's been signed.

### **Viewing electronic lab results on the Practice Home**

Unsigned electronic lab results will appear in the Practice Home **Reports** inbox of the Ordering Provider. Results are listed in order of your sort preferences, either **Oldest First** or **Newest First**. Reports with abnormal results will show the corresponding test names in red t (shown in the image below).

Click the patient's name to open their chart and view the full report.

### **Viewing electronic lab results in the patient’s chart**

Unsigned electronic lab results will appear in the **Requiring Action** section of the patient’s chart. You will see the following details in Requiring Action:

- The date of the report.
- The Provider or Delegate the report is assigned to.
- The date and time the results were collected.
- **Sign Off** options, including the options to sign off and attach the Report to a new Patient Letter or Provider Letter.

Click on the name of the report to open the full report view to see the following details:

- Report details:
 - **Requisition No.** - The unique lab order ID assigned by the lab vendor.
 - **Order by** - The name of the Provider that ordered the tests.
 - **Vendor** - The name of the lab vendor.
 - **Document Date** - The date of the report.
 - **File Received** - The date the report was transmitted to Elation.
 - **Collected** - The date the lab specimens were collected.
 - **Completed** - The date the test results were completed.
 - **Status** - The status of the results
 - **Accession No.** - The unique ID assigned to the lab specimens associated with the results.
- Test result details:
 - The test name and test value.
 - The last 3 values for the same test from previous results, if available.
 - Abnormal test results - Look for abnormal test results in red, bold text.
 - The reference range for the test - Position your cursor over the test value to see reference ranges, if available.
 - Any notes as shared by the lab.
- A PDF version of the report - Click the **Download PDF version of report** button at the bottom of a report to download a PDF version of the report. Only some lab vendors (e.g. Quest and Genova Diagnostics) send the PDF version of the report along with the electronic version. Consult your lab representative if you have any questions about this behavior.

## **Signing electronic lab results**

Any Provider Level User can sign off on any electronic lab results, even if the results are assigned to a different provider in the practice. Staff Level Users can sign off on electronic lab results if they were delegated sign off permissions. [Click here for instructions on how to reassign lab results to a Delegate](#reassign).

To sign off on electronic lab results:

| | |
| --- | --- |
| **1** | Locate the electronic lab result in the Practice Home or patient’s chart. |
| **2** | Click**Sign Off**. |

## **Moving an electronic lab result to a different patient chart**

To move an electronic lab result to a different patient’s chart:

| | |
| --- | --- |
| **1** | Locate the electronic lab result in the Practice Home or patient’s chart. |
| **2** | Click **Actions** -> **Refile to Other Patient Chart**. |
| **3** | Search for the patient’s chart by their name and then select their name from the search results. |
| **4** | Click **File**. |
| **5** | The report will now appear in the other patient chart. |

## **Reassigning electronic lab results to a different Provider or Delegate**

To reassign electronic lab results to a different Provider or Delegate for sign off:

| | |
| --- | --- |
| **1** | Locate the electronic lab result in the Practice Home or patient’s chart. |
| **2** | Click **Actions** -> **Reassign to Provider** or **Actions** -> **Reassign to Delegate**. |
| **3** | Search for and select the name of the Provider or Delegate you want to assign the report to. |
| **4** | Click **Assign**. |
| **5** | The report is now assigned to a new Provider or Delegate. |

## **Exporting lab results to visit notes**

To export lab results to a visit note:

| | |
| --- | --- |
| **1** | Open the lab report in **Reports** -> **Lab** window. |
| **2** | Use any of the workflows below based on what you’d like to export   1. To export a single test value, position your cursor over the test value and click **Actions** and choose one of the export locations. 2. To export all abnormal values, go to the bottom of the report and click **More Actions** -> **Reference All Abnormal Values in Note**. 3. To export multiple test values:    1. Click on the star next to each value you want to include.    2. Go to the bottom of the report and click **More Actions** -> **Reference All Starred in Note**. |

## **Managing duplicate charts created when receiving electronic lab results**

Electronic lab results are routed to patient charts by matching first name, last name, date of birth, and sex at birth. If the interface is unable to find an exact patient match, then it will automatically create a new patient chart in Elation to house the lab results. The new chart will show a pink banner at the top to indicate it was auto-generated by Elation. If you find that it’s a duplicate of an existing chart, you can merge it, along with the lab results, into the patient’s actual chart

[Click here for instructions on how to merge patient charts](https://help.elationemr.com/s/article/merging-duplicate-charts).

## **Sharing electronic lab results with patients**

Manually share electronic lab results with patients via their Patient Passport account. [Click here for instructions on how to manually send patients their lab results via a Patient Letter](https://help.elationemr.com/s/article/elation-patient-passport-an-introduction#attaching).

# **Frequently Asked Questions**

#### **How do I prevent electronic lab results from creating new patient charts for patients that do not belong to my practice?**

Sometimes lab vendors may accidentally send you a report for a patient that is not yours or send you a report for a patient that is no longer active in your practice.

If the interface is unable to find an exact match based on the patient’s first name, last name, date of birth, and sex at birth, then it will automatically create a new patient chart in Elation to house the lab results. This feature cannot be disabled.

If the patient has an existing chart then you can merge the charts together by following the instructions in [this article](https://help.elationemr.com/s/article/merging-duplicate-charts).

If the patient does not belong to your practice you can choose to delete the patient chart at your discretion.

# **Related Articles**

- [Lab Orders & Results Introduction](Lab-Orders-and-Results-Introduction.md)
- [Lab Orders & Results - Managing lab vendors](Managing-lab-vendors.md)
- [Lab Orders & Results - Using the electronic Lab Order Form](Electronic-Lab-Order-Form.md)
- [Practice Home Guide- Checking for requiring action items](check-for-your-offices-daily-to-do-list.md)
- [Chronological Record Search Guide- Searching for records in the patient's chart](using-the-search-tool-in-your-patient-chart.md)
- [Letters & Referrals Guide- Sending messages to patients & corresponding with third party professionals](how-to-send-a-fax.md)
- [Document Tags for Visit Notes & Reports Guide](tag-reports-and-notes-with-document-tags.md)
- [Patient List Report Guide- Searching your patient panel](find-patients-with-elations-patient-list.md)
- [Patient Chart Guide- Uploading documents directly within the patient's chart](filing-documents-to-a-patient-chart.md)