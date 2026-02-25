# How to Enable the Procore Bidding + COMPASS Integration

Source: https://v2.support.procore.com/product-manuals/bidding-project/tutorials/how-to-enable-compass-integration

---

## Background

Procore customers using COMPASS **by Bespoke Metrics** can seamlessly view COMPASS qualification data and invite companies to qualify directly within the Bidding tool on a Procore project. If your company does *not* have a COMPASS account, you can still access Procore project data for companies listed in the Procore Construction Network.

This guide will provide you with information about the key features of the COMPASS integration with Procore's Bidding tool. You will also find the steps necessary to enable the COMPASS integration for your company.

### Key Features

- Search and filter bidders from the Procore Construction Networkâs view within Bid Management using the Qualification Status (Qualified, Qualified w/ Exceptions, Denied, Expired) that you assigned a vendor in COMPASS.
- Search and find bidders using business information such as Trades, Business Certifications, and Office Addresses.
- View the assigned Project and Aggregate Limits, Qualification Expiration Date, Q-Score, EMR ratings for the past three years, Annual Revenue and Average Contract Value, and the Health & Safety Contact for vendors your company has qualified within COMPASS.
- Send Invitations to Qualify to vendors through COMPASS directly from the Bidding Tool in Procore. Invitees will need to register and provide their data through COMPASS.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company Directory tool.
- **Additional Requirements:**

 - The COMPASS integration with Procore Bid Management is available for customers in the US and Canada.
 - Your company must have an active subscription to Procore Bid Management.
 - Your projects must also be upgraded to Enhanced Bidding.

## Steps

### Enable the COMPASS integration

