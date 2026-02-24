# Create a Coordination Issue

Source: https://v2.support.procore.com/product-manuals/coordination-issues-project/tutorials/create-a-coordination-issue

---

## Background

Identifying and recording model issues early is critical for saving time and budget. By resolving these conflicts upfront, you significantly reduce the volume of RFIs and Change Events required later in the project. You can create a coordination issue from these Procore tools and products: Coordination Issues, Drawings, or Models in the Procore Web application, with the **Procore BIM Plugin** in AutodeskÂ® NavisworksÂ®, when using the NavisworksÂ® Clash Detective with Procore Clash Manager, or directly from the field using Augmented Reality for BIM on the Procore for Mobile iOS app.

## Things to Consider

- [Required User Permissions](https://v2.support.procore.com/process-guides/permissions-matrix/project-level-coordination-issues-permissions#:~:text=Create%20a%20Coordination%20Issue%0AWeb)
- **Additional Information**:

 - Your current view and any markups are captured when you click 'New Issue'. If you make changes to the view or markups, the system updates the snapshot.
 - Your environment may include custom fields and configurable fieldsets not documented here. See [What are configurable fieldsets and which Procore tools support them?](/faq-what-are-configurable-fieldsets-and-which-procore-tools-support-them)
 - AutodeskÂ® NavisworksÂ® cloud markup is not supported in the Procore BIM Plugin. See [Why canât I use the cloud redline tool in Navisworks?](https://support.procore.com/faq/why-cant-i-use-the-cloud-redline-tool-in-navisworks)

## Prerequisites

- To follow these steps from your AutodeskÂ® design software using the Procore BIM Plugin:

 - The Procore BIM Plugin must be installed on the WindowsÂ® computer running your AutodeskÂ® software. See [Download & Install](/product-manuals/procore-bim-plugins/download-install).
 - Link your NavisworksÂ® model to a specific Procore project. See [Associate a NavisworksÂ® Model with a Procore Project](/product-manuals/coordination-issues-project/tutorials/associate-a-navisworks-model-with-a-procore-project).
 - Add locations that match your coordination schedule to the Procore project. See [Add Locations to a Project](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project). For example, if your schedule breaks the project down by building, level, and zone (e.g., Building A > Level 3 > North Corridor), make sure the locations in the Project Admin tool mirror this.

## Video

## Steps

There are several ways to create a coordination issue. Choose the platform and tool that works best for you.

### Within the Procore Web Platform

- From the project's **Coordination Issues** tool **Show/Hide Details**

 1. Navigate to the **Coordination Issues** tool.
 2. Click **Create**.
 3. Complete these fields:

     - **Title\***. Enter a clear, descriptive issue title for your collaborators.
     - **Description**. Describe the issue. The entry is also saved as a viewpoint comment on the final NWD file.
     - **Location**. Select the issue location. To add a location to this list, see [Add Locations to a Project](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project) or [Import Locations Using the Procore BIM Plugin for RevitÂ®](/product-manuals/admin-project/tutorials/import-locations-using-the-procore-plug-in-for-revit) and [Edit Tiered Locations](/product-manuals/admin-project/tutorials/edit-multi-tiered-locations).
     - **Location**. Select the specific project area where the issue is located. The available options in this list are managed in the locations utility in the Project Admin tool.
     - **Assignee**: Select the person who is responsible for resolving the issue. The person must have 'Standard' or 'Admin' permissions on the Coordination Issues tool to be selected as an assignee.
     - **Watchers.** Select the members to notify by email about issue updates. Watchers must have 'Read Only' level permissions or higher on the tool.
     - **Due Date**. The targeted deadline for the issue resolution.
     - **Priority**. The urgency level. The system's pre-defined options are *Low*, *Medium*, *High*, *Critical*.
     - **Trade**. The discipline involved. The available options in this list are managed in the Trades utility in the Company Admin tool.
     - **Type**. The category of the issue used for reporting purposes. The system's pre-defined options are *Building Code*, *Clash*, *Client Feedback*, *Constructability*, *Coordination*, *Design Review*, *Existing Condition*, *Requirement Change*, and *Other*.
     - **Attachments**. Up to 20 images, PDFs, or documents relevant to the issue.
 4. Click **Create**. Procore creates a new issue in the *Open* status.
- From the project's **Drawings** tool **Show/Hide Details**

 1. Navigate to the project's **Drawings** tool.
 2. Find your drawing using one of these options:

     - From the **Current Drawings** tab, click the **Drawing No**. link to open it.
     - From the **Drawing Sets** tab, find the set, and click **View**. Then click **Drawing No**. to open it.
 3. Click **Markup** at the top of the viewer.
 4. In the markup toolbar, do one of the following:

     - **Drop a Pin for the Issue:** Click the **Pins** icon in the toolbar. If you don't see **Pins**, click **Photos** or **Punch** to expand the markup options, and then click **Issue.** Click a location on the drawing to open a shortcut menu.
     - **Link a Shape to the Issue:** Select a standard toolbar option (for example, **Cloud,** **Arrow**, **Text**). Draw the shape in the desired location on the drawing. Then click the **Paperclip** icon in popup toolbar and choose **Coordination Issue**. This opens a shortcut menu.
 5. In the shortcut menu, choose **Create New Coordination Issue** to open a new issue in the side panel. You also have the option to choose **Link to Existing Coordination Issue**.
 6. Type a **Title** (required) for the issue.
 7. Complete any other optional fields.
 8. When finished, click **Create**.   
     Procore adds your new markup to the drawing. Unless published, markups are only visible to you.

 ##### Tip

 **Ready to share your markup with others?** Click the markup that you added and choose **Publish.** This makes your new markup visible to your team and generates a snapshot for the coordination issue.

- From the project's **Models** tool **Show/Hide Details**

 1. Navigate to the project's **Models** tool.
 2. Click a model's tile to open it in the Model Viewer.
 3. Navigate to the area on the model where you want to create a coordination issue. For navigation tips, see [View a Model.](/process-guides/user-guide-publish-and-manage-models-from-the-documents-tool/view-models)
 4. Click the **Issues** icon to open the **Coordination Issues** side panel.
 5. Click the **Plus** icon at the top of the panel to create a new issue**.**
 6. *Optional:* To update the issue's snapshot, modify the model's field of view. Then, hover over the image in the side panel and click **Update Snapshot**.
 7. Complete these fields:

     - **Title**: Type a title for the issue. This is the first reference that collaborators see when reviewing an issue.
     - **Description**: Enter a description of the issue.
     - **Location**: Select the issue location.
     - **Due Date**: Set a due date on the calendar.
     - **Priority**: Select the issue priority. Options are: *Low*, *Medium*, *High*, *Critical.*
     - **Assignee**: Select the person who is responsible for resolving the issue. The person must have 'Standard' or 'Admin' permissions on the Coordination Issues tool to be selected as an assignee.
     - **Watchers.** Select the members to notify by email about issue updates. Watchers must have 'Read Only' level permissions or higher on the tool.
     - **Trade**: Select the relevant trade associated with the issue.
     - **Type**: Select the issue type. Options are: *Building Code*, *Clash*, *Client Feedback*, *Constructability*, *Coordination*, *Design Review*, *Existing Condition*, and *Other*.
     - **Attachments**: Click **Attach Files** or drag and drop a file to add an attachment.
 8. Click **Create**. Procore creates a new issue in the *Open* status. Once created, click in the side panel to view it in the Coordination Issues tool.

### Via the Procore BIM Plugin

- From **AutoDeskÂ® NavisworksÂ®** with the **Procore BIM Plugin****Show/Hide Details**

 1. Open a model in NavisworksÂ® and find the conflict or issue that needs to be tracked.
 2. Click the **Procore** tab.
 3. In the **Coordination Issues** ribbon, click **Coordination Issues**, and then click **New Issue**.

     ##### Â Note

     Clicking 'New Issue' captures your current view and any markups. This snapshot is live and automatically updates with any changes you make.

 - Complete these fields:

    - **Snapshot**. A snapshot of the conflict to track as a coordination issue.
    - **Title**. A brief summary of the issue. This field is required (\*).
    - **Description**. Detailed information about the issue to help the assignee understand the context.
    - **Location**. The specific project area where the issue is located. The available options in this list are managed in the locations utility in the Project Admin tool.
    - **Assignee**. The team member responsible for resolving the issue. The system limits this list to users with 'Read Only' level permissions or higher on the tool.
    - **Watchers.** Team members to notify by email about issue updates. The system limits entries to users with 'Read Only' level permissions or higher on the tool.
    - **Due Date**. The targeted deadline for the issue resolution.
    - **Priority**. The urgency level. The system's pre-defined options are *Low*, *Medium*, *High*, *Critical*.
    - **Trade**. The discipline involved. The available options in this list are managed in the Trades utility in the Company Admin tool.
    - **Type**. The category of the issue used for reporting purposes. The system's pre-defined options are *Building Code*, *Clash*, *Client Feedback*, *Constructability*, *Coordination*, *Design Review*, *Existing Condition*, *Requirement Change*, and *Other*.
    - **Attachments**. Up to 20 images, PDFs, or documents relevant to the issue.
 - Click **Create**. Procore creates a new issue in the *Open* status.

- From **AutoDeskÂ® NavisworksÂ® Clash Detective** using Procore Clash Manager with the **Procore BIM Plugin****Show/Hide Details**

 1. Select one or more clashes or clash groups in NavisworksÂ® Clash Detective.
 2. Click **Create CIs** in Procore Clash Manager.
 3. Select the **Assignee** as the person responsible for resolving the issue.
 4. Select the **Location** for the projectâs locations.
 5. Select the issue **Type**.
 6. Select the **Priority** for the issue.
 7. Enter a description of the coordination issue. You can select one or more of the following as part of the description:

     - Append clash comments
     - Append redline text
 8. Enter the due date.
 9. Click **Create**. Once the issue is created, the Procore logo appears next to the clash or clash group in NavisworksÂ® Clash Detective. The issue displays in the Procore Coordination Issues panel in NavisworksÂ® and in the Procore web application.

### On a Mobile Device

- From the **Procore for Mobile (iOS)** app using **AR for BIM Models** **Show/Hide Details**

 1. Navigate to the **Models** tool on your iOS device.
 2. Tap to open the relevant model.
 3. Tap the **AR (Augmented Reality)** button in the viewer toolbar.
 4. Once you've identified the clash or issue in AR view, tap **Create** > **Coordination Issue**.
 5. Complete these fields:

     - **Title\***. Enter a clear, descriptive issue title for your collaborators.
     - **Description**. Describe the issue. The entry is also saved as a viewpoint comment on the final NWD file.
     - **Attachments**: Creating an issue automatically attaches four (4) images (augmented reality, device camera, model only, and 2D view). You can add up to 20 files per issue.
     - **Location**. The specific project area where the issue is located. The available options in this list are managed in the locations utility in the Project Admin tool.
     - **Assignee**: Select the person who is responsible for resolving the issue. The person must have 'Standard' or 'Admin' permissions on the Coordination Issues tool to be selected as an assignee.
     - **Due Date**. The targeted deadline for the issue resolution.
     - **Priority**. The urgency level. The system's pre-defined options are *Low*, *Medium*, *High*, *Critical*.
     - **Trade**. The discipline involved. The available options in this list are managed in the Trades utility in the Company Admin tool.
     - **Type**. The category of the issue used for reporting purposes. The system's pre-defined options are *Building Code*, *Clash*, *Client Feedback*, *Constructability*, *Coordination*, *Design Review*, *Existing Condition*, *Requirement Change*, and *Other*.
     - **Attachments**. Procore automatically captures a photo of what you were looking at in AR. It also includes a screenshot of the 3D Model view, and a snapshot showing your pin location on the 2D floor plan.
 6. Tap **Create**. Procore creates a new issue in the *Open* status.