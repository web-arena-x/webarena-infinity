# Create an hh2 Service Account in Sage 100 ContractorÂ®

Source: https://v2.support.procore.com/product-manuals/sage-100/tutorials/create-an-hh2-service-account-in-sage-100

---

## Background

A *service account* is a special user account that is created in the Sage 100 ContractorÂ® system. This account is required by the hh2 Cloud Service ([www.hh2.com](http://www.hh2.com)) to give the hh2 synchronization client the ability to sync the data in your Sage 100 ContractorÂ® database with the hh2 Cloud Service. This account also permits the hh2 Cloud Service to sync the hh2 data with Procore.

## Things to Consider

- **Required User Permission**:

  - Permission to create new user accounts in your company's Sage 100 ContractorÂ® database.
- **Additional Information**:

  - The service account must be granted *Application Admin* and *Security Admin* access permission to your Windows-based Sage 100 ContractorÂ® server.
  - The Sage 100 ContractorÂ® server should be running on a Windows server or standalone computer, and NOT a workstation.
  - For best results, perform these steps either at the server or from a location with remote access to your server.

## Steps

1. Log in to your Sage 100 ContractorÂ® server.
2. Create a new user account to act as the "service account" (e.g., create an account named 'hh2Admin'). For instructions, refer to the User Guide for your version of Sage 100 ContractorÂ®.   
   ***Important!*** Do NOT use a Windows user account.
3. Configure the new service account as follows:

   - Add the account to the *Application Admin* and *Security Admin* groups.
   - Mark the âPassword Never Expiresâ option for the account's password.   
     *Note*: Next, your Procore point of contact  will work with you to install and configure the hh2 synchronization client on the system running your Sage 100 ContractorÂ® database.