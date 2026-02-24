# Manage Consolidated Tool Settings

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/manage-tool-settings

---

## Background

The consolidated tool settings page provides easy access to manage all project level tools from a single location. Instead of navigating to each tool and clicking the settings cog, you can visit the consolidated tool settings page to view all tool settings to which you have the required permissions.

- Toggle the tool to 'Active' or 'Inactive' to enable or disable it for use on your project.
- Click into the 'Configure' menu for each tool setting to select which type of setting you want to manage. Then, the relevant settings page for that tool will open in a new browser tab.

The consolidated tool settings page can be accessed through the Project level Admin tool for users with permission to interact with that tool. For users with the permissions required to manage tool settings, but who don't have permissions to the Project level Admin tool, the consolidated tool settings page is accessible from the [Project Overview](/process-guides/about-the-project-overview/) page.

## Things to Consider

- **Required User Permissions**:

 - To access consolidated tool settings from the Admin tool:\* 'Admin' level permissions on the Project level Admin tool.
 - To access consolidated tool settings from the Project Overview for users without 'Admin' level permissions on the Admin tool:

    - The minimum permission level required to modify settings for the tool you want to manage.
- **Considerations:**

 - For tools with Company level configuration options, both Project level and Company level tool settings are accessible from the consolidated Tool Settings page.
 - Visibility of tools and configuration options is dependent on individual user permissions:

    - If a user does not have permissions to configure settings for a tool, that tool will not appear in their list.
    - If a user has permissions to configure some, but not all, settings for a tool, they will only see the settings they have permission to view or manage.
 - The 'Configure' menu next to a listed tool is not shown if there are no configuration settings available for that tool.
 - The option to activate or inactivate a tool appears grayed out and unavailable in the following scenarios:

    - The tool can't be inactivated. For example, the Home tool can't be inactivated because it is the tool users land on when selecting any project.
    - Procore must inactivate the tool on your behalf. For example, inactivating the Change Events tool can impact other financial objects, and so to make sure you don't experience adverse effects, Procore must inactivate this tool on your behalf.
    - The user doesn't have permission to activate or inactivate tools.

## Steps

### Navigate to the Consolidated Tool Settings page:

Do one of the following:

1. For users with 'Admin' level permissions to the Project level Admin tool:

   1. Navigate to the Project level **Admin** tool.
   2. Under **Project Settings**, click **Tool Settings.**
2. For users with 'Admin' level permissions to one (1) or more tools, but who do NOT have permissions to the Project level Admin tool:

   1. Navigate to the **Project Overview.**
   2. Select the ellipse icon and choose **Project Details**.
   3. Click the button labeled **Go to Tool Settings.**

### Configure Tool Settings:

Manage the following from the consolidated Tool Settings page:

- **Activate a tool.** Toggle the switch next to the tool name to turn the tool on or off for your project.
- **Configure settings.** Select an option from the menu to configure settings in the desired area.

 - **Company Settings.** Settings that impact how your Project level tools work, but are configured at the Company level in Procore. These settings typically impact all projects, or their configurations can be assigned to a some projects but not others.
 - **Project Settings.** Settings that are specific to your project, and do not typically impact any other projects within your company.