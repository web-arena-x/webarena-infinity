# Forward a Submittal for Review

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/forward-a-submittal-for-review

---

## Background

This feature lets you forward a submittal to someone outside the original workflow for additional information

##### Example

Typically, after creating a submittal item and adding members to the workflow, an architect reviews it first, followed by a project engineer. However, for this submittal, the architect wants a structural engineer to review it first and then pass it to the project engineer. The architect can use the steps below to forward the submittal to the structural engineer, which adds them to the workflow to capture their response in Procore.

## Things to Consider

- **Required User Permissions:**

  - 'Standard' level permissions or higher on the project's Submittals tool and the current [Ball In Court](/glossary-of-terms) for the submittal.
- **Prerequisites:**

  - The 'Allow Approvers to Add Reviewers to Their Step in the Workflow' configuration setting must be enabled. This setting is enabled by default in Procore. See [Configure Advanced Settings: Submittals Tool](/product-manuals/submittals-project/tutorials/configure-settings-submittals-tool).
- **Additional Information:**

  - The submittal's status must be 'Open'.
  - If a user has already been added to the submittal's workflow, you will not be able to forward the submittal to that user. They can respond to the submittal in the order specified by the submittal's workflow.
  - If you forward a submittal to another user, you must wait for them to submit their response before you can respond. After they respond, the BIC will be shifted back to you and you will have the option to either (1) respond to the submittal or (2) forward it to another user for their review.
  - If a submittal is forwarded to you by a member of the submittal's workflow, you cannot forward the submittal to another user.

## Prerequisites

*Optional:* [Review Submittal PDF Attachments](/product-manuals/submittals-project/tutorials/review-submittal-pdf-attachments)

## Steps

1. Navigate to the project's **Submittals** tool.
2. Click **View** next to the submittal to forward.
3. Review the submittal's information and any included attachments.

   ##### Â Note

   Any PDF attachments that you added markups to in Procore are with your response automatically. See [Review Submittal PDF Attachments](/product-manuals/submittals-project/tutorials/review-submittal-pdf-attachments).

- Under **Submittal Workflow**, click **Respond**.
- *Optional.* Click **Attach Files** to open the Attach Files window. If the corresponding tool (\*) is enabled on the project, choose from these options:

  - **My Computer**. Upload files from your computer or network.
  - **Photos\***. Select a photo album to attach from the drop-down menu. To learn more, see [Photos](https://support.procore.com/products/online/user-guide/project-level/photos).
  - **Documents\***. Select the documents to attach. To learn more, see [Documents](https://support.procore.com/products/online/user-guide/project-level/documents).
  - **Forms\***. Select the template to attach. To learn more, see [Forms](https://support.procore.com/products/online/user-guide/project-level/forms).

    ##### Example

    This example shows the My Computer page of the Attach Files window.