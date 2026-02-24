# Installing and using the Assignment Control app

Source: https://support.zendesk.com/hc/en-us/articles/4408881625754-Installing-and-using-the-Assignment-Control-app

---

The [Assignment Control](https://www.zendesk.com/apps/support/assignment-control/) app is designed to limit the available assignees for a ticket. By targeting specific users, groups, tags, or organizations, this enables specific groups or users to be hidden from the **Ticket Assignee** drop-down.

This article contains the following topics:

- [How the app works](#h_8587345c-867d-4587-aeb7-34eca20838ea)
- [Installing the Assignment Control app](#h_cc5354a3-b593-4464-b380-5ce8c556dbd7)
- [Using the Assignment Control app](#h_a01f8f7d-066b-43df-b557-1eed7dcc5598)
- [Release Notes](#h_a01f8f7d-066b-43df-b557-1eed7dcc5598)

## How the app works

The Assignment Control app hides certain users or groups from the assignee drop-down. This allows administrators to limit to whom an agent can assign a ticket. Targeting certain users, groups, tags, or organizations means that agents can have a more limited, easier to manage list of other agents and groups to whom they can assign a ticket.

## Installing the Assignment Control app

1. In Zendesk Support, click **Admin** (![](https://support.zendesk.com/hc/article_attachments/360043525093/manage_icon.png)), then select **Apps** > **Marketplace**. Enter "Assignment Control" in the search bar.
2. Double-click on the Assignment Control app icon, and click **Install**.
3. In the Installation section, enter a name for the Assignment Control app, enable group and role restrictions if required. **![](https://support.zendesk.com/hc/article_attachments/7856673181850)**
4. On the app details page, click **Install.**

These configuration options are also available after installation by navigating to  **Admin** > **Apps** > **Manage**, and under the Currently installed tab, click the Assignment Control app dropdown options, and select **Change settings**.

## Using the Assignment Control app

The Assignment Control app does not appear in the ticket editor in Support. You may see a small eye at the upper right-hand corner of the app sidebar to indicate that an application is running in the background.

![](https://support.zendesk.com/hc/article_attachments/7856678509210)

All the functionality for the app is controlled from the application settings screen. Before setting the various settings, it may be helpful to obtain the user, group, and organization IDs you'll need. You can obtain these IDs by navigating to **Settings** > **Manage** > **People.** The ID for groups and users can be found in the URL on the individual page for that particular user or group.

In the **hidden\_user\_ids** and **hidden\_group\_ids** fields, place the ids for the users and groups that you wish to have hidden in the assignee drop-down. Note that if you hide an entire group, users within that group will not be available unless they are also members of other groups. IDs should be added in the following format

```
3586939372, 2489672093 
```

In the fields labeled as targeted, choose which specific groups, organizations, tags, and users will have the hidden restrictions applied. For instance, if you want keep agents in a Tier 1 group from being able to assign tickets to agents in a Tier 3 group, you would place the id for the Tier 3 group in the **hidden\_group\_ids** field and the id for the Tier 1 group in the **targeted\_group\_ids** field. You must fill in at least one of the targeted fields for the app to work.

**Note:** The Assignment Control app only functions in the ticket editor.  It will not hide users or groups in ticket views.

## Release Notes

**Version 2.0.4 - 2020-08-31**

- Fixed an issue that caused the app to slow down when opening multiple tickets and having a large group of assignees hidden.