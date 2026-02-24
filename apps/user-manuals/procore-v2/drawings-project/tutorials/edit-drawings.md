# Edit Drawings

Source: https://v2.support.procore.com/product-manuals/drawings-project/tutorials/edit-drawings

---

## Things to Consider

- **Required User Permissions:**

 - 'Admin' on the project's Drawings tool.
- **Additional** **Information:**

 - When you bulk edit multiple drawings at once, all selected drawings will inherit the same changes.
 - If your project uses [Drawing Areas](/faq-what-are-drawing-areas) and you want to move drawings to another area, you can use the 'Edit' option to move them. See [Can I move drawings to another drawing area?](/product-manuals/drawings-project/tutorials/move-drawings-to-another-drawing-area)

## Steps

1. Navigate to your project's **Drawings** tool.
2. There are two ways to edit drawings: 
   Edit a Single Drawing Bulk Edit Multiple Drawings

### Edit a Single Drawing

1. Click **Info** next to the drawing you want to edit information for.
2. Edit information for the drawing in the following sections:

   - To edit fields in the 'General Information' section, click **Edit**.   
     OR
   - To edit fields in the 'Versions' section, hover over a field. 
     *Note*: If you are able to edit the field, the edit icon will appear next to it.
3. Click the field you want to edit.
4. Edit the fields as necessary.

   - **General Information**

     ##### Â Note

     If custom fields for drawings have been added to the project, you may see additional fields in this section. Any information filled out for these custom fields will be specific to the revision, meaning any changes will not appear on other revisions for the drawing. See [What are custom fields and which Procore tools support them?](/faq-what-are-custom-fields-and-which-procore-tools-support-them)

- **Drawing No**.: Edit the drawing number to coincide with your records. 
 *Note*: Any specified drawing number must be unique. You will not be allowed to create a duplicate drawing number.
- **Drawing Title**: Edit the drawing's title.
- **Discipline**: Change the discipline of the drawing to organize it into a different category on the Drawing Log page. You can also double-click the field to choose from a list of your default and custom disciplines.
- **Obsolete**: Mark this checkbox if you want to mark your drawing as obsolete. 
 *Note*: This action will remove it from the current drawing set, but will not delete it. For more information on obsolete drawings, see [Mark Drawings as Obsolete](/product-manuals/drawings-project/tutorials/mark-drawings-as-obsolete).
- **Drawing No**.: Edit the drawing number to coincide with your records. 
 *Note*: Any specified drawing number must be unique. You will not be allowed to create a duplicate drawing number.
- **Drawing Title**: Edit the drawing's title.
- **Discipline**: Change the discipline of the drawing to organize it into a different category on the Drawing Log page. You can also double-click the field to choose from a list of your default and custom disciplines.
- **Obsolete**: Mark this checkbox if you want to mark your drawing as obsolete. 
 *Note*: This action will remove it from the current drawing set, but will not delete it. For more information on obsolete drawings, see [Mark Drawings as Obsolete](/product-manuals/drawings-project/tutorials/mark-drawings-as-obsolete).
- **Versions**

 - **Revision**: Edit the drawing's revision number or letter. 
    *Note* : Procore will automatically number the revision as the next number in the sequence, but you can also change it to a letter.
 - **Drawing Set** : Edit the drawing's set. This will move the drawing into the set in the set view. Additionally, you can edit the drawing set's information such as its date and title. For more information, see [Configure Advanced Settings: Drawings](/product-manuals/drawings-project/tutorials/configure-advanced-settings-drawings).
 - **Drawing Date**: Edit the date the drawing was created as defined on the drawing itself.
 - **Received Date** : Edit the date you received the drawing.
 - **Status**: You cannot change the drawing's status from this page. You can publish drawings from the set view. See [Publish Drawings](/process-guides/user-guide-bidding-and-estimating-integration/publish-drawings). You cannot unpublish drawings once they are published
- To save changes made to fields in the 'General Information' section, click **Update**. 
 Changes made to fields in the 'Versions' section are automatically saved when clicking out of the field.

### Bulk Edit Multiple Drawings

1. Navigate to the Drawings list page.
2. Mark the checkboxes next to the drawings you want to edit, or click **Select All** to select all the drawings in the set you are viewing. 
   *Note* : You can select multiple drawings from different drawing sets.
3. Click **Bulk Edit** .
4. Mark the checkboxes next to the fields you want to edit and update the information as appropriate.

   - **Discipline***Note*: There is a 255-character limit on the discipline title.
   - **Drawing Date**
   - **Received Date**
   - **Drawing Set**
   - **Change Obsolete Status**
   - **Drawing Area:** If you want to move drawings to another [drawing area](/faq-what-are-drawing-areas), choose whether you want to move them to an existing area or create a new one: 
     See [How can I move drawings to another drawing area?](/product-manuals/drawings-project/tutorials/move-drawings-to-another-drawing-area)

     - **To move drawings to an existing area**:

       - Begin typing the name of the drawing area, or double click into the field to view a list of existing drawing areas.
     - **To move drawings to a new area**:

       - Enter a name for the area in the 'Drawing Area' field. 
         *Note*: The drawing area name must be less than 255 characters, and the name cannot already exist in the project.
5. Click **Update.***Note*: If you moved drawings to another area, the following occurs:

   - A banner appears at the top of the page confirming that the drawings were moved. 
     OR If one or more drawings has the same drawing number as a drawing in the existing area, you are prompted to confirm the drawings on the review page.
   - Email notifications are sent in the following scenarios:

     - If more than 50 drawings are being moved at one time, you will receive an email when the drawing move is complete.
     - If drawings were unable to be moved, you will receive an email with one or more error messages.
   - Drawings will be in the 'Unpublished' state after being moved to a new area. To publish drawings, see [Publish Drawings](/process-guides/user-guide-bidding-and-estimating-integration/publish-drawings).
   - Drawing hyperlinks may take a couple minutes to appear after the drawings have been confirmed.