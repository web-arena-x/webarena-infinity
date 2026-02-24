# Understanding follow-up tickets

Source: https://support.zendesk.com/hc/en-us/articles/8421655952026-Understanding-follow-up-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

When you respond to a closed ticket, a follow-up ticket is automatically created, pulling most data from the original. Some fields like comments and priority aren't included, but tags are inherited. You can reset tags with a trigger if needed. Follow-up tickets also maintain the original ticket's brand and support address. They aren't created when recovering tickets from the Suspended tickets view.

Any response to a closed ticket from any channel automatically [creates a follow-up ticket](https://support.zendesk.com/hc/en-us/articles/4408883882522).
This creates a new ticket that references the closed ticket and pulls most data from the original, closed ticket into the new, follow-up ticket.

When a follow-up ticket is created, it includes most field values and properties from the original ticket, with a few exceptions.

This article contains these topics:

- [Fields not included from the original ticket](#topic_f3k_xf1_ndc)
- [Follow-up ticket considerations](#topic_q4r_vk5_ncc)

## Fields not included from the original ticket

The following fields are not included on the follow-up ticket from the original ticket:

- Comments
- Priority
- Type
- Group or Assignee

 Admins can turn on a setting to [include the original group and assignee on follow-up tickets](https://support.zendesk.com/hc/en-us/articles/6937092811162) though.
- Skills

 Instead, [skills are applied to the follow-up ticket based on your routing rules](https://support.zendesk.com/hc/en-us/articles/5833458075930#topic_vgq_xxv_3mb) when the follow-up ticket is created.
- External ID

## Follow-up ticket considerations

- Follow-up tickets inherit all tags from the original ticket. You can reset follow-up tickets' [tags and tag-based fields with a trigger](https://support.zendesk.com/hc/en-us/articles/4408884146842) if needed.
- The [channel for follow-up tickets](https://support.zendesk.com/hc/en-us/articles/4408824097050/#topic_ewn_jkf_qtb) is **Closed Ticket**.

 In Explore, follow-up tickets are reported through two different channels, depending on which attribute you're using:

 - **Closed Ticket:** The **Update channel** attribute in the [Updates history](https://support.zendesk.com/hc/en-us/articles/4408827693594#topic_as3_slp_4y) dataset uses this channel value.
 - **Web:** The **Ticket channel** attribute in the [Support datasets](https://support.zendesk.com/hc/en-us/articles/4408827693594) uses this channel value.

    See [Explore recipe:
    Filtering for follow-up tickets](https://support.zendesk.com/hc/en-us/articles/4408827192986-Explore-recipe-Filtering-for-follow-up-tickets?source=search) for more information on including follow-up tickets in your Explore reports.
- When someone replies to a side conversation that belongs to a closed or archived ticket, a [follow-up ticket is automatically created](https://support.zendesk.com/hc/en-us/articles/4408837750170).
- When a follow-up ticket is created from an email response to a closed ticket, the ticket inherits the previous brand of the closed ticket. The follow-up ticket uses the support address associated with the email that generated the original ticket.

 When an agent creates a follow-up ticket from the Agent Workspace, the ticket uses your default support address. Or, if you've set up multiple brands, it uses the default support address of the ticket's brand.
- Follow-up tickets are not created when recovering tickets from the [Suspended tickets view](https://support.zendesk.com/hc/en-us/articles/4408893392922#topic_ukg_lbf_kd).