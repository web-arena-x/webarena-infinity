# Create Custom Incident Statuses

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/create-custom-incident-statuses

---

## Background

In incident management, the status field is essential for tracking the progress of each incident as it moves through review and resolution.

## Things to Consider

- [Required User Permissions](/product-manuals/incidents-project/permissions)
- **Additional Information:**

 - All custom statuses are mapped to a **Global Status,** which dictates the core system behavior for an incident. You must map every custom status you create to one of the three Global Statusesâ**Draft**, **Open**, or a **Closed** status.
 - Mapping to **Draft** or **Open** keeps the incident active and editable, while mapping to either **Closed-successful** or **Closed-unsuccessful** will finalize and lock the incident.

## Steps

1. Navigate to the company level **Admin** tool. 
   This reveals the Company Settings page.
2. Under 'Tool Settings,' click **Incidents**.
3. Within the Incidents Settings, locate and click **Statuses**:

   - Click **Add Status**.
   - Enter a name for the new custom status (ex., Investigation or In Review.)
   - Select the **Global Status** to map your custom status to.
   - Click **Create**. 
     Your custom status is now added to the list.