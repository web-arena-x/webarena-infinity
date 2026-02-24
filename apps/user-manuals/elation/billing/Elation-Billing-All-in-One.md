# Elation Billing- Using Elation's all-in-one billing solution to manage your claims

Source: https://help.elationhealth.com/s/article/Elation-Billing-All-in-One

---

## **Contents**

- [What is Elation Billing?](#description)
- [Why is Elation Billing valuable?](#value)
- [What information is synchronized?](#sync_overview)
- [How do I get started?](#start)
 - [Mapping Data](#mapping)
- [Patient Charts](#charts)
 - [Creating Charts](#creating_charts)
 - [Merging Charts](#merging_charts)
 - [Deleting Charts](#deleting_charts)
- [Patient Demographics](#demographics)
- [Patient Insurance](#insurance)
 - [Carriers](#carriers)
- [Bills](#bills)
 - Additional billing fields
- [Getting Support](#support)

## **What is Elation Billing?**

Elation Billing is Elation’s all-in-one solution for managing your claims and revenue. Elation Billing reduces the need for double documenting in two softwares and allows practices to store all their clinical data in the EHR while using Elation Billing to manage their revenue.

## **Why is Elation Billing valuable?**

Using an all-in-one solution, like Elation Billing, to manage your clinical and financial workflows allows you to simplify billing workflows, eliminates integration challenges, and reduces time spent on duplicate claim entries. This in turn allows you to focus more time on patient care.

## **What information is synchronized?**

| Data | Sync Direction |
| --- | --- |
| Patient Charts | Elation EHR → Elation Billing |
| Demographics | Elation EHR → Elation Billing |
| Insurance | Elation EHR → Elation Billing |
| Bills | Elation EHR → Elation Billing |

##

## **How do I get started?**

If you are interested in using Elation Billing, please notify your Elation customer service representative using [this form](https://www.elationhealth.com/launchbilling/) or the “I need help” -> “Contact Elation Support” option in the EHR. Your customer service representative will reach out to you to further discuss your interests.

###

### **Mapping Data**

Follow these instructions to map the following data between Elation EHR & Elation Billing:

1. Providers- Provider mapping is automatic between Elation EHR & Elation Billing.
2. Practice Locations- Practice Location is automatic between Elation EHR and Elation Billing. You must still select a default Place of Service code in Elation EHR for each Practice Location.
3. Payers/Carriers- Payer/Carriers are automatically mapped between Elation EHR and Elation Billing.
4. CPT Codes- You can freely add CPT Codes to a visit note in Elation EHR and those will be automatically pushed to the Superbill in Elation Billing.

##

## **Patient Charts**

### **Creating Charts**

All patient charts must be created in Elation EHR in order for the patient's chart to be created in Elation Billing. See the [Patient Demographics section](#demographics) for details about managing demographics information after charts are created in the EHR.

####

### **Merging Charts**

Each chart can only have a one to one connection between Elation EHR and Elation Billing and this connection is established upon chart creation. If you happen to see a duplicate chart for the same patient in the EHR, please make sure you find the chart that is connected between the EHR and Elation Billing and keep the connected chart after performing a merge.

- For example, patient John Smith has one chart in Elation Billing but two charts in the EHR. The best way to find out which of the two charts in the EHR is connected to Elation Billing is by clicking on the "Elation EHR Record" button for the chart in Elation Billing to see which EHR patient chart is tied to the Elation Billing chart.

Here are the proper merge steps for EHR charts:

1. Open the duplicate chart that is not connected to the integration
2. Click on the patient's name to open their Demographics
3. Click on the "Merge Chart" button
4. Find & select the chart you want to keep (the one that is connected to the integration)
5. Click "Merge Chart"
6. Confirm you understand the transfer of data and then click "Yes, merge charts"

### **Deleting Charts**

Deleting a chart in Elation EHR will not delete the chart in Elation Billing and vice versa. Please take caution when deleting charts in the EHR as charts have a one to one connection to Elation Billing. If the patient is still active in your practice, the deleted chart must be restored in order for the patient's information to sync properly from the EHR to Elation Billing. Contact Elation using the "I need help" button if you need to restore a deleted chart in the EHR.

## **Patient Demographics**

The synchronization of Patient Demographics is uni-directional from Elation EHR to Elation Billing. Any changes or updates to demographics information must occur in the EHR. The following table shows a mapping of the Patient Demographics fields that are shared between Elation EHR and Elation Billing and their matching field names.

| Elation EHR Field Name | Elation Billing Field Name |
| --- | --- |
| Legal First Name | First Name |
| Legal Last Name | Last Name |
| Date of birth | DOB (Age) |
| Sex at Birth | Gender |
| SSN | Social Security |
| Mobile Phone   - If Mobile Phone does not exist then the phone number in the primary phone field in Elation is pushed to LightningMD | Best Phone |
| Email | Best Email |
| Address | Address 1 |
| Ste or apt # | Address 2 |
| City | City |
| State | State |
| Zip | Zip |
| Guarantor First Name | Responsible Party First Name |
| Guarantor Last Name | Responsible Party Last Name |
| Guarantor Phone # | Responsible Party Best Phone |
| Guarantor Address | Responsible Party Address 1 |
| Guarantor City | Responsible Party City |
| Guarantor State | Responsible Party State |
| Guarantor Zip | Responsible Party Zip |
| Link to Elation Chart | Elation EHR RECORD |




## **Patient Insurance**

The synchronization of insurance information is uni-directional from Elation EHR to Elation Billing. Practices must enter insurance information in the EHR in order for the insurance information to push to Elation Billing.

The following table lists the insurance related fields that are pushed from Elation EHR to Elation Billing and show how the EHR fields map to the Elation Billing fields. Fields that are not listed are not shared between Elation EHR and Elation Billing:

| Elation EHR Field Name | Elation Billing Field Name |
| --- | --- |
| Insurance Carrier Name | Insurance Payer |
| Group ID | Group Number |
| Member ID | Member ID |
| Patient's relation to policyholder | Relationship |

### **Carriers**

Insurance Carrier details should only be maintained in Elation EHR as Elation EHR is the source of truth for insurance. Best practice is to select the patient’s Insurance from the drop-down options that appear.

**Important Notes**:

- If you are adding a NEW Insurance to your EHR, this new insurance will automatically be mapped to a Payer in Elation Billing.
- Elation EHR ‘Plan’ level details are not shared with Elation Billing. If it is important to distinguish between different coverage plans under different Payers, create a separate Elation EHR Carrier for each coverage plan.

## **Bills**

The synchronization of bills is uni-directional from Elation EHR to Elation Billing. By default, once a provider signs a visit note in the EHR, the billing information from the visit note is pushed to Elation Billing as a Superbill. As best practice, review your bill to make sure coding is accurate and complete before signing your visit note because once a bill is pushed to Elation Billing, edits must be made in both the EHR and Elation Billing if needed. We recommend turning on the [Billing Guidance](billing-settings---service-locations--procedure-codes.md#billing_guidance) feature which will notify you if you are missing any CPT codes or ICD-10 codes upon signing your visit note.

- **User Tip**: If you prefer your bills are pushed independent of signing a visit note, we recommend turning on the Delayed Billing feature. The Delayed Billing feature allows you to hold your bills in [Billing Home](Billing-Home.md) for review until you are ready to send them to Elation Billing. [Click here to learn more about the Delayed Billing feature](https://help.elationemr.com/s/article/How-to-set-up-Delayed-Billing).

The following table lists the fields that are pushed from Elation EHR to Elation Billing and show how the EHR fields map to the Elation Billing fields. Fields that are not listed are not shared between Elation EHR and Elation Billing:

| Elation EHR Field Names | Elation Billing Field Names |
| --- | --- |
| CPT Code | CPT |
| Modifier | MOD |
| Dxs\* | DX |
| Service Location (POS) | Location |
| Charge | CHG |
| Unit | UNIT |
| Referring Provider | Referring Provider |
| Rendering Provider | Rendering Provider |

**\*Important Notes**:

- While you can enter more than 12 diagnosis codes on a bill in the EHR, Elation Billing does not support automatic claim splitting at this time. Please limit to a maximum of 12 diagnoses per bill. Elation Billing will receive all your diagnosis codes and will transmit up to 12 diagnoses per claim, with each charge line item on the claim also having up to 4 diagnosis pointers (the top 4 diagnosis codes from each procedure code on the bill will be used).
- The charges associated with your Popular CPT Codes Settings in the EHR will serve as your Fee Schedule for Elation Billing. Store the default charge for each CPT Code you bill for in the Popular CPT Codes Settings of your EHR to readily populate the charge in your bill.

### **Additional billing fields**

You can enable additional incident-to billing fields and synchronize these fields from Elation EHR to Elation Billing. The fields include **Supervising Provider**, **Billing Provider**, **Ordering Provider** and **Prior Authorization** and the mapping is shown below. To enable any of these fields:

1. Go to Elation EHR
2. Click on your email at the top of your account and then click “Settings”
3. Click “Billing” to open the Billing settings
4. Scroll down to the Billing Fields section
5. Click on the toggle to configure the fields you want to include on your bills - green is ON (enabled) and gray is OFF (disabled)
6. Once a field is enabled, it will appear at the top of the bill in your EHR visit notes
   - Data stored in enabled fields will also push to Elation Billing when you push the bill over.

| Elation EHR Field Names | Elation Billing Field Names |
| --- | --- |
| Ordering Provider | Ordering Provider |
| Supervising Provider | Supervising Provider |
| Prior Authorization | Auth/Referral Number (Prior Authorization) |
| Billing Provider (appears after you check off the “Mark as incident-to encounter” box) | Billing Provider |

- **Ordering Provider**: This field is used when services provided require a referral or order from another healthcare provider such as durable medical equipment, diagnostic imaging, laboratory tests, specialist consultations, and certain medical procedures. This is not a common field for Primary Care.
- **Billing Provider**: This field is commonly used for incident-to billing.

## **Getting Support**

If you need assistance with Elation Billing, contact Elation by clicking on the blue chat box at the bottom right of your Elation Billing account or visit our [Help Center](https://help.billing.elationemr.com/en/).

####

## **Related Articles**

- [Patient Demographics Guide- Managing patient insurance](Managing-Insurance.md)
- [Billing Guide- Delayed Billing](How-to-set-up-Delayed-Billing.md)
- [Billing Guide- Creating a superbill & coding for your visit](billing.md)
- [Billing Guide- Navigating Billing Settings](billing-settings---service-locations--procedure-codes.md)