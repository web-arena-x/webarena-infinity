# Remove Duplicate Companies from the Company Directory

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/remove-duplicate-companies-from-the-company-directory

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

It is possible to have duplicate company records in your company's Directory. To ensure correct and complete company information, you can consolidate duplicate company records into a single record that can be linked to a company in your ERP system. Each ERP company can only link to a single company record in your Procore Directory.

## Things to Consider

- **User Permissions**

 - 'Admin' level permissions on the Company level Directory tool.
- **Additional Information**

 - You can only manually consolidate companies if there are no commitments that are tied to the specific company entry. Once a commitment is tied to a company, the entry must remain active in order to maintain an accurate information. In such cases, the only option is to merge the duplicate company entries.

## Steps

There are two different ways to remove duplicate entries in your Company level Directory.

- Merge Duplicate Company Entries
- Manually Consolidate Duplicate Company Entries

#### Merge Duplicate Company Entries

*Recommended if there are several instances of duplicate companies.*

1. See [Merge Companies](/product-manuals/directory-company/tutorials/merge-companies).

#### Manually Consolidate Duplicate Company Entries

*Recommended if there is only one or a few companies to merge.*

1. Move users from the company entry that you want to deprecate to the company entry that you want to keep active.
2. Change the name of the company you want to deprecate by adding an 'x' as a prefix to the name (e.g. 'X-CompanyName') to clearly note that it's an inactive company and should not be selected for use.
3. Set the company to 'Inactive'.