# Create Your Company's Default Work Breakdown Structure

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/create-your-companys-default-work-breakdown-structure

---

## Background

When you are setting up your Work Breakdown Structure for the first time, you have a choice between using the default budget code and structure that comes with Procore or you can customize this structure to create your own company level WBS. This tutorial provides you with an overview of the the steps you take to customize Procore's default WBS for your company's Procore account. If you are customizing your WBS, you'll want to complete this step before customizing your WBS for your individual projects.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

## Prerequisites

- Your company's Procore account must first receive the Work Breakdown Structure update.

## Steps

When getting started with WBS, you can use Procore's default WBS or you can add custom segments. The steps below assume you want to add custom segments to your company's budget code structure.

1. Create your custom 

   A *segment* is a discrete category that an organization uses to break down its work into manageable components. In Procore's Work Breakdown Structure, segments are the building blocks for creating your company's budget code structure.

   Segment and add custom 

   A *segment item* is a member component of a segment. In Procore's Work Breakdown Structure, a segment item is always created within a segment.

   Segment Item[s](/glossary-of-terms) as follows:

   - [Add Custom Segments](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments)
   - [Add Segment Items](/process-guides/company-administration-work-breakdown-structure-guide/add-segment-items)
2. If you need to make changes to your segments, it is recommended that you do that now:

   - [Edit Custom Segment Settings](/process-guides/company-administration-work-breakdown-structure-guide/edit-custom-segment-settings)
   - [Edit Segment Items](/process-guides/company-administration-work-breakdown-structure-guide/edit-segment-items)
   - [Delete Custom Segments](/process-guides/company-administration-work-breakdown-structure-guide/delete-custom-segments)
3. If you want to add custom segment items to your default segments, do the following:

   - [Add Company Cost Codes](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-codes)
   - [Add Company Cost Types](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-types)

     ##### Â Tips

     **Want to view your cost codes and cost types?** To view your existing cost code and cost type segment settings, see:

     - [View Company Cost Code Segment Settings](/process-guides/company-administration-work-breakdown-structure-guide/view-the-company-cost-code-segment-settings)
     - [View Company Cost Type Segment Settings](/process-guides/company-administration-work-breakdown-structure-guide/view-the-company-cost-types-segment-settings)

     **How do we manage 'Sub Jobs'?** You can enable the optional 'Sub Job' segment in the Company level Admin tool. See [Enable Sub Jobs for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects). However, in WBS, the 'Sub Job' segment is managed in the Project level Admin tool. You can add sub jobs as you would add any other segment item. To learn how, see [Add Segment Items to a Project](/process-guides/project-administration-work-breakdown-structure-guide/add-segment-items).

- Now that your segments appear as you want them, you can configure your company's budget code structure as follows:

 - [Arrange the Company Budget Code Structure](/process-guides/company-administration-work-breakdown-structure-guide/set-company-budget-code-structure)

## Next Step

- [Create Your Project's Work Breakdown Structure](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/create-your-projects-wbs)