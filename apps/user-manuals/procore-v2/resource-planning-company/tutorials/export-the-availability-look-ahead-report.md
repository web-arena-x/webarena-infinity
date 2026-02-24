# Export the Availability Look-Ahead Report

Source: https://v2.support.procore.com/product-manuals/resource-planning-company/tutorials/export-the-availability-look-ahead-report

---

## Background

When planning resource assignments, you can export reports that help you understand the availability of your resources. The Availability Look-Ahead report displays what people are currently available for assignments, as well as the date that people with current assignments become available for new assignments.

## Things to Consider

- [Required User](/product-manuals/resource-planning-company/permissions) [Permissions](/product-manuals/resource-planning-company/permissions)
- Only people with a job title are included in the Availability Look-Ahead report.
- People listed in the report are grouped by job title.
- The information in the report reflects your access to information in Resource Planning.
- Supported File Formats:

  - Comma Separated Values (CSV)
  - Portable Document File (PDF)

## Prerequisites

- [Configure Job Titles for Resource Planning](/product-manuals/resource-planning-company/tutorials/configure-job-titles-for-resource-planning)

## Steps

1. Navigate to the Company level **Resource Planning** tool.
2. Click **Reports** and select **Availability Look-Ahead.**
3. Select the **Job Titles** you want to see availability for.
4. Configure your report:

   - **How many assignments out would you like to show?** Select whether to show **1**, **2**, or **3** assignments per person.
   - **Assignment Column(s) Color.** Select the color to differentiate the assignments in the report.
   - **What format would you like for people's names?** Select the format to display the person's name.
   - **Display employees' employee number?** Move the toggle to the **ON** position to display the employee number in the report.
   - **Display employees' job title?** Move the toggle to the **ON** position to display the job title in the report.
   - **For each assignment, what columns would you like to display?** Mark the checkboxes to display the following information in the report:

     - **Project Name.** The project name.
     - **Project Number.** The project number.
     - **Assignment Start Date.** The assignment start date.
     - **Assignment End Date.** The assignment end date.
     - **Assignment Duration.** The duration of the assignment.
     - **Assignment Status.** The assignment's status.
     - **State/Province.** The state or province of the employee.
     - **Role.** The person's job title.
   - **Would you like to show a 'Available After' date for each resource?** Move the toggle to the **ON** position to display next date the person is available to be assigned.
   - **Sort Job Titles by soonest 'Available After' date?** Move the toggle to the **ON** position to sort job titles by the soonest 'Available After' date.
5. Click the **export**  icon, then select to download a **PDF** or **CSV**.

   - If exporting a PDF, select the **page orientation** and **paper size**.
6. Click **Export PDF** or **Export CSV**.

   - *Note:* If a report does not immediately download, you can check the status by navigating to **Reports** and **Queued Downloads**.