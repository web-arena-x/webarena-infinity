# Setting up ticket view in Salesforce

Source: https://support.zendesk.com/hc/en-us/articles/4408834115738-Setting-up-ticket-view-in-Salesforce

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Set up a ticket view in Salesforce to access real-time support data directly from Account, Contact, Lead, Opportunity, and Case pages. This feature doesn't store data in Salesforce or use API calls. Configure ticket view, add components to pages, and manage user access to enhance support visibility. Ensure proper installation and resolve any permission issues for seamless integration.

This article describes setting up a view of Zendesk tickets for your users in Salesforce.
This feature queries Zendesk Support in real-time from the Account, Contact, Lead, Opportunity, and Case pages and doesn't store Zendesk data in Salesforce or consume API calls.

Before creating a ticket view in Salesforce, you must [Connect your Salesforce organization to Zendesk](https://support.zendesk.com/hc/en-us/articles/4408821555482).

This article includes the following topics:

- [Turning on and configuring ticket view for Salesforce](#topic_nxp_dbv_4jb)
- [Adding a Lightning component or Visualforce page to your Salesforce page](#topic_c35_l2v_4jb)
- [Checking if ticket view has successfully installed](#id_q4s_y5n_ckb)
- [Allowing profiles to view ticket view](#topic_wwx_fwr_wlb)

Related information:

- [Salesforce integration resources](https://support.zendesk.com/hc/en-us/articles/4408827957274)
- [Setting up Ticket Sync from Zendesk to Salesforce](https://support.zendesk.com/hc/en-us/articles/4408828449050)

## Turning on and configuring ticket view for Salesforce

The ticket view feature is a view of your Zendesk tickets in Salesforce. It is configured in Admin Center.

If you connected multiple Salesforce organizations and Zendesk accounts, repeat these steps for each organization where you'd like to add a ticket view.

**To turn on and configure ticket view**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Salesforce**.
3. On the Salesforce connection page, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the Salesforce organization you want to turn on ticket view.
4. Click **Install managed package**. The package installs a Lightning component and Visualforce component in your Salesforce account that will be used for ticket view. Zendesk recommends selecting **Install for All Users**. Users who are not granted access are unable to view Zendesk tickets in Salesforce.
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_managed_package.png)
5. Click **Install**.
6. After installation of the package is complete, return to Admin Center and refresh the **Ticket view** tab.
7. Select the **Turn on Zendesk ticket view for Salesforce** checkbox.
8. In the **Map fields** section, configure the matching criteria to filter which tickets are displayed in Salesforce.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_map_fields_new.png)

   The default criteria for how tickets are displayed on Salesforce pages are as follows:

   - **Find account tickets by**: Show tickets where the ticket requester's Zendesk organization name matches the Salesforce account name. Person accounts are also supported by selecting **Ticket requester email** and under Using Salesforce field, selecting **Person account email address**.
   - **Find contact tickets by**: Show tickets where the requester email address matches the Salesforce contact email.
   - **Find opportunity tickets by**: Show tickets where the ticket requester’s Zendesk organization name matches the Salesforce account name.
   - **Find lead tickets by**: Show tickets where the requester email address matches the Salesforce contact email.

   You can also set the account-wide filtering and ticket sorting displayed in Salesforce. By default, all unclosed tickets sorted by descending status are shown.

   The field used for matching within Salesforce needs to be visible to Salesforce users looking at ticket view. The minimum requirement is read-access only.

   Each Salesforce user can set their personal default filtering and sorting by changing this in the Zendesk UI in Salesforce.

   Salesforce limits the number of characters in queries. If the total number of characters (plus padding) in the matching criteria exceeds 4,000, then no results are returned. For example, if you define a view based on matching requester email addresses to related contact email addresses and the account has many contacts, the matching criteria may exceed the 4,000-character limit.
9. After you’ve turned on and configured your ticket view settings, click **Save**.

## Setting up user access to Zendesk tickets in Salesforce

Define which user profiles in Salesforce can view Zendesk tickets.

**To select user profiles to view Zendesk tickets**

1. In Salesforce, click the cog (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_cog.png)) in the upper right pane, then click **Setup**.
2. In the left navigation pane under **PLATFORM TOOLS**, select **Apps**
   > **Connected Apps** > **Manage Connected Apps**.
3. Click the **Salesforce Integration for Zendesk** app. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_manage_apps.png)
4. Click **Edit Policies**.
5. Under **OAuth Policies**, set Permitted Users to **Admin approved users are pre-authorized**, then click **Save**. This is a required setting.
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_oauth_policies.png)
6. Return to the Manage Connected Apps page, then click the **Salesforce Integration for Zendesk** app.
7. Under Profiles, select **Manage Profiles**.
8. Select the user profiles in Salesforce that can view Zendesk tickets. You *must* select the System Administrator profile. User profiles that are not selected will not be able to view Zendesk tickets.
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_manage_profiles.png)
9. Click **Save**.

Your setup is complete.

## Adding a Lightning component or Visualforce page to your Salesforce page

After [turning on and configuring ticket view](#topic_nxp_dbv_4jb), you must add the Lightning component or Visualforce page to your Salesforce Contact, Lead, Opportunity, or Case pages to display Zendesk tickets. A single ticket view component displays tickets for all Zendesk accounts connected to the organization. Users can filter tickets by Zendesk account.

If you choose to add a Lightning component, you must have a Salesforce [My Domain subdomain](https://help.salesforce.com/articleView?id=domain_name_setup.htm&type=5).

**To add a Lightning component or Visualforce page to your Salesforce page**

1. In Salesforce, click on the App Launcher icon in the upper left, select **View All**, then click the link to a Cases, Accounts, Contacts, Leads, or Opportunities page.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Salesforce_pages_apps.png)
2. Select the Case, Account, Contact, Lead, or Opportunity object.

   Note: The ticket view in the Case page is view only.
3. Click the cog icon on the upper right, then select **Edit Page**.
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_edit_page.png)
4. To use the Lightning component, find your Lightning component listed under Custom in the list of components on the left. Remember, this only works if you have [My Domain](https://help.salesforce.com/articleView?id=domain_name_setup.htm&type=5) enabled.
5. Drag **Zendesk\_Ticket\_View** onto the page. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_lightning.png)
6. To use the Visualforce page, find the Visualforce component listed under Standard in the left sidebar.
7. Drag the **Visualforce** page onto the page layout and select the **Zendesk\_Ticket\_View\_Account** on the right sidebar under the Visualforce Page Name menu. Repeat this step for the Contact, Lead and Opportunity pages.
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_visualforce.png)
8. Click **Save**.

