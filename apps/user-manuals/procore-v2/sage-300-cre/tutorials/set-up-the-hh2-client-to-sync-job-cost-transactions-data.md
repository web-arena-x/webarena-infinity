# Set Up the hh2 Sync Client to Sync Cost Transactions Data

Source: https://v2.support.procore.com/product-manuals/sage-300-cre/tutorials/set-up-the-hh2-client-to-sync-job-cost-transactions-data

---

## Background

If your Procore company account is integrated with Sage 300 CREÂ®, you can import job cost transactions from Sage 300 CREÂ® and include them as direct costs in Procore budget line items. In addition to the lump-sum job-to-date cost values imported from Sage 300 CREÂ®, users on integrated companies can view specific transaction details (for example: date, invoice number, and other cost typesâsuch as payroll and expense) around individual job cost transactions as direct costs in the project's Budget tool.

## Things to Consider

- **Required User Permissions**:

  - The company's 

    A *Procore Administrator* is a user who has 'Admin' level permissions on all of the Company level Tools in Procore. Granting a user âAdminâ level permissions in the Company level Directory tool automatically assigns that user âAdminâ permissions on all Company level tools. Also called a *Company Administrator*.

    ProcoreÂ Administrator should supply the steps below to the company's IT administrator for the hh2 tool.
  - The person performing the steps will need to log into the Sage 300 CREÂ® server using an account with administrative privileges.
- **Supported ERP** **Integrations**:

  - Your company's Procore account must already be integrated with Sage 300 CREÂ®.
- **Prerequisites:**

  - Enable the Direct Costs tool on the project that is integrated with Sage 300 CREÂ®.
  - Before enabling these features on your Procore company account, .
  - Ensure that you have a confirmed configuration date with your Procore point of contact .
- **Limitations**:

  - If you enable the Direct Costs tool on a project integrated with Sage 300 CREÂ®, you will NOT have the ability to sync any direct costs created in Procore back to Sage 300 CREÂ®.

## Steps

1. Log in to your Sage 300 CREÂ® server using an account with administrative privileges.
2. Launch your company's hh2 Synchronization Client.
3. Click **Connect**.
4. Browse to the **Local Connections** tab.
5. Click **Mappings**.
6. Click **Advanced Mappings**.
7. Place a checkmark in the **GL Account** and **GL Account Prefix**, **Invoice (AP)** and **Job (JC)**.  
   ***Important!*** Do NOT remove any previously selected checkmarks. Doing so could negatively impact your existing Sage 300 CREÂ® configuration settings.
8. Click **Transaction**(**JC**) to highlight it, then remove the checkmarks from the circles as follows:

   - Commitment Change Order
   - Credit Account
   - Debit Account
   - Employee
   - Equipment
   - Pay Id
   - Reference 1
   - Reference 2
9. Click **Save**.
10. Navigate to the **Sync** tab.
11. Place a checkmark next to your connection as shown below.
12. Click **Settings.**
13. Select a **Sync Type** of *Deep* and the timeframe of *The beginning of time*.
14. Click **OK**.
15. Click the arrow to expand the options under your connection.
16. Click **Deselect All**.
17. Place a checkmark in the **GL Account** and **GL Account Prefix**, **Invoice (AP)** and **Transaction (JC)***.*
18. Click **Sync**.  
    After the sync is complete, you can close the hh2 Synchronization Client and log off of the Sage 300 CREÂ® server.