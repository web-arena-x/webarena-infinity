# Managing trigger categories for ticket triggers

Source: https://support.zendesk.com/hc/en-us/articles/4408832263066-Managing-trigger-categories-for-ticket-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Objects and rules > Business rules >
Triggers

This article describes how admins and [agents in custom roles with business rules permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can manage
trigger categories for ticket triggers. This includes viewing categories, renaming categories,
rearranging ticket triggers within categories, moving ticket triggers between categories,
reordering categories, and deleting categories. To create trigger categories, see [Creating categories to organize ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408834781594).

This article includes the following sections:

- [Viewing ticket trigger categories](#topic_zr2_smn_tnb)
- [Reordering ticket trigger categories](#topic_avl_ksn_tnb)
- [Renaming ticket trigger categories](#topic_vwm_ftn_tnb)
- [Deleting ticket trigger categories](#topic_df5_y5n_tnb)

**Related articles:**

- [Creating categories to organize ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408834781594)

## Viewing ticket trigger categories

Trigger categories appear in the ticket triggers list. You can expand or collapse
categories to see which ticket triggers are included in each category.

**To view triggers categories**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Tickets** tab.
3. Click the expander (>) next to a category to show or hide ticket triggers in a
   category.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_categories_viewing.png)

   Categories can include both active and
   inactive ticket triggers. The **Status** drop-down allows you to control which type is
   visible.
4. Select **Active** from the **Status** drop-down to see the number of active
   ticket triggers in each category.
5. Select **Inactive** from the **Status** drop-down to see the number of inactive
   ticket triggers in each category.
6. To quickly collapse your categories view, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the column headings in the ticket triggers list, then
   select **Collapse all categories**.

## Reordering ticket trigger categories

You can reorder trigger categories to change the order in which the ticket
triggers run. This section describes how to reorder trigger categories. To reorder
individual ticket triggers, see [Reordering and sorting ticket
triggers](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_vnl_zpy_tb).

Keep in mind that the order you set for trigger categories must match the order
in which you want your ticket triggers to run. Run order has a big impact on how you decide
to create and organize ticket triggers within categories. For more information, see [Understanding when triggers run and fire](https://support.zendesk.com/hc/en-us/articles/4408886797466#topic_chq_xct_pbc).

**To reorder a trigger category**

1. In the ticket triggers list, click **Edit order** (at the top of the list).

   You’ll
   see a list of categories and ticket triggers in the default sort order.
2. Click the up (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/reorder_up.png)) or down (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/reorder_down.png)) arrows to move the category, along with all its triggers, up
   or down in the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_categories_order_tm.png)
3. **Save** your changes.

If you receive an error when you reorder your trigger categories, see [Trigger order wasn't updated](https://support.zendesk.com/hc/en-us/articles/4408881509914).

## Renaming ticket trigger categories

Renaming a category does not impact the ticket triggers included in the category.

**To rename a trigger category**

1. In the ticket triggers list, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the category you want to rename.
2. Select **Rename** from the menu.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_categories_rename.png)
3. Enter a new name for the category, then click **Update**.

## Deleting ticket trigger categories

Instead of deleting ticket triggers individually, you can delete all ticket triggers in a
category at the same time. Before you can delete a trigger category, all ticket triggers in
the category must be inactive or moved to another category. To delete or deactivate
individual ticket triggers, see [Deleting and deactivating ticket
triggers](https://support.zendesk.com/hc/en-us/articles/4408882237722-Managing-triggers#topic_jvv_kqy_tb).

**To delete a trigger category**

1. Make sure all triggers in the category are [inactive](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_jvv_kqy_tb).
2. From the **Status** drop-down at the top of the ticket triggers list, select
   **Inactive**.
3. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the category you want to delete, then select
   **Delete**.

   A count of all the ticket triggers that will be deleted with the
   category appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/triggers_categories_delete_tm.png)
4. Click **Delete category and triggers**.

   The category and all ticket
   triggers in the category are deleted.