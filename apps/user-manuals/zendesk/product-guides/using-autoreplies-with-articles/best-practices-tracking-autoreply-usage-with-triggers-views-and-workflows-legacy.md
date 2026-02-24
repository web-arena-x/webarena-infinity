# Best practices: Tracking autoreply usage with triggers, views, and workflows (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4408894189082-Best-practices-Tracking-autoreply-usage-with-triggers-views-and-workflows-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

As of July 31, 2025, the autoreplies with articles feature is considered legacy functionality. Instead, [use AI agents](https://support.zendesk.com/hc/en-us/articles/6478272212506) to deliver generative AI-powered responses on messaging, email, and web form channels.

Figuring out the best way to set up triggers, automations, views, and tags to track [autoreply](https://support.zendesk.com/hc/en-us/articles/5515145726106) usage can be confusing for many users. In this article, contains recommendations for the following situations:

- [Automatic tagging](#h0sj62mlybt1v22j6318w7tje224ap8)
- [Viewing tickets marked helpful](#h6sj62nqvip1ywrfsne4sgstjelcu)
- [Removing the tags from reopened autoreply tickets](#h12sj62nw8r7l8ge0k14yz8w11jlu149)
- [Following up with customers who self-solve](#h18sj62nx6mm1yuf1ro1puuvsqxzhxpv)
- [Creating an autoreply trigger for follow-up tickets](#follow_up)
- [Suppressing CSAT surveys on autoreply tickets](#h4sj6s9qzf4e3irv3q7518x1frubcj)

## Automatic tagging

There are five tags that the autoreplies feature automatically adds to tickets to simplify setting up of new triggers and automation.

| | |
| --- | --- |
| **Ticket tag name** | **When is it added?** |
| ar\_suggest\_false | Added when a suggestion is successfully triggered but failed to find any matching articles |
| ar\_suggest\_true | Added when a there is a successful article suggestion |
| ar\_marked\_unhelpful | Added when the end user indicated that the suggestion was unhelpful |
| ar\_marked\_helpful | Added when the end user marks the suggestion as helpful |
| ai\_agent\_automated\_resolution | Added when the ticket is automatically resolved by an AI agent using an [autoreply with articles](https://support.zendesk.com/hc/en-us/articles/5352026794010#topic_o2r_13x_4wb) or [article recommendations](https://support.zendesk.com/hc/en-us/articles/5352026794010#topic_p4p_zqr_y1c). Note: This tag is not added to closed tickets. If you use automations to close tickets, make sure those automations are configured to act at least 72 hours after the last public reply. This helps make sure all applicable automated resolutions have this tag applied to the ticket. |

Note that if you use the answer\_bot\_fired tag, your existing triggers will continue working as they do today. 

To optimize how triggers are fired, set up new triggers to take new actions, or change automations, you have to start with some basic tag manipulation:

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. For every trigger listed in the **Answer Bot trigger**section, select **Edit**.
3. Scroll down to the bottom of the trigger, to the Actions section and select **Add Action**.
4. Select **Add tags** from the drop-down list and then insert the tag **answer\_bot\_fired**.
5. Save the trigger.

Now all tickets autoreplies have fired on will have the **answer\_bot\_fired** tag, and you can easily create a view to see them:

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. Click **Add view**.
3. Create a new view with these conditions:
   - Status | Less than | Closed
   - Tags | Contains at least one of the following |  **answer\_bot\_fired**

## Viewing tickets marked helpful

You can create a view to see all tickets that an end user has marked helpful based on an autreply suggestion. Tickets an end user has marked as helpful by an autoreply suggestion are automatically given the ar\_marked\_helpful tag.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. Click **Add view**.
3. Create a new view with these conditions:
   - Status | Greater than | On-hold (or Pending, if On-hold status is not available for your account)
   - Tags | Contains at least one of the following | ar\_marked\_helpful

## Removing tags from reopened autoreply tickets

You could even take this one step further and add another trigger to remove the **ar\_marked\_helpful** tag, if a ticket is reopened:

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. On the triggers page, click the **Ticket** tab, then click **Create trigger**.
3. Set the conditions:
   - Status | Changed from | Solved
   - Status | Not changed to | Closed
   - Tags | Contains at least one of the following | ar\_marked\_helpful
4. Add the actions:
   - Select **Add tags** from the drop-down list and then insert the tag answer\_bot\_reopen.
   - Select **Remove tags**from the drop-down list and then insert the tag ar\_marked\_helpful.
5. Save the trigger.

## Following up when customers self-solve

Extending on the previous steps, you can also add another action to send the requester a follow-up email to confirm that their request has been marked as solved.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. Create the trigger in the previous section, with these additional actions:
   - Email user | (requester)
   - Enter an email subject and body
3. Save the trigger.

## Creating an autoreply trigger for follow-up tickets

In some situations, you may want to check in on a *closed* ticket. Closed tickets cannot be reopened, so to continue the conversation (rather than starting a new one) you need to [create a follow-up ticket](https://support.zendesk.com/hc/en-us/articles/4408883882522).

When you create a follow-up ticket, all of the closed ticket's information, including tags, is carried over into the new ticket. That means that the default ar\_marked\_helpful tag is applied to the follow-up ticket, which prevents autoreplies from firing on the new ticket. If you want to include article suggestions in the ticket notifications, you'll need to remove the ar\_marked\_helpful tag.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Triggers**.
2. On the triggers page, click the **Ticket** tab, then click **Create trigger**.
3. Set the conditions:
   - Ticket | Is | Created
   - Channel | Is | Closed ticket
   - Tags | Contain | ar\_marked\_helpful
4. Add the actions:
   - Remove tags | ar\_marked\_helpful ar\_suggest\_false  ar\_suggest\_true  ar\_marked\_unhelpful
5. Save the trigger.

## Suppressing CSAT surveys on autoreply tickets

Customer Satisfaction (CSAT) surveys were designed primarily for when human agents have been involved in solving the ticket. Many customers choose to disable satisfaction surveys for autoreply tickets. This assumes that you are tagging tickets solved by an autoreply suggestion with the answer\_bot\_solved tag.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Business rules > Automations**.
2. Open the automation that's been set up to send CSAT surveys By default it's called Request customer satisfaction rating (System Automation).
3. Add a new condition:
   - Tags | Contains none of the following | answer\_bot\_solved
4. Save the automation.