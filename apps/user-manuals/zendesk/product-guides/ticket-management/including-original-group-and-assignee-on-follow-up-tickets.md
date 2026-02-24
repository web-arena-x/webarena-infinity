# Including original group and assignee on follow-up tickets

Source: https://support.zendesk.com/hc/en-us/articles/6937092811162-Including-original-group-and-assignee-on-follow-up-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Any response to a closed ticket from any channel automatically [creates a follow-up ticket](https://support.zendesk.com/hc/en-us/articles/4408883882522).

This creates a new ticket that references the closed ticket and pulls most data from the original, closed ticket into the new, follow-up ticket (see [Understanding follow-up tickets](https://support.zendesk.com/hc/en-us/articles/8421655952026)).

By default, the group and assignee are not copied to the follow-up ticket. Admins can decide whether the group and assignee are copied from the original ticket to the follow-up ticket.

**To include the original group and assignee on follow-up tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Assignments and notifications** to expand it.
3. Select **Copy original assignee and group to follow-up ticket**.
4. Click **Save**.

   If you need to turn this setting off after turning it on, deselect the setting and save your changes.

## Understanding follow up tickets when the original group or assignee is invalid

There might be scenarios where the original group or assignee becomes invalid during the time between the ticket closing and the follow-up ticket being created. A group becomes invalid when it's deleted. An assignee becomes invalid if they're no longer part of the assigned group, have been demoted to an end user, or have been removed from your account.

If you’ve turned on copying the original assignee and group and one of these scenarios occurs, Zendesk does the following:

- If the original group is invalid, Zendesk uses the system ticket rules to determine the follow-up ticket’s group and assignee.
- If the original group exists but the assignee is invalid, Zendesk copies the original group on the follow-up ticket and uses the system ticket rules to determine the assignee.
- If both the group and the assignee are invalid when a follow-up ticket is created, Zendesk uses the system ticket rules to determine the group and the assignee.

See [About system ticket rules](https://support.zendesk.com/hc/en-us/articles/4408894213018) to learn more.