# Billing Home Guide- A dashboard for managing your bills

Source: https://help.elationhealth.com/s/article/Billing-Home

---

## **Contents**

- [What is Billing Home?](#description)
- [Why is Billing Home useful?](#value)
- [How to access Billing Home](#access)
- [How to use Billing Home](#how_to_use)
 - [General layout](#general_layout)
 - [Using filters](#using_filters)
 - [Actions Menu](#actions_menu)
 - [Editing the Patient payment or Billing notes fields](#patient_payment_and_billing_notes)
 - [Practice Management System (PMS) Integration users](#PMS_users)
    - [Example of the journey of a bill for PMS users](#bill_journey_PMS_Users)
    - [Best Practices for PMS users](#best_practices_for_PMS)
    - [Additional Billing Settings for PMS users](#additional_settings)
- [How to print a report of my bills](#print_report)
- [How to download a report of my bills](#download_report)
- [Common use cases](#common_use_cases)
 - [Following up on incomplete bills](#incomplete_bills)
 - [Worklist for generating claims](#generating_claims)
 - [Following up on unbilled claims](#unbilled_claims)
 - [Get yearly totals for each CPT code](#yearly_cpt_totals)
- [Frequently Asked Questions (FAQ)](#FAQ)

##

##

## **What is Billing Home?**

Billing Home is an enhanced redesign of the Billing Report. Billing Home shows you all the visit notes tied to patient encounters as well as their associated billing details. The new Billing Home allows you to monitor and update your bills, just like the Billing Report, with added new functionalities such as additional filtering options and a better layout.

**Important Note**: [Information on the Billing Report is available here](https://help.elationhealth.com/s/article/billing-report).

## **Why is Billing Home useful?**

The layout of Billing Home is designed to allow for easy scanning of bill information. The new grid layout for the dashboard adds predictability for where you can expect to find certain details. Each row is one bill and you can easily scroll through the dashboard to find the specific detail you are looking for. Quick filters allow you to easily access bills that correlate to common billing workflows. You can also use our custom filters for more advanced workflow.

## **How to access Billing Home**

Click on the “Billing Home” option under “Reports” in the blue navigation bar at the top of any page in Elation to access Billing Home.

## **How to use Billing Home**

### **General Layout**

The layout of Billing Home is designed for easy access to information. Each page of the dashboard will show up to 25 bills based on the filters selected. Here is a breakdown of the layout:

1. Quick Filters - See the bills tied to specific statuses with the click of a button.
2. Customer Filters - Apply your own custom filters for bill details. See the [Using Filters](#using_filters) section below for more details.
3. A column for each bill detail

| Column Name | Description |
| --- | --- |
| **Date of service** | Shows the date of the visit note tied to the bill. |
| **Patient** | Shows the name and date of birth of the patient. *\*The name and date of birth will not display for [VIP patients](https://help.elationemr.com/s/article/vip-chart-feature). You will only see the Patient ID.* |
| **Status** | See the [Custom Filters](#using_filters) section below for more details. |
| **Provider** | If you are a Provider Level User, the dashboard will default to only showing your bills. Use the **Providers** filter to see bills of other Providers in your practice if needed. If you are a Staff Level User, the dashboard will default to showing bills for all Providers. Use the **Providers** filter to see bills of specific Providers only if needed. |
| **Service location** | Shows the Service Location ([Practice Location](https://app.elationemr.com/settings/practice-locations/)) tied to the bill. |
| **POS** | Shows the place of service code tied to the bill. |
| **Billing ref #** | You can type your own billing reference number (ie. a Claim #) when choosing to manually “Mark as Billed”. *\*If you are using a PMS integration that responds with confirmation of receiving the claim, the reference number will display here.* |
| **Primary insurance** | Shows the patient’s Insurance and Plan Name, Group ID and Member ID |
| **Secondary insurance** | Shows the patient’s Insurance and Plan Name, Group ID and Member ID |
| **Codes** | Displays all procedural and diagnostic codes, including modifiers. **User Tip**: Enable the [Billing Guidance feature](billing-settings---service-locations--procedure-codes.md#billing_guidance) to ensure codes are always added to your bills prior to signing your Visit Note. *\*If you are using Elation's* [*Risk Assessment*](https://help.elationemr.com/s/article/how-to-use-elations-risk-assessment-feature) *feature, you will also see the risk score of ICD-10 codes.* |
| **Charges**, **Quantity**, and **Total** | Displays the charge, quantity and total amount tied to the procedures in the bill. *\*Only for customers using the [Patient Invoicing feature](https://help.elationemr.com/s/article/patient-invoicing).* |
| **Patient Payment** | For customers to record payment received from the patient.  *\*This field is not linked to the [Patient Payment feature powered by Stripe](https://help.elationemr.com/s/article/using-elation-to-securely-collect-patient-payments).* |
| **Billing Notes** | |

1. A single row for each bill
2. Additional actions you can take for specific bills. [See the Actions Menu section below for more details](#actions_menu).
3. Scroll bars for easy navigation
4. Page arrows for navigating across multiple pages of bills (25 bills per page)
5. “Edit Columns” button for customizing the Billing Home column headers
   - Select "Compact View" if you want to minimize the white space in each bill line.
   - Select the columns you wish to display in the Billing Home by checking off the corresponding column names.
   - Rearrange the order in which each column appears as needed.
   - The “Actions” button, **Date of service**column and **Patient** column are always On and pinned by default.
6. “Print filtered results” for printing the data you filtered for
7. “Download filtered results” button for downloading the data you filtered for
8. “Switch to old Billing Report” button for users who want to return to the previous version of the Billing Report
9. “Bulk Send Bills to PMS” button *(\*only available for customers with PMS Integrations. [See below.](#PMS_users))*

### **Using Filters**

1. Quick Filters - These buttons allow you to see the bills tied to specific statuses with the click of a button.
2. Customer Filters - You can now apply your own custom filters for the following bill details:
   1. **Visit dates** - Filter by predefined date ranges or a custom date range of your choice. The default is 'Last 7 Days'.
   2. **Status** - Filter for claims by specific statuses. Reference the following chart for more information:

| Previous Status Name | New Status Name | Description |
| --- | --- | --- |
| ------------------------------ | **No bill** | Visit notes without any billing information |
| Unbilled | **Awaiting Sign Off** | Unsigned visit notes with billing information |
| Unbilled | **Signed** | Signed visit notes with billing information |
| Billed Manually | **Mark as Billed** | Someone in the practice used the “Mark as Billed” action to manually update the status of the bill. |

1. **Providers** - Filter for bills signed by specific providers.
   - If you are a Provider Level User, the dashboard will default to only showing your bills. Use the Providers filter to see bills of other Providers in your practice if needed.
   - If you are a Staff Level User, the dashboard will default to showing bills for all Providers. Use the Providers filter to see bills of specific Providers only if needed.
   - The filter will also allow you to search for bills tied to deactivated Providers.
2. **Service location** - Filter by the Service Location ([Practice Location](https://app.elationemr.com/settings/practice-locations/)) selected for the bill (including deactivated Service Locations).
3. **Place of service (POS)** - Filter by the Place of Service selected for the bill.
4. **Primary Insurance** - Filter by the Primary Insurance company listed in the patient's demographics.

### **Editing the Patient payment or Billing notes fields**

You can click into the **Patient payment** or **Billing notes** field of any bill in Billing Home to add information directly into those fields. Any data entered into the **Patient payment** or **Billing notes** field will automatically save once you click away from the field.

### **Actions Menu**

Depending on the status of your bill, you may see one or more of the following actions you can take when clicking on the Actions Menu button ![]():

| Action | Description | Only available for the following statuses |
| --- | --- | --- |
| Add Bill | Opens the billing window in the Billing Home | **No bill** |
| Open Bill | Opens the billing window in the Billing Home | **Awaiting Sign Off** |
| Open Visit Note | Opens the patient’s chart and visit note draft | All statuses |
| Mark as Billed | Marks the status of the bill as ‘Billed’ and allows you to enter a Billing Reference # | **Awaiting Sign Off** and **Signed** |
| Edit Billing Ref. # | Allows you to edit the stored Billing Reference # | **Marked as billed** |
| View Bill History | Shows the history of status changes on a bill and displays the date of the change *(\*For PMS integration users, if a bill fails to be sent to your PMS and an error message is provided to us by your integrated PMS, we will display the error message in the Bill History log.)* | All statuses except **No bill** |
| Send to PMS | Pushes the bill to your integrated PMS. *(\*Only available for customers with PMS Integrations)* | **Signed** |
| Resend to PMS | Re-pushes the bill to your integrated PMS *(\*Only available for customers with PMS Integrations)* | **Sent to PMS** and **Failed to send** |

### **Practice Management System (PMS) Integration users**

If you use a Practice Management System (PMS) Integration alongside Elation, you will see clearer filters, statuses and actions that detail or drive the synchronization of bills from Elation to your integrated PMS.

- Filters & Statuses

| Previous Status Name | New Status Name | Description |
| --- | --- | --- |
| Pushed | Sent to PMS | Bill sent to PMS |
| Pushed | Failed to Send | Bill sent to PMS and PMS sent notice of a failure to receive |
| Billed | Received by PMS | Bill sent to PMS and PMS confirmed receipt |

- Sent & Received details
 - Underneath the Sent to PMS and Received by PMS statuses you will see a date and time indicator of when the bill was sent to or received by your integrated PMS
- “Bulk Send Bills to PMS”
 - Go to the *[Additional Billing Settings](#additional_settings)* section of this article to learn more about configuring this Setting.
 - When enabled in your Billing Settings, the “Bulk Send Bills to PMS” button at the top of the dashboard will allow you to send all bills of a specific status to your integrated PMS.
    - If you have applied additional filters to the Billing Home, click "Send ... filtered bills" if you want to only send filtered bills to your PMS.
 - The following actions can be made available when enabling this button:
    - ”Send all **Signed**” - allows you to send all bills in the **Signed** status to your integrated PMS. If you have applied additional filters to the Billing Home then only filtered bills in the **Signed** status will be sent to your integrated PMS.
    - ”Resend all **Sent to PMS**” - allows you to send all bills in the **Sent to PMS** status to your integrated PMS. If you have applied additional filters to the Billing Home then only filtered bills in the **Sent to PMS** status will be sent to your integrated PMS.
    - ”Resend all **Failed to send**” - allows you to send all bills in the **Failed to Send** status to your integrated PMS. If you have applied additional filters to the Billing Home then only filtered bills in the **Failed to Send** status will be sent to your integrated PMS.
- “Send to PMS” and “Resend to PMS” actions
 - In the Actions Menu ![]() next to each bill, you can send or resend individual bills to your integrated PMS by clicking “Send to PMS” or “Resend to PMS”

**Important Note**: Consult the User Manual for your integrated PMS for full details on how to push bills from Elation to your integrated PMS.

#### **Example of the journey of a bill for PMS users**

#### **Best Practices for PMS users**

When Elation pushes a bill to your PMS the bill will be placed in the Sent to PMS status. This does not mean that the PMS received your bill as not all PMS integrations notify Elation when they successfully receive a bill or if they fail to receive a bill. Consult your PMS Integration Manual for full details on what kind of statuses your PMS integration supports.

- PMS Integrations that support a confirmation of receipt will place the bill in the Received by PMS status and return a billing reference number which Elation will store in the **Billing ref #** field.
- PMS integrations that support a failed receipt notification will place the bill in the Failed to Send status. Failed bills will also appear in the Requiring Actions queue for Providers to review.

For bills in the Sent to PMS status, always review the claim in your PMS to understand and correct potential errors. After corrective measures are taken to update the bill in Elation, practices should choose to resend the bill to the PMS.

**Important Note**: Consult your PMS Integration Manual for full details on what kind of statuses your PMS integration supports and what actions you can take for bills in Elation.

#### **Additional Billing Settings for PMS users**

The **Billing Home - Bulk Send to PMS** setting in your [*Billing* Settings](billing-settings---service-locations--procedure-codes.md) will allow you to enable or disable the “Bulk Send Bills to PMS” button in Billing Home. When toggled on, the “Bulk Send Bills to PMS” button allows you to bulk send filtered bills or all bills of a specific status to your integrated PMS. When toggled off the “Bulk Send Bills to PMS” button will not be available and each bill will need to be sent one by one to your integrated PMS via the Actions Menu ![](). Note that bulk send actions impact ALL bills in the respective status you select.

You also have 3 options that you can configure along with the “Bulk Send Bills to PMS” button:

- Enable option to bulk send "Signed" bills
 - This Setting requires the ‘Delayed Bills’ setting to also be enabled in your Billing Settings. A ”Send all **Signed**” action will be available under “Bulk Send Bills to PMS” to allow you to send all bills in the **Signed** status to your integrated PMS.
- Enable option to bulk resend "Failed to Send" bills
 - A ”Resend all **Failed to send**” action will be available under “Bulk Send Bills to PMS” to allow you to send all bills in the **Failed to Send** status to your integrated PMS.
- Enable option to bulk resend "Sent to PMS" bills
 - A ”Resend all **Sent to PMS**” action will be available under “Bulk Send Bills to PMS” to allow you to send all bills in the **Sent to PMS** status to your integrated PMS.

**How to print a report of my bills** To print a copy of the bills displayed (filtered view), click on the "Print filtered bills" button ![]() at the top of Billing Home. The printed report will separate the filtered bills by the status of the bill.

## **How to download a report of my bills**

To download a copy of the bills displayed (filtered view), click on the "Download filtered bills" button ![]() at the top of Billing Home.

- **User Tip**: Patient Tags will be visible in the downloaded report. You can filter for bills based on tags you add to the patient. [Learn more about the Patient Tags feature here](https://help.elationemr.com/s/article/adding-patient-tags).

## **Common use cases**

### **Following up on incomplete bills**

Billing Home can be used to follow up on incomplete bills to make sure coding is complete before generating a claim for services rendered. You can use the following Quick Filters to quickly view all your incomplete bills:

- **No Bill**
- **Awaiting Sign Off**

You can also use the **Service location** and **Place of service (POS)** Custom Filters to make sure you are entering the correct service location and Place of Service Code for your claim.

### **Worklist for generating claims**

Billing Home can be used by a biller to make sure a bill is submitted to the Payer for processing. Billers can use the **Signed** Quick Filter to view all the signed bills and create claims from the details listed for each bill. Once a claim is sent, they can click on the Actions Menu ![]() next to the bill and click the “Mark as Billed” button to enter a billing reference number (ex. Claim #) for that bill. This allows for quick referencing and follow up between Elation and your billing system.

### **Following up on unbilled claims**

Billing Home can be used to follow up unbilled claims to make sure a bill is submitted to the Payer for processing. You can use the **Signed** Quick Filter to view all your signed bills and then look at the **Billing ref. #** column to see which bill is missing a billing reference number. That claim could potentially be unprocessed.

### **Get yearly totals for each CPT code**

You can use Billing Home together with a spreadsheet software (e.g. Excel or Google Sheets) to get yearly totals by CPT code for your practice's accounting needs.

| | |
| --- | --- |
| 1 | **Open Billing Home** In Elation, go to Reports -> Billing Home. |
| 2 | **Set the date range to the desired year** Use the Visit dates filter to set a custom range for the full year you want to review (for example, Jan 1–Dec 31). |
| 3 | **Download the filtered results as a CSV** At the top of Billing Home, click Download filtered bills to export the filtered view of your bills. |
| 4 | **Create a pivot table in a spreadsheet software**   1. Open the CSV in a spreadsheet software (e.g. Excel or Google Sheets). 2. Insert a pivot table. 3. Configure the pivot:    - **Rows: CPT** **code** (and optionally description, if included in your export).    - **Values:** Count of rows to see how many times each **CPT code** was billed, and/or sum of charge amounts to see total dollars billed per **CPT code**.    - **Filters (optional):** Add **Date of Service**, **Provider**, **Service location**, or **Payer** if you want to further narrow the results. 4. This gives you a yearly CPT summary. |

#### **Use the same pattern for other summary questions**

You can repeat the same instructions — filter in **Billing Home** -> Download filtered bills -> Build a pivot table — to answer many other operational and accounting questions that require aggregate answers, such as:

1. **Totals by Provider** - Filter by the date range you care about in Billing Home, download the filtered CSV, then build a pivot table with **Provider** as rows and sum of charge amounts (and/or count of bills) as values.
2. **Totals by Payer** - Filter by Visit dates and insurance, download the filtered CSV, then pivot on your payer field (for example, **Primary Insurance**) as rows, with sum of charge amounts and/or count of bills as values.
3. **Monthly trends** - After downloading the CSV, derive a 'month' column from **Date of Service** and use it in the pivot table as rows or columns with sum of charge amounts as values to see volume and revenue trends across months in the same year.

## **Frequently Asked Questions (FAQ)** **Can I edit my bill details from the Billing Home?**

Yes, click on the Actions Menu ![]() next to the bill you want to edit and click “Add Bill” or “Open Bill” to edit the bill directly in Billing Home. This action is only available for bills in the **No bill** or **Awaiting Sign Off** statuses.

#### **Can I customize the quick filters available?**

The available Quick filters cannot be customized at this time. We will notify you if this feature becomes available in the future.

#### **Can I save frequently used filters?**

The ability to save commonly used filters is not available at this time. We will notify you if this feature becomes available in the future.

#### **Can I customize the columns available in the Billing Home?**

You can click the “Edit Columns” button ![]() to select which available columns you want displayed in the Billing Home for your entire practice. However, you cannot add columns that are not available.

#### **Can I set permissions around which users can take which actions?**

The ability to permissions around which users can take which actions is not available at this time. We will notify you if this feature becomes available in the future.

#### **Can I send bills from a specific date range to my integrated PMS?**

To send bills from a specific data range to your integrated PMS, use the date filter to filter by the date range you want to send and then click on the Actions Menu ![]() next to the bill and select "Send to PMS".

You can also bulk send bills from a specific date range to your integrated PMS if you click the "Bulk Send" button.

#### **Can I switch back to the old Billing Report view?**

Yes, you can switch back to the old Billing Report view by clicking the "Switch to old Billing Report" button.

Please tell us why you like the old layout more using the 'Send feedback' form under the "I need help" options.

## **Related Articles**

1. [Billing Guide- Billing Report](/s/article/billing-report)
2. [Billing Guide- Creating a Super Bill & coding for your visit](billing.md)
3. [Billing Guide- Navigating Billing Settings](billing-settings---service-locations--procedure-codes.md)
4. [Billing Guide- Frequently Asked Questions](Billing-Guide-Frequently-Asked-Questions.md)
5. [Practice Locations Guide- Listing your service locations](adding-a-second-practice-location.md)
6. [Billing Guide- Patient Invoicing- Generating invoices to patients for services rendered](patient-invoicing.md)
7. [Elation Billing- Using Elation's all-in-one billing solution to manage your claims](Elation-Billing-All-in-One.md)
8. [Patient Payments Guide- Securely collect payments digitally from patients](using-elation-to-securely-collect-patient-payments.md)
9. [Billing Guide- Delayed Billing](How-to-set-up-Delayed-Billing.md)