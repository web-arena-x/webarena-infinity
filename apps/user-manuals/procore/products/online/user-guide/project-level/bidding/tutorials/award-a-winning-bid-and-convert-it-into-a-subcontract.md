# Award a Winning Bid and Convert it into a Subcontract - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/award-a-winning-bid-and-convert-it-into-a-subcontract

---

##### Legacy Content

If your project has been updated to [Bid Management Enhanced Experience](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-bid-management-enhanced-experience "About Bid Management Enhanced Experience"), see [Award a Bid and Convert it to a Subcontract or Purchase Order](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/award-a-bid-and-convert-it-to-a-subcontract-or-purchase-order "Award a Bid and Convert it to a Subcontract or Purchase Order") for updated steps.

## Objective

To select the winning bid and convert it into a new [subcontract](../../../../../../references/construction-management/glossary-of-terms.md#Subcontract "Glossary of Terms").

## Background

When you select a winning bid, you have the option to convert it to a subcontract as shown below. After the conversion, you can also send the subcontract by email to the vendor who was awarded the scope of work.

Alternatively, you can also convert a winning bid to a [purchase order](../../../../../../references/construction-management/glossary-of-terms.md#Purchase_Order "Glossary of Terms"). For details, see [Award a Winning Bid and Convert it into a Purchase Order](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/award-a-winning-bid-and-convert-it-into-a-purchase-order "Award a Winning Bid and Convert it into a Purchase Order").

## Things to Consider

- **Required User Permissions:**
  - 'Admin' level permissions on the project's Bidding tool.  
    AND
  - 'Admin' level permissions on the project's Commitments tool.
- **For companies using the** ![icon-erp-synced2.png](https://support.procore.com/@api/deki/files/138807/icon-erp-synced2.png?revision=1&size=bestfit&width=39&height=15)**ERP Integrations tool: **Show/Hide**** 

  - The **Convert to Contract** button is supported.
  - ***Important!*** To sync data with your [integrated ERP system](../../../../../../references/construction-management/glossary-of-terms.md#Integrated_ERP_System "Glossary of Terms"), you must set the cost code cost type (see [Which integrated ERP systems support the 'Cost Type' concept?](https://support.procore.com/faq/which-integrated-erp-systems-support-the-category-concept "Which integrated ERP systems support the 'Cost Type' concept?")) on the subcontracts as follow:
    - **Integration by Procore**. Use the default cost code cost type set up for Viewpoint® Spectrum® during the implementation process.
    - **Integration by Procore**. Navigate to the **ERP Integrations** tool, click **Configure Settings **![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15)****, and then manually select a default cost code cost type for Vista.
    - **QuickBooks® Desktop**. The cost type for subcontracts should always be set to Other 'O'.
    - **Sage 100 Contractor®**. Navigate to the **ERP Integrations** tool, click **Configure Settings **![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15)****, and then manually select a default cost code cost type for the contract
    - **Sage 300 CRE®**. Navigate to the **ERP Integrations** tool, click **Configure Settings **![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15)****, and then manually select a default cost code cost type for the contract.
    - **Xero™**. Navigate to the **ERP Integrations** tool, click **Configure Settings **![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15)****, and then manually select a default cost code cost type for the contract.

## Prerequisites

- The Commitments tool needs to be turned on enabled in order to convert winning bids.
- The company that has the bid being converted to a subcontract must be added to the project directory before the bid conversion.
- To award a contract to the winning bid, the following must be true:
  - The Bid Sheet must be past its Due Date/Time.
  - At least one (1) bid must be submitted from an invited bidder (for example, a subcontractor/vendor).

## Steps

1. Navigate to the project's ﻿**Bidding**﻿ tool.
2. Locate your bid package.
3. Click **View**.
4. In the **Bidders** tab, locate the company with the winning bid.
5. Click **View**.  
   ![view-bidder.png](https://support.procore.com/@api/deki/files/70383/view-bidder.png?revision=4)
6. In the right sidebar, click ﻿**Convert to Subcontract﻿**.  
     
   ![convert-bid-to-subcontract.png](https://support.procore.com/@api/deki/files/79107/convert-bid-to-subcontract.png?revision=4)  
     
   *Notes*﻿*:*
   - The company with the winning bid must be added to the Project Directory in your company's Procore account before creating a purchase order or subcontract.  Companies AND individual users associated with the company are NOT automatically added to the Project Directory.
   - If the conversion was successful, a banner appears to confirm it.  
     ![convert-bid-successful.png](https://support.procore.com/@api/deki/files/83586/convert-bid-successful.png?revision=1)  
       
     Procore launches the project's Commitments tool and opens the new contract's General tab. The appropriate information from the winning bid is automatically completed in the new contract.
7. In the ****General**** tab of the contract, click the ****Schedule of Values**** tab. To learn more, see [Schedule of Values](https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/view-a-subcontract#Schedule_of_Values "View a Subcontract").
8. If you want to notify the company about the winning bid, click **Email Contract**﻿.  
   This reveals the commitment's Emails tab.  
     
   ![email-bid-contract.png](https://support.procore.com/@api/deki/files/83589/email-bid-contract.png?revision=2)
9. In the **Emails** tab, do the following:
   - **To**. Select the names of the desired recipients.
   - **CC**. Select the names of the people who should be carbon-copied on the email.
   - **Private**. Mark the checkbox if you only want the recipients and users with 'Admin' level permission to the Commitments tool to see the email. This is the default setting.
   - **Attachments**. Add one or more files to the email message. If appropriate to your situation, it is recommended that you always add your company's official contract form as an attachment.
   - **Message**. Type the body of your email message. It is recommended that you always provide clear instructions to your recipients (i.e., subcontractors) with regards to how contracts and documents must be signed. Your message should also include a reminder to return the signed contract, which can conveniently be added as an attachment in their email response.  
     *Note:* The email message will automatically include the contract details.
10. Click ﻿**Send﻿**.  
    The system sends the contract to the designated recipients.

## See Also

- [Award a Winning Bid and Convert it into a Purchase Order](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/award-a-winning-bid-and-convert-it-into-a-purchase-order "Award a Winning Bid and Convert it into a Purchase Order")

If you would like to learn more about Procore's bidding software and how it can help your business, please visit our [construction bidding software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/bidding "https://www.procore.com/project-management/bidding").