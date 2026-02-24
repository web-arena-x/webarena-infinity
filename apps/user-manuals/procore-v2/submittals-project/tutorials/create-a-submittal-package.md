# Create a Submittal Package

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/create-a-submittal-package

---

## Background

A *submittal package* is a container that stores one or more *submittals*. Typically, a *general contractor* creates submittal packages that list all of the individual submittals specific to a particular trade or *subcontractor*. For example, one might create a submittal package to contain all of the plumbing-related submittals in a commercial building project.

## Things to Consider

- **Required User Permissions:**

  - *To create a submittal package:*\* 'Admin' level permissions on the Submittals tool.  
     OR\* 'Read Only' or 'Standard' level permissions on the Submittals tool with the ['Create Submittal Package' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Limitations:**

  - A submittal can only be added to one (1) submittal package. However, you can move a submittal from one package to another when editing the submittal. See [Edit a Submittal](/product-manuals/submittals-project/tutorials/edit-a-submittal).

## Steps

1. Navigate to the project's **Submittals** tool.
2. Click **+Create > Submittals Package** .
3. In the 'General' tab, complete the data entry in the 'General Information' area as follows:

   - **Title:** Enter a descriptive name for the submittal package.
   - **Spec Section:** Depending upon whether the Project level Specifications tool (see [Specifications](/product-manuals/specifications-project/)) is enabled or disabled on the project, choose one of these options:

     - *If the Specifications tool is enabled on the project:* Select the appropriate spec section for the submittal package from the drop down list. *Note:* If you want to create a new Spec Section in the Specifications tool, click the **Create New Spec Section** option. In the Create New Specification Section window, enter a new **Spec #** (this is a required field) and **Description**. Then click **Create Spec Section**.
     - *If the Specifications tool is not enabled on the project:* Type the corresponding spec section number for the submittal in the field. The number you enter here should always correspond to the appropriate section of the project's spec book.
   - **Number:** Enter a number for the submittal package. The system automatically fills in this field with the next available number, but you can enter a different number. *Note:* If you enter a number already used for another submittal package, the 'Duplicate Numbers' window displays.

     - To use the next available number for the submittal package, click **Use Next Available**.
     - To use the duplicate number you entered for the submittal package, click **Continue**.
     - To use a different and unique number for the submittal package, click **Cancel** and enter a new number for the submittal package.
   - **Description:** Enter a descriptive summary about the submittal package. This description is visible to the reviewers designated in the Design Team Workflow, the responsible subcontractor, and members of the package's distribution list.
   - **Package Attachments:** Do one of the following:

     - *To move files from your computer or a network location into Procore*, select the desired file(s) and use a drag-and-drop operation to place them in the grey **Drag and Drop File(s)** area.
     - *To select a file stored in the Drawings tool* (see [Drawings](/product-manuals/drawings-project/)), click **Attach File(s)** and choose **Select a Drawing from Procore** from the shortcut menu.
     - *To select a file stored in the Documents tool* (see [Documents](/product-manuals/documents-project/)), click **Attach File(s)** and choose **Select a File from Procore** from the shortcut menu.

       - *Note*: If your company has integrated third-party tools with Procore, additional options may appear in the shortcut menu.
     - *To upload a file from your computer*, click **Attach File(s)** and choose **Upload a File From Your Computer** from the shortcut menu.
4. If you want to add one or more existing submittals to this package, see [Add an Existing Submittal to a Submittal Package](/product-manuals/submittals-project/tutorials/add-an-existing-submittal-to-a-submittal-package).
5. If you want to create a new submittal in this package, see [Create a New Submittal in a Submittal Package](/product-manuals/submittals-project/tutorials/create-a-new-submittal-in-a-submittal-package).
6. Click **Create Package**. A GREEN banner appears to confirm that the system successfully created the new submittal package.