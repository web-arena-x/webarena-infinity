# Set Up the hh2 Synchronization Client for Exporting PCCOs

Source: https://v2.support.procore.com/product-manuals/sage-300-cre/tutorials/set-up-the-hh2-synchronization-client-for-exporting-pccos

---

## Background

To learn how to export a Prime Contract Change Order, see [Export a PCCO to ERP](/product-manuals/erp-integrations-company/tutorials/export-a-pcco-to-erp).

## Things to Consider

- **Required User Permissions**:

  - The company's 

    A *Procore Administrator* is a user who has 'Admin' level permissions on all of the Company level Tools in Procore. Granting a user âAdminâ level permissions in the Company level Directory tool automatically assigns that user âAdminâ permissions on all Company level tools. Also called a *Company Administrator*.

    ProcoreÂ Administrator should supply the steps below to the company's IT administrator for the hh2 tool.
  - The person performing the steps will need to log into the Sage 300 CREÂ® server using an account with administrative privileges.
- **Supported ERP** **Integrations**:

  - Your company's Procore account must already be integrated with Sage 300 CREÂ®.
- **Limitations**:

  - The sync process for the Prime Contract Change Orders is NOT bidirectional. You will not have the ability to import change orders or updates made in Sage 300 CREÂ® to Procore.

## Steps

1. Log into your Sage 300 CREÂ® server using an account with administrative privileges.
2. Launch your company's hh2 Synchronization Client.
3. Click **Connect**.
4. Browse to the **Local Connections** tab.
5. Click **Mappings**.
6. Click **Advanced Mappings**.
7. Place a checkmark next to the following items:  
   ***Important!*** Do NOT remove any previously selected checkmarks. Doing so could negatively impact your existing Sage 300 CREÂ® configuration settings.

   - Contract (CN)
   - Contract Change Order (CN)
   - Contract Change Order Item (CN)
   - Contract Item (CN).
   - Customer
   - Customer Type
   - Invoice (AP)
   - Job (CV)   
     *Note*: This may already be selected.
   - Quick Bill Contract
   - Quick Bill Contract Item
8. If you own the **Project Management (PJ) Module** in Sage 300 CREÂ®, you will also place a checkmark next to the following items (**if not, go the next step**):

   - Contract Change Order (PJ)
   - Contract Change Request (PJ)
9. Click **Transaction (JC)** to highlight it.
10. Place a checkmark next to **ALL** the items in the panel on the right.
11. Remove the following checkmarks from the circles in the panel on the left:

    - Commitment Change Order
    - Credit Account
    - Debit Account
    - Employee
    - Equipment
    - Pay ID
    - Reference 1
    - Reference 2
12. Click **Save**.
13. Navigate to the **Sync** tab.
14. Place a checkmark next to your connection as shown below.
15. Click **Settings** **.**
16. Select a Sync Type of **Deep** and the timeframe of **âThe beginning of timeâ**.
17. Click **OK**.
18. Click the arrow to expand the options under your connection as shown below.
19. Click **Deselect All**.  
     This removes all the checkmarks from the selected items.
20. Place a checkmark in the circle next to the following items:

    - Contract (CN)
    - Contract Change Order (CN)
    - Contract Change Order Item (CN)
    - Contract Item (CN).
    - Customer
    - Customer Type
    - Quick Bill Contract
    - Quick Bill Contract Item
21. If you own the **Project Management (PJ) Module** in Sage 300 CREÂ®, you will also place a checkmark next to the following items (**if not, go to the next step**):

    - Contract Change Order (PJ)
    - Contract Change Request (PJ)
22. Click **Sync**.  
     After the sync is complete, you can close the hh2 Synchronization Client and log off of the Sage 300 CREÂ® server.