# Managing Confluence spaces connected to your Zendesk account

Source: https://support.zendesk.com/hc/en-us/articles/9796584600218-Managing-Confluence-spaces-connected-to-your-Zendesk-account

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

You can [configure a connection to ingest content](https://support.zendesk.com/hc/en-us/articles/9796599390874) from your Confluence sites and spaces to your Zendesk account where it can be available for help center search, generative search, and advanced AI agents, and Agent Workspace. Once you've created a Confluence connection, you can make changes to the connected site and spaces as needed.

This article contains the following topics:

- [Viewing Confluence connection details](#topic_cvp_glb_xgc)
- [Managing viewer permissions for Confluence content](#topic_z5f_xts_ygc)
- [Manually resyncing Confluence content](#topic_x2c_xlb_xgc)
- [Disconnecting a Confluence site or space](#topic_c5b_bmb_xgc)

**Related articles:**

- [Connecting external content to your Zendesk account to power workflows](https://support.zendesk.com/hc/en-us/articles/9822956298010)

## Viewing Confluence connection details

When you add spaces to your Knowledge connector to Confluence, you can view information about the connection, when it was created and by whom, and when it was last synced.

**To view Confluence connection details**

1. In Knowledge admin, click **Manage articles** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_manage_articles.png)) in the sidebar.
2. Click **External content > Connections**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-confcnct-extcontent-connect.png)
3. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) on the row for the space you want to manage, then select **Manage**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-confcnct-manage.png)
4. View details about the connection:
   - **Created**: When the connection was created
   - **Connected by**: Name of the Knowledge admin who created the connection
   - **Items**: Number of connected pages in the space
   - **Status**: Sync status
   - **Last synced**: When the last sync occurred. Syncs are automatically performed every 12 hours, though can also be [triggered manually](#topic_x2c_xlb_xgc)
   - **Connection**: Link to the space in the Confluence site

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-confcnt-manage-view.png)
5. Click **Save**.

## Managing viewer permissions for Confluence content

You can set the view permissions for who can view connected Confluence content in your Zendesk workflows.

**To manage viewer permissions for Confluence content**

1. In Knowledge admin, click **Manage articles** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_manage_articles.png)) in the sidebar.
2. Click **External content > Connections**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-confcnct-extcontent-connect.png)
3. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) on the row for the space you want to manage, then select **Manage**.
4. Under **Viewing permissions** select one of the following options to determine which [user segments](https://support.zendesk.com/hc/en-us/articles/4408837707290) can view content from this space:
   - **Only visible to selected user segments**: Select up to 10 user segments from any of the following (an Enterprise plan is required to select multiple user segments):
     - **Signed-in users**: Includes internal and external users who create an account and sign in to your help center.
     - **Agents and admins**: Includes team members only, so that you can create content that is internal-only.

       Note: Light agents are included in this segment. For a list of light agent permissions, see [Understanding and setting light agent permissions](https://support.zendesk.com/hc/en-us/articles/4408846501402-Understanding-and-setting-light-agent-permissions-).
     - **Custom user segment**: Allows you to restrict viewing access to specific users based on tags, organizations, or groups by applying user segments. See [Creating user segments to restrict access](https://support.zendesk.com/hc/en-us/articles/4408837707290).
   - **Visible to everyone**: Includes anyone who visits your help center and does not require sign in.
5. Click **Save**.

## Manually resyncing Confluence content

When you connect Confluence as an external content source, a sync process runs every 24 hours to update new or changed content. You can manually force a sync.

**To manually resync Confluence content**

1. On the Connections page, click the options menu (![](https://support.zendesk.com/hc/article_attachments/9831407365402)) for the site or space you want to sync.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-connector-syncagain.png)
2. Select **Sync again**.

   The Confluence spaces sync immediately, and the Last synced column is updated with the most recent sync time.

## Disconnecting a Confluence site or space

You can remove connections to Confluence sites or spaces if you no longer want to sync their content. If you remove a site connection, all space connections within that site will be removed. To remove an individual space connection but retain others within the site, remove the space connection only.

When you remove a connection, the related content is no longer available to your help center, generative search, advanced AI agents, or Agent Workspace.

**To disconnect a Confluence site**

1. On the Connections page, click the options menu (![](https://support.zendesk.com/hc/article_attachments/9831407365402)) for the site or space you want to disconnect.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-confcnt-remove-connection-new.png)
2. Select **Remove connection**.
3. Review the message, then click **Remove connection**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-confcnt-removecnct-conf.png)

   The space is removed from the Connection list, and is no longer available as an external content source.