1. Navigate to the [COMPASS integration page](https://marketplace.procore.com/apps/compass-9c106db9-b0ee-4df3-8df8-362c60fc592c) in the Procore App Marketplace.
2. **Login** to your Procore account and confirm you have selected the correct company.
3. Click **Install**.

   - You will be redirected to the Company Admin Tool Settings page for Bidding in Procore.
4. Click **Login** to COMPASS.

   - This turns on data sharing from COMPASS to Procore for your account.

### Sync COMPASS Data for Companies in Your Directory

1. Navigate to the Company level **Directory** tool.
2. Click the **Companies** tab.
3. Next to the company, click **Edit**.
4. Locate the 'Entity Type' and select **EIN**.
5. Enter the **EIN number** next to the 'Entity Type'. 
    COMPASS information will sync instantly and be available in the Bidding tool.

##### Â Note

This information can now be found [here](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/manage-the-bidding-and-compass-integration).

### To stop using the COMPASS integration:

1. Navigate to the [Company Admin Tool Settings](/product-manuals/admin-company/tutorials/configure-tool-settings-from-the-company-admin-tool) page for Bidding.
2. Click **Logout of COMPASS**.

## Common Questions

### What Data can I see on bidders with the COMPASS Integration?

When adding bidders either through the Procore Construction Network or your Directory, you can click on a company name to open a side panel and see Qualifications data on the bidder.

- The Qualifications data is divided into three categories:

 - The **Overview** tab provides general business information such as office locations, union status, business certifications, trades, and licenses. This information comes from the Procore Construction Network.
 - The **Qualifications** tab contains data that comes from the COMPASS data connection. This is data submitted by vendors once a year into COMPASS. It includes their EMR History for the last three years, Average Contract Size for the previous year, Annual Revenue Bucket for the previous year, Health and Safety Contact information, and QScore. It also contains their Qualification Status, Project and Aggregate Limit, and Qualification expiration date if available in COMPASS.\* COMPASS subscribers can also view a vendor's COMPASS project history while in the Qualifications tab of the side panel. This data includes up to five (5) current and five (5) completed projects that the vendor submitted to their COMPASS account.The following information will be available for each project where available:\* Project Name\* Subcontract Value\* Location\* (Estimated) Completion Date\* GC / Owner\* Scope of Work / CSI Code
 - The **Procore Activity** tab contains data compiled from Procore projects such as their total and active count of projects in the past three years, most common project types and the Change Order vs Contract rate in the past three years. It also includes the number of OSHA inspections and violations for the past three years, the number of mechanics liens filed by or against the company in the past three years, and number of bankruptcies filed by this company in the past three years, and the number of tax liens filed by the contractor in the past three years.
- Data from COMPASS can also be viewed in the Procore Directory by ensuring the following:

 - The company name and address in Procore match the company name and address used in the vendorâs COMPASS account. 
     OR
 - Add the EIN numbers for the vendor in your Procore Directory.

For more information about Qualification data viewable in Procore, see [Where does the 'Qualifications' data come from when searching for bidders?](/faq-where-does-the-qualifications-data-come-from-when-searching-for-bidders)

### What is the COMPASS QScore?

- The **COMPASS QScore** is COMPASSâs assessment of Subcontractor Risk based on key Business, Finance, and Health & Safety variables. A numerical score between 1.0 (Lowest Risk) and 7.9 (Highest Risk) is assigned by COMPASS to represent that risk.
- This QScore is available for all companies registered with COMPASS that have submitted their business and financial information to the COMPASS application.
- This QScore is available publicly and may be used by any user searching for bidders without the need for a subscription to COMPASS.

### What is EMR?

- EMR stands for **Experience Modification Rate**. It is a numerical representation used in the field of workers' compensation insurance. It is a factor that influences an employer's premium based on their historical workplace injury and illness claims compared to their industry average.
- The standard Experience Modification Rating is 1, which means that the business is about as safe as the average business. If the business had a few more safety incidents than most businesses in the industry, the EMR will be higher than 1.
- EMR is typically used to assess the Health & Safety risk for a vendor in the construction industry. Generally, an EMR of 1 or lower is considered good.

### What does the Change Order vs Contracts data mean?

**Change Order vs Contracts Rate** is a percentage that represents the contractor's average change in price from the original contract based on change orders. The percentage displayed in the application corresponds to all projects known to Procore that this vendor was on in the past three years.

### Can Customers without a COMPASS subscription access COMPASS data in Procore?

Yes, customers *without* a COMPASS subscription will have a slightly different experience in Procore. Users will be able to view the following *public* data on vendors when adding bidders from the Directory and from the Procore Construction Network:

#### COMPASS QScore

COMPASS provides a QScore, which is COMPASSâs assessment of Subcontractor Risk based on key Business, Finance, and Health & Safety variables. A numerical score between 1.0 (Lowest Risk) and 7.9 (Highest Risk) is assigned by COMPASS to represent that risk. This QScore is available for all companies registered with COMPASS that have submitted their business and financial information to the COMPASS application. This QScore is available publicly and may be used by any Bidding 2.0 user to search for bidders without the need for a subscription to COMPASS.

- Customers can filter vendors in the Procore Construction Network using the QScore filter.
- Customers will be able to view the QScore for vendors added from both the Procore Construction Network and their directory where available.
- The QScore is available for about 30-40k vendors in the Procore Construction Network.

#### Procore Activity

Procore Activity consists of two types of data:

- **Data from the vendorâs project history on the Procore platform:** Vendors can control visibility of this data through their Construction Network profile. If Procore Activity data is visible on the construction network, it will be visible inside Bidding. This data consists of:

 - The total and active count of projects in Procore,
 - Their most common project type in Procore,
 - The Change Order vs Contract rate for projects in the past three years.
- **Data collected from public sources:** This includes

 - The number of OSHA inspections and violations,
 - The number of mechanics liens filed by or against the vendor in the past three years,
 - Bankruptcies filed by the vendor in the past three years,
 - Tax lien data filed against the vendor in the past three years.

#### Data from the Procore Construction Network

General business information on the vendor such as their office locations, business certifications, and trades that the vendor submitted to their Procore Construction Network profile will be visible when adding vendors to a bid package either from the construction network or the companyâs directory.

### What is the difference between a claimed and an unclaimed business on the Procore Construction Network?

All businesses listed on the Procore Construction Network include relevant information about the business and the trades and services they provide.

Through Procore, you can connect directly with claimed businesses for bidding, payments, and more. Below are the main differences between a claimed and unclaimed business.

| Claimed | Unclaimed |
| --- | --- |
| - Provides business information including market sector, company type, and trades and services. - Company is active on Procore. - Can be invited to bid on projects in Procore. - Can be paid using Procore Pay. - Can invite and manage their team in Procore. - Can update their business information on the Procore Construction Network. - Can publish or unpublish their business page on the Procore Construction Network. | - Provides business information including market sector, company type, and trades and services. |