# Set Up the Export Subcontractor Invoices Feature for Sage 300 CREÂ®

Source: https://v2.support.procore.com/product-manuals/sage-300-cre/tutorials/set-up-the-subconttractor-invoices-feature-for-sage-300-cre

---

## Background

If you have 'Admin' permission on the company's ERP Integrations tool, you can complete the initial setup for the Sage 300 CREÂ® subcontractor invoices feature so that your team can sync invoices from Procore to Sage 300 CREÂ®.

## Things to Consider

- **Required User Permissions**:

  - to request to turn the feature ON and to designate the 

    In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

    Accounting Approver who will be authorized to sync invoices. You must be your company's Procore Administrator to make this request.
  - *To complete the initial setup steps below,* âAdminâ on the companyâs ERP Integrations tool and login credentials for your company's 

    The *hh**2* *synchronization client* is a third-party client application developed by hh2. When the ERP Integrations tool is enabled on a company's Procore account and the tool is configured to work with Sage 300 CREÂ®CRE, your Procore point of contact  will work with your Procore Administrator to install and configure the hh2 synchronization client on your Sage 300 CREÂ® Server. This allows data to sync between your Sage 300 CREÂ® database server and Procore.

    hh2Â Synchronization Client.
- **Requirements**:

  - The hh2 sync client must be running version 1.31.467.xxxx or higher.
  - The ERP Integrations tool must be enabled on the company account.
  - The ERP Integrations tool must be configured to work with Sage 300 CREÂ®.
  - The *Not Required* option but must be set for 'Date Received Usage' and 'Payment Date Usage' in the 'AP Settings - Invoice Settings' in Sage 300 CREÂ® as described below.
- **Additional Information**:

  - Some fields in a Procore subcontractor invoice are NOT exported directly to Sage 300 CREÂ®. Instead, the system first uses those fields to calculate a value and then the calculated value is exported to Sage 300 CREÂ®. For details, see [Sage 300 CREÂ® - Data Mapping](/product-manuals/sage-300-cre/detailed-data-mapping).
- **Limitation**:

  - If your company is using the ERP Integrations tool to import Sage 300 CREÂ® tax codes and tax groups into Procore, you will not be able to export subcontractor invoices to Sage 300 CREÂ®. To learn more about tax codes and groups, see [How can I use tax codes on a Procore project?](/faq-how-can-i-use-tax-codes-on-a-procore-project) and [Set Up the Import Sage 300 CREÂ® Tax Groups Feature](/product-manuals/sage-300-cre/tutorials/set-up-the-imoprt-sage-300-cre-tax-groups-feature).

## Workflows

## Steps

1. Configure the hh2 Sync Client for Subcontractor Invoice Exports
2. Set the 'Date Received Usage' and 'Payment Date Usage' to Not Required in Sage 300 CREÂ®
3. Set Up Subcontractor Invoice Exports in Procore

#### Configure the hh2 Sync Client for Subcontractor Invoice Exports

First, configure the settings for subcontractor invoice exports in the 

The *hh**2* *synchronization client* is a third-party client application developed by hh2. When the ERP Integrations tool is enabled on a company's Procore account and the tool is configured to work with Sage 300 CREÂ®CRE, your Procore point of contact  will work with your Procore Administrator to install and configure the hh2 synchronization client on your Sage 300 CREÂ® Server. This allows data to sync between your Sage 300 CREÂ® database server and Procore.

hh2Â Synchronization Client:

1. Log into your Sage 300 CREÂ® server using an account with administrative privileges.
2. Launch your company's hh2 Sync Client.

   ##### Â Important

   The hh2 sync client must be running version 1.31.467.xxxx or higher.

- Click **Connect**.
- Browse to the **Local Connections** tab.
- Click **Mappings**.
- Click **Advanced Mappings**.
- Place a checkmark in these circles:

  - Distribution (AP)
  - Distribution Payment (AP)
  - Invoice (AP)
  - Payment (AP)
  - Invoice Payment (AP)
  - Invoice Settings (AP)
- Click **Save**.

---

#### Set the 'Date Received Usage' and 'Payment Date Usage' to Not Required in Sage 300 CREÂ®

Either the *Not Used* or *Not Required* option button must be selected for 'Date Received Usage' and 'Payment Date Usage' in the 'AP Settings - Invoice Settings' in Sage 300 CREÂ®. To learn more about these settings, see your Sage 300 CREÂ® user guide or help system.

---

#### Set Up Subcontractor Invoice Exports in Procore

Next, complete the following setup task in Procore:

#### Email Your List of Accounting Approvers to Procore

1. Ask your companyâs Procore Executive Sponsor to with the following information:

   - **Email addresses for the accounting approvers who should be granted the additional permission to export subcontractor invoices to Sage 300 CREÂ®.**

     ##### Â Note

     - If you do not know your companyâs Executive Sponsor, see the Executive Sponsor field under **Account Information** in the company's **Admin** tool.
     - If there is no Executive Sponsor listed, contact your companyâs 

       A *Procore Administrator* is a user who has 'Admin' level permissions on all of the Company level Tools in Procore. Granting a user âAdminâ level permissions in the Company level Directory tool automatically assigns that user âAdminâ permissions on all Company level tools. Also called a *Company Administrator*.

       ProcoreÂ Administrator.

- Wait for your Executive Sponsor to confirm that the Procore ERP Support Team has granted permissions to your company's designated accounting approvers.  
   Once permission has been granted, you can begin using the feature.