# How are duplicate companies handled between the Directory tool and Procore Construction Network? - Procore

Source: https://support.procore.com/faq/how-are-duplicate-companies-handled-between-the-directory-tool-and-procore-construction-network

---

##### Limited Release

The [Procore Construction](https://support.procore.com/faq/what-is-the-procore-construction-network "What is the Procore Construction Network?") [Network](https://support.procore.com/faq/what-is-the-procore-construction-network "What is the Procore Construction Network?") is currently available in English in [Canada and the United States](https://support.procore.com/faq/in-what-regions-is-the-procore-construction-network-available "In what regions is the Procore Construction Network available?").

## Background

When you need to solicit bids for a project, you can use the [new Bid Management experience](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-bid-management-enhanced-experience "About Bid Management Enhanced Experience") to create a bid form to break down scope and cost information and help to standardize the responses that are received from bidders.

Once you create your bid form, you can [add companies to bid](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/add-bidders-to-a-bid-form "Add Bidders to a Bid Form") on your projects from your Company level Directory or the Procore Construction Network.  If you add bidders from the Procore Construction Network, their company and bid contacts are added to your Company level Directory as a '[connected company](../references/construction-management/glossary-of-terms.md#Connected_Company "Glossary of Terms")' and 'connected users'. See [What happens when companies and users are added from the Procore Construction Network to the Company Directory?](https://support.procore.com/faq/what-happens-when-companies-and-users-are-added-from-the-procore-construction-network-to-the-company-directory "What happens when companies and users are added from the Procore Construction Network to the Company Directory?")

While Procore can detect duplicate companies based on the Bid Contact, it is possible to end up with duplicate companies in your Directory if the Connected Company has different information on their business profile.

## Answer

Procore can detect and prevent a duplicate company being added to your Company level Directory from the Procore Construction Network if the Bid Contact's email address already exists in your Directory.

- [How Duplicates are Prevented](#How_Duplicates_are_Prevented "How are duplicate companies handled between the Directory tool and Procore Construction Network?")
- [How Duplicates Happen](#How_Duplicates_Happen "How are duplicate companies handled between the Directory tool and Procore Construction Network?")
- [How to Manage Duplicates](#How_to_Manage_Duplicates "How are duplicate companies handled between the Directory tool and Procore Construction Network?")

| | |
| --- | --- |
| How Duplicates are Prevented When adding a company from the Procore Construction Network, duplicates are prevented if:   - The company is already listed in your Company level Directory    AND - All Bid Contacts are already listed in your Company level Directory   Procore will notify you and prevent you from adding the Procore Construction Network company so as to prevent creating a duplicate company in your Directory. Tip To invite the Procore Construction Network to bid, you can remove the current Bid Contacts from company already listed in your Directory and try again. This will add a new 'Connected Company' in the Directory along with their Bid Contacts. *Note:* This will create a duplicate company. See below for how to [manage duplicates](#How_to_Manage_Duplicates "How are duplicate companies handled between the Directory tool and Procore Construction Network?"). | How Duplicates are Created When you add a company from the Procore Construction Network, a duplicate company is created if:   - The company is already listed in your Company level Directory    AND - All Bid Contacts are NOT listed in your Company level Directory   The Procore Construction Network company is added to your Company level Directory as a separate "Connected Company" with a different Bid Contact and email address. The original company record remains in your directory *unconnected*. |

### How to Manage Duplicates

You can merge the information from your local company record to the connected company record to have a single record. See [Merge Companies](https://support.procore.com/products/online/user-guide/company-level/directory/tutorials/merge-companies "Merge Companies").

See Also

- [What happens when companies and users are added from the Procore Construction Network to the Company Directory?](https://support.procore.com/faq/what-happens-when-companies-and-users-are-added-from-the-procore-construction-network-to-the-company-directory "What happens when companies and users are added from the Procore Construction Network to the Company Directory?")
- [Add Bidders to a Bid Form](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/add-bidders-to-a-bid-form "Add Bidders to a Bid Form (Beta)")
- [Merge Companies](https://support.procore.com/products/online/user-guide/company-level/directory/tutorials/merge-companies "Merge Companies")