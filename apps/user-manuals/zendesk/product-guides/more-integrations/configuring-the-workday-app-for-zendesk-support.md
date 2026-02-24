# Configuring the Workday app for Zendesk Support

Source: https://support.zendesk.com/hc/en-us/articles/9391945391642-Configuring-the-Workday-app-for-Zendesk-Support

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Configure the Workday app to customize how your team accesses employee data. Add or remove fields, map them to match records, and rearrange objects to suit your needs. You can also reorder, edit, or remove objects to ensure the app displays relevant information for agents. This flexibility helps tailor the app to your support processes, enhancing your team's ability to manage customer inquiries effectively.

After [installing and connecting](https://support.zendesk.com/hc/en-us/articles/8220920383258) the Workday app for Zendesk Support, Zendesk admins and team members in a [custom role with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can configure it to suit your company's needs. For example, you can add or remove fields, map fields, and rearrange objects to change the order and appearance of the app.

To learn more about how the integration works, see [About the Workday app for Zendesk Support](https://support.zendesk.com/hc/en-us/articles/8220920383258#topic_spz_k3r_mdc).

This article includes the following topics:

- [Adding Workday objects and fields to the app](#topic_pkp_xmw_5bb)
- [Reordering, editing, or removing objects](#topic_jdv_xm3_xcc)

## Adding Workday objects and fields to the app

Initially, the app displays a list of standard Workday fields and requires no configuration:

- Phone number
- Mailing address
- Job title
- Department
- Manager's name
- Employment status (full-time, part-time, etc.)

However, your agents may require access to different objects or more fields when working on tickets. In this case, add fields to the app as needed. Note that when adding objects, an agent must have permission in Workday to view all fields within that object. Otherwise, the agent won't be able to view the object.

During this process, you'll match Workday and Zendesk fields so that the correct data from Workday displays in the sidebar. Later, you can edit and reorganize fields.

**To add Workday objects to the app**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Workday** link.
3. If you have multiple connections, click the name of the connection you are setting up.
4. In the Manage data section, click **Add Workday object**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/workday_add_workday_object.png)
5. In the Select object field, select the name of the Workday object you'd like to add from the drop-down list, then click **Next**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/workday_dropdown_add_object.png)
6. In the Matching fields section, select the Zendesk and Workday fields the app should use to find matching records, then click **Next**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/workday_match_fields.png)

   Select fields that make sense for your use case. For any Zendesk ticket, Zendesk attempts to find a record in Workday with data in the selected field that exactly matches the data in the specified Zendesk field.
   In the case of a drop-down field, the field tag value is used instead of the title.
7. In the Select fields to display section, select the Workday fields you’d like to display in the app. Begin typing to display available fields, and select them from the drop-down list as they appear. You can reorder them later. When you’re done adding fields, click **Next**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/workday_fields_display.png)
8. Click **Add**.

The preview pane displays how the added objects will appear to agents. Use the preview to determine whether objects need to be adjusted or reordered.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/workday_app_admin_preview.png)

## Reordering, editing, or removing objects

You can reorder, edit, and remove objects within the app configuration. Make sure you click **Save** after making changes.

- Click the grabber icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_grabber_icon.png)) to drag and drop objects and fields within objects to reorder them. The order represented in the configuration will determine the order of fields displayed in the Workday app.
- To delete an object from the app, click **Delete** from the drop-down menu, then click **Delete object** to confirm.
- To edit an object, click **Edit**. The name of the object will be read only, but all other fields can be modified, including field matching.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/workday_fields_edit.png)