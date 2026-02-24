# Delete a Prime Contract

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/delete-a-prime-contract

---

## Background

Typically, most project users will only want to delete a prime contract from a Procore project before it is placed into the 'Approved' status and before your project team starts creating [Prime Contract Change Orders](/glossary-of-terms) (PCCOs).

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Prime Contracts tool.  
     OR
  - 'Read Only' or 'Standard' level permissions on the project's Prime Contracts tool with the ['Delete Prime Contract' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template.
- **Additional Information:**

  - You cannot delete a contract in the 'Approved' status.
  - You cannot delete a contract if your team has created any change orders.

## Steps

1. Navigate to the project's **Prime Contracts** tool.
2. Locate the contract to delete. Then click its **Number** link.
3. Click **Delete**.

   ##### Â Notes

   If the **Delete** button is grayed out and unavailable, hover your mouse cursor over the button's tooltip to discover the reason why. Typically, the delete button is unavailable only when one or more of the following reasons is true:

   - The prime contract is in the 'Approved' status.
   - The prime contract has one or more Prime Contract Change Orders (PCCOs). You must always delete PCCOs before you can delete a prime contract. See [Delete a Prime Contract Change Order](/product-manuals/prime-contracts-project/tutorials/delete-a-prime-contract-change-order).

- Click **OK** in the confirmation window.