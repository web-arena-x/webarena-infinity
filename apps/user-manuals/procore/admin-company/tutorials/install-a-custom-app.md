# Install a Custom App

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/install-a-custom-app

---

## Background

As a company administrator, you have the ability to add install a custom App in a company in Procore.

## Things to Consider

- **Required User Permissions**

 - 'Admin' level permissions on the Company level Directory tool.

## Steps

### Install an App

1. Navigate to the Company level **Admin** tool.
2. Under 'Company Settings', click **App Management**.
3. Click **Install App** and choose **Install Custom App**.
4. Enter the 36-character 'App Version ID' provided to you by the custom App developer.
5. Click **Install**.
6. Click **Install** again to confirm the installation.
7. If you want to create an App configuration now for this App and apply it to one or more projects, or configure it globally, continue with the steps outlined below. Otherwise, click **Skip**.

   1. Use the **Projects** dropdown to select the projects you want to apply the App configuration to. You can choose **Select All** if you want to apply the configuration to all projects in the company.

      - Note: If you want to configure the App globally with the same configuration settings across all projects in your company, click **Add to Active and Future Projects**.
   2. Enter a **Title** for the new App configuration.
   3. Enter values for any required or optional 'Configurable Fields'.
   4. Click **Create**.

To learn more about App configurations, see [What are App Configurations and how do I work with them?](/faq-what-are-app-configurations)

### Configure Permissions for a Data Connection App

If the app you're installing is listed as a Data Connection app, continue with the steps below.

##### To enable permissions for the app on some projects

1. After installing the app, navigate to the **App Management** tool from the **Select an App** menu in Procore.
2. Click **View** next to the app you're configuring.
3. Click the **Permissions** tab.
4. Select the project(s) the app will be available in from the **Permitted Projects** drop-down menu.
5. Click **Add.**

##### to enable permissions for the app on all current and future projects

1. Once the integration is installed, go to the Company Level **Permissions** tool.
2. Click the **Projects Permissions Template** tab.
3. Create a **Global** permission template that provides the permissions the app lists as required. See [Create Permission Template](/product-manuals/permissions-company/tutorials/create-a-project-permissions-template) for detailed instructions. 
   *Note: It's best to name the permission template with the app's name to easily identify it.*
4. Go to the Company level **Directory.**
5. Search for the app name to locate its "user" account in the Directory.
6. Click **Edit** next to the user account.
7. In the permissions area of the user record, click the **Select Default Permission Template** option.
8. Choose the template you've set up for the app, then click **Apply**. 
   *Note: Do NOT manually adjust permissions for the app's user account in the permissions grid in the Company Directory tool. A permission template must be applied.*
9. Next, mark the checkbox for **Add [app-user-name] to all new projects**. 
    This setting will add the âApp Userâ to all new Procore projects moving forward.
10. To add the âApp Userâ to existing projects, click **Add All** next to **Projects this user does not belong to**.
11. Click **Save.**

## Next Steps

- [Create an App Configuration and Apply it to Projects](/product-manuals/home-project/tutorials/configure-app-in-project)