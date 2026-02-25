# View a Prime Contract's Change Orders (Beta)

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/view-a-prime-contracts-change-orders

---

## Background

To navigate to the change orders associated with a prime contract, click the **Change Orders** tab in the contract. The number of sections in this tab corresponds to the number of change order tiers configured for the project's Prime Contracts tool. See [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)

#### Available Sections in the Change Orders Tab

This table shows which change order sections are available in the **Change Orders** tab of a prime contract.

| Change Order Tier | Prime Contract Change Orders PCCOs | Change Order Requests CORs | Potential Change Orders Prime PCOs |
| --- | --- | --- | --- |
| One (1) Tier |  |  |  |
| Two (2) Tiers |  |  |  |
| Three (3) Tiers |  |  |  |
| *These are the available columns in each section's table* | *Number, Revision, Title, Status, Amount, Date Initiated, Due Date, Review Date, Designated Reviewer, PCOs* | *Number, Revision, Title, Status, Amount, Date Initiated, Due Date Review Date, Designated Reviewer, PCOs* | *Number, Revision, Title, Status, Amount, Schedule Impact, Date Initiated, Change Reason, COR, PCCO, Change Events, Change Event Type* |

## Things to Consider

- **Required User Permissions**:

  - *Private Contracts:*

    - **Admin** level permission on the Prime Contracts tool.   
      OR
    - **Standard** level permissions on the Prime Contracts tool can see change orders they have created.
- **Additional Information**:

  - The number of sections in this tab depends on the number of change order tiers configured in the Prime Contracts tool.

## Prerequisites

Depending on the number of change order tiers configured in your environment, you will need to create one (1) or more of the following items for your prime contract, in order for Procore to list in the available section.

- [Create a Change Order Request for a Prime Contract](/product-manuals/prime-contracts-project/tutorials/create-a-change-order-request)
- [Create a Potential Change Order for a Prime Contract](/product-manuals/prime-contracts-project/tutorials/create-a-potential-change-order-for-a-prime-contract)
- [Create a Prime Contract Change Order](/product-manuals/prime-contracts-project/tutorials/create-a-prime-contract-change-order)

## Steps

1. Navigate to the project's **Prime Contracts** tool.
2. In the contracts table, locate the prime contract.
3. Click the contract's **Number** link to open it.
4. In the contract, click the **Change Orders** tab.

   ##### Example

   Depending on the number of change order tiers configured in your environment, the 'Change Orders' tab includes one (1) to three (3) different sections. See [Configure the Number of Prime Contract Change Order Tiers](/product-manuals/prime-contracts-project/tutorials/configure-the-number-of-prime-contract-change-order-tiers).

- Choose from these options:

  - To open a change order, click one of the hyperlinks in the table in the change order section.
  - To export a list of the change orders, click the **PDF** or **CSV** button at the top of the table.