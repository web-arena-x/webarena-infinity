# Lab Orders & Results - Managing lab vendors

Source: https://help.elationhealth.com/s/article/labs-settings

---

# **Contents**

- [Overview](#Overview)
 - [What are the different types of lab vendor interfaces that Elation supports?](#different_lab_interfaces)
- [Workflow Guides](#Workflow_Guides)
 1. [Request a lab interface](#request_interface)
     - [Special instructions for Genova Diagnostics](#Genova_Diagnostics)
 2. [Manage lab vendors in Elation](#manage_lab_vendors)
     - [Add lab vendors](#add_lab_vendors)
     - [Customize lab vendor details](#customize_vendor_details)
     - [Track the status of a lab interface set-up](#track_status)
     - [Troubleshooting a lab interface that stopped working](#troubleshooting_interface)
     - [Delete lab vendors](#delete_vendors)
     - [Specify a default lab vendor for your practice](#default_lab_vendor)
 3. [Complete training](#complete_training)
- [Frequently Asked Questions (FAQ)](#FAQ)

# **Overview**

## **What are the different types of lab vendor interfaces that Elation supports?**

The three types of lab vendor interfaces are listed in the table below. Click on corresponding links for specific workflows as needed.

| | | | |
| --- | --- | --- | --- |
| **Lab Vendor Interface Type** | **No interface** | **Unidirectional interface** | **Bidirectional Interface** |
| **Methods for ordering labs** | - [eFax](efaxing-lab-and-radiology-orders.md) - [Print](https://help.elationemr.com/s/article/Regular-Lab-Order-Form#print_order) | - [eFax](efaxing-lab-and-radiology-orders.md) - [Print](https://help.elationemr.com/s/article/Regular-Lab-Order-Form#print_order) | - [Electronic](https://help.elationemr.com/s/article/Electronic-Lab-Order-Form) |
| **Methods for receiving results** | - [eFax](Receiving-faxes-in-your-Elation-Fax-Inbox.md) - [Scan & upload](filing-documents-to-a-patient-chart.md) | - [Electronic](Viewing-results-from-lab-interfaces.md) | - [Electronic](Viewing-results-from-lab-interfaces.md) |
| **Vendor List** | —----------------------- | [Click here for a list of lab vendors that offer a unidirectional lab interface with Elation](https://www.elationhealth.com/integrations/?ucterms=partner_service:laboratories). | [Click here for a list of lab vendors that offer a bidirectional lab interface with Elation](https://www.elationhealth.com/integrations/?ucterms=partner_service:laboratories-bidirectional). |

# **Workflow Guides**

## **1.  Request a lab interface**

To request a lab interface, click **I need help** -> **Contact Elation Support** and send Elation the following information (with the exception of [Genova Diagnostics](#Genova_Diagnostics)):

- The name of the lab vendor you want to interface with
- Your lab account number for that lab vendor
- The full name of your lab representative for that lab vendor
- The email address of your lab representative for that lab vendor

### **Special instructions for Genova Diagnostics**

Follow these instructions to submit an interface request with Genova Diagnostics:

1. Login to your myGDX (Genova Diagnostics) account via this link: <https://www.gdx.net/mygdx/login>
2. Click **Account Settings**.
3. Click **Update EHR Preferences**.
4. Find ‘Elation Health’ under **EHR Provider**.
5. Check off the **Ordering Interface** and **Results Interface** boxes
6. Click **Add**.

Afterwards Genova Diagnostics will work with us to activate your interface and you will be notified once it is live.

## **2. Manage lab vendors in Elation**

### **Add lab vendors**

To add a lab vendor to your Lab Order Form:

| | |
| --- | --- |
| **1** | Click on your email address in the upper righthand corner of Elation. |
| **2** | Go to **Settings** -> **Labs**. |
| **3** | Click **+Add Lab Vendor**. |
| **4** | Type the name of the Lab Vendor you want to add.   - If Elation has an interface with the lab vendor, their name will appear as an option for you to select from. - If Elation does not have an interface with the lab vendor, type their name as you would like it to appear on your Lab Order Form. |
| **5** | Click **Add**. |

### **Customize lab vendor details**

To customize the details of lab vendors in your lab vendor list:

| | |
| --- | --- |
| **1** | Click on your email address in the upper righthand corner of Elation. |
| **2** | Go to **Settings** -> **Labs**. |
| **3** | Click the **Details** button to the right of the lab vendor’s name. |
| **4** | Adjust any of the following details as needed:   - **Printed Orders** - Show this lab vendor on the Lab Order Form. This is by default **On**. - **Electronic Ordering** - [Monitor the status of your interface set up](#track_status). - **Electronic Results** - [Monitor the status of your interface set up](#track_status). - **Compendium** - Understand the compendium options for the lab vendor. - If the lab vendor does not have a compendium available, you’ll have access to a generic Elation compendium and can [create and utilize custom tests](https://help.elationemr.com/s/article/Creating-tests-for-Order-Forms) when creating orders via the [regular Lab Order Form](https://help.elationemr.com/s/article/Regular-Lab-Order-Form). - If the lab vendor has their own test compendium, only tests that are part of the compendium can be selected when creating orders via the [electronic Lab Order Form](https://help.elationemr.com/s/article/Electronic-Lab-Order-Form). - **Locations** - Provide the name, address, phone, or fax details of vendor patient service centers to be displayed on the printed lab order. These **Locations** will appear in the **Site** selection of the Lab Order form; if no locations are added here, you’ll still be able to select “Any site” within the form.   - To add a location:     1. Click the **+Add a location** button     2. Enter the **Name** of the location (required).     3. Some customers use the first line of the street address as the location name if the location does not have a formal name.     4. Enter **Address**, **Phone** and/or **Fax** information as needed.     5. Click **Save**. |
| **5** | Click **Close** to close the lab vendor details window. |

### **Track the status of a lab interface set-up**

To track the status of a lab interface set-up:

| | |
| --- | --- |
| **1** | Click on your email address in the upper righthand corner of Elation. |
| **2** | Go to **Settings** -> **Labs**. |
| **3** | For the vendor in question, check the **Electronic Orders?** or **Electronic Results?** columns to see the status of the lab interface. The statuses can be as follows:   - **Not Available** - Interface is not offered. - **Set Up** - Interface request not initiated. - **Waiting on lab** - Interface request sent to the lab, awaiting their response. - **Pending testing** - Interface is pending testing. - **Completed testing** - **pending go-live** - Interface testing completed and waiting to enable interface. - **Blocked** - **lab needs paperwork** - Interface enablement request is on hold pending additional paperwork from your practice. - **Live** - Interface is live and data can be transmitted. |

### **Troubleshooting a lab interface that stopped working**

If a lab interface that was previously working has stopped functioning, follow these steps to diagnose and resolve the issue. Common issues include:

- A lab vendor you previously ordered from no longer appears as an electronic destination.
- Electronic results from a vendor have stopped arriving.

#### **Step 1 – Check your lab vendor settings**

| | |
| --- | --- |
| **1** | Click on your email address in the upper righthand corner of Elation. |
| **2** | Go to **Settings** -> **Labs**. |
| **3** | Verify the vendor is still listed in your lab vendor list. |
| **4** | Check the **Electronic Ordering** and **Electronic Results** fields to confirm the interface type (unidirectional or bidirectional) and current status. The status should show **Live** if the interface is active and data can be transmitted. Other statuses—such as **Blocked - lab needs paperwork**, **Pending testing**, or **Set Up**—indicate the interface is not currently operational. |

#### **Step 2 – Validate your account with the lab**

Contact your lab vendor directly to confirm:

- Your account is still active.
- Your account is correctly associated with Elation for electronic ordering or results delivery.

#### **Step 3 – Contact Elation Support**

If the vendor is missing from your list, the interface status looks incorrect, or you have confirmed your lab-side account is active but the issue persists, contact Elation Support.

Click **I need help** -> **Contact Elation Support** and include the following information:

- Practice name
- Vendor name
- Lab account number
- Lab representative contact information (if applicable)
- One or two examples of recent orders or reports that failed or did not transmit as expected (include order IDs, Patient IDs and dates)

### **Delete lab vendors**

To delete a lab vendor from your lab vendor list:

| | |
| --- | --- |
| **1** | Click on your email address in the upper righthand corner of Elation. |
| **2** | Go to **Settings** -> **Labs**. |
| **3** | Click the **Details** button to the right of the lab vendor’s name. |
| **4** | Click **Delete this lab vendor** at the bottom of the window. |

Deleted lab vendors will no longer appear in your Lab Order Form.

### **Specify a default lab vendor for your practice**

To set a default lab vendor that will automatically populate when any member of your practice creates a new lab order:

| | |
| --- | --- |
| **1** | Go to **Settings** -> **Lab Orders**. |
| **2** | Go to the **Lab Order Settings** section. |
| **3** | Use the **Default Lab Vendor** dropdown to select the default lab vendor. Your selection will be automatically saved. |

## **3. Complete training**

Some vendors, such as Labcorp, require everyone in the practice to complete training prior to enabling a lab interface. [Click here to watch the Labcorp training video](https://vimeo.com/418182520/abc5baa2bc).

# **Frequently Asked Questions**

#### **I do not see an interface for the lab I work with. Can Elation build a new lab interface with that lab?**

To request a lab interface build with Elation, click **I need help** -> **Contact Elation Support** and send us the following information:

1. The name of the vendor.
2. The name and email address of your contact at the vendor.

Elation will review the request and reach out to the vendor to determine if an interface is possible and keep you updated on the progress of the request.

# **Related Articles**

- [Lab Orders & Results Introduction](Lab-Orders-and-Results-Introduction.md)
- [Lab Orders & Results - Using the regular Lab Order Form](Regular-Lab-Order-Form.md)
- [Lab Orders & Results - Using the electronic Lab Order Form](Electronic-Lab-Order-Form.md)
- [Lab Orders & Results - Managing electronic lab results](Viewing-results-from-lab-interfaces.md)