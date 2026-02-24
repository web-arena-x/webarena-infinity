# Upload Drawing Revisions - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/upload-drawing-revisions

---

## Objective

To upload revisions to existing drawings in a project's Drawings tool in Procore.

## Background

If you have already uploaded drawings to a project in Procore and need to upload revisions, you will upload them in the same way you would normally [upload drawings](#s989 "Upload Drawings") to the Drawings tool. When you upload drawing revisions to a project, Procore will recognize the drawing number as a duplicate of one you have already uploaded and mark it as a revision of the existing drawing. The drawing revision will automatically appear under the Revision History of the existing drawing.

## Things to Consider

- **Required User Permissions:**
 - 'Admin' permissions on the Drawings tool. 
    OR 'Read Only' or 'Standard' permissions on the Drawings tool with the ['Upload Drawings' or 'Upload and Review Drawings' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Drawings "Grant Granular Permissions in a Permission Template") enabled on your permission template.
- **Additional Information:**
 - Drawings must be uploaded in the PDF file format. The PDF file must be version 1.6 or later.
 - You can upload a drawing with the same revision number or letter as long as one of the following fields is unique: Set Name, Drawing Date, or Received Date. See [Can I upload drawings with the same revision?](https://support.procore.com/faq/can-i-upload-drawings-with-the-same-revision "Can I upload drawings with the same revision?")
 - Markups added to the Private or Personal and Published layer of a previous drawing revision will be preserved and inherited by the new drawing revisions. If you add markups to the old revision after a newer revision is uploaded, they will not be added to the new revision.
 - Sketches will not carry over to a new revision upon uploading.
 - Notification emails are sent after the upload has completed processing. See [Who receives a notification for updates in the Drawings tool?](https://support.procore.com/faq/who-receives-a-notification-for-updates-in-the-drawings-tool "Who receives a notification for updates in the Drawings tool?")
 - If your drawing upload fails, it could be due to a file that is encrypted, password protected, or corrupt. See [Why are my drawing uploads failing?](https://support.procore.com/faq/why-are-my-drawing-uploads-failing "Why are my drawing uploads failing?")

## Video

| |
| --- |
| |

## Steps

1. Navigate to the project's **Drawings** tool.
2. Click **Upload**.
3. Click **Attach Files**.

   Tip For best results, format your drawings for OCR. See [How can I improve the accuracy of OCR on my drawings?](https://support.procore.com/faq/how-can-i-improve-the-accuracy-of-ocr-on-my-drawings "How can I improve the accuracy of OCR on my drawings?")
4. Select the files to upload from your computer.
5. Once uploaded, click **Attach**.
6. Click the **Select or Create Set** drop-down menu under **Drawing Set**.
7. Choose one of these options: 
   **Select a Drawing Set** To add the drawing to an existing set: Start typing the set name. Procore shows any sets matching your entry and you can highlight the match to select it.
   ![select-drawing-set.png](https://support.procore.com/@api/deki/files/479833/select-drawing-set.png?revision=1&size=bestfit&width=750&height=314) 
     
   **Create a Drawing Set** To add the drawing to a new set: Type a set name and click **Create Set [Your Set Name]**.
     
   ![create-drawing-set.png](https://support.procore.com/@api/deki/files/479832/create-drawing-set.png?revision=1&size=bestfit&width=750&height=294)
8. Fill in these fields:
   - **Set Date**: The date the architect sent the drawing set.
     - If adding to an existing set, Procore populates this field automatically.
     - If creating a new set, click the field to select a date from the calendar.
   - **Default Drawing Date**: The date the drawings were authored. This appears as the 'Drawing Date' on all drawings in the set.
     - Click the field to select a date from the calendar.
   - **Default Received Date**: The date a drawing was received or issued by the creator of the drawings (i.e. the design team).
     - Click the field to select a date from the calendar.
   - **Advanced Options**: Click the**arrow** ![caret-icon.png](https://support.procore.com/@api/deki/files/115902/caret-icon.png?revision=1&size=bestfit&width=13&height=17) icon next to Advanced Options to show the following options. 
       
     ![upload-drawings-advanced-options.png](https://support.procore.com/@api/deki/files/479834/upload-drawings-advanced-options.png?revision=2&size=bestfit&width=750&height=814) 
     - **Default Revision**:If your set has a default drawing revision number or letter, enter it here. The default revision will be set as the 'Revision' for all drawings in this upload. 
       *Note:* If a default revision is not specified, Procore will use the drawing number to determine the revision.
     - **Drawing No. Contains Revision**: Click the drop-down menu and select the option that applies to the drawings. If a drawing number contains a revision, the drawing number will be separated at the first decimal or underscore into the Drawing No. and the Revision. For example, a drawing with 'A203.01' would show 'A203' as the Drawing No., and '01' as the Revision.  
       *Note:* See 'Get From Filename' below for guidelines on filenames if you use both settings.
       - **No Rev in Drawing Number**: Select if the drawings do not include revisions in the drawing numbers.
       - **Rev is After First Decimal**: Select if the drawings contain revisions after the first decimal of a drawing number (example: A203.**01**).
       - **Rev is After First Underscore**: Select if the drawings contain revisions after the first underscore of a drawing number (example: A203\_**01**).
       - **Rev is After Last Underscore**: Select if the drawings contain revisions after the last underscore of a drawing number (example: A203\_\_EE\_\_**01**)
     - **Drawing Number**:
       - **Get From Filename**: Mark the checkbox if you want Procore to pull the number and title of an individual drawing based off of the filename. This will bypass OCR and result in higher accuracy in the naming of your drawings. 
         ***Important!***If you are using the 'Drawing No. Contains Revision' setting above, drawing filenames should match the following formats:
         - For 'No Rev in Drawing Number': *Number\_Title.pdf* *Note:* If there is no underscore between the drawing number and title, the entire filename will be entered for the drawing number.
         - For 'Rev is After First Decimal': *Number.RevNumber\_Title.pdf*
         - For 'Rev is After First Underscore': *Number\_RevNumber\_Title.pdf*
         - For 'Rev is After Last Underscore': *Number\_Title\_RevNumber.pdf*
     - **Drawing Language**: Procore's OCR can scan for drawings in English, French, German, and Spanish. The language for your drawings is automatically selected based on the locale of the project or company, but you can select another language from the drop-down menu if necessary. See [Can I change the language that Procore scans my drawings for?](https://support.procore.com/faq/can-i-change-the-language-that-procore-scans-my-drawings-for "Can I change the language that Procore scans my drawings for?")
9. After the upload has been processed, you can [Review and Confirm the Drawings](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/review-and-confirm-drawings "Review and Confirm Drawings"). 
   *Note:* A progress indicator is available in the 'Items to Review' pop up window. 
   ![drawings-items-to-review-pop-up.png](https://support.procore.com/@api/deki/files/528910/drawings-items-to-review-pop-up.png?revision=1&size=bestfit&width=930&height=350)

##### Note

- If the drawing numbers are the same, Procore's [OCR](http://en.wikipedia.org/wiki/Optical_character_recognition) will automatically recognize the the Drawing Number, Title, and Discipline fields.
- If the drawing has the same number as another drawing in the same area, Procore will automatically fill in the rest of the information including the next revision number (in sequence with the lastly uploaded revision with that number).

## Next Steps

1. [Review and Confirm Drawings](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/review-and-confirm-drawings "Review and Confirm Drawings")
2. [Publish Drawings](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/publish-drawings "Publish Drawings")

If you would like to learn more about Procore's construction drawings software and how it can help your business, please visit our [construction drawing management software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/drawings "https://www.procore.com/project-management/drawings").