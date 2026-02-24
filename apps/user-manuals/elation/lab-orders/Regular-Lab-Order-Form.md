# Lab Orders & Results - Using the regular Lab Order Form

Source: https://help.elationhealth.com/s/article/Regular-Lab-Order-Form

---

# **Contents**

- [Overview](#Overview)
- [Workflow Instructions](#Workflow_Instructions)
 - [Creating a lab order](#create_order)
 - [Transmitting the lab order](#transmit_order)
    - [Transmitting the lab order to the lab vendor via Elation fax](#transmit_via_fax)
    - [Transmitting the lab order to a patient](#transmit_to_patient)
 - [Printing specimen labels](#print_specimen_labels)
 - [Printing a lab order](#print_order)
- [Resources](#Resources)
 - [Glossary of Lab Order Form fields and buttons](#glossary)
- [Frequently Asked Questions (FAQ)](#FAQ)

# **Overview**

Use this article to learn how to create and transmit lab orders for the following lab interface scenarios:

- Lab vendors without an interface.
- Lab Vendors with a live or pending results-only interface.
- Lab Vendors with a pending bidirectional lab interface.

Here is an example of what the regular version of Elation’s Lab Order Form looks like in these situations. The buttons that allow you to complete the order will include:

- **Print & Close**
- **Sign & Close**
- (if applicable) **Sign & Hold**

ℹ️   **BIDIRECTIONAL LAB INTERFACES** [Click here for instructions on how to complete lab orders if you have a live bidirectional lab interface with the vendor](https://help.elationemr.com/s/article/Electronic-Lab-Order-Form).

# **Workflow Instructions**

## **Creating a lab order**

| | |
| --- | --- |
| **1** | Create a lab order use any of the the following options:   1. At the top of the patient's chart, click **Orders** -> **Lab Order**. 2. In any visit note or non-visit note draft, click **Lab**. 3. In an existing signed Lab Order, click **Actions** -> **Reorder** to re-order the same tests as the signed Lab Order. |
| **2** | Fill out the Lab Order Form. Fields with an asterisk are required. The chart below explains the core fields in the form. [Click here to see definitions for the remaining fields and buttons](#glossary).   | | | | --- | --- | | **Field / Button** | **Instructions** | | \***Lab** | Select the vendor with whom you are placing the order.   - Use the [Labs Settings page](https://help.elationemr.com/s/article/labs-settings) to add additional vendors if needed.   **💡**  **USER TIP** Type the first few letters of the lab vendor's name to filter your list of lab vendors. | | **Site** | Designate whether the specimen will be collected at any vendor patient service center, a specific vendor patient service center, or in-house.   - Additional location details can be set on the [Labs Settings page](https://help.elationemr.com/s/article/labs-settings), if needed. | | \***Tests** | Enter the test(s) you want the patient to complete. [Click here for instructions on how to create your own lab tests](https://help.elationemr.com/s/article/Creating-tests-for-Order-Forms). | | **Add Dx** | If there are diagnoses that need to be associated with a specific test, use this field to add those diagnoses. Test-level diagnosis codes will take precedence over order-level diagnosis codes. | | \***Dx for All** | Add diagnoses that are relevant to all the test(s) in the order. Order-level diagnosis codes are secondary to test-level diagnosis codes. **💡**  **USER TIP** If you've already entered diagnoses in the patient'sProblem List or visit note, these diagnoses will automatically appear in the dropdown menu for you to select. Use the [Problem List Guide](https://help.elationemr.com/s/article/managing-your-problem-list) to learn more about this feature. | | **Coll** | **If you selected ‘Any site’ or a specific vendor patient service center for the Site**, optionally specify when the test should be performed in the **Schedule Collection** **Date** field. **If you selected ‘In-house draw’ for the Site**, specify the **Document Collection** date and time that the specimen collection was completed. [Click here to learn about placing a lab order on hold until specimens collection is completed](https://help.elationemr.com/s/article/Order-Forms-Guide-Putting-lab-orders-on-hold-for-specimen-collection). | | \***Patient Condition** | Specify fasting requirements, if any, for the test(s). | | **Bill Type** | Specify whom to bill for the lab test(s). As a best practice, ensure the patient's demographic and insurance details in the chart are as comprehensive as possible, as this information will be printed on the lab order. If you would like to specify a default **Bill Type** for all of your lab orders:   1. Go to **Settings** -> **Lab Orders**. 2. Go to the **Lab Order Settings** section. 3. Use the **Default Bill Type** dropdown to select the default bill type. Your selection will be automatically saved. | |
| **3** | Use any of the options below to sign the lab order.   - **Print & Close** - **Sign & Close** - **Sign & Hold** |

ℹ️   **CAUTION** Once a lab order is signed, it cannot be edited.

####

## **Transmitting the lab order**

### **Transmitting the lab order to the lab vendor via Elation fax**

Attach a signed lab order to a Provider Letter to fax the lab order to the lab vendor. [Click here for full instructions](https://help.elationemr.com/s/article/efaxing-lab-and-radiology-orders).

### **Transmitting the lab order to a patient**

Attach a signed lab order to a Patient Letter to send a copy of the lab order to the patient via Patient Passport. [Click here for full instructions](https://help.elationemr.com/s/article/elation-patient-passport-an-introduction#write_message).

## **Printing specimen labels**

To print specimen labels for the lab order:

1. Locate the order in the **Chronological Record** or under the **Reports** -> **Lab Reports** tab.
2. Click **Actions**
   - To [print labels with a Dymo printer](https://help.elationemr.com/s/article/Orders-Guide-DYMO-printer), select **Print DYMO Specimen Labels**.
   - To print labels at the bottom of a regular sheet of paper (compatible with Labcorp forms), select **Print Specimen Labels**.

Below is an example of a specimen label printout for a Labcorp order.

## **Printing a lab order**

To print a lab order (without specimen labels):

1. Locate the order in the **Chronological Record** or under the **Reports** -> **Lab Reports** tab.
2. Click **Actions** -> **Print**.

# **Resources**

## **Glossary of Lab Order Form fields and buttons**

| | |
| --- | --- |
| **Field / Button** | **Explanation** |
| **View Order Sets** | View and apply commonly used [Lab Order Sets](https://help.elationemr.com/s/article/Managing-lab-order-sets) to the lab order. |
| **Send STAT via Phone** | Check this box if you want to instruct the lab to share results with you urgently by phone. |
| **Send STAT via Fax** | Check this box if you want to instruct the lab to share results with you urgently by fax. |
| **Show and print dual codes** | Show both ICD-9 and ICD-10 codes for selected diagnoses. |
| **Save as Order Set** | Save the tests, test-level diagnosis codes and order-level diagnosis codes listed as a new Order Set. |
| **Lab Instructions** | List any additional notes or instructions you want to share with the lab here. |
| **Notify via** | Add an internal note about how your practice should notify the patient about their lab results. |
| **Send a copy of test results to…** | List the name(s) of provider(s) to whom the lab vendor should send a copy of the results. ℹ️   **REMINDER** Labs are not obligated to share the results with the providers listed. This instruction is a courtesy request. |
| **St. Order** | Indicate the testing frequency and, if applicable, specify an **End date** for the standing order. |
| **RMDR** | Specify who to send an Elation alert to if results are not received by a specified date. The **Reminder date** is the date the reminder will be sent. |
| **Keep this confidential** | Check the **Keep this confidential** box to mark the order as a confidential record in the patient’s chart. **💡**  **USER TIP** If you mark a record as confidential, that record will always have a special indicator that can be seen when this order is shown in the patient's chart. This indicator will prompt members of your practice to take caution when printing or sharing the record. Learn more about confidential records in the [Patient Chart Guide- Managing confidential records](https://elation.lightning.force.com/articles/Knowledge/confidential-items-in-your-patient-chart) article. |
| **Print & Close** | Simultaneously sign and print the lab order and close the lab order window. |
| **Sign & Close** | Simultaneously sign the lab order and close the lab order window. |
| **Sign & Hold** | Simultaneously sign the lab order and put the lab order on hold so that specimen collection at your practice can occur later. This option will only be active if you selected  “in-house lab” as the Site and left the **Document collection** date blank. [Click here to learn about placing a lab order on hold until specimen collection is completed](https://help.elationemr.com/s/article/Order-Forms-Guide-Putting-lab-orders-on-hold-for-specimen-collection). |
| **Save as Draft** | Save the lab order as a draft and close the lab order window. The lab order draft will remain in the **Requiring Action** section of the patient’s chart until it is signed or discarded. |
| **Discard** | Delete the lab order draft. |
| **X** | Save the lab order as a draft and close the lab order window. The lab order draft will remain in the **Requiring Action** section of the patient’s chart until it is signed or discarded. |

#

# **Frequently Asked Questions**

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
- The BMP test was assigned two test-level diagnosis codes and is also linked to the order-level diagnosis code E11.9:
 - C22.1 will be treated as the primary diagnosis code since it is the first test-level diagnosis code.
 - H40.1190 will be treated as the secondary diagnosis code as it is the second test-level diagnosis code.
 - E11.9 will be treated as the tertiary diagnosis code because it is associated at the order-level.

#### **Can I move a diagnosis code from the test-level to the order-level or vice versa?**

Diagnosis codes cannot be dragged-and-dropped to relocate them. To change their placement, delete the code from the current location and re-add it to the desired one.

#### **What do the different Bill Types mean?**

- **Third Party** = Bill the Patient's insurance information on file
- **Patient** = Bill the Patient directly
- **Client** = Bill my practice
- **Worker's Comp** = Bill the patient's workers’ compensation payer
- **Special Billing** = Allows you to designate that you have a special code that you would like to associate with this order.

####

#### **How can I create a lab order for patients without insurance?**

If you choose "Patient" as the **Bill Type**then you do not have to enter insurance information for the patient. The patient would then be expected to pay at the lab center.

#### **How do I create a standing order for a patient that needs to get the same tests done on a periodic basis?**

To specify a standing order for a patient requiring periodic testing, create the lab order as usual. Be sure to complete the **St. Order** fields to indicate the desired testing frequency and, if applicable, specify an **End date** for the order.

ℹ️   **REMINDER** Some lab vendors may still require you to send a new lab order for each recurring test. If a new lab order will be needed, use the [Post-Date Office Message](https://help.elationemr.com/s/article/post-date-a-message-to-yourself-or-a-colleague) feature to set a reminder for yourself to generate the order at the appropriate time.

####

#### **Can staff members help me create lab orders?**

Yes! Staff Level Users can draft lab orders for any patient. Once they are done drafting an order, Staff Level Users can click **Save as Draft & Close** to keep the lab order in the Requiring Action section of the patient's chart for providers to complete and sign off. When Staff Level Users draft lab orders, the orders are always assigned to the Provider Assigned in Practice that's designated in the patient's demographics.

If you would like to allow staff members to **sign** lab orders on your behalf, you can assign them as a delegate. [Click here to learn more about staff delegates](https://help.elationemr.com/s/article/staff-permissions--staff-delegates).

####

#### **Does Elation have any integrations with lab centers?**

Yes, Elation has integrations with many lab centers to receive electronic lab results. For a subset of these lab vendors, we can also send orders electronically from the Lab Order Form. You can always view the latest list of integrated partners and their integration type on our [Partners](https://www.elationhealth.com/integrations/) page. To request an integration with one of our integrated partners, click the **I need help** -> **Contact Elation Support** button at the top of your Elation account and send the following information to our Support Team:

1. Name of the lab center
2. Full name of your lab center representative
3. Email and phone number of your lab center representative

####

#### **Can I order other medical tests in Elation?**

Yes! You can also order imaging (radiology), cardiac, pulmonary, and sleep tests in Elation. Find out more about the different medical tests forms in the [Order Forms Introduction](https://help.elationemr.com/s/article/Order-Forms-Introduction-Ordering-medical-tests-for-your-patients) article.

# **Related Articles**

- [Lab Orders & Results Introduction](Lab-Orders-and-Results-Introduction.md)
- [Lab Orders & Results - Managing lab vendors](Managing-lab-vendors.md)
- [Lab Orders & Results - Using the electronic Lab Order Form](Electronic-Lab-Order-Form.md)
- [Lab Orders & Results - Managing lab order sets](Managing-lab-order-sets.md)
- [Orders Guide - Creating tests for Order Forms](Creating-tests-for-Order-Forms.md)
- [Orders Guide- Following up on outstanding orders & referrals](follow-up-outstanding-orders-referrals.md)