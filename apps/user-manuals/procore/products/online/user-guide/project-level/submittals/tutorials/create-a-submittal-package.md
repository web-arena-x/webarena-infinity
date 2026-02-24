# Create a Submittal Package - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal-package

---

## Objective

To create a new [submittal package](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Package "references/construction-management/glossary-of-terms#Submittal Package").

## Background

A *submittal package* is a container that stores one or more *submittals*. Typically, a *general contractor* creates submittal packages that list all of the individual submittals specific to a particular trade or *subcontractor*. For example, one might create a submittal package to contain all of the plumbing-related submittals in a commercial building project.

## Things to Consider

- **Required User Permissions:**
 - *To create a submittal package:*
    - 'Admin' level permissions on the Submittals tool. 
      OR
    - 'Read Only' or 'Standard' level permissions on the Submittals tool with the ['Create Submittal Package' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Submittals "Grant Granular Permissions in a Project Permissions Template") enabled on your permissions template.
- **Limitations:**
 - A submittal can only be added to one (1) submittal package. However, you can move a submittal from one package to another when editing the submittal. See [Edit a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/edit-a-submittal "Edit a Submittal").

## Steps

1. Navigate to the project's ﻿**Submittals**﻿ tool.
2. Click ****+Create > Submittals Package****﻿.
3. In the 'General' tab, complete the data entry in the 'General Information' area as follows: 
   *Note:* An asterisk (\*) denotes a required field.
   - **Title:** Enter a descriptive name for the submittal package.
   - **Spec Section:** Depending upon whether the Project level Specifications tool (see [Specifications](https://support.procore.com/products/online/user-guide/project-level/specifications "products/online/user-guide/project-level/specifications")) is enabled or disabled on the project, choose one of these options:
     - *If the Specifications tool is enabled on the project:* Select the appropriate spec section for the submittal package from the drop down list. 
       *Note:* If you want to create a new Spec Section in the Specifications tool, click the **Create New Spec Section** option. In the Create New Specification Section window, enter a new **Spec #** (this is a required field) and **Description**. Then click **Create Spec Section**. 
       OR
     - *If the Specifications tool is not enabled on the project:* Type the corresponding spec section number for the submittal in the field. The number you enter here should always correspond to the appropriate section of the project's spec book.
   - **Number:** Enter a number for the submittal package. The system automatically fills in this field with the next available number, but you can enter a different number. 
     *Note:*If you enter a number already used for another submittal package, the 'Duplicate Numbers' window displays.
     - To use the next available number for the submittal package, click **Use Next Available**. 
       OR
     - To use the duplicate number you entered for the submittal package, click **Continue**. 
       OR
     - To use a different and unique number for the submittal package, click **Cancel** and enter a new number for the submittal package.
   - **Description****:** Enter a descriptive summary about the submittal package. This description is visible to the reviewers designated in the Design Team Workflow, the responsible subcontractor, and members of the package's distribution list.
   - **Package Attachments:** Choose from these options to add file attachments to the submittal item:
     - *To move files from your computer or a network location into Procore*, select the desired file(s) and use a drag-and-drop operation to place them in the grey **Drag and Drop File(s)**area.
     - *To select a file stored in the Drawings tool* (see [Drawings](https://support.procore.com/products/online/user-guide/project-level/drawings "/products/online/user-guide/project-level/drawings")), click **Attach File(s)**and choose**Select a Drawing from Procore** from the shortcut menu.
     - *To select a file stored in the Documents tool*(see [Documents](https://support.procore.com/products/online/user-guide/project-level/documents "/products/online/user-guide/project-level/documents")), click **Attach File(s)** and choose **Select a File from Procore** from the shortcut menu. 
       *Note*: If your company has integrated third-party tools with Procore, additional options may appear in the shortcut menu.
     - *To upload a file from your computer*, click **Attach File(s)**and choose **Upload a File From Your Computer** from the shortcut menu.
4. If you want to add one or more existing submittals to this package, see [Add an Existing Submittal to a Submittal Package](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/add-an-existing-submittal-to-a-submittal-package "Add an Existing Submittal to a Submittal Package").
5. If you want to create a new submittal in this package, see [Create a New Submittal in a Submittal Package](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-new-submittal-in-a-submittal-package "Create a New Submittal in a Submittal Package").
6. Click **Create Package**.  
   A GREEN banner appears to confirm that the system successfully created the new submittal package.

## See Also

- [Edit a Submittal Package](/products/online/user-guide/project-level/submittals/tutorials/edit-a-submittal-package "Edit a Submittal Package")
- [Bulk Edit Submittals in a Submittal Package](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/bulk-edit-submittals "Bulk Edit Submittals in a Package")
- [Send a Submittal Package for Review](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/send-the-submittals-in-a-package-for-review "Send a Submittal Package for Review")