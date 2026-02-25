# (Beta) Plan a Custom Workflow Template

Source: https://v2.support.procore.com/product-manuals/workflows-company/tutorials/plan-a-custom-workflow-template

---

##### Â In Beta

This page details functionality that is not available in Procore's production environment. Access to the features documented here is limited to specific Procore customers who have signed the required agreement to participate in Procore's Company level Workflows Tool Beta Program. The content on this page is for informational purposes only and all information and content on this page is subject to change without any prior notice. To learn more, see [About the Workflows Beta Program](/product-manuals/workflows-company/tutorials/about-the-workflows-tool).

## Background

Before getting started with a new custom workflow, Procore recommends that you create an initial plan or sketch of your existing workflow process. These initial planning steps don't need to be complicated. However, writing it down is a good practice, as it helps you gather the details you need for your custom workflow to satisfy your requirements.

As you plan your custom workflow, it is helpful to first understand the existing process currently being used in your company's Procore accounts. It is also important to work with your stakeholders, to ensure that your new custom workflow addresses your specific business needs and conditions.

## Things to Consider

- **Required User Permissions:**

  - This planning step is NOT performed in the Procore web application.

## Prerequisites

- You must be a registered Beta Program Participant. See [About the Workflows Beta Program](/product-manuals/workflows-company/tutorials/about-the-workflows-tool).

## Steps

### Create a Plan for Your Custom Workflow

In this tutorial, we asked ourselves the following questions in order to develop a custom workflow for subcontractor invoices. You can use this planning document as a guide for developing your own plan. Because every company and project can be different, the plans you develop in your environment will be different.

| Question | Example |
| --- | --- |
| What is the goal of the workflow? | To route subcontractor invoices through our company's sign-off conditions and approval process. |
| What action triggers the start of the workflow? | An invoice contact at a 'Contract Company' submits a completed subcontractor invoice in 'Draft' form to our Procore project. |
| What action(s) signify the end of the workflow? | - For invoices under $100,000.00 USD, a Project Manager (PM) approves the subcontractor invoice for payment. - For invoices under $1,000,000.00 USD, a Vice President (VP) approves the subcontractor invoice for payment. - For invoices $10,000.000.000 USD and over, an Executive approves the subcontractor invoice for payment, and the status of the invoice changes to 'Approved'. |
| What are the key actions and decisions of the workflow? | - An invoice creator submits a 'Draft' invoice. Depending on who has permission to create an invoice, a creator can be:    - An [invoice contact](/glossary-of-terms) at a 'Contract Company' who submits a 'Draft' invoice in response to an 'Invite to Bill'.   OR   - An [invoice administrator](/glossary-of-terms) at your company creates a subcontractor invoice on behalf of the invoice contact. - A Project Manager must review the 'Draft' invoice. Upon receipt of the invoice, an approval response is defined by the Project Manager changing the subcontractor invoice status to 'Under Review'.    - If the invoice is less than the amount defined by our company's signature conditions, the invoice's status will change to 'Approved'. If it is greater than the amount defined by our company, the invoice must be routed to a Vice President.   - If the Project Manager returns the invoice to the invoice contact, the status will move to 'Revise and Resubmit' and the invoice contact will then revise the invoice and resubmit it to the Project Manager. - A Vice President must review the invoice in the 'Under Review' status.    - If the invoice is less than the amount defined by our company's signature conditions for an Executive, an approval response is defined by the Vice President changing the invoice's status to 'Approved.'   - If the invoice is greater than the amount defined by our company, it must be routed to an Executive. |
| Across all of your Procore projects, which roles are responsible for completing each action in the workflow? | - Invoice Creator (for example, an invoice contact and/or invoice administrator) - Project Manager - Vice President - Executive |
| Who needs to be informed when an action is complete? *Note: This might include individuals not responsible for completing actions in the workflow.* | - When an Invoice Creator submits an invoice to request payment, a Project Manager must be informed. - When a Project Manager approves an invoice, the invoice contact and accountants must be informed. - When the invoice amount exceeds the signature conditions defined for a Project Manager, the Vice President must be informed. - When a Project Manager returns an invoice, the invoice contact must be informed. - When a Vice President rejects an invoice, the invoice contact and Project Manager must be informed so it can be revised. - When a Vice President approves an invoice, the invoice contact, accountants, and Project Manager must be informed. - When the invoice amount exceeds the signature conditions defined for a Vice President, the Executive and Project Manager must be informed. - When the Executive approves an invoice, the invoice contact, accountants, and Project Manager must be informed. - When the Executive returns an invoice, the invoice contact and Project Manager must be informed so it can be revised. |
| What are the roles and groups that need to be informed of actions? *Note: List them all.* | - Invoice Creator (for example, an invoice contact and/or invoice administrator) - Project Manager - Accountants - Vice President - Executive |

## Next Steps

- Add a Custom Workflow for Subcontractor Invoices