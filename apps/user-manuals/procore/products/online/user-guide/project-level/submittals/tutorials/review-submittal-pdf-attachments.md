# Review Submittal PDF Attachments - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/review-submittal-pdf-attachments

---

## Objective

To review submittal PDF attachments in Procore.

## Background

While reviewing a submittal’s PDF attachments in Procore, users who have the current Ball In Court (BIC) responsibility on the submittal can apply markups and add personal stamps directly in Procore's web application. Users with 'Admin' level permissions on the project's Submittals tool who have the current Ball In Court responsibility can also add a blank page or a cover page to the front of the PDF.

## Things to Consider

- **Required User Permissions:**
  - *To add markup* *and stamps to a submittal PDF attachment in Procore:*
    - 'Standard' level permissions or higher on the Submittals tool with the current Ball In Court responsibility.
  - *To add a blank page or a cover page to a submittal PDF attachment in Procore:*
    - 'Admin' level permissions on the project's Submittals tool with the current Ball in Court responsibility.
- **Additional Information:**
  - The submittal's status must be 'Open'.
  - If you want to use a personal stamp when adding markups to a submittal PDF attachment in Procore, see [Manage Personal Submittal Markup Stamps](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/manage-personal-submittal-markup-stamps "Manage Personal Submittal Markup Stamps").
  - Adding markups or stamps to a submittal PDF attachment in Procore automatically adds the attachment to your response in the Submittal Workflow.
  - Any user who has permission to view a submittal also has permission to view its attachments and any markups or stamps added in Procore.
  - If two or more users are viewing a submittal PDF attachment at the same time:
    - The other users' initials display at the top of the attachment viewer.
    - Markups added by all users are saved automatically, but the markups do not automatically appear in the attachment viewer in real-time for other users viewing the attachment. To see another user's markups, refresh the page.
    - The 'Current' version of the attachment shifts to the step in the workflow with the user who added the most recent markups or stamps to the attachment.
  - Deleting a blank page or a cover page will reset the undo/redo queue, meaning that any markup actions completed in your current review session before the page was deleted cannot be undone or redone using the 'Undo' and 'Redo' buttons or keyboard shortcuts.
  - Ball In Court responsibility on a submittal shifts to the Submittal Manager after all steps in the Submittal Workflow are complete.

## Steps

