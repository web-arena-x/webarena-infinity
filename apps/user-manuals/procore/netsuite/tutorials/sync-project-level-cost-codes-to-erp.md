# Sync Project Level WBS Codes to NetSuiteÂ®

Source: https://v2.support.procore.com/product-manuals/netsuite/tutorials/sync-project-level-cost-codes-to-erp

---

## Background

Company level WBS codes are pulled down onto a project in Procore. Each full WBS code on the project (cost code, cost type, custom segment) will be synced to NetSuiteÂ® as an **Item**. The syncing of new WBS codes at the project level code is triggered in the following ways:

- The WBS Code is used on a Subcontractor Invoice that is synced to NetSuiteÂ®.
- The WBS Code is added to the Procore Budget and a manual Cost Code Sync is run.

##### Â Note

Each project level WBS Code only needs to be synced once to create the NetSuiteÂ® Item. The NetSuiteÂ® Item will be a concatenation of the Procore project number + the WBS code. Once it is created via one of the above workflows, it is synced.

##### Â Important

By design, the integration workflow for WBS Codes will sync and create the NetSuiteÂ® Item during Subcontractor Invoice export automaticallyif it has not already been synced previously. Generally, the only time you need to run a manual Cost Code sync is if you need the NetSuiteÂ® Item before a Subcontractor Invoice is exported for that WBS Code for the purposes of assigning Direct Cost transactions in NetSuiteÂ®.