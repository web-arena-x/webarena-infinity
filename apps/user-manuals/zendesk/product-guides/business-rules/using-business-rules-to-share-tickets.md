# Using business rules to share tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408887148698-Using-business-rules-to-share-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

You must be on an Enterprise plan to use the **Share ticket with** action to automatically share tickets.

Admins can create [sharing agreements](https://support.zendesk.com/hc/en-us/articles/4408893967514) between Zendesk accounts, and agents can manually or automatically share tickets to another Zendesk account.

This article contains the following topics:

- [Conditions and actions for shared tickets](#topic_unx_pdm_yfb)
- [Example 1: Using the share ticket action](#topic_ygn_vnl_yfb)
- [Example 2: Using the received from condition](#topic_xbw_vnl_yfb)
- [Example 3: Creating a view](#topic_n1d_xql_yfb)

## Conditions and actions for shared tickets

You can use the following conditions in triggers, automations, and views. These conditions might vary depending on your sharing agreements.

| Condition | Description |
| --- | --- |
| Ticket details: Received from <*Zendesk subdomain*> | Processes rules on tickets received from the selected subdomain (automations, triggers, and views) |
| Ticket details: Sent to <*Zendesk subdomain*> | Processes rules on tickets sent to the selected subdomain (automations, triggers, and views) |
| Ticket Channel > Is > Ticket sharing | Processes rules only on shared tickets (automations, triggers, and views) |
| Update via > Is > Ticket sharing | Processes rules only on tickets that have been updated through a sharing agreement (triggers only) |

On Enterprise plans you can use the following ticket sharing action for automations and triggers.

| Action | Description |
| --- | --- |
| Share ticket with <*Zendesk subdomain*> | Shares the ticket with the selected Zendesk subdomain (automations and triggers) |

## Example 1: Using the share ticket action

In this example, the trigger uses the **Share ticket with** action (available in Support Enterprise) and fires whenever a ticket contains the tag **image\_sensor**. When the tag is included, the trigger shares the ticket with Kongen Image Sensors.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/business-rule-share1.png)

## Example 2: Using the received from condition

In this example, the trigger adds the **from\_kongen** tag to all tickets shared from Kongen. It's good practice to add a tag to help you identify tickets in your account that have been shared from another account.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/business-rule-share2.png)

## Example 3: Creating a view

You can use the tag information you've added to create views. This example shows a view of all tickets that were received from Kongen using the tag that was added in example 2.

![View created using business rules](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/business-rule-share3.png)