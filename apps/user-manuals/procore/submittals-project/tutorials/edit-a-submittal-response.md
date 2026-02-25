# Edit a Submittal Response

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/edit-a-submittal-response

---

## Background

Follow these steps when a submitter or approver is unable to add their submittal response. For example, if an approver is traveling and provides verbal confirmation about their response, a user with 'Admin' level permissions on the project's Submittals tool can add the approver's response on their behalf.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Submittals tool.
- **Additional Information:**

  - You can only edit a response for a submitter or approver who has the current Ball In Court responsibility in the submittal workflow. See [Change the Ball in Court on a Submittal](/product-manuals/submittals-project/tutorials/change-the-ball-in-court-on-a-submittal).
  - The **Forward for Review** option is NOT available when editing a response on behalf of a submitter or approver. See [Forward a Submittal for Review](/product-manuals/submittals-project/tutorials/forward-a-submittal-for-review).
  - Users in the submittal workflow can only update their own responses when the submittal's status is 'Open' and they have the current Ball In Court responsibility. See [Upload and Submit a Submittal](/product-manuals/submittals-project/tutorials/upload-and-submit-a-submittal), [Respond to a Submittal as an Approver](/product-manuals/submittals-project/tutorials/respond-to-a-submittal-as-an-approver), and [Respond to a Forwarded Submittal as a Reviewer](/product-manuals/submittals-project/tutorials/respond-to-a-forwarded-submittal-as-a-reviewer).
  - If your company has created custom submittal responses for use with the project's **Submittals** tool (see [Manage Custom Submittals Responses](/product-manuals/submittals-project/tutorials/manage-custom-submittal-responses)), the responses have been customized to fit the specific needs of your organization. See your company's Procore Administrator or the Submittals Manager for information about the proper use for each response on your project.

## Steps

1. Navigate to the project's **Submittals** tool.
2. Click **View** next to the submittal with the response you want to edit.
3. In the 'Submittal Workflow' table, click the vertical ellipsis (â®) at the end of the row with the user's name with the response you want to edit and click **Edit Response**.
4. *Optional:* Attach any files to include with the response.

   - Click **Attach File(s)** to add files from within Procore or from your computer.\* Locate and select (or upload) the files you want to include using the **My Computer**, **Photos**, **Documents**, or **Forms** options. The options you see may vary based on your user permissions on the other project tools.\* Click **Attach**.
5. Click **Next**.
6. Add the following information for the response:

   - **Response**. Select the appropriate response from the dropdown menu.
   - **Sent Date**. *Optional*. Select the date the submittal was sent.
   - **Returned Date**. *Optional*. Select the date the submittal was returned.
   - **Comments**. *Optional*. Enter any comments to include with the response.
7. Click **Preview**.
8. Preview the response.

   ##### Â Tip

   If there's another step in the submittal's workflow, the user's name or group of users' names in the next step will display in the 'Next in Workflow' field.

- Click one of the following options:

  - Click **Save** to save the response without sending emails.
  - Click **Save & Send Email** to save the response and send email notifications to other users. See [Who receives an email when a submittal is created or updated?](/faq-who-receives-an-email-when-a-submittal-is-created-or-updated)
  - Click **Back** if you need to change any information you added.
  - Click **Cancel** to close the window and return to the submittal's page. *Note:* Any information you added before closing the window won't be saved.

The system sends an email notification to any user types selected in the 'Approver Role Responds (via Workflow)' email configuration after you save your response. See [Who receives an email when a submittal is created or updated?](/faq-who-receives-an-email-when-a-submittal-is-created-or-updated)

The system waits until all required users in each step of a submittal's workflow respond before shifting the Ball In Court to the next step.