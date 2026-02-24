# Workspaces Guide- Common Use Cases (Premium)

Source: https://help.elationhealth.com/s/article/Workspaces-Use-Cases

---

## **Recommended Reading**

Before reading this article, we recommend reading the [Workspaces Introduction](workspaces-guide.md) article to learn about the Workspaces feature.

## **Contents**

- [When would I use the Workspaces feature?](#purpose)
- [Workspaces Use Cases](#use_cases)
 - [Primary Care Practice with a Mobile COVID Clinic](#secondary_clinical_focus)
 - [A network of Primary Care clinics with locations across 3 states](#network)
 - [A multi-speciality clinic with divided responsibilities](#multi_specialty)

## **When would I use the Workspaces feature?**

Customers within a single practice can add a flexible organizational layer (known as Workspaces in Elation) to the Elation ‘practice’ concept enabling them to deploy specific settings, resources, and configurations to different members of their organization based on different operational scenarios such as practice locations, clinical focus or role-specific responsibilities.

**Important Note**: The Workspaces feature is a product for Premium EHR customers only.

## **Workspaces Use Cases**

This section will showcase a few common use cases for Workspaces configuration. The following use cases will be discussed in detail:

- [Primary Care Practice with a Mobile COVID Clinic](#secondary_clinical_focus)
- [A network of Primary Care clinics with locations across 3 states](#network)
- [A multi-speciality clinic with divided responsibilities](#multi_specialty)

### **Primary Care Practice with a Mobile COVID Clinic**

This use case is ideal for practices with more than one clinical focus or location. Horizon Medical is a Los Angeles based, 3 provider + 6 staff, Primary Care practice that runs a Mobile COVID Clinic. The Mobile COVID Clinic

1. operates with Jane Doe as the doctor every Tuesdays and Thursdays
2. offers COVID-19 testing at a local school
3. administers care for patients who are diagnosed with COVID-19

Based on the above scenario, Horizon Medical will set up 2 [User Groups](user-groups.md) with the following members:

1. User Group #1- Main Office
   - John Smith, MD
   - Sam Smith, MD
   - Jane Doe, MD
   - 4 main office staff
2. User Group #2- COVID Clinic
   - Jane Doe, MD
   - 2 mobile clinic office staff

Based on the above scenario, Horizon Medical will set up 2 Workspaces with the following resources. This will allow the Mobile COVID Clinic users (the third column)  to see and use the resources specific to COVID-19 testing and care.

| Resources | Workspace #1- Main Office | Workspace #2- Mobile COVID Clinic |
| --- | --- | --- |
| **Time Zone** |
| | (PDT -07:00) US - Pacific | (PDT -07:00) US - Pacific |
| **User Access** |
| COVID Clinic (User Group) | | X |
| Main Office (User Group) | X | |
| **Provider Lists** |
| COVID Clinic (User Group) | | X |
| Main Office (User Group) | X | |
| **Practice Locations** |
| Horizon Medical | X | |
| Horizon Medical COVID Clinic | | X |
| **Print Headers** |
| Horizon Medical | X | |
| Horizon Medical COVID Clinic | | X |
| **Lab Accounts** |
| Office location specific Lab Accounts | X | |
| Mobile clinic specific Lab Accounts | | X |
| **Physical Exam Templates** |
| General Well | X | X |
| Medical Annual Wellness Exam | X | |
| Welcome to Medicare | X | |
| Well Womens | X | |
| **Review of Systems Templates** |
| General Female | X | X |
| General Male | X | X |
| **Letter & Referral Templates** |
| Request for Medical Records | X | |
| Sick Note for Sick | X | X |
| **Visit Note Templates** |
| Annual Wellness Visit | X | |
| COVID 19 Follow Up | X | X |
| COVID 19 Mobile Clinic Billing | | X |
| COVID 19 Office Billing | X | |
| COVID 19 Screening | X | X |
| Hypertension Follow Up | X | |
| Telehealth Attestation | X | |

### **A network of Primary Care clinics with locations across 3 states**

This use case is ideal for large networks of clinics with multiple locations. Clean Health is a network of Primary Care clinics with 3 locations- Phoenix (Arizona), San Diego (California) and Las Vegas (Nevada). Clean Health, Inc. will set up 3 User Groups to separate the employees for each location and have the time stamps displayed in the appropriate time zones. Patients can visit locations across states when traveling for work. Additionally, the San Diego office offers civil surgeon services for United States Citizenship and Immigration Services (USCIS) and has additional resources they want to separate from other offices.

Based on the above scenario, Clean Health will set up 3 Workspaces with the following resources. This will allow each office to see only the resources that are relevant to their office/location.

| Resources | Workspace #1- Las Vegas | Workspace #2- Phoenix | Workspace #3- San Diego |
| --- | --- | --- | --- |
| **Time Zone** |
| | (PDT -07:00) US - Pacific | (MDT -06:00) US - Mountain | (PDT -07:00) US - Pacific |
| **User Access** |
| Las Vegas (User Group) | X | | |
| Phoenix (User Group) | | X | |
| San Diego (User Group) | | | X |
| **Provider Lists** |
| Las Vegas (User Group) | X | | |
| Phoenix (User Group) | | X | |
| San Diego (User Group) | | | X |
| **Practice Locations** |
| Clean Health- Las Vegas | X | | |
| Clean Health- Phoenix | | X | |
| Clean Health- San Diego | | | X |
| **Print Headers** |
| Clean Health- Las Vegas | X | | |
| Clean Health- Phoenix | | X | |
| Clean Health- San Diego | | | X |
| **Lab Accounts** |
| LabCorp- San Diego | | | X |
| Quest- Las Vegas | X | | |
| Quest- Phoenix | | X | |
| Quest- San Diego | | | X |
| **Physical Exam Templates** |
| General Annual | X | X | X |
| Medicare Annual Wellness | X | X | X |
| USCIS | | | X |
| Welcome to Medicare | X | X | X |
| Well Womens | X | X | X |
| **Review of Systems** |
| General Female | X | X | X |
| General Male | X | X | X |
| **Letter & Referral Templates** |
| Request for Medical Records | X | X | X |
| Sick Note for Work | X | X | X |
| **Visit Note Templates** |
| Annual Wellness Visit | X | X | X |
| Hypertension Follow Up | X | X | X |
| Telehealth Attestation | X | X | X |
| USCIS Attestation | | | X |
| USCIS Exams | | | X |
| USCIS Vaccines | | | X |






### **A multi-speciality clinic with divided responsibilities**

This use case is ideal for practices that have various employees with distinct responsibilities. Spectrum Health is a 8 provider clinic that offers Primary Care, Acupuncture and Weight Loss services. Different providers and staff are responsible for different services while patients have access to all services during each visit.

Based on the above scenario, Spectrum Health will set up 3 [User Groups](user-groups.md) with the following members:

| Role | User Group #1- Primary Care | User Group #2- Acupuncture | User Group #3- Weight Loss |
| --- | --- | --- | --- |
| Primary Care Clinicians (4) | X | | |
| Acupuncturist (2) | | X | |
| Weight Loss Coaches (2) | | | X |
| Front Desk (2) | X | X | X |
| Medical Assistants (3) | X | | |
| Therapy Assistants (2) | | X | X |



Based on the above scenario, Spectrum Health will set up 3 Workspaces with the following resources. This will allow each Group to see only the resources that are relevant to their responsibilities.

| | | | |
| --- | --- | --- | --- |
| **Resources** | **Workspace #1- Primary Care** | **Workspace #2- Acupuncture** | **Workspace #3- Weight Loss** |
| **Time Zone** |
| | (PDT -07:00) US - Pacific | (PDT -07:00) US - Pacific | (PDT -07:00) US - Pacific |
| **User Access** |
| Acupuncture (User Group) | | X | |
| Primary Care (User Group) | X | | |
| Weight Loss (User Group) | | | X |
| **Provider Lists** |
| Acupuncture (User Group) | | X | |
| Primary Care (User Group) | X | | |
| Weight Loss (User Group) | | | X |
| **Practice Locations** |
| Spectrum Health | X | X | X |
| **Print Headers** |
| Spectrum Health | X | X | X |
| **Lab Accounts** |
| LabCorp | X | X | X |
| **Physical Exam Templates** |
| General Annual | X | X | X |
| Medicare Annual Wellness Exam | X | X | X |
| Welcome to Medicare | X | X | X |
| Well Womens | X | X | X |
| **Review of Systems Templates** |
| General Female | X | X | X |
| General Male | X | X | X |
| **Letter & Referral Templates** |
| Acupuncture Follow Up Guidelines | | X | |
| Request for Medical Records | X | | |
| Sick Note for Work | X | | |
| Weight Loss Counseling Referral | X | | |
| Weight Loss Program - First 3 months | | | X |
| Weight Loss Program - First 6-12 months | | | X |
| Weight Loss Program - First 12-16 months | | | X |
| **Visit Note Templates** |
| Acupuncture Attestation | | X | |
| Annual Wellness Visit | X | | |
| COVID-19 Follow Up | X | | |
| COVID-19 Screening | X | | |
| Hypertension Follow Up | X | | |
| Nutrition Review | | | X |
| Telehealth Attestation | X | | |
| Weight Loss- Initial Evaluation | | | X |
| Weight Loss- Follow Up | | | X |
| Weight Loss- Meal Plan (F) | | | X |
| Weight Loss- Meal Plan (M) | | | X |




## **Related Articles**

- [Workspaces Introduction](workspaces-guide.md)
- [User Groups Guide- Simplifying office messages & expanded calendar view](user-groups.md)