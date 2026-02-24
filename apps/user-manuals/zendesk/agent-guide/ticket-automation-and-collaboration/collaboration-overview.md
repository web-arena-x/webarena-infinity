# Collaboration overview

Source: https://support.zendesk.com/hc/en-us/articles/4408829504154-Collaboration-overview

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Collaboration add-on |

Zendesk Support and Ticketing System Functionality within Zendesk Suite include several collaboration features that help administrators, agents, and end users communicate with each other and monitor ticket-related information. This article briefly describes the collaboration features available and includes some guidance on when to use each one. It also includes a simple example of how these features can work together. For complete documentation about light agents and side conversations, review the links in the corresponding sections below.

Collaboration features include:

- **Light agents**: Light agents have limited permissions but can stay informed about tickets and, when needed, provide subject matter expertise and advice by adding private comments.
- **Side conversations**: Side conversations enable you to bring in other people from internal and external teams to collaborate on tickets without interrupting the main conversation flow within the ticket.
- **CCs and followers**: With this feature, Zendesk tickets can include both **CCs**and **Followers** fields. By default, followers can be agents, light agents, or admins. CCs can be agents, admins, or end users. CCs work just like email. They're public to your end user. Followers are invisible to end users and get ticket update notifications.

Note: All references to *Zendesk Support* in this article apply to both Zendesk Support, the product, and the Ticketing System Functionality included in the Zendesk Suite.

This article includes the following sections:

