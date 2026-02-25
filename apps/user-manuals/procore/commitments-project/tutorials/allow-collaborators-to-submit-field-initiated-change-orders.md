# Allow Collaborators to Submit Field-Initiated Change Orders

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/allow-collaborators-to-submit-field-initiated-change-orders

---

## Background

A *collaborator* is a person or company who has agreed to perform work for you or your company, such as an external contractor or vendor. If you want your collaborators to have the ability to submit potential change orders for their commitments in Procore, you can complete the steps below.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Commitments tool.
- **Additional Information:**

 - To create new [budget codes](/glossary-of-terms) on a change order that were not previously in the contract's scope, the user account must be granted edit access to the contract's [Schedule of Values](/glossary-of-terms) (SOV) with the following granular permissions: '[Update Work Order Contract](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template)' and '[Update Purchase Order Contract](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template)'.

## Steps

### Set the 'Contract Configuration' Settings on the Commitments Tool

1. Navigate to the project's Commitments tool.
2. Click **Configure Settings**.
3. Place a mark in these checkboxes:

   - **Enable Field-Initiated Change Orders** This setting allows users to create change orders from a commitment without granting them access to the Change Events tool.
   - **Allow Standard Level Users to Create CCOs** This setting provides users who have been assigned 'Standard' level permissions on the tool with the added privilege of creating potential change orders when the number of Commitment Change Order tiers is greater than one.
        
     *NOTE:* The setting to 'Allow Standard Level Users to Create PCOs' is only available for two and three-tier change orders.
4. **Add a user account for the collaborator to the project's Directory tool.** First, create a Procore user account for the collaborator(s) that will be submitting field-initiated change orders. You must add this user to the Project Directory. See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory) or [Bulk Add Users and Companies to a Project Directory](/process-guides/set-up-a-project-directory/add-users-from-the-company-directory).

   - If you already created a project permission template for your collaborators, you can assign it to the collaborator when adding the user account.
   - If you do NOT want to create a project permission template, you can edit the user's record and choose 'Do Not Assign a Template' from the 'Project Permissions Templates' section and then manually set the permissions detailed above.
5. **Invite the Collaborator to the Procore project.** In the Project Directory tool, you can then invite (or reinvite) the collaborator(s) to join the project. See [Invite or Reinvite a User to Join a Procore Project](/product-manuals/directory-project/tutorials/invite-or-reinvite-a-person-to-a-project).
6. **Add the user to the 'Private' list on the appropriate commitment contract.** Add the collaborator's name to the 'Select a Person' list in the 'Private' area of the contract as described in [Create a Subcontract](/product-manuals/commitments-project/tutorials/create-a-subcontract). This ensures that the collaborator only has permission to view their own contract.

After the collaborator joins the project and the contract is 'Approved', your collaborator can create change orders against the contract and Procore will use the data entered to automatically create a change event.

## Next Step

- [Submit a Field-Initiated Change Order as a Collaborator (Beta)](/product-manuals/commitments-project/tutorials/submit-a-field-initiated-change-order-as-a-collaborator)