# Review Submittal PDF Attachments

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/review-submittal-pdf-attachments

---

## Background

While reviewing a submittalâs PDF attachments in Procore, users who have the current Ball In Court (BIC) responsibility on the submittal can apply markups and add personal stamps directly in Procore's web application. Users with 'Admin' level permissions on the project's Submittals tool who have the current Ball In Court responsibility can also add a blank page or a cover page to the front of the PDF.

## Things to Consider

- **Required User Permissions:**

  - *To add markup* *and stamps to a submittal PDF attachment in Procore:* 'Standard' level permissions or higher on the Submittals tool with the current Ball In Court responsibility.
  - *To add a blank page or a cover page to a submittal PDF attachment in Procore, you need one of the following:*

    - 'Admin' level permissions on the project's Submittals tool with the current Ball in Court responsibility.
- **Additional Information:**

  - The submittal's status must be 'Open'.
  - If you want to use a personal stamp when adding markups to a submittal PDF attachment in Procore, see [Manage Personal Submittal Markup Stamps](/product-manuals/submittals-project/tutorials/manage-personal-submittal-markup-stamps).
  - Adding markups or stamps to a submittal PDF attachment in Procore automatically adds the attachment to your response in the Submittal Workflow.
  - Any user who has permission to view a submittal also has permission to view its attachments and any markups or stamps added in Procore.
  - If two or more users are viewing a submittal PDF attachment at the same time:

    - The other users' initials display at the top of the attachment viewer.
    - Markups added by all users are saved automatically, but the markups do not automatically appear in the attachment viewer in real-time for other users viewing the attachment. To see another user's markups, refresh the page.
    - The 'Current' version of the attachment shifts to the step in the workflow with the user who added the most recent markups or stamps to the attachment.
  - Deleting a blank page or a cover page will reset the undo/redo queue, meaning that any markup actions completed in your current review session before the page was deleted cannot be undone or redone using the 'Undo' and 'Redo' buttons or keyboard shortcuts.
  - Ball In Court responsibility on a submittal shifts to the Submittal Manager after all steps in the Submittal Workflow are complete.

## Steps

- Add Markup to a Submittal PDF Attachment
- Optional: Add or Remove a Blank Page or Cover Page to a Submittal PDF Attachment

### Add Markup to a Submittal PDF Attachment

1. Navigate to the project's **Submittals** tool.
2. Click the **Items**, **Packages**, **Spec Sections**, or **Ball In Court** tab. See [Switch Between Submittals Views](/product-manuals/submittals-project/tutorials/switch-between-submittals-views).
3. Click **View** next to the submittal with the PDF attachment you want to add markup to.
4. In the 'Submittal Workflow' table, click **Open** next to the PDF attachment you want to add markup to.

   ##### Â Tip

   Current attachments are indicated by a 'Current' label in the 'Version' column. See [When is a submittal attachment labeled as 'Current' in the 'Submittal Workflow' table?](/faq-when-is-a-submittal-attachment-labeled-as-current-in-the-submittal-worfklow-table)

- Use the markup tools to add markups or one of your submittal stamps to the file.  
  *Note:* If you change an applicable markup tool's attributes (stroke width, color, or opacity) before using that markup tool, the system will apply the same attributes by default each time you use that markup tool. Editing the attributes for an existing markup does not affect the markup tool's default attributes.

1The attachment viewer must be in 'Scroll Mode'. 2Scrolling left and right are only available when the page view in the attachment viewer is narrower than the actual page width.  
6. When you are finished adding your markups and stamps, click **Close** to close the attachment viewer and to return to the submittal.

    

The submittal PDF attachment you added markups to will have a markup pencil  icon next to it and 'Current' will display in the 'Version' column to indicate which version of the attachment is the most up-to-date.

    

### Optional: Add or Remove a Blank Page or Cover Page

This task can only be performed by Submittal Managers and users with 'Admin' level permissions on the project's Submittals tool with the current Ball In Court responsibility.

1. Navigate to the project's **Submittals** tool.
2. Click the **Items**, **Packages**, **Spec Sections**, or **Ball In Court** tab. See [Switch Between Submittals Views](/product-manuals/submittals-project/tutorials/switch-between-submittals-views).
3. Click **View** next to the submittal with the PDF attachment you want to add a blank page or a Procore-generated cover page to.
4. In the 'Submittal Workflow' table, click **Open** next to the PDF attachment you want to add a blank page or a Procore-generated cover page to.

   ##### Â Tip

   Current attachments are indicated by a 'Current' label in the 'Version' column. See [When is a submittal attachment labeled as 'Current' in the 'Submittal Workflow' table?](/faq-when-is-a-submittal-attachment-labeled-as-current-in-the-submittal-worfklow-table)

   Adding a cover sheet or blank sheet to an attachment does *not* give it the label of "Current" in the Version column of the 'Submittal Workflow' table.

- Open the page navigation menu by pressing ALT + T (or OPTION + T) on your keyboard or by clicking the angle bracket tab.
- Click **Add** **Page**.
- Select **Blank Page** or **Cover Page** in the 'Add Page' window.
- To remove a blank page or a Procore-generated cover page, open the page navigation menu and click the  icon next to the page number.

  ##### Â Important

  - This page can only be deleted when it has no markups. If you have added markup to the page, you can delete your markups and then delete the page, but you cannot delete another user's markups.
  - Deleting a blank page or a cover page will reset the undo/redo queue, meaning that any markup actions completed in your current review session before the page was deleted cannot be undone or redone using the 'Undo' and 'Redo' buttons or keyboard shortcuts.