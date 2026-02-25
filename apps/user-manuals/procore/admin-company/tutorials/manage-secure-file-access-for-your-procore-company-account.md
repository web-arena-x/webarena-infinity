# Manage Secure File Access for Your Procore Company Account

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/manage-secure-file-access-for-your-procore-company-account

---

## Background

To protect your data, the Company Admin tool's Secure File Access feature requires users to log in to Procore before they can view files shared from Procore emails, PDF exports, or the API. Turning this setting ON is valuable for organizations with strict IT security requirements or those handling sensitive project information.

For companies with lower IT security requirements, a [Company Admin](/faq-what-is-a-company-admin) can change the setting to allow anyone with the link to access a file without logging in.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information**:

 - This setting is applied at a company level, it cannot be configured for projects.
 - By default, Procore requires users to log in before they can see shared documents. Disabling this feature lowers your company's document security and should only be done if your company's policies permit it.
 - To learn how Procore customer information is stored, see [Where and how does Procore store customer information?](/faq-where-and-how-does-procore-store-customer-information)

## Steps

1. Navigate to the Company level Admin tool.
2. Under Company Settings, click Security Settings.
3. Click the Document Security tab.
4. Locate the Default Login Requirement card. By default, the Secure File Access setting is enabled on all new Procore company accounts, requiring users to log in before accessing shared documents outside of Procore on all projects.
5. *(Optional)* If your company has granted you the authority to change the default setting, proceed with the next step.

   ##### Â Warning: YOU are about to modify a critical security setting. Proceed with Caution.

   Disabling the Secure File Access feature may impact your company's data security. Before making any changes, consider these risks:

   - **Uncontrolled Document Dissemination**: Once a link is shared publicly, your company loses all control over who can view it, copy it, or share it further. You will not know who is viewing your documents, which could include unauthorized third parties.
   - **Potential Exposure of Sensitive Information**: Sensitive or proprietary information (such as bids, plans, financial data, or personal employee/client information) could be exposed to unauthorized third parties or the public.
   - **Loss of Auditing and Traceability**: Access to documents via public links is anonymous and is not tracked in Procore's audit logs. You will have no record of who has viewed potentially sensitive information.
   - **Potential for Misalignment with Agreements and Policies**: The sharing of certain types of data may conflict with existing legal agreements (e.g., Non-Disclosure Agreements) or company policies.
   - **Changes to this setting do not apply retroactively to previous files**. Any changes made to this setting are not retroactive. Disabling public links will not affect files that were previously shared.

- *(Optional)* Under **Require Users to Log in Before Accessing Shared Documents Outside of Procore**, turn the toggle **OFF**.

 ##### Example

 This shows the Secure File Access feature in the OFF position. ***Warning*****: This allows anyone with a direct link to access a shared file without logging in to Procore.**

- *(Optional)* Choose one (1) of these options only when the Secure File Access toggle is **ON**:

 - **Company Level (All Projects)**. Turn this setting ON to secure all of your projects.
 - **Selected Projects**. Turn this setting ON to secure only the selected projects.

    ##### Example

    This shows the Secure File Access feature in the ON position with the secure setting applied only to selected projects. ***Caution*****: All projects not selected here are unsecured. Anyone with a direct link can access a shared file on an unsecured project without logging in to Procore**.