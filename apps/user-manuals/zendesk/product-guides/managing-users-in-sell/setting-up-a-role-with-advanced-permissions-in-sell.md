# Setting up a role with advanced permissions in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408825410458-Setting-up-a-role-with-advanced-permissions-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on Sell Professional plans and above](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_ee.png)

A role determines what users can do with lead, contact, or deal in Sell. Roles are helpful if you are setting up multiple users with the same permissions. For example, if you have a Business Development team, you might want all members on that team to have exactly the same permissions.

On Professional and Enterprise plans, you can create custom roles, where you specify how users assigned this role can view, create, and manage their own, and other users' records in Sell. These options can be set separately for leads, contacts, and deals. You can assign any number of users to a role.

You need admin rights to work with roles.

You must [enable advanced permissions](https://support.zendesk.com/hc/en-us/articles/4408819704474) to create and use these custom roles in Sell.

This article contains the following topics:

- [Creating a role with advanced action and hierarchy permissions](#topic-1__ul_odm_vs1_g4b)
- [Updating a role](#topic-1__section_n2m_vs1_g4b)
- [Deleting a role](#topic-1__section_q2m_vs1_g4b)

Related articles:

- [Assigning a user to a role](https://support.zendesk.com/hc/en-us/articles/4408824231066)
- [Understanding advanced permissions in Sell](https://support.zendesk.com/hc/en-us/articles/4408819704474)

## Creating a role with advanced action and hierarchy permissions

Each time you add a new user, you can assign them to the custom role you have already created, instead of setting their permissions individually.

When you have created a [user hierarchy](https://support.zendesk.com/hc/en-us/articles/4408824266522), you can create roles, based on the team structure defined in the user hierarchy.

**To set up a new role**

1. Click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then go to **[Manage > Users](https://app.futuresimple.com/permissions)**.
2. Open the **Roles** tab. Note: This tab is visible only after you have set up a [user hierarchy](https://support.zendesk.com/hc/en-us/articles/4408824266522).
3. Click **New role**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_role_create.png)
4. In **Create a new role**, specify a name for the role (for example, *Inside Sales*), and an optional description to explain what the role covers. This benefits the other admins on your account.

   Choose a meaningful role name, so that you can easily identify it when you assign the role to a user.
5. In **Configure permissions**, there are five permissions groups for leads, contacts, and deals, which deal with what a user can do with their own, *peer*, *subordinate*, or *manager* records. These terms all correspond to the user's position in the [user hierarchy](https://support.zendesk.com/hc/en-us/articles/4408824266522). Consider what permissions you want for your user:
   - View: the user has read-only access (this is the most restrictive permission type and a user can't comment on or amend a record in any way)
   - Add: the user can enter a new lead, contact, or deal to Sell
   - Update: the user can perform a large range of actions, including the ability to:
     - Edit fields
     - Move deals through stages, move leads to statuses
     - Add notes, add log activities, set up appointments
     - Communicate, (send emails, make calls, send text messages)
     - Add and remove documents, add and remove products
   - Reassign ownership: the user can, for example, move a deal from one owner to another. They can also convert leads to contacts.
   - Delete: the user has delete access. Use caution when granting delete access. Deals, for example, can't be recovered if they have been deleted.
6. Under **Configure permissions**, open the **Leads** tab. A number of options are available to specify how users with this role can work with leads. The default values are presented for each permission type. Set the role permissions for each type of action:
   - **Can view leads**:
     - Their and subordinates' leads
     - Their, subordinates', and peers' leads
     - Their, subordinates', peers', and manager's leads
     - Same leads as the manager
   - **Can add leads**: select the check box if they can add leads, deselect the checkbox if they cannot add leads.
   - **Can update leads**: select the check box if they can update leads, then define whose leads they can update. Deselect the checkbox if they cannot update leads.
     - Only their and subordinates' leads
     - All leads they can view
   - **Can reassign ownership and convert leads**: select the check box if they can reassign ownership and convert leads, then define whose leads they can do this to. Deselect the checkbox if they cannot.
     - Only their and subordinates' leads
     - All leads they can view
   - **Can delete leads**: select the check box if they can delete leads, then define whose leads they can delete. Deselect the checkbox if they cannot delete leads.
     - Only their and subordinates' leads
     - All leads they can view
7. Open the **Contacts** tab. A number of options are available to specify how users with this role can work with contacts. The default values are presented for each permission type. Set the role permissions for each type of action:
   - **Can view contacts**:
     - Their and subordinates' contacts
     - Their, subordinates', and peers' contacts
     - Their, subordinates', peers', and manager's contacts
     - Same contacts as their manager
   - **Set different permissions for viewing prospects and customers**: select the check box if you differentiate between prospects and customers, then select an action permission:

     Can view prospects and customers

     - Their and subordinates' prospects and customers
     - Their, subordinates', and peers' prospects and customers
     - Their, subordinates', peers', and manager's prospects and customers
     - Same prospects and customers as their manager
   - **Can add contacts**: select the check box if they can add contacts, deselect the check box if they cannot add contacts.
   - **Can update contacts**:
     - Only their and subordinates' contacts
     - All contacts they can view
   - **Can reassign ownership of contacts**:
     - Only their and subordinates' contacts
     - All contacts they can view
   - **Can delete contacts**:
     - Only their and subordinates' contacts
     - All contacts they can view
8. Open the **Deals** tab. A number of fields are available to specify how users with this role can work with deals. The default values are presented for each permission type. Set the role permissions for each type of action:
   - **Can view deals**:
     - Their and subordinates' deals
     - Their, subordinates', and peers' deals
     - Their, subordinates', peers', and manager's deals
     - Same deals as their manager
   - **Can add deals**: select the check box if they can create deals, deselect the check box if they cannot make deals.
   - **Can update deals**:
     - Only their and subordinates' deals
     - All deals they can view
   - **Can reassign ownership of deals**:
     - Only their and subordinates' deals
     - All deals they can view
   - **Can delete deals**:
     - Only their and subordinates' deals
     - All deals they can view
9. Click **Save** to create the new role.
10. In **User Management > Roles**, you'll see the new role with a column showing the number of users assigned to that role. When you first create the role, the assigned user count is 0.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_role_overview.png)

You are now ready to [add users to the role](https://support.zendesk.com/hc/en-us/articles/4408824231066).

## Updating a role

You can update an existing role from the **Roles** tab. Note: If you update settings in a role, then as soon as you save your changes, the updates are applied to all users that are assigned to that role. You can see the users assigned to the role if you hover over the users assigned text above **Save**.

**To update a role**

1. Click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select **[Manage > Users](https://app.futuresimple.com/permissions)**.
2. Open the **Roles** tab.
3. Click the name of the role that you want to update.
4. Edit the name, description, or permissions that you want to change.
5. Click **Save**.

   Your updates are applied to all users assigned to that role.

## Deleting a role

You can delete an existing role from the **Roles** tab. Note: You can't delete a role if there are users assigned to that role. To proceed, you must either assign the users to a new role, or unassign them and set up their permissions manually. Then you can delete the role.

**To delete a role**

1. Click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select **[Manage > Users](https://app.futuresimple.com/permissions)**.
2. Open the **Roles** tab.
3. Click the name of the role that you want to delete and check the assigned users column to ensure there are no users assigned to this role. You must remove the role from any users before you can delete the role.If you hover over the number in the assigned users column, you can see the names of any users assigned to the role.
4. Click **Delete this role**. You'll only see this option if you have no users assigned to the role.
5. Click **Delete** to confirm that you want to delete the role.

   The role is deleted and can't be retrieved.