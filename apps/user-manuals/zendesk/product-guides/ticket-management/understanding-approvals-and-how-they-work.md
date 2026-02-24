# Understanding approvals and how they work

Source: https://support.zendesk.com/hc/en-us/articles/8481179038490-Understanding-approvals-and-how-they-work

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Customer Service Suite** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Employee Service Suite** | Growth, Professional, Enterprise, or Enterprise Plus |

Verified AI summary ◀▼

Approvals streamline ticket workflows by allowing you to request decisions from authorized agents or end users. This feature enhances efficiency, compliance, and quality control while providing transparency on request status. You can use approvals for tasks like software access, refunds, or employee changes. Track decisions with the approval status field.

Approvals are requests that agents make on behalf of other agents and end users.
Agents send requests to approvers. Approvers are other agents or end users who have the authority to review the request information and make a decision.

Incorporating approvals into your ticket workflow can:

- Increase agent efficiency by removing the need for manual interventions or dependence on external applications.
- Ensure compliance by recording approval decisions within Zendesk to ensure adherence to your organization’s compliance policies.
- Maintain quality control by adding an approval step into your organization’s standard operating procedures.
- Provide transparency on the approval request's status to the approval requester, approver, and the assignee of the associated ticket.

This article provides an overview of approvals and how they work in Zendesk.
It describes who can make approval requests, who can approve requests, and examples of how approvals are used in both customer service and employee service cases.

This article contains the following topics:

- [About the approval request process](#topic_j5n_3hs_tdc)
- [Understanding who makes requests and who approves requests](#topic_zyc_whs_tdc)
- [Approval request examples](#topic_fwz_43s_tdc)
- [Reporting on approval requests](#topic_sph_kcj_cgc)
- [Approval request resources](#topic_ndd_xst_yfc)

## Considerations for approval requests

Before using approval requests, consider the following limitations:

- A ticket can have a maximum of one active approval request at a time.
- A ticket can have a maximum of 50 inactive approval requests. When this limit is reached, no new approval requests can be created for the ticket.
- Agent approvers can respond to approval requests with a comment. Each approval request can have a maximum of 40 comments, and each comment on an approval request can be a maximum of 500 characters.
- For accounts that have more than one ticket form, the approval status field must be manually [added to ticket forms](https://support.zendesk.com/hc/en-us/articles/4408883152794).
- For end users to be able to access approval requests assigned to them, your help center must be on the latest version of the standard Copenhagen theme or you must [manually update your custom theme](https://support.zendesk.com/hc/en-us/articles/4408832681626#topic_xrf_2r4_yfc).
- Approval requests can't be exposed to end users in accounts with more than one help center. However, it's still possible to select them as an approver. If you turn on approvals while you have multiple help centers, train your agents to avoid assigning approval requests to end users.

## Understanding the approval request lifecycle

The main steps of the approval request process consist of the following:

1. An agent [creates an approval request](https://support.zendesk.com/hc/en-us/articles/8481158639770)
   from a ticket in the Agent Workspace.
   Within the request, the agent designates another agent or an end user as the approver.

   After an approval request is created, the ticket associated with it can't be closed until the approver responds or the request is withdrawn.
2. The approver receives an email notification that they have an approval request to review.
3. The approver then [responds to the request](https://support.zendesk.com/hc/en-us/articles/8481193191322)
   by approving or denying. Agent approvers also have the option to respond with a comment.

   Agent approvers respond to approval requests in the Agent Workspace. End user-approvers must respond to requests from the help center.
4. The agent who created the approval request receives the approver’s response.

The image below illustrates an overview of the approvals workflow:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/es_approvals_workflow_chart2.png)

Note: It's also possible for the agent who requested the approval and the agent assigned to the ticket to withdraw an approval request prior to the approver responding to it.

## Understanding who makes requests and who approves requests

Approval requests are always created by agents. Typically, agents submit approval requests on behalf of other agents and end users when a ticket assigned to them requires approval from someone else. For example, tickets requesting access to software or tickets requesting refunds beyond a certain threshold. When the agent [creates requests](https://support.zendesk.com/hc/en-us/articles/8481158639770)
on tickets they’re working on from the Agent Workspace and sends them to approvers.

Approvers are users who have the authority to review approval request information and make a decision. They respond to approval requests, but are not solving the ticket. Both agents and end users can be approvers.

- On Zendesk Employee Service Suite Growth plans and above, all agents and end users are employees of the same organization. In this context, agents are employees with an agent seat and can access the Agent Workspace in Zendesk Support to respond to approvals. End users, or employees without an agent seat, have access to your organization's internal help center where they can respond to approvals.
- On Customer Service Suite Professional plans and above, agents respond to approval requests from the Agent Workspace. In this context, end users are the requesters and are generally not part of the same organization as the agent. However, both agents and end users can still be approvers, with agents responding to requests in the Agent Workspace and end users responding through the help center.

See [Responding to an approval request](https://support.zendesk.com/hc/en-us/articles/8481193191322)
to learn more.

Note: For end users to be able to respond to approval requests in your help center, you must update its theme. See [Updating your theme with EAP features](https://support.zendesk.com/hc/en-us/articles/8841434696218).

## Approval request examples

Depending on how your organization uses Zendesk, you can use approvals for both customer service and employee service needs.

Some examples of how you may want to use approvals include:

- Software and hardware procurement and access
- Employee promotions or job changes
- Long-term leave requests
- Payroll issues
- Refunds

For example, say your organization uses the Employee Service Suite.
A new employee in your company needs access to software and [submits a service request](https://support.zendesk.com/hc/en-us/articles/9443951695514)
through the service catalog. An employee with an agent seat can create an approval request associated with the service request's ticket on behalf of the new employee in the Agent Workspace and send it to an approver for review. In this example, the approver could be the new employee’s manager or another employee in your IT department. The other employee may or may not have an agent seat.

Alternatively, if your organization uses the Customer Service Suite, you can request approvals to resolve customer service tickets. For example, an agent has been assigned a ticket requesting a refund.
They need authorization to proceed with the end user's refund, so the agent creates an approval request and sends it to an approver in your organization, such as the agent's team lead.

In all of the examples above, the approval decisions are tracked in the approval request on the ticket and in the [ticket events](https://support.zendesk.com/hc/en-us/articles/4408829602970)
so that you can keep track of approvals in your organization.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/es_approvals_ticket_messages.png)

## Reporting on approval requests

When approval requests are turned on for an account, a new ticket field is created: **Approval status**. This field automatically reflects the status of an approval request associated with the ticket and can be leveraged in Explore reporting. See [Reporting with custom fields](https://support.zendesk.com/hc/en-us/articles/4408824384538).

## Approval request resources

To learn more about turning on and using approval requests, see:

- [Turning approval requests on and off](https://support.zendesk.com/hc/en-us/articles/9475816348442)
- [Creating approval requests](https://support.zendesk.com/hc/en-us/articles/8481158639770)
- [Viewing and withdrawing approval requests](https://support.zendesk.com/hc/en-us/articles/9483757385114)
- [Responding to an approval request as an agent](https://support.zendesk.com/hc/en-us/articles/8481193191322)
- [Responding to approval requests as an end user](https://support.zendesk.com/hc/en-us/articles/4408837910426#topic_ay1_m3h_zfc)