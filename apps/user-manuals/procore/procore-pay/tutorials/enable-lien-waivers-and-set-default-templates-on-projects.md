# Enable Lien Waivers & Set Default Templates on Projects

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/enable-lien-waivers-and-set-default-templates-on-projects

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

For payors managing lien waivers with Procore Pay, an invoice administrator enables lien waiver types and templates for the Project level Invoice Management tools in Procore. On each Procore project, an invoice administrator can enable *Conditional*, *Unconditional*, or both types of lien waivers. To learn more, see [What types of lien waiver templates can you create in Procore?](/process-guides/payor-setup-guide/about-lien-waivers)

Payors also have these options:

- If your company's Payments Admin has created one or more lien waiver templates in the Company level Payments tool, you can also set the default lien waiver template to generate for your project's invoices. Once enabled, the Procore Pay software can generate the appropriate lien waiver(s) on a project invoice.
- If your company wants to collect sworn statements on your first- and sub-tier lien waivers, your template must include the sworn statement fields. Procore Pay's sworn statements comply with [Chicago Title Waiver Format](https://support.procore.com/products/online/user-guide/company-level/payments/glossary).

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)
- **Additional Information**:

  - Lien waivers are powered by Levelset, a Procore Company.
  - You do not need to create a Levelset account with Procore Pay. See [Do I need to create a Levelset account for use with Procore Pay?](/faq-do-i-need-to-create-a-levelset-account-for-use-with-procore-pay)
  - To select a template in the steps below:\* The project must have an 'Address', 'City', 'State', and 'ZIP' provided in the Project level Admin tool on the General tab in the [Project Location](/product-manuals/admin-project/tutorials/update-general-project-information) section.\* The project's state must match the 'State' defined in a lien waiver template. See [Create Lien Waiver Templates](/process-guides/payor-setup-guide/create-lien-waiver-templates).
  - To learn about the waiver configuration settings that carry over to a project template, see [What gets copied over to a new project from a project template?](/faq-what-gets-copied-over-to-a-new-project-when-applying-a-project-template)
  - To include sworn statements as part of a lien waiver template, contact your Procore point of contact .

## Prerequisites

- [Enable or Disable Procore Pay on Your Projects](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/enable-or-disable-pay)
- [Create Lien Waiver Templates](/process-guides/payor-setup-guide/create-lien-waiver-templates)
- [Enable Lien Waivers in the Company Payments Tool](/process-guides/payor-setup-guide/enable-lien-waivers)
- If you plan to collect sworn statements with Procore Pay, you must also:

  - [Enable Sworn Statement Collection for Lien Waivers as a Payor](/product-manuals/procore-pay/tutorials/enable-sworn-statement-collection-for-lien-waivers-as-a-payor)

## Steps

- [Enable Lien Waivers](#enable-lien-waivers)   
   OR
- [Enable First- and Sub-Tier Lien Waivers with Sworn Statement](#enable-first-and-subtier-waivers-with-sworn-statements)

## Enable Lien Waivers

1. Navigate to the Project level **Invoicing** tool.
2. Click the **Settings**  icon.  
    This opens the Invoicing tool's Settings page.
3. Scroll to the **Lien Waivers** section. Then choose from these options:

   ##### Â Tips

   - **Don't see any options?** The lien waiver settings must be enabled for Procore Pay. See Enable Lien Waivers in the Company Payments Tool. See The project must have a 'State' selected in the Project level Admin tool on the General tab in the Project Location section.
   - **What do the different lien waiver types mean?** To learn about the types, see What types of lien waiver templates can you create?

- **Enable Conditional Lien Waivers**  
   Mark this checkbox to enable the use of any conditional lien waiver templates created for use by your company. Clear the checkbox to disable the use of those templates. When you mark the checkbox, you also have the option to set the default template for the project:

  ##### Â Tips

  - **Why am I seeing a 'No template' message?** If the 'No template' message appears, create a lien waiver template for the waiver type. See [Create Lien Waiver Templates](/process-guides/payor-setup-guide/create-lien-waiver-templates). To appear in this list, the 'State' defined for the template must match the Procore project's [Project Location](/product-manuals/admin-project/tutorials/update-general-project-information) information.
  - **How do I know if a lien waiver is compliant with State requirements?** For states that mandate the use of a specific lien waiver form, Procore Pay's Levelset integration provides lien waiver templates that comply with state requirements. For states without mandates, best practice templates are available. See [Lien Waiver Release Forms - State by State](https://www.levelset.com/blog/lien-waiver-form/#Lien%5FWaiver%5FRelease%5FForms%5F-%5FState%5Fby%5FState) on the Levelset website. *Note*: Your company must ensure that lien waiver templates comply with all applicable laws and regulations. Always consult a legal advisor.
  - **Why can't I select a template from the drop-down list?** If the drop-down list is grayed out and unavailable, Levelset's lien waiver database has determined that lien waiver type is unavailable in the project's State.
  - **What do the different lien waiver types mean?** To learn about the types, see [What types of lien waiver templates can you create?](/process-guides/payor-setup-guide/about-lien-waivers)