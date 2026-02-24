# Forward a Submittal for Review - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/forward-a-submittal-for-review

---

## Objective

To forward a submittal item to a user outside the workflow for review.

## Background

This feature lets you forward a submittal to someone outside the original workflow for additional information

##### Example

Typically, after creating a submittal item and adding members to the workflow, an architect reviews it first, followed by a project engineer. However, for this submittal, the architect wants a structural engineer to review it first and then pass it to the project engineer. The architect can use the steps below to forward the submittal to the structural engineer, which adds them to the workflow to capture their response in Procore.

## Things to Consider

- **Required User Permissions:**
 - 'Standard' level permissions or higher on the project's Submittals tool and the current [Ball In Court](../../../../../../references/construction-management/glossary-of-terms.md#BIC "references/construction-management/glossary-of-terms#BIC") for the submittal.
- **Prerequisites:**
 - The 'Allow Approvers to Add Reviewers to Their Step in the Workflow' configuration setting must be enabled. This setting is enabled by default in Procore. See [Configure Advanced Settings: Submittals Tool](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/configure-settings-submittals-tool "Configure Advanced Settings: Submittals Tool").
- **Additional Information:**
 - The submittal's status must be 'Open'.
 - If a user has already been added to the submittal's workflow, you will not be able to forward the submittal to that user. They can respond to the submittal in the order specified by the submittal's workflow.
 - If you forward a submittal to another user, you must wait for them to submit their response before you can respond. After they respond, the BIC will be shifted back to you and you will have the option to either (1) respond to the submittal or (2) forward it to another user for their review.
 - If a submittal is forwarded to you by a member of the submittal's workflow, you cannot forward the submittal to another user.

## Prerequisites

*Optional:* [Review Submittal PDF Attachments](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/review-submittal-pdf-attachments "Review Submittal PDF Attachments")

## Steps

1. Navigate to the project's **Submittals** tool.
2. Click **View** next to the submittal to forward.
3. Review the submittal's information and any included attachments.

   ##### Note

   Any PDF attachments that you added markups to in Procore are with your response automatically. See [Review Submittal PDF Attachments](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/review-submittal-pdf-attachments "Review Submittal PDF Attachments").
4. Under **Submittal Workflow**, click **Respond**. 
     
   ![submittal-workflow-respond.png](https://support.procore.com/@api/deki/files/481074/submittal-workflow-respond.png?revision=2)
5. *Optional.* Click **Attach Files** to open the Attach Files window. If the corresponding tool (\*) is enabled on the project, choose from these options:
   - **My Computer**. Upload files from your computer or network.
   - **Photos\***. Select a photo album to attach from the drop-down menu. To learn more, see [Photos](https://support.procore.com/products/online/user-guide/project-level/photos "Photos").
   - **Documents\***. Select the documents to attach. To learn more, see [Documents](https://support.procore.com/products/online/user-guide/project-level/documents "Project Documents").
   - **Forms\***. Select the template to attach. To learn more, see [Forms](https://support.procore.com/products/online/user-guide/project-level/forms "Forms").

     ##### Example

     This example shows the My Computer page of the Attach Files window.  
     ![upload-files.png](https://support.procore.com/@api/deki/files/481206/upload-files.png?revision=1)
6. Click **Attach**. 
   The attachments appear in the **Attach Files to Send to the Next Reviewer** window. 
   ![attach-files-to-send-to-next-reviewer.png](https://support.procore.com/@api/deki/files/481207/attach-files-to-send-to-next-reviewer.png?revision=1)
7. Click **Next**.
8. In the **Respond** window, click **Forward for Review**. This link is only visible if you are the [Ball In Court](../../../../../../references/construction-management/glossary-of-terms.md#Ball_In_Court "Glossary of Terms") reviewer.  
     
   ![forward-for-review.png](https://support.procore.com/@api/deki/files/481208/forward-for-review.png?revision=1)
9. Add the following information:
   - **Forward To**. Select the user you want to forward the submittal to. 
     *Note:* To appear as a selection in the list, the user must be added to the Project level Directory tool. See [Add a User Account to the Project Directory](https://support.procore.com/products/online/user-guide/project-level/directory/tutorials/add-user-account-to-project-directory "Add a User Account to the Project Directory").
   - **Return By**. Select the date by which the reviewer must respond to the submittal. 
     *Note:* The date you select must be on or before the due date for your response.
   - **Comments**. *Optional*. Enter any comments you want to send to the reviewer.
   - **Attach Files**. *Optional*. Add any files you want to send to the reviewer. 
       
     ![respond.png](https://support.procore.com/@api/deki/files/481210/respond.png?revision=1)
10. Click **Preview** to review the information.
11. Click one of the following options:
    - Click Forwardto forward the submittal to the user you selected.
    - Click **Back** if you need to change any information you added.
    - Click **Cancel** to close the window and return to the submittal's page. *Note:* Any information you added before closing the window won't be saved. 
        
      ![preview-and-respond.png](https://support.procore.com/@api/deki/files/481211/preview-and-respond.png?revision=1)

The system automatically adds the user to the 'Submittal Workflow' table and sets them as the Ball In Court. Their name will be added to the same workflow step as the approver who forwarded the submittal to them. 
*Notes:*

- The reviewer will receive an email notification from Procore letting them know action is required.
- The system changes the response of the approver who forwarded the submittal to 'Forwarded for Review'.

## Next Steps

- [Respond to a Forwarded Submittal as a Reviewer](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/respond-to-a-forwarded-submittal-as-a-reviewer "Respond to a Forwarded Submittal as a Reviewer")

## See Also

- [Respond to a Submittal as an Approver](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/respond-to-a-submittal-as-an-approver "Respond to a Submittal as an Approver")

## 

If you would like to learn more about Procore's submittals management software and how it can help your business, please visit our [construction submittals software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/submittals "https://www.procore.com/project-management/submittals").