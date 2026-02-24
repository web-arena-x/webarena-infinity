# Adding custom object records to capture custom data

Source: https://support.zendesk.com/hc/en-us/articles/5402508938778-Adding-custom-object-records-to-capture-custom-data

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Location: 
Support > Custom objects

Zendesk provides many types of native data objects for storing and managing
your customer
data, including tickets, users, organizations, and more. These are called
*standard
objects*. However, standard
objects can't provide every possible type of data
object that your organization might want. With custom objects, admins
can
[create custom objects](https://support.zendesk.com/hc/en-us/articles/5392409465370)
to capture data that doesn't fit into
those standard objects. Then,
[agents with permission](https://support.zendesk.com/hc/en-us/articles/6034260247066)
can add that information to Zendesk
by creating custom object records.

This article contains the following topics:

- [Understanding custom objects](#topic_f2g_ty4_mwb)
- [Adding a custom object record](#topic_ibh_1bp_mwb)
- [Adding a related custom object record](#topic_hhc_dbp_mwb)
- [Adding attachments to a custom object record](#topic_abp_byp_pgc)
- [Searching for custom object records](#topic_bxl_dxq_fyb)

If you're looking to update custom object records, see
[Managing custom object records](https://support.zendesk.com/hc/en-us/articles/6093145333786).

## Understanding custom objects

A custom object is a user-defined object with unique fields and permissions.
Custom objects can be almost anything, including a product, contract,
delivery
driver, asset, or event. Think of a custom object as a data table.
Each of the
custom object's fields is a column in the table. After the table
is created and the
columns are added, agents can add data to the table. Each row of
data in the table
represents a custom object record. Another way to think of a custom
object is as a
schema or model, which is created and made available to users to
add data, such as
in a ticket or form. Every time an agent uses the custom object to
add data to
Zendesk or an admin bulk uploads data for an object, new records
are created. These
records can then interact with business rules, such as triggers and
lookup
relationship fields.

Here's an example. Let's say you're a car rental company. A Zendesk
admin at your company created
two custom objects to track vehicles and reservations:
*vehicles* and
*rental
agreements*. Using
these custom objects, every vehicle and reservation can be
tracked within Zendesk. Now, when a customer contacts the company
to rent a car, a
ticket is created for them. The standard ticket and user objects
hold information
about the customer and their request. In your account, an admin defined
lookup
relationship fields connecting the rental agreements and vehicles
to tickets and
users, so everything the agents need to resolve the request is now
available in the
ticket. They're able to search records of available cars in the requested
location
and date, create a rental agreement, and relate the rental agreement
to the vehicle
and user.

Later, the customer has an issue with their rental car, and they
contact your company again.
Again, a ticket is created for them and is associated with the user,
the vehicle,
and the rental agreement. Because each of these custom objects has
been added to the
ticket form, agents can see details about both the vehicle and the
rental agreement within
the ticket while they assist the customer.

## Adding a custom object record

To add data to a custom object, you create a record. Within the record
you'll add the
information to the custom object's fields. Admins and
[agents with permission](https://support.zendesk.com/hc/en-us/articles/6034260247066)
can edit records.

**To create a custom object record**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Custom
   objects** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_custom_objects_records_page.png)) in the sidebar.
2. Select the custom object you'd like to add a record for.
3. On the records page for that custom object, click
   **Add**.
4. Enter the required information. If you have it, you can also
   add the optional
   information.

   If autonumbering is turned on for the custom object, the
   record name field is pre-defined and automatically generated
   when the record
   is added.
5. (Optional) If the object is configured to allow record icons,
   you can click the
   placeholder icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/edit_custom_object_record_icon.png))
   next to
   **Add *object name***,
   select **Upload image**, and select
   and upload an icon for the record.
6. Click **Add**.

## Adding a related custom object record

When an admin creates a custom object, they also define its relationship
to other
standard and custom objects in Zendesk. Adding related records helps
connect this
new record to other records in Zendesk as the admin intended. From
the Custom object
records page, you can add related custom object records. This isn't
supported for
adding related standard object records.

To help you keep track of which object you're adding a related record
to, the tab in
agent workspace includes the object's name as a subtitle.

**To add a related record**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Custom
   objects** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_custom_objects_records_page.png)) in the sidebar.
2. Select the custom object for which you'd like to edit a record.
3. Click the name of the record you want to add a related record
   to.
4. Scroll to find the related object you want to add a record
   for and click
   **+Add**.
5. Enter the information you have for the related object, then
   click
   **Add**.

## Adding attachments to a custom object record

When an admin creates a custom object, they can decide whether to
allow attachments
to be added to the object's records. If they do, admins and agents
with permission
to edit the custom object's records can add up to five attachments
per record. Each
attachment can't exceed 10MB in size.

**To add an attachment to a record**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Custom
   objects** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_custom_objects_records_page.png)) in the sidebar.
2. Select the custom object for which you'd like to edit a record.
3. Click the record's name to view the record's details, then
   click the
   **Attachments** tab.
4. Click **Upload attachment** and
   select the file from the file
   manager.

   Alternatively, you can drag and drop files onto the list
   of
   attachments to add them.

## Searching for custom object records

After creating custom object records, they are visible in the Custom
object records
page in Zendesk Support. For more information about using the record
lists and
searching for records, see
[About the Custom object records page](https://support.zendesk.com/hc/en-us/articles/6088606067866).