# Patient Forms Guide - Creating and managing Patient Forms

Source: https://help.elationhealth.com/s/article/Patient-Forms-Guide

---

# **Contents**

- [Overview](#overview)
 - [Does Elation have pre-built Patient Forms and questions?](#pre-built_forms)
 - [How do I create my own Patient Forms?](#create_forms)
 - [Anatomy of a Patient Form](#anatomy)
- [Setup](#setup)
 - [Specifying who can create or edit forms](#create_permissions)
 - [Specifying who can sign off on completed forms](#sign_permissions)
- [Workflow Instructions](#workflows)
 - [Generating a Patient Form draft from a PDF or image](#upload_form)
 - [Creating a Patient Form from scratch or from a template](#create_forms)
 - [Using pre-defined sections](#pre-defined_ections)
 - [Using prebuilt questions](#pre-built_questions)
 - [Creating your own questions](#own_questions)
 - [Using a Patient Form Template](#template)
 - [Managing the Patient Forms List](#managing_forms)
 - [Editing Patient Forms](#editing_forms)
 - [Deleting Patient Forms](#deleting_forms)
- [Frequently Asked Questions (FAQ)](#FAQ)

# **Overview**

## **Does Elation have pre-built Patient Forms and questions?**

Yes, Elation has the following pre-built Patient Forms templates:

- New Patient Medical History
- Follow-up Medical History
- Demographics
- Insurance Information
- COVID-19 Screening
- Medicare AWV

Each template is associated with a set of pre-built questions. You can customize any of the templates to fit your needs and create your own personalized versions of these forms.

## **How do I create my own Patient Forms?**

Use the Patient Forms builder to create your own Patient Forms. You can build forms in several ways:

- Use pre-built templates, sections, and questions.
- Create your own questions and sections from scratch.
- Covert a PDF or image of a form into a structured form.

See below for step-by-step instructions.

## **Anatomy of a Patient Form**

Here are the core components of a Patient Form as it’s being built.

![]()

| | | | |
| --- | --- | --- | --- |
| **Letter** | **Name** | **Description** | **Visible to patients?** |
| A | Form Name | Internal name of the form. | No |
| B | Sign-off permission indicator | Enables Staff Level Users to sign off on patient responses. | No |
| C | Title (What patient sees) | External name of the form. | Yes |
| D | Form Description | Description of the form. | Yes |
| E | Section | Organizes related questions together. Each form can have multiple sections.   - To move the section to a new location in the form, click and hold the **Grid** icon, drag the section to its new location and then let go of your cursor. | Yes   - Each section is separated by a horizontal line. |
| F | Section Title | Internal title of the section. | No |
| G | Exports to preference | Defines where responses from this section can be exported to in the patient’s chart. | No |
| H | Section shortcut (delete) | Deletes the section. | No |
| I | Intro Text (What patient sees) | Provides context or explanation for the upcoming question(s). | Yes |
| J | Question | The item that asks for specific information or a response from the patient. Each section can have multiple questions.   - To move the question to a new location in the section, click and hold the **Grid** icon, drag the question to its new location and then let go of your cursor. | Yes |
| K | Question Text | The prompt that you want the patient to answer. | Yes |
| L | Answer Helper Text | Example(s) of what the patient can input as an answer. E.g. If you want the patient to enter their Date of Birth as a two digit month, two digit date and four digit year, enter the **Answer Help Text** as 'MM/DD/YYYY'. | Yes |
| M | Question type description | Describes the answer format for the question. | No |
| N | Question shortcuts (copy & delete) | Options to duplicate the question to create a similar question or delete the question. | No |
| O | Question settings | Specify additional preferences for the question format. (Only available for the **Checkbox List Question** format.) | No |
| P | Delete icon | Deletes the answer option. | No |
| Q | Add answer option icon | Adds an answer option. | No |
| R | Add question | Adds a new question to that section. | No |
| S | Add section | Adds a new section. | No |
| T | Add predefined section | Add a predefined section to the form. | No |
| U | Save changes | Save form edits. | No |
| V | Back | Return to the Patient Forms list. | No |

# **Setup**

## **Specifying who can create or edit forms**

By default, anyone in the practice can create or edit Patient Forms. If preferred, you can set it so that only [Admin Level Users](https://help.elationemr.com/s/article/administrative-privileges) can configure patient forms by following these steps:

| | |
| --- | --- |
| **1** | Go to **Settings** -> **Patient Forms**. |
| **2** | Click the **Admin only** toggle until it turns green (ON). |

Changes to this setting will be applied immediately.

## **Specifying who can sign off on completed forms**

By default, only Provider Level Users can sign off on forms responses. For each Patient Form, Admin Level Users can enable a setting that allows Staff Level Users to sign off on its form responses. This feature is ideal for forms that generally do not require provider oversight such as forms for demographics or insurance collection.

To allow staff to sign off on a specific patient form, check the box labeled **This form does not require provider sign-off** when editing that form.

# **Workflow Instructions**

## **Generating a Patient Form draft from a PDF or image**

| | |
| --- | --- |
| **1** | Go to **Settings** -> **Patient Forms**. |
| **2** | Click **Create from PDF or Image**. |
| **3** | Select the PDF or image of your form from your device and click **Open**.   - Supported languages are English, German, French, Spanish, Italian and Portuguese. |
| **4** | A new browser tab will open to generate a draft of the form. **Do not close this tab** until the draft is complete, or the form will not be generated. |
| **5** | Once the draft is generated, review the internal **Form Name** in the upper lefthand corner. This name will only be seen by members of your practice. |
| **6** | **(Admin Level  User Only)** Specify whether the completed form requires sign-off from a Provider Level User by checking or unchecking the **This form does not require provider sign-off** box.   - [Click here for information about this setting](#sign_permissions). |
| **7** | Review the external **Title** and **Form Description**. These will be visible to your patients while they fill out the form. |
| **8** | Review each section and make adjustments as needed.   - Adjust the section title as needed. - Adjust where you want the section responses to export to, if allowed. - Add question(s) to the section, see step #9 below. Each section must have at least one question. |
| **9** | Review each question and make adjustments as needed.   - Add a custom question by clicking **+ Add question**.   - [Click here for more information about adding custom questions](#own_questions).   - To reorganize questions, click and hold the **Grid** icon, drag the question to its new location in the same section and then let go of your cursor. Questions cannot be moved across sections.   - Specify where the responses should export to by default in the **Export to** field.     - You will not be able to edit the default export to location for all prebuilt questions except ‘Other’. |
| **10** | Click **Save form** to save any changes. |
| **11** | Click the **back arrow** to return to the main Settings page. |

## **Creating a Patient Form from scratch or from a template**

| | |
| --- | --- |
| **1** | Go to **Settings** -> **Patient Forms**. |
| **2** | Choose how you want to build your form:   - To select a template from the dropdown to use a prebuilt form as a starting point., click **Create from Template**.   - [Click here to learn more about form templates](#template). - To start building from scratch, click **Create a Blank Form**. |
| **3** | Fill out the internal **Form Name** in the upper lefthand corner. This name will only be seen by members of your practice. |
| **4** | **(Admin Level  User Only)** Specify whether the completed form requires sign-off from a Provider Level User by checking or unchecking the **This form does not require provider sign-off** box.   - [Click here for information about this setting](#sign_permissions). |
| **5** | Give the form a **Title** and **Form Description**. Both are visible to the patient. |
| **6** | Customize the sections of your form.   - Templates come with certain predefined sections, predefined export to settings and pre-built questions.   - You can only edit the default export to location for the ‘Other’ predefined section. - A blank form will start you off with a blank section. - Click **+ Add section** to add a custom section.   Customization options include   - Adjusting the **Section Title** & **Intro Text**. - Selecting where the responses export to in the patient's chart.   - Only certain predefined sections can be exported to patient demographics fields. - Adding questions (see step #7 below). Each section must have at least one question. - Changing the order in which the sections display in the form using the **Grid** icon. |
| **7** | Customize the questions of your form:   - Templates come with certain predefined sections, predefined export to settings and pre-built questions.    - You can only edit the default export to location for the ‘Other’ predefined section. - A blank form will start you off with a blank section where you must add at least one question. - Click **+ Add question** to add a custom question to any section.   - [Click here for more information about adding custom questions](#own_questions).   To reorganize questions, click and hold the **Grid** icon, drag the question to its new location in the same section and then let go of your cursor. Questions cannot be moved across sections. |
| **8** | Click **Save form** to save any changes. |
| **9** | Click the **back arrow** to return to the main Settings page. |

## **Using pre-defined sections**

Each pre-defined section includes a title, default export settings for responses, and one or more pre-set questions. Each predefined section can only be added once to a patient form except for 'Other'.

| | |
| --- | --- |
| **1** | Click **Add predefined section** to add a predefined section. |
| **2** | Customize the **Section Title** & **Intro Text**. |
| **3** | Adjust where you want the section responses to export to it you are using the 'Other' section. |
| **4** | Review the pre-built questions that come with the predefined section.   1. Add a custom question by clicking **+ Add question**.    1. [Click here for more information about adding your own questions](#own_questions). 2. Copy a pre-built question to use it as a starting point for a similar question using the **copy** icon. |

Other customization options include:

- To delete a predefined section, click the **trash can** icon.
- To move the predefined section to a new location in the form, click and hold the **Grid** icon, drag the section to its new location and then let go of your cursor.

## **Using prebuilt questions**

Prebuilt questions are designed to collect structured data that fits directly into areas of the chart like Demographics, Clinical Questionnaires, Medication Lists, and Health Maintenance. Each prebuilt question is formatted to suit the type of information being collected. For example, the **Medical History** question uses checkboxes so patients can easily select the conditions they have.

Some prebuilt questions cannot be edited because they are either formatted for the areas they must export to (e.g. **Demographics: Preferred Language**) or they are standard instruments with pre-configured scoring (e.g. **Depression (PHQ-2)**).

Responses to prebuilt questions will be exported to the located defined by the section it is in. You can’t edit the default export destination for prebuilt questions, except for those located in the ‘Other’ predefined section.

## **Creating your own questions**

Create custom questions to collect information that’s specific to your practice, workflows, or patient population. Responses to custom questions will be exported to the located defined by the section it is in. [Click here to view sample use cases for Patient Forms](https://help.elationemr.com/s/article/Patient-Forms-Sample-Forms-and-Use-Cases).

The question formats available are:

| | | |
| --- | --- | --- |
| **Question Format** | **Use Case** | **Example** |
| Short answer | A single-line text field where the patient can type a brief, free-text response. | “What is the name and address of your preferred pharmacy?” |
| Patient signature | Allows patients to provide their electronic signature. | “Please sign below to consent to treatment.” |
| Dropdown Select | A list of options that appears when the patient clicks the dropdown menu. The patient can choose only **one** answer from the list. | “Select your primary language.” |
| Radio Select | A set of visible options displayed as circles. The patient can choose only **one** answer. | “What is your current smoking status?” |
| Checkbox | A list of options with checkboxes. The patient can choose **one or more** answers. You can also specify the following:   - **Allow free-text input accompanying each option** - **Include a pre-defined 'Other' choice** | “Which symptoms are you experiencing?” |
| Free-text list | Allows patients to enter several responses, saved as individual items. | “List any supplements you’re currently taking.” |

| | |
| --- | --- |
| **1** | Add a new question by clicking **+ Add question**. |
| **2** | Select the question format you want to use. |
| **3** | Customize the question and answer options.   - Add **Answer Help Text** as guidance for the patient if needed. (e.g. if you want the patient to enter their Date of Birth as a two digit month, two digit date and four digit year, enter the **Answer Help Text** as 'MM/DD/YYYY') - Click **+** to add additional answer options. - Click the **trash can** icon to delete unneeded answer options. |
| **4** | To reorder the questions, click and hold the **Grid** icon, drag the question to its new location and then let go of your cursor. |
| **5** | To copy a question to use it as a starting point for a similar question, click the **copy** icon. |

## **Using a Patient Form Template**

Templates come with predefined sections and questions to help you quickly create commonly used forms. To use a template simply click on the template name when creating a new form.

For example

- The **Demographics Template** allows you to collect information for certain demographics fields, such as the patient's preferred pronouns or emergency contact information, to maintain the most up to date demographics for each patient.
 - Only the sections and questions available in the **Demographics Template** can be exported to a patient's demographics. You cannot create your own questions for exporting to patient demographics fields.
- The **Medicare AWV Template** allows you to send patients a list of typical questions for a Medicare Annual Wellness Visit. This way, you can collect responses before the appointment and reference them in the note, streamlining the visit.

## **Managing the Patient Forms List**

Newly created forms will appear at the bottom of the **Manage Forms** list on the Patient Forms Settings page. To reorder your forms, click the **Grid**icon and drag and drop the form to a new location.

Each form displays the following details:

- Form title
- Creator and creation date
- Last modified by and last modified date
- Linked Appointment Types, if the form is attached to any

This makes it easy to track form updates and understand how each form is being used in your workflow.

## **Editing Patient Forms**

When you edit a form, any changes you make will automatically apply moving forward. Patients will see the updated version the next time they load the form.

| | |
| --- | --- |
| **1** | Go to **Settings** -> **Patient Forms**. |
| **2** | Click **Edit** next to the form you want to edit. |
| **3** | Make your edits and then click **Save form** to save any changes. |
| **4** | Click the **back arrow** to return to the main Settings page. |

## **Deleting Patient Forms**

ℹ️   **CAUTION** Deleted with caution as deleted forms cannot be restored. Deleting a form will immediately remove it from any linked appointment types. If the form was already sent to a patient, they may no longer be able to complete it—so make sure it’s no longer needed before deleting.

| | |
| --- | --- |
| **1** | Go to **Settings** -> **Patient Forms**. |
| **2** | Click **Delete** next to the form you want to delete. |
| **3** | Click **Delete** again to confirm. |

# **Frequently Asked Questions**

[Click here to view frequently asked questions about Patient Forms](https://help.elationemr.com/s/article/Patient-Forms-Frequently-Asked-Questions).

# **Related Articles**

- [Patient Forms Introduction](Getting-Started-with-Patient-Forms.md)
- [Patient Forms Guide - Sending forms to patients](https://help.elationemr.com/s/article/Sending-forms-to-patients)
- [Patient Forms Guide - Managing forms responses](https://help.elationemr.com/s/article/Managing-forms-responses)
- [Patient Forms Guide - Receiving and filling out forms as a patient](https://help.elationemr.com/s/article/Receiving-and-filling-out-forms-as-a-patient)
- [Patient Forms Guide - Sample Forms and Use Cases](https://help.elationemr.com/s/article/Patient-Forms-Sample-Forms-and-Use-Cases)
- [Patient Forms Guide - Frequently Asked Questions](https://help.elationemr.com/s/article/Patient-Forms-Frequently-Asked-Questions)
- [How to set up your Patient Booking Site](Patient-Booking-Site.md)
- [How to set up Elation Integrated Video](Elation-Telehealth-powered-by-Zoom.md)