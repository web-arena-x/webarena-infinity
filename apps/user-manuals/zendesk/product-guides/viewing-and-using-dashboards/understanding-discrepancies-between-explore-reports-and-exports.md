# Understanding discrepancies between Explore reports and exports

Source: https://support.zendesk.com/hc/en-us/articles/4944328779162-Understanding-discrepancies-between-Explore-reports-and-exports

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

You might [schedule dashboard reports](https://support.zendesk.com/hc/en-us/articles/4408843602714) out of Explore to deliver PDFs to your team. Or, you might manually pull numbers every month and put them in a spreadsheet. You might also [create reports](https://support.zendesk.com/hc/en-us/articles/4408821589530) in Explore for the same numbers. If these methods show different results, that can be confusing—why don’t the numbers match up?

As you dig into these discrepancies, the key point to remember is that PDFs and spreadsheets are static, while Explore is dynamic.

This article contains the following topics:

- [Why results change](#topic_fgf_1mt_v5b)
- [Keeping numbers in perspective](#topic_wxc_hmt_v5b)
- [Using the right aggregators](#topic_n5w_hmt_v5b)
- [Conclusion](#topic_zxd_jmt_v5b)

## Why results change

As an example, say you exported data on August 1 for the whole month of July and put it into a spreadsheet. But later, in September, you run another report in Explore on the same data, and it shows different numbers for July.

| July column based on an export run in August: | July column in a report run in Explore in September: |
| | |

Read on to learn:

- [Why is there a difference in tickets created?](#topic_cz2_bmt_v5b)
- [Why is there a difference in tickets solved?](#topic_fyy_cmt_v5b)
- [Why is there a difference in tickets in a certain category?](#topic_imh_2mt_v5b)

### Why is there a difference in tickets created?

The total number of tickets created can go down if you’ve been deleting tickets.

Deleted tickets are removed from the [Tickets dataset](../building-reports/metrics-and-attributes-for-zendesk-support.md#topic_zlf_slp_4y). So, if you [mark tickets as spam](https://support.zendesk.com/hc/en-us/articles/4408842999066) or otherwise [delete them](https://support.zendesk.com/hc/en-us/articles/4408883872538), these tickets are removed from the overall number of tickets. This, by extension, also changes the number of ticket creations.

In the example above, the number of tickets created dropped from 705 to 693. That suggests that 12 tickets were deleted between the data being exported in August and the report being run in Explore in September.

On the other hand, the total number of tickets created can go up if you’ve been [recovering deleted tickets](../../agent-guide/ticket-management/viewing-and-recovering-deleted-tickets.md#topic_zmy_j24_xw).

To examine your deleted and recovered ticket numbers, you can use the **Deletions** and **Recoveries** metrics in the [Updates history dataset](../building-reports/metrics-and-attributes-for-zendesk-support.md#topic_as3_slp_4y).

For **Deletions**, you can’t see details like the ticket ID or other attributes (because the tickets have been deleted), but you can see:

- When the tickets were deleted, using the **Update - Timestamp** attribute
- Who deleted the tickets, using the **Updater name** attribute

For **Recoveries**, you can look at similar information about when it happened and who did it, and you can also look at other ticket attributes like the ticket ID (because the ticket exists again).

### Why is there a difference in tickets solved?

Typically, you look at created tickets by the **Ticket created - Date** attribute, and solved tickets by the **Ticket solved - Date** attribute.
However, there are scenarios in which these numbers fluctuate based on certain events.

When looking at solved tickets by *solved* date, these numbers are affected by the **Reopens** metric (available in the Tickets and Updates history datasets). This number changes if tickets are reopened between the time the data is exported and the time the report is run in Explore. A reopen can either remove a ticket from this metric entirely (because it’s no longer solved) or move it from one period to another (if the last solve was in a different period than the first solve).

When looking at solved tickets by *creation* date, these numbers are affected by resolutions over time. If 10 tickets were created on Monday, and 2 were solved the same day, an export shows 2 solved tickets for Monday. If another 3 are solved on Tuesday, the report—and next export— show 5 solved tickets were created on Monday.

The **Tickets solved** metric in the Updates history dataset looks only at the *last* solve of the currently solved tickets. You can see this by looking at the metric’s formula, specifically the two conditions in bold:

```
IF ([Changes - Field name]="status" 
    AND [Changes - Previous value]!="solved" 
    AND ([Changes - New value]="solved" OR [Changes - New value]="closed") 
    AND ([Ticket status - Unsorted] = "Solved" OR [Ticket status - Unsorted] = "Closed") 
    AND [Update - Timestamp]=[Ticket solved - Timestamp]) 
THEN [Update ID] 
ENDIF
```

If you want to track *all* solves, you can [create a standard calculated metric](https://support.zendesk.com/hc/en-us/articles/4408824243738)
that strips out those two conditions for current status and date, leaving you with the following formula:

```
IF ([Changes - Field name]="status" 
    AND [Changes - Previous value]!="solved" 
    AND ([Changes - New value]="solved" OR [Changes - New value]="closed")) 
THEN [Update ID]
ENDIF
```

### Why is there a difference in tickets in a certain category?

The Tickets dataset looks at the current state of tickets—including status, group, assignee, priority, custom fields, and more. That means that if a field is changed between the time the data is exported and the time you run a report in Explore, there will likely be changes in your results.

In the example screenshots above, you can see that the export from August shows 10 blips and 61 bugs. But in the September report, Explore shows 2 blips and 69 bugs. This suggests that 8 tickets were recategorized from blip to bug between when the export and report were run.

This type of change can also affect your report’s filters. For example, say that you have a report filtered to show only tickets for Group A. If a ticket is moved from Group A to another group between the time of the export and the report, that ticket won’t appear in your report anymore.

The reverse is true for tickets that were originally assigned to Group B and then reassigned to Group A. More tickets will appear in your report than previously, due to the filter.

## Keeping numbers in perspective

When looking at discrepancies between Explore reports and exports, it helps to keep the actual numbers themselves in perspective. Consider the following:

- If one result changes from 20 tickets to 21, the increase is 1. That doesn’t feel big. But that’s a 5% change.
- If another result changes from 1,998 to 2,100, the difference is 102. That might feel big. But it’s also only a 5% change.

When it comes to variances, look at the percentage as well as the raw number. This can help you to understand what is material or not.

Think about how many agents you have. If you have 200 agents, and one result changes by 102, this suggests that approximately half your agents, on average, changed that field on one ticket between the data being exported and the report being run in Explore.

Again, you can examine these results in the Updates history dataset. Use the **Updater name** attribute to filter a report showing the relevant [Changes - Field name] attribute and the previous or new result that’s puzzling you.

Tip: See [Explore recipe: Tracking ticket assigns across groups](https://support.zendesk.com/hc/en-us/articles/4408835929882) for an example of how to create a formula using [Changes - Field name].

Frequently, you’ll see a wide distribution of changes—for example, 100 agents all making approximately one field change in the period.

However, you might see that one or two agents are changing field results more often.
Perhaps they’re a manager tidying up after their team members. Or maybe they’re new and didn’t initially understand how to apply the field, in which case more training might be useful.

## Using the right aggregators

Finally, when you’re looking at durations, it’s a good idea to remember “quantity vs.
quality.”

By default, Explore uses the median (MED) aggregator for metrics like first reply time and resolution time. But you might have some assignees or groups who deal with very few tickets, and in a very different way from your regular agents. Perhaps they’re from finance or security teams who aren’t brought into tickets very frequently and who don’t have the same expectations for response times.

Using the MED aggregator on duration metrics helps protect you from these outliers.
If you use the mean (AVG) aggregator, this protection is reduced. For example, say the finance team has been sitting on that one ticket from that one client for six months while the rest of your team is routinely solving tickets within a week. The finance team outlier seriously impacts your unsolved tickets age, especially if you’re using the AVG aggregator.

When the finance team finally does solve that ticket, the resolution time for the period in which they solved it could also be significantly affected—again, especially if you’re using AVG.

## Conclusion

Numbers changing over time can be confusing. We get that. Particularly if your boss is asking you about it. But there can be a lot of logical reasons for changes.

If you’re concerned, consider the issues raised above and how they might be impacting the situation. If you still have questions, browse the [Explore documentation](https://support.zendesk.com/hc/en-us/categories/4405298746906) or [community](https://support.zendesk.com/hc/en-us/community/topics/1260801325209) for help, or [contact Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).