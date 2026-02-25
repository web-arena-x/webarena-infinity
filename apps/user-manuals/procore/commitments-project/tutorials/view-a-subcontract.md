# View a Subcontract

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/view-a-subcontract

---

## Background

Depending on the permissions that have been granted, you may be able to view the details of a subcontract.

## Things to Consider

- **Required User Permissions:**

 - *To view subcontracts NOT marked Private*, 'Read-Only' level permissions or higher on the project's Commitments tool.
 - *To view subcontracts marked Private*:

    - 'Admin' level permissions on the project's Commitments tool. 
      OR
    - 'Read-Only' or 'Standard' level permissions on the project's Commitments tool and you must be a member of the 'Private' list on the subcontract. 
      OR
    - 'Read-Only' or 'Standard' level permissions on the project's Commitments tool with the ['View Private Work Order Contract' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on the permission template. This permission allows you to view the Change Orders tab on the subcontract.

## Prerequisites

- [Create a Subcontract](/product-manuals/commitments-project/tutorials/create-a-subcontract)

## Steps

1. Navigate to the project's **Commitments** tool.
2. Under the **Contracts** tab, locate the purchase order or subcontract. Then click **Edit**.

   For companies using the ERP Integrations tool, color-coded icons and ribbons appear in relevant areas of Procore to show the current status of an item.

   | **ICON** | **RIBBON** | **COLOR** | **DEFINITION** |
   | --- | --- | --- | --- |
   | | | **YELLOW** | Data that was sent ERP Integrations tool for approval has been retrieved from the tool by an end user. OR Data that was sent to the ERP Integrations tool has been rejected for export to the integrated ERP system by an accounting approver. |
   | | | **GREEN** | Data is synced between Procore and an integrated ERP system. |
   | | | **BLUE** | Data was sent to the ERP Integrations tool and is waiting for accounting approver to accept it for export to the integrated ERP system. |
   | | | **GREEN** | When a user is designated as an accounting approver, this badge appears next to their user profile in the Company and Project Directory. |
3. View the subcontract's information by clicking the following tabs:

   - General Information
   - Schedule of Values
   - Change Orders
   - Invoices
   - Payments Issued
   - Related Items
   - Emails
   - Change History
   - Advanced Settings

#### General Information

- **General Information**View the basic subcontract information that was entered when creating the subcontract.
- **Contract Dates**View important contract dates.
- **Additional Information**View contract inclusions and exclusions.
- **Contract Summary Report**View amounts for the *Original Contract, Approved Change Orders, Revised Contract, Pending Change Orders, Draft Change Orders, Invoices, Payments Issued, Percent Paid,* and *Remaining Outstanding Balance.*

#### Schedule of Values

This tab displays the [Schedule of Values](/glossary-of-terms) for the subcontract, which lists the cost codes, contract amount, billed to date and remaining costs.

#### Change Orders

The Change Orders tab provides an overview of any change orders that have been created for that particular subcontract. You can view the status, the amount, and the due date for each change order. You can also export each change order to a PDF or CSV.

##### Â Note

This tab is available to users with 'Admin' permission on the Commitments tool. If you have 'Read-Only' or 'Standard' permission, you must be added as a member of a commitments 'Private' list in order to see it or your company's [Procore Administrator](https://support.procore.com/procore-learning-paths/general-contractor/procore-administrator) must grant you the appropriate granular permission. See [Grant Granular Permissions in a Permission Template](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template).

#### RFQs

If the Change Events tool is enabled on the project, this tab displays any Request for Quotes (RFQs) that are related to the subcontract.

#### Invoices

This tab displays any invoices submitted for that subcontract and outlines the period, billing date, revised contract sum, payment due, retainage, balance to finish, and percentage complete.

#### Payments Issued

This tab displays all payments that have been issued for the subcontract.

#### Related Items

This tab displays all items related to the subcontract. Related items can be manually added to each subcontract. In this case, the Bid Sheet is automatically listed as a related item because this subcontract was converted to a contract from the Bid Sheet.

#### Emails

This tab displays all email communication associated with the subcontract.

##### Â Note

You will only be able to view this tab if you have 'Admin' level permissions on the Commitments tool or are included in the email.

#### Change History

The Change History tab outlines changes made to the subcontract, who performed the change, details of the change, from what it was changed from and what it was changed to, and the date and time of the change. Items in this history cannot be deleted.

##### Â Note

You can only view this tab if you have 'Admin' level permissions on the Commitments tool.