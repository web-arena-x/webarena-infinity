# Lab Orders & Results - Using the electronic Lab Order Form

Source: https://help.elationhealth.com/s/article/Quest-eOrdering-in-Elation

---

# **Contents**

- [Overview](#overview)
- [Workflow Instructions](#Workflow_Instructions)
 - [Creating a lab order](#create_lab_order)
 - [Transmitting the lab order](#transmit_lab_order)
    - [Transmitting the lab order electronically to the lab vendor](#transmit_lab_order_to_lab)
    - [Transmitting the lab order to a patient](#transmit_lab_order_to_patient)
 - [Printing specimen labels](#printing_specimen_labels)
 - [Printing a lab order](#printing_lab_order)
- [Resources](#Resources)
 - [Glossary of Lab Order Form fields and buttons](#Glossary)
- [Frequently Asked Questions (FAQ)](#FAQ)
 - [Lab Order Form Usage](#usage)
 - [Special Ordering Scenarios](#special_scenarios)
 - [Permissions](#permissions)

📖 **RECOMMENDED READING**

[Click here for a list of lab vendors that offer a bidirectional lab interface with Elation](https://www.elationhealth.com/integrations/?ucterms=partner_service:laboratories-bidirectional).

# **Overview**

Use this article to learn how to create and transmit lab orders if you have a  live bidirectional lab interface with the vendor, known as eOrdering.

Here is an example of what your electronic Lab Order Form looks like in this situation. The buttons that allow you to complete the order will include:

- **eOrder**
- **eOrder & Print**
- (if applicable) **Sign & Hold**

ℹ️ **NON-ELECTRONIC ORDERING** If you don’t have a bidirectional interface with the lab vendor that you wish to order from, [click here for instructions on how to create a regular Lab Order](https://help.elationemr.com/s/article/Regular-Lab-Order-Form).

📖 **MISSING A LAB?**

Only lab vendors with an active integration with your Elation account are available for electronic ordering in the Lab Order Form.

If a lab vendor you previously used no longer appears:

| | |
| --- | --- |
| **1** | Go to **Settings** → **Labs** and locate the lab vendor**.** |
| **2** | Check the **Electronic Orders? column** to confirm the interface status is **Live**. Any other status indicates the interface is not currently active. |
| **3** | If the lab vendor is missing from your list or the interface status has changed unexpectedly, follow the troubleshooting steps in [Managing lab vendors → Troubleshooting a lab or imaging interface that stopped working](Managing-lab-vendors.md#troubleshooting_interface). |

# **Workflow Instructions**

## **Creating a lab order**

| | |
| --- | --- |
| **1** | Create a Lab Order use any of the the following options:   1. At the top of the patient's chart, click Orders -> Lab Order. 2. In any visit note or non-visit note draft, click Lab. 3. In an existing signed Lab Order, click Actions -> Reorder to re-order the same test(s) as the signed Lab Order. |
| **2** | Fill out the Lab Order Form. Fields with an asterisk are required. The chart below explains the core fields in the form. Any vendor-specific eOrdering requirements are also highlighted. [Click here to see definitions for the remaining fields and buttons](#Glossary).   | | | | | --- | --- | --- | | **Field / Button** | **Instruction** | **Vendor Specific Requirements** | | \***Lab** | Select the vendor with whom you are placing the order.   - Use the [Labs Settings page](https://help.elationemr.com/s/article/labs-settings) to add additional vendors if needed.   **💡**  **USER TIP** Type the first few letters of the lab vendor's name to filter your list of lab vendors. | **Scarlet Health Requirements** Electronic lab orders for Scarlet Health are routed through the Bioreference lab interface. Choose Bioreference as the lab vendor when creating lab orders for Scarlet Health. | | **Site** | Designate whether the specimen will be collected at any vendor patient service center, a specific vendor patient service center, or in-house. If ‘Any site’ is selected, all patient service centers will receive your order.   - Additional location details can be set on the [Labs Settings page](https://help.elationemr.com/s/article/labs-settings), if needed. | | | \***Tests** | Enter the test(s) you want the patient to complete. You must select a test from the lab vendor’s proprietary compendium, which is maintained and updated monthly by the vendor. **💡**  **USER TIP** If you cannot find a test in the test search, search for the test using different terms (e.g. the Complete Metabolic Panel is known as "CMP" for Labcorp). If you have a question about a specific test or test code, please contact your lab representative for assistance. Custom tests and test codes are not supported for electronic orders. | **Scarlet Health Requirements** - Because Scarlet Health shares an interface with Bioreference, you must include the test "TH31-8" in any lab order that is intended for Scarlet Health. - Scarlet Health cannot handle specimens that are collected in-house by a healthcare provider or must be collected over an extended time period (e.g. stool specimens, pap smear and biopsy collections).   - Review each test in your Lab Order to make sure Scarlet Health can support the specimen collection requirements before sending the Lab Order to Scarlet Health.   - Instruct the ordering Provider to regularly check their email inbox for notifications from Scarlet Health regarding ineligible Lab Orders. | | **Add Dx** | If there are diagnoses that need to be associated with a specific test, use this field to add those diagnoses. Test-level diagnosis codes will take precedence over order-level diagnosis codes. | | | \***Dx for All** | Add diagnoses that are relevant to all the test(s) in the order. Order-level diagnosis codes are secondary to test-level diagnosis codes. **💡**  **USER TIP** If you've already entered diagnoses in the patient'sProblem List or visit note, these diagnoses will automatically appear in the dropdown menu for you to select. Use the [Problem List Guide](https://help.elationemr.com/s/article/managing-your-problem-list) to learn more about this feature. | | | **Coll** | **If you selected ‘Any site’ or 'a specific vendor patient service center for the Site**, optionally specify when the test should be performed in the **Schedule Collection** **Date** field. **If you selected ‘In-house draw’ for the Site**, specify the **Document Collection** date and time that the specimen collection was completed. [Click here to learn about placing a lab order on hold until specimens collection is completed](https://help.elationemr.com/s/article/Order-Forms-Guide-Putting-lab-orders-on-hold-for-specimen-collection). | | | \***Patient Condition** | Specify fasting requirements, if any, for the test(s). | | | **Bill Type** | Specify whom to bill for the lab test(s). As a best practice, ensure the patient's demographic and insurance details in the chart are as comprehensive as possible, as this information may be sent to the lab vendor along with the lab order, depending on the specified **Bill Type**. If you would like to specify a default **Bill Type** for all of your lab orders:   1. Go to **Settings** -> **Lab Orders**. 2. Go to the **Lab Order Settings** section. 3. Use the **Default Bill Type** dropdown to select the default bill type. Your selection will be automatically saved. | **Labcorp Requirements** - For Labcorp, the following insurance and demographics details must be included when eOrdering with Labcorp and the **Bill Type** is set to ‘Third Party’. - **Address** - **City** - **State** - **Zip** - **Guarantor - First name** - **Guarantor - Last name** - **Guarantor - Relationship** - **Guarantor - Address** - **Guarantor - City** - **Guarantor - State** - **Guarantor - Zip** - **Insurance - Carrier Name** - **Insurance - Carrier Address** - **Insurance - Carrier City** - **Insurance - Carrier State** - **Insurance - Carrier Zip** - **Insurance - Group ID** - **Insurance - Member ID** - **Coverage Type** **Quest Requirements** - For Quest, **Bill Type** must be specified and the following insurance and demographics details must be included when eOrdering with Quest Diagnostics and the **Bill Type** set to ‘Third Party’. - **Insurance - Carrier Name** - **Insurance - Carrier Address** - **Insurance - Carrier City** - **Insurance - Carrier State** - **Insurance - Carrier Zip** - **Insurance - Member ID** - **Primary Insurance Policyholder** (if not ‘Self’) - **Patient’s relation to policyholder** (if not ‘Self’) - **Primary Insurance Policyholder  - First name** (if not ‘Self’) - **Primary Insurance Policyholder  - Last name** (if not ‘Self’) | |
| **3** | Use any of the options below to sign the lab order:   - **eOrder** - **eOrder & Print** - (if applicable) **Sign & Hold** |

## **Transmitting the lab order**

### **Transmitting the lab order electronically to the lab vendor**

Clicking **eOrder** or **eOrder & Print** will immediately send lab orders electronically to the lab vendor. Afterwards, the signed order will be saved in the patient’s chart.

- The following information will be added to the signed lab order:
 - Date & time of the lab order - Stores the date and time the lab order was signed.
 - Signed by - Stores the name of Provider (and their delegate, if applicable) that signed the lab order.
- If any issues occur while sending the electronic order, a notification will appear in your **Requiring Action** queue.

ℹ️   **ON-HOLD ORDERS** If you click **Sign & Hold** to hold your order for specimen collection, then the lab order will not be sent to the interfaced lab vendor until a specimen collection date is documented. [Click here to learn about placing a lab order on hold until specimen collection is completed](https://help.elationemr.com/s/article/Order-Forms-Guide-Putting-lab-orders-on-hold-for-specimen-collection).

##

### **Transmitting the lab order to a patient**

Attach a signed lab order to a Patient Letter to send a copy of the lab order to the patient via Patient Passport. [Click here for full instructions](https://help.elationemr.com/s/article/elation-patient-passport-an-introduction#write_message).

## **Printing specimen labels**

To print specimen labels for the lab order:

1. Locate the order in the **Chronological Record** or under the **Reports** -> **Lab Reports** tab.
2. Click **Actions**
   - To [print labels with a Dymo printer](https://help.elationemr.com/s/article/Orders-Guide-DYMO-printer), select **Print DYMO Specimen Labels**.
   - To print labels at the bottom of a regular sheet of paper (compatible with Labcorp forms), select **Print Specimen Labels**.

Below is an example of specimen labels in a printed Labcorp order.

## **Printing a lab order**

To print a lab order (without specimen labels):

1. Locate the order in the **Chronological Record** or under the **Reports** -> **Lab Reports** tab.
2. Click **Actions** -> **Print**.

##

# **Resources**

## **Glossary of Lab Order Form fields and buttons**

| | |
| --- | --- |
| **Field / Button** | **Explanation** |
| **View Order Sets** | View and apply commonly used [Lab Order Sets](https://help.elationemr.com/s/article/Managing-lab-order-sets) to the lab order. Only vendor-specific order sets will be available for selection. |
| **Send STAT via Phone** | **This information will not be printed on the lab order or sent electronically to the lab vendor.** Reach out to the lab vendor separately to request results urgently. |
| **Send STAT via Fax** | **This information will not be printed on the lab order or sent electronically to the lab vendor.** Reach out to the lab vendor separately to request results urgently. |
| **Lab Requested Information** | Answer any test-specific ask-on-entry (AOE) questions that appear in the **Lab Requested Information** section after selecting a test. Any unanswered questions may prompt the lab to contact you for verification before the patient can proceed with the order. |
| **Show and print dual codes** | Show both ICD-9 and ICD-10 codes for selected diagnoses. |
| **Save as Order Set** | Save the tests, test-level diagnosis codes and order-level diagnosis codes listed as a new Order Set. |
| **Check Medicare Eligibility** | Click the **Check Medicare Eligibility** button that appears whenever ‘Third Party (e.g. Insurance)’ is selected as the **Bill Type** if you wish to verify Medicare coverage for the selected lab tests and diagnoses through the lab vendor’s Advanced Beneficiary Notice service. If the patient is not covered, the estimated test cost will be displayed, and a printable Advanced Beneficiary Notice (ABN) form will be generated for the patient to complete. |
| **Lab Instructions** | **This information is not transmitted in an eOrder.** Reach out to the lab vendor separately if you have any special instructions for them. |
| **Notify via** | **This information is not transmitted in an eOrder.** Add an internal note about how your practice should notify the patient about their lab results. |
| **Send a copy of test results to…** | List the name(s) of provider(s) to whom the lab vendor should send a copy of the results. ℹ️   **REMINDER** Labs are not obligated to share the results with the providers listed. This instruction is a courtesy request. |
| **St. Order** | **This information is not transmitted in an eOrder.** Reach out to the lab vendor separately if you wish to designate a standing order. |
| **RMDR** | **This information is not transmitted in an eOrder.** Specify who to send an Elation alert to if results are not received by a specified date. The **Reminder date** is the date the reminder will be sent. |
| **Keep this confidential** | **This information is not transmitted in an eOrder.** Check the **Keep this confidential** box to mark the order as a confidential record in the patient’s chart. **💡**  **USER TIP** If you mark a record as confidential, that record will always have a special indicator when this order is shown in the patient's chart. This indicator will prompt members of your practice to take caution when printing or sharing the record. Learn more about confidential records in the [Patient Chart Guide- Managing confidential records](https://elation.lightning.force.com/articles/Knowledge/confidential-items-in-your-patient-chart) article. |
| **eOrder** | Send the lab order electronically to the lab vendor immediately. |
| **eOrder & Print** | Send the lab order electronically to the lab vendor immediately and then print the lab order. |
| **Sign & Hold** | Simultaneously sign the lab order and put the lab order on hold. This option will only be active if you selected ‘in-house labs’ for the Site and left the **Document collection** date blank. The lab order will not be sent to the lab vendor until the Document collection date is documented. [Click here to learn about placing a lab order on hold until specimen collection is completed](https://help.elationemr.com/s/article/Order-Forms-Guide-Putting-lab-orders-on-hold-for-specimen-collection). |
| **Save as Draft** | Save the lab order as a draft and close the lab order window. The lab order draft will remain in the **Requiring Action** section of the patient’s chart until it is signed or discarded. |
| **Discard** | Delete the lab order draft. |
| **X** | Save the lab order as a draft and close the lab order window. The lab order draft will remain in the **Requiring Action** section of the patient’s chart until it is signed or discarded. |

# **Frequently Asked Questions**

## **Lab Order Form Usage**

#### **How many lab tests can I add to a single lab order?**

You can add up to 40 lab tests per lab order.

#### **How many diagnosis codes can I add to a single lab order?**

You can add up to 120 unique diagnosis codes per lab order.

####

####

#### **Do I need to add a test-level diagnosis code to every test in the lab order?**

No, adding a test-level diagnosis code to every test in the lab order is not required. Tests without a test-level diagnosis code will automatically be linked to the order-level diagnosis codes.

#### **Do I need to add order-level diagnosis codes to a lab order if it already has test-level diagnosis codes?**

No, order-level diagnosis codes are not required if each test has an associated test-level diagnosis code. However, if any test lacks a test-level diagnosis code, you must either assign a test-level diagnosis code to that test or add an order-level diagnosis code.

#### **How does the lab interpret test-level diagnosis codes versus order-level diagnosis codes?**

Test-level diagnosis codes precede order-level diagnosis codes. See the example below:

- The CBC test was not assigned any test-level diagnosis codes, so it will be linked only to the order-level diagnosis code E11.9, which will be treated as the primary diagnosis code for the CBC test.
- The BMP test was assigned two test-level diagnosis codes and is also  linked to the order-level diagnosis code E11.9:
 - C22.1 will be treated as the primary diagnosis code since it is the first test-level diagnosis code.
 - H40.1190 will be treated as the secondary diagnosis code as it is the second test-level diagnosis code.
 - E11.9 will be treated as the tertiary diagnosis code because it is associated at the order-level.

#### **Can I move a diagnosis code from the test-level to the order-level or vice versa?**

Diagnosis codes cannot be dragged-and-dropped to relocate them. To change their placement, delete the code from the current location and re-add it to the desired one.

#### **What do the different Bill Types mean?**

- **Third Party** = Bill the Patient's insurance information on file
- **Patient** = Bill the Patient directly
- **Client** = Bill my practice
- **Worker's Comp** = Bill the patient's worker's compensation payer
- **Special Billing** = Allows you to designate that you have a special code that you would like to associate with this order.

## **Special Ordering Scenarios**

#### **How can I create a lab order for patients without insurance?**

If you choose "Patient" as the **Bill Type**then you do not have to enter insurance information for the patient. The patient would then be expected to pay at the lab center.

#### **How do I create a standing order for a patient that needs to get the same tests done on a periodic basis?**

Contact the lab vendor directly to set up a standing order for a patient requiring periodic testing as the Elation Electronic Lab Order Form does not support standing orders.

#### **How do I create a lab order for Quest’s Patient Service Center (PSC)?**

To specify that a lab order is for any Quest Patient Service Center (PSC), choose ‘Any Site’ in the **Site** field of Lab Order Form. This will allow the patient to complete the Lab Order at any Quest location of their choice.

#### **How do I create a lab order through Quest’s Uninsured Patient Program (UPP)?**

To designate a lab order under the Quest Uninsured Patient Program (UPP), contact your Quest representative to obtain the required insurance name and address for eOrdering. Ensure this Insurance Carrier is set for any patient enrolled in UPP. When a lab order is submitted with the UPP insurance details, Quest's Insurance Master Database will recognize the address, match it to the corresponding Quest UPP payer code, and bill the patient accordingly.

####

## **Permissions**

#### **Can staff members help me create lab orders?**

Yes! Staff Level Users can draft lab orders for any patient. Once they are done drafting an order, Staff Level Users can click **Save as Draft & Close** to keep the lab order in the Requiring Action section of the patient's chart for providers to complete and sign off. When Staff Level Users draft lab orders, the orders are always assigned to the Provider Assigned in Practice that's designated in the patient's demographics.

If you would like to allow staff members to **sign** lab orders on your behalf, you can assign them as a delegate. [Click here to learn more about staff delegates](https://help.elationemr.com/s/article/staff-permissions--staff-delegates).

## **Related Articles**

- [Lab Orders & Results Introduction](Lab-Orders-and-Results-Introduction.md)
- [Lab Orders & Results - Using the regular Lab Order Form](Regular-Lab-Order-Form.md)
- [Lab Orders & Results - Managing lab vendors](Managing-lab-vendors.md)
- [Lab Orders & Results - Managing electronic lab results](Viewing-results-from-lab-interfaces.md)
- [Orders Guide- Following up on outstanding orders & referrals](follow-up-outstanding-orders-referrals.md)