- [When to use light agents](#topic_cvn_xxq_4fb)
- [When to use side conversations](#topic_qk4_yxq_4fb)
- [When to use CCs and followers](#topic_kzy_zwq_4fb)
- [Collaboration example](#topic_gks_gch_3gb)

## When to use light agents

Note: Light agents are included in Zendesk Suite Growth and above. You can purchase [additional light agents](https://support.zendesk.com/hc/en-us/articles/651056291177) for any Suite plan. They are also available as a [Collaboration add-on](https://support.zendesk.com/hc/en-us/articles/4408834152730) for Support Professional plans and above.

Not all Zendesk Support users in your company need full agent capabilities, so Zendesk created a *Light Agent* role. As a light agent, team members can access Support, view tickets, and leave internal notes.

For example, typically agents can handle most technical questions, but sometimes the Engineering team needs to provide advice. By making the members of the Engineering team light agents, they can be added as followers on a ticket. The engineer can then sign in to Support to view all the details and leave internal notes.

For more information, see [Understanding and setting light agent permissions](../../product-guides/team-members-and-groups/understanding-and-setting-light-agent-permissions.md).

## When to use side conversations

Note: Side conversations are included in Zendesk Suite Professional and above. They are also available as a [Collaboration add-on](https://support.zendesk.com/hc/en-us/articles/4408834152730) for Support Professional plans and above.

Many larger companies have complex workflows that require agents to reach out to other departments, partners, and vendors. Instead of resorting to complicated workflows, like changing the requester on tickets multiple times, or managing multiple tickets, you can use side conversations to collaborate with anyone (inside or outside your company) in a separate self-contained conversation within the ticket.

Side conversations make it easy and natural to get more people involved in tickets and centralize communications within Support. Agents can choose what customer information to share with collaborating teams to ensure important information stays within the ticket.

Sample use cases include:

- **Internal collaboration**: Side conversations make it easy to reach out to people in other teams or departments via email, child ticket, or Slack. For example, suppose an agent needs to check with the finance team and the legal team before replying to the requester. If they have a group in Zendesk, a child ticket makes the most sense. If Slack is a more natural place, that is available, and if neither of those work, email is always an option.
- **External collaboration**: Some workflows require an agent to regularly work with external partners and vendors. Side conversations enable them to send emails to these partners directly from the ticket rather than leaving Support or managing separate child tickets. For example, an e-commerce company may need to reach out to suppliers for product information and shipping estimates.
- **Marketplace business**: Businesses that act as a middleman between end users and suppliers must regularly act as the liaison between the two parties. Side conversations allow the agent to communicate with both sides in one ticket. For example, a freight company may need to communicate with both the shipper and the driver to coordinate a job.

For more information, see [Using side conversations in tickets](https://support.zendesk.com/hc/en-us/articles/4408844206746-Using-side-conversations-in-tickets-add-on-).

## When to use CCs and followers

CCs and followers give you better control over how you can manage public and private comments within the ticket. Agents can add and remove CCs just like in email. Agents can follow the ticket without exposing their identity to end users. Followers receive notifications when ticket updates occur, and they can view and create internal notes.

Refer to the following table to help you decide when to include users as CCs or as followers:

| Followers | CCs |
| --- | --- |
| Available for light agents, agents, or admins. | Available by default for agents, admins, or end users. Available as an option for light agents. Anyone you include as a CC in the ticket must have a Support profile, but there are no restrictions if you add someone as a CC in an email client. |
| Visibility is private by default: - Followers can watch tickets without exposing their address. It works like a   persistent BCC on the ticket. - End users don’t see followers listed when they view their requests from the   Help Center. | Visibility is public and always transparent: - The names and email addresses of CCs appear in email notifications. - End users see the names of CCs when they view their requests from the Help   Center. |
| Followers can be added by agents or admins, but not end users. Followers receive a private email when the ticket is updated with public replies or internal notes. | CCs can be added by end users (using email) or agents and admins (using email or Support). CCs receive emails (with visibility to the requester and other CCs) when the ticket is updated with a public comment. |
| If desired, agents and admins who are followers can issue public comments by replying to a CC email or adding a public reply to the ticket. They can also comment publicly by replying to a follower notification if it was sent for a public comment. | |

For more information, see [Using CCs and followers](https://support.zendesk.com/hc/en-us/articles/4408822451482).

## Collaboration example

The following is a simple example that shows how to use collaboration features available in Zendesk Support.

### Customer requests a new SSL certificate

In this example, a customer uses Zendesk Support to request a new SSL certificate for their website:

- Victoria is a Customer Support representative who works for Certs, Inc., a company that sells SSL security certificates for websites. When a customer needs to update a certificate on their website, they file a Zendesk Support ticket to request a new certificate.

 Victoria has an agent role in Zendesk Support because she needs full access to manage and reply to tickets.
- Victoria’s boss, Venkat, is the VP of Customer Support. He manages all the Customer Support representatives and makes sure that customers receive their certificates in a timely manner.

 Venkat has a light agent role in Zendesk Support. He doesn’t need full agent access, but he needs to supervise account activity and view reports to make sure things are running smoothly.
- Ken is the IT manager for a small e-commerce business, e-Fun!, Inc. He buys his website certificates from Victoria’s company and he works with a third-party vendor, Service, Inc., to host the e-Fun! websites.

 Ken has end-user access to the Zendesk Support account at Victoria’s company.

Ken receives a notification that one of his website certificates will expire in 30 days. Ken creates a new Zendesk Support ticket with Certs, Inc. and requests a new certificate for the site.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/collab_example_new_ticket.png)

Ken is the ticket requester and Victoria is the agent assigned to the ticket.

Before Victoria can complete the ticket request, she needs to make sure Ken’s company has a PO with the funds to pay for the new certificate. Victoria adds her boss, Venkat, as a follower to the ticket, so he’s aware of the request.

Victoria then starts a side conversation with the Finance Department to make sure funding is available. When she starts the side conversation with Finance, she decides what information to include (or not include) about the ticket.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/collab_example_side_conversation.png)

Finance replies to Victoria and confirms that funding is available.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/collab_example_close_side_conversation.png)

Because the funding issue is resolved, Victoria closes the side conversation by marking it done.

Victoria notifies Ken, the requester, that the certificate has been approved.
She includes a link that Ken can use to pick up the certificate and attaches instructions on how to install the certificate.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/collab_example_reply.png)

Also, as Ken requested, Victoria adds his website vendor, Service, Inc., as a CC to the ticket so they also know the new certificate is ready.

As a ticket follower, Venkat can see that Victoria has sent out the new certificate. He adds an Internal note to the ticket telling Victoria that she did a nice job!

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/collab_example_internal_note.png)

### Who sees what?

Based on their role, each participant in this example has slightly different visibility into ticket information:

- Because Venkat is a follower, he can see the entire ticket history, including the side conversation Victoria had with Finance. His name and email address are never exposed to Ken or Ken’s web hosting service.
- For Victoria’s side conversation with Finance, the Finance department only sees the information Victoria included in the side conversation email. They do not see the original ticket request, or any ticket follow-up.
- Ken sees his original request and Victoria’s reply with her link to the new certificate. He can also see that she included his web hosting vendor as a CC. He does not see her side conversation with Finance or Venkat’s internal note.
- Because Victoria added them as a CC, Ken’s web hosting vendor, Service, Inc., receives an email that includes the reply Victoria sent to Ken with a link to pick up the certificate. They see all public comments in the main part of the ticket, but they do not see Victoria's side conversation with Finance, and they don't see Venkat’s internal note.
- Victoria sees everything in the ticket, including the internal note from Venkat.