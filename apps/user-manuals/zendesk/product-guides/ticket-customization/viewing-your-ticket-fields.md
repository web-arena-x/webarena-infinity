# Viewing your ticket fields

Source: https://support.zendesk.com/hc/en-us/articles/4408832419738-Viewing-your-ticket-fields

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

You can view all of your standard and custom ticket fields on the **Fields** page in Zendesk Admin Center. There you can browse, search, and filter your ticket fields. You can also change the display of ticket fields on the page.

This article contains the following topics:

- [Accessing ticket fields](#topic_k24_3gw_jz)
- [Browsing and searching the ticket fields list](#topic_l24_3gw_jz)
- [Modifying and sorting on columns](#topic_vgj_3gw_jz)
- [Filtering the ticket fields list](#topic_slv_spb_cdb)

Related articles:

- [Editing and managing your ticket fields](https://support.zendesk.com/hc/en-us/articles/4408828883738).
- [Adding custom fields to your tickets and support request forms](https://support.zendesk.com/hc/en-us/articles/4408883152794)

## Accessing ticket fields

You must be an admin to access and view your ticket fields in Admin Center.

**To access your ticket fields**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Tickets > Fields**.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/new_ticket_fields_page.png)

  From here, you can browse, sort, search, and filter your ticket fields. You can also [export](https://support.zendesk.com/hc/en-us/articles/4408836502682--New-Importing-and-exporting-values-for-ticket-fields) ticket fields.

## Browsing and searching the ticket fields list

The ticket fields list is divided into two tabs based on activation status. The default view on the Fields page is the list of Active fields. To view fields that have been deactivated, click the Inactive tab.

By default, ticket fields are listed in the order they were created. If you have a large number of fields, the list will be paginated. You can scroll through the pages using the controls at the bottom of the page:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/pagination.png)

### Searching the ticket fields list

You can search your list of ticket fields by entering a search value into the search box at the top of the page:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_fields_search.png)

Ticket fields are searchable by the following values:

- **Title**: The name given to a ticket field, including partial title
- **Field IDs**, unique numeric identifiers given to each ticket field, including partial ID numbers
- **Ticket field values**, the values created in a drop-down or multi-select field.

## Modifying and sorting on ticket field columns

You can customize the information displayed on the Fields page by adding and removing columns for the fields list.

Initially, there are four default columns applied to the fields list: Title, Field ID, Type, and Date modified.

The following columns may be available for inclusion in the fields list:

- **Active forms**, the number of forms a ticket field appears on. You can hover over the number to view a list of the forms using that field.

  Note: This column is only available to customers on Support Enterprise and Zendesk Suite Growth plans and above.
- **Field ID**, unique numeric identifiers given to each ticket field, including partial ID numbers
- **Type**, the ticket field’s format (Drop-down, multi-select, numeric, and the like).
- **Created by**, the admin who created the field.
- **Date created**, the date the field was created.
- **Date modified**, when the field was last edited.
- **Permissions**, including:
  - Editable for end-users
  - Visible for end-users
  - Required for agents
  - Required for end-users

  When displayed, the permissions options applied to the field are indicated by a check mark.

Note: Column choice is session-based; that is, if you add columns to the fields list, then log off and log in on a new device, the list reverts to the four default columns.

**To add or remove a column from the ticket field list**

1. On the Fields page, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)) to display the list of available columns. Columns currently applied to the list are indicated by a blue check mark.
2. Click the column(s) you want to apply to or remove from the ticket fields list. The change is applied to the list immediately.

**To sort your ticket fields by column**

1. Click the name of the column you want to use to sort your ticket field list. The list is reorganized based on the information in that column.
2. Click the column name again to reset the sort order.

## Filtering the ticket fields list

The Filter menu allows you to display only those ticket fields that meet certain criteria:

- **Type**: The ticket field’s format (Drop-down, multi-select, numeric, and the like).
- **Created by**: The ticket field's creation source (Admin, App, or Zendesk).
- **Permissions**: Agents only, Read-only for end-users, and Editable for end users.
- **Requirements**: Whether the field is required to solve a ticket or submit a request.
- **Status**: Active or inactive.

You can apply multiple filters to the list. If you use more than one filter, they are applied as an OR statement - that is, choosing the *Type > text* and *Created by app* filters will display all text-type ticket fields, regardless of their creator, as well as all fields created by an app, regardless of their field type.

**To apply filters to the ticket field list**

1. Click the **Filter** menu.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_fields_applied_fields.png)
2. Click the filters you want to apply to the ticket field list, then click **Apply filters**.

   The filters are applied immediately.

**To clear filters applied to the ticket field list**

- Click the **x** by the label name under the search box.

  Or click **Clear filters** to remove all filters.