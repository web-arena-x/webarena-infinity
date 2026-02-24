# Link ERP Companies to Procore Companies

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/link-erp-companies-to-procore-companies

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

When your Procore account is integrated with an ERP system, and that integration supports a connection between companies in the ERP system and 'Companies' in the Procore directory, you should link those records for consistency, data integrity, and functional requirements of other elements of your integration.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permissions on the company's ERP Integrations tool.
- **Prerequisites**:

 - Complete the steps in [Consolidate Duplicate Companies in the Company Directory](/product-manuals/erp-integrations-company/tutorials/consolidate-duplicate-companies-in-the-company-directory).
- **Considerations:**

 - You only need to link active ERP companies that will be used in new projects that will be managed in Procore. Inactive ERP companies should be archived in the Company level ERP Integration tool.
 - Once a company in your ERP system is linked to a company in Procore, any changes to address information may not be synced between the two systems. Address changes may be made automatically, dependent on your ERP Integration, or may need to be made manually in both Procore and your ERP system.

## Steps

1. Navigate to the company's **ERP Integrations** tool.
2. Click the **Companies** subtab.
3. Mark the "Show suggested Procore matches" filter checkbox to quickly find ERP companies that have an exact name match with an existing company in your Procore Directory.
4. If all the suggested matches look correct, click the **Link All** button. 
    OR If a suggested match is incorrect, ignore the match by temporarily moving it to the "Archived" filter.
   *Note*: *The search filter is based upon the Name field and is not case-sensitive.* OR Optional: If the ERP company is not going to be used in any new projects, click the 'Archive' icon.
5. After all of the suggested matches are linked, remove the mark from the **Show Suggested Matches in Procore** checkbox.
6. Now that youâve linked all the easy matches, match an ERP company with an existing company in your Procore Directory that did NOT show up as a suggested match in the previous step. For example, if a company in Procore is spelled with â&â instead of âandâ, that can cause the existing company to not appear as a âsuggested match.â
7. Find an ERP company that you want to link and click **Link to Existing Company**. Type the name of the company. If a similar entry exists, it should appear in the list. When you find a correct match, select it and click **Link**.