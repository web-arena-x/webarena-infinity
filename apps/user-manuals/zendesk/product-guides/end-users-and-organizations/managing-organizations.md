# Managing organizations

Source: https://support.zendesk.com/hc/en-us/articles/4408846640410-Managing-organizations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can manage organizations by viewing and editing organization settings, manually adding end users to organizations, and deleting organizations as needed. You must be an admin to manage organization assignments for agents.

Topics covered in this article:

- [Editing an organization](#topic_cab_ihe_bc)
- [Manually adding users to an organization](#topic_wyj_dse_bc)
- [Restricting agents to an organization](#topic_ebz_dtn_bc)
- [Creating views by organization](#topic_kwp_zcf_bc)
- [Deleting an organization](#topic_ys3_pqc_4qb)

Related articles:

- [About the Organizations page](https://support.zendesk.com/hc/en-us/articles/4408821417114)

## Editing an organization

You can edit an organization's settings as needed. You must be an administrator or an [agent in a custom role with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) to edit organizations.

**To edit an organization**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click the **Organizations** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/organizations_icon.png)) in the sidebar.
2. Find the organization you want to edit and click its name.
3. Make your edits.

   Your updates are saved automatically.

## Manually adding users to an organization

You can add team members and end users to an organization at the time they are created or later by editing their profile. You can also include users' organizations when [importing new users in a bulk import operation](https://support.zendesk.com/hc/en-us/articles/4408893496218-Bulk-importing-users-and-organizations).

You must be an admin to manage organization assignments for agents. Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can add end users to organizations.

On Team plans, users can belong to only one organization. On all other plans, you can [enable multiple organizations for users](https://support.zendesk.com/hc/en-us/articles/4408838140314/), allowing users to belong to up to 300 organizations. However, a user doesn't have to belong to any organization.

**To add a new user to an organization**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click the **Organizations** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/organizations_icon.png)) in the sidebar.
2. Find the organization you want to add a new user to and click the organization's name.
3. Click the drop-down icon at the top-right of the page and select **Add user**.
4. Enter a **Name** and **Email** address.
5. Select a **User type** and then click **Add**.

   The user’s profile page appears, where you can enter any other required information.

**To add an existing user to an organization**

1. Navigate to a user's profile in Zendesk Support (see [Viewing a user's profile in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408822762650-Viewing-a-user-s-profile-in-Zendesk-Support)).
2. In the **Org** field, start entering an organization name.
3. Select the organization name from the suggested matches.

   Your update is saved automatically.

If you add users to multiple organizations, see [Managing users in multiple organizations](https://support.zendesk.com/hc/en-us/articles/4408838309530-Managing-users-in-multiple-organizations-Plus-and-Enterprise-).

## Restricting agents to an organization

One of the options you have for managing ticket workflow and controlling agent access to tickets is to add them directly to an organization and then restrict their access privileges to that organization. You must be an administrator to set this up.

On Enterprise plans, you can restrict access to an organization for all agents in a custom role, but you can't restrict access on an individual agent level.

**To restrict agents in a custom role to an organization (Enterprise)**

- [Create or edit a custom agent role](https://support.zendesk.com/hc/en-us/articles/4408882153882-Using-custom-agent-roles-Enterprise-#topic_cxn_hig_bd) and set ticket access to **Requested by end users in this agent's organization**. You can restrict a custom role to one or multiple organizations.

On Team, Growth, and Professional plans, when you restrict agent access to tickets within their organization, those agents can no longer update end user information or add end users to tickets, and they can't view end user information on the Customers page.

**To restrict an agent to an organization (Team, Growth, and Professional)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. Click the agent that you want to edit, then, on the agent's page, click **Manage in Support**.
3. Under **Access**, select **Tickets in agent's org.**
4. Under **Org**, select the name of the organization, or you can enter a new one.

   If you are on the Growth or Professional plan, you can add more than one org, if you want to restrict the agent's access to multiple organizations.

   Your update is saved automatically, so when you are finished you can navigate away.

Regardless of the groups they belong to, agents will only have access to the organization's tickets.

Note: Notwithstanding ticket access restrictions, CC'ing an agent on any ticket lets the agent receive email notifications of all public and private updates to the ticket.

## Creating views by organization

You can use organizations when creating views and business rules.

For example, a common use for organizations in a view is to monitor ticket activity.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/orgs_view_example.png)

This view displays unsolved tickets that are assigned to an organization named *Customers*.

## Deleting an organization

You can delete an organization as needed. You must be an administrator or [agent in a custom role with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) to delete organizations.

Note: When you delete an organization, any business rules you set up using the organization you deleted will no longer function properly.

**To delete an organization**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click the **Organizations** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/organizations_icon.png)) in the sidebar.
2. Find the organization you want to edit and then click on the organization's name.
3. Click the options arrow in the upper right, then select **Delete**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/organization-options.png)
4. Confirm that you want to delete the organization.

   Any users that were assigned to the organization will be removed from the organization (since it doesn't exist anymore)
   and the organization will be removed from any tickets it was assigned to. Any business rules you set up using the organization you deleted will no longer function properly.