# Workflows 2.0 Transition Guide

Source: https://v2.support.procore.com/product-manuals/workflows-company/tutorials/workflows-transition-guide

---

## Summary

This guide is for anyone looking for guided assistance with transitioning from Procore's Legacy Workflows built by Custom Solutions to the Self-Serve Workflows 2.0 beta. This guide will outline and reference material to be considered and reviewed as well as the appropriate steps to take to have a successful transition.

## Things to Consider

Workflows 2.0 is an application experience that connects with multiple tools including Commitments, Prime Contracts, Change Orders, Subcontractor Invoicing, and more. Workflows 2.0 puts the power of creating custom workflow templates in the hands of the user.

Workflows 2.0 currently does not have complete feature parity with Legacy workflows. However, Workflows 2.0 has capabilities that Legacy Workflows does not have. The following article outlines the differences between the two. Anyone using Legacy workflows (Workflows built by [Procore Custom Solutions](https://support.procore.com/products/online/custom-solutions)) should review the following documents prior to requesting to transition to Workflows 2.0. See [What are the differences between legacy and self-serve workflows?](/faq-what-are-the-differences-between-legacy-and-self-serve-workflows)

### Tool-Specific Reminders for 'Mid-Flight' Items

- **Subcontractor Invoicing, Commitments, Prime Contracts**: Follow all of the steps below which include building your Self-Serve Workflow, assigning it to all active projects, marking it as the tool's default workflow, and configuring on the project level.
- **Subcontractor Invoicing** - Only 'Approved' and 'Approved as Noted' are considered 'finish' statuses for the transition. All other subcontractor invoicing statuses will be considered 'mid-flight' which will trigger the workflow to restart upon selecting the update button in the company-level Workflows tool configuration settings page.

## What steps should I complete before transitioning my workflows:

Procore recommends completing the following steps in order:*Note: Custom Solutions does not assist in the transition without the purchase of Remote Admin Services.*

1. [Create a Custom Workflow Template](/product-manuals/workflows-company/tutorials/create-a-workflow-template).
2. [Assign a Custom Workflow Template to a Project](/product-manuals/workflows-company/tutorials/assign-a-workflow-template-to-a-project).
3. [Configure a Custom Workflow Template on a Project](/product-manuals/workflows-company/tutorials/configure-a-workflow-template-on-a-project).
4. [Set a Default Custom Workflow Template on a Project](/product-manuals/workflows-company/tutorials/configure-a-workflow-template-on-a-project).
5. Test Workflows 2.0 in a [Sandbox Environment](https://developers.procore.com/documentation/development-environments).  
   *Note: This step is highly recommended and strongly encouraged.*
6. Complete steps 1-4 for each active project in your regular Procore environment (Not the Sandbox).  
   *Note: If you do not complete this step for each active project that has a mid-flight workflow, your new custom workflows will NOT be applied to the items that had legacy workflows applied.*
7. Review the following article and understand the differences between Legacy and Workflows 2.0. See [What are the differences between legacy and self-serve workflows?](/faq-what-are-the-differences-between-legacy-and-self-serve-workflows)
8. [Transition your Company to Self-Serve Workflows](/product-manuals/workflows-company/tutorials/request-self-serve-workflows-transition).  
   *Note: Once the request has been made, a product manager will reach out to you to confirm the request within 5 business days.*
9. After the request is approved, click the **Update** button from the company level Workflows tool configuration settings page.

Once you click update and confirm, the following will happen to existing items with a Legacy workflow:

**Finished Items v1 Legacy Workflow** - (Approved, Void/Terminated Status) - These items will not be impacted by the transition.

**Mid-Flight Items that had a Legacy Workflow** - Any item not in a finished state will revert back to the first step of the Self-Serve workflow assuming the self-serve workflow was created, configured, and marked as the default workflow prior to transitioning (See steps above). If no Self-Serve workflow was applied, then the mid-flight item will revert to a 'Draft' status. Self-serve workflows can only be applied to new items moving forward.

## Notes for After Transition

**Reporting**:

- Workflows 2.0 has reporting functions similar to Legacy Workflows available through Enhanced Reporting. However, field names have changed. See [Enhanced Reporting](https://support.procore.com/tc/procore/Legacy/Release%5FDocumentation%5FArchives/2022/Reports:%5FEnhanced%5FReporting%5Ffor%5FWorkflows).

**PDF Exports**:

- Workflow history (Legacy or Self-Serve) is available for select tools with assistance from Procore's Custom Solutions team. If you had a previous custom PDF with the workflow history, it will carry over for the following supported tools:

  - Commitments (Purchase Orders and Subcontracts)
  - Prime Contracts
  - Subcontractor Invoicing
  - Change Orders - 1 Tier & 2 Tier

**APIs**:

- The Self-Serve Workflows API is in a Closed Pilot and is only available to test by request. The timeline for the API Open Beta is TBD.