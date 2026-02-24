# Configure Settings: Project Admin

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/configure-settings-project-admin

---

## Background

The options in the Project Settings menu give you the ability to configure a variety of advanced settings for a project.

## Things to Consider

- **Required User Permissions:**

 - You need one of the following:

    - 'Admin' level permissions on the Project level Admin tool.
    - For many actions, 'Read Only' or Standard' permissions on the Project level Admin tool, AND one or more granular permissions. See [Grant Granular Permissions in a Project Permissions Template](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) for more information.

## Steps

To learn about your options, click a link below:

- Configure Project Settings
- Tool Configuration
- Permissions

### Configure Project Settings

Under **Project Settings**, click a link to perform the following tasks:

| Project Settings | Click this link... | To perform these tasks... |
| --- | --- | --- |
| | **General** | [Update General Project Information](/product-manuals/admin-project/tutorials/update-general-project-information) [Enable ERP Job Cost Transaction Syncing on a Procore Project](/product-manuals/erp-integrations-company/tutorials/enable-erp-job-cost-transaction-syncing-on-a-procore-project) [Export a PCCO with Multiple PCOs as Individual PCIs to CMiC](/product-manuals/cmic/tutorials/export-a-pcco-with-multiple-pcos-as-individual-pcis-to-cmic) [Export a PCCO as an OCO to CMiC](/product-manuals/cmic/tutorials/export-a-pcco-as-an-oco-to-cmic) |
| | **Active Tools** | [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools) |
| | **Work Breakdown Structure****1** | [Create Your Project's Work Breakdown Structure](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/create-your-projects-wbs) |
| | **Working Days** | [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days) |
| | **Locations** | [Download & Install the Procore BIM Plugin](/product-manuals/procore-bim-plugins/download-install) [Add Tiered Locations to a Project](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project) [Edit Tiered Locations](/product-manuals/admin-project/tutorials/edit-multi-tiered-locations) [Delete Tiered Locations](/product-manuals/admin-project/tutorials/delete-multi-tiered-locations) |
| | **Spec Sections****2** | [Add Spec Sections to the Admin Tool](/product-manuals/admin-project/tutorials/add-spec-sections-to-the-admin-tool) [Import Spec Sections to the Admin Tool](/product-manuals/admin-project/tutorials/import-spec-sections-to-the-admin-tool) [Edit Spec Sections in the Admin Tool](/product-manuals/admin-project/tutorials/edit-spec-sections-in-the-admin-tool) [Delete Spec Sections from the Admin Tool](/product-manuals/admin-project/tutorials/delete-spec-sections-from-the-admin-tool) |
| | **Classifications** | [Enable Classifications on a Project](/product-manuals/admin-project/tutorials/enable-classifications-on-a-project) |
| | **Equipment** | [Add Equipment](/product-manuals/admin-project/tutorials/add-equipment) |
| | **Webhooks** | [Configure Project Webhooks](/product-manuals/admin-project/tutorials/configure-webhooks) |
| | **Unit Quantity Based Budget** | [Import a Unit Quantity Based Budget](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/import-your-budget) |

1 *Cost code, cost type, and the optional sub job segment are part of Procore's* [Work Breakdown Structure](https://support.procore.com/products/online/work-breakdown-structure)*. For the 'Sub Jobs' segment to appear, your company's Procore Administrator must enable the sub job feature. See* [Enable Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects)*.*

2 *The 'Spec Sections' link only appears when the Project level Specifications tool is NOT an active tool on the project.*

### Tool Configuration

To learn about the options in the **Tool Configuration** menu, see the links below:

*Note:* These options only appear if the corresponding tool is active on the project. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools)

| Tool Configuration | Click this link... | To perform these tasks... |
| --- | --- | --- |
| | **Home** | [Update the Project Home Settings](/product-manuals/home-project/tutorials/configure-advanced-settings-project-home) |
| | **Emails** | [Configure Advanced Settings: Emails](/product-manuals/emails-project/tutorials/configure-advanced-settings-emails) |
| | **Bidding** | [Edit Project Bidding Configuration](/product-manuals/admin-project/tutorials/edit-project-bidding-configuration) |
| | **Punch List** | [Configure Advanced Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list) |
| | **Documents** | [Configure Advanced Settings: Project Documents](/product-manuals/documents-project/tutorials/configure-advanced-settings-documents) |

### Permissions

1. Click the **Configure Settings** icon. 
   *Note:* The **Permissions Table** page automatically opens.
2. Set the user's access permission level for the tool by clicking the icon in the desired column so a GREEN checkmark appears:
3. The color-coded icons in the user permissions area denotes the user's access permission level to the tool. To learn more, see [What are the default permission levels in Procore?](/faq-what-are-the-default-permission-levels-in-procore)

   | Icon | Color | Definition |
   | --- | --- | --- |
   | | **GREEN** | The user has been granted this access permission level to the tool. |
   | | **RED** | The user has NOT been granted this access permission to the tool. |
   | | **GREY** | The user is either a Procore Administrator or has been granted permissions to the Procore tools on this project using a permissions template (see [What is a permissions template?](/faq-what-is-a-permissions-template)). |