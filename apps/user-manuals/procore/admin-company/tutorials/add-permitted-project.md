# Add a Permitted Project to a Data Connection App

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/add-permitted-project

---

## Background

Company administrators can manage the list of permitted projects for a data connection App. The App is only allowed to run in permitted projects using the permissions defined in the DMSA.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' on the Company Admin tool.

## Steps

1. Log in to Procore and navigate to the Company Admin tool.
2. In right side panel, select **App Management** under Company Settings.
3. On the App Management page, locate the data connection App you want to add permitted projects to and click **View**.
4. Click the Permissions tab.
5. Select one or more projects in the permitted projects drop-down and click **Add**.

### Add All New Projects as Permitted Projects

You can configure the Company Directory settings for the DMSA account so that all new projects created in the company will be added as permitted projects.

1. Once the integration is installed, go to the Company Level **Permissions** tool.
2. Click the **Projects Permissions Template** tab.
3. Create a **Global** permission template that provides the permissions the app lists as required. See [Create Permission Template](/product-manuals/permissions-company/tutorials/create-a-project-permissions-template) for detailed instructions. *Note: It's best to name the permission template with the app's name to easily identify it.*
4. Go to the Company level **Directory.**
5. Search for the app name to locate its "user" account in the Directory.
6. Click **Edit** next to the user account.
7. In the permissions area of the user record, click the **Select Default Permission Template** option.
8. Choose the template you've set up for the app, then click **Apply**.
9. Next, mark the checkbox for **Add [app-user-name] to all new projects**. This setting will add the âApp Userâ to all new Procore projects moving forward.
10. To add the âApp Userâ to existing projects, click **Add All** next to **Projects this user does not belong to**.
11. Click **Save** at the bottom fo the page.

### Add Existing Current Projects as Permitted Projects

You can configure the Company Directory settings for the DMSA account so that one or more existing current projects in the company will be added as permitted projects.

1. Go to the Company Level **Permissions** tool.
2. Click the **Projects Permissions Template** tab.
3. Create a **Global** permission template that provides the permissions the app lists as required. See [Create Permission Template](/product-manuals/permissions-company/tutorials/create-a-project-permissions-template) for detailed instructions. 
   *Note: It's best to name the permission template with the app's name to easily identify it.*
4. Navigate to the Company Directory tool.
5. Locate the directory user associated with the DMSA application, then click **Edit**.
6. In the permissions area of the user record, click the **Select Default Permission Template** option.
7. Choose the template you've set up for the app, then click **Apply**.
8. Next, mark the checkbox for **Add [app-user-name] to all new projects**. This setting will add the âApp Userâ to all new Procore projects moving forward.
9. Scroll down to the Current Project Settings section and click **Add All** to add all existing current projects as permitted projects, or click **Add** for one or more individual projects as needed.
10. Click **Save** at the bottom of the page.