# How does Procore assign numbers to RFIs? - Procore

Source: https://support.procore.com/faq/how-does-procore-assign-numbers-to-rfis

---

## Answer

Procore assigns numbers to RFIs as follows:

- **Numbers are only assigned to RFIs when created or placed into *Open* status**. An RFI is automatically assigned a number when it is placed into the *Open* status. If you create a *Draft* RFI, it is NOT assigned a number until the [RFI Manager](../references/construction-management/glossary-of-terms.md#RFI_Manager "Glossary of Terms") (or a user with 'Admin' level permission to the RFIs tool) changes its status to *Open*. If you create an RFI in the *Open* status and then change its status to *Draft*, the number assigned while it was in the *Open* state is retained.   
  *Note*: Who can place an RFI into the 'Open' status depends upon the permission level a user has be granted on the Project level RFI tool. For details, see [What is a Draft RFI?](https://support.procore.com/faq/what-is-a-draft-rfi "What is a 'Draft' RFI?")
- **Numbers are assigned in sequential order**. The RFIs tool always assigns new numbers in sequential order (i.e., 1, 2, 3, and so on).
- **Duplicate numbers are NOT permitted**. Duplicate RFI numbers are never permitted in Procore. To learn more, see [Can I create an RFI with a duplicate number?](https://support.procore.com/faq/can-i-create-an-rfi-with-a-duplicate-number "Can I create an RFI with a duplicate number?")
- **Numbers from deleted RFIs are NOT reused**. As an example, lets assume you have created three (3) RFIs (e.g., 1, 2, and 3). If you decide to delete 2, the next RFI that you create will be 4. The system will NOT reuse the deleted RFI's number.

###### If You Want to Customize Your RFI Numbering Scheme

By default, Procore begins assigning single digit numbers to RFIs (e.g,. 1, 2, 3, and so on). However, the RFIs tool also provides your project team with the ability to create customized numbering sequences. For details, see [How do I configure a prefix and starting number for a project's RFIs?](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-a-prefix-and-starting-number-for-rfis "How do I configure a prefix and starting number for a project's RFIs?")

## See Also

- [How do I configure a prefix and starting number for a project's RFIs?](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/configure-a-prefix-and-starting-number-for-rfis "How do I configure a prefix and starting number for a project's RFIs?")
- [Can I create an RFI with a duplicate number?](https://support.procore.com/faq/can-i-create-an-rfi-with-a-duplicate-number "Can I create an RFI with a duplicate number?")
- [What is a Draft RFI?](https://support.procore.com/faq/what-is-a-draft-rfi "What is a draft RFI?")

## 

If you would like to learn more about Procore's RFI software and how it can help your business, please visit our [request for information (RFI) construction software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/rfis "https://www.procore.com/project-management/rfis").