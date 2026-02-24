# Adjusting your business rules to handle private tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408829344538-Adjusting-your-business-rules-to-handle-private-tickets

---

When you allow your agents to create private tickets, you introduce a new and different kind of workflow into your experience of Zendesk. Private tickets are tickets with only private (internal) comments, and just like individual private comments, they aren't visible to your customers until a public comment is added. However, they can still cause email and other notifications to be sent out through triggers and automations. Sometimes you may find this to be useful (i.e., sending a customer satisfaction survey after logging a phone call), but generally you may want to prevent it. With judicious use of conditions, you can do just that.

**Note**: This article includes information on adjusting your business rule conditions. If you are using placeholders to format your comments, see [Zendesk placeholder comments reference](https://support.zendesk.com/hc/en-us/articles/4408886858138-Zendesk-Support-placeholders-reference#topic_giz_opl_rc) for information.

This article discusses adjustments you may want to make to your business rules, including:

- [System (default) rules](#SystemRules)
- [Custom rules](#CustomRules)
- [Service level agreements](#SLAs)

Related articles:

- [Enabling private ticket creation](https://support.zendesk.com/hc/en-us/articles/4408842918298)
- [Creating a private ticket for an end-user](https://support.zendesk.com/hc/en-us/articles/4408882462618#topic_uyq_5rx_yy)

## System rules

There is one default trigger and three default automations you'll want to look at first:

- Notify requester of received request (trigger)
- Request customer satisfaction rating (automation)
- Pending notification 24 hours (automation)
- Pending notification 5 days (automation)

If your account is newer, you may already see a condition, [Ticket: Privacy] [Ticket has public comments]. This condition identifies whether a ticket is public or private - if the ticket has any public comments it is public; no public comments indicate the ticket is private. If you do not see this condition, you may want to consider adding it to avoid sending any of the above mentioned notifications to your customers. As mentioned, you may want to send satisfaction rating surveys, but the choice is up to you.

**To update the above-listed triggers and automations to avoid sending notifications from private tickets to end-users**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Objects and rules** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) in the sidebar, then select **Business Rules > Triggers** (or **Automations**).
2. Click the default trigger or automation you want to update.
3. Under **Meet all of the following conditions**, click the + to add a new condition.
4. Use the drop-down menus to create a new condition: **[Ticket: Privacy] [Ticket has public comments]**.
5. Click **Submit**.

## Custom rules

If you've set up rules to send custom notifications to your customers, a little more work will be needed. There are essentially three trigger and automation actions to look out for:

- Notifications: Email user (only if it's sent to the requester)
- Notifications: Tweet requester
- Notifications: Notify target

Take a look at any trigger that sends a notification. If it does, you may want to add the [Ticket: Privacy] [Ticket has public comments] condition. Ultimately, it's up to you, as there may be some occasions where you want to send these. You don't need to worry about emails to Groups or the Assignee. You also only need to worry about targets when they produce some public facing message.

You can update custom rules as described [above.](#howto)

If you are an Enterprise subscriber you can use [Business Rule Analysis](https://support.zendesk.com/hc/en-us/articles/4408889285530-Analyzing-your-business-rules-Enterprise-) to track down all the rules that send a notification to the requester.

## Service Level Agreements

You may not want SLAs to apply to private tickets. It also pays to look through these agreements and make some decisions. Note that once you turn on the feature, many of the metrics tracked for SLAs are not applicable to these tickets. Anything that tracks reply time or requester wait times isn't meaningful until a ticket has at least one public comment. If you'd like to completely exclude private tickets from an SLA, just add the condition [Privacy] [Is] [Ticket has public comments].