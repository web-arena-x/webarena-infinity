# Calendar Guide- Searching for appointments using the Appointment Report

Source: https://help.elationhealth.com/s/article/Calendar-Guide-Searching-for-appointments-with-the-Appointments

---

## **Contents**

- [What is an Appointment Report?](#description)
- [Use cases for an Appointment Report](#use_cases)
- [Generating an Appointment Report](#generate)
 - [Important Report Tips](#report_tips)
    - [Generating Appointment Reports With Future Dates](#future_report)
    - [Generating Appointment Reports- Time Constraints](#time_constraints)
    - [Custom Sorting in CSV Files](#custom_sort)

##

## **What is an Appointment Report?**

The Appointment Report feature in Elation allows you to generate a report of all of a practice's or provider's appointments as recorded in their Elation calendar within a given time frame. The report contents include:

- Appointment date & time
- Patient Full Name, Date of Birth & primary phone number
- Appointment type
- Appointment reason
- Appointment status
- Any patient payment information recorded
- Patient's insurance details

## **Use cases for an Appointment Report**

The Appointment Report is a good administrative report for tracking patient appointments over a period of time. Here are some common uses cases we have seen from various customers:

1. Generating a report to follow up on patients who are due for recurring visits (ex. annual exams, recurring procedures/tests, chronic conditions follows ups)
   - **User Tip**: We recommend consistent and detailed use of the *Appointment Type*, *Appointment Reason* & *Appointment Status* fields in order to yield the best results.
2. Generating a total amount for payments collected from patients at the end of the day to 'close out' your day
   - **User Tip**: Record any cash, check or other payments collected from patients in the *Pt Payment* field of the appointment. At the end of the day, use the *Appointment Report* for that day to make sure the total collected and the total recorded match.
3. Generating a report to understand business trends and patient needs
4. Generating a report for [a provider who is leaving the practice](User-Accounts-Guide-Best-practices-for-deactivating-accounts.md) to reassign appointments to an active provider.

## **Generating an Appointment Report**

To generate an Appointment Report, follow these steps:

1. Click "Reports" >> "Appointment Report" at the top of any page in Elation
   - By default, the Appointment Report will show your own appointments (if you are a provider level user) or the appointments of a staff member's default physician (if you are a staff level user)
   - By default, the report will show the appointments for the last 7 calendar days
2. Select "All Providers" or another provider's name if you would like to change the provider filter for the report
3. Select a different "From:" or "To:" to filter for a different time frame
4. Click "Update List" to update the report after changing any filters
5. Click the "Download List of Appointments as CSV" button if needed to download the Appointment Report as a CSV file and view the results in a spreadsheet software application where you have [advanced customization options](#custom_sort)

### **Important Report Tips**

#### **Generating Appointment Reports With Future Dates**

If you need to filter for a date in the future, type in the date manually in the MM/DD/YYYY format instead of using the Calendar picker
![]()

#### **Generating Appointment Reports- Time Constraints**

- If you filter for a timeframe that is greater than 14 calendar days, you will not be able to see the report contents in Elation. You will need to click the "Download List of Appointments as CSV" button to view the results in a spreadsheet software application.
- If you need to filter for a timeframe that is larger than 6 months, you will need to break up the time frame into multiple reports, download the reports to your computer as a CSV file and then combine the data in a spreadsheet software application. For example, if you would like to see all appointments from 2020, you will need to run 3 reports; each with the following time frames:
 - 01/01/2020 to 05/31/2020
 - 06/01/2020 to 10/31/2020
 - 11/01/2020 to 12/31/2020

#### **Custom Sorting In CSV Files**

- Downloading reports as CSV files allows you to further customize your report. CSV files can be viewed in spreadsheet software applications, such as Google Sheets and Microsoft Excel. You can use the advanced spreadsheet capabilities of these applications to best fit your practice’s needs. For example, to see an Appointment Report of “no show” appointments, you can sort the column of [appointment] “Type” in the spreadsheet application so that all “no show” appointments are grouped together.
- For specific instructions on how to sort columns in Microsoft Excel or Google Sheets, please reference these links below.
 - [Microsoft Excel](https://support.microsoft.com/en-us/office/sort-data-in-a-range-or-table-62d0b95d-2a90-4610-a6ae-2e545c4a4654#OfficeVersion=Windows)
 - [Google Sheets](https://support.google.com/docs/answer/3540681?hl=en&co=GENIE.Platform%3DDesktop)

## **Related Articles**

- [Patient Booking Site Guide](Patient-Booking-Site.md)
- [Calendar Guide- How to set up the provider calendar](calendar-and-booking-settings.md)
- [User Accounts Guide- Best practices for disabling accounts](User-Accounts-Guide-Best-practices-for-deactivating-accounts.md)