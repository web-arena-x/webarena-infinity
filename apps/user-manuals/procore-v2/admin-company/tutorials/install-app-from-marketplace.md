# Install an App from the Procore Marketplace

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/install-app-from-marketplace

---

## Background

As a company administrator, you have the ability to install an App from the [Procore Marketplace](https://marketplace.procore.com/) to your company in Procore. You can install an App while you are in Procore, or install one directly from the Marketplace. There are two types of apps that can be installed:

- **Data Connection (DMSA) app.** This type of app will require the configuration of a permission template for the DMSA "user" in the Company Level Directory to allow the app to function as intended on all projects.
- **Embedded (Auth code) app.** No additional permission configurations are required for this type of app.

You can see whether you've installed a data connection or embedded app when viewing your company's list of installed apps in the App Management tool.

##### Â Note

Some apps may have both **Data Connection** and **Embedded** listed as the app type in the App Management tool. In this case, you need to follow configuration steps for a **Data Connection** app.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Directory tool.

## Steps

### Install an App

1. Navigate to the [Procore Marketplace](https://marketplace.procore.com/).
2. Click **Log In**. Enter your Procore credentials and click **Log In** again. 
    If you are a Company Admin in more than one company, you will be prompted to select the company you want to install the App in.
3. Navigate to and click the tile for the App you want to install.
4. Click **Install App**.
5. Click **Install** to confirm your selection. You are guided through the remaining installation steps.

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