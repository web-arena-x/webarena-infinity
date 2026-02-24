# How do I add people to the submittal workflow? - Procore

Source: https://support.procore.com/faq/how-do-i-add-people-to-the-submittal-workflow

---

## Answers

Procore's submittal workflow model provides your users with more flexibility when setting the approval path for a submittal. This deployment is complete and the new model prevents project users with 'Admin' level permission on the Submittals tool from having to specifically configure the tool to use [sequential approval](../references/construction-management/glossary-of-terms.md#Sequential_Approval) or [parallel approval](../references/construction-management/glossary-of-terms.md#Parallel_Approval). A new submittal workflow table has been implemented on all Procore accounts and allows your users to create and edit submittals that use either sequential, parallel, or a combination of both approval models:

- [How to add people to a submittal workflow](#How_to_add_people_to_a_submittal_workflow "How do I add people to the submittal workflow?")
- [How to add people for sequential approval](#How_to_add_people_for_sequential_approval "How do I add people to the submittal workflow?")
- [How to add people for parallel approval](#How_to_add_people_for_parallel_approval "How do I add people to the submittal workflow?")
- [How to manage submittal workflow templates](#How_to_manage_submittal_workflow_templates "How do I add people to the submittal workflow?")

### How to add people to a submittal workflow

If you want a step in the new submittal workflow to use sequential approval, add only one (1) user to each line item in the workflow. You can add multiple steps to a workflow and each line step will be processed by Procore in sequential order. If you want a step in the new submittal workflow to use parallel approval, simply add two (2) or more users to that step. In the example below, there are three (3) sequential approval steps, but the third step has two (2) users in parallel. When a step is processed in parallel, all members of the group must submit a response before the [Ball In Court](../references/construction-management/glossary-of-terms.md#Ball_In_Court "Glossary of Terms") responsibility shifts to the next step unless all members marked as 'Required' have responded.

![demo-sequential-parallel.gif](https://support.procore.com/@api/deki/files/47551/demo-sequential-parallel.gif?revision=1)

### How to add people for sequential approval

If you want the submittal workflow to use sequential approval, add only one (1) user to each line item in the workflow. You can add multiple line items to a workflow and each line item will be processed by Procore in sequential order. The following example shows you how to create a sequential approval workflow that includes one (1) line item on a workflow that contains four (4) members total.

![demo-sequential-workflow.gif](https://support.procore.com/@api/deki/files/47552/demo-sequential-workflow.gif?revision=1)

### How to add people for parallel approval

If you want to use parallel approval on a submittal, add two (2) or more people to a line item. You can add multiple line items to a workflow and each line item will be processed by Procore in sequential order. The following example shows you how to create a parallel group of approvers.

![demo-parallel-only.gif](https://support.procore.com/@api/deki/files/47550/demo-parallel-only.gif?revision=1)

### How to manage submittal workflow templates

If you are a user with 'Admin' level permission to a project's Submittals tool, you can create submittal workflow templates in the 'Submittal Workflow Templates' page of the **Configure Settings** area. See [Manage Submittal Workflow Templates](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/manage-submittal-workflow-templates "Manage Submittal Workflow Templates"). Your submittal creators can choose one (1) of these templates in the 'Select a Template' drop-down list on the create and edit submittal page. After a template is applied to a submittal, the membership, role, and days to submit/respond values can be customized on a submittal-by-submittal basis. See [Apply a Submittal Template to a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/apply-a-submittal-workflow-template-to-a-submittal "Apply a Submittal Workflow Template to a Submittal").

![demo-submittal-workflow-templates.gif](https://support.procore.com/@api/deki/files/52674/demo-submittal-workflow-templates.gif?revision=1)

## See Also

- [Create a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal "Create a Submittal")
- [Manage Submittal Workflow Templates](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/manage-submittal-workflow-templates "Manage Submittal Workflow Templates")
- [Apply a Submittal Workflow Template to a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/apply-a-submittal-workflow-template-to-a-submittal "Apply a Submittal Workflow Template to a Submittal")

## 

If you would like to learn more about Procore's submittals management software and how it can help your business, please visit our [construction submittals software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/submittals "https://www.procore.com/project-management/submittals").