# View Contract Compliance Documents for Commitments as a Payor

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/view-contract-compliance-documents-for-commitments-as-a-payor

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

When enabled on a Procore project, Procore Pay adds a 'Compliance' tab to the project's commitments. On a subcontractor invoice, the controls in the 'Contract Compliance Documents' card work with the 'Contract Compliant' setting in the 'Payment Requirements' tab of the Company level Payments tool. This allows your team to track and review the status of the commitment contract's compliance document entries (for example, agreements, bonds, licenses, permits, and more). This helps your team ensure that all documents comply with the contract's requirements before your team releases invoice payments with Procore Pay.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)
- **Additional Information**:

  - To view contract compliance documents as a user with 'Read-Only' or 'Standard' level permissions on the Commitments tool, you must have the permissions detailed in [View a Subcontract](/product-manuals/commitments-project/tutorials/view-a-subcontract).
  - To preview a file attachment in the **Details** pane of a contract compliance document entry:\* The user who created or edited the entry must complete the upload by clicking **Save**.\* Your web browser must support the file type of the attachment. If the file type is not supported, a **Download** button appears so you can view it on your computer.

## Prerequisites

- To add the 'Compliance' tab to a project's commitments, enable Procore Pay on the project. See [Enable or Disable Procore Pay on Your Projects](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/enable-or-disable-pay).
- To track compliance status with Procore Pay, turn the 'Contract Compliant' payment requirement ON. See [Configure Payment Requirements: Commitment Requirements](/process-guides/payor-setup-guide/configure-payment-requirements).
- An [invoice administrator](/process-guides/payor-setup-guide/add-invoice-administrators) must first [Create Contract Compliance Documents for Commitments as an Invoice Administrator](/process-guides/invoice-administrator-guide/create-contract-documents--statuses).

## Steps

- View the Contract Compliance Documents Card
- View a Contract Compliance Document's Details

### View the Contract Compliance Documents Card

1. Navigate to the project's **Commitments** tool.
2. In the **Contracts** tab, locate the commitment to work with.
3. Click the **Number** link to open it.
4. In the commitment, click the **Compliance** tab.
5. Scroll to the **Contract Compliance Documents** card.  
    Any existing documents and their corresponding statuses appear in the table in the Contract Compliance Documents card.

##### Contract Compliance Documents Card

This image shows you the Contract Compliance Documents card.

This table details the elements of the Contract Compliance Documents card.

| Element | Type | Description |
| --- | --- | --- |
| Create New | Menu Button | **Available to invoice administrators only**. Click this button to add a new compliance document to the commitment contract. See [Manage Contract Compliance Documents & Statuses for a Commitment](https://support.procore.com/products/online/procore-pay/tutorials/manage-contract-compliance-documents-and-statuses-for-a-commitment) for instructions. |
| Compliance Status | Status | Procore looks at the status of each listed document to determine the status to show:   - **Compliant**. Indicates all listed documents are in a compliant status. - **Not Compliant**. Indicates one (1) or more listed documents are in a not-compliant status. |
| Name | Field | Shows the name entered for the contract compliance document. Click the hyperlink to open the document and view the document details. |
| Type | Field | Shows the selected document type. Selections include *Bond*, *License*, *Master Agreement*, *Permit*, *W-9*, and *Other*. |
| Status | Field | Shows the current status set for the document: *Compliant* or *Not Compliant* *.* |
| Effective Date | Field | Shows the effective date of the document in the Company or Project Directory. |
| Expiration Date | Field | Shows the expiration date for the document in the Company or Project Directory. The following icons also appear to alert when a document is near or past its expiration date:    **Expiring Soon**. Starts showing 14 days before the expiration date.    **Expired**. Starts showing one (1) day after the expiration date. *Note*: Invoice administrators have the option to configure expiration notifications to invoice contacts. To learn more, see [Create Contract Compliance Documents for Commitments as an Invoice Administrator](/process-guides/invoice-administrator-guide/create-contract-documents--statuses). |
| Notes | Field | Shows any comments about the contract compliance document. |
|  | Icon | Shows that the entry has a file attachment. Each compliance document entry can have one (1) attachment. You cannot download attachments by clicking this icon. |
|  | Icon | **Available to invoice administrators only**. Hover the mouse cursor over a document row. Then click this icon to place a document into edit mode. This opens the document for viewing and you can edit the information in the Details panel. |
|  | Icon | Hover the mouse cursor over a document row. Then click this icon to download a copy of the document. |
|  | Icon | **Available to invoice administrators only**. Hover the mouse cursor over a document row. Then click this icon to permanently remove the document from the list of contract compliance documents. |

### View a Contract Compliance Document's Details

1. Navigate to the project's **Commitments** tool.
2. In the **Contracts** tab, locate the commitment to work with.
3. Click the **Number** link to open it.
4. In the commitment, click the **Compliance** tab.
5. Scroll to the **Contract Compliance Documents** card.  
    Any existing documents and their corresponding statuses appear in the table.
6. Locate the contract compliance document to view.
7. Click the document's **Name** link to open it.

##### Contract Compliance Details Page

This image shows you the Contract Compliance Details page.

This table details the elements of Contract Compliance Details page. If you are an invoice administrator, additional editing options are available. For details, see [Edit Contract Compliance Documents for Commitments as an Invoice Administrator](/product-manuals/procore-pay/tutorials/edit-contract-compliance-documents-for-commitments-as-an-invoice-administrator).

| Element | Type | Description |
| --- | --- | --- |
| Page Preview | Frame | If your web browser supports the attachment's file type, a preview of the file appears in the window. If the attachment has multiple pages, you can:   - Click the **Show/Hide** pages button on the left side of the window. - Enter a page number in the Page control at the bottom of the window to jump to a page. - Use the zoom in/out features to adjust the attachment display.   If you web browser doesn't support the attachment's file type, a **Download** button appears instead of a preview, so you can view the attachment on your computer. |
|  | Menu | Click the vertical ellipsis to and choose the **Download** option to download the file attachment to your computer. |
| Name | Field | Shows the name entered for the contract compliance document. Click the hyperlink to open the document and view the document details. |
| Type | Field | Shows the selected document type. Selections include *Bond*, *License*, *Master Agreement*, *Permit*, *W-9*, and *Other*. |
| Status | Field | Shows the current status set for the document: *Compliant* or *Not Compliant* *.* |
| Effective Date | Field | Shows the effective date of the document in the Company or Project Directory. |
| Expiration Date | Field | Shows the expiration date for the compliance document. The following icons also appear to alert when a document is near or past its expiration date:    **Expiring Soon**. Starts showing 14 days before the expiration date.    **Expired**. Starts showing one (1) day after the expiration date. *Note*: Invoice Administrators have the option to configure the send expiration notifications to invoice contacts. To learn more, see [Create Contract Compliance Documents for Commitments as an Invoice Administrator](/process-guides/invoice-administrator-guide/create-contract-documents--statuses). |
| Notes | Field | Shows any comments about the contract compliance document. |
| Attachment | Field | Shows a hyperlink for the file attachment and opens the attachment in a Details pane in a separate browser window. |
|  | Icon | Hover the mouse cursor over a document row. Then click this icon to download a copy of the document. |