# Create a Bid Template - Procore

Source: https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-a-bid-template

---

##### In Beta

This feature is currently in beta for customers using the [**Enhanced Bid Management Experience**](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-bid-management-enhanced-experience "About Bid Management Enhanced Experience"). Follow these steps to opt in:

1. Navigate to the Company level **Admin** tool.
2. Under 'Project Settings', select **Bidding**.
3. In the 'New! Template Collections (Beta)' banner, click **Opt-In**. 
   ![clipboard_ec02d02345c49988b51dc4ceaba65bcc2.png](https://support.procore.com/@api/deki/files/515859/clipboard_ec02d02345c49988b51dc4ceaba65bcc2.png?revision=1)
4. Review the beta participant terms and mark the checkbox to agree.
5. Click **Accept Terms** to opt in.

## Objective

To create a bid template in the Company Admin tool.

## Background

Bid templates significantly reduce the time needed to create Bid Packages and Bid Forms. You can create templates for your bid forms and prospective bidders to use in your projects. These templates include details such as line items, amounts, included and excluded scope. Bidder lists can encompass both companies and specific bid recipients.

You have the option to create new templates or convert an existing bid package into a template.

When building bid packages for a project, simply select these templates to efficiently create your bid forms and bidder lists.

## Things to Consider

- **Required User Permissions:**
 - *To view, create, or edit a bid template*:
    - 'Admin' level permissions for the Company Admin tool.  
      AND
    - 'Read Only' level permissions or higher for the Company Directory tool.
- Bid templates can only be created with ****Base bid**** and ****Alternates**** scope.
- Bid Templates can only utilize cost codes from the Company level of Procore. Project specific cost codes need to be added at the project level.

## Prerequisites

- Bid templates must be created within an existing ****[Bid](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-a-bid-template-collection "Create a Bidding Template Collection")**** ****[Template Collection](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-a-bid-template-collection "Create a Bidding Template Collection").****

## Steps

1. Navigate to the Company's **Admin** tool.
2. Under '****Tool Settings****', click ****Bidding****.
3. Navigate to the **Templates**tab.
4. Click the name of Template Collection where the Template will be created. See **[Create a Bid Template Collection](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-a-bid-template-collection "Create a Bidding Template Collection").**
5. Click **Create**in the **Bid Templates** panel.
6. Enter a **Name**for the Bid Template.

#### Add Sections (Optional)

1. Click ****Add Section****.
2. Enter a name for the section.
3. To add a line item for the section, click the ****Add Line Item**** menu or the ****plus +****icon for the section****.  
   ![bidding-add-line-item.png](https://support.procore.com/@api/deki/files/445920/bidding-add-line-item.png?revision=1)****
4. Continue adding sections and line items as necessary.
5. **Optional:**To reorder sections or line items, click and drag over the grip ![icon-reorder-grip.png](https://support.procore.com/@api/deki/files/120680/icon-reorder-grip.png?revision=1&size=bestfit&height=16) icon and drop it in a new area.
6. **Optional:**If you need to delete a section, click the ****vertical ellipsis**** ![icon-ellipsis-vertical.png](https://support.procore.com/@api/deki/files/158014/icon-ellipsis-vertical.png?revision=2&size=bestfit&width=16&height=16) icon and select ****Delete****. This will delete the section and all of its line items.

#### Add Line Items

1. In the Base Bid section, click the ****Add Line Item**** drop-down menu.
2. Select one of the following line item types:
   - ****Cost Code****: Select if you want to add a line item with a cost code.
   - ****Plain Text****: Select if you want to add a general line item without a cost code.
3. Enter the following information: 
   ****Note:****Required fields are indicated by an asterisk (\*).
   - ****Items\*****:
     - For a Cost Code line item, click the ****Select Cost Code**** drop-down menu and select a cost code.
     - For a Plain Text line item, click into the field and enter a name for the item.
   - ****Description****: Enter a description for the line item, if necessary.
   - ****Response Field Type\*****: Select a response type for the line item. The 'Response Field Type' automatically populates based on the previous line item added, but you can change it as needed.
     - ****Amount****: Select if an amount should be entered.
     - ****Unit/Quantity****: Select if a unit and quantity should be entered.
     - ****Include/Exclude****: Select if this line item should be entered as an inclusion or exclusion for the bid.
4. To add additional line items, click ****Add Line Item**** and repeat the same process.  
     
   ![bid-template-add-sections.png](https://support.procore.com/@api/deki/files/500638/bid-template-add-sections.png?revision=1)
5. If you want to allow bidders to provide alternative options or substitutions, scroll to the Alternates section and add line items as necessary.
6. Click **Create**when the Bid Template is complete.

### Add Bidders

1. In the Bidders section, click the ****Add Bidders****.
2. Use the ****Search**** ****bar**** and ****Filters**** menu to find existing companies from the Company level Directory tool.
3. Mark the checkbox next to each company you want to add to the bid form.
4. Click **Add Bidders**when you are finished adding bidders to the Bid Template. 
   *Note:*Bidders added to a Bid Template will NOT be notified.

![bid-template-add-bidders.png](https://support.procore.com/@api/deki/files/500637/bid-template-add-bidders.png?revision=1&size=bestfit&width=1104&height=596)

## Next Steps

- [Create a Bid Package](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/create-a-bid-package "Create a Bid Package")

## See Also

- [Create a Bid Package](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/create-a-bid-package "Create a Bid Package")