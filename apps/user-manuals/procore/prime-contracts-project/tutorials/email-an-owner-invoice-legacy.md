# Email an Owner Invoice from the Prime Contracts Tool (Legacy)

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/email-an-owner-invoice-legacy

---

##### Â Legacy Content

This page details the legacy owner invoice experience. A modernized experience is also available.

## Background

After creating an [upstream invoice](/glossary-of-terms) that bills against a [client contract](/glossary-of-terms), [funding](/glossary-of-terms), or [prime contract](/glossary-of-terms), you can send a copy of the invoice's 'Detail' tab to your upstream collaborator to review. Once reviewed, your collaborator can then reply directly to that message to indicate that they have approved your invoice for payment (or to supply you with a reason for rejecting your invoice). To ensure that your collaborator's response is captured in writing, Procore saves all replies to your outgoing message's 'From' address in the Emails tab on the invoice.

## Things to Consider

- [Required User Permissions](/product-manuals/prime-contracts-project/permissions)
- **Additional Information:**

  - Clicking the **Email Invoice** button sends a copy of the invoice's 'Detail' tab to the designated recipients.
  - The data on the 'Configurable PDF' tab of the invoice is NOT provided with this email message.

## Prerequisites

- [Create an Owner Invoice](/product-manuals/prime-contracts-project/tutorials/create-an-owner-invoice)

## Steps

1. Navigate to the project's **Prime Contracts** tool.
2. In the table, locate the contract.
3. Click the **Number** link to open it.
4. Click the **Invoices** tab
5. Locate the invoice to send in the table.
6. Click the **Invoice #** link to open it.
7. Click **Email** **Invoice**.   
    This launches the 'Forward Invoice #[#] for [Contract or Funding] #[#] - [Billing Period Start - Billing Period End]' window in the **Emails** tab of the invoice.

   ##### Â Notes

   - The **Email Invoice** button sends a copy of the invoice's 'Detail' tab to the designated recipients.
   - The data on the 'Configurable PDF' tab of the invoice is NOT provided with this email message.

- Complete the following fields:

  - **To**. Enter the name of the person you are requesting payment from.
  - **CC**. Enter in names of people you want to be copied on the email thread. Your name appears in this field by default.
  - **BCC**. Enter in names of people you want to be copied on the email thread.
  - **Private**. Mark this checkbox if you only want the invoice to be available to the [invoice administrator](/glossary-of-terms) and those named in the To/Cc fields.
  - **Subject**. This field will populate with the number of the invoice.
  - **Attachments**. Attach any related documents or files.
  - **Message**. Include an additional message regarding the invoice.
- Click **Send**.  
   A YELLOW 'Communication Created' banner appears to confirm the outgoing message has been created and added to Procore's outgoing email queue.

##### Â Notes

- A record of your outgoing message is saved in the 'Emails' tab on the invoice.
- Any messages sent to the 'From' address on your outgoing message are automatically saved in the invoice's 'Emails' tab. This provides your message recipients with the convenience to use the reply feature in their email program. It also captures your collaborator's approve or reject responses in writing.