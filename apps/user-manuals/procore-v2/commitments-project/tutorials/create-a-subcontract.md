# Create a Subcontract (Legacy)

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/create-a-subcontract

---

##### Â Legacy Content

This tutorial details Procore's legacy experience for creating a subcontract. The information on this page will be replaced with updated content when the redesigned commitments beta experience is generally available.

***Important!*** If you are using the commitments beta experience, please see the [Create Subcontracts](/product-manuals/commitments-project/tutorials/create-subcontracts) tutorial instead of the information below.

## Background

Subcontracts can be awarded during both the preconstruction and construction phases of a project and are typically created and tracked in Procore by project management. After a prime contract award, the project manager creates purchase orders and subcontracts for specific trades to secure materials and subcontractor services for a project.

## Things to Consider

- **Required User Permissions:**

 - *To create a subcontract and see/enter data on the Schedule of Values (SOV) tab, users must have one of the following permissions levels:*

    - 'Admin' level permissions on the project's Commitments tool.
    - 'Standard' level permissions on the project's Commitments tool and the 'Allow Users to See SOV Items' setting must be enabled and your name must be selected in the 'Select a Person' drop-down list
 - *To create a subcontract only*, 'Read Only' or 'Standard' level permissions on the project's Commitments tool with the 'Create Work Order Contract' granular permission enabled on your permissions template.
- **Additional Information:**

 - An alternative way to create a subcontract is to award a winning bid and convert it into a subcontract. See [Award a Winning Bid and Convert it into a Subcontract](/product-manuals/bidding-project/tutorials/award-a-winning-bid-and-convert-it-into-a-subcontract).
 - To set the accounting method for the subcontract, see [How do I set the accounting method for a contract or funding?](/faq-how-do-i-set-the-accounting-method-for-a-contract-or-funding)
 - **For companies using the** **ERP Integrations tool:** Prerequisites, requirements, limitations, and considerations might apply depending on the ERP system your Procore account is integrated with.

## Prerequisites

- [Configure Advanced Settings: Commitments](/product-manuals/commitments-project/tutorials/configure-advanced-settings-commitments)
- To use the Procore + DocuSignÂ® integration to request signatures on a contract, see [Enable or Disable the DocuSignÂ® Integration on a Procore Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project).

## Steps

- Step 1: Create a Subcontract
- Step 2: Enter the Schedule of Values (SOV)

#### Step 1: Create a Subcontract

1. Navigate to the project's **Commitments** tool.
2. Click **+Create** and select **Subcontract** from the drop-down menu.
3. In the 'General' tab under 'General Information', do the following:

   - **Sign with DocuSignÂ®**If you have enabled the Procore + DocuSignÂ® integration (see [Enable or Disable the DocuSignÂ® Integration on a Procore Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project)), a checkmark appears in this box by default. If you do NOT want to collect signatures with DocuSignÂ®, remove the mark.

     ##### Â Tip

     **How do you collect signatures with DocuSign?** After the data entry for the item is complete, Procore recommends changing the item's status to 'Out for Signature' before clicking the **Complete with DocuSign** button to launch the DocuSignÂ® application. If you have not previously signed in, you will be prompted to [Log In to DocuSignÂ®](/product-manuals/docusign/tutorials/log-in-to-docusign). Once you are signed in, you can prepare the DocuSign\_Â®\_ envelope for signatures. After the signature process is complete, Procore automatically changes the status of the item to 'Approved' and marks the item as 'Executed'. To learn more, see [DocuSignÂ®](/product-manuals/docusign/).

- **Number #**Accept the default number, enter a new number, or create a custom numbering scheme.

 **For companies using the** **ERP Integrations tool:**

 - In order to send the commitment to the ERP Integrations tool to be accepted for export by an accounting approver:

    - Your integrated ERP system may impose a maximum character limit.
    - Prerequisites, limitations, and considerations might apply depending on the ERP system your Procore account is integrated with. Visit Things to Know about your ERP Integration for details.
- **Title**Enter a descriptive title for the subcontract.
- **Contract Company**Select the company responsible for completing the work on the subcontract (for example, American Construction Co.). 
 *Notes*:

 - To appear in this list as a selection, add the company to the Project Directory.
 - You must select a contract company before you can name an invoice contact.
- **Invoice** **Contacts**Select one (1) or more employees of the 'Contract Company' to designate as the invoice contact(s). After saving the subcontract, any users added here will be added to the 'Private' list. You must select a 'Contract Company' before you can select invoice contacts.
- **Status**Assign a status to the subcontract.
- **Executed**. Mark this checkbox to denote that the subcontract was fully signed and executed.

 ##### Â Notes

 - Many Procore users choose to place a checkmark in the Executed box when placing the commitment into the 'Approved' or 'Complete' status.
 - The time at which your project team places a checkmark in the Executed box should always be aligned with your project's unique business process