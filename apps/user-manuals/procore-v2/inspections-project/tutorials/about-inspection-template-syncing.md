# About Inspection Template Syncing

Source: https://v2.support.procore.com/product-manuals/inspections-project/tutorials/about-inspection-template-syncing

---

## Overview

In the past, inspection templates have been created at the Company level and added to the Project level. However, there has not been a mechanism to keep templates in sync across the Company and Project levels. In the absence of a syncing mechanism, over time edits to templates at the Company or Project level can cause templates to drift apart in their content and wording. This can impact the ability to perform inspections in a consistent way across projects and report on results to identify trends.

In order to address this, Procore released a new feature to keep Company level templates synced with Project level templates on February 13, 2017. Now, when a Project level Inspections tool Admin user is managing the inspection template library for a project, they can see the changes listed below.

## Benefits

- Benefits of this update include:

 - Establishing Company level standards while preserving Project level flexibility
 - Maintaining consistency in inspection procedures across projects
 - Enhancing reporting capabilities and trend analysis through company-wide standardization
 - Introducing the âDetailsâ field for inspection items
 - Introducing Project level inspection templates

## Key Changes

*Inspections created and/or performed prior to 2/13/17 will* ***not*** *be affected.*

- **At the Project level, an inspection template and information therein that was created at the Company level appears with a golden key icon next to it.** This indicates that the project inspection is synced to that company template, and any changes made to the template at the Company level will be synced to the template. Changes will only be synced to the template; changes will not impact the inspection once you [Create a Project level Inspection](/process-guides/project-equipment-user-guide/create-inspection-web).
- **Company level information can only be editable at the Company level** and are not editable at the Project level. This information includes Inspection Name, Type, Trade, Description, Attachments, Sections, and Inspection Items.
- **When editing a company template at the Project level, additional Project level information can be added to the template.** This includes Project level Description, Attachments, Sections, and Inspection Items. **Project level information is not synced with the Company level template.**
- **A new Details field is associated with every inspection item.** Details only appear in the Project level template and can be edited for Company level and Project level inspection items. This allows users to create a general inspection question (e.g., Confirm vapor barrier conforms with specifications and approved submittal) and then add project-specific details (e.g., Moisturbloc 6-mil Film Vapor Barrier Underlayment per approved submittal).
- **If a company template is edited at the Company level, those changes are synced to the corresponding template at the Project level for all projects using that company template.**

## Important to Know

- **What immediate changes can be expected following release of template syncing?**

 - If the project and company templates sharing a common name are exactly the same, then users will not see immediate changes to their project template content.
 - If the project and company templates sharing a common name have different Types or Trades, then the Type and/or Trade on the Project level template have been updated to the Type and/or Trade from the Company level inspection template.
 - If the project and company templates sharing a common name have different Sections or Inspection Items, then:\* Company level Sections and Inspection Items that were not previously on the Project level template have been added to the Project level template.\* Project level Sections and Inspection Items that do not match the company template will remain on the Project level template and be treated as Project level Sections and Inspection Items.
 - If a Project level template does not share a common name with a company template, it has become a Project level template and will not be synced with a Company level template.

## FAQ

- **Will my Company level information sync to the project level?**

 - Yes.
- **Will my Project level information sync to the company level?**

 - No.
- **Who should I contact if I want to make changes to a template?**

 - Contact an individual at your company who has Admin permissions on Inspections at the Company level.
- **Will this change inspections that I performed in the past?**

 - No. It will only affect the template from which your team will build inspections in the configure settings.
- **If I create a Project level template, can I push to the Company level?**

 - No. If you want to use a template on more than one project the best practice is to create the template at the company level.