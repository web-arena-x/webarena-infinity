# Adding services to your service catalog

Source: https://support.zendesk.com/hc/en-us/articles/8478940252698-Adding-services-to-your-service-catalog

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

Verified AI summary ◀▼

Create a service catalog to streamline user requests by adding services and assets. As an admin, you can define service items with custom fields, file uploads, and asset types. Once created, save them as drafts and publish when ready. This setup automates ticket creation, linking requests to services with necessary details for resolution.

The service catalog is a user-defined ticket channel. If the service catalog [has been turned on](https://support.zendesk.com/hc/en-us/articles/9443951511450), Support admins can create a list of
services and assets that users can then request through the help center. When a user
submits a service request, a ticket is automatically created and linked to the service
or asset, and includes all of the unique fields and data required to resolve the
request. This article describes how to add services to your service catalog and publish
them so users can start submitting service requests.

This article contains the following topics:

- [Adding services to the service catalog](#topic_rnl_d3f_pdc)
- [Publishing services to your service catalog](#topic_cc4_cw1_wfc)

Related articles:

- [Editing and managing services in your service
  catalog](https://support.zendesk.com/hc/en-us/articles/9444017009690)
- [Submitting service catalog
  requests](https://support.zendesk.com/hc/en-us/articles/4408846805530#topic_ijj_s2k_cgc)

## Adding services to the service catalog

When you create and publish a service, it's added to the service catalog items list
and is available for users to request from their service catalog.

When you create service catalog items, accompanying [ticket forms](https://support.zendesk.com/hc/en-us/articles/4408836460698#topic_p3b_rwv_dgc) are created automatically. A
ticket field named *Service* is also automatically created on your instance
when you start using the service catalog. You cannot edit or delete these ticket
forms or ticket fields.

You must be a Support admin to create services.

**To create a service catalog item**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Service catalog**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Service-cat-tag-icon.png)) in the sidebar.
2. Click **Create service**.
3. Add the **Title** and description for the service.

   The title and
   description are used to identify the service to end users on the related
   catalog page. When users select the service, the full description
   appears on the service catalog page for that service.

   You can use
   the rich text editor to add formatting and images to your description,
   which will be visible to users.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-service-cat-title.png)
4. Configure the service request form by clicking **Add field** and
   selecting from the following options:
   - **Fields**: Allows you to add custom ticket fields to the service
     item, allowing users to provide more details about their specific
     request. In the sidebar, click the add icon (+) next to each [custom ticket field](https://support.zendesk.com/hc/en-us/articles/4408838961562) you
     want to add to the service.

     Adding custom ticket fields to
     services allows users to provide more details about their
     specific request. For example, if you're adding an Apple MacBook
     Pro to your service catalog, you might want to add fields for
     storage size, shipping address, or other details.

     If the
     field that you're looking for isn't listed in the Fields
     sidebar, you can [create](https://support.zendesk.com/hc/en-us/articles/4408883152794) a new custom
     ticket field or [update](https://support.zendesk.com/hc/en-us/articles/4408828883738) an existing
     field's permissions.

     Note: To be available for use in services,
     custom ticket fields must have their permissions set to
     **Customers can edit**.
   - **Upload files**: Allows users to add attachments to service
     requests for this service item. Use the sidebar to modify the
     attachments **Field name** and **Description** and select
     whether attachments are **Required to submit a request**.
   - **Available asset types**: (ITAM EAP only) Allows users to select
     the type of IT asset associated with the service request. Use the
     sidebar to select which types of available assets should be listed
     for this service catalog item. This field is often used in service
     requests for new hardware.
   - **Assigned assets to user**: (ITAM EAP only) Allows users to
     select IT assets already assigned to them that are associated with
     the service request. Use the sidebar to select which types of assets
     should be available to select for this service catalog item. This
     field is often used in service requests related to issues with a
     user's assets.

     Select whether the field is **Required to submit a
     request** and whether to **Allow users to choose certain
     asset types**.
5. (Optional) If you want to add a thumbnail image to the service, making it
   easier to recognize within the catalog, click the settings icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) in the top right corner and then browse for or
   drag and drop a file into the panel.
6. Click **Save draft**.

   When you're ready to make the service available
   to users in the service catalog, you must [publish it](#topic_cc4_cw1_wfc).

## Publishing services to your service catalog

Services can be created ahead of time and saved as drafts. To add the service to the
service catalog, a Support admin must publish it.

**To publish services**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Service catalog**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Service-cat-tag-icon.png)) in the sidebar..

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-service-list-admin.png)
2. Click the title of the service you want to publish.
3. Click the drop-down arrow next to **Save draft** and select
   **Publish**.