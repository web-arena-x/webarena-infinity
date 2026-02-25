# Merge Companies

Source: https://v2.support.procore.com/product-manuals/directory-company/tutorials/merge-companies

---

## Background

If you have duplicate companies listed in the Company level Directory, you can merge the company records into a single record. When merging companies, you are asked to select a 'primary' company in which to merge the other company records. Upon merging, all items and users associated with the merged companies will be associated with the primary company.

## Things to Consider

##### Â Warning

Merging companies is an action that **cannot be reversed**. All information not specified to be kept will be permanently removed and is NOT recoverable.

- [Required User Permissions](/product-manuals/directory-company/permissions)
- The primary company will inherit all associated users as well as the following information from the companies being merged (fields not listed will remain the same for the primary company):

 - Bid comments and star ratings
 - Cost codes
 - Insurance
 - Trades
 - Project history
- The following companies cannot be merged:

 - Two [connected companies](/faq-what-happens-when-companies-and-users-are-added-from-the-procore-construction-network-to-the-directory).
 - Two companies currently listed on the same bid package or bid form.
 - Companies with the 'Lock Schedule of Values and Contract Company' setting is enabled, when the primary company is linked to an approved Prime Contract or Commitment. If you need to merge the company, the setting can be turned OFF while merging and back ON once the merge is complete. See [Update the Tool Settings for Contracts](/product-manuals/admin-company/tutorials/update-the-tool-settings-for-contracts).
- When merging a local company and a 

 A *connected company* is a business or organization that is listed on the [Procore Construction Network](/faq-what-is-the-procore-construction-network) and added as a company in your Company level Directory tool. While you can edit and maintain some of the businessâs information in your Company level Directory, the business also has a public profile with information that they maintain.

 Connected Company, the connected company must be be the 'primary' company. See [What happens when companies and users are added from the Procore Construction Network to the Company Directory?](/faq-what-happens-when-companies-and-users-are-added-from-the-procore-construction-network-to-the-directory)
- Any data that is NOT selected when merging will be permanently removed. However, if merging with a connected company, you can still view all the connected company's information on their [Public Profile](/product-manuals/directory-company/tutorials/view-company-details-in-the-company-level-directory-tool).
- When a merge occurs, changes are tracked in the Change History of the primary company and in the [Merge History](/product-manuals/directory-company/tutorials/view-merge-company-history).
- For companies using the ERP Integrations tool: **Show/Hide**

 - Duplicate vendor/company must be consolidated (see [Consolidate Duplicate Vendors in the Company Directory](https://support.procore.com/tc/procore/Legacy/ERP%5FArchives/QuickBooks%5FLegacy%5FTutorials/consolidate-duplicate-vendors-in-the-company-directory)) or merged in Procore before your data is synced with an ERP-integrated system (e.g., Sage 300 CRE or QuickBooks).
 - If your company has enabled the ERP Integrations tool for a third-party accounting system, the Company Merge subtab will prompt you to choose a Sage ID if one or more of the vendors selected for merging are synced with Sage. Merged vendors which are not selected as the primary vendor will be unlinked and archived in the ERP Vendors subtab.   
    *Note*: For example, if Vendor A and Vendor B are both linked with Sage when they are merged, and Vendor A is chosen as the primary vendor, Vendor B will then be unlinked from Sage and archived in the ERP Vendors subtab.

## Steps

1. Navigate to the Company level **Directory** tool.
2. Click the **Configure Settings** icon.
3. Click **Merge Companies**.
4. Review the instructions.
5. Click **Begin Merging**.
6. Identify the companies you want to merge.

   - *To change the sort order of the table*, click a column header. The default sort order is in ascending alphabetical order by Company Name.
   - *To search for specific companies,* enter their name(s) in the 'Search for Companies' field and click **Search**.
   - *To filter the list to show 'exact matches only'*, select one of the following options in the 'Exact Match' drop-down menu:\* Company Name\* Address\* Phone\* Fax
7. Mark the checkboxes for the companies you want to merge.
8. Click **Next Step**.
9. Select the 'Primary' company that the other record(s) will be merged into.

   ##### Â Note

   - If merging a [connected company](/glossary-of-terms), the connected company must be the primary company.
   - If merging a connected company with a company linked to your third-party ERP system, the connected company still must be the primary company. However, the ERP Vendor ID is maintained and is added to the merged record. Other Procore data, such as Commitments, attributed with the original ERP vendor record is merged as well.
   - If merging a company that is linked to your third-party ERP system, the link for the primary vendor will be saved and the other vendor(s) will be unlinked from the ERP system and then archived in the 'Vendors' tab of the ERP Integrations tool.

   ##### 

   - Vendor A and Vendor B are both linked with an ERP system and you want to merge the records.
   - If you specify Vendor A as the primary company, the information from Vendor B will be moved into Vendor A.
   - Then the Vendor B record will be unlinked from ERP and archived in the Vendors subtab of the ERP Integrations tool.
   - The record for Vendor B will also be permanently removed from the Company Directory