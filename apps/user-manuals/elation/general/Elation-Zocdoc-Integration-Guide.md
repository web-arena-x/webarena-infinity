# Elation-Zocdoc Integration Guide

Source: https://help.elationhealth.com/s/article/Elation-Zocdoc-Integration-Guide

---

**Contents**

- [What is Zocdoc?](#description)
- [What is the Elation-Zocdoc integration?](#elation_zocdoc_integration)
- [How do I get started?](#getting_started)
 - [New Zocdoc User](#new_user)
 - [Existing Zocdoc User](#existing_user)
 - [Availability Setup](#availability_setup)
- [What information is synchronized?](#info_sync)
 - [Elation to Zocdoc](#elation_to_zocdoc)
 - [Zocdoc to Elation](#zocdoc_to_elation)
- [Editing appointments in Elation](#editing_appointments)
- [Getting Support](#getting_support)
- [Frequently Asked Questions](#faq)



**What is Zocdoc?** Zocdoc© is an online platform that allows patients to find and book appointments with healthcare providers in their area. Zocdoc helps patients find available appointments quickly based on criteria such as accepted insurance, distance, provider speciality, and more.



**What is the Elation-Zocdoc integration?** The integration between Elation and Zocdoc allows your practice to efficiently view and manage calendar availability and Zocdoc bookings. The Zocdoc calendar pulls real-time availability from provider calendars in Elation to display available appointments to patients. When a patient books an appointment with a provider on Zocdoc, their Elation calendar will update and reflect the Zocdoc booking.



**How do I get started?** At least one Provider Level User at your practice will need to have an account with Zocdoc to start the integration.

**Zocdoc User Setup**

To connect your ZocDoc account to your Elation account, submit a request here: <https://www.zocdoc.com/partner/elationhealth>. Zocdoc will reach out to you once the form has been completed.

- **Important Note:** If you do not have an account with Zocdoc, please register for an account through this Zocdoc-Elation landing page so that ZocDoc knows you are an Elation user when you register: <https://www.zocdoc.com/partner/elationhealth>




**Availability Setup** Before the Zocdoc integration is turned on, please set your available working hours in Zocdoc to  ensure that patients do not schedule appointments with you outside of your office hours.



**What information is synchronized?** The integration between Elation and Zocdoc primarily focuses on appointments, insurance, and basic patient demographic information syncing. When a patient books an appointment through Zocdoc, the appointment will appear on the Elation calendar for the provider who they scheduled with.


**Elation to Zocdoc** Elation will send the following information to Zocdoc:

- Provider availability
 - Based on the availability from the provider’s calendar on the Practice Home page

    - **Important Note:** Providers must also [set available working hours in Zocdoc](#availability_setup) to ensure that patients do not schedule appointments outside of office hours.
- Appointment status updates
 - When an appointment status is updated in Elation, it will reflect in Zocdoc


**Zocdoc to Elation** When appointments are scheduled in Zocdoc, Elation will receive information regarding the appointment, the patient’s demographics, and insurance.

**Appointments** When appointments are scheduled in Zocdoc, Elation will receive:

- Time of the appointment
- Duration of the appointment
- Which provider the appointment is scheduled with


**Demographics** The following demographic fields will sync from Zocdoc to Elation:

| **Elation Field Name** | Zocdoc Field Name |
| --- | --- |
| Legal first name | First |
| Legal last name | Last |
| Date of birth | Date of birth |
| Sex at birth | Sex |

- **Important Note:** Zocdoc will try to find a matching chart in Elation for the patient based on the criteria in the table below. If they do not find an exact match, then they will create a new patient chart in Elation.



**Insurance** The following insurance fields will sync from Zocdoc to Elation:

| **Elation Field Name** | Zocdoc Field Name |
| --- | --- |
| Insurance Card Photos (front and back) | Insurance Card Photos (front and back) |
| Insurance carrier name | Carrier |
| Plane name | Plan |
| Member ID | Member ID |




**Editing appointments in Elation** If you need to edit an appointment, you must edit the appointment in Elation. Edits made to the appointments in Elation will sync and be reflected on the Zocdoc calendar.


**Getting Support** If you encounter any issues with your Elation-Zocdoc integration, please reach out to Zocdoc by emailing service@zocdoc.com.


**Frequently Asked Questions** **What if not all providers at my practice want to integrate with Zocdoc?** Zocdoc can set up the integration for your practice to meet your specific needs. If not all providers at your practice want to integrate with Zocdoc, then the integration can be set up for those specific providers who would like to integrate and will not affect providers who do not want to integrate with Zocdoc.


© 2023 Zocdoc, Inc.