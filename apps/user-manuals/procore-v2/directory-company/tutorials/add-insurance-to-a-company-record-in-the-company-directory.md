# Add Insurance to a Company Record in the Company Directory

Source: https://v2.support.procore.com/product-manuals/directory-company/tutorials/add-insurance-to-a-company-record-in-the-company-directory

---

## Background

An 

In Procore, the term *Insurance Manager* refers to an internal employee (or multiple employees) at your company who serve as your organization's primary point of contact(s) for ensuring that the insurance policies for your contractors, subcontractors, and other vendors are in compliance with requirements and that their required policies and certificates are kept up-to-date.

Insurance Manager can use the steps below to add insurance information (for example, insurance policies, insurance certificates, and other supporting documents) for the contractors, subcontractors, or other vendors who have company records in the Company level Directory tool. See [Designate an Insurance Manager for Your Procore Company](/product-manuals/directory-company/tutorials/designate-an-insurance-manager-for-your-procore-company).

##### Â Tip

If you want to add an Insurance Provider as a vendor/company in your Company Directory, add the provider first. See [Add or Edit a Vendor/Company to the Company Directory](/product-manuals/directory-company/tutorials/add-a-company-to-the-company-directory).

## Things to Consider

- [Required User](/product-manuals/directory-company/permissions) [Permissions](/product-manuals/directory-company/permissions)
- Updates to a vendor's insurance record are listed in the Change History tab.
- Follow the steps below only when you want to add insurance to the company record for all projects. If you want to add project-specific insurance to a vendor record, follow steps to [Add Project Insurance to a Company Record in the Project Directory](/product-manuals/directory-project/tutorials/add-project-insurance-to-a-company-in-the-project-directory).
- **If your company has enabled the ERP Integrations tool, the following is also true:**

 - The Vendor Insurance from Sage 300 CREÂ® will be synced with Procore's insurance: *Insurance Type* (e.g., General, Automotive, Umbrella, and Worker's), *Effective Date*, *Expiration Date*, *Limit Amount*, *Name*, and *Policy Number*.

## Steps

1. Navigate to the Company level **Directory** tool.
2. Click the **Companies** tab.
3. Click **Edit** next to the company.
4. In the vendor's record, click the **Insurance** tab.
5. Click **Add Company Insurance**.
6. In the **Add Insurance to [Company Name] Insurance Information (Global)** page, complete the following:

   - **Type**. Enter the type of insurance coverage (e.g., General Liability, Umbrella/Excess Liability, Builder's Risk, Professional Liability, Pollution Coverage, and so on).

     Type (Insurance)
   - **Insurance Provider**. Input the insurance carrier's name exactly as it appears on the insurance certificate.

     Insurance Provider
   - **Policy Number**. Type the full policy number exactly as it appears on your certificate.

     Policy Number (Insurance)
   - **Exempt**. If the company for which you are entering insurance information holds a certificate or affidavit of exemption, mark this checkbox (e.g., Workers' Compensation).

     Exempt (Insurance)
   - **Limit Amount**: Enter the limit amount for the insurance in this box (e.g., If your combined single limit amount is two million dollars, enter 2,000,000). *Note*: You can enter up to seventeen (17) characters.

     Limit Amount (Insurance)
   - **Information Received**: Mark this checkbox if you received the complete set of paperwork regarding this insurance.

     Information Received (Insurance)
   - **Effective Date**: Enter the effective date as it appears on the certificate.

     Effective Date (Insurance)
   - **Expiration Date**: Enter the expiration date as it appears on the certificate.

     Expiration Date (Insurance)
   - **Send Expiration Notification?**: Mark this checkbox to have automatic notification emails sent to users designated as insurance managers in your Directory and the vendor's primary contact and [invoice contacts](/faq-what-is-an-invoice-contact) when the insurance is about to expire. See [Who receives notification emails when a vendor's insurance expires?](/faq-who-receives-notification-emails-when-a-vendors-insurance-expires)

     Send Expiration Notification? (Insurance)
   - **Status**. Select one of Procore's default informational statuses from the drop-down list. See [What are the default statuses for insurance in Procore?](/faq-what-are-the-default-statuses-for-insurance-in-procore)*Notes*:

     - The default status setting when adding new insurance information is set to *Compliant*. However, it is up to the person performing the data entry to ensure that the status setting is accurate. When the insurance expires (based on the data entered in the 'Expiration Date' field), the status automatically changes to *Non-Compliant*. To change the status, see [Update Expiring Insurance for a Vendor in the Company Directory](/product-manuals/directory-company/tutorials/update-expiring-insurance-for-a-vendor-in-the-company-directory).
     - Compliance and registration standards vary between countries, states, cities, and usage must always be governed by your organization's standards and requirements.
     - Changing a status at a later time will NOT trigger an email notification. Email notifications are only sent to the designated Insurance Manager when triggered by the Expiration Date. When insurance has expired, the status will automatically change to non-compliant. See [Designate an Insurance Manager for Your Procore Company](/product-manuals/directory-company/tutorials/designate-an-insurance-manager-for-your-procore-company).

     Status
   - **Notes**. Type any additional information about the insurance.

     Notes
   - **Additional Insured**. Add a free-text entry about any additional insured entities for the Certificate of Insurance (COI).

     Additional Insured
   - **Attachments**: Click the **Attach File(s)** link or use the **Drag-and-Drop File(s)** area to add the relevant insurance policy, certificates, and any affidavits here.

     Attachments (Insurance)
7. Click **Add**.