A view of your Zendesk tickets appears on your Salesforce page, as shown in the example below.

Note: If you see the message "No tickets in this list," it means your organizations in Zendesk don't have users assigned to them.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Salesforce_ticket_view_multi_filter.png)

If agents encounter permission errors when viewing tickets, check that the user profiles in Salesforce have access to Zendesk tickets. For more information, see [Setting up user access to Zendesk tickets in Salesforce](https://support.zendesk.com/hc/en-us/articles/4408821555482-Setting-up-the-Zendesk-for-Salesforce-integration#topic_n1c_jtm_4jb).

## Checking if ticket view has successfully installed

The following procedure helps you check if ticket view has successfully installed in Salesforce.

**To check your ticket view installation**

1. Go to **Salesforce** > **Setup** > **Deployment Status**.
     
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_ticket_view_check1.png)
2. Check the deployment time when you installed the package and see if the deployment was successful or failed. If deployment failed, Salesforce will provide you with detailed errors. Review the errors and resolve them. If you are unable to resolve them, [contact Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850)
   and provide a screenshot of the error.
3. Check if the components were successfully created.

   For the Lightning component, go to **Salesforce** > **Setup** > **Lightning Components** > **Zendesk\_Ticket\_View**.
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_ticket_view_check2.png)

   For the Visualforce page, go to **Salesforce** >
   **Setup** > **Visualforce Pages** >
   **Zendesk\_Ticket\_View**. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_ticket_view_check3.png)

To resolve issues with your ticket view configuration, see [Resolving ticket view errors](https://support.zendesk.com/hc/en-us/articles/4408828717466-Known-issues-and-troubleshooting#h_14a189a2-52c0-4f87-8cb1-df5a88e2bd81).

## Allowing profiles to view ticket view

You can allow profiles to access ticket view in Visualforce pages.

**To allow profiles to view ticket view**

1. In Salesforce, go to **Setup** > **Custom Code** >
   **Visualforce Pages**.
2. Next to the label that includes Zendesk\_Ticket\_View\_Contact, Zendesk\_Ticket\_View\_Lead, Zendesk\_Ticket\_View\_Opportunity, and Zendesk\_Ticket\_View\_Account, click **Security** under the Action column.
3. Select profiles from Available Profiles, add them to Enabled Profiles, then click **Save**.