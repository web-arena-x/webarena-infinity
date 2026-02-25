# Delete Lien Waiver Templates

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/delete-lien-waiver-templates

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

Only Payments Admins and Payments Disbursers can delete a custom lien waiver template in the payor environment. This permanently removes any custom lien waiver templates from Procore Pay and the system no longer uses it to generate lien waivers on new project invoices. Any previous lien waivers generated from the template on the project's existing invoices can continue to be previewed, signed, and viewed.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)
- **Additional Information**:

  - Lien waivers are powered by Levelset, a Procore Company.
  - You do not need to create a Levelset account with Procore Pay. See [Do I need to create a Levelset account for use with Procore Pay?](/faq-do-i-need-to-create-a-levelset-account-for-use-with-procore-pay)
  - Before deleting a template, be aware that:\* The default lien waiver templates included with Procore Pay cannot be deleted. You can only delete your own custom lien waiver templates.\* A delete action is permanent and cannot be recovered.\* If you delete a lien waiver template before any project lien waivers based on that template are signed by a specialty contractor, signatures will be collected using a lien waiver based on the default template provided by Levelset for the specific project scenario.\* If you delete a lien waiver template after a lien waiver is signed, users can continue to preview and view the signed lien waiver based on that template.

## Prerequisites

- [Create Lien Waiver Templates](/process-guides/payor-setup-guide/create-lien-waiver-templates)

## Video

## Steps

1. Navigate to the Company level **Payments** tool.
2. Click the **Payments Settings**  icon.  
    This opens the Payments Settings page. The Payment Processing tab is active by default.
3. Click the **Payment Requirements** tab.   
    The Lien Waivers page is active by default.
4. Locate the template to delete in the table.

   ##### Â Tip

   **How is the data grouped?** By default, Procore groups lien waiver templates by type. To learn more, see [What types of lien waiver templates can you create in Procore?](/process-guides/payor-setup-guide/about-lien-waivers)

- Click the  **trash can** icon to delete the template.
- In the **Delete Lien Waiver Template?** message, choose an option:

  - To keep the template, click **Cancel**.
  - To permanently remove the template, click **Delete**.

Once deleted, the template no longer appears as a selection in the Invoice Settings. See [Enable Lien Waivers & Set Default Templates on Projects](/process-guides/payor-setup-guide/enable-templates-on-projects). Any previous lien waivers generated from the template on the project's existing invoices can continue to be previewed, signed, and viewed.