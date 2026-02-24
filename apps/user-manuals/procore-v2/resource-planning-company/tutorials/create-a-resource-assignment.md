# Create Resource Assignments

Source: https://v2.support.procore.com/product-manuals/resource-planning-company/tutorials/create-a-resource-assignment

---

## Background

Assignments allow you to manage your resources by assigning resources to projects. Assignments can also be used for forecasting and planning future work. You can keep these assignments private until you are ready to notify the assignee or other members of your team.

You can bulk create assignments with the new Assignments Gantt. You can also make assignments to fill resource requests. See [Fill a Resource Request](/product-manuals/resource-planning-company/tutorials/fill-a-resource-request).

## Things to Consider

- [Required User](/product-manuals/resource-planning-company/permissions) [Permissions](/product-manuals/resource-planning-company/permissions)
- You can manage user visibility of assignments with assignment request statuses. See [Configure Assignment Request Statuses for Resource Planning](/product-manuals/resource-planning-company/tutorials/configure-assignment-and-request-statuses-for-resource-planning).
- Linked users  that are given resource assignments are automatically added to the project.
- When equipment is assigned a Resource Assignment from the Assignment Gantt (Beta), it is automatically added to the project.
- **Timesheets** **Show/Hide Details**

  - If creating a Timesheet for a user with an assignment, their start and stop times are automatically filled in to the timesheet based on their assignment in Resource Planning.
  - Data syncing between Resource Planning and Procore is required. See [What is Data Syncing for Resource Planning?](/faq-what-is-data-syncing-for-resource-planning)
  - Assignees must be 'Users' in Procore, and not 'Contacts'. See [What people information is synced between Resource Planning and the Procore Company Directory?](/faq-what-people-information-is-synced-between-resource-planning-and-the-procore-company-directory)

## Steps

You can create resource assignments from the following places:

