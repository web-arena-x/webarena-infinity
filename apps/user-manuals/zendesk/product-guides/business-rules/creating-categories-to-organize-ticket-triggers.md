# Creating categories to organize ticket triggers 

Source: https://support.zendesk.com/hc/en-us/articles/4408834781594-Creating-categories-to-organize-ticket-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Objects and rules > Business rules >
Triggers

Ticket trigger *categories* allow you to visually group ticket triggers for easier organization and management. This article describes how admins and [agents in custom roles with business rules permissions](https://support.zendesk.com/hc/en-us/articles/4408882153882) can create ticket trigger categories.

This article includes the following sections:

- [About ticket trigger categories](#topic_kkt_22f_mnb)
- [Creating categories for ticket triggers](#topic_vbd_2ym_tnb)
- [Organizing ticket triggers within categories](#topic_cdk_m1n_tnb)
- [Using the Zendesk API for ticket trigger categories](#topic_v42_wqj_bpb)

**Related articles:**

- [Managing ticket trigger categories](https://support.zendesk.com/hc/en-us/articles/4408832263066)

## **About ticket trigger categories**

To help you manage ticket triggers in your account, you can add additional ticket trigger categories. Ticket trigger categories enable you to arrange ticket triggers into groups or collections based on trigger functions or other criteria. This feature is particularly useful for accounts that have a large number of ticket triggers. You can expand or collapse the categories to show or hide triggers in each collection.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_categories_all2.png)

When you decide how to group your ticket triggers into categories, keep in mind that the order you set for ticket trigger categories must match the order in which you want triggers to run. Run order will have a big impact on how you decide to create and organize triggers within categories. For example, in the illustration above, all triggers in the Email Triggers category run before any triggers in the API Triggers category. For more information, see [Understanding when ticket triggers run and fire](https://support.zendesk.com/hc/en-us/articles/4408822236058-About-triggers-and-how-they-work#h_15524764971513292862138) and the best practices for [ordering your ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_vnl_zpy_tb).

## Creating categories for ticket triggers

You can create new trigger categories and add ticket triggers to them.

**To create a trigger category for ticket triggers**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Select the **Tickets** tab.
3. Open the **Add trigger** drop-down menu at the top of the tab and select **Add category**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_categories_add_menu.png)
4. Enter a name for the category and click **Add**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_categories_name.png)

   A new category appears at the bottom of the ticket triggers list. You can create new ticket triggers and add them to the category, or move existing ticket triggers to the category.
5. To create a new ticket trigger and add it to the category, click **+Add trigger** in the category.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_categories_add_button.png)

   For details on adding triggers, see [Creating ticket triggers for automatic ticket updates and notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466).
6. To move an existing ticket trigger to the category, you can [drag-and-drop it](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_vnl_zpy_tb) into the category or [edit the trigger](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_dwq_zoy_tb) and select the **Category**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_category_change.png)

   You can also [reorder triggers](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_vnl_zpy_tb) using drag-and-drop to move ticket triggers between categories.

## Organizing ticket triggers within categories

Once you've added trigger categories, you can do the following to organize ticket triggers within categories:

- To set the order of ticket triggers within a category, see [reordering ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_vnl_zpy_tb).
- To move ticket triggers from one category to another, you can:
 - Drag-and-drop one or more ticket triggers between categories. For more information on how to drag-and-drop triggers, see [Reordering triggers](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_vnl_zpy_tb).
 - Select the checkbox next to one or more ticket triggers, click **Move to category**, select the category, and click **Move**. When using this method to move ticket triggers into a category, their order will be the same as they were in the original category.
 - [Edit](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_dwq_zoy_tb)
    the ticket trigger and select a new **Category**.
- To add a new ticket trigger to a specific location in the triggers list, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to a ticket trigger, then choose **Add trigger below** from the menu.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_categories_add_below.png)
- To delete a ticket trigger from a category, see [Deleting ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_fqc_2m2_zsb).

## Using the Zendesk API for ticket trigger categories

Once you are using trigger categories, you can designate a category when creating a new ticket trigger via the Zendesk API. If you don’t specify a category when creating a new ticket trigger, Zendesk will select a category for you. You’ll also be able to make changes to trigger categories themselves through the API. See our [API documentation](https://developer.zendesk.com/rest_api/docs/support/triggers).