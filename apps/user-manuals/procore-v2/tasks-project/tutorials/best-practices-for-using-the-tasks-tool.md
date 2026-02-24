# Best Practices for Using the Tasks Tool

Source: https://v2.support.procore.com/product-manuals/tasks-project/tutorials/best-practices-for-using-the-tasks-tool

---

## Background

Procore's Project level Tasks tool gives you the ability to track and manage action items during a construction project's lifespan.

## Things to Consider

- **Required User Permission**:

  - 'Admin' level permission on the Company's Admin tool.

## Steps

To successfully configure Tasks tool, begin by following the steps below.

1. Configure your Permission Templates
2. Set your Categories
3. Enable the Tasks Tool on Projects

#### Configure your Permission Templates

Update your permission templates to include the Tasks tool. We recommend granting all users at least 'Standard' level access to the Tasks tool, so that team members can create tasks and be assigned items.

1. Navigate to the project's **Directory** tool.
2. Locate a user in the Directory list.
3. Click **Edit** next to the user's name.
4. Scroll to the **Project Permissions Templates** drop-down list and select **Do Not Apply a Template**.  
   Choosing this option allows you to define unique permissions for the user.
5. Scroll to the 'Tasks' row and select **Standard.***Note:* Users with 'Admin' level access to the Directory tool will automatically have 'Admin' level access to the Tasks tool.
6. Choose one of the following options:

   - If you want to save the changes without emailing the user about the change, click **Save**.
   - If you want to notify the user of the change, click **Save and Send Notification**.  
     *Note:* This button is only available when the user has previously logged into Procore.
   - If this is a new user and you want to invite them to join Procore, click **Save and Send Invite to Procore**.  
     *Note:* This button is only available when the user has not logged into Procore.

#### Set your Categories

In the Company Admin tool, you can [create categories](/product-manuals/admin-company/tutorials/add-task-categories) to which you can assign tasks within a project.

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Tasks.**
3. Enter the new category into the text box.
4. Click **Create** to add the new category.   
   This category can now be assigned to a project level task.

#### Enable the Tasks Tool on your Project

By default, the **Tasks** tool will be enabled for any existing projects. To ensure the Tasks tool is enabled on future projects, you can enable it in your Standard Project Template by following the steps below.

1. Navigate to your desired project template. See [Configure a Project Template](/product-manuals/portfolio-company/tutorials/configure-a-project-template).
2. Navigate to the project's **Admin** tool.
3. Under **Project Settings**, click **Active Tabs.**  
   *Note*: This reveals a list of tools and their status as active or inactive in the project.
4. Mark the checkbox next to **Tasks** to enable the tool in your project.
5. Click **Update** to save your project settings.