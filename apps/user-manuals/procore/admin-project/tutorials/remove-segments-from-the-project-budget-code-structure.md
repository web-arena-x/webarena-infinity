# Remove Segments from the Project Budget Code Structure

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/remove-segments-from-the-project-budget-code-structure

---

## Background

You can remove a custom segment from your project level budget code structure, as long as there are no budget codes using that segment on your project.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Project level Admin tool.
- **Additional Information:**

 - You can only remove a custom segment from the project level budget code structure if there are no budget codes using that segment on the project.
 - You cannot remove a custom segment from the company level budget code structure.
 - To learn how the company and project level budget code structures interact, see [What happens to projects when I change the segment order of my company's budget code structure in WBS?](/faq-what-happens-to-projects-when-i-change-the-segment-order-of-my-companys-budget-code-structure-in-wbs)
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

## Prerequisites

- [Add Custom Segments to the Project's Budget Code Structure](/process-guides/project-administration-work-breakdown-structure-guide/add-custom-segments-to-the-project-budget-code-structure)

## Steps

1. Navigate to the Project level **Admin** tool.
2. Under 'Project Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, right-click the vertical ellipsis and choose the **Remove from Budget Code Structure** menu option.   
      
      
      
    Procore removes the selected budget code from the project's 'Budget Code Structure' section.