# Adding custom ticket fields to your tickets and forms

Source: https://support.zendesk.com/hc/en-us/articles/4408883152794-Adding-custom-ticket-fields-to-your-tickets-and-forms

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Create custom ticket fields to gather detailed information from customers and agents. These fields can be visible to agents only or both agents and end users, and can be used in triggers, automations, and reports. Admins can clone existing fields and manage their visibility and requirements. Note that deleting a field removes its data unless it's a tag-generating field like drop-down or checkbox.

Location: Admin Center > Objects and rules > Tickets > Fields

You can add [numerous types of custom fields](https://support.zendesk.com/hc/en-us/articles/4408838961562) to ticket forms and make them visible to agents only or to both agents and end users.

After you create your custom ticket field, you can use it in triggers, automations, macros, and views. On Suite Professional and above, you can report on custom ticket fields in Explore.

You must be an administrator to create custom ticket fields and add them to ticket forms.

Topics covered in this article:

- [How custom ticket fields work](#topic_upd_ynk_xj)
- [Adding a custom ticket field for agents and end users](#topic_ubz_ynk_xj)
- [Understanding the persistence of custom field data](#topic_jkc_m4d_hk)

Related articles:

- [Managing custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4408828883738)
- [Editing and managing ticket forms](https://support.zendesk.com/hc/en-us/articles/5494868102426)

## How custom ticket fields work

Custom ticket fields are typically used to gather more information about the support issue or product or service. You can add custom fields to your tickets for agents and you can also add them to your Help Center Submit a Request form if you want end users to see the custom field. Custom ticket fields can be required or optional.

Note: Custom ticket fields that are required for agents to solve a ticket can be bypassed by triggers, automations, and API updates when solving and closing tickets.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/submit_a_request.png)

Drop-down list, multi-select, and checkbox custom fields generate tags that can also be used in automations, macros, triggers, reports, and views (see [Understanding custom ticket fields, tags, and business rules](https://support.zendesk.com/hc/en-us/articles/4408834953114#topic_ext_est_kc)). Lookup relationship fields can be used in triggers and views (see [Using lookup relationship fields in triggers and views](https://support.zendesk.com/hc/en-us/articles/4591924111770#topic_pgk_llh_vtb). All custom fields can be referenced as placeholders (see [Placeholders for custom fields](https://support.zendesk.com/hc/en-us/articles/4408887218330#topic_nfp_nja_vb)).

## Creating custom ticket fields

You can add custom fields to tickets to gather more information about the customer or issue. Fields can be visible to agents only or to both agents and end users.

You can permit end users to view the custom field in their ticket by making the field visible, or you can add the custom field to the Support Request form by making the field both visible and editable.

Before you begin, see [Optimizing your ticket form](https://support.zendesk.com/hc/en-us/articles/4408888481178) to understand ticket fields and do some planning to build an optimal ticket form.

Tip: Check out [The 'Resolution' field](https://support.zendesk.com/hc/en-us/articles/4408822200346) and [The 'About' field](https://support.zendesk.com/hc/en-us/articles/4409155792026) to learn about two custom fields used by Zendesk.

You must be an administrator to create custom ticket fields.

The following video gives you an overview of how to create custom ticket fields:

Creating custom ticket fields [1:41]

**To add a custom ticket field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Fields**.
2. Click **Add field**.
3. Select a **field type**, then enter a **Display name**.

   When naming custom fields, don't use reserved system or feature names such as "channel." These names are reserved by Zendesk and won't work in custom fields.
4. (Optional) Enter a **Description** for the custom field. This is visible to admins only.
5. Under **Permissions**, select an option:

   - **Agents can edit**: Only agents can view and edit the field. It appears in tickets.
   - **Customers can edit**: Agents and end users can view and edit the field. It appears in tickets and in the support request form in the help center.
   - **Customers can view**: Agents can view and edit the field. End users can only view the field. It appears in tickets and on end users' [requests](https://support.zendesk.com/hc/en-us/articles/4408846805530#topic_qgd_mqd_yy), but isn't included in the support request form in the help center.

   For a single ticket form, the new field automatically appears in your ticket form. If you use multiple ticket forms, you'll have to manually add the field to any ticket forms you'd like to include it in.
6. If the field is visible to customers, enter a **Title shown to customers** and **Description shown to customers**.

   The customer title and description options aren't available if the field is only visible to agents. Descriptions appear in plain text, with no line breaks.
7. If the agent must complete the field to solve the ticket, select **Required to solve a ticket**.

   Note: Required fields for solving a ticket can be bypassed by triggers and automations . These fields are also bypassed when an agent merges a ticket.
8. If the end user must complete this field to submit the ticket, select **Required to submit a request**.
9. Enter an optional **Description shown to end users**.
10. Configure any additional options, depending on your field type.
    - **Field option** (checkbox fields only, optional):

      Enter a tag to apply to a ticket when the checkbox is selected.
    - **Field validation** (regex fields only):

      Enter a regular expression to create an input mask to validate entry.
    - **Field values** (drop-down and multi-select fields):
      - Enter a value for each option to include in the list, along with an associated tag.

        Each tag must be unique (see [Understanding tags and fields](https://support.zendesk.com/hc/en-us/articles/4408881943194)). You can [bulk import](https://support.zendesk.com/hc/en-us/articles/4408836502682) field values if you have a large number to add. Click the **X** to remove a value.
      - Click **Sort ascending** or use the grabber icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/drag_and_drop_handle.png)) to manually reorder the field values.
      - To create a nested drop-down list, separate categories and values with a double colon (::). See [Organizing drop-down lists](https://support.zendesk.com/hc/en-us/articles/4408829395738).
    - **Related object** and **Set a filter** (lookup relationship fields only)

      Select the type of object to relate, and optionally define filters that restrict possible values for the field. See [Adding lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770#topic_kmz_wl3_ttb).
11. (Optional) Specify a **Default value** for the custom field.

    In a drop-down list, the default value applies only to new tickets created by agents through the Support interface or created by users wherever the ticket form is displayed. If you change an existing ticket form to one with a drop-down list with a default option, the default option is not displayed and is shown as blank.
12. Click **Save** or, to create another custom field, click the drop-down icon and select **Save and add another**.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_fields_save_menu.png)

    If you have a single ticket form, the new field automatically appears in your ticket form.

    (Enterprise only) If you have multiple ticket forms, [edit the ticket forms](https://support.zendesk.com/hc/en-us/articles/5494868102426#topic_c5x_l3b_lk) where you want the field to appear, drag the field from the right onto the ticket form, then click **Save**.
    Repeat for additional ticket forms.
13. If needed, you can [reorder your custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4420210121114#topic_j2z_wy5_dfc).

The custom field appears on new tickets. It also appears on less-than-closed, closed, and archived tickets with a null '-' or empty value.

If the field does not appear on a new ticket, you might need to restart your browser.

Not all custom field types are available across business rules and views. For a list of which custom fields apply, see [Using custom ticket fields in business rules and views](https://support.zendesk.com/hc/en-us/articles/4408887162394).

On Suite Professional and above, you can [report on custom fields in Explore](../building-reports/reporting-with-custom-fields.md).

## Cloning custom ticket fields

Administrators and agents in custom roles with permission can create new custom fields from scratch or clone existing ticket fields and modify them as needed.

**To clone a custom ticket field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Fields**.
2. Hover over the row of the user field you want to clone, then click the option menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Clone**.

   A detailed view of the ticket field's settings is displayed.
3. Edit the **Display name** so that it is unique.
4. Set any other options for your field, depending on the type.
5. Click **Save**.

   If you have a single ticket form, the new field automatically appears in your ticket form.

   (Enterprise only) If you have multiple ticket forms, [edit the ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858#topic_c5x_l3b_lk) where you want the field to appear, drag the field from the right onto the ticket form, then click **Save**.
   Repeat for additional ticket forms.
6. If needed, you can [reorder your ticket fields](https://support.zendesk.com/hc/en-us/articles/4408828883738#topic_wrl_jm4_ht).

## Understanding the persistence of custom field data

If you delete a custom field, the data from the custom field is not preserved in existing tickets, including closed tickets. The data is preserved only if the custom field also adds a tag to a ticket. The three custom fields that add tags are the drop-down list, the checkbox, and multi-select fields. If you delete one of these custom fields, then the data in tickets persist as tags.

For example, suppose you have a drop-down list in your ticket form to associate tickets with different product names. After a while, a decision is made to stop providing support for one of the products. If you remove the product from the drop-down list, the product name persists in existing tickets as a tag. If however you use a text field to record a product ID and you delete the text field, the product ID is not preserved in your tickets.