# Perform an On-Demand Sync with Sage 100 ContractorÂ®

Source: https://v2.support.procore.com/product-manuals/sage-100/tutorials/perform-an-on-demand-sync-with-sage-100

---

## Background

To keep the data in your Sage 100 ContractorÂ® and Procore systems synchronized, you can perform an on-demand sync. An *on-demand sync* is a manual process that ensures the data in your company's Sage 100 ContractorÂ® database remains concurrent with your company's data in Procore. To perform an on-demand sync, the Sage 100 ContractorÂ® Connector requires your company to have an active account with the hh2 cloud service ([www.hh2.com](http://www.hh2.com)). In addition, an hh2 synchronization client must be installed on your Sage 100 ContractorÂ® server. Both of these steps are completed during the setup process with the help of your Procore point of contact .

After the systems are configured, users with the appropriate permissions can perform an on-demand sync by completing two steps:

- Step 1: Sync Your Sage 100 ContractorÂ® Data with hh2
- Step 2: Refresh/Sync Your hh2 Data with Procore

It is important to note that when you add data to Sage 100 ContractorÂ®, Procore can only retrieve that data from the hh2 cloud service. That means, you must always ensure that the data in the Sage 100 ContractorÂ® server is synced with the data in hh2 before you attempt to refresh/sync your hh2 data to Procore. Sage 100 ContractorÂ® is configured to auto-sync with hh2. However, if you do not want to wait for the auto-sync to occur, you can manually perform an auto-sync using the steps described below (see Step 1: Sync Your Sage 100 ContractorÂ® Data with hh2. Once that step is complete, you can proceed with Step 2: Refresh/Sync Your hh2 Data with Procore.

## Things to Consider

- **Required User Permissions**:

  - *To perform Step 1: Sync Your* *Sage 100 ContractorÂ®* *Data with hh**2**,* you must know the login credentials for your company's *hh**2* cloud service account.
  - *To perform Step 2: Refresh/Sync Your hh**2* *Data with Procore*, your Procore user account must have 'Standard' or 'Admin' level permission to the ERP Integrations tool.

## Steps

***Important!*** When performing an on-demand sync, always complete Step 1: Sync Your Sage 100 ContractorÂ® Data with hh2 before proceeding with Step 2: Refresh/Sync Your hh2 Data with Procore.

### Step 1: Sync Your Sage 100 ContractorÂ® Data with hh2

You must have access to your company's hh2 credentials to perform the steps below.

1. Log in to your company's hh2 account.  
   (e.g., <https://example.hh2.com>, where 'example' is your company's unique identifier)
2. In the left pane under **Quick Menu**, click **Accounting Sync**.
3. Click **Settings** to adjust the sync settings between Sage and hh2.  
   This reveals the Sync Filters page.
4. In the Sync Filters page, do the following:

   - **Date Range**. Specify a narrow date range for performing faster sync actions (e.g., Today, Past Week, Past Month, Past Year, or All Changes).
   - **Sync Depth.** Choose the desired type of sync: *Shallow Sync* or *Deep Sync*.  
     *Note*: Typically, you will choose *Shallow Sync*. To learn about each option, information is available on the Sync Filters page.
   - When finished, click **Apply Settings.**
5. Click **Start Sync**.
6. Continue with Step 2: Refresh/Sync Your hh2 Data with Procore.

### Step 2: Refresh/Sync Your hh2 Data with Procore

1. Ensure that Step 1: Sync Your Sage 100 ContractorÂ® Data with hh2 has been completed.
2. Log in to the Procore web application (see [Log in to Procore Web](/product-manuals/directory-company/tutorials/log-in-to-procore-web)).  
   *Note*: Your Procore user account must have 'Standard' or 'Admin' level permission to the ERP Integrations tool.
3. Navigate to your company's **ERP Integrations** tool.
4. Click one of the following subtabs:

   - **Std. Cost Codes & Categories**
   - **Vendors**
   - **Jobs**
   - **Subjobs**
   - **Jobs Costs**  
     *Note*: You will not be permitted to perform an on-demand sync from the Budgets, Commitments, or Change Orders subtabs. Instead, this data must be sent to the ERP Integrations tool to be accepted or rejected for export to Sage 100 ContractorÂ® by an 

     In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

     Accounting Approver.
5. Depending on the selected subtab, click the appropriate button to initiate the on-demand sync:

   - In the 'Std. Cost Codes & Categories' subtab, click **Sync Cost Codes & Categories**.
   - In the 'Vendors' subtab, click **Refresh Vendor List**.
   - In the 'Jobs' subtab, click **Refresh Job List**.
   - In the 'Sub Jobs' subtab, click **Refresh Job List**.
   - In the 'Job Costs 'tab, click **Sync Job Costs**.   
     *Note*: You must sync/refresh the data for each subtab individually.
6. After the on-demand sync process is complete, ensure that the data in Procore and Sage 100 ContractorÂ® matches.