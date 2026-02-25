# Perform an On-Demand Sync with Sage 300 CREÂ®

Source: https://v2.support.procore.com/product-manuals/sage-300-cre/tutorials/perform-an-on-demand-sync-with-sage-300-cre

---

## Background

To keep the data in your Sage 300 CREÂ® and Procore systems synchronized, you can perform an on-demand sync. An *on-demand sync* is a manual process that ensures the data in your company's Sage 300 CREÂ® database remains concurrent with your company's data in Procore.

To perform an on-demand sync, the [Sage 300 CREÂ® Connector](https://marketplace.procore.com/apps/procore-built-sage-300-cre-connector) requires your company to have an active account with the hh2 cloud service ([www.hh2.com](http://www.hh2.com)). In addition, an hh2 synchronization client must be installed on your Sage 300 CREÂ® server. Both of these steps are completed during the setup process with the help of your Procore point of contact .

After the systems are configured, users with the appropriate permissions can perform an on-demand sync by completing two steps:

- Step 1: Sync Your Sage 300 CRE Data with hh2
- Step 2: Refresh/Sync Your hh2 Data with Procore

It is important to note that when you add data to Sage 300 CREÂ®, Procore can only retrieve that data from the hh2 cloud service. That means, it is imperative that you always ensure that the data in Sage 300 CREÂ® server is synced with the data in hh2 before you attempt to refresh/sync your hh2 data to Procore. Sage 300 CREÂ® is configured to auto-sync with hh2. However, if you do not want to wait for the auto-sync to occur, you can manually perform an auto-sync using the steps described below (see Step 1: Sync Your Sage 300 Data with hh2. Once that step is complete, you can proceed with Step 2: Refresh/Sync Your hh2 Data with Procore.

## Things to Consider

- **Required User Permissions**:

  - *To perform Step 1: Sync Your Sage 300 CRE Data with hh2,* you must know the login credentials for your company's hh2 cloud service account.
  - *To perform Step 2: Refresh/Sync Your hh2 Data with Procore*, your Procore user account must have 'Standard' or 'Admin' level permission to the ERP Integrations tool.
- **Additional Information**:

  - An on-demand sync can be performed using a button on the following tabs in the ERP Integrations tool:

    - Standard Cost Codes & Cost Types
    - Vendors
    - Jobs
    - Sub Jobs
    - Prime Contracts
    - Job Costs
  - An on-demand sync is NOT available on the Budgets, Commitments, Commitment Change Orders, or Prime Contract Change Orders tabs. Instead, this data must be sent to the ERP Integrations tool to be accepted or rejected for export to Sage 300 CREÂ® by an 

    In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

    Accounting Approver.

## Steps

***Important!*** When performing an on-demand sync, always complete Step 1: Sync Your Sage 300 CREÂ® with hh2 before proceeding with Step 2: Refresh/Sync Your hh2 Data with Procore.

### Step 1: Sync Your Sage 300 CRE Data with hh2

You must have access to your company's hh2 credentials to perform the steps below.

1. Log in to your company's hh2 account.  
    (e.g., <https://example.hh2.com>, where 'example' is your company's unique identifier)
2. In the left pane under **Quick Menu**, click **Accounting Sync**.
3. Click **Settings** to adjust the sync settings between Sage 300 CREÂ® and hh2.  
    This reveals the Sync Filters page.
4. In the Sync Filters page, do the following:

   - **Date Range**. Specify a narrow date range for performing faster sync actions (e.g., Today, Past Week, Past Month, Past Year, or All Changes).
   - **Sync Depth.** Choose the desired type of sync: *Shallow Sync* or *Deep Sync*.  
     *Note*: Typically, you will choose *Shallow Sync*. To learn about each option, information is available on the Sync Filters page.
   - When finished click **Apply Settings.**
5. Click **Start Sync**.
6. Continue with Step 2: Refresh/Sync Your hh2 Data with Procore.

### Step 2: Refresh/Sync Your hh2 Data with Procore

1. Ensure that Step 1: Sync Your Sage 300 CREÂ® Data with hh2 has successfully completed.
2. Log in to the Procore web application.   
   *Note*: Your Procore user account must have 'Standard' or 'Admin' level permission to the ERP Integrations tool.
3. Navigate to your company's **ERP Integrations** tool.
4. Click one (1) of the following tabs:

   - **Std. Cost Codes & Cost Types**
   - **Vendors**
   - **Jobs**
   - **Sub Jobs**
   - **Jobs Costs**
   - **Prime Contracts**  
     *Note*: An on-demand sync is NOT available on the Budgets, Commitments, Commitment Change Orders, or Prime Contract Change Orders tabs. Instead, this data must be sent to the ERP Integrations tool to be accepted or rejected for export to Sage 300 CREÂ® by an 

     In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

     Accounting Approver.
5. Depending on the selected tab, click the appropriate button to initiate the on-demand sync:

   - In the 'Std. Cost Codes & Categories' tab, click **Sync Cost Codes & Cost Types**.
   - In the 'Vendors' tab, click **Refresh Vendor List**.
   - In the 'Jobs' tab, click **Refresh Job List**.
   - In the 'Sub Jobs' tab, click **Refresh Job List**.
   - In the 'Prime Contracts' tab, click **Refresh Prime Contract List**.
   - In the 'Job Costs ' tab, click **Sync Job Costs**.   
     *Note*: You must sync/refresh the data for each individual tab.
6. After the on-demand sync process is complete, ensure that the data in Procore and Sage 300 CREÂ® match.