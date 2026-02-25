# Enable or Disable the Subcontractor SOV Tab on the Commitments Tool

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/enable-or-disable-the-ssov-tab-on-the-commitments-tool

---

## Background

In Procore's Commitments tool, the Subcontractor SOV tab provides contractors who perform project work with a place to enter a detailed SOV breakdown about a commitment. The Subcontractor SOV is separate from the general SOV tab on a commitment. Once completed, the line items on the Subcontractor SOV can be submitted for review and approval of the work. By default, the Subcontractor SOV tab is enabled in Procore's Commitments tool.

You can enable or disable the Subcontractor SOV tab on:

- **All of the purchase orders and subcontracts in the project's Commitments tool**. For instructions, see below.
- **An individual purchase order or subcontract**. For instructions, see [Enable or Disable the Subcontractor SOV Tab on a Commitment](/product-manuals/commitments-project/tutorials/enable-or-disable-the-ssov-tab-on-a-commitment).

Once enabled, the line items on the Subcontractor SOV tab are automatically included in your project's [subcontractor invoices](/glossary-of-terms). To learn more, see [About Subcontractor Invoices](/product-manuals/invoicing-project/tutorials/about-subcontractor-invoices).

## Things to Consider

- [Required User Permissions](/product-manuals/commitments-project/permissions)
- **Additional Information:**
- By default, the Subcontractor SOV tab is enabled in the project's Commitments tool.
- **Limitations:**

 - The Subcontractor SOV tab is only supported when a purchase order or subcontract is configured to use the Amount Based accounting method. It is NOT supported with the Unit-Quantity Based accounting method. See [How do I set the accounting method for a contract or funding?](/faq-how-do-i-set-the-accounting-method-for-a-contract-or-funding)

## Prerequisites

- Add the Commitments tool to the project. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).

## Steps

1. Navigate to the project's **Commitments** tool.
2. Click the **Configure Settings** icon.
3. On the **Contract Configuration** page, scroll to the **Default Contract Settings** area.
4. In the **Enable Subcontractor SOV by Default** check box, do the following:

   - To enable the tab, place a mark in the check box. This is the default setting.
   - To disable the tab, remove the mark from the check box.

     ##### Â Notes

     - The Subcontractor SOV tab is only supported when a purchase order or subcontract is configured to use the Amount Based accounting method. It is NOT supported with the Unit-Quantity Based method. See [How do I set the accounting method for a contract or funding?](/faq-how-do-i-set-the-accounting-method-for-a-contract-or-funding)
     - If the 'Enable Always Editable Schedule of Values' configuration setting is turned ON in the Commitments tool, be aware of some important limitations. For details, see [What is the 'Enable Always Editable Schedule of Values' setting?](/faq-what-is-the-enable-always-editable-schedule-of-values-setting)

- Click **Update**.