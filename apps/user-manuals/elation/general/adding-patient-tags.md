# Patient Tags Guide- Classifying patients for administrative efficiency

Source: https://help.elationhealth.com/s/article/adding-patient-tags

---

## **Contents**

- [What are Patient Tags?](#description)
- [Using Patient Tags](#using_tags)
 - [Applying Patient Tags to a patient's chart](#adding_tags_to_charts)
 - [Editing or removing removing Patient Tags from a patient's chart](#editing_or_removing_tags_from_charts)
 - [Creating Patient Tags from the patient's chart](#creating_tags_from_chart)
- [Managing the *Patient Tags* Settings page](#settings)
 - [​​​​​​​Premium EHR features](#premium_EHR)
- [Common Use Cases](#common_use_cases)
 - [Common ways Elation customers use Patient Tags](#common_tags)
 - [Special Patient Tags](#special_tags)
 - [Running reports on applied Patient Tags](#patient_list_report)
- [Frequently Asked Questions (FAQ)](#FAQ)

## **What are Patient Tags?**

Patient Tags is a feature that allows you to add classification labels (or tags) to a patient's chart. Patient Tags will allow you to see short notes about your patients without having to open their patient demographic section. You can also use the Patient List Report to easily search for patients by the Patient Tags in their chart.

Patient Tags are located underneath the patient's name & date of birth in the patient chart.
![]()

## **Using Patient Tags**

### **Applying Patient Tags to a patient's chart**

1. Open a patient's chart & find the patient's name
2. Click the "+" button underneath the patient's name and date of birth or click existing Patient Tags to apply additional Patient Tags.
3. Type in any phrase in the *Edit Patient Chart Tags* box to search for Patient Tags in your database.
4. Select the Patient Tag from the database to apply it to the patient's chart.
   - If the tag you want to add is not in the database, follow the [add new tag](#add_from_search) instructions to add it to your database first.
5. Continue selecting Patient Tags until you are done.
6. Click "Update Tags" to save your changes.

### **Editing or removing removing Patient Tags from a patient's chart**

1. Open a patient's chart & find the patient's name.
2. Click existing Patient Tags to edit or remove Patient Tags.
3. Click the "x" button next to any Patient Tag(s) you want to remove to remove the Patient Tag(s).
4. Add new Patient Tags to replace any of the ones you removed if needed.
5. Click "Update Tags" to save your changes.

**User Tips**:

- If you want to edit the name of a specific Patient Tag in your database, see the [*Managing the Patient Tags Settings page* section](#settings) below.
- If you want to delete a Patient Tag from your database, see the [*Managing the Patient Tags Settings page* section](#settings) below.



**Creating Patient Tags from the patient's chart**

You can create the Patient Tags directly from the *Edit Patient Chart Tags* box:

1. Type out the exact name of the new tag in the *Edit Patient Chart Tags* box.
2. Click "Create tag..." to add the new tag to your database.

![]()

1. Click "Update Tags" to save your new tag to the patient's chart.

## **Managing the *Patient Tags* Settings page**

The *Patient Tags* settings page will allow you to add, edit, merge and remove Patient Tags.

- Click "+ Add Patient Tag" to add a new Patient Tag to your database at any time.
- Click "edit" next to a Patient Tag to edit the name of Patient Tag.
 - Editing a Patient Tag will trigger an update to all associated Patient Tags in the patient's chart.
- Click "merge" to merge the Patient Tag with another Patient Tag in your database.
 - Merging a Patient Tag will trigger an update to all associated Patient Tags in the patient's chart.
- Click "remove" to delete the Patient Tag.
 - Removing (deleting) a Patient Tag from the *Patient Tags* Settings page will not delete the Patient Tag from any charts where the Patient Tag is in use. If you want to remove the deleted Patient Tag from patient charts, use the [Patient List Report](find-patients-with-elations-patient-list.md) to find all patients that have the deleted Patient Tag and individually remove the Patient Tag from each chart.
 - Deleted Patient Tags will no longer appear in the Patient Tag search.

####

### **Premium EHR features**

Premium EHR users can enable a Setting to only allow Admin Level Users to make edits to the *Patient Tags* Settings page. Once enabled, only Admin Level Users can add, edit or remove Patient Tags from the *Patient Tags* Settings page in their Elation Settings. Non-Admin Level Users will only be able to view the Settings page but will not be able to edit.


**Important Note**: This feature is part of Elation's Premium EHR offering. Once this feature is activated it will take effect immediately.

- If you are already a Premium EHR user and you are interested in using this feature, click the "I need help" button to notify Elation and a member of the Elation Team will activate the feature for you.
- If you are interested in upgrading to Premium EHR to use this features, click the "I need help" -> "Contract Elation Support" button and a member of the Elation team will assist you.




## **Common Use Cases**

### **Common ways Elation customers use Patient Tags**

- Noting the name of the care facility or hospital that the patient is residing in
- Noting care directives
- Noting special details about the patient such as
 - time frames in which the patient is available for contact
 - names of care takers

### **Special Patient Tags**

1. Elation has two special tags that are preloaded for two care directives to allow you to easily identify these instructions in the chart
   - Physician Orders for Life-Sustaining Treatment (POLST)- The tag is called *POLST*and will display in pink.
   - Do not resuscitate (DNR)- The tag is called *DNR* and will display in red.
2. If you use certain integrations with Elation, the integration can create Patient Tags on your behalf for certain functions. Depending on the integration, special tags created by the integration cannot be edited or removed.

### **Running reports on applied Patient Tags**

Patient Tags is a filter that can be used in the Patient List Report to help you search for patients based on the way you classify them using tags. See the [Patient List Report Guide- Searching your patient panel](find-patients-with-elations-patient-list.md) article for more details on how to use Patient Tags as a filter.

## **Frequently Asked Questions**

#### **Can I add color to Patient Tags I created?**

You cannot add color to tags you create. All tags will display in gray except for the [two special care directive tags](#special_tags) noted above.

#### **Is there a way for me to delete all the Patient Tags from my database and start fresh?**

You can only remove Patient Tags from the database one at a time. We recommend using the "edit", "merge", and "remove" buttons on the [*Patient Tags* settings page](https://app.elationemr.com/settings/patient-tags/) to manage your Patient Tags database and keep each tag unique and distinct.

- Removing (deleting) a Patient Tag from the *Patient Tags* Settings page will not delete the Patient Tag from any charts where the Patient Tag is in use. If you want to remove the deleted Patient Tag from patient charts, use the [Patient List Report](find-patients-with-elations-patient-list.md) to find all patients that have the deleted Patient Tag and individually remove the Patient Tag from each chart.
- Deleted Patient Tags will no longer appear in the Patient Tag search.

#### **What happens to Patient Tags in the patient's chart when I merge charts?**

When you use Elation's [merge chart feature](https://help.elationemr.com/s/article/merging-duplicate-charts) to combine multiple charts into one, Patient Tags will also be combined so that tags from all charts will be in the merged chart.



**Next Step**

**Explore the Patient Tag feature and start classifying your patients for administrative reporting.**





## **Related Articles**

- [Patient List Report Guide- Searching your patient panel](find-patients-with-elations-patient-list.md)
- [Document Tags for Visit Notes & Reports Guide](tag-reports-and-notes-with-document-tags.md)