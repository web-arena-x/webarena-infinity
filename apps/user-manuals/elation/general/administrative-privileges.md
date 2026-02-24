# User Accounts Guide- Administrative privileges

Source: https://help.elationhealth.com/s/article/administrative-privileges

---

## **Contents**

- [What are Administrative ('Admin') level privileges?](#description)
- [Why are Administrative ('Admin') level privileges useful?](#value)
- [Assigning Administrative ('Admin') level privileges](#assign)
- [Revoking Administrative ('Admin') level privileges](#revoke)
- ['Admin' settings](#settings)
 - [Settings that are always 'Admin' only](#always_admin_only)
 - [Settings that you can assign to be 'Admin' only](#assign_admin_only)
- [Frequently Asked Questions](#faq)

## **What are Administrative ('Admin') level privileges?**

Administrative ('Admin') level privileges allow you to prevent certain members of your practice (with access to Elation EHR) from taking certain actions in your practice's Elation account. Administrative ('Admin') users are allowed to take more actions in Elation compare to non-Administrative ('Admin') users such as:

1. [manage Elation user accounts for providers and staff](managing-user-accounts.md)
2. enable certain features such as:
   - [Multi-factor Authentication (MFA)](Multifactor-Authentication-MFA.md)
   - [Patient Booking Site](Patient-Booking-Site.md)
   - [Patient Forms](Getting-Started-with-Patient-Forms.md)
   - [Patient Payments](using-elation-to-securely-collect-patient-payments.md)
   - [Patient Invoicing](patient-invoicing.md)
   - [Automated Appointment Reminders](appointment-reminders.md)
   - [Integrated Video (Zoom)](Elation-Telehealth-powered-by-Zoom.md)©
3. configure different settings such as:
   - [user groups](user-groups.md)
   - [visit note categories](visit-note-categories.md)
   - [report categories](report-types.md)
   - [Patient Passport message routing](https://help.elationemr.com/s/article/elation-patient-passport-an-introduction#Routing)
   - [popular CPT Codes for billing](https://help.elationemr.com/s/article/billing-settings---service-locations--procedure-codes#Where%20do%20I%20find%20the%20Popular%20Procedure%20Codes%20list?)
   - [practice locations](adding-a-second-practice-location.md)
   - [Insurance Carriers list](https://help.elationemr.com/s/article/Managing-Insurance)
   - [templates](https://help.elationemr.com/s/article/templates-settings)
   - [lab vendors list](https://help.elationemr.com/s/article/labs-settings#managing_vendors)
   - [appointment types](https://help.elationemr.com/s/article/calendar-and-booking-settings#Appointment_Types)
   - [virtual visit instructions](https://help.elationemr.com/s/article/Elation-Telehealth-powered-by-Zoom#VirtualVisitInstructions)



## **Why are Administrative ('Admin') level privileges useful?**

Administrative ('Admin') level privileges allow you to specify who can enable advanced features and who can configure important settings that impact your practice's workflows. Administrative ('Admin') level privileges are generally assigned to the owner(s) or manager(s) of the practice because they are most knowledgable about how they want to run the practice as well as what configurations are important in the Elation settings to maximize efficiency.



## **Assigning Administrative ('Admin') level privileges**

Only users within the practice with administrative ('Admin') level privileges can assign administrative ('Admin') level privileges to other users in the practice. To assign administrative ('Admin') level privileges:

1. Click on your email at the top of your Elation account and click "Settings"
2. Click "Manage Accounts"
3. Click on the "Make Admin" button next to the user's name to assign them administrative ('Admin') level privileges

## **Revoking Administrative ('Admin') level privileges**

Only users within the practice with administrative ('Admin') level privileges can revoke administrative ('Admin') level privileges for other users in the practice. To revoke administrative ('Admin') level privileges:

1. Click on your email at the top of your Elation account and click "Settings"
2. Click "Manage Accounts"
3. Click on the "Remove Admin" button next to the user's name to remove administrative ('Admin') level privileges

## **'Admin' Settings**

There are two types of 'Admin' only settings in Elation. There are:

1. Settings that are always 'Admin' only
2. Settings that you can assign to be 'Admin' only

### **Settings that are always 'Admin' only**

Settings that are always 'Admin' only are under the *Admin User Only* section of the *Elation Settings* page. Only 'Admin' users can view and edit the settings under this section. These are the settings that are always 'Admin' only:

- [Manage Accounts](managing-user-accounts.md)
- [User Groups](user-groups.md)
- [Report](report-types.md) & [Visit Note Categories](visit-note-categories.md)
- [Patient Passport Messages](https://help.elationemr.com/s/article/elation-patient-passport-an-introduction#Routing)
- [Security & Privacy](https://help.elationemr.com/s/article/Multifactor-Authentication-MFA)

### **Settings that you can assign to be 'Admin' only**

Settings that you can assign to be 'Admin' only will have an "Admin only" toggle at the top of the page. Anyone can turn the toggle on but only 'Admin' users can turn the toggle off after it is turned on

- Gray = Off
- Green = On

![]()


All users can view these settings but only 'Admin' users can edit the settings. These are the settings that can be set to 'Admin' only:

- [Billing](https://help.elationemr.com/s/article/billing-settings---service-locations--procedure-codes)
- [Patient Payments](using-elation-to-securely-collect-patient-payments.md)
- [Membership Management](Introduction-to-Membership-Management-with-Elation.md) (special feature)
- [Practice Locations](adding-a-second-practice-location.md)
- [Insurance](https://help.elationemr.com/s/article/Managing-Insurance)
- [Templates](https://help.elationemr.com/s/article/templates-settings)
- [Prescriptions](https://help.elationemr.com/s/article/create-and-use-custom-rx-templates)
- [Sort Settings](https://help.elationemr.com/s/article/chronological-record-sort-settings)
- [Labs](https://help.elationemr.com/s/article/labs-settings#managing_vendors)
- [Lab Orders](https://help.elationhealth.com/s/article/ordering-lab-tests#order_sets)
- [Calendar & Booking](Patient-Booking-Site.md)
- [Virtual Visits](Elation-Telehealth-powered-by-Zoom.md)
- [Patient Forms](Getting-Started-with-Patient-Forms.md)
- [Collaborative View Sharing](the-collaborative-view-hi-only.md#toggle) (special feature)

**Important Note**: Certain features allow you create data outside of the settings page (prescription templates, PE/ROS templates, letters and order sets). 'Admin' and 'non-Admin' users will be able to create templates and order sets from the patients chart but only 'Admin' users can edit or remove prescription templates, PE/ROS templates, letters and order sets from the settings pages if you make theses settings pages 'Admin only'.




## **Frequently Asked Questions (FAQ)**

#### **Can I make all settings in Elation 'Admin' only?**

Only certain settings in Elation can be 'Admin' only. Elation will notify you if we introduce more 'Admin' only settings to Elation.


#### **I made the lab order feature 'Admin' only in Elation but my non-Admin staff was still able to create a new lab order set. Why?**

Lab Order Sets can be created in the Lab Order Form in the patient's chart. For this reason, 'Admin' and 'non-Admin' users will be able to create lab order sets from the patients chart but only 'Admin' users can edit or remove lab order sets from the settings page.


#### **I made the prescriptions (rx) order set feature 'Admin' only in Elation but my non-Admin staff was still able to create a new prescription (rx) order set. Why?**

Prescription Order Sets can be created in the Prescription (Rx) Form in the patient's chart. For this reason, 'Admin' and 'non-Admin' users will be able to create prescription order sets from the patients chart but only 'Admin' users can edit or remove prescription order sets from the settings page.



*Copyright ©2023 Zoom Video Communications, Inc. All rights reserved.*



## **Related Articles**

- [User Accounts Guide- Managing Elation accounts for providers and staff](managing-user-accounts.md)
- [VIP Charts- Limiting access to certain patient charts](vip-chart-feature.md)