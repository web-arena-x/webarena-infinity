# Patient Chart Guide- Creating a new patient chart

Source: https://help.elationhealth.com/s/article/Patient-Chart-Guide-Creating-a-new-patient-chart

---

## **Contents**

- [What is a patient chart?](#description)
- [Creating new patient chart](#new_chart)
- [Frequently Asked Questions](#faq)

## **What is a patient chart?**

All records in the Elation EHR must be tied to specific patient. A *Patient Chart* is the feature that stores all of these records in one place. The *Patient Chart* can be divided into the following sections:

1. [Patient Demographics](Patient-Demographics-Guide.md)
2. [Clinical Profile](clinical-profile-record-patient-medical-history.md)
3. [Chart Navigation Bar](Patient-Chart-Navigation-Bar.md)
4. [Chronological Record](store-everything-in-chronological-record.md)

## **Creating a new patient chart**

To create a new patient chart:

1. Go to the [Practice Home](https://app.elationemr.com/patients/) page and click on the "New Chart" button in the gray navigation bar.
2. Fill in the patient's demographics details- especially the required fields of *legal first name*, *legal last name*, *date of birth*, *sex at birth* and *Provider assigned in practice*

   - **User Tips**:
     - If there is only one provider in the practice, the *Provider assigned in practice* will always default to that provider's name.
     - If you are provider creating a patient chart, the *Provider assigned in practice* will default to your own name regardless of how many providers there are in the practice.
     - If you are a staff creating a patient chart in a multi-provider practice, the *Provider assigned in practice* will default to the name of the provider you set as your *Default physician* under "Settings" >> "User Settings".
3. Review the [Patient Demographics Guide](Patient-Demographics-Guide.md#Tips) to learn more about the various demographics fields. The Patient Demographics Guide also has a guided video.
4. Click "Create & Open Chart" or "Create Chart" when done.

- **User Tip**: If you are searching for a patient in one of the Patient Search options and you do not see a chart for the patient in the search results, simply click the "Create a new patient chart with this name" button to create a new chart directly from the search.
   ![]()

**Important Note:**If you click one of the "Create Chart" options for a new chart that has the same first name, last name, date of birth, and sex at birth as another patient at your practice, you will receive an alert indicating that you could be creating a duplicate chart. You can open a new tab to review the potential duplicate by clicking into the blue text of the name in the alert.

![]()




## **Frequently Asked Questions (FAQ)**

#### **Can I block certain users from creating charts?**

You cannot block certain users from creating charts in Elation. All users can create charts.

#### **Can I see who created a patient chart?**

You can use the Audit Log feature to look up who created a patient chart. However, you must know the approximate date it was created. To use the Audit Log feature:

1. Open the patient's chart
2. Click the "More" button at the top of the patient's chart
3. Click "Data Exchange" >> "Audit Logs"
4. Once the Audit Log window opens, set the "Start date" and "End date" of the timeframe you wish to search
5. Look for the *Action* "add" and the *Record Type* "Patient"
6. Once you find the record, look under the *Performed By* column to see who performed the action.




## **Related Articles**

- [Patient Demographics Guide](Patient-Demographics-Guide.md)
- [Patient List Report Guide- Searching your patient panel](find-patients-with-elations-patient-list.md)