- [Add Markup to a Submittal PDF Attachment](#Add_Markup_to_a_Submittal_PDF_Attachment "Review Submittal PDF Attachments")
- [Optional: Add or Remove a Blank Page or Cover Page to a Submittal PDF Attachment](#Optional:_Add_or_Remove_a_Blank_Page_or_Cover_Page "Review Submittal PDF Attachments")

### Add Markup to a Submittal PDF Attachment

1. Navigate to the project's **Submittals** tool.
2. Click the **Items**, **Packages**, **Spec Sections**, or **Ball In Court** tab. See [Switch Between Submittals Views](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/switch-between-submittals-views "Switch Between Submittals Views").
3. Click **View** next to the submittal with the PDF attachment you want to add markup to.
4. In the 'Submittal Workflow' table, click **Open** next to the PDF attachment you want to add markup to.

   ##### Tip

   Current attachments are indicated by a 'Current' label in the 'Version' column. See [When is a submittal attachment labeled as 'Current' in the 'Submittal Workflow' table?](https://support.procore.com/faq/when-is-a-submittal-attachment-labeled-as-current-in-the-submittal-worfklow-table "When is a submittal attachment labeled as 'Current' in the 'Submittal Workflow' table?")
5. Use the markup tools to add markups or one of your submittal stamps to the file.  
   *Note:*If you change an applicable markup tool's attributes (stroke width, color, or opacity) before using that markup tool, the system will apply the same attributes by default each time you use that markup tool. Editing the attributes for an existing markup does not affect the markup tool's default attributes.  
     
   This table lists the features and available keyboard shortcuts to use when viewing and adding markups to submittal PDF attachments.  

   | Button | Label | Action | Windows Keyboard Shortcut | Mac Keyboard Shortcut |
   | --- | --- | --- | --- | --- |
   | icon-markup-left.png | Hide/Show Page Navigator | Hide or show the Page Navigator menu. | ALT + T | OPTION + T |
   |  | Select | Click to select or move a markup on the page. To select multiple markups, hold SHIFT on your keyboard and click on each markup you want to select as part of a group. | Press V | Press V |
   | N/A | Scroll Mode | Use your mouse or the arrow keys on your keyboard to scroll on the page and scroll between pages. | Press V | Press V |
   | icon-markup-pan.png | Pan | Click and drag your cursor to move across the page.  For temporary panning, hold the SPACEBAR. | SHIFT + V | SHIFT + V |
   | N/A | Pan Mode | Click and drag your cursor to move across the page.  For temporary panning, hold the SPACEBAR. | SHIFT + V | SHIFT + V |
   | icon-markup-draw.png | Pen | Draw a freehand line or shape. | Press P to select this tool. | Press P to select this tool. |
   | btn-stroke-75x75.png | Line | Draw a line. | Press L to select this tool. | Press L to select this tool. |
   | btn-arrow-75x75.png | Arrow | Draw an arrow. | Press A to select this tool. | Press A to select this tool. |
   | btn-box-75x75.png | Rectangle | Draw a rectangle. | Press R to select this tool. | Press R to select this tool. |
   | btn-oval-75x75.png | Ellipse | Draw a circle or oval. | Press E to select this tool. | Press E to select this tool. |
   | btn-cloud-75x75.png | Cloud | Draw a rectangular cloud. | Press C to select this tool. | Press C to select this tool. |
   | btn-highlighter-75x75.png | Freehand Highlight | Highlight with a freehand highlighter. | Press F to select this tool. | Press F to select this tool. |
   | btn-highlight-text.png | Highlight | Highlight text on a page. | Press H to select this tool. | Press H to select this tool. |
   | btn-text-75x75.png | Text | Add a text box. The text box must be filled to be selectable. The font size can be adjusted by selecting a filled text box and moving the slider above the text box. | Press T to select this tool. | Press T to select this tool. |
   |  | Stamp | Open the stamp menu and click the stamp you want to add. See [Manage Personal Submittal Markup Stamps](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/manage-personal-submittal-markup-stamps "Manage Personal Submittal Markup Stamps"). | Press S to open the stamp menu. | Press S to open the stamp menu. |
   | icon-undo.png | Undo | Undo the most recent markup action in your current review session. This excludes adding or removing blank or cover pages. | CTRL + Z | CMD + Z |
   | icon-redo.png | Redo | Redo the most recently undone markup action in your current review session. | CTRL + Y | CMD + Y |
   | btn-stroke-75x75.png | Stroke | Choose the desired stroke width for a selected markup. Adjusting the stroke width for a text box adds or modifies a border around the text box. | N/A | N/A |
   | btn-color-75x75.png | Color | Choose the color for a selected markup. | N/A | N/A |
   | btn-opacity-75x75.png | Opacity | Choose the opacity percentage for the fill color on a selected markup.  *Note*: The opacity cannot be adjusted for Line, Arrow, Cloud, or Stamp markups. | N/A | N/A |
   | N/A | Duplicate | Duplicate a selected markup. | CTRL + D | CMD + D |
   | N/A | Delete | Delete a selected markup. | DELETE | DELETE  *Mozilla Firefox Only:  SHIFT + DELETE* |
   | N/A | Copy | Copy a selected markup. | CTRL + C | CMD + C |
   | N/A | Paste | Paste a copied markup. | CTRL + V | CMD + V |
   | icon-markup-zoom-in.png | Zoom In | Zoom in on the page. | CTRL + Plus Sign (+) | CMD + Plus Sign (+) |
   | icon-markup-zoom-out.png | Zoom Out | Zoom out on the page. | CTRL + Minus Sign (-) | CMD + Minus Sign (-) |
   | N/A | Zoom to Fit | Fit the full page in the attachment viewer. | CTRL + 9 | CMD + 9  *Safari: CTRL + 9* |
   | N/A | Zoom to Width | Fill the attachment viewer with the full width of the page. | CTRL + 0 | CMD + 0  or  CTRL + 0 |
   | icon-markup-page-next.png | Previous Page | Move to the previous page. | SHIFT + Up Arrow (↑) | SHIFT + Up Arrow (↑) |
   | icon-markup-page-previous.png | Next Page | Move to the next page. | SHIFT + Down Arrow (↓) | SHIFT + Down Arrow (↓) |
   | N/A | Scroll Up | Scroll up the page. 1 | Up Arrow (↑) | Up Arrow (↑) |
   | N/A | Scroll Down | Scroll down the page. 1 | Down Arrow (↓) | Down Arrow (↓) |
   | N/A | Scroll Left | Scroll left on the page. 1, 2 | Left Arrow (←) | Left Arrow (←) |
   | N/A | Scroll Right | Scroll right on the page. 1, 2 | Right Arrow (→) | Right Arrow (→) |

   1 The attachment viewer must be in 'Scroll Mode'.

   2 Scrolling left and right are only available when the page view in the attachment viewer is narrower than the actual page width.
6. When you are finished adding your markups and stamps, click **Close** to close the attachment viewer and to return to the submittal.  
     
   ![submittals-pdf-close.png](https://support.procore.com/@api/deki/files/234666/submittals-pdf-close.png?revision=1)  
     
   The submittal PDF attachment you added markups to will have a markup pencil ![icon-markup-current-file.png](https://support.procore.com/@api/deki/files/153419/icon-markup-current-file.png?revision=2&size=bestfit&width=20&height=20) icon next to it and 'Current' will display in the 'Version' column to indicate which version of the attachment is the most up-to-date.  
     
   ![submittals-submittal-workflow-markup-added.png](https://support.procore.com/@api/deki/files/142065/submittals-submittal-workflow-markup-added.png?revision=3)

### Optional: Add or Remove a Blank Page or Cover Page

This task can only be performed by Submittal Managers and users with 'Admin' level permissions on the project's Submittals tool with the current Ball In Court responsibility.

1. Navigate to the project's **Submittals** tool.
2. Click the **Items**, **Packages**, **Spec Sections**, or **Ball In Court** tab. See [Switch Between Submittals Views](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/switch-between-submittals-views "Switch Between Submittals Views").
3. Click **View** next to the submittal with the PDF attachment you want to add a blank page or a Procore-generated cover page to.
4. In the 'Submittal Workflow' table, click **Open** next to the PDF attachment you want to add a blank page or a Procore-generated cover page to.

   ##### Tip

   Current attachments are indicated by a 'Current' label in the 'Version' column. See [When is a submittal attachment labeled as 'Current' in the 'Submittal Workflow' table?](https://support.procore.com/faq/when-is-a-submittal-attachment-labeled-as-current-in-the-submittal-worfklow-table "When is a submittal attachment labeled as 'Current' in the 'Submittal Workflow' table?")  
     
   Adding a cover sheet or blank sheet to an attachment does *not* give it the label of "Current" in the Version column of the 'Submittal Workflow' table.
5. Open the page navigation menu by pressing ALT + T (or OPTION + T) on your keyboard or by clicking the angle bracket tab.  
     
   ![submittals-pdf-page-navigation-menu.png](https://support.procore.com/@api/deki/files/153833/submittals-pdf-page-navigation-menu.png?revision=2)
6. Click **Add****Page**.  
     
   ![submittals-pdf-add-page.png](https://support.procore.com/@api/deki/files/153921/submittals-pdf-add-page.png?revision=2)
7. Select**Blank Page** or **Cover Page** in the 'Add Page' window.  
     
   ![submittals-pdf-add-page-window.png](https://support.procore.com/@api/deki/files/153922/submittals-pdf-add-page-window.png?revision=1)
8. To remove a blank page or a Procore-generated cover page, open the page navigation menu and click the ![icon-delete-trash.png](https://support.procore.com/@api/deki/files/90896/icon-delete-trash.png?revision=1&size=bestfit&width=15&height=15) icon next to the page number.

   ##### Important

   - This page can only be deleted when it has no markups. If you have added markup to the page, you can delete your markups and then delete the page, but you cannot delete another user's markups.
   - Deleting a blank page or a cover page will reset the undo/redo queue, meaning that any markup actions completed in your current review session before the page was deleted cannot be undone or redone using the 'Undo' and 'Redo' buttons or keyboard shortcuts.

   ![submittals-pdf-delete-page.png](https://support.procore.com/@api/deki/files/153923/submittals-pdf-delete-page.png?revision=2)
9. Click **Close** to close the attachment viewer and to return to the submittal.  
     
   ![submittals-pdf-close.png](https://support.procore.com/@api/deki/files/234666/submittals-pdf-close.png?revision=1)  
     
   The markup pencil ![icon-markup-current-file.png](https://support.procore.com/@api/deki/files/153419/icon-markup-current-file.png?revision=2&size=bestfit&width=20&height=20) icon shows next to the submittal PDF attachment if a cover sheet was added but not if a blank sheet was added.    
     
   ![submittals-submittal-workflow-markup-added.png](https://support.procore.com/@api/deki/files/142065/submittals-submittal-workflow-markup-added.png?revision=3)

## Next Steps

- [Respond to a Submittal as an Approver](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/respond-to-a-submittal-as-an-approver "Respond to a Submittal as an Approver")

## See Also

- [Manage Personal Submittal Markup Stamps](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/manage-personal-submittal-markup-stamps "Manage Personal Submittal Markup Stamps")
- [View Submittal Attachments](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/view-submittal-attachments "View Submittal Attachments")
- [Delete Attachments from the Submittal Workflow](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/delete-attachments-from-the-submittal-workflow "Delete Attachments from the Submittal Workflow")

##