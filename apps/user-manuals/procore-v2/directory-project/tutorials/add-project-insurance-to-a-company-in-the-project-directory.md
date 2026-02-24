# Add Project Insurance to a Company Record in the Project Directory

Source: https://v2.support.procore.com/product-manuals/directory-project/tutorials/add-project-insurance-to-a-company-in-the-project-directory

---

##### Â In Beta

A redesigned version of the Project Directory is currently in beta and can be enabled with [Procore Explore](/product-manuals/admin-company/tutorials/manage-features-with-procore-explore).

## Background

An 

In Procore, the term *Insurance Manager* refers to an internal employee (or multiple employees) at your company who serve as your organization's primary point of contact(s) for ensuring that the insurance policies for your contractors, subcontractors, and other vendors are in compliance with requirements and that their required policies and certificates are kept up-to-date.

Insurance Manager can use the steps below to add insurance information (for example, insurance policies and certificates) for the contractors, subcontractors, and other vendors who have company records in the Project level Directory tool.

## Things to Consider

- [Required User Permissions](/product-manuals/directory-project/permissions)
- If you have enabled the ERP Integrations tool for Sage 300 CRE, the system locks the following insurance fields when a Sage 300 CREÂ® vendor with insurance information is synced with Procore: Insurance Type (e.g., General, Automotive, Umbrella, and Worker's), Effective Date, Expiration Date, Limit Amount, Name, and Policy Number.
- Insurance updates are recorded in the company record's 'Change History' tab.
- If you would like to add the Insurance Provider as a Vendor/Company in the Project or Company Directory, add the provider first. See [Add a Company to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory) or [Add a Company to the Company Directory](/product-manuals/directory-company/tutorials/add-a-company-to-the-company-directory).
- Changing a 'Status' at a later time will NOT trigger any automated email notifications, because Procore's automated email notifications to the Insurance Manager are associated with the Expiration Date.
- **For companies using the** **ERP Integrations tool:**

 - If you have enabled the ERP Integrations tool for Sage 300 CRE, the system locks the following insurance fields when a Sage 300 CRE vendor with insurance information is synced with Procore: Insurance Type (e.g., *General*, *Automotive*, *Umbrella*, and *Worker's*), Effective Date, Expiration Date, Limit Amount, Name, and Policy Number.

## Steps

1. Navigate to the Project level **Directory** tool.
2. Click the **Companies** tab.
3. Next to the company, click **Edit.** OR Click the **company name**.
4. Click the **Insurance** tab.
5. Click **Add Project Insurance**.
6. Fill out the form:

   - **Type**. Enter the type of insurance coverage (*eneral Liability*, *Umbrella/Excess Liability*, *Builder's Risk*, *Professional Liability*, *Pollution Coverage*, and so on).
   - **Insurance Provider**. Input the insurance carrier's name exactly as it appears on the insurance certificate.
   - **Policy Number**. Type the full policy number exactly as it appears on your certificate.
   - **Exempt**. If the company for which you are entering insurance information holds a certificate or affidavit of exemption, mark this checkbox (e.g., Workers' Compensation).
   - **Limit Amount**. Enter the limit amount for the insurance in this box (If the combined single limit amount is two million dollars, enter 2,000,000).   
     *Note*: You can enter up to 17 characters in the Limit Amount box.
   - **Information Received**. Mark this checkbox if you received the complete set of paperwork regarding this insurance.
   - **Effective Date**. Enter the effective date as it appears on the certificate.
   - **Expiration Date**. Enter the expiration date as it appears on the certificate.
   - **Send Expiration Notification?**: Mark this checkbox to have automatic notification emails sent to users designated as insurance managers in your Directory and the vendor's primary contact and invoice contacts when the insurance is about to expire. See [Who receives notification emails when a vendor's insurance expires?](/faq-who-receives-notification-emails-when-a-vendors-insurance-expires)
   - **Status**. Select one of Procore's default informational statuses from the drop-down list. See [What are the default statuses for insurance in Procore?](/faq-what-are-the-default-statuses-for-insurance-in-procore)
   - **Notes**. Type any additional information about the insurance.
   - **Additional Insured**. Add a free-text entry about any additional insured entities for the Certificate of Insurance (COI).
   - Attachments. Click the **Attach File(s)** link or use the **Drag-and-Drop File(s)** area to add the relevant insurance policy, certificates, and any affidavits here.
7. Click **Add**.