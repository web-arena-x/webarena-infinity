# Add Sub-Tier Subcontractor Information to Commitments

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/add-sub-tier-subcontractor-information-to-commitments

---

## Background

On construction projects, General Contractors hire first-tier subcontractors (i.e., Specialty Contractors) to perform work. In turn, first-tier subcontractors often hire additional subcontractors and suppliers (i.e., sub-tier subcontractors). This creates a multi-layered payment chain with a critical risk: the potential for a lien to be filed against the property by any lower-tier subcontractors who don't get paid. To mitigate risk, General Contractors must collect documentation (most importantly, lien waivers) from every party that works on the job, not just their direct hires.

To help minimize the administrative burden of collecting and tracking a lien waiver from every sub-tier on a project, Procore Pay centralizes this complex workflow in its Invoice Management tools. In addition, Invoice Management supports a maximum of 100 sub-tiers per commitment, with up to five (5) nested levels.

A General Contractor's invoice administrators can add sub-tier details and documents, like lien notices or joint check agreements, directly to a first-tier subcontractor's commitment at any time. A Specialty Contractor's invoice contact is restricted to adding sub-tier details and documents to their subcontractor invoices when it's in the *Draft* or *Revise & Resubmit* status.

Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)
- **Additional Information**:

  - Permissions for adding and editing sub-tiers differ by stakeholder. A General Contractor's invoice administrator can make these changes on both commitments and subcontractor invoices. In contrast, a Specialty Contractor's invoice contact is restricted to adding sub-tiers to subcontractor invoices only. See [Add Sub-Tier Information for a Subcontractor Invoice](/process-guides/invoice-administrator-guide/add-sub-tier-information-for-a-subcontractor-invoice).
  - You can add up to 100 sub-tiers total. Each sub-tier can have a chain of sub-tiers below it. However, Procore limits the hierarchy to these five (5) levels, from the perspective of the General Contractor. For details, see [What is a sub-tier subcontractor?](/process-guides/invoice-administrator-guide/what-is-a-sub-tier-subcontractor) An error message appears if users attempt to add a sixth level.
  - General Contractors can add or edit sub-tier subcontractors on a commitment at any time. Specialty Contractors can only edit nested sub-tiers on their subcontractor invoice while it's in the *Revise & Resubmit* or *Draft* status.
  - To ensure data integrity, the system also prevents circular nesting of sub-tiers (e.g., a sub-tier hiring itself).
  - To learn more about sub-tier subcontractors, see [What is a sub-tier subcontractor?](/process-guides/invoice-administrator-guide/what-is-a-sub-tier-subcontractor)

## Prerequisites

- [Enable Procore Pay as a Payor](/process-guides/payor-setup-guide/enable-procore-pay)
- [Enable or Procore Pay on Your Projects](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/enable-or-disable-pay)
- [Enable Lien Waivers in the Company Payments Tool](/process-guides/payor-setup-guide/enable-lien-waivers)
- [Enable Lien Waivers & Set Default Templates on Projects](/process-guides/payor-setup-guide/enable-templates-on-projects)
- [Enable Sub-Tier Waivers on Project Invoices as an Invoice Administrator](/process-guides/payor-setup-guide/enable-sub-tier-waivers)
- [Create a Commitment](https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/create-a-commitment)

## Steps

1. Navigate to the Project level **Commitments** tool.
2. In the **Contracts** tab, click the commitment to open.
3. In the commitment, click the **Lien Rights** tab.
4. Click **Add Sub-Tier**.  
    This opens the **Add a Sub-Tier** window.
5. Enter the following information:

   ##### Â Note

   An asterisk (\*) indicates a required field.

- **Sub-Tier Company Name**.\* Type a name for the sub-tier.
- **Hired By**. Select the sub-tier's hiring company from the list.
- **Estimated Contract Amount**.\* Enter the estimated contract amount for this sub-tier.
- **Amount Billed to Date**. Procore automatically calculates the 'Amount Billed to Date' for this sub-tier by totaling all amounts from their previous invoices.
- **Joint Check on All Invoices**. Check this box to issue joint checks for all of this sub-tier's future invoices. This setting is only available for sub-tiers hired directly by the Subcontractor; it is disabled for any sub-tiers hired by all other tiers. See [About Joint Checks with Procore Pay](https://support.procore.com/products/online/procore-pay/tutorials/about-joint-checks-with-procore-pay).
- **Sub-Tier Type**. Choose *Subcontractor* or *Supplier*.
- **Kind of Work**. Enter the sub-tier's scope of work for the commitment.
- **Sub-Tier Waiver Contact Email**. Type the email address for the [sub-tier waiver contact](https://support.procore.com/products/online/user-guide/company-level/payments/glossary).
- **Phone Number**. Type the primary telephone number for this sub-tier.
- **Street Address**. Type the primary address for this sub-tier.

  ##### Â Note

  To add an apartment, suite, or unit number, click the **Add Apt, Suite, Unit** link to show those entry fields.

- **City**. Enter the city for this sub-tier's primary address.
- **State**. Enter the state for this sub-tier's primary address.
- **ZIP**. Enter the postal code for this sub-tier's primary address.
- **Country**. Enter the country for this sub-tier's primary address.
- **Waiver Status**. Select *Active, Final Expected, Final Received, Exempt, or Lien Filed* from the drop-down list. To learn about the statuses, see [What are the sub-tier statuses on a commitment in Procore Pay?](/faq-what-are-the-sub-tier-statuses-on-a-commitment-with-procore-pay)
- **Last Notice Received On**. Select the date the last notice was received.
- **First Date on Project**. Select the date this sub-tier first worked on the project.
- **Last Date on Project**. Select the date this sub-tier last worked on the project.
- **Notes**. Enter any notes about this sub-tier.
- **Notices**. Attach the 'Notices' by clicking the **Attach Files** button or by dragging and dropping PDFs here. You can upload up to 100 files.

  ##### Â Note

  When you upload a file attachment, it immediately appears in the document viewer. If you upload the file, the most recent upload appears first in the document viewer.