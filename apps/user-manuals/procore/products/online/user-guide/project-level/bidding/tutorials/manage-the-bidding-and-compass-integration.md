# Manage the Bidding and COMPASS Integration - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/manage-the-bidding-and-compass-integration

---

Table of Contents

**Table of Contents**

- Welcome 
  - [Overview](https://support.procore.com/#)
  - [Requirements](https://support.procore.com/#)
- [Enable or Disable the Integration](https://support.procore.com/#)
- Sync COMPASS Data to Procore 
  - [Verify COMPASS Data](https://support.procore.com/#)
  - [Add Companies to your Directory](https://support.procore.com/#)
  - [Update Companies in your Directory](https://support.procore.com/#)
- View COMPASS Data When Adding Bidders 
  - [Add from Directory](https://support.procore.com/#)
  - [Add from Procore Construction Network](https://support.procore.com/#)
  - [Add from Single Contractor View](https://support.procore.com/#)
- [View COMPASS when Leveling Bids](https://support.procore.com/#)

## Overview

##### **NOTE: This article is linked in the Procore app under the Bidding Tool in the Compass Banner.**

Article link: [https://support.procore.com/products...ss-integration](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/manage-the-bidding-and-compass-integration "https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/manage-the-bidding-and-compass-integration")

##### Limited Release

The COMPASS integration is available to users of the [Enhanced Bid Management experience](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-bid-management-enhanced-experience "About Bid Management Enhanced Experience") in the **United States** and **Canada**.

Procore customers using COMPASSby Bespoke Metrics can seamlessly view COMPASS qualification data and invite companies to qualify directly within the Bidding tool on a Procore project. If your company does **not**have a COMPASS account, you can still access Procore project data, and the QScore for companies listed in the Procore Construction Network.

This guide will walk you through the following steps:

1. Enable the COMPASS Integration
2. Sync COMPASS Data to Procore
   1. Add or Update COMPASS Companies in your Directory
3. View Qualification Data in the Bidding Tool

##### Tip

Learn more [about the Bidding + Compass Integration](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-the-bidding-compass-integration "About the Bidding + COMPASS Integration") including answers to [common questions](about-the-bidding-compass-integration.md#chapt4 "About the Bidding + COMPASS Integration").

## Requirements

- **Required User Permissions:**
  - 'Admin' level permissions on the project's Bidding tool.
- **Additional Requirements**
  - Your company must have an active subscription to Procore Bid Management.
  - Your projects must also be upgraded to the [Enhanced Bid Management](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-bid-management-enhanced-experience "About Bid Management Enhanced Experience") experience.
  - To view COMPASS data for companies listed in your Directory, the company's EIN number must be added to the company's details.

## Enable or Disable the Integration

1. Navigate to the [COMPASS integration page](https://marketplace.procore.com/apps/compass-by-bespoke-metrics "https://marketplace.procore.com/apps/compass-by-bespoke-metrics") in the Procore App Marketplace.
2. **Login** to your Procore account and confirm you have selected the correct company.
3. Click **Install**.
   - You will be redirected to the Company Admin Tool Settings page for Bidding in Procore.
4. Click **Login** to COMPASS to turn on data sharing from COMPASS to Procore for your account.

##### Note

To **disable** the COMPASS integration:

1. Navigate to the Company level **Admin** tool.
2. Click **Bidding** under [Tool Settings](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/configure-tool-settings-from-the-company-admin-tool "Configure Tool Settings from the Company Admin Tool").
3. Click ****Logout of COMPASS****.

## Verify COMPASS Data

1. Ensure that the subcontractor is fully entered in COMPASS with the following information:  
   *Note:* You will not be able to edit this information, however it is required for the Procore integration.
   - **Legal Company Name**
   - **Accurate Mailing Address**
   - **FEIN (Tax ID Number)**
2. Allow time for data to sync to Procore. COMPASS syncs to Procore twice per day. New vendors added to COMPASS will not appear in Procore immediately, but will appear after the next scheduled sync. It can take up to 12 hours to see COMPASS data reflected in Procore.

##### Important

After data is synced, you can begin viewing Qualification data in Procore's Bidding when you [add bidders from the Procore Construction Network.](https://support.procore.com/# "add company")

However, if the vendor is NOT listed on the Procore Construction Network, you must first [add the vendor to your Company Directory](https://support.procore.com/# "add company")  to see Qualification data in the Bidding tool.

## Add Companies to your Directory

Companies listed in your COMPASS account are NOT automatically added to your Company Directory in Procore. You must add them manually or from the Procore Construction Network to see their Qualification data when adding bidders from your Directory.

1. Navigate to the Company level **Directory** tool.
2. Click **Add Company.**
3. ##### Limited Release

   This workflow is currently available in English in the United States and Canada. [Learn more](https://support.procore.com/faq/what-happens-when-companies-and-users-are-added-from-the-procore-construction-network-to-the-company-directory "What happens when companies and users are added from the Procore Construction Network to the Company Directory?").

   - Enter the 'Company Name' and click **Search** to search for the company in the [Procore Construction Network](https://support.procore.com/faq/what-is-the-procore-construction-network "What is the Procore Construction Network?").
   - From the search results, take one of the following actions:
     - Click **Add** next to the company you want to add to your directory.  
       *Note:* The company is added as a [connected company](../../../../../../references/construction-management/glossary-of-terms.md#Connected_Company "Glossary of Terms") and the company's name, address, website, and phone number are added to your directory. You can [update the company's information](https://support.procore.com/products/online/user-guide/company-level/directory/tutorials/edit-a-company-in-the-company-directory "Edit a Company in the Company Directory") in your directory.
     - Click **Add Company Manually** to continue adding the company.
4. Complete the form, ensuring the company name and mailing address match what is in COMPASS.
5. Click **Create**.
6. Locate the 'Entity Type' and select **EIN**.
7. Enter the EIN number next to the 'Entity Type'.
8. Click **Save**.  
   COMPASS information will sync instantly and be available in the Bidding tool.

## Update Companies in your Directory

For companies already in your Directory, COMPASS data syncs automatically when key information matches. To enable this sync, ensure the information aligns by following the steps below.

1. Navigate to the Company level ****Directory****tool.
2. Click the ****Companies**** tab.
3. Next to the company, click **Edit**.
4. Ensure the following fields match what is in COMPASS:
   1. Company Name
   2. Address
   3. Locate the 'Entity Type' and select **EIN**.
      1. Enter the **EIN number** next to the 'Entity Type'.
5. Click **Save**.  
   COMPASS information will sync instantly and be available in the Bidding tool.

##### Note

If you do not have the EIN number, you can follow these same steps, but update the Company Name and Address to match exactly what is in COMPASS. However, this method takes at least three days to sync and process addresses.

## Add from Directory

1. Navigate to the project's **Bidding** tool.
2. Open the bid package.
3. Across from the bid form you want to add bidders to, click the **plus** ![icon-plus-2.png](https://support.procore.com/@api/deki/files/341368/icon-plus-2.png?revision=1&size=bestfit&width=18&height=19) icon and select **Directory**.  
   ![add-bidders-plus.png](https://support.procore.com/@api/deki/files/513958/add-bidders-plus.png?revision=1)  
   OR  
   Click the **bid form name.**
   1. Click the **Bidders** tab.
   2. Click **Add Bidders** and select **Directory**.
4. *Optional:* [Search for and Filter Companies to Add to a Bid Form](search-for-and-filter-companies-to-add-to-a-bid-form.md#Filter_Companies_in_the_Directory "Search for and Filter Companies to Add to a Bid Form").
5. *Optional:* Click the Company name to view it's details.

   ##### Note

   Depending on the company information, the following information is available:

   - ****Company Information**** from your directory is available by default.
   - ****Overview**** and ****Procore Activity**** tabs are available if the bidding company is a [connected company](../../../../../../references/construction-management/glossary-of-terms.md#Connected_Company "Glossary of Terms"), or you have the company's EIN or valid address in your company's Direcotry.  
     **Note:**The Overview tab replaces the default company information section.
   - ****Qualifications**** are available if you use the COMPASS integration. See [About the Bidding + COMPASS Integration](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-the-bidding-compass-integration "About the Bidding + COMPASS Integration").
6. Mark the checkbox for the companies you want to add to the bid form.
7. Decide when to invite bidders:
   - To add the bidders without sending an invitation, click **Add Bidders**.
   - To invite the bidders now:
     1. Click **Send Invitations**.
     2. Click **Send** to confirm sending the bid invitation email.

## Add from Procore Construction Network

##### Limited Release

This feature is currently available in English for customers in the United States and Canada.

1. Navigate to the project's **Bidding** tool.
2. Open the bid package.
3. Across from the bid form you want to add bidders to, click the **plus** ![icon-plus-2.png](https://support.procore.com/@api/deki/files/341368/icon-plus-2.png?revision=1&size=bestfit&width=18&height=19) icon and select **Construction Network**.  
   ![]()OR  
   Click the **bid form name.**
   1. Click the **Bidders** tab.
   2. Click **Add Bidders** and select **Directory**.
4. *Optional:* [Search for and Filter Companies to Add to a Bid Form](search-for-and-filter-companies-to-add-to-a-bid-form.md#Filter_Companies_in_the_Construction_Network "Search for and Filter Companies to Add to a Bid Form").
5. *Optional:* Click the Company name to view it's details.
6. Mark the checkbox for the companies you want to add to the bid form.
7. Decide when to invite bidders:
   - To add the bidders without sending an invitation, click **Add Bidders**.
   - To invite the bidders now:
     1. Click **Send Invitations**.
     2. Click **Send** to confirm sending the bid invitation email.

##### Note

Companies added from the Procore Construction Network are automatically added to your Directory. See [What happens when companies and users are added from the Procore Construction Network to the Company Directory?](https://support.procore.com/faq/what-happens-when-companies-and-users-are-added-from-the-procore-construction-network-to-the-company-directory "What happens when companies and users are added from the Procore Construction Network to the Company Directory?")

## Add from Single Contractor View

##### Beta

- **Single Contractor View**can be [enabled by an administrator in Procore Explore](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/manage-features-with-procore-explore "Manage Features With Procore Explore").
- This feature is currently available in English for customers using the [Bid Management Enhanced Experience](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-bid-management-enhanced-experience "About Bid Management Enhanced Experience").

1. Navigate to the project's **Bidding** tool.
2. Open the bid package.
3. Across from the bid form you want to add bidders to, click the **plus** ![icon-plus-2.png](https://support.procore.com/@api/deki/files/341368/icon-plus-2.png?revision=1&size=bestfit&width=18&height=19) icon.  
   ![single contractor plus.png](https://support.procore.com/@api/deki/files/528375/single_contractor_plus.png?revision=1)  
   OR  
   Click the **bid form name.**
   1. Click the **Bidders** tab.
   2. Click **Add Bidders**.
4. *Optional:* [Search for and Filter Companies to Add to a Bid Form](search-for-and-filter-companies-to-add-to-a-bid-form.md#Filter_Companies_in_the_Directory "Search for and Filter Companies to Add to a Bid Form").
5. *Optional:* Click the Company name to view it's details.

   ##### Note

   Depending on the company information, the following information is available:

   - ****Company Information**** from your directory is available by default.
   - ****Overview**** and ****Procore Activity**** tabs are available if the bidding company is a [connected company](../../../../../../references/construction-management/glossary-of-terms.md#Connected_Company "Glossary of Terms"), or you have the company's EIN or valid address in your company's Direcotry.  
     **Note:**The Overview tab replaces the default company information section.
   - ****Qualifications**** are available if you use the COMPASS integration. See [About the Bidding + COMPASS Integration](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-the-bidding-compass-integration "About the Bidding + COMPASS Integration").
6. Mark the checkbox for the companies you want to add to the bid form.
7. Decide when to invite bidders:
   - To add the bidders without sending an invitation, click **Add Bidders**.
   - To invite the bidders now:
     1. Click **Send Invitations**.
     2. Click **Send** to confirm sending the bid invitation email.

## View COMPASS when Leveling Bids

1. Navigate to the project's **Bidding** tool.
2. Click **View** or the **name** of the relevant bid package.  
   *Note:* You can also click the name of the bid package.
3. Click the**bid form name**.
4. Click the **Bid Leveling** tab.
5. Click the **Leveled Bids** view.
6. Take any of the following actions:
   - **Alternates**
     1. Expand the 'Alternates' section.
     2. Move the **toggles** ![icon-toggle-on.png](https://support.procore.com/@api/deki/files/93011/icon-toggle-on.png?revision=1&size=bestfit&width=25&height=25) ON or ![icon-toggle-off.png](https://support.procore.com/@api/deki/files/93010/icon-toggle-off.png?revision=1&size=bestfit&width=25&height=25) OFF to show or hide alternates.
   - **Bid Summary**
     1. View how many items are excluded or missing from the submitted bid.
   - **Configure Columns for Submitted Bids**
     1. Click the **table filter** ![icon-ag-grid-table-filter-menu.png](https://support.procore.com/@api/deki/files/233087/icon-ag-grid-table-filter-menu.png?revision=3&size=bestfit&width=18&height=18) icon.
     2. Move the **toggles** ![icon-toggle-on.png](https://support.procore.com/@api/deki/files/93011/icon-toggle-on.png?revision=1&size=bestfit&width=25&height=25) ON or ![icon-toggle-off.png](https://support.procore.com/@api/deki/files/93010/icon-toggle-off.png?revision=1&size=bestfit&width=25&height=25) OFF to show or hide a bid.
   - **Edit Line Items.**
     1. Double click the **field** in the bid you want to edit.  
        *Note*: Fields that have been edited will have a triangle in the cell.
     2. If available, select **Include** or **Exclude**.  
        *Note:* This is based on the 'Response Field Type' in the bid form.
     3. Enter the new **amount**.
     4. *Optional:* Enter a **note**.
     5. *Optional:* Select a **Line Item Color**.
     6. Click **Add**.
     7. *Optional:* Click **View Activity** to view change history for the field,
   - **Private Line Items**
     1. Locate the 'Private Line Items' section.
     2. Click **+** icon.
     3. Click **Add Line Item** and select **Cost Code** or **Plain Text**.
     4. Enter the item's **Cost Code** or ****Name****, ****Description****, and select the ****Response Field Type****.
     5. *Optional:* To create a section for your line items, click ****Add Section**** and enter the section name.
     6. *Optional:*Repeat the steps above to add additional sections and line items.
     7. *Optional*: To delete a section or line item, click the **vertical ellipses**![icon-ellipsis-vertical.png](https://support.procore.com/@api/deki/files/158014/icon-ellipsis-vertical.png?revision=2&size=bestfit&width=16&height=16)and select **Delete Section** or **Delete Line Item.** Click **Delete** to confirm.
     8. Click **Save**.
     9. Click into any of the fields for your private line items to enter included or excluded quantities. See the 'Edit Line Items' section above for more information.
   - **Sort Bids**
     1. Click **Sort** to re-sort bids from lowest to highest.  
        *Note:* Bids are automatically sorted from lowest to highest from left to right. Use this button to re-sort after editing a bid.
7. *Optional:* [Export Bid Leveling Data](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/export-leveled-bids "Export Leveled Bids").