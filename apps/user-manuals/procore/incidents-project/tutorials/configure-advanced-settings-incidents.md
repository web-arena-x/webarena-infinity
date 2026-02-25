# Configure Advanced Settings: Incidents

Source: https://v2.support.procore.com/product-manuals/incidents-project/tutorials/configure-advanced-settings-incidents

---

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Incidents tool.
- **Additional Information:**

 - Your company's Procore Administrator can also configure other options for the Incidents tool in the Company Admin tool. See [Add Custom Options for Incident Fields](/product-manuals/admin-company/tutorials/add-custom-options-for-incident-fields).

## Prerequisites

- Add the Incidents tool to the project. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).

## Steps

1. Navigate to the project's **Incidents** tool.
2. Click the **Configure Settings** icon.
3. Click one of these options:

- Configurations
- Permissions Table

### Configurations

1. Click **Incidents Settings**.
2. Do the following:

   - **Default Distribution.** Add users to the distribution list who should have access to incidents even if they're not directly involved. This might be useful if you want to grant a user with 'Read-only' or 'Standard' permissions on the Incidents tool access to private incidents without giving them permissions to change the configurations on the tool.
   - **Private by Default**. Mark the checkbox if you would like all incidents you create to be private by default. Private incidents will be available to the creator of the incident and all 'Admin' level users on the Incidents tool.

### Permissions Table

- Click **Permissions Table**.
- Under **Name**, locate the user's name.
- Click the *None*, *Read-Only*, *Standard*, or *Admin* column until a GREEN arrow appears.

 - Access
 - No Access
 - If a gray X appears and you are not able to change a setting, your Procore Administrator is managing permissions using a template. See [Edit a Project Permissions Template](/product-manuals/permissions-company/tutorials/edit-a-project-permissions-template).

 For a list of what users can do at each permission level in Incidents, see the [Permissions Matrix](/product-manuals/incidents-project/permissions).