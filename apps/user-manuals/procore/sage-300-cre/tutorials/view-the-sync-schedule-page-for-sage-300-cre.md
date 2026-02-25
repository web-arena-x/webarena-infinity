# View the Sync Schedule Page for Sage 300 CREÂ®

Source: https://v2.support.procore.com/product-manuals/sage-300-cre/tutorials/view-the-sync-schedule-page-for-sage-300-cre

---

## Background

When your company has enabled the ERP Integrations tool and configured it to work with Sage 300 CREÂ®, the sync schedule between the two systems is managed automatically by the 

The *hh**2* *synchronization client* is a third-party client application developed by hh2. When the ERP Integrations tool is enabled on a company's Procore account and the tool is configured to work with Sage 300 CREÂ®CRE, your Procore point of contact  will work with your Procore Administrator to install and configure the hh2 synchronization client on your Sage 300 CREÂ® Server. This allows data to sync between your Sage 300 CREÂ® database server and Procore.

hh2Â Synchronization Client. For most auto-syncs, data will sync from the Sage 300 CREÂ® server to the hh2 service every five (5) minutes. In addition, Procore polls the hh2 cloud service for data every 30 minutes. When Procore detects that new and/or updated data is present in the hh2 cloud, they are automatically synced to Procore. In addition, any changes from Procore are exported to hh2 and then synced to Sage 300 CREÂ®. This ensures that your data is updated frequently. If you have questions about the Auto Sync, please reach out to your Procore point of contact .

## Things to Consider

- **Required User Permission**:

  - *To view the Sync Schedule page*, 'Admin' on the ERP Integrations tool.
- **Additional Information**:

  - *If you want to manually sync the data*, see [Perform an On-Demand Sync with Sage 300 CREÂ®](/product-manuals/sage-300-cre/tutorials/perform-an-on-demand-sync-with-sage-300-cre).

## Steps

1. Navigate to the company's **ERP Integrations** tool.  
    This reveals the Sage 300 CREÂ® Integration page.
2. Click **Configure Settings**.  
    This reveals the Integration Settings page.
3. Click **Sync Schedule**.  
      
      
      
    This reveals the Sync Schedule page, where you can view a list of items that are synced between the two system. This page contains the following fields:

   - **Sync Standard and Project Cost Codes/Categories and Project Job Costs**.
   - **Refresh Sage 300 CRE Vendor List and Vendor Types**.
   - **Sync Job Costs and Refresh Sage 300 CRE Job List**.   
     *Note*: To learn more about the notification system to keep data in sync, see [How often can I sync data between Sage and Procore?](/faq-how-often-can-i-sync-data-between-sage-300-cre-and-procore)