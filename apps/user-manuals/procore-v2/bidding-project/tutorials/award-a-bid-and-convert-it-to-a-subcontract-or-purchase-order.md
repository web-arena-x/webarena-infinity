# Award a Bid and Convert it to a Subcontract or Purchase Order

Source: https://v2.support.procore.com/product-manuals/bidding-project/tutorials/award-a-bid-and-convert-it-to-a-subcontract-or-purchase-order

---

##### Â Note

The content below describes functionality that is part of the new *Bid Management Enhanced Experience*. See [About Bid Management Enhanced Experience](/process-guides/about-bid-management-enhanced-experience/).

## Background

With Procore, you now have the flexibility to choose whether to convert the **original bid** or the **leveled bid version** into a subcontract or purchase order. Once a bid (including a leveled bid) is awarded and converted, you can immediately email the resulting contract to the vendor.

If you don't want to create a contract yet, you can also "soft award" a bid. See [Soft Award a Bid](/product-manuals/bidding-project/tutorials/soft-award-a-bid).

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Bidding tool. 
     AND
 - 'Admin' level permissions on the project's Commitments tool.
- For companies using the ERP Integrations tool: **Show/Hide**

 - The **Convert to Contract** and **Convert to Contract** buttons are supported.
 - ***Important!*** To sync data with your [integrated ERP system](/glossary-of-terms), you must set the cost code cost type (see [Which integrated ERP systems support the 'Cost Type' concept?](/faq-which-integrated-erp-systems-support-the-category-concept)) on the contracts as follows:

    - ViewpointÂ® SpectrumÂ®. Use the default cost code cost type set up for ViewpointÂ® SpectrumÂ® during the implementation process.
    - Integration by Procore. Navigate to the **ERP Integrations** tool, click **Configure Settings** , and then manually select a default cost code cost type for VistaÂ®.
    - QuickBooksÂ® Desktop. The cost type for subcontracts should always be set to Other 'O'.
    - QuickBooksÂ® Online. Navigate to the **ERP Integrations** tool, click **Configure Settings** , and then manually select a default cost code cost type for the contract.
    - Sage 100 ContractorÂ®. Navigate to the **ERP Integrations** tool, click **Configure Settings** , and then manually select a default cost code cost type for the contract
    - Sage 300 CREÂ®. Navigate to the **ERP Integrations** tool, click **Configure Settings** , and then manually select a default cost code cost type for the contract.
    - Xeroâ¢. Navigate to the **ERP Integrations** tool, click **Configure Settings** , and then manually select a default cost code cost type for the contract.

## Prerequisites

- The Commitments tool needs to be turned on enabled in order to convert winning bids.
- At least one (1) bid must be submitted from an invited bidder.

## Steps

#### Convert an Original Bid to a Commitment

1. Navigate to the project's **Bidding** tool.
2. Click **View** on the bid package you want to award a bid for.
3. Click the name of the company you want to select as the winning bid. 
   OR Click the **vertical ellipsis** icon next to the selected company and skip the next step.
   *Note:* The selected company must be in the '**Awarded**' status.
4. Click the **Award Bidder** menu.
5. Select **Convert to Purchase Order** OR Select **Convert to Subcontract**.
6. Click **Award and Convert.***Note:* After the bid is successfully converted, the project's Commitments tool opens to the General tab of the new contract. The appropriate information from the winning bid is automatically copied over to the new contract.
7. Continue to **Complete Commitment Details** below.

#### Convert a Leveled Bid to a Commitment

1. Navigate to the project's **Bidding** tool.
2. Click **View** or the name of the relevant bid package.
3. Click the bid form **name**.
4. Click the **Bid Leveling** tab.
5. Click the **Leveled Bids** view.
6. Click the **vertical ellipsis icon** next to the name of the company you want to select as the winning bid.
7. Select **Convert to Subcontract**OR Select **Convert to Purchase Order**
8. When the **Award Bid & Convert Contract** window opens, choose from the following:

   - **Leveled Bid:** Only includes the most recent bid adjustments, private line items and alternates.
   - **Submitted Bid**: Includes original bid submitted by or on behalf of your bidders.
9. Click **Award and Convert.***Note:* After the bid is successfully converted, the project's Commitments tool opens to the General tab of the new contract. The appropriate information from the winning bid is automatically copied over to the new contract.

#### Complete Commitment Details

1. In the 'General' tab of the contract, click the **Schedule of Values** tab. To learn more, see [Schedule of Values](/product-manuals/commitments-project/tutorials/view-a-subcontract).
2. To notify the company about the winning bid:

   1. Click **Email Contract** .
   2. In the **Emails** tab, complete the following information:

      - **To**: Select the names of the recipients.
      - **CC**: Select the names of the people who should be copied on the email.
      - **Private**: Mark the checkbox if you only want the recipients and users with 'Admin' level permission to the Commitments tool to see the email. This is the default setting.
      - **Attachments**: Add one or more files to the email message. If appropriate, it is recommended that you add your company's official contract form as an attachment.
      - **Message**: Type the body of your email message. It is recommended to provide clear instructions to your recipients (i.e., subcontractors) with regards to how contracts and documents must be signed. Your message should also include a reminder to return the signed contract, which can conveniently be added as an attachment in their email response. 
        *Note:* The email message will automatically include the contract details.
   3. When you are ready to email the contract, click **Send** . 
       The system sends the contract to the designated recipients.