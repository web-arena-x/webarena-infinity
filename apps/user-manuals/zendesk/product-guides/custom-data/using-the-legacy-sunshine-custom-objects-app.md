# Using the legacy Sunshine Custom Objects app

Source: https://support.zendesk.com/hc/en-us/articles/4408828715674-Using-the-legacy-Sunshine-Custom-Objects-app

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Important: A new custom object experience is available. See [Understanding the new custom objects](https://support.zendesk.com/hc/en-us/articles/5914453843994).

If you're using legacy
custom objects, you will continue to have access to your objects, records, and
relationships. All resources to aid in your continued use of legacy custom objects have been
labeled as "legacy." Custom object documentation without the "legacy" label applies only to
the new custom object experience.

Note: The legacy Sunshine Custom Objects app described in this article was never made generally available. It was released in early access and the program was closed. Zendesk is no longer accepting customer requests for this app.

With the legacy Sunshine Custom Objects app, agents can see custom object records
related to the ticket requester. In addition to the Zendesk native data objects for storing
and managing your customer data, custom objects provide you the ability to tailor your Zendesk
account to meet your business needs. For example, an e-commerce company might want to use
custom objects to look up information about a customer's orders, and respond with accurate
information about the status of a product's availability.

The legacy Custom Objects app brings records into the context of a ticket and
requester in Support, reducing an agent's need to navigate multiple interfaces to get a
complete picture of a requester's relationship to your business. The benefits include reduced
solve time and higher CSAT scores.

To populate the data needed for the app, you'll need to create custom objects,
records, and relationships to users, tickets, and more, through the [Sunshine API](https://developer.zendesk.com/rest_api/docs/sunshine/introduction), or in [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408834725402). To able to use this app you will need to have
relationships configured between one or more custom objects, and your users, tickets or
organizations.

The article includes the following sections:

- [About the legacy Sunshine Custom Objects app](#topic_uec_o41_wpo)
- [Viewing or editing related legacy objects](#topic_xtc_o41_wpo)
- [Filtering the available records](#topic_gq2_s11_wpo)

**Related articles and announcements**

- [Sunshine custom objects guide for admins](https://support.zendesk.com/hc/en-us/articles/4408834725402)

## About the legacy Sunshine Custom Objects app

Once you have created relationships to ticket requesters, agents can see the
related object records in the Custom Objects app on the ticket. For instructions on creating
custom objects and relationships, see [Sunshine custom objects guide for admins](https://support.zendesk.com/hc/en-us/articles/4408834725402). Agents can view any of
the related objects which have the following native Zendesk object types as a source:

- zen:ticket
- zen:organization
- zen:user

The Custom Objects app contains a tabbed interface that allows agents to either view and
edit related records, or filter records. In the **Related** tab, agents select a source,
and then an object from that source for display.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_obj_app_source.png)

When a related record is displayed, agents can click on the record and see the details for
it. Agents who have been granted permissions on the custom object can edit the object's
details. Agents can help keep object record data current by editing inaccurate custom object
records from within the app.

While working on tickets, agents may want to examine other unrelated object records, and to
possibly identify new relationships to create. In the **Filter** tab, agents can specify
queries to identify particular object records of interest. When an unrelated object is
identified that should be related to a ticket requester, agents can create a relationship in
the app. For example, an agent learns from another system that the customer has a
subscription that should be linked to her.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_obj_app_filter.png)

## Viewing or editing related legacy objects

When displaying a related object, you select the source or target of a relationship type,
and then you select the specific object from that source that you want to display. You can
select a source for your related-object results from the predefined native Zendesk object
types.

**To select related legacy objects for display**

1. In the ticket, select **Apps** from the upper-right toolbar.
2. Expand **Custom Objects**.
3. Select a relationship type between the ones that exist from the **Select
   relationship** menu.

   The app displays a list of custom object results for the
   relationship. This example shows the selection of the shoes\_order relationship from the
   zen:user relationships source.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_obj_app_results.png)
4. Click a result to see the object details.

   For example, an agent may want to examine
   the property in\_stock. The agent notes that the value of the property
   is zero, and can respond accordingly to the ticket requester about the
   order.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_obj_app_results.png)

**To edit a legacy object's details**

1. In the object details, click the edit icon to the right of any of the object's
   attributes.
2. Enter a new value for the attribute.
3. Click the check mark icon to save your change.

   The new attribute value is stored in
   the object record.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_obj_app_edit.png)

## Filtering the available records

You can filter and display all your available custom object records.

**To filter the displayed records**

1. In the ticket, select **Apps** from the upper-right toolbar.
2. Expand **Custom Objects**.
3. Select the **Filter** tab.
4. Select a custom object type from the **Select object** field.
5. Specify one or more attributes in which to search for a string in the **Select
   attributes** field.
6. Specify a full-word string for which you want to search in the **Includes** field.

   For example, you enter Acme as a brand name. Note these considerations:

   - You should enter a string value that matches a full word. An exact match must be
     found.
   - Entering a full word will return results that include multiple-word phrases.

     For
     example, a search for the string "Acme" will also return "Acme
     Corporation".

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_obj_app_filter.png)
7. Click **Filter**.

   The app displays a list of results for your search criteria.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_obj_app_results2.png)

**To edit an object**

1. In the results on the **Filter** tab, click an object to view its details.
2. Click the edit icon to the right of any of the object's attributes.
3. Enter a new value for the attribute.
4. Click the check mark icon to save your change.

   The new attribute value is stored in the object record.

**To add a relationship to a legacy object**

Agents can relate a found object from the **Filter** tab to zen:user, zen:ticket, or
zen:organization sources. When doing so, agents select one of the existing relationships for
the selected source.

1. Review the results on the **Filter** tab. You can click an object to view its
   details.
2. Click the plus icon to the right of the object for which you want to create a
   relationship.
3. Select a source from the **Relate to** menu to create a relationship.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_obj_app_relate.png)

   You can see the new relationship in the
   **Related** tab.

   Note these considerations that may affect your results:

   - Only the relationships that involve the selected source in the first step relating
     dropdown (zen:user, zen:ticket, and zen:organization) *and* the currently
     selected object type (here: shoes), will be displayed.
   - The **Filter** tab doesn't filter out objects that are already related. This is
     because it is possible to relate an object to a source through different relationship
     types, although this is not a recommended practice.