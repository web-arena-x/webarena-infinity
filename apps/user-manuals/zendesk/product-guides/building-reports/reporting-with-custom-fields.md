# Reporting with custom fields

Source: https://support.zendesk.com/hc/en-us/articles/4408824384538-Reporting-with-custom-fields

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

You can add custom fields to your Zendesk Support tickets to enable you to collect information that's not collected by default. For example, you could add a drop-down list to tickets that enables the requester of the ticket to choose their office location.

When your data is next synchronized with Explore, custom fields are also synchronized and can be used in your reports. This synchronization occurs every hour. Explore synchronizes ticket, user, and organization custom fields from Support.

For details about how to create and use custom fields in Support, see [Adding custom fields to your tickets and support request forms](https://support.zendesk.com/hc/en-us/articles/4408883152794-Adding-custom-fields-to-your-tickets-and-support-request-forms).

This article contains the following topics:

- [How custom fields synchronize with Explore](#topic_glv_tww_23b)
- [Finding custom fields in Explore](#topic_d2z_rxw_23b)
- [Custom fields example](#topic_tzq_zcs_4gb)
- [Tips for using custom fields in Explore](#topic_fpf_h1x_23b)

## How custom fields synchronize with Explore

When you create, edit, delete, or reactivate custom fields in Zendesk Support, the following happens in Explore:

- When a custom field is created or reactivated in Support, a corresponding metric or attribute is created in Explore at the next data sync (which can take between 1-2 hours). The custom field values must have been used in tickets, users, or organizations for them to appear under the corresponding metric or attribute in Explore.
- When a custom field title or value is updated in Support, the metric or attribute title or value is updated in Explore.
- When a custom field is deactivated in Support, the corresponding metric or attribute will no longer appear in new Explore reports, but will continue to display on existing reports where it was used.
- If you delete an active field without deactivating it first, it will not be deleted from Explore. When this happens, the tag associated with the deleted field value appears in Explore reports instead of the value's name.

 For example, if you had a custom ticket field value named "VIP Plan" with the tag "vip\_plan" and then you deleted the "VIP Plan" custom ticket field value, Explore reports would show "vip\_plan" as the attribute value instead of "VIP Plan." Additionally, if you then created a new drop-down field value with an identical tag to the one you just deleted, the attribute value in Explore reports would change to the new value you created.

 If you need help with a deleted field that was not deactivated first, [contact Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).
- When multiple custom fields share the same name, issues can occur. If a shared field name is used in a formula, Explore's formula editor always resolves that field as the custom field with that name that was created first. This means you can't create formulas with a custom field that shares the same name as another custom field and was created after the first one. If you have multiple custom fields with the same name, deactivate and delete the one that isn't needed, or rename it.
- If a custom field [uses dynamic content](https://support.zendesk.com/hc/en-us/articles/4408883892762), updates to the dynamic content itself don’t automatically sync with Explore. If you update dynamic content, you must also update the custom field that uses that content so that Explore pulls in the updated data. To trigger an update to the custom field, you can add a space to the field name, click Save, and then immediately remove the space and save again.
- Explore uses the default Zendesk account language for the dynamic content used in custom fields. This means that the field values are shown in the same language for all Explore users. The default language is synced by Explore during the latest field update. If the default language is updated, the custom field that uses dynamic content also needs to be updated to propagate the new default language to Explore custom field attributes.

## Finding custom fields in Explore

All ticket, user, organization, contact, lead, and deal custom fields are synced with Explore and automatically placed in the corresponding attribute or metric folders of the datasets. From there they can be selected and used on the reports or dashboards.

Only the latest field value is recorded in the standard Explore metrics and attributes. In the **Updates history** dataset, you can track updates to the fields by using the **Changes** attributes. For details, see [Metrics and attributes for Zendesk Support](metrics-and-attributes-for-zendesk-support.md#topic_zdl_flq_4y).

Note: The Support - Backlog history and Support - Group SLAs datasets do not contain custom fields.

Use the tables below to help you understand where to find your custom fields in Explore.

Remember to double-check which Explore folder you're selecting the metric or attribute from. For example, you might see the same field name under both **Ticket custom fields** and **Requester/user custom fields**, and the value might vary depending on which you select.

Table 1. For Zendesk Support

| Field type | Object type in Explore | Explore folder |
| --- | --- | --- |
| Drop-down Multi-select Text (single line) Multi-line Checkbox Credit card Regex | Attribute | Ticket custom fields Requester/User custom fields Requester/User organization custom fields |
| Date | Attribute | Each date attribute is represented by multiple time dimensions placed in the attribute’s individual folder |
| Numeric Decimal | Metric | Numeric custom fields |
| Lookup relationship This applies only to lookup relationship fields that are present on standard objects, including tickets, users, and organizations. Lookup relationship fields present on custom objects cannot be reported on. However, for lookup relationship fields present on a standard object that link to a custom object, Explore can return the ID and name of the custom object. | Attribute Relationship lookup data is available only from April 6, 2023 onward. Relationship lookup data related to custom objects is available only from September 18, 2023 onward. For lookup fields with a related object of User, if a user has no tickets (as either a Requester or Submitter), then that user record isn't returned in Explore. For more information, see [Using lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770). | Ticket custom fields Requester/User custom fields Requester/User organization custom fields The attribute names of lookup fields with a related object of Ticket are appended with " - id". The attribute names of lookup fields with a related object of User or Organization are appended with either " - id" or " - name". Additionally, if an " - id" field is related to a custom object, you can click the attribute’s value in a report and select **Open link** to see the custom object record. For details, see [Viewing lookup relationships](https://support.zendesk.com/hc/en-us/articles/4591924111770#topic_lzc_235_z5b). |

Note: If you've set up [multiple organizations for users](https://support.zendesk.com/hc/en-us/articles/4408838309530-Managing-users-in-multiple-organizations-Professional-and-Enterprise-#topic_spj_srp_dp), Explore will always report custom field information from the [default organization](https://support.zendesk.com/hc/en-us/articles/4408838309530-Managing-users-in-multiple-organizations-Professional-and-Enterprise-#topic_cjl_trp_dp). This means that any additional organizations added will report incorrect information.

## Custom fields example

In this example, you'll create a custom field containing a drop-down list that lets agents add the requesters office floor to a ticket. You'll then synchronize this with Explore and finally, create a simple report showing tickets associated with each office floor. You must be a Support administrator to add the custom field.

### Create the custom field in Support

Perform the following actions in Zendesk Support.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Fields**.
2. Click the **Add field** button.
3. Click **New Field** at the top of the page, and enter a title for the field, in this case **Office location**.
4. From the list of field types, click **Drop-down**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_custom_fields1.png)
5. In the properties for the list, enter a title for the list, an optional description, and configure permissions as to who can set values for this field.

   For detailed information about the options on this page, see [Adding custom fields to your tickets and support request forms](https://support.zendesk.com/hc/en-us/articles/4408883152794-Adding-custom-fields-to-your-tickets-and-support-request-forms).
6. In the **Field values** section, enter each line of the list. For this example, enter **1st Floor**, **2nd Floor**, **3rd Floor**, **4th Floor**, and **5th Floor**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_custom_fields2.png)
7. Click **Save**.
8. Add the custom field to the ticket forms you want to use it with. For help, see [Adding custom fields to your tickets and support request forms](https://support.zendesk.com/hc/en-us/articles/4408883152794-Adding-custom-fields-to-your-tickets-and-support-request-forms).

The new custom field is now available in your Support tickets. Before you move on, create a few tickets using this new field, or update the field on some existing tickets.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_custom_fields3.png)

Tip: You might need to refresh your browser window before you see the new field.

### Create the Explore report

Perform the following actions in Zendesk Explore after your data has synchronized. Synchronization takes place once every hour.

1. In Explore, create a new report using the **Support: Tickets** dataset.
   For more help, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530-Creating-queries).
2. In the **Metrics** panel, add the **Tickets** metric.
3. In the **Rows** panel, expand **Ticket custom fields**, and then click **Office location**. It might take a few seconds to display the custom field.

   Tip: To find custom fields for users, expand **User custom fields** and for organizations, expand **Organization custom fields**.
4. Explore generates the report in a table similar to the following:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_custom_fields5.png)

   Tip: Previously, Explore displayed custom field values as a tag instead of the actual value. If you have report filters, calculated metrics, or calculated attributes that reference the tag values, update these with the new custom field value to ensure they continue to work correctly.
5. Give the report a name, and then save it.

## Tips for using custom fields in Explore

Use the tips in the following table to help you understand how custom fields work in Explore and how you can get the best from them:

| Field type (from Zendesk Support) | Values | Usage |
| --- | --- | --- |
| Drop-down Multi-select | Agents or end-users select values from drop-down and multi-select fields. These values appear in Explore as they are recorded in the Support UI. However, if a value is later deleted from the field in Support, its tag will be displayed in Explore instead of the actual value. | The drop-down field is commonly used to track information about the user or their request. Some common examples are category, issue type, region, plan, etc. Drop-down fields work in a similar way to built-in Support fields like **Type** or **Priority**. Use the multi-select field when multiple values are required. For example, you could record multiple product areas, services provided, or areas of interest. Use this field type when a drop-down field cannot be used as an alternative. Reporting on this field type is more complex than reporting for a drop-down field. For example, while you can use the [CONTAINS](../writing-formulas/explore-functions-reference.md#topic_l1t_plf_dhb) or [REGEX\_MATCH](../writing-formulas/explore-functions-reference.md#topic_i1d_vlf_dhb) function to create a custom attribute for multi-select field values, you cannot create an attribute that simultaneously includes one value while excluding another. |
| Checkbox | Checkbox fields have three values:   - **True** if the box is checked - **False** if the box is not checked - **NULL** if the ticket was closed before the checkbox was   created (for ticket custom fields), or if the user or   organization was created before the checkbox was created   (for requester/user organization custom fields) | The checkbox is the simplest field type to use and is commonly applied as a report filter. Examples: Submitted for review, Serviced, Completed. |
| Text (single line) Multi-line | Text field values are manually typed in by agents or end users, meaning the field might contain a large number of values. Additionally, the values entered might be inconsistent or contain spelling mistakes. | Normally, text fields are used as notes to record additional unstructured data. This makes them less useful for reporting purposes. However, they can still be added to table reports to provide context about tickets or users. |
| Credit card Regex | Values for these fields are also manually typed in by agents or end users, but the format is controlled by the credit card number format or custom regular expression. | Because these fields provide a more structured way of recording data, they can be more useful for reporting purposes than standard text fields. |
| Date | Each date attribute is represented by multiple time dimensions like Date, Month, Year, etc. | Enables you to record dates or deadlines, like date of birth, project end date, and booking date. They can be used in reports, dashboard filters or calculated metrics in the same way as any built-in time attributes. |
| Numeric Decimal | Numeric and decimal fields allow storing numeric values that can be computed in the same way as any other metric using the available Explore aggregators. | These fields are similar to the system metrics, like Agent Replies or Resolution Time. Examples you could use are revenue, project length, or area in square meters. |

Note: The maximum length of a custom field is 65,535 characters after encoding.