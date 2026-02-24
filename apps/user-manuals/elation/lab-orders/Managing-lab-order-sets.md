# Lab Orders & Results - Managing lab order sets

Source: https://help.elationhealth.com/s/article/Managing-lab-order-sets

---

# **Contents**

- [Overview](#Overview)
 - [What are Lab Order Sets?](#description)
 - [What are the benefits of Lab Order Sets?](#benefits)
- [Workflow Instructions](#Workflow_Instructions)
 - [Creating Lab Order Sets](#create_lab_order_sets)
    - [Creating Lab Order Sets from the Lab Order Form](#create_from_lab_order)
    - [Creating Lab Order Sets from the Lab Orders Settings page](#create_from_Settings)
    - [Special instructions for Scarlet Health Lab Order Sets](#Scarlet_Health)
 - [Editing Lab Order Sets](#edit)
 - [Deleting Lab Order Sets](#delete)
 - [Applying Lab Order Sets to lab orders](#apply)
    - [Show Lab Order Sets first in test search results](#search)
- [Frequently Asked Questions (FAQ)](#FAQ)

# **Overview**

## **What are Lab Order Sets?**

Lab Order Sets are templates of tests that are frequently ordered together  and optionally their corresponding diagnoses. Lab Order Sets are saved at the practice level so they can be used by any user for any patient.

## **What are the benefits of Lab Order Sets?**

Lab Order Sets speed up the lab ordering process by reducing the number clicks needed to input tests and diagnoses into an order form. Lab Order Sets can also help standardize ordering protocols across your practice.

# **Workflow Instructions**

## **Creating Lab Order Sets**

The type of interface that you have with a lab vendor will determine how you must approach managing its order sets.

| | | |
| --- | --- | --- |
| | Vendors with whom you have **no** interface or a **unidirectional** interface | Vendors with whom you have a **bidirectional** interface |
| **Set-up** | A **generic** set of lab order sets can be used across all of these vendors. | **Separate** order sets must be created for each vendor. |
| **Test Selection** | You can add tests from Elation’s generic  compendium and your practice’s user-created tests. | You can only add tests from each vendor’s own compendium. User-created tests are not allowed. |

Each time you go-live with a new bidirectional interface, make sure you review and recreate any order sets that you need to use for that vendor.

Lab order sets can be created from a patient’s chart or from the Lab Orders Settings page.

### **Creating Lab Order Sets from the Lab Order Form**

To create Lab Order Sets from the Lab Order Form:

| | |
| --- | --- |
| **1** | Go to a patient's chart. |
| **2** | At the top of the patient's chart, click **Orders** -> **Lab Order**. |
| **3** | Select the **Lab** you wish to create an order set for. |
| **4** | Search for and select the appropriate lab **Tests.** |
| **5** | Optionally add any test-level diagnoses or **Dx for All** (order-level diagnoses). |
| **6** | Click **Save as Order Set**. |
| **7** | Enter the **Order set name**. The order set name must be unique. |
| **8** | Click **Save**. |

### **Creating Lab Order Sets from the Lab Orders Settings page**

To create Lab Order Sets from the Lab Orders Settings page:

| | |
| --- | --- |
| **1** | Click your email address in the upper righthand corner of Elation. |
| **2** | Go to **Settings** -> **Lab Orders**. |
| **3** | Scroll to the correct section of the page.   1. If you’re creating an order set for a vendor with a bidirectional interface, locate the vendor name and click the **+Add Order Set** button. 2. If you’re creating an order set for a vendor with no interface or a unidirectional interface, scroll down to the “Other Lab Order Sets” section and click the **+Add Order Set** button. |
| **4** | Enter a **Name** for the order set. The order set name must be unique. |
| **5** | Search for and select the appropriate lab **Tests**. |
| **6** | Optionally add any test-level diagnoses or **Dx for All** (order-level diagnoses). |
| **7** | Click **Save**. |

### **Special instructions for Scarlet Health Lab Order Sets**

Electronic lab orders for Scarlet Health are routed through the Bioreference lab interface which means there are some special requirements when you create order sets for Scarlet Health:

- Create the order set under the Bioreference lab

 **💡**  **USER TIP** Add a prefix such as ‘SH’ to the Lab Order Set name so you can tell these apart from your Bioreference order sets
- When adding tests, select ones that are marked as Scarlet Health.
- Add "TH31-8" as one of the tests in the order set. This test is used by the interface to identify Scarlet Health orders so **it must be included**.

## **Editing Lab Order Sets**

To edit a Lab Order Set:

| | |
| --- | --- |
| **1** | Click your email address in the upper righthand corner of Elation. |
| **2** | Go to **Settings** -> **Lab Orders**. |
| **3** | Find the Lab Order Set you want to edit. |
| **4** | Click the **pencil** button (edit button) next to the Lab Order Set to enter edit mode. |
| **5** | Make edits as needed. |
| **6** | Click **Save** to save your changes. |

## **Deleting Lab Order Sets**

To delete a Lab Order Set:

| | |
| --- | --- |
| **1** | Click your email address in the upper righthand corner of Elation. |
| **2** | Go to **Settings** -> **Lab Orders**. |
| **3** | Find the Lab Order Set you want to delete. |
| **4** | Click the **trash can** button (delete button) next to the Lab Order Set. |
| **5** | Choose **Yes** in the delete confirmation box to proceed with deleting the Lab Order Set. |

ℹ️   **CAUTION** Take caution when deleting Lab Order Sets as deleted Lab Order Sets cannot be restored. Deleting a Lab Order Set deletes it for all users in your practice.

## **Applying Lab Order Sets to lab orders**

To apply a Lab Order Set to a lab order:

| | |
| --- | --- |
| **1** | Open a lab order draft |
| **2** | Apply a Lab Order Set using one of these methods:   1. Click **View Order Sets** at the top of the Lab Order Form to browse all available Lab Order Sets and then click on the Lab Order Set to add it to the lab order. 2. Click into the **Tests** field and search for any Lab Order Set by its name and then click on the name of the Lab Order Set to add it to the lab order.    - If you’d like to see your Lab Order Set results ahead of any individual tests, configure the setting below. |

### **Show Lab Order Sets first in test search results**

To show Lab Order Sets first in test search results:

| | |
| --- | --- |
| **1** | Go to **Settings** -> **Lab Orders**. |
| **2** | Go to the **Lab Order Settings** section. |
| **3** | Change the **Sort Lab Test Suggestions By** dropdown to **Order sets first.** This change will be automatically saved. |

# **Frequently Asked Questions**

#### **Why can't I find a lab test that I have ordered before?**

The directory of tests available (compendium), may be different depending on which Lab Vendor is selected for the Lab Order. Lab Vendors with a bidirectional lab interface utilize their own compendiums which means you must search for the test the exact way it is spelled out in their compendium. Try searching for the test using different terms (e.g. the Complete Metabolic Panel is known as "CMP" for LabCorp) to improve your search results.

If you have a question about a specific test or test code, please contact your lab representative for assistance.

#### **I cannot see some of the Lab Order Sets I created in the Lab Order Form. Why is this happening?**

Some of your Lab Order Sets may not be visible because they are linked to a different Lab Vendor than the one selected for the Lab Order. To resolve this, check the [Lab Orders Settings](https://app.elationemr.com/settings/laborders/) page to ensure your order set was created under the correct vendor. If needed, create a new Lab Order Set.

#### **When I tried to save a new Lab Order Set I saw an error message that says the name is non-unique and the Lab Order Set won’t save. Why is this happening?**

You are seeing this error message because each Lab Order Set must have a unique name regardless of the lab vendor. Choose a different unique name for the Lab Order Set you are trying to create and then click **Save**.

# **Related Articles**

- [Lab Orders & Results Introduction](Lab-Orders-and-Results-Introduction.md)
- [Lab Orders & Results - Using the regular Lab Order Form](Regular-Lab-Order-Form.md)
- [Lab Orders & Results - Using the electronic Lab Order Form](Electronic-Lab-Order-Form.md)
- [Orders Guide - Creating tests for Order Forms](Creating-tests-for-Order-Forms.md)
- [Lab Orders & Results - Managing lab vendors](Managing-lab-vendors.md)