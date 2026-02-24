# How do I add missing cost codes so I can migrate projects to the new bid management experience? - Procore

Source: https://support.procore.com/faq/how-do-i-add-missing-cost-codes-so-i-can-migrate-projects-to-the-new-bid-management-experience

---

## Background

If a Procore project has any bid packages with line items that are missing cost codes, the project cannot be updated to Bid Management Enhanced Experience. When you begin the process of joining the beta to migrate to the new experience, you will see an error message that you need to update cost codes.

This may be a result of the following situations:

- A bidder submitted a bid, but did not select a cost code for one or more line items in the Planroom tool.
- A bid solicitor deleted a cost code that was previously used in a bid.

## Answer

#### From the Company Level

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Bidding**.
3. Click **Update**in the 'Introducing Bid Management Enhanced Experience' banner.  
   ![admin-bidding-banner.png](https://support.procore.com/@api/deki/files/404117/admin-bidding-banner.png?revision=1)
4. If any project is missing cost codes for bid line items, you will see an 'Action Required to Update Projects' error message with a list of affected projects. Open each of the affected projects and choose the automatic or manual option for each project.

#### From the Project Level

1. Navigate to the project's **Bidding** tool.
2. In the 'Introducing Bid Management Enhanced Experience' banner, click Update.  
     
   ![bidding-banner.png](https://support.procore.com/@api/deki/files/404116/bidding-banner.png?revision=1)
3. If the project is missing cost codes for bid line items, you will see an 'Action Required to Bid Packages' error message.  
   Choose whether you want to automatically assign one cost code to all affected line items, or add them all manually:
   - **Automatic**:
     1. Click the **Select a Cost Code** drop-down menu and select the cost code that you want to add.  
        ![bidding-auto-add-cost-code.png](https://support.procore.com/@api/deki/files/364309/bidding-auto-add-cost-code.png?revision=2)
     2. Click **Next**.  
        Procore will automatically add the missing cost codes for all affected bid packages, and you will be taken to the 'Accept Terms' page for the beta.
   - **Manual**:
     1. We recommend opening the Bidding tool in a new tab so that you can refer back to the list of affected bid packages and companies.
     2. Click **View** on an affected bid package.
     3. On the Bidders tab, click **View** on the company that is missing cost codes.
     4. In the Bid Sheet section, select a cost code to apply to the line item.  
        ![bidding-cost-code.png](https://support.procore.com/@api/deki/files/364307/bidding-cost-code.png?revision=1)
     5. Repeat this process for each affected bid package. After all missing cost codes have been added and you click **Update** in the banner again, you will be taken to an 'Update All Bid Packages' message.

#### See Also

- [How do I update to the new bid management experience?](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/update-to-the-new-bid-management-experience "How do I opt in to the new Bidding experience?")
- [What happens when I update a project to the new bid management experience?](https://support.procore.com/faq/what-happens-when-i-update-a-project-to-the-new-bid-management-experience "What happens when I update a project to the new bid management experience?")
- [About Bid Management Enhanced Experience](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-bid-management-enhanced-experience "About Bid Management 2.0 (Beta)")