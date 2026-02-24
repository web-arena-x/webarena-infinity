# Managing ticket tags

Source: https://support.zendesk.com/hc/en-us/articles/4408846535834-Managing-ticket-tags

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Tags are words, or combinations of words, you can use to add more context to tickets (see [About tags](about-tags.md)). This article describes how you can manage ticket tags for your Zendesk account. You must be an administrator to do the tag management tasks described in this article.

This article contains the following sections:

- [Analyzing ticket tag activity](#topic_utx_jma_vb)
- [Viewing all tickets where a tag is applied](#topic_hrf_1xn_bfb)
- [Deleting a tag and removing it from all non-closed tickets](#topic_twq_xla_vb)
- [Using ticket tags in macros, triggers, and automations](#topic_umd_ona_vb)

Related topics:

- [Enabling and disabling ticket tags](https://support.zendesk.com/hc/en-us/articles/4408829424794--Update-Enabling-and-disabling-ticket-tags)
- [Creating views based on ticket tags](https://support.zendesk.com/hc/en-us/articles/4408835059482--Update-Working-with-ticket-tags#topic_cvw_rma_vb)

## Analyzing ticket tag activity

Zendesk Support provides you with a view into the tags that have been applied to your tickets. Admins can view the 100 most-active tags for the last two months. This list is updated daily.

**To analyze tag activity**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
 **Objects and rules** in the sidebar, then select **Tickets > Tags**.

## Viewing all tickets where a tag is applied

To help you manage tags, it can be useful to see where the tag is applied.

The Tags page displays the 100 most used tags for the past two months. If the tag you're looking for isn't on the list, you can [search for tickets by tag](https://support.zendesk.com/hc/en-us/articles/4408835059482--Update-Working-with-ticket-tags#topic_ntk_ina_vb). You can also [create a view](https://support.zendesk.com/hc/en-us/articles/4408835059482--Update-Working-with-ticket-tags#topic_cvw_rma_vb) to see all tickets based on a specific tag.

**To see where tags are applied**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Tags**.

   A list of the 100 most used tags in the last two months appears, including tags applied to tickets where the ticket was later deleted or the tag removed. The number of times the tag has been applied to tickets in this time period is also listed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tags_admin_page.png)
2. Click a tag name or **View** to view all tickets where the tag is applied.

   A list of tickets associated with the tag opens on the search page in Zendesk Support.

## Deleting a tag and removing it from all non-closed tickets

You can use a batch operation to remove a tag from all open tickets that contain the tag. Tags can't be deleted from closed tickets. You can also edit each ticket manually to delete individual tags from a ticket (see [Deleting tags from tickets](https://support.zendesk.com/hc/en-us/articles/4408835059482#topic_usl_l34_bfb)).

Deleting a tag from all non-closed tickets doesn't delete the tag from your account immediately. Deleted tags may still appear as suggestions in your account until the closed tickets that contain the tag are retired out of the list and the tag isn't used again for 60 days. After this happens, the tag will no longer appear as a suggestion. Also, deleting tags from tickets doesn't remove references to them in automations, macros, and triggers.

**To delete a tag from open tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Tags**.
2. Click the tag that you want to delete.

   A list of tickets associated with the tag opens on the search page in Zendesk Support.
3. Select the check box at the top of the list, then click **Edit**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tags_batch_delete.png)
4. In the Update ticket(s) dialog, enter the tag name in the **Remove Tags** field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tags_remove_update.png)
5. Click **Submit**.

**Admin > Tags** displays the top 100 most-used tags for the past two months. To delete a tag that isn't on the list, you can [search for tickets by tag](https://support.zendesk.com/hc/en-us/articles/4408835059482--Update-Working-with-ticket-tags#topic_ntk_ina_vb) and delete them manually from the tickets and topics that you have access to.

## Using ticket tags in macros, triggers, and automations

Adding tags to your tickets gives you even more flexibility to track, manage, and interact with your tickets. They can be used to attach additional data to your tickets, which you can then use in your automations, macros, and triggers. You can use business rules to add, remove, or set tags. If you select the *set tags* action, the current tags will be replaced with the tags you enter.

As an example, let's look at how a tag can be used in a trigger. If you use email subdomains, you may have set up a subdomain to track the tickets that are generated through responses to your newsletter. You can set up a trigger to check for the origin of the ticket using the **Ticket received at** condition, as shown here:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tag_in_trigger_new.png)

You can then add an action that adds a tag to the ticket, as shown here:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tag_as_trigger_action_new.png)

You can then use this tag to create a view that shows you all the tickets that have been created from newsletter responses. You can also use the tag as a condition or an action in some other automation, macro, or trigger. For example you might want to exclude this tag for some reason when you're defining the selection of tickets you want to be acted on by a trigger, as shown here:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tag_as_trigger_condition.png)

Drop-down custom fields also create ticket tags and they can also be used in automations, macros, and triggers as well.