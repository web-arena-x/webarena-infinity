# Connecting Confluence to your Zendesk account as an external knowledge source

Source: https://support.zendesk.com/hc/en-us/articles/9796599390874-Connecting-Confluence-to-your-Zendesk-account-as-an-external-knowledge-source

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Note: The ability to connect Confluence content to your Zendesk account is available for all plans. However, the storage limits for external data vary by plan. See [Managing data storage in your Zendesk account](https://support.zendesk.com/hc/en-us/articles/4408835043994).

You can connect your Confluence Cloud site to your Zendesk account and make the content available for help center search, generative search, advanced AI agents, and Agent Workspace. You can configure up to 50 [external content sources](https://support.zendesk.com/hc/en-us/articles/9822956298010), which makes the related content available in all of these areas. [Users with permission](https://support.zendesk.com/hc/en-us/articles/9796584600218#topic_z5f_xts_ygc) who are performing searches in your help center can access your Confluence content directly from the search results page.

When you connect Confluence to Zendesk, you’ll see your Confluence spaces listed as an external search source. You can use the [Manage search sources view](https://support.zendesk.com/hc/en-us/articles/4593607942298) to select the spaces that you want to include in your search results.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-confcnct-mng-ext-source.png)

You must be a Knowledge admin to set up and manage external content connections.

This article contains the following topics:

- [Connecting a Confluence site](#topic_ftg_xjt_wgc)
- [Adding another Confluence space](#topic_t1w_vps_ygc)

**Related articles**:

- [Managing Confluence spaces connected to your Zendesk account](https://support.zendesk.com/hc/en-us/articles/9796584600218)
- [Knowledge product limits for your help center](https://support.zendesk.com/hc/en-us/articles/4408831783962)

## Connecting a Confluence site

You can create a connection to ingest and sync content from your Confluence spaces.

Note: Labels added to Confluence content are not synced to Zendesk.

**To set up a Confluence connection**

1. In Knowledge admin, click **Manage articles** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_manage_articles.png)) in the sidebar.
2. Click **External content > Connections**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-confcnct-extcontent-connect.png)
3. Click **Create connection**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-connections-create-connection.png)
4. In the Confluence card, click **Connect**.

   Note: If you aren't logged into Confluence, you'll be redirected to a login screen after connecting. You must be logged into Confluence before proceeding. Log into Confluence with a user account that has the correct permissions for content you want to sync to Zendesk.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-confcnctr-create.png)
5. Select your Confluence site from the drop-down list and click **Accept**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-confcnct-reqaccess.png)
6. In the **Confluence site** menu, select the Confluence site that you want to connect.
7. In the **Spaces** menu, select the spaces that you want to connect to Knowledge.

   Note: Connections to personal spaces in Confluence are not permitted.

   Only the first 20 spaces (shown in alphabetical order) appear in the drop-down menu. To select a space that doesn't appear in the menu, begin typing the name of the space in the search box, then select it once it appears. To remove a space, click **X** on the space tag.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-confcnct-syncconfsite.png)
8. Click **Sync** to begin syncing your site.

   When the sync is complete, the page will show a green Synced status for each synced space.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-confcnct-synced-complete.png)

To include Confluence content in

- Help center search results, see [Including external content in your help center search results](https://support.zendesk.com/hc/en-us/articles/4593607942298).
- Agent Workspace, see [Using quick answers for generative search in tickets](https://support.zendesk.com/hc/en-us/articles/6942763726106).

## Adding another Confluence space

After you create a connection to a Confluence site, you can add more spaces to the connection at any time.

**To add spaces to your Confluence connection**

1. In Knowledge admin, click **Manage articles** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_manage_articles.png)) in the sidebar.
2. Click **External content > Connections**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-confcnct-extcontent-connect.png)
3. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) on the Confluence site row that contains the spaces you want to add, then select **Add content**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-confcnct-addcontent.png)
4. In the **Confluence site** menu, select the Confluence site that contains the spaces you want to add.
5. In the **Spaces** menu, select the spaces that you want to connect to Knowledge.

   Only the first 20 spaces (shown in alphabetical order)
   appear in the drop-down menu. To select a space that doesn't appear in the menu, begin typing the name of the space in the search box, then select it once it appears. To remove a space, click **X** on the space tag.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-confcnct-syncconfsite.png)
6. Click **Sync** to add the spaces and begin syncing them to Knowledge.

   When the sync is complete, the page will show a green Synced status for each newly added and synced space.

When you add spaces to an existing connection, you must configure those new spaces as external content to make them available in help center search results and AI agent responses.

To include Confluence content in

- Help center search results, see [Including external content in your help center search results](https://support.zendesk.com/hc/en-us/articles/4593607942298).
- Agent Workspace, see [Using quick answers for generative search in tickets](https://support.zendesk.com/hc/en-us/articles/6942763726106).