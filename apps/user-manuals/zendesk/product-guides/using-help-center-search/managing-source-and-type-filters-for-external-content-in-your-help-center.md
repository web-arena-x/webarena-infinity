# Managing source and type filters for external content in your help center

Source: https://support.zendesk.com/hc/en-us/articles/4593648456730-Managing-source-and-type-filters-for-external-content-in-your-help-center

---

If you're setting up a new web crawler, the name that you assign to the crawler will automatically be used to create the Source value. If you want to change the name later, you can always edit or assign a different source name.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

When you set up [help center federated search](https://support.zendesk.com/hc/en-us/articles/4593564000410), you must
define the *source* and *type* of the external content that you want
to make available in your help center:

- **Source**: Refers to the origin of the external content, such as a
  forum, issue tracker, or learning management system.
- **Type**: Refers to the kind of content, such as blog posts, tech
  notes, or bug reports.

If you're setting up a new web crawler, the name that you assign to the
crawler will automatically be used to create the Source value. If you
want to change the name later, you can always edit or assign a different
source name.

When [external content appears in a help center
search](https://support.zendesk.com/hc/en-us/articles/4593607942298), that content is grouped under the appropriate source and
type names, making it easier for users to find the information they are
looking for.

![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/search-crawler-guide-filter.png)

This article contains the following topics:

- [Create an external source or
  type](#topic_cnf_rb1_y5b)
- [Edit an external source or type
  name](#topic_j4h_3vc_x4b)
- [Delete an external source or
  type](#topic_f3d_tcy_x4b)

## Creating an external source and type

You can create new sources and types for your external content. However, if
you're using connectors or web crawlers to ingest external content, source and type
are automatically created, and unecessary for you to create manually.

In the help center, the search results filter will show the source or type whenever
external content associated with that source or type appears in the search results.

Tip: To help users filter and locate content
quickly, consider useful groupings and names for your external content sources
and types when creating them. See [Help center guide for end users (Using the
search filters)](https://support.zendesk.com/hc/en-us/articles/4408837910426#topic_ilh_5dk_ytb).

**To create an external source or type**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) in the sidebar.
2. Click **Search settings**.
3. Under **Search filters**, click **Manage**.
4. On the **Sources** tab, click **Create source**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-oneclick-searchfilters.png)
5. In the **Name** field, type a name that describes where this content
   lives, then click **Create**.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide-ew-searchadmin-createsource-modal.png)
6. On the **Types** tab, click **Create type**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-oneclick-types.png)
7. In the **Name** field, enter a name that describes what kind of content
   this is, then click **Create**.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide-ew-searchadmin-createtype-modal.png)

## Editing an external source or type name

You can change the name associated with an external content source or type
if you want to control how that element appears in the UI.

**To edit an external source or type name**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) in the sidebar.
2. Click **Search settings**.
3. Under **Search filters**, click **Manage**.
4. Select the **Sources** or **Types** tab, depending on the element that
   you want to edit.
5. On the row of the source or type that you want to edit, click the options
   menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)), and then click **Edit
   name**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-oneclick-editnametype.png)
6. In the **Name** field, type the new name.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-sc-edit-source-name.png)
7. Click **Save**.

## Deleting an external source or type

You can delete an external source or type if you no longer plan to ingest external
content associated with that source or type into your help center search.

Important: Do not delete the source or type for the
[connectors to Confluence](https://support.zendesk.com/hc/en-us/articles/9796599390874) from this
page. If you do so, the connectors will break and you won't be able to reconnect
them. To remove a Confluence connection, see [Managing the Knowledge connector to
Confluence](https://support.zendesk.com/hc/en-us/articles/9796584600218).

When you delete an external source or type, the following will occur:

- External content records belonging to this source or type won’t be
  included in help center results.
- Any crawler or external content connection associated with this
  source or type will be deleted, and the connection related to the deleted
  source or type becomes unsyncable.
- If you have any API integrations that add external records to this
  source or type, they may break.

**To delete an external source or type**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) in the sidebar.
2. Click **Search settings**.
3. Under **Search filters**, click **Manage**.
4. Select the **Sources** or **Types** tab, depending on the element that
   you want to delete.
5. On the row of the source or type that you want to edit, click the options
   menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)), and then click
   **Delete**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-oneclick-searchfilterdel.png)
6. Click **Delete**.
7. Read the **Delete source** confirmation content and select the check
   boxes to indicate that you understand each item.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide-sc-delete-search-filter+conf.png)
8. Click **Delete**.