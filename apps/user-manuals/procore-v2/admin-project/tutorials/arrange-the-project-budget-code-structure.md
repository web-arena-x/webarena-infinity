# Arrange the Project Budget Code Structure

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/arrange-the-project-budget-code-structure

---

## Background

Your company's Procore Administrator can enable a setting that allows users with the required user permissions to arrange the segments in a project's budget code structure in any order you want. Because editing a project's budget code structure permanently disconnects it from the company's budget code structure, you should only use this setting when a project requires a unique budget code structure.

## Things to Consider

- **Required User Permissions:**

One of the following:

- 'Admin' level permissions on the Project level Admin tool.
- 'Read Only' or 'Standard' level permissions on the Project level Admin tool with the ['Manage WBS Codes' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

## Prerequisites

- [Enable Project Level Budget Code Structure Edits](/process-guides/company-administration-work-breakdown-structure-guide/enable-project-level-budget-code-structure-edits)

## Steps

1. Navigate to the Project level **Admin** tool.
2. In the right pane, click the **Work Breakdown Structure** link.
3. In the 'Budget Code Structure' section, click the **Edit** button.
4. At the 'Edit Budget Code Structure' window, read the message.

   ##### Â Important

   If you choose to edit a project's budget code structure, be aware that the edit action permanently disconnects the project from the company's budget code structure. Any changes that you make to the project will only apply to that project. In addition, all changes made to the company's budget code structure will have NO effect on the project's budget code structure in the future.

- If you want to proceed, click **Edit**.
- In the 'Segment Order' table, click and hold the double grip and then use a drag-and-drop operation to place each segment in the desired position. The 'Order' area reflects the segment order you define for your project's budget code structure.
- Click **Save**.

##### Â Tip

**Did you know you can customize the budget code descriptions for your project?** Customization is useful when your team wants to create two or more descriptions for a single budget code. Customization can also improve the readability of your codes on financial line items for your end users. To learn more, see [Why and how do I create a custom budget code description for Procore's Project Financials tools?](/faq-why-and-how-do-i-create-a-custom-budget-code-description-for-procores-project-financials-tools)