# Delete a Custom Trade

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/delete-a-custom-trade

---

## Background

If you want to delete one or more of the custom trades that you added to your company's Procore account, use the steps below.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:** Trades interact with these Procore tools:

 - **Bidding** **:** If you've enabled the Bidding tool on a project, you can set trade information for a vendor in the Directory tool. See [Set Bidder Information at the Company Level](/product-manuals/directory-company/tutorials/set-bidder-information-company-level).
 - **Daily Log** **:**

    - Daily Construction Report Log. See [Daily Construction Report Log](/product-manuals/daily-log-project/tutorials/create-daily-construction-report-entries).
    - Manpower Log. See [Manpower Log](/product-manuals/daily-log-project/tutorials/create-manpower-entries).
 - **Directory:** After a trade is deleted, the selection will no longer be visible in the Trade list in the Filter Records By area. See [Search and Filter the Company Directory](/product-manuals/directory-company/tutorials/search-and-filter-the-company-directory) and [Search and Filter the Project Directory](/product-manuals/directory-project/tutorials/search-and-filter-the-project-directory).
 - **Inspections:** Inspection Template. See [Create a Company Level Inspection Template](/product-manuals/inspections-company/tutorials/create-a-company-level-inspection-template).
 - **Observations:** Observation. See [Create an Observation](/product-manuals/observations-project/tutorials/create-an-observation) and [Edit an Observation](/product-manuals/observations-project/tutorials/edit-an-observation).
 - **Photos:** You can set trade information for photos from the photos viewer. See [Set A Photo Trade](/product-manuals/photos-project/tutorials/set-photo-trade).
 - **Punch List:** Punch List Items. See [Create a Punch List Item](/product-manuals/punch-list-project/tutorials/create-a-punch-list-item) and [Edit a Punch List Item](/product-manuals/punch-list-project/tutorials/edit-a-punch-list-item).

*Note*: You cannot delete a trade when it is tied to a Procore object that was created in one of the above Company or Project level tools. You must first disassociate the trade assignment with that object.

## Steps

1. Navigate to the company's **Admin** tool.
2. Under 'Company Settings', click **Trades**.
3. Under the 'Trades' list, click the **delete** icon across from the trade you want to remove. 
   *Note*: You cannot delete a trade from the Company level Admin's tools Trade Configuration list if it is tied to a Procore object in one of the Company or Project level tools. For example, if the trade has been associated with an inspection template, you cannot delete that trade.