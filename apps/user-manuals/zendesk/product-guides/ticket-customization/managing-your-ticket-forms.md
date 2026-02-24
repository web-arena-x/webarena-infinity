# Managing your ticket forms

Source: https://support.zendesk.com/hc/en-us/articles/4408836460698-Managing-your-ticket-forms

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Location: Admin Center > Objects and rules > Tickets > Forms

A [ticket form](https://support.zendesk.com/hc/en-us/articles/4408888481178) is a set of ticket fields for a specific type of support request. If you have [created multiple ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858), use the Ticket forms page in Admin Center to manage them.

This article covers the following topics:

- [Changing the default ticket form](#topic_ldz_2rb_lk)
- [Activating and deactivating ticket forms](#topic_y1x_1bc_cdb)
- [Changing the order of your ticket forms](#topic_xrp_1bc_cdb)
- [Searching for and filtering ticket forms](#topic_nyh_1bc_cdb)
- [Deleting ticket forms](#topic_k1d_1bc_cdb)
- [Cloning ticket forms](#topic_b5w_rwd_t3b)
- [Managing service request forms](#topic_p3b_rwv_dgc)

To edit an individual ticket form, see [Editing ticket forms](https://support.zendesk.com/hc/en-us/articles/5494868102426). If you want to change the instructions end users see when selecting a ticket form or if you want to link directly to a ticket form, see [Presenting ticket forms to end users](https://support.zendesk.com/hc/en-us/articles/4408842873498).

## Changing the default ticket form

All Zendesk Suite and Support plans have at least one standard ticket form: *Default ticket form*. Some plans allow you to create additional, custom ticket forms, and Employee Service Suite plans include several additional standard ticket forms that are specific to HR and IT.

If you have only one ticket form, it is your default ticket form. If you create multiple ticket forms, then one of the forms will be set as the default. You can change the default ticket form at any time. The default form will always be visible to end users to ensure that you have a request form to display to end users in Zendesk Support.

If you do not have any other active ticket forms, the default ticket form automatically includes all of your active ticket fields, and any new active ticket fields you create automatically appear on your default form. However, when you have two or more active ticket forms, new active ticket fields you create are *not* automatically added to your default form; you have to manually add new ticket fields to your default form when you have multiple active forms.

**To change the default ticket form**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Move the cursor over the ticket form that you want to use as your default ticket form and then click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_forms_menu_icon.png)) on the right side when it appears.
3. Select **Make default**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_forms_make_default_v2.png)

   The new default is set.

   The ticket form that was previously set as default remains visible to end users. If you do not want that form to be visible to end users, you can edit the form and deselect the option **Form name for end users**.

If you're using multiple [brands](https://support.zendesk.com/hc/en-us/articles/4408822414490) Zendesk recommends keeping the default ticket form for your account assigned to all brands. If a brand can't access the default ticket form for the account, the first ticket form available to the brand that is [listed](#topic_xrp_1bc_cdb)
on the Ticket forms page will be used as the default. If the brand doesn't have any forms assigned, the default ticket form is used regardless.

## Activating and deactivating ticket forms

Ticket forms are active by default and available to agents. Any active forms that you've set as visible to end users will also be available to end users.

You can deactivate a ticket form if you do not want it to be available to agents and end users. Deactivating a ticket form does not affect tickets where the form was previously applied.

Active and inactive ticket forms are grouped accordingly in the **Ticket Forms** admin page.

**To activate or deactivate a ticket form**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Click the **Active** or **Inactive** tab.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_forms_active_tab.png)
3. Move the cursor over the ticket form that you want to activate or deactivate and then click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_forms_menu_icon.png)) on the right side when it appears.
4. Select **Activate** or **Deactivate**.

   The ticket form moves to the active or inactive tab, depending on the action you selected.

## Changing the order of your ticket forms

The order that ticket forms appear on the **Ticket Forms** admin page is also the order they appear in the drop-down list for agents in the ticket page and for end users in Zendesk Support. The first form in the list is used, by default, for AI agent tickets.

**To change the order of your ticket forms**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Click the name of the form you'd like to move, then drag it to a new position.

   The ticket forms appear in the new order.

   You can’t drag ticket forms to or from the Active and Inactive tabs.
3. Repeat if you'd like to move another ticket form to a new position.

## Searching for and filtering ticket forms

You can search for and filter ticket forms on the **Ticket Forms** admin page by brand.

**To search and filter for forms**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Select the tab you want to search and filter: **Ticket forms** or **Service request forms**.

   Service request forms are special ticket forms used exclusively for requests [submitted](https://support.zendesk.com/hc/en-us/articles/9443951695514)
   through the [service catalog](https://support.zendesk.com/hc/en-us/articles/8478940252698).
3. Enter a form title in the search bar or click **Filters**.
4. Select the filters you want to apply:
   - **Brand**: Filter by forms associated with specific brands or **Ticket forms without brands**.
   - **Status**: Filter by forms that are **active** or **inactive**.
5. (Optional) If you already applied filters, you can clear them by choosing **Clear filters**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_forms_clear_filters.png)

## Deleting ticket forms

You can delete any active or inactive ticket form. Deleting a ticket form does not affect tickets where the form was previously applied.

**To delete a ticket form**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Open the ticket form for editing.
3. In the upper-right corner, click the menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_forms_menu_icon.png)) and choose **Delete**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_forms_delete_v2.png)

   A confirmation screen displays.
4. Click **Delete** to delete the ticket form.

## Cloning ticket forms

Information about how to clone ticket forms is located in [Creating ticket forms to support multiple request types](https://support.zendesk.com/hc/en-us/articles/4408846520858).

## Managing service request forms

Service request forms are a special type of ticket forms. Unlike other ticket forms, service request forms are only used for requests [submitted](https://support.zendesk.com/hc/en-us/articles/4408846805530#topic_ijj_s2k_cgc) through the [service catalog](https://support.zendesk.com/hc/en-us/articles/8478940252698).
Service request forms can't be edited or deleted.

**To access a list of service catalog forms**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. On the Forms page, click the **Service request forms** tab.

   From this list, you can [add and modify](https://support.zendesk.com/hc/en-us/articles/4408834799770) a service request form's conditional fields or open [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c).