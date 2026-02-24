# Working with ticket tags

Source: https://support.zendesk.com/hc/en-us/articles/4408835059482-Working-with-ticket-tags

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Tags are words, or combinations of words, you can use to add more context to
tickets (see [About tags](../../product-guides/business-rules/about-tags.md)). Depending on your
support workflow, you might want to add tags to provide more context for the
request so that tickets can be viewed and tracked, or processed by your
account's business rules.

Agents can add or remove tags in tickets, create views based on ticket tags, and
search for tickets by tags. [Agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) can add
and remove tags only if their custom role allows it.

This article contains the following sections:

- [Adding tags to tickets](#topic_vwg_ola_vb)
- [Deleting tags from tickets](#topic_usl_l34_bfb)
- [Creating views based on ticket tags](#topic_cvw_rma_vb)
- [Searching for tickets by tags](#topic_ntk_ina_vb)

## Adding tags to tickets

Agents can manually add tags to tickets to add more context. [Agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882)
can add and remove tags only if their custom role allows it.

There's no limit on the number of tags for a ticket, but there is a limit
on the total number of characters in the Tags field. The Tag field
supports up to 5096 characters. After you reach this limit, you will
no longer be able to add more tags. None of your existing tags will
be automatically removed.

Tip: Avoid adding tags for common words, such as 'and'
and 'the.' These words will generate a high number of tags,
making automatic tagging a much less useful tool. If you've
already created common words as tags, you can [delete](https://support.zendesk.com/hc/en-us/articles/4408846535834--Update-Managing-ticket-tags#topic_twq_xla_vb) them.

The following video gives you an overview of how to add tags to your tickets:

Adding tags to tickets [0:54]

**To add tags to a ticket**

1. Create or edit a ticket.
2. Enter new tags, separated by a space, in **Tags**.

   - If the tag you are typing does not exist, it
     will be created when you press Enter.
   - If the tag you are typing exists, and has been
     used in a ticket in the last 60 days, the
     autocomplete displays suggested tags you can
     choose from.

     For example, if
     you begin typing `cust`, the tags
     `vip_customer` and
     `customer_feedback` will show up;
     however, `locust_street` will
     not.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tags_auto_suggest.png)

   For more information about formatting your
   tags, see [About tag
   formatting](#topic_ayh_32l_c3c).
3. Click **Submit** to create or update the
   ticket.

   The tags are added to the ticket. It
   takes up to 24 hours for tags to appear in the tag
   cloud and for the tag autofill feature to take
   effect.

### About tag formatting

As you enter a tag in the Tags field, note the following:

- You can use only alphanumeric, dash, underscore,
  colon, and the forward slash characters.
- You can't use other special characters, such as
  #, @, or !. If you try to add tags with characters
  that are not allowed, they disappear when the
  ticket is updated.
- Zendesk supports UTF-8 (Unicode). All languages
  supported by Zendesk can be added to tags.
- You can create a tag with more than one word if
  the words are connected with an underscore, dash,
  or forward slash character.

  Zendesk recommends being consistent with the
  character you use to connect multiple words in
  tags. Multiple words connected with an underscore
  will be treated as a different tag from the same
  words connected by a dash or forward slash. For
  example, a trigger that's configured to work on a
  ticket with a customer\_refund tag will not work on
  ticket with a customer-refund or customer/refund
  tag unless all three tags are added to the trigger
  condition. They have to be an exact
  match.

## Deleting tags from tickets

Agents can delete tags on one ticket at a time. Deleting a tag from a
ticket only removes the tag from that ticket; the tag will still
appear on other tickets and in your account as a suggestion. If a
tag hasn't been used for 60 days, it no longer appears as a
suggestion.

Admins can use a batch operation to remove a tag from all open tickets
that contain the tag. See [Deleting
a tag and removing it from all non-closed
tickets](https://support.zendesk.com/hc/en-us/articles/4408846535834--Update-Managing-ticket-tags#topic_twq_xla_vb).

**To delete tags from a ticket**

1. Open a non-closed ticket.

   You cannot delete tags from closed
   tickets.
2. In the **Tags** field of the ticket, click the close box (x)
   for the tags you want to delete. The tag is removed from the
   ticket.

## Creating views based on ticket tags

You can add tags as conditions in views, which enables you to quickly
view all tickets that contain specific tags. Agents can create
personal views for their own use. Admins can create shared views.
You can also [view all
tickets where a tag is applied](https://support.zendesk.com/hc/en-us/articles/4408846535834--Update-Managing-ticket-tags#topic_hrf_1xn_bfb).

**To create views by tags**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. [Create a new view](https://support.zendesk.com/hc/en-us/articles/4408888828570-Creating-views-to-manage-ticket-workflow#topic_vcr_xfp_ec), or
   open an existing view for editing.
3. Add a **Tags** condition.
4. Choose the condition operator **Contains at least one
   of the following**.
5. Enter one or more tags (separated with a space).
6. Add any other conditions that you'd like (for example,
   adding a condition for open tickets).
7. Set the view formatting options as needed.
8. Click **Add View**.

Your new view is listed in the Views menu.

## Searching for tickets by tags

You can search for tags contained in tickets and forum articles. Using
the search box, enter the name of the tag and the search results
will display all the tickets and forum articles that contain the
tag.

You can further improve your search results for tags by using property
keywords in your searches. For tags, the property keyword is called
‘tags’ and is used like this:

```
tags:installation
```

Your search results will contain only occurrences of the word
‘installation’ when used as a tag.

When searching for tags, you must use the exact tag string or your search
will fail. For example. if you've got a multi-word tag called
about\_sales a search for sales will not return this tag. You need to
search for the exact string:

```
tags:about_sales
```