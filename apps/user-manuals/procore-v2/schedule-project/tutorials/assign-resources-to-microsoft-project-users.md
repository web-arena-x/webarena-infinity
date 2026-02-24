# Assign Resources to Microsoft Project Users

Source: https://v2.support.procore.com/product-manuals/schedule-project/tutorials/assign-resources-to-microsoft-project-users

---

## Background

In Microsoft Project, the Gantt Chart view lets project managers assign 'Resources Names' to tasks on a project schedule. The 'Resource Names' corresponds to the name of the person who is responsible for completing a project task.

If your project has integrated Procore's Schedule tool to work with one of the supported versions of Microsoft Project, the 'Resource Name' information in your project schedule will be uploaded into Procore with any scheduled tasks that includes named resources.   
See [Integrate a Microsoft Project Schedule Using Procore Drive](/product-manuals/procore-drive/tutorials/integrate-a-microsoft-project-schedule-using-procore-drive).

After your Microsoft Project schedule is uploaded successfully, you can use the project's Schedule tool to update the resources imported with your schedule by assigning 'Resources' to specific project users using the Steps below.

Once the resources in your Microsoft Project schedule are assigned to the appropriate Procore users, any scheduled task with a 'Resource Name' in Microsoft Project will now have a Procore user name associated with it. This gives the the 'Schedule Work Log' in the project's Daily Log tool the ability to display the name of the Procore user who is assigned to complete the work.

## Things to Consider

- **Required User Permissions**:

  - 'Admin' on the project's Schedule tool.  
    *Note:* To view or edit information on the Permissions Table page for the Schedule tool, 'Admin' permission to the project's Directory tool is also required.

## Prerequisites

- Prior to uploading the Microsoft Project Schedule, ensure the schedule includes resource assignments on the project's tasks.   
  For instructions, see the Help System for your version of Microsoft Project.
- Before you can complete the steps below, you must upload a MS Project Schedule to the Schedule Tool.   
  See [Integrate a Microsoft Project Schedule Using Procore Drive](/product-manuals/procore-drive/tutorials/integrate-a-microsoft-project-schedule-using-procore-drive).

## Steps

### Assign Resources to Users

1. Navigate to the project's **Schedule** tool.
2. Click **Configure Schedule Settings.**
3. Click **User Permissions.**
4. Next to the desired user(s) in the list, select the desired resource names from the **Resource** drop-down list.  
   *Note*: In order for selections to appear in the drop-down list, your imported Microsoft Project Schedule must include data in the **Resource Names** column.
5. *Optional*: If you want the person assigned as the resource to receive a weekly notification from Procore, mark the **Weekly Resource Email** checkbox.
6. Click **Back** when you're finished.