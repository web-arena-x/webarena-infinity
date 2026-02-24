# Update to the New Bid Management Experience

Source: https://v2.support.procore.com/product-manuals/bidding-project/tutorials/update-to-the-new-bid-management-experience

---

## Background

Procore has released *Bid Management Enhanced Experience*, a streamlined experience for managing bids in the Bidding tool. This experience includes features such as bid forms, bid leveling, and an integration with the Procore Construction Network. Until the new experience is made available for all Procore accounts, you can enable it on a project-by-project basis, or for all projects in your account.

## ThingsÂ to Consider

- **Required User Permissions:**

 - To enable the experience at the Project level for a specific project, 'Admin' level permissions on the project's Bidding tool.
 - To enable the experience for all projects, 'Admin' level permissions on the company's Directory tool.

## Steps

*Note:* If you receive an error message that you need to update cost codes, see the What if I get an error message that I need to add missing cost codes? section below.

##### Â Warning

Updating projects to the new bid management experience is final. After you click 'Update', projects cannot be switched back to the legacy experience.

#### Turn On for a specific Project

1. Navigate to the project's **Bidding** tool. 
    An 'Introducing Bid Management Enhanced Experience' banner is shown at the top of the page describing the new bidding experience.
2. If one or more bids in the project have line items that are missing cost codes, you will see a message that you need to add cost codes. See What if I get an error message that I need to add missing cost codes? below.
3. Review the information on the 'Update All Bid Packages' window.
4. If you are certain you want to update to the new experience, click **Update**. 
    The project will begin updating to the new experience at midnight (12:00am) in the project's timezone. An 'Update in Progress' banner is shown within the project while the update is occurring. Avoid editing bid packages during this time to avoid any potential of data loss.

#### Turn On for All Projects

##### Â Caution

Only enable the new experience at the Company level if you are certain you want to update ALL projects on the account to the new experience. Projects cannot be switched back to the legacy experience after agreeing to update.

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Bidding**. 
    An 'Introducing Bid Management Enhanced Experience' banner is shown at the top of the page describing the new bidding experience.
3. If one or more bids in the project have line items that are missing cost codes, you will see a message that you need to add cost codes. See What if I get an error message that I need to add missing cost codes? below.
4. Review the information on the 'Update All Bid Packages' window.
5. If you are certain you want to update all projects to the new experience, click **Update**. 
    Each project will begin updating to the new experience at midnight (12:00am) in the project's timezone. An 'Update in Progress' banner is shown within the project while the update is occurring. Avoid editing bid packages during this time to avoid any potential of data loss.

### What if I get an error message that I need to add missing cost codes?

If a Procore project has any bid packages with line items that are missing cost codes, the project cannot be updated to Bid Management Enhanced Experience. When you begin the process of joining the beta to migrate to the new experience, you will see an error message that you need to update cost codes.

This may be a result of the following situations:

- A bidder submitted a bid, but did not select a cost code for one or more line items in the Planroom tool.
- A bid solicitor deleted a cost code that was previously used in a bid.

#### Steps

#### From the Company Level

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Bidding**.
3. Click **Update** in the 'Introducing Bid Management Enhanced Experience' banner.
4. If any project is missing cost codes for bid line items, you will see an 'Action Required to Update Projects' error message with a list of affected projects. Open each of the affected projects and choose the automatic or manual option for each project.

#### From the Project Level

1. Navigate to the project's **Bidding** tool.
2. In the 'Introducing Bid Management Enhanced Experience' banner, click Update.
3. If the project is missing cost codes for bid line items, you will see an 'Action Required to Bid Packages' error message. 
    Choose whether you want to automatically assign one cost code to all affected line items, or add them all manually:

   - **Automatic**:

     1. Click the **Select a Cost Code** drop-down menu and select the cost code that you want to add.
     2. Click **Next**. 
         Procore will automatically add the missing cost codes for all affected bid packages, and you will be taken to the 'Accept Terms' page for the beta.
   - **Manual**:

     1. We recommend opening the Bidding tool in a new tab so that you can refer back to the list of affected bid packages and companies.
     2. Click **View** on an affected bid package.
     3. On the Bidders tab, click **View** on the company that is missing cost codes.
     4. In the Bid Sheet section, select a cost code to apply to the line item.
     5. Repeat this process for each affected bid package. After all missing cost codes have been added and you click **Update** in the banner again, you will be taken to an 'Update All Bid Packages' message.