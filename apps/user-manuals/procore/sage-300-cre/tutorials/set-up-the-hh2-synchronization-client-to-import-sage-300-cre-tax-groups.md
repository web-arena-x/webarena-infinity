# Set Up the hh2 Synchronization Client to Import Sage 300 CRE Tax Groups

Source: https://v2.support.procore.com/product-manuals/sage-300-cre/tutorials/set-up-the-hh2-synchronization-client-to-import-sage-300-cre-tax-groups

---

## Background

Before you can perform the integration steps described in [Setup the Import Sage 300 CREÂ® Tax Groups Feature](/product-manuals/sage-300-cre/tutorials/set-up-the-imoprt-sage-300-cre-tax-groups-feature), you must perform the steps below on the hh2 synchronization client.

## Things to Consider

- **Required User Permissions**:

  - The company's 

    A *Procore Administrator* is a user who has 'Admin' level permissions on all of the Company level Tools in Procore. Granting a user âAdminâ level permissions in the Company level Directory tool automatically assigns that user âAdminâ permissions on all Company level tools. Also called a *Company Administrator*.

    ProcoreÂ Administrator should supply the steps below to the company's IT administrator for the hh2 tool.
  - The person performing the steps will need to log into the Sage 300 CREÂ® server using an account with administrative privileges.
- **Supported ERP** **Integrations**:

  - Your company's Procore account must already be integrated with Sage 300 CREÂ®.
- **Limitations**:

  - The sync process for tax groups/tax codes is NOT bidirectional. You will not have the ability to export tax codes from Procore to create tax groups in Sage 300 CREÂ®.

## Steps

1. Log into your Sage 300 CREÂ® server using an account with administrative privileges.
2. Launch your company's hh2 Synchronization Client.
3. Click **Connect**.
4. Browse to the **Local Connections** tab.
5. Click **Mappings**.
6. Click **Advanced Mappings**.
7. Place a checkmark next to the following items:  
   ***Important!*** Do NOT remove any previously selected checkmarks. Doing so could negatively impact your existing Sage 300 CREÂ® configuration settings.

   - Tax Group
   - Tax Rate
8. Click **Sync.**
9. Click **Settings** **.**
10. Select a Sync Type of **Deep** and the timeframe of **âThe beginning of timeâ**.
11. Click **OK**.
12. Click the arrow to expand the options under your connection as shown below.
13. Click **Sync**.  
     After the sync is complete, you can close the hh2 Synchronization Client and log off of the Sage 300 CREÂ® server.