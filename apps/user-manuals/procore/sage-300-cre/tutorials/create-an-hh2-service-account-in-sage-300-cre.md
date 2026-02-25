# Create an hh2 Service Account in Sage 300 CREÂ®

Source: https://v2.support.procore.com/product-manuals/sage-300-cre/tutorials/create-an-hh2-service-account-in-sage-300-cre

---

## Background

A *service account* is a special user account that is created in the Sage 300 CREÂ® system. This account is required by the hh2 Cloud Service ([www.hh2.com](http://www.hh2.com)) to give the hh2 synchronization client the ability to sync the data in your Sage 300 CREÂ® database with the hh2 Cloud Service. This account also permits the hh2 Cloud Service to sync the hh2 data with Procore.

## Things to Consider

- **Required User Permission**:

  - Permission to create new user accounts in your company's Sage 300 CREÂ® database.
- **Additional Information**:

  - The service account must be granted *Application Admin* and *Security Admin* access permission to your Windows-based Sage 300 CREÂ® server.
  - The Sage 300 CREÂ® server should be running on a Windows server or standalone computer, and NOT a workstation.
  - For best results, perform these steps either at the server or from a location with remote access to your server.

## Steps

1. Log in to your Sage 300 CREÂ® server.
2. Create a new user account to act as the "service account" (e.g., create an account named 'hh2Admin'). For instructions, refer to the User Guide for your version of Sage 300 CREÂ®.   
   ***Important!*** Do NOT use a Windows user account.
3. Configure the new service account as follows:

   - Add the account to the *Application Admin* and *Security Admin* groups.
   - Mark the âPassword Never Expiresâ option for the account's password.   
     *Note*: Next, your Procore point of contact  will work with you to install and configure the hh2 synchronization client on the system running your Sage 300 CRE database.