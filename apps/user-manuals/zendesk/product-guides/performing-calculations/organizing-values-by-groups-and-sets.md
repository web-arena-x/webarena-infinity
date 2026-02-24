# Organizing values by groups and sets

Source: https://support.zendesk.com/hc/en-us/articles/4408836227866-Organizing-values-by-groups-and-sets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

You can use groups and sets to organize your results. Groups and sets can be used in calculated elements, unlike filtered attributes. This is useful if you only want to perform calculations on specific values in an attribute.

- **Groups** are a way to group the results from an attribute together. For example, you could create an attribute called UK Offices that groups together all organizations in the UK so that you only need to refer to these once in your report.
- **Sets** are a way of ensuring that only certain results from an attribute will be included. For example, you might want to add a list of priority one requesters (such as director level staff) as a set, so you can restrict certain results to just those people.

This article contains the following sections:

- [Creating groups](#topic_epc_gw1_fv)
- [Creating sets](#topic_fsd_gw1_fv)
- [Deleting and renaming groups and sets](#topic_yss_xdn_3gb)

## Creating groups

A *group* attribute is a way to organize another attribute's values. A group attribute has the following advantages over a set:

- You can use groups to look at the aggregated results for an attribute values, so you can compare results at a more granular level.
- You can create multiple, exclusive groups from an attribute, so you can organize your results into a hierarchy.

**To create a new group attribute**

1. From the calculation menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_calculations.png)), choose **Group**.
2. On the **Group** panel, enter a name for your group.
3. Under **Computed from**, choose an attribute. This example uses the **Ticket tags** attribute to create a group for various ticket tags.
4. Select the values you want to add to a group.
5. Click the **+** icon to add values to a group.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_group.png)
6. If you want to add more values to the open group, select the values then click the right arrow. If you want to remove values from the open group, select the value then click the left arrow. You can create multiple groups at the same time.
7. Select the location for values that don't fall into one of the groups you created.
   There are three options:
   - **Put left values into another group**: Values will be placed in an other group.
   - **Keep left values "as is"**: Values will be left as individual values.
   - **Remove left values**: Values will be removed from your attribute.
8. Click the **Save** button when you are finished selecting your values. You've now created a new group that shows only the items you chose. Before you can see its results, you need to add it to a report.
9. Add your group attribute to the **Rows** or **Columns** panel of any report.

## Creating sets

A *set* is a list of selected attribute values. You can use the set calculated attribute to create a new attribute containing only specific values. You can also use sets to rename or reorder your values.

Note: When you create a dashboard data filter using a set as the data filter column, only the attributes that are part of that set will be available for the dashboard viewer to choose from.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_set.png)

In addition to the normal set calculation there are two other types of sets you can create:

- [Set](#topic_cts_3bs_qmb)
- [Ordered set](#topic_ssy_cnw_fv)
- [Renamed set](#topic_exv_bnw_fv)

### Set

A set is used to create a reusable list of attribute values. For example, you could create a set based on the **Assignee name** attribute, but only returning the names you choose. In this example, you'll create a new attribute that only returns results for the names you choose.

**To create a set**

1. In the report builder, open the Calculations menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_calculations.png)).
2. Select the **Set** option.
3. On the **Set** panel under **Computed from**, choose **Assignee name**.
4. From the list of assignees, choose the names you want.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_set_new.png)
5. Give your set a name, then click **Save**.

You can now use your new set in any of your Explore reports.

### Ordered set

An *ordered set* is useful when you want to arrange values in an order that is not alphabetical or numerical. For example, you could use an ordered set to create a funnel report for ticket priority.

Note: When using an ordered set avoid using the sort option in the result manipulation menu. It will override the order you specify.

**To create an ordered set**

1. In the report builder, open the Calculations menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_calculations.png)).
2. Select the **Ordered set** option.
3. On the **Custom order** panel, enter a name for your set. In the example below, the ordered set is named Priority.
4. From the **Computed from** drop-down, choose the attribute you want to use to make your set.
5. Drag and drop values until they are in the preferred order.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_ordered_set.png)
6. When you are finished, click **Save**.

You can now use your new attribute in any Explore report.

### Renamed set

A *renamed set* can be used to shorten results, create aliases, or replace technical text with more common labels. You can use renaming as an alternative to groups by giving several values the same name.

**To create a renamed set**

1. In the calculations menu, select **Renamed set**.
2. On the **Rename values** panel, enter a name for your renamed set.
3. From the **Computed from** dropdown, choose the attribute you want to use to make your set.
4. Enter the new value names for each attribute result in the text boxes.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_renamed.png)
5. When you are finished renaming your values, click **Save**.
6. Add your renamed set to your report.

## Deleting and renaming groups and sets

You can delete or rename groups and sets you created in the organize data structure menu.

**To delete or rename a group or set**

1. In an Explore report, click one of the attribute panels (like **Columns** or **Rows**), then click **Add**.
2. Expand **Calculated attributes**, then click the pen icon next to the attribute containing the group or set you want to edit or delete.
3. On the **Rename values** panel, you can enter a new name for the attribute or click **Options** > **Delete** to remove it.

   ![Deleting or editing a renamed set.](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_metric_update_5.png)