# Installing and configuring the Salesforce app for Zendesk Support

Source: https://support.zendesk.com/hc/en-us/articles/4408834679066-Installing-and-configuring-the-Salesforce-app-for-Zendesk-Support

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

The Salesforce app lets you view Salesforce data directly in tickets. After installation, configure settings like data refresh rates, object visibility, and user access. Connect multiple Salesforce organizations for comprehensive data access. Customize data display and refresh rates to suit your needs, and allow agents to manually refresh data for up-to-date information. Manage role and group access to optimize user experience.

The Salesforce app for Zendesk Support allows agents to view Salesforce data directly within
Zendesk tickets. After the app is installed, admins can configure various settings, such
as the Salesforce objects and fields that appear, data refresh rates, data filters, and
user access.

This article contains the following topics:

- [About the Salesforce app for Zendesk Support](#topic_xcl_4l3_xcc)
- [Installing, connecting, and turning on the Salesforce app](#topic_axj_2c2_sjb)
- [Configuring the Salesforce app](#id_cp2_5j2_sjb)
  - [Configuring the Salesforce data cache refresh rate](#topic_uch_kfk_sjb)
  - [Allowing agents to refresh the cache manually](#topic_swr_4xg_zcc)
  - [Adding Salesforce objects to the app](#topic_pkp_xmw_5bb)
  - [Matching fields](#topic_o1n_k5v_xcc)
  - [Filtering the related objects](#topic_pbj_zyj_sjb)
  - [Reordering, editing, or removing objects](#topic_jdv_xm3_xcc)

## About the Salesforce app for Zendesk Support

The Zendesk for Salesforce app allows agents to view Salesforce information from a
ticket in Zendesk. For agents to see the app in the sidebar, you need to install the
app, connect your Zendesk account to Salesforce, and then turn on the app. See [Installing and connecting the Salesforce
app](#topic_axj_2c2_sjb).

With a ticket open in Zendesk, click the **Apps** button on the upper-right side
of the ticket page. The Salesforce app is displayed in the right sidebar. The app is
visible only on existing tickets.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_sidebar_app_new.png)

The app supports connecting multiple Salesforce organizations to a Zendesk instance,
allowing agents to see Salesforce data for all your organizations in the sidebar of
a ticket. Multiple connections are only supported for the sidebar app and not for
other integration use cases.

### Considerations

- The Salesforce app for Zendesk Support doesn't support Salesforce
  account hierarchy.
- A Salesforce organization name cannot include the following characters:
  `` ? / ` _ < > ``. Including any of these characters
  in the organization name will cause the installation to fail.

## Installing, connecting, and turning on the Salesforce app

Follow the procedures in this section if you’re installing the Salesforce app in
Zendesk for the first time or re-installing the app.

If you’re connecting multiple Salesforce organizations to your Zendesk instance,
repeat steps 2-3 for each organization you’d like to connect to Zendesk.

There are three steps to installing and turning on the app:

1. [Connecting your Zendesk
   Support instance to Salesforce](#topic_tsg_gm3_xcc)
2. [Installing and activating the Salesforce app](#topic_ncf_1m3_xcc)
3. [Enable role and group restrictions](#topic_ylh_wl3_xcc)

### Connecting your Zendesk Support instance to Salesforce

After installing the Salesforce app, you need to connect Zendesk to Salesforce.
You must have [appropriate Salesforce credentials](https://support.zendesk.com/hc/en-us/articles/4408843355290) to
perform this task.

For instructions, see [Connecting your Salesforce organization to
Zendesk](https://support.zendesk.com/hc/en-us/articles/4408821555482).

### Installing and activating the Salesforce app

Turning on the Salesforce app makes it visible to agents in existing tickets. If
you still have yet to configure the app, return to this step when you're ready.
You can also turn off the app if you need to hide it temporarily.

**To turn on the Salesforce app**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Salesforce** link.
3. If you have multiple connections, click the name of the connection you are
   setting up.
4. Click the **Support app** tab.
5. Select **Turn on Salesforce app for Zendesk Support** to install the app
   and make it visible to agents. Deselect this option to turn off the
   app.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_turn_on_app.png)
6. Click **Save**.

### Enable role and group restrictions

If required, select and configure role and group restrictions for the Salesforce
app.

**To enable role restrictions**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Apps > Zendesk Support
   apps**.
2. For the Salesforce app, click the gear drop-down menu and click
   **Change settings**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_settings_menu.png)
3. Select and configure role restrictions and group restrictions.
   - To restrict access to the app by role, select **Enable role
     restrictions**, then select the roles that should have
     access.
   - To restrict access to the app by group, select **Enable group
     restrictions**, then select the groups that should have
     access.

## Configuring the Salesforce app

You can customize the data displayed in the Salesforce app and how often the data is
refreshed by configuring the app settings discussed in this section. Only Zendesk
admins and team members in a [custom role with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can configure the app.

After changing the ticket or app configuration, it can take up to 60 minutes for
recently viewed tickets to appear updated in the Salesforce app. For information on
changing this rate, see [Configuring the Salesforce data cache refresh rate](#topic_uch_kfk_sjb).

### Configuring the Salesforce data cache refresh rate

When you open a Zendesk ticket, the app fetches and displays Salesforce data you
selected in the procedure [Adding Salesforce objects to the app](#topic_pkp_xmw_5bb). The
app uses the Salesforce API to pull records. To reduce the API load, data is
refreshed every 60 minutes by default.

The data refresh setting allows you to define how long Salesforce data is cached
in the Zendesk database. During the caching window, changes in Salesforce will
not be reflected in the app. After the caching period, the data will be fetched
the next time an agent visits the ticket.

- A **shorter refresh rate** means data is collected from Salesforce more
  often and is more likely to be up to date. However, this can impact the
  Salesforce API limits.
- A **longer refresh rate** means data is collected less often but reduces
  the risk of reaching the Salesforce API limits.

**To configure the Salesforce app data refresh setting**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Salesforce** link.
3. If you have multiple connections, click the name of the connection you are
   setting up.
4. Click the **Support app** tab.
5. Under **Set data caching duration**, select the data refresh setting from
   the drop-down list.   
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_caching_duration_setting.png)
6. Click **Save**.

### Allowing agents to refresh the cache manually

You can allow agents to refresh the cache manually so they can instantly fetch
updated customer details from Salesforce to Zendesk Support.

**To allow agents to refresh cached data from Salesforce**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Salesforce** link.
3. If you have multiple connections, click the name of the connection you are
   setting up.
4. Click the **Support app** tab.
5. Select **Manually update the cached data from Salesforce as needed**.
6. Click **Save**.

### Adding Salesforce objects to the app

Initially, the Salesforce app displays no data. Zendesk admins must configure the
app to show the Salesforce data agents want to see when working on tickets. This
process entails adding the Salesforce data objects to the app and filtering and
arranging them so they display how they'd like.

**To add Salesforce objects to the app**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Salesforce** link.
3. If you have multiple connections, click the name of the connection you are
   setting up.
4. Click the **Support app** tab.
5. In the Manage data section, click **Add Salesforce object**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_add_salesforce_object.png)
6. In the Select object field, select the name of the object (or record type)
   you'd like to add from the drop-down list, then click **Next**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_dropdown_add_object.png)
7. In the Map fields section, select the Zendesk and Salesforce fields the app
   should use to find matching records, then click **Next**. See [Matching fields](#topic_o1n_k5v_xcc).
8. In the Select fields to display section, select the Salesforce fields you’d
   like to display in the app. Begin typing to display available fields, and
   select them from the drop-down list as they appear. You can reorder them
   later. When you’re done adding fields, click **Next**.

   Note: Adding more than five fields may slow data
   retrieval and cause timeouts or errors.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_select_fields_to_display.png)
9. In the Apply filters step, select the fields for each object you’d like to
   filter results for, then click **Next**. See [Filtering the returned
   objects](#topic_pbj_zyj_sjb).
10. Click **Add**.

The preview pane displays how the added object will appear to agents. Use the
preview to determine whether objects need to be adjusted or reordered.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_app_admin_preview.png)

### Matching fields

The purpose of the Match fields section is to specify the Zendesk and Salesforce
fields that the app should use to find matching records. Select fields that make
sense for your use case.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_match_fields.png)

For any Zendesk ticket, Zendesk attempts to find a record in Salesforce with data
in the selected object and field that exactly matches the data in the specified
Zendesk field. In the case of a drop-down field, the field tag value is used
instead of the title.

When you’re finished mapping fields, click **Save** (if you’re editing the
Salesforce object) or **Next** (if you’re adding a new Salesforce
object).

Note: You can't map a Salesforce field to a [custom user field](https://support.zendesk.com/hc/en-us/articles/4408822051866) or a [custom organization field](https://support.zendesk.com/hc/en-us/articles/4408842677786) for record
lookup. Additionally, mapping numeric fields is not supported. It's possible to
add a lookup record that returns no records. This is where the Record ID in
Salesforce is returned instead of the actual value of the field. For more
information, see [Salesforce: Syncing lookup field information
to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408823748890).

### Filtering the related objects

You can filter the related objects in the app by date and value. Filters can be
helpful if you'd like to narrow results by specific values and provide agents
with better visibility into the correct records. For example, if a customer has
purchased 100 products, applying a filter for products valued over $1000 and
purchased after a specific date will narrow the results, allowing the agent to
find the most relevant information.

**To filter related objects**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Salesforce** link.
3. If you have multiple connections, click the name of the connection you are
   setting up.
4. Click the **Support app** tab.
5. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the object you want to filter, then
   click **Edit**.
6. In the Apply filters step, expand the related object you want to filter,
   then set the filtering conditions. For example, if you filter opportunities,
   you could show opportunities won by setting **Won is true**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_apply_filters.png)
7. Click **Save**.

### Reordering, editing, or removing objects

You can reorder, edit, and remove objects within the app configuration. Make sure
you click **Save** after making changes.

- Click the grabber icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_grabber_icon.png)) to drag and drop objects and fields within
  objects to reorder them. The order represented in the configuration will
  determine the order of fields displayed in the Salesforce app.
- To delete an object from the app, click **Delete** from the drop-down
  menu, then click **Delete object** to confirm.
- To edit an object, click **Edit**. The name of the object will be read
  only, but all other fields can be modified, including field matching and
  filters.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_delete_object.png)