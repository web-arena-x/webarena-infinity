# Editing and managing custom omnichannel routing queues

Source: https://support.zendesk.com/hc/en-us/articles/6716541571994-Editing-and-managing-custom-omnichannel-routing-queues

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Location:  Admin Center > Objects and rules > Omnichannel routing >
Queues

If you're using [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) with [custom queues](https://support.zendesk.com/hc/en-us/articles/6712096584090), you might need to modify your queues from
time to time. You must have the [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) to use omnichannel routing.

This article includes the following topics:

- [Reordering your queues list](#topic_kkb_g43_j1c)
- [Viewing or editing a queue configuration](#topic_tqm_5n3_j1c)
- [Deleting a queue](#topic_qxm_wn3_j1c)

If you need to create custom queues, see [Creating additional omnichannel routing queues](https://support.zendesk.com/hc/en-us/articles/6716530152858).

## Reordering your queues list

Omnichannel routing evaluates queues in the order they are listed on the Queues page.
As soon as a ticket meets a queue's conditions, it's added to that queue, and the
routing engine moves on to the next ticket awaiting placement in a queue.

**To reorder your queues**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Omnichannel routing >
   Queues**.
2. Use the drag-and-drop icons (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/drag_and_drop_handle.png)) in the **Order** column to
   reorder your queues as needed.

## Viewing or editing a queue configuration

Sometimes it's necessary to check on and adjust settings after you create a queue.
Changes to a queue are applied to new tickets entering the queue. Tickets already in
the queue are routed based on the queue's configuration at the time the tickets
entered the queue.

Note: If you're editing the
conditions for a custom queue that distributes tickets between subqueues, you
must deselect the subqueue option in order to save your changes. After the
updated conditions are saved, you can re-select and configure the subqueues as
needed.

**To view or edit a queue's configuration**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Omnichannel routing >
   Queues**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the queue you want to view or edit and
   then click **Edit**.
3. Make your changes and click **Save**.

## Deleting a queue

After a queue is deleted, no new tickets can be assigned to that queue. However, if
there are still tickets in a queue when it's deleted, the tickets continue to be
routed as if from that queue to the primary and secondary groups. Deleting a queue
that still contains tickets can negatively affect the routing of those tickets.

Deleting a queue is permanent.

**To delete a queue**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Omnichannel routing >
   Queues**.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the queue you want to view or edit and
   click **Delete**.
3. In the confirmation dialog, click **Delete queue**.