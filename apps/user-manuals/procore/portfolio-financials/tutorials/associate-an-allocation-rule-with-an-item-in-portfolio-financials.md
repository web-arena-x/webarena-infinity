# Associate an Allocation Rule with an Item in Portfolio Financials

Source: https://v2.support.procore.com/product-manuals/portfolio-financials/tutorials/associate-an-allocation-rule-with-an-item-in-portfolio-financials

---

##### Â Legacy

This information is intended for accounts with [Portfolio Financials](/product-manuals/portfolio-financials/) product in Procore. Please reach out to your Procore point of contact  for more information.

## Background

In order to allocate a percentage of each cost item to components, you must first add an allocation rule. After allocation rules are set, you can see rollups of costs for each component in the 'Components' tab. Associating cost items with cost items will allocate their associated budgets and holds. All invoices submitted against a contract will automatically be associated with the components associated with the chosen Allocation Rule, while change orders can be associated with other rules as necessary.

## Things to Consider

- **Required User Permissions**:

  - 'Full Access' to the project or higher.

## Prerequisites

- Components and allocation rules must be set for the project. See [Add a Component to a Project](/product-manuals/portfolio-financials/tutorials/add-a-component-to-a-project-in-portfolio-financials) and [Add Allocation Rules for Components](/product-manuals/portfolio-financials/tutorials/add-allocation-rules-for-components-in-portfolio-financials).

## Steps

1. Navigate to the **Cost Tracker** section of the **Project Page**.
2. Follow the steps below depending on the type of item that want to associate with the allocation rule:

   - Cost Item
   - Contract
   - Schedule of Values
   - Change Order

#### To associate an allocation rule with a cost item:

*Note:* Associating cost items will allocate their associated budgets and holds.

1. Navigate to the **Cost Tracker** section of the **Project Page**.
2. In the 'Allocation Rule' column, click the drop-down menu for the cost item.
3. Select an existing allocation rule to associate with the cost item.

#### To associate an allocation rule with a contract:

1. Add a new contract. See [Add a Contract to a Cost Item in Portfolio Financials](/product-manuals/portfolio-financials/tutorials/add-a-contract-to-a-cost-item-in-portfolio-financials).
2. Make sure that the 'Cost Breakdown' setting is turned to the OFF  position.
3. Select a rule from the **Contract Allocation Rule** drop-down menu.  
      
      
      
   *Note*: All invoices submitted against this contract will automatically be tagged to the component(s) associated with the chosen allocation rule, while change orders may be associated with other rules as necessary.

#### To associate allocation rules with individual Schedule of Values on a contract:

1. Add a new contract. See [Add a Contract to a Cost Item in Portfolio Financials](/product-manuals/portfolio-financials/tutorials/add-a-contract-to-a-cost-item-in-portfolio-financials).
2. Make sure that the 'Cost Breakdown' setting is turned to the ON  position.  
   *Note:* This process is identical for awarding a Schedule of Values received from a bid.
3. Use the drop-down menus in the **Allocation Rule** column to choose allocation rules for all relevant schedule items.  
      
      
      
   *Note:* Any schedule of values that are not tagged with an allocation rule will NOT appear as committed costs in the Components section of the Project Page.

#### To associate an allocation rule with a change order:

1. Navigate to the **Change Orders** tab of the relevant Contract Room.
2. Add a new change order. See [Add a Change Order in Portfolio Financials](/product-manuals/portfolio-financials/tutorials/add-a-change-order-in-portfolio-financials).
3. Enter all relevant information, and choose a rule from the **Allocation Rule** drop-down menu.  
      
      
      
   *Note:* Change orders will only be allocated to a component if an allocation rule is directly applied to them - regardless of the allocation rule applied to their associated contract.