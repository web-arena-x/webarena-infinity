# Review and Publish Specifications

Source: https://v2.support.procore.com/product-manuals/specifications-project/tutorials/review-and-publish-specifications

---

## Things to Consider

- [Required User Permissions](/product-manuals/specifications-project/permissions)
- Section numbers that match existing section numbers in the Specifications log are treated as revisions. This applies even if the description is different.
- Currently, Procore only looks for the following standard specification formats to divide your specifications:

  - CSI MasterFormat for US and Canada (English and French).
  - NCS Format by NATSPEC for Australia.  
    *Note:* If your specifications follow another format, you can select 'No Format/Other Format' in the Format drop-down menu when uploading specifications. In this case, Procore will not split the specifications into sections. Instead, you can review and split the specifications manually or quickly publish them as a single spec section without reviewing. See [Upload Specifications](/product-manuals/specifications-project/tutorials/upload-specifications).

## Prerequisites

- Specifications must be successfully uploaded, processed, and ready for review. See [Upload Specifications](/product-manuals/specifications-project/tutorials/upload-specifications).

## Steps

1. Navigate to the project's **Specifications** tool.
2. Click **Items to Review.**
3. Hover over the item you want to review and click  **Review**.
4. Your specifications are automatically divided into their respective spec sections, along with their title and number. However, if any of the fields are incorrect or missing, you can manually edit or add them.

   - **Edit a specification section number, title, or revision number:**

     - Click into the field and make your updates. Click outside the field to save.  
       *Notes:*

       - You cannot delete the first section break in the specification book.
       - If you attempt to edit a revision number to one that already exists, you will receive an error message.
   - **Add Break**: If a spec section break was not processed correctly, you can manually add a break to the beginning of a page by clicking the respective button, and then adding the section title and number. Save your changes by clicking outside of the text field or clicking **Enter** on your keyboard.  
      ***Important***: You can only add a new section at a page break in the PDF. If the sections of your spec book begin in the middle of pages, we recommend that you edit the spec book so that there is a page break between sections and re-upload. See [What if my specification sections or divisions start in the middle of a page](/faq-what-if-my-spec-sections-or-divisions-start-in-the-middle-of-a-page)
   - Click **Clear** to delete all specification section breaks, their positions within the upload, as well as their titles and numbers. The entire Table of Contents box will be cleared of all data, but the first section (Table of Contents) will remain.
5. Save your changes:

   - Next to each break, click **Publish [*****section title*****]** to publish an individual section.
   - At the bottom of the page, click **Leave and Resume Later** to save your progress to finish later.
   - At the bottom of the page, click **Publish All**.
6. After you publish the sections, the sections will be divided into divisions based on the first two numbers of the section.  
   For example, if your section number is '02220 - Site Clearing', Procore will match '02' with '02' in the country-specific standard codes. It will then organize the sections under division headers in your Specifications log.