# Updating ticket requesters and organizations

Source: https://support.zendesk.com/hc/en-us/articles/4408886900506-Updating-ticket-requesters-and-organizations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

It's possible to change an existing ticket's requester to someone else and, if a requester belongs to more than one organization, you can also change the organization their ticket is assigned to.

Note: Your Zendesk Support settings must be configured to allow CCs on tickets for you to be able to change the ticket requester. For details, see [Setting CC permissions for tickets](https://support.zendesk.com/hc/en-us/articles/4408843795482-Configuring-CC-permissions-and-notifications#topic_x3t_4p5_cq).

This article includes the following sections:

- [Changing the ticket requester](#topic_jwd_bnr_wt)
- [Changing the ticket requester's organization](#topic_k3w_m34_dp)

Note: You can't change the requester on a ticket that has been [shared](https://support.zendesk.com/hc/en-us/articles/4408886265370-Sharing-tickets) or closed.

## Changing the ticket requester

You may want to change the user designated as the ticket requester if someone sent in a support request on someone else's behalf. The user who you want to set as the requester must be an existing user.

**To change the ticket requester**

1. Open the ticket where you want to change the requester.
2. Click directly into the **Requester** field in the ticket properties panel to change the requester. 

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/requester-field.png)
3. Begin entering a user's name, email domain, or organization name and the relevant results appear. Select the user. If the user does not yet have an account, add them by clicking **+Add user** at the bottom of the search results.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/requester_add_user.png)
4. Click **Submit** to save the ticket update.

After you've changed a requester, you can later see who the original requester was by checking the ticket's events and notifications.

## Changing the ticket requester's organization

On Professional and Enterprise, end-users can belong to multiple organizations. If a ticket's requester belongs to multiple organizations, the ticket can be assigned to any of the requester's organizations.

Note: An administrator must enable multiple organizations for users (see [Enabling multiple organizations for users](https://support.zendesk.com/hc/en-us/articles/4408838140314)).

When a user who belongs to multiple organizations submits a ticket by email, it is assigned to their default organization. When the user creates a ticket in your Help Center, or when an agent creates a ticket on behalf of the user, the user or agent can select the organization for the ticket. You can change the organization for a ticket, if necessary.

When a ticket [is created through an API call](https://developer.zendesk.com/rest_api/docs/support/tickets), the ticket is assigned to the requester's organization\_id as specified in the call. If the call doesn't specify an organization\_id or specifies an organization\_id that the requester isn't part of, the ticket is assigned to the requester's default organization.

Here's what happens to tickets when the requester is removed from an organization or when an organization is deleted:

- When a requester is removed from an organization, any tickets associated with that user and that organization, will be assigned to the user's default organization if the user belongs to multiple organizations. If the user does not belong to multiple organizations, the tickets will not be associated with an organization.
- When an organization is deleted, any tickets associated with the deleted organization will be assigned to the requester's default organization. If the organization that was deleted was the requester's default organization, one of the requester's other organizations will be promoted to default, then any working tickets will be associated with the requester's new default organization. If the user does not belong to multiple organizations, the tickets will not be associated with an organization.

**To change the organization for a ticket when the requester belongs to multiple organizations**

- In the ticket, click the current **Organization**, then select one of the requester's other organizations.

 If the requester does not belong to multiple organizations you will not see the Organization field on the ticket. You can only choose an organization that the requester belongs to.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_change_org.png)

 The organization for the ticket appears in the ticket and at the top of the ticket.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_org_name_at_top.png)