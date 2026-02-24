# How do I set the accounting method for bids? - Procore

Source: https://support.procore.com/faq/how-do-i-set-the-accounting-method-for-bids

---

##### Note

The content below describes functionality that is part of the new *Bid Management Enhanced Experience*. See [About Bid Management Enhanced Experience](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-bid-management-enhanced-experience "About Bid Management Enhanced Experience").

##### Important

If your project has NOT been updated to Bid Management Enhanced Experience and you are using the Legacy experience, you can choose an accounting method for bids in the [Configure Settings page for Bidding](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/configure-advanced-settings-bidding "Configure Advanced Settings: Bidding"), and when you [create or edit a bid package](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/create-a-bid-package "Create a Bid Package").

*Note:* This change does not affect bid packages that were created before this release. See [Bidding: Flexible Response Types](https://support.procore.com/tc/procore/Legacy/Release_Documentation_Archives/2023/Bidding%3A_Flexible_Response_Types "Bidding: Flexible Response Types (Coming Soon)").

## Background

Instead of being restricted to one accounting method for an entire bid package, you have the flexibility to choose an accounting method for each line item in the 'Field Response Type' column on bid forms.

Through this field, you can also control which bids should have itemized amounts, and which should be lump sum. See the [How can a Lump Sum bid be submitted?](#How_can_a_Lump_Sum_bid_be_submitted.3F "How do I set the accounting method for bids?") section below for more information.

## Answer

For projects using Bid Management Enhanced Experience, users with 'Admin' level permission to the Bidding tool can set the accounting method for each line item in the 'Response Field Type' column on a bid form. See [Create a Bid Form](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/create-a-bid-form "Create a Bid Form"). This column allows you to choose a response type (such as 'Amount') for each line item, providing greater flexibility when soliciting bids.

The 'Response Field Type' column has the following options to select for each line item:

- **Amount**
- **Unit & Quantity**
- **Include/Exclude**

![bidding-response-field-type.png](https://support.procore.com/@api/deki/files/421006/bidding-response-field-type.png?revision=2)

### Considerations

- The 'Include/Exclude' option is only available to select in the Base Bid section. The Alternates section uses 'Amount' and 'Unit & Quantity'.
- The 'Response Field Type' automatically populates as you add line items, but you can change it as needed.
 - The first line item you add to the Base Bid will have the 'Response Field Type' set to 'Amount' by default.
 - When you add another line item, the 'Response Field Type' is automatically copied from the previous line item. For example, if you select 'Include/Exclude' for a line item, the next line item that you add will already have 'Include/Exclude' selected.
- If a bid has already been submitted, you can't edit the Response Field Type for items that were set to 'Amount' or 'Unit & Quantity'.
- If you edit line items on a bid form after bids have been submitted, you'll have an option to send a correspondence about the change and resend bid invitations.

#### How can a Lump Sum bid be submitted?

If you want a bid to be submitted as a lump sum instead of having itemized amounts, you can select 'Include/Exclude' for the line items. This ensures that bidders specify what is or isn't included in their bid, and allows an amount to be entered in the 'Total' field at the end of the bid. See [Submit a Bid on Behalf of a Bidder](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/submit-a-bid-on-behalf-of-a-bidder "Submit a Bid on Behalf of a Bidder") or [Submit a Bid](https://support.procore.com/products/online/user-guide/company-level/planroom/tutorials/submit-a-bid "Submit a Bid").

After the bids have been submitted in Procore, you can use the bid leveling feature to easily identify what's included in the total cost of each bid. See [Level Bids for a Bid Form](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/level-bids-for-a-bid-form "Level Bids for a Bid Form").

## See Also

- [Create a Bid Form](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/create-a-bid-form "Create a Bid Form")
- [How do I set the accounting method for a contract or funding?](https://support.procore.com/faq/how-do-i-set-the-accounting-method-for-a-contract-or-funding "How do I set the accounting method for a contract or funding?")