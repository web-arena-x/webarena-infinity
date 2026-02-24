# Award a Bid and Convert it to a Subcontract or Purchase Order - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/award-a-bid-and-convert-it-to-a-subcontract-or-purchase-order

---

##### Note

The content below describes functionality that is part of the new *Bid Management Enhanced Experience*. See [About Bid Management Enhanced Experience](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-bid-management-enhanced-experience "About Bid Management Enhanced Experience").

## Objective

To select the winning bid and convert it into a new [subcontract](../../../../../../references/construction-management/glossary-of-terms.md#Subcontract "Glossary of Terms") or [purchase order](../../../../../../references/construction-management/glossary-of-terms.md#Purchase_Order "Glossary of Terms").

## Background

With Procore, you now have the flexibility to choose whether to convert the **original bid** or the **leveled bid version** into a subcontract or purchase order. Once a bid (including a leveled bid) is awarded and converted, you can immediately email the resulting contract to the vendor.

If you don't want to create a contract yet, you can also "soft award" a bid. See [Soft Award a Bid](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/soft-award-a-bid "Soft Award a Bid").

## Things to Consider

- **Required User Permissions:**
  - 'Admin' level permissions on the project's Bidding tool.  
    AND
  - 'Admin' level permissions on the project's Commitments tool.
- **For companies using the** ![icon-erp-synced2.png](https://support.procore.com/@api/deki/files/138807/icon-erp-synced2.png?revision=1&size=bestfit&width=39&height=15)**ERP Integrations tool: **Show/Hide**** 

  - The **Convert to Contract** and **Convert to Contract** buttons are only supported when converting an original bid.
    - Leveled bids can not be converted to a contract when the project is ERP-synced.
  - ***Important!*** To sync data with your [integrated ERP system](../../../../../../references/construction-management/glossary-of-terms.md#Integrated_ERP_System "Glossary of Terms"), you must set the cost code cost type (see [Which integrated ERP systems support the 'Cost Type' concept?](https://support.procore.com/faq/which-integrated-erp-systems-support-the-category-concept "Which integrated ERP systems support the 'Cost Type' concept?")) on the contracts as follows:
    - **Integration by Procore**. Use the default cost code cost type set up for Viewpoint® Spectrum® during the implementation process.
    - **Integration by Procore**. Navigate to the **ERP Integrations** tool, click **Configure Settings **![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15)****, and then manually select a default cost code cost type for Vista.
    - **QuickBooks® Desktop**. The cost type for subcontracts should always be set to Other 'O'.
    - **QuickBooks® Online**. Navigate to the **ERP Integrations** tool, click **Configure Settings **![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15)****, and then manually select a default cost code cost type for the contract.
    - **Sage 100 Contractor®**. Navigate to the **ERP Integrations** tool, click **Configure Settings **![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15)****, and then manually select a default cost code cost type for the contract
    - **Sage 300 CRE®**. Navigate to the **ERP Integrations** tool, click **Configure Settings **![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15)****, and then manually select a default cost code cost type for the contract.
    - **Xero™**. Navigate to the **ERP Integrations** tool, click **Configure Settings **![icons-settings-gear.png](https://support.procore.com/@api/deki/files/89566/icons-settings-gear.png?revision=2&size=bestfit&width=15&height=15)****, and then manually select a default cost code cost type for the contract.

## Prerequisites

- The Commitments tool needs to be turned on enabled in order to convert winning bids.
- At least one (1) bid must be submitted from an invited bidder.

## Steps

### Convert an Original Bid to a Commitment

1. Navigate to the project's **Bidding** tool.
2. Click **View** on the bid package you want to award a bid for.
3. Click the name of the company you want to select as the winning bid.  
   OR  
   Click the **vertical ellipsis** ![icon-ellipsis-vertical.png](https://support.procore.com/@api/deki/files/158014/icon-ellipsis-vertical.png?revision=2&size=bestfit&width=16&height=16)icon next to the selected company.  
   *Note:*The selected company must be in the 'Awarded' status.
4. Click the **Award Bidder** menu and select **Convert to Purchase Order** or **Convert to Subcontract**.
5. Click **Award &** **Convert**.  
   *Note:* After the bid is successfully converted, the project's Commitments tool opens to the General tab of the new contract. The appropriate information from the winning bid is automatically copied over to the new contract.
6. Continue to Complete Commitment Details below.

### Convert a Leveled Bid to a Commitment

1. Navigate to the project's **Bidding** tool.
2. Click **View** or the name of the relevant bid package.  
   *Note:* You can also click the name of the bid package.
3. Click the bid form **name**.
4. Click the **Bid Leveling tab**.
5. Click the **Leveled Bids** view.
6. Click the **vertical ellipsis** ![icon-ellipsis-vertical.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEUAAABECAYAAADX0fiMAAAE1klEQVR4AeybXyjsWxTH956bE29KkpKulAd0KJQH3GSIpMyLl3NTvAnFPZk33bniQS6lIfn3ZO4TzgNpXJGikLwcEklxH9yJoRQP3Mnsu9c4pzONPTO/329+s7aHrdbM/q39XbPX+sw2/exlLET9vCGgoLxBQoiC8t6geDyeP1dWVtjQ0BAbGBhg8/Pz7OTk5D9BnqguKTuFMUanpqZYTU3NZ/5DZmdnydzcHOnt7SU2my3Bbrczr9f7CZVE0GLoUDgQS0tLi39kZIT4fL6gVH4Ml5aWSGNjo+v6+vr3H168kQVvqdeVnE7ny97e3utFhMe7uzvS09Pj4BBpBFlcplChnJ+f/zs5Oam5kP39fbKxseHXHGCSEBXKzs5O+svLi67Uj46OdOnNEKNCOT4+1p3z2dmZ7phYA1ChPD8/6843PT1dd0ysAahQ8vPzdeebl5enOybWAFQoJSUluvJNTk4mFRUVv+oKMkGMCqWgoIDyexTNaTscDpKamvqX5gCThKhQIGd+t/qBv/swDGsWi4W0t7eT2tpa4/coYV89+gQ6FEqpj9/iU/73DuyCNxlmZWUFbvk7OzulAIGE0KHAomANDQ10e3ubrq2tbY2NjZGJiQnCrz+73W5aVFQkDQjkJg0KLA6WmZn5i9VqpZWVlZR/foyAT7ZJhyIbgGh9BUVARUFRUAQEBC61UxQUAQGBS+2U9wbl9vbWtrm5yfgRZcBgDD5BnqguaTvF5XIxftP2pa2tjYyPjwcMxuCDOVQKIYuhQ4GDaF486+/vJ09PTyHpkIAP5kAD2jcCBAc6lOnpaT//NYlaGmhAG1UYBwEqlIuLi6/880NzGU6nk0CM5gCThKhQ+Gn+x3ANMFE9oIUY0Vw8fahQjJzmG4mJFRgqlIeHB935Pj4+6o6JNQAVipGT+dzc3Fhr1B2PCqWwsFB3gkZidC8SEoAKpbS0lFZXV4ekEP4StBATXhGfGVQoUAJvW9TyY0cYRjTQgDaiKE6T6FBSUlL+XlhYcJSVlYUtCeZAA9qwojhOoEOBWtLS0v6YmZmhw8PDpKmpicAHMBiMwQdzoAGtDJMC5Xuh9fX1tK+vjy4uLgYMxuD7Pi/rWSoUWUVHW1dBERBSUBQUAQGBC2OnCJZ93y4FRfD+KCgKioCAwKV2ioIiICBwSd8pXq/3N35yz9bX19nV1dUXQY7oLmlQDg4OWF1dHSsvLx/mPR7S0dFBqqqqbPyaud1uhk4iaEEpUHibgzU3N0P7IiiV1yHfOaS7u5t0dXXxXhiT8r9v6FBWV1cZtEn9/shfzuA6+HJUZNErR9MfUaHwXfCJn6ZpLmJ0dJRcXl5+1RxgkhAVytbWluv+/l5z6tAM293d/ag5wCQhKhQjja3T01OTStX+MqhQPB6P9sy+KW9ubr6N8J5QoeTk5OiuzEiM7kVCAjRDCYkzdGnk+z5GYgwlFxSECsVqtf6kp0jQQkxQvihDVCiUUv/g4OBlYmJi1OJAA1qIiSo2WYAKBXLPzs7O4n0dkpGRAZdCgznQgFYoiLMTHQrUU1xcTJeXl39ubW0NNMISEhIIGDTEwAdzoAGtDJMCBQpNSkr6x263B5pgh4eHH8CgKQY+mAONLJMGJbhg/rnhAwv2yRy/CygyAYjWVlAEVP4HAAD//wNXcXYAAAAGSURBVAMAwoKKmLcv6boAAAAASUVORK5CYII=)next to the name of the company you want to select as the winning bid.
7. Select **Convert to Subcontract**  
   OR  
   Select **Convert to Purchase Order**
8. When the **Award Bid & Convert Contract** window opens, choose from the following:
   - **Leveled Bid**: Only includes the most recent bid adjustments, private line items and alternates.
   - **Submitted Bid**: Includes original bid submitted by or on behalf of your bidders.
9. Click **Award &** **Convert**.  
   *Note:* After the bid is successfully converted, the project's Commitments tool opens to the General tab of the new contract. The appropriate information from the winning bid is automatically copied over to the new contract.

### Complete Commitment Details

1. In the 'General' tab of the contract, click the ****Schedule of Values**** tab. To learn more, see [Schedule of Values](https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/view-a-subcontract#Schedule_of_Values "View a Subcontract").
2. To notify the company about the winning bid:
   1. Click **Email Contract**﻿.
   2. In the **Emails** tab, complete the following information:
      - **To**: Select the names of the recipients.
      - **CC**: Select the names of the people who should be copied on the email.
      - **Private**: Mark the checkbox if you only want the recipients and users with 'Admin' level permission to the Commitments tool to see the email. This is the default setting.
      - **Attachments**: Add one or more files to the email message. If appropriate, it is recommended that you add your company's official contract form as an attachment.
      - **Message**: Type the body of your email message. It is recommended to provide clear instructions to your recipients (i.e., subcontractors) with regards to how contracts and documents must be signed. Your message should also include a reminder to return the signed contract, which can conveniently be added as an attachment in their email response.  
        *Note:* The email message will automatically include the contract details.
   3. When you are ready to email the contract, click ﻿**Send﻿**.  
      The system sends the contract to the designated recipients.

## See Also

- [Commitments](https://support.procore.com/products/online/user-guide/project-level/commitments "Commitments")
- [Soft Award a Bid](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/soft-award-a-bid "Soft Award a Bid")
- [Level Bids for a Bid Form](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/level-bids-for-a-bid-form "Level Bids for a Bid Form (Beta)")