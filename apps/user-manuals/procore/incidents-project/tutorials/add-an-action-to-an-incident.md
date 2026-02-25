# Add an Action to an Incident

Source: https://v2.support.procore.com/product-manuals/incidents-project/tutorials/add-an-action-to-an-incident

---

## Things to Consider

- **Required User Permissions:**

 - *To add an action to any incident:* 'Admin' level permissions on the project's Incidents tool.
 - *To add an action to an incident you created:* 'Standard' level permissions on the project's Incidents tool.
 - *To add an observation to an action:*

    - 'Admin' level permissions on the project's Incidents tool AND 'Standard' or 'Admin' level permissions on the project's Observations tool.
      *Note:* Users with 'Standard' level permissions on the project's Incidents and Observations tools can only add observations to actions on incidents they created.
 - *To detach an observation from an action:*

    - 'Admin' level permissions on the project's Incidents tool. 
      AND 'Standard' or 'Admin' level permissions on the project's Observations tool.
      *Note:* Users with 'Standard' level permissions on the project's Incidents and Observations tools can only detach observations they created.
- **Additional Information:**

 - An observation created from an action can only be detached from an action in the Incidents tool. To delete an observation created from an action, see [Delete an Observation](/product-manuals/observations-project/tutorials/delete-an-observation).

## Prerequisites

- [Create an Incident](/product-manuals/incidents-project/tutorials/create-an-incident)

## Steps

1. Navigate to the project's **Incidents** tool.
2. Click the **Incidents** tab.
3. Click **View** next to the incident you want to add an action to.
4. Scroll to **Actions** and click **Add Action**.
5. Select an **Action** **Type**. The default type selections in Procore are *Corrective* and *Preventative*. 
   *Note:* Additional type options can be added in the Company Admin tool. See [Add Custom Options for Incident Fields](/product-manuals/admin-company/tutorials/add-custom-options-for-incident-fields).
6. **Description.** Enter any information you want to add to the action's record.
7. **Attachments**. Attach any files you want to add to the action's record.
8. Click **Create**.
9. *Optional:* Click **Create Observation** and select the observation type.   
   This redirects you to the 'New Observation' page in the Observations tool where you can assign and track the action. Consider the following:

   - Fieldsets configured for the Observations tool will be respected. See [Create New Configurable Fieldsets](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets).
   - An observation cannot be deleted from within the Incidents tool. You can only detach an observation from an action in the Incidents tool. To delete an observation, see [Delete an Observation](/product-manuals/observations-project/tutorials/delete-an-observation).