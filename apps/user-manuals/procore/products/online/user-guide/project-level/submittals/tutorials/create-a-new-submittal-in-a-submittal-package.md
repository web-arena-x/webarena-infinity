# Create a New Submittal in a Submittal Package - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-new-submittal-in-a-submittal-package

---

## Objective

To create a new submittal in a [submittal package](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Package "references/construction-management/glossary-of-terms#Submittal Package").

## Background

A *submittal package* is a container that stores one or more *submittals*. Typically, a *general contractor* creates submittal packages that list all of the individual submittals specific to a particular trade or *subcontractor*. For example, one might create a submittal package to contain all of the plumbing-related submittals in a commercial building project.

## Things to Consider

- **Required User Permission**:
  - 'Admin' level permissions to the project's Submittals tool.
- **Prerequisite:**
  - Complete the steps in [Create a Submittal Package](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal-package "Create a Submittal Package").
- **Limitation**:
  - A submittal can only be added to one submittal package. However, you can move a submittal from one submittal package to another when editing the submittal.
- **Additional Information**:
  - After a submittal package is created, a user with 'Admin' level permission to the Submittals tool can use the **Create Revision** button to revise the submittal package.

## Steps

1. Navigate to the project's **Submittals** tool.
2. Click the **Packages** tab.
3. Locate the desired submittal package and click **Edit**.
4. Click **Create Submittal**.
5. Complete the following data entry:  
   *Note*: An asterisk (\*) denotes a required field.
   - **Title**. The descriptive name that best summarizes the information in the submittal.
   - **Private**. Place a mark in the **Visible Only to Admins, Workflow, and Distribution List Members** checkbox. This limits who can view the submittal in Procore.
   - **Spec Section**. Denotes the corresponding section from the project's specifications book. See [Where do the selections in the 'Specification Sections' drop-down list in the Submittals tool come from?](https://support.procore.com/faq/where-do-the-selections-in-the-spec-sections-drop-down-list-come-from "Where do the selections in the 'Spec Sections' drop-down list in the Submittals tool come from?")
   - **Type**: Select the submittal type from the list.
   - **Number & Revision**: Procore automatically assigns the submittal item a number and revision. If this is the first submittal item being created in the package, it is assigned the number one (1). If this is the first revision of the item in the package, it is assigned revision number zero (0). For subsequent submittal items and submittal item revisions, the number is increments by a value of one (1).
   - **Status**: Define the state of the submittal in the Status box. You have these options:
     - **Open**(Default). Select this option to indicate that the submittal is waiting for approvers to respond.
     - **Draft**. Select this option to indicate that the submittal has been created but has not yet entered the submittal review and [approval workflow](../../../../../../references/construction-management/glossary-of-terms.md#Approval_Workflow "/references/construction-management/glossary-of-terms#Approval_Workflow").
     - **Closed**. Select this option after both the submittal and the subcontractor is approved to perform the contracted work.   
       (*Note*: A user with 'Admin' level permissions to the company's Admin tool can create custom statuses for use with the Project level Submittals tool. See [Create a Custom Submittal Log Status](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-custom-submittal-log-statuses "products/online/user-guide/company-level/admin/tutorials/create-a-custom-log-status").)
   - **Responsible Contractor**: ﻿Select the responsible company or vendor from the list. Typically, this is the contractor (or subcontractor).
   - **Received From**. The contact for the responsible contractor who provided the submittal information to the project team.
   - **Submittal Manager**: Select the name of the person responsible for managing the submittal throughout its lifecycle. This is a required field. The default entry for this field is the submittal creator.
   - **Attachments**: Choose from these options to add file attachments to the submittal item:
     - *To upload a file from your computer*, click **Attach File(s)**and choose **Upload a File From Your** **Computer** from the shortcut menu.
     - *To select a file stored in the Documents tool*(see [Documents](https://support.procore.com/products/online/user-guide/project-level/documents "/products/online/user-guide/project-level/documents")), click **Attach File(s)** and choose **Select a File from Procore** from the shortcut menu.
     - *To select a file stored in the Drawings tool* (see [Drawings](https://support.procore.com/products/online/user-guide/project-level/drawings "/products/online/user-guide/project-level/drawings")), click **Attach File(s)**and choose **Select a Drawing** from Procore from the shortcut menu.   
       *Note*: If your company has integrated third-party tools with Procore, additional options may appear in the shortcut menu.
     - *To move files from your computer or a network location into Procore*, select the desired file(s) and use a drag-and-drop operation to place them in the grey **Drag and Drop File(s)**area.
6. Click **Create & Add to Package**.

## See Also

- [Send the Submittals in a Package for Review](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/send-the-submittals-in-a-package-for-review "Send the Submittals in a Package for Review")
- [Edit a Submittal Package](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/edit-a-submittal-package "Edit a Submittal Package")
- [Bulk Edit Submittals in a Package](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/bulk-edit-submittals "Bulk Edit Submittals in a Package")
- [Edit a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/edit-a-submittal "products/online/user-guide/project-level/submittals/tutorials/edit-a-submittal-item")