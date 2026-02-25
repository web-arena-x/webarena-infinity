# Complete a Prime Contract Change Order with DocuSignÂ®

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/complete-a-prime-contract-change-order-with-docusign

---

## Background

If you have a DocuSignÂ® account, you can connect your Procore prime contract change order to DocuSignÂ® to manage the signature process. This provides the parties on the contract change with a way to receive, review, and return their signatures onlineâat any time and from any Internet-enabled device.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Prime Contracts tool.
  - 'Admin' level permissions on the project's Change Orders tool.
- **Additional Information:**

  - Once you sign into you DocuSignÂ® account from Procore, you will NOT need to sign in again until the login token expires. Once expired, the 'Re-Authentication Required' banner appears in Procore. To learn more, see [What do the different DocuSignÂ® banners in Procore mean?](/faq-what-do-the-different-docusign-banners-in-procore-mean)
  - If you do not have DocuSignÂ® enabled, see [Create a Prime Contract Change Order from a Change Event](/product-manuals/change-events-project/tutorials/create-a-prime-contract-change-order-from-a-change-event) or [Create a Prime Contract Change Order](/product-manuals/prime-contracts-project/tutorials/create-a-prime-contract-change-order).
- For companies using the  ERP Integrations tool: **Show/Hide**

  - Not all ERP integrations support the sync of change orders. For those that do, additional requirements, limitations, and considerations vary depending on the ERP system your company's account is integrated with.

## Prerequisites

- [Enable the DocuSignÂ® Integration on Your Company's Procore Account](/product-manuals/admin-company/tutorials/enable-the-docusign-integration-on-your-companys-procore-account)
- [Enable the DocuSignÂ® Integration on a Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project)
- To request signatures using the Procore + DocuSignÂ® integration, you must have an active DocuSignÂ® account. For details, see:

  - [Do I need a DocuSignÂ© account?](/faq-do-i-need-a-docusign-account)
  - [How do I get a DocuSignÂ® account?](/faq-how-do-i-get-a-docusign-account)
- [Create Prime Contracts](/product-manuals/prime-contracts-project/tutorials/create-prime-contracts)
- [Create a Prime Contract Change Order from a Change Event](/product-manuals/change-events-project/tutorials/create-a-prime-contract-change-order-from-a-change-event) or [Create a Prime Contract Change Order](/product-manuals/prime-contracts-project/tutorials/create-a-prime-contract-change-order)

## Steps

1. Open the Change Order
2. Log In to DocuSignÂ®
3. Prepare the DocuSignÂ® Envelope

### Open the Change Order

The steps you use to open the change order depend on your configuration settings and whether the Change Events tool is enabled on the project.

##### Â Tip

**Unsure about whether to enable the Change Events tool on a project?**

Your Procore Administrator can turn the tool ON or OFF. However, it is important to learn more about that process first. For details, see [Can I enable the Change Events tool on my existing project?](/faq-can-i-enable-the-change-events-tool-on-my-project) and [Can I disable the Change Events tool?](/faq-can-i-disable-the-change-events-tool)

#### For Contracts Using the 1-tier change order Setting and For Projects using the Change Events tool

1. Navigate to the project's **Change Events** tool.
2. In the **Line Items** tab, click the change event's **Number** link.
3. In the change event, click **Edit**.
4. Scroll to the **Prime Contract Change Order** section.
5. Locate the change order to send for signature and click **View**.
6. In the change order, click **Edit**.
7. Mark the **Sign with DocuSign** check box.
8. In the change order, click **Edit** and complete the data entry.
9. Click the **Complete with DocuSign** button at the bottom of the page.

#### For Contracts Using the 2- or 3-Tier Change Order Setting and For Projects Not using the Change Events Tool

If the Prime Contracts tool on your project is configured to the use two (2) or three (3) tier change order setting, or if the Change Events tool is NOT active on your project, use these steps to open the change order:

1. Navigate to the project's **Prime Contracts** tool.
2. Locate the prime contract with the change order. Click the **Number** link.
3. Under **General Information**, click **Edit**.
4. Mark the **Sign with DocuSign** check box.
5. In the **General Information** card, click **Save**.
6. Click the **Change Orders** tab.
7. In the **Prime Contract Change Orders** table, click the **Number** link.
8. In the change order, click **Edit** and complete the data entry.
9. Click the **Complete with DocuSign** button at the bottom of the page.

### Log In to DocuSignÂ®

If you are NOT logged into your DocuSignÂ®account when you launch the DocuSignÂ® application from Procore:

##### Â Notes

- To learn how to gain access to DocuSignÂ® from a Procore tool, see one of the tasks in [Which Procore project tools support the DocuSignÂ® integration?](/faq-which-procore-project-tools-support-the-docusign-integration)
- To log into DocuSignÂ® from Procore, you need valid login credentials (an email address and a password) for a DocuSignÂ® account. To learn more, see [Do I need a DocuSignÂ© account?](/faq-do-i-need-a-docusign-account) and [How do I get a DocuSignÂ® account?](/faq-how-do-i-get-a-docusign-account)

1. At the DocuSignÂ® Log In page, type your email address in the **Email** box:
2. Click **Next**.
3. Enter your password.
4. Click **Log In**.

### Prepare the DocuSignÂ® Envelope

Once you are logged into the DocuSignÂ®, the 'Upload a Document and Add Envelope Recipient' page appears. Complete these steps:

- Add Documents to the Envelope
- Add Recipients to the Envelope
- Add a Message to All Recipients
- Preview the Signature Fields & Send the Envelope

#### Add Documents to the Envelope

The following Procore information automatically populates the DocuSignÂ® envelope:

- A PDF copy of the change order is automatically added to the 'Add Documents to Envelope' section.
- The required signature boxes for each 'Role' on the contract. For example, the *General Contractor* or *Subcontractor* who are parties on the change order. This includes each users 'Name' and 'Email Address.' For more information, see Add Recipients to the Envelope below.

1. *Optional:* If you want to add additional documents to the envelope, choose one of the available options under the 'Add Documents to the Envelope' section:

       

   ##### Â Note

   The available options in the 'Add Documents to the Envelope' section are developed and maintained by DocuSignÂ®. To learn how to use DocuSignÂ®, Procore recommends reviewing the content on [support.docusign.com](https://support.docusign.com/).