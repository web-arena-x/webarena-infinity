# Elation Note Guide - Managing Elation Note Templates

Source: https://help.elationhealth.com/s/article/Elation-Note-Guide-Managing-Templates

---

# **Contents**

- [Overview](#overview)
 - [What are Elation Note Templates?](#description)
 - [What templates are made available through Elation’s template library?](#library)
- [Workflow Instructions](#workflows)
 - [Creating an Elation Note Template](#create)
 - [Editing an Elation Note Template](#edit)
 - [Deleting an Elation Note Template](#delete)
 - [Adding an Elation Note Template to a draft note](#addtonote)
- [Frequently Asked Questions (FAQ)](#faq)

#

# **Overview**

## **What are Elation Note Templates?**

Templates are prebuilt, reusable formats designed for specific visit types—like annual wellness exams—or procedures where documentation can follow a consistent structure. They help reduce manual typing, prevent omissions, and support a smooth, organized workflow during the visit.

The Elation Note has its own template builder that lets you take advantage of both standard and custom blocks to create more flexible, structured templates.

ℹ️   **NOTE** Legacy visit note templates are still supported in the Elation Note and can be applied by typing the **/template** command into the note. If you need to edit a legacy visit note template, refer to the instructions on [this Help Center page](https://help.elationemr.com/s/article/elation-visit-note-templates#CreateTemplate).

## **What templates are made available through Elation’s template library?**

When your Elation account is first set up, it will come preloaded with the following Elation Note templates:

- \*E Medicare Annual Wellness Visit - AWV

ℹ️  **NOTES**

- The ability to edit the **\*E Medicare Annual Wellness Visit – AWV** template from Elation’s Template Library will be available soon.
- The **\*E Medicare Annual Wellness Visit – AWV** template won't populate values for hosted database customers. Support for this data through the hosted database will be available soon.

# **Workflow Instructions**

## **Creating an Elation Note Template**

| | |
| --- | --- |
| **1** | In the blue navigation bar at the top of your Elation account, click your **email address** followed by **Settings**. |
| **2** | In the left-hand navigation menu, click the **Elation Note Templates** page. |
| **3** | Click **+ Create Template**. A pop-up window will appear with what resembles a blank Elation Note. |
| **4** | Fill in the mandatory **Template name** field with a description that will help you search for and identify this template in the future. |
| **5** | Add any of the following types of content to the template:   - Blocks (both standard and custom)   - Use the **+ Add Block** button and select from the dropdown menu or press the forward slack (**/**) key on your keyboard to search for a block. [Click here for more information on how to add blocks to a template or draft note](https://help.elationemr.com/s/article/Elation-Note-Guide-Using-visit-note-blocks#add).   - Within the block, add as much or as little content as you’d like to populate the template. You can type this content directly or copy and paste text from another source. - Free-text   - Outside any of the blocks, you can free-text any content. The same workflows for adding text directly to a draft note apply to the creation of a template. [Click here for more information](https://help.elationemr.com/s/article/Elation-Note-Guide-Documenting-an-encounter#typedirectly). - Dynamic Macros   - Use the at sign (**@**) key on your keyboard to insert dynamic fields into any standard block or text field to insert any of the following real-time patient data into your visit note.     - **Clinical Profile (Allergies)**       - Bulleted list of active allergies from the **Allergies** section of the Clinical Profile.     - **Clinical Profile (Medications)**       - Bulleted list of active, permanent medications from the **Permanent Rx Meds** section of the patient's Clinical Profile.     - **Clinical Profile (Problems)**       - Bulleted list of active problems from the **Problem List** section of the patient's Clinical Profile.     - **Patient age**       - Patient's age at the time of visit.     - **Patient DOB**       - Patient's **Date of birth** from their Demographics.     - **Patient name**       - Patient's **Legal first name**, **Middle name** & **Legal last name** from their Demographics.   - When a template containing a dynamic macro is applied to a visit note, any @ fields will automatically be replaced with the corresponding patient data. |
| **6** | Click **Save & Close** to complete. |

ℹ️   **EXCEPTIONS** Dynamic macros cannot be used in custom blocks, Vitals fields, structured PE and ROS fields or anywhere outside of the Elation Note draft or template builder.

## **Editing an Elation Note Template**

| | |
| --- | --- |
| **1** | Locate the Template on the Settings page. |
| **2** | Click the **pencil** icon. |
| **3** | Make edits in the pop-up window. |
| **4** | Click **Save & Close**. |

####

**Deleting an Elation Note Template**

| | |
| --- | --- |
| **1** | Locate the Template on the Settings page. |
| **2** | Click the **trash can** icon. |

ℹ️   **CAUTION** Delete with caution as deleted templates cannot be restored.

####

## **Adding an Elation Note Template to a draft note**

[Click here to learn how to add a Template to an Elation Note.](https://help.elationemr.com/s/article/Elation-Note-Guide-Documenting-an-encounter#Template)

#

# **Frequently Asked Questions**

#### **Is it possible to duplicate an Elation Note Template to make a new one?**

You cannot duplicate an Elation Note Template to make a new one. This feature is coming soon!

**Is there an easy way to convert a legacy visit note template to an Elation Note Template?**

At this time, a legacy visit note template must be manually converted to an Elation Note Template. You can still apply a legacy visit note template to the Elation Note.

**Can I add dynamic macros to a custom block?**

No, dynamic macros cannot be added to a custom block.

**Can I add more dynamic macros?**

No, additional dynamic macros cannot be added. Let us know what macros you’d like to see in Elation by sending us feedback via the **I need help** button.

**Can I create a new PE or ROS template from the Elation Note?**

No, you cannot create a new PE or ROS template from the Elation Note. Open a legacy note, create the new PE or ROS template there, and you’ll be able to apply it to any Elation Note moving forward.

**Is there a library of Templates I can access?**

Elation has a few sample templates that will be made available to all customers soon.

**Can Elation create a template for me?**

Elation cannot create templates for you.

#### **If I delete a custom block that was added to a Template, what happens to the Template?**

If you need to delete a custom block, we recommend reviewing your templates and removing the custom block first. If you don’t remove a custom block from a template before deleting the custom block, the template, draft and signed note will show an empty block where the custom block used to be. Our team will be working on a fix for this soon.

# **Related Articles**

- [Elation Note Introduction](Elation-Note.md)
- [Elation Note Guide - Managing custom blocks](https://help.elationemr.com/s/article/Elation-Note-Guide-custom-blocks)
- [Elation Note Guide - Using visit note blocks](https://help.elationemr.com/s/article/Elation-Note-Guide-Using-visit-note-blocks)
- [Elation Note Guide - Documenting an encounter](https://help.elationemr.com/s/article/Elation-Note-Guide-Documenting-an-encounter)
- [Elation Note Guide - Release Summary](Elation-Note-Release-Summary.md)