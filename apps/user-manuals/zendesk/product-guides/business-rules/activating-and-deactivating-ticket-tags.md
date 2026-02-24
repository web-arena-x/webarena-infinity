# Activating and deactivating ticket tags

Source: https://support.zendesk.com/hc/en-us/articles/4408829424794-Activating-and-deactivating-ticket-tags

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Tags are words, or combinations of words, you can use to add more context to tickets (see [About tags](about-tags.md)). Manual ticket tagging is activated by default, but automatic ticket tagging is not. With manual ticket tagging, agents can add and edit tags on tickets. With automatic ticket tagging, Zendesk Support scans incoming ticket descriptions and adds tags that match. You must be an administrator or an [agent in a custom role with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) to activate and deactivate ticket tagging.

This article contains the following sections:

- [Deactivating manual ticket tagging](#topic_ly1_1s4_bfb)
- [Turning on and off automatic ticket tagging](#topic_ynp_ds4_bfb)

## Deactivating manual ticket tagging

Manual ticket tagging is activated by default. You can turn off manual ticket tagging if you'd like. You might do this if you rely solely on [automatic tagging](#topic_ynp_ds4_bfb) or if you simply don't use tags. When you deactivate manual ticket tagging, the **Tags** field does not appear on new tickets.

**To deactivate manual ticket tagging**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Tags** to expand it.
3. Deselect the **Allow tags on tickets** option.

   Note: Deactivating manual ticket tagging only removes the ability to add tags via the ticket interface. Agents, admins, and integrations can still add, remove, or modify tags on tickets via the [Update Ticket](https://developer.zendesk.com/rest_api/docs/support/tickets#update-ticket) API.
4. Click **Save**.

   If you deactivate this setting, any existing tags that were applied to tickets will remain, but you cannot add new tags.

## Turning on and off automatic ticket tagging

If you turn on automatic ticket tagging, Zendesk Support scans new incoming ticket descriptions looking for words longer than two characters and then compares those words to tags that have already been used. The top three matches are added to the ticket. You can then use those tags in your business rules to, for example, automatically route tickets to specific groups or agents.

Tags are only automatically added to tickets that come from end-users via the ticket channels. Tags will not be added if an agent submits a ticket from within Support. However, if an agent creates a new ticket using an email, automatic tags will be applied.

Automatic ticket tagging might not work in languages other than English.

If you use [conditional ticket fields](https://support.zendesk.com/hc/en-us/articles/4408834799770#topic_ydk_2b1_phb), it's not recommended to turn on automatic ticket tagging because it can potentially select field values and override end users' form selections.

**To turn on automatic ticket tagging**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Tags** to expand it.
3. Select **Allow tags on tickets**, then select **Turn on automatic ticket tagging**.
4. Click **Save**.

**To turn off automatic ticket tagging**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Tags** to expand it.
3. Under **Allow tags on tickets**, deselect **Turn on automatic ticket tagging**.
4. Click **Save**.

   If you turn off automatic tagging, you can still add tags manually.