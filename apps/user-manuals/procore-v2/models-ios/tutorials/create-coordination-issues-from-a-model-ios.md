# Create Coordination Issues from a Model (iOS)

Source: https://v2.support.procore.com/product-manuals/models-ios/tutorials/create-coordination-issues-from-a-model-ios

---

## Background

If an issue is discovered when viewing a model, you can choose to create a coordination issue so that the issue can be tracked in the project's Coordination Issues tool. If you want to create an observation instead, see [Create Observations from a Model (iOS)](/product-manuals/models-ios/tutorials/create-observations-from-a-model-ios).

## Things to Consider

- **Required User Permissions**:

  - 'Read Only' or 'Admin' permissions to the Models tool.  
     AND
  - 'Standard' or 'Admin' permissions to the Coordination Issues tool.
- **Additional Information**:

  - If you are working in offline mode, the coordination issue will be uploaded when a network connection is reestablished.
  - The coordination issue will sync to the Coordination Issues tool and the Procore plugin in NavisworksÂ®.

## Prerequisites

- At least one model must have been published to the Procore project. See [Publish a Model to Procore](/product-manuals/models-project/tutorials/publish-a-model-to-procore).
- The Coordination Issues tool must be active on the project.

## Steps

1. Navigate to the **Models** tool on the Procore app using an iOS mobile device.
2. Tap the model you want to open.  
   *Note:* If you have not downloaded the model to your device yet, tap **Download**. See [Download or Remove Models from a Device (iOS)](/product-manuals/models-ios/tutorials/download-or-remove-models-from-a-mobile-device-ios).
3. Locate the area of the model that you want to create a coordination issue for.
4. Tap the **Create**  icon.
5. Tap **Coordination Issue**.
6. Complete these fields as needed:

   - **Title**: Type a title for the issue. This is the first reference that collaborators see when reviewing an issue.
   - **Description**: Enter a description of the issue.
   - **Location**: Select the issue location.
   - **Due Date**: Set a due date on the calendar.
   - **Priority**: Select the issue priority. Options are: *Low*, *Medium*, *High*, *Critical.*
   - **Assignee**: Select the person who is responsible for resolving the issue. The person must have 'Standard' or 'Admin' permissions on the Coordination Issues tool to be selected as an assignee.
   - **Watchers.** Select the members to notify by email about issue updates. Watchers must have 'Read Only' level permissions or higher on the tool.
   - **Trade**: Select the relevant trade associated with the issue.
   - **Type**: Select the issue type. Options are: *Building Code*, *Clash*, *Client Feedback*, *Constructability*, *Coordination*, *Design Review*, *Existing Condition*, and *Other*.
7. Click **Create**.  
   *Note:* The coordination issue is automatically created.