# Installing and using the Super Admin app

Source: https://support.zendesk.com/hc/en-us/articles/4408881571482-Installing-and-using-the-Super-Admin-app

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

The [Super Admin app](https://www.zendesk.com/apps/support/super-admin/) is a tool for bulk updating agents and end users in Zendesk Support. An administrator can search for agents or end users by several properties, and then either export the result or select specific users to update in bulk.  The app is available in the [Zendesk Marketplace](https://www.zendesk.com/apps/support/super-admin). 

This article contains the following topics:

- [Installation](#h_5e1e8c89-e124-4ed6-92c6-f10218e03279)
- [Using the Super Admin app](#h_cf631d39-194c-458e-87b6-a917e3115be3)
- [Searching for and updating agents](#h_57ca0919-3131-470d-9f2a-f8bb66caf10c)
- [Searching for and updating end users](#h_f5133dc6-f21b-4c4e-93fd-64ee5b84fa45)
- [Release Notes](#h_94659fa1-f93b-4964-8315-96a77dd5dd4e)
- [Feedback](#h_01GFRAPBWV9EZ7W8KKQHXMGEEX)

## Installation

1. In [Admin Center](../account-administration/using-zendesk-admin-center.md#topic_hfg_dyz_1hb), click **Apps and integrations** ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)![](https://support.zendesk.com/hc/article_attachments/360043525093/manage_icon.png)) in the sidebar, then select **Apps > Zendesk Support apps**.
2. Click the **Marketplace** button and search for "Super Admin" in the search bar at the upper left of the page.
3. Click the Super Admin app icon, and click **Install**.
4. Select your account to install this app.
5. In the **Installation** section, select any of the settings that you want to apply to your configuration.
6. Click **Install**.

## Using the Super Admin app

Click on the **Super Admin** icon on the left sidebar, and the full page application opens in a tab.

![mceclip0.png](https://support.zendesk.com/hc/article_attachments/7856497914522)

From the main page, you can choose to search and manage agents or end users.

### Searching for agents

You can search for agents by roles and groups.  Alternatively, you can click on **Suspended** or **Active** status and see all agents that are in that state.  There is also a search box that can be used to search for values in **Name**, **Email**, or **Tags**.

After the search results are found, click the **Export** button to export the list of agents to a CSV file for further analysis. You can also toggle various fields in the view by clicking the gear icon next to the **Export** button:

![](https://support.zendesk.com/hc/article_attachments/7856503415706)

### Updating multiple agents

After searching for agents, you can update the details of multiple agents.

**To update multiple agents**

1. When your list of agents is shown, select the checkbox next to the agents you would like to edit.
2. Click **Edit Agents** and update the following fields:  
   - Role
   - Default group
   - Add tags
   - Remove tags
   - Suspension: active or suspended

   ![](https://support.zendesk.com/hc/article_attachments/7856503417882)
3. Click **Confirm** and wait for the app to complete the updates.  
   **Note:** During the update process, do not close the app window.

### Searching and updating end users

The app also enables searching and updating multiple end users.

**To search and update end users**

1. In the SuperAdmin app, click the **End Users** tab.
2. Search for end users by keywords in the search field, or click on the **Suspended/Active** status.
3. Once the search results has been found, toggle various fields in the view by clicking the gear icon.  
   ![](https://support.zendesk.com/hc/article_attachments/7856497914010)
4. Once your list of end users has been found, select the checkbox next to the agents you would like to edit.
5. Click on the **Edit End Users** button and update the following fields:  
   - Role
   - Add tags
   - Remove tags
   - Suspension: active or suspended

   ![](https://support.zendesk.com/hc/article_attachments/7856497915418)
6. Click **Confirm** and wait for the app to complete the updates. **Note**: During the update process, do not close the app window.

### Release notes

**Version 1.1.1 - 2021-03-08**

- Translations for non-English languages released

**Version 1.1.0 - 2020-09-28**

- New feature - Added the ability to terminate agents sessions

**Version 1.0.1 - 2020-09-09**

- Added a loading indicator
- Updated agents and end-users screen so that it doesn't fetch all rows on load
- Restricted agent group searching by the default group
- Removed listing of all groups (Just default group)

**Version 1.0 - 2020-06-22**

- Initial release

### Feedback

Post any Super Admin app feedback or feature requests in the [official feedback thread](https://support.zendesk.com/hc/en-us/community/posts/4409217165466) in the Community.