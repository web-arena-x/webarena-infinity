# Create a Commitment Potential Change Order

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/create-a-commitment-potential-change-order

---

## Background

When a change to the scope of work or the original [commitment contract](/process-guides/materials-user-guide-with-financials/create-a-change-order-cco) amount occurs during a construction project, the change management process begins. You can create a PCO if your company's [Procore Administrator](https://support.procore.com/procore-learning-paths/general-contractor/procore-administrator) configures the Commitments tool with the two (2)- or three (3)-tier change order configuration setting. See [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)

## Things to Consider

- **Required User Permissions:**

 - Admin' level permissions on the project's Commitments tool.

    ##### Â Important

    **Do not use the steps below when**:

    - The Change Events tool is enabled on the projects. Follow these steps instead: [Create a Commitment Potential Change Order from a Change Event](/product-manuals/change-events-project/tutorials/create-a-commitment-potential-change-order-from-a-change-event).
    - The Commitments tool is configured with the one (1) tier change order configuration setting. Follow these steps instead: [Create a Commitment Change Order](/process-guides/materials-user-guide-with-financials/create-a-change-order-cco).

- **Additional Information:**

 - After a change order is approved, the next step depends on the Commitments tool's change order configuration setting:\* For the two (2)-tier change order setting, continue with [Create a Commitment Change Order](/process-guides/materials-user-guide-with-financials/create-a-change-order-cco).\* For the three (3)-tier change order setting, continue with these steps: [Create a Change Order Request for a Commitment](/product-manuals/commitments-project/tutorials/create-a-change-order-request-for-a-commitment)
- **Limitations**:

 - To create a change order for a commitment, the commitment must be in the 'Approved' status.
- For companies using the ERP Integrations tool: **Show/Hide**

 - Additional considerations, requirements, and limitations can apply depending on the ERP system your account is integrated with. See [Things to Know About your ERP Integration](https://support.procore.com/products/online/user-guide/company-level/erp-integrations/things-to-know-about-your-erp-integration) for details.

## Prerequisites

- The Commitments tool must be configured with the two (2) or three (3) tier change order configuration setting. See [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)

## Steps

- Create a Potential Change Order
- Add a Schedule of Values to a Potential Change Order

### Create a Potential Change Order

1. Navigate to the project's **Commitments** tool.
2. Locate the commitment contract to work with. Then click its **Number** link.
3. Click the **Change Orders** tab.
4. Click **Create Potential CO**.
5. Complete the following fields:

   - **Sign with DocuSignÂ®** If you have enabled the Procore + DocuSignÂ® integration (see [Enable or Disable the DocuSignÂ® Integration on a Procore Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project)), a checkmark appears in this box by default. If you do NOT want to collect signatures with DocuSignÂ®, remove the mark.

     ##### Â Tip

     **How do you collect signatures with DocuSign?** After the data entry for the item is complete, Procore recommends changing the item's status to 'Out for Signature' before clicking the **Complete with DocuSign** button to launch the DocuSignÂ® application. If you have not previously signed in, you will be prompted to [Log In to DocuSignÂ®](/product-manuals/docusign/tutorials/log-in-to-docusign). Once you are signed in, you can prepare the DocuSign\_Â®\_ envelope for signatures. After the signature process is complete, Procore automatically changes the status of the item to 'Approved' and marks the item as 'Executed'. To learn more, see [DocuSignÂ®](/product-manuals/docusign/).

- **Number** Accept the default number, enter a new number, or create a custom numbering scheme.

 ##### Â Tip

 **How are numbers assigned?** To learn how Procore assigns numbers and to understand your custom numbering options, see [Can I customize the numbering system for financial objects in Procore?](/faq-can-i-customize-the-numbering-system-for-financial-management-objects-in-procore)