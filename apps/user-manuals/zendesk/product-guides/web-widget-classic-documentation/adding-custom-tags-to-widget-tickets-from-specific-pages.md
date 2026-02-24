# Adding custom tags to Widget tickets from specific pages

Source: https://support.zendesk.com/hc/en-us/articles/4408835672218-Adding-custom-tags-to-Widget-tickets-from-specific-pages

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

All tickets submitted through Web Widget (Classic) include the URL for the page the user was
on when the ticket was sent. Administrators can use triggers to add custom tags, agent
assignments, and other actions to these tickets, based on the originating page, to streamline
your ticket workflow.

Related articles:

- [Using Web Widget (Classic) to embed customer service on your
  website](https://support.zendesk.com/hc/en-us/articles/4408836216218)
- [Advanced customization of Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408832257562)

For general information on triggers, see [Triggers resources](https://support.zendesk.com/hc/en-us/articles/4408843730458).

For example, let's say you are the administrator for a health care website, and you want to
add the tag "peanut\_allergies" to any tickets submitted through Web Widget (Classic) from a
help center article about managing peanut allergies.

**To add a custom tag to a ticket based on its originating page**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Objects and rules**
   icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)) in the sidebar, then select **Business rules > Triggers**.
2. On the Triggers page, click **Add trigger**.
3. Enter a descriptive title for your trigger.
4. In the section **Meet all of the following conditions:** use the drop-down menus to
   select the following options:
   - **Ticket: Channel**
   - **Is**
   - **Web Widget**

     Click the [plus] and add another condition with the following
     options:
   - **Ticket: Comment text...**
   - **Contains the following string**
   - In the text entry box: **Enter the URL of the page you want to trigger the custom
     tag.**
5. In the section **Perform these actions:** select the following options:
   - In the drop-down menu: **Ticket: Add tags**
   - In the text entry box: **Enter the text of the tag you want applied to the ticket
     (for example, peanut\_allergies)**.
6. At the bottom of the page, click **Create trigger**.

With these conditions, any ticket that is submitted through Web Widget (Classic), when
Web Widget (Classic) is launched from the URL included in step 4 above, has the tag
“peanut\_allergies” applied to it upon submission.