- [Assignments Boards](#create-a-resource-assignment-from-the-assignments-boards)
- [Assignments Gantt](#create-a-resource-assignment-from-the-assignments-gantt)
- [Assignments Gantt (Beta)](#create-resource-assignments-from-the-assignments-gantt-beta)
- [Assignments List](#create-a-resource-assignment-from-the-assignments-list)

##### Â Tip

You can **bulk create assignments** using the Assignment Gantt (Beta).

## Create a Resource Assignment from the Assignments Boards

On the Assignments Boards, you can create a resource assignment the in following ways:

- The 'New' Button
- Drag and Drop from the Resource Bench

##### Create a Resource Assignment with the 'New' Button

1. Navigate to the Company level **Resource Planning** tool.
2. Click **Assignments** and select **Assignments Boards**.
3. Click **New**.
4. Complete the assignment information. **Show/Hide Fields**

   - **Project.** The project that the assignment is for.
   - **Person.** The assignee.
   - **Category**. The category for the assignment.
   - **Subcategory**. The subcategory for the assignment.
   - **Status**. The assignment status.
   - **Working Days**. The working days needed for the Assignment.
   - **Tags**. The tags for the assignment. See [Configure Tags for Resource Planning](/product-manuals/resource-planning-company/tutorials/configure-tags-for-resource-planning)[.](/process-guides/resource-planning-setup-guide/what-are-tags)
   - **Start Day**. The date the work assignment starts.

     - **Date**. The specific start date for the assignment.
     - **Project Start**. If the assignment starts on the same date as the project, select the project start date.
   - **End Day**. The date the work assignment ends.

     - **Date**. The specific end date for the assignment.
     - **Weeks**. How many weeks the assignment is for.
     - **Project End**. If the assignment ends on the same date as the project, select the project end date.
   - **Allocation Type**. Whether the Allocation Type is in **Hours** of **Percent**. See [What is a Resource Allocation Type?](/faq-what-is-a-resource-allocation-type)

     - **Work Hours Start**. If you selected 'Hours', enter the time of day the assignment begins.
     - **Work Hours Start**. If you selected 'Hours', enter the time of day the assignment ends.
     - **Percent.** If you selected 'Percent', enter the percent allocated to the assignment
   - **Overtime**. Mark this checkbox to allow overtime for any time that goes over the allotted paid hours per shift.
5. Click **Save** to save the assignment.  
   OR  
   Click the **caret**  icon and select **Save and Alert** to save the assignment and send an Assignment Alert to the assignee.

##### Create a Resource Assignment using Drag and Drop

1. Navigate to the Company level **Resource Planning** tool.
2. Click **Assignments** and select **Assignments Boards**.
3. Locate your 'Resource Bench'. See [What is the 'resource bench' in Resource Planning?](/faq-what-is-the-resource-bench-in-resource-planning)
4. Locate the person you want to assign. See [Search, Sort, and Filter People on the Assignments Boards](/product-manuals/resource-planning-company/tutorials/search-sort-and-filter-people-on-the-assignments-boards).
5. From the 'Resource Bench', use a drag-and-drop operation to move the assignee's name to the project. See [What is the 'resource bench' in Resource Planning?](/faq-what-is-the-resource-bench-in-resource-planning)
6. Complete the assignment information. **Show/Hide Fields**

   - **Project.** The project that the assignment is for.
   - **Person.** The assignee.
   - **Category**. The category for the assignment.
   - **Subcategory**. The subcategory for the assignment.
   - **Status**. The assignment status.
   - **Working Days**. The working days needed for the Assignment.
   - **Tags**. The tags for the assignment. See [Configure Tags for Resource Planning](/product-manuals/resource-planning-company/tutorials/configure-tags-for-resource-planning)[.](/process-guides/resource-planning-setup-guide/what-are-tags)
   - **Start Day**. The date the work assignment starts.

     - **Date**. The specific start date for the assignment.
     - **Project Start**. If the assignment starts on the same date as the project, select the project start date.
   - **End Day**. The date the work assignment ends.

     - **Date**. The specific end date for the assignment.
     - **Weeks**. How many weeks the assignment is for.
     - **Project End**. If the assignment ends on the same date as the project, select the project end date.
   - **Allocation Type**. Whether the Allocation Type is in **Hours** of **Percent**. See [What is a Resource Allocation Type?](/faq-what-is-a-resource-allocation-type)

     - **Work Hours Start**. If you selected 'Hours', enter the time of day the assignment begins.
     - **Work Hours Start**. If you selected 'Hours', enter the time of day the assignment ends.
     - **Percent.** If you selected 'Percent', enter the percent allocated to the assignment
   - **Overtime**. Mark this checkbox to allow overtime for any time that goes over the allotted paid hours per shift.
7. Click **Save** to save the assignment.  
   OR  
   Click the **caret**  icon and select **Save and Alert** to save the assignment and send an Assignment Alert to the assignee.

## Create a Resource Assignment from the Assignments Gantt

1. Navigate to the Company level **Resource Planning** tool.
2. Click **Assignments** and select **Gantt**.
3. Click **New**.
4. Complete the assignment information. **Show/Hide Fields**

   - **Project.** The project that the assignment is for.
   - **Person.** The assignee.
   - **Category**. The category for the assignment.
   - **Subcategory**. The subcategory for the assignment.
   - **Status**. The assignment status.
   - **Working Days**. The working days needed for the Assignment.
   - **Tags**. The tags for the assignment. See [Configure Tags for Resource Planning](/product-manuals/resource-planning-company/tutorials/configure-tags-for-resource-planning)[.](/process-guides/resource-planning-setup-guide/what-are-tags)
   - **Start Day**. The date the work assignment starts.

     - **Date**. The specific start date for the assignment.
     - **Project Start**. If the assignment starts on the same date as the project, select the project start date.
   - **End Day**. The date the work assignment ends.

     - **Date**. The specific end date for the assignment.
     - **Weeks**. How many weeks the assignment is for.
     - **Project End**. If the assignment ends on the same date as the project, select the project end date.
   - **Allocation Type**. Whether the Allocation Type is in **Hours** of **Percent**. See [What is a Resource Allocation Type?](/faq-what-is-a-resource-allocation-type)

     - **Work Hours Start**. If you selected 'Hours', enter the time of day the assignment begins.
     - **Work Hours Start**. If you selected 'Hours', enter the time of day the assignment ends.
     - **Percent.** If you selected 'Percent', enter the percent allocated to the assignment
   - **Overtime**. Mark this checkbox to allow overtime for any time that goes over the allotted paid hours per shift.
5. Click **Save** to save the assignment.  
   OR  
   Click the **caret**  icon and select **Save and Alert** to save the assignment and send an Assignment Alert to the assignee.

## Create Resource Assignments from the Assignments Gantt (Beta)

*Note:* Users given assignments this way are also added to the project in the company's Directory.

##### Â In Beta

This feature is in beta and available for customers using the Resource Planning tool.

##### Â Tip

You can also create this by [creating a copy](/process-guides/resource-planning-gantt-user-guide/copy-project) of an existing item on the Assignments Gantt.