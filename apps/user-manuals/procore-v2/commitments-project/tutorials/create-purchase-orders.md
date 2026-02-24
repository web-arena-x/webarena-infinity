# Create Purchase Orders

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/create-purchase-orders

---

## Background

In Procore, a *Purchase Order (PO)* is a documented financial *commitment* that details the types, quantities, and agreed-upon prices for products or services. As part of the procurement process, purchase orders are created by a 'buyer' (for example, a *general contractor*) and issued to a 'seller' (for example, a *subcontractor*) to cover the cost of a contract. Once accepted by the 'seller,' a purchase order represents an agreement between the two parties

## Things to Consider

- **Required User Permissions:**

 - *To create a purchase order and see/enter data on the Schedule of Values (SOV) tab:*

    - Admin' level permissions on the project's **Commitments** tool.   
      OR
    - 'Standard' level permissions on the project's **Commitments** tool and the **Allow Users to See SOV Items** setting must be enabled and your name must be selected in the **Select a Person** drop-down list.
- **For companies using the** **ERP Integrations tool:** Prerequisites, requirements, limitations, and considerations might apply depending on the ERP system your Procore account is integrated with.

## Prerequisites

- [Configure Advanced Settings: Commitments](/product-manuals/commitments-project/tutorials/configure-advanced-settings-commitments)

## Steps

1. Navigate to the project's **Commitments** tool.
2. On the **Contracts** tab, click the **Create** button and choose **Purchase Order** from the drop-down list.

   ##### Â Note

   - The **Create** button is available when you are viewing the Contracts and Recycle Bin tabs. New purchase orders are always added to the Contracts tab.
   - The **Export** button is only available on the Contracts tab. To learn more, see [Export a Commitments List](/product-manuals/commitments-project/tutorials/export-a-commitments-list).

- Continue with the next steps:

 - Add the Basic Information
 - Update the General Information
 - Update the Contract Access
 - Update the Contract Dates
 - Update the Schedule of Values

    - Add Line Items to the Schedule of Values
    - Import Line Items to the Schedule of Values from a CSV File
 - Attach Files
 - Save the Contract

#### Add the Basic Information

Update the basic information as follows:

##### Â Notes

- There are no required fields when adding the basic information.
- If you click the **Create** button without completing any data entry, Procore saves the contract, lists you as the creator, and automatically places it in the *Draft* status.

- **Contract Number**To number your contract(s), choose from these options:

 - If you number your contracts using a sequential numbering system, you can enter any combination of alpha-numeric characters in this box. For subsequent contracts, Procore automatically applies consecutive numbering in ascending order.

    ##### Example

    The examples below show you how Procore's ascending consecutive numbering works:

    - If the previous contract was 1, the next contracts are 2, 3, and so on.
    - If the previous contract was PC-0001, the next contracts are PC-0002, PC-0003, and so on.
    - If the previous contract was DCA00010-12-G-0001, the next contracts are DCA00010-12-G-0002, DCA00010-12-G-0003, and so on.