# Understanding and setting light agent permissions 

Source: https://support.zendesk.com/hc/en-us/articles/4408846501402-Understanding-and-setting-light-agent-permissions

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Collaboration add-on |

Verified AI summary ◀▼

Light agents can view tickets, make private comments, and provide expertise without full permissions. You can configure their access to tickets and reports based on your plan. Light agents can't be assigned tickets or change statuses unless they're the requester. Customize their permissions for ticket access and reporting to fit your team's needs while maintaining control over their capabilities.

Note: Most Zendesk Suite plans automatically include a default number of
light agents based on your plan type, but you can [buy more light agents](https://support.zendesk.com/hc/en-us/articles/6510562911770#topic_dzr_hf5_5zb) if needed. These restrictions
do not apply to legacy plans or add-ons.

- Suite Team plans offer light agent seats as an add-on.
- Suite Growth plans include up to 50 light agents.
- Suite Professional plans include up to 100 light agents.
- Suite Enterprise plans include up to 1000 light agents.
- Suite Enterprise Plus plans include up to 5000 light agents.

Light agents have limited permissions but can stay informed about tickets and, when needed,
provide subject matter expertise and advice by adding private comments to the ticket. Ticket
comments by light agents are private, including the first comment of any tickets they create.
However, when a light agent is the ticket requester, and they're not a member of the group or
brand, their private comment will be converted to public.

To assign a light agent role, see [Setting roles and access in Zendesk Admin Center](https://support.zendesk.com/hc/en-us/articles/4408824375450).

This article contains the following sections:

- [Understanding what light agents can do](#topic_vwz_qm1_blb)
- [Configuring light agent ticket access and reporting permissions](#topic_mxz_qm1_blb)

Related articles:

- [About light agents and contributors](https://support.zendesk.com/hc/en-us/articles/4408832171034#topic_mjl_s3c_wrb)

You are prohibited from using the API or any
Software to effectively provide light agents with access, functionality, or permissions that
they are not otherwise permitted to use or access in the Zendesk Support Agent user interface
(as set forth below).

## Understanding what light agents can do

Light agents have the following access and permissions.

Note: If you've created [shared macros](https://support.zendesk.com/hc/en-us/articles/4408844187034#topic_zh2_4nw_4y), your light agents can't use a macro
that applies an action that they don't have permission to do. For example, if you have a
shared macro that changes the ticket status, light agents can access the macro but if they
try to apply it, the ticket status won't change.

| Area | Light agents can... | Light agents can't... |
| --- | --- | --- |
| Tickets | - View either tickets assigned to groups they're in or view all tickets - Make private comments. On Enterprise plans and above, if they're the ticket   requester and lose access to the ticket because they're not a member of the   group or brand, their private comment will be converted to public. - Be the ticket requester - Edit ticket properties at the time of ticket creation - Be CC'd on tickets (see [Setting permissions for CCs and   followers](https://support.zendesk.com/hc/en-us/articles/4408843795482#topic_x3t_4p5_cq)). End users won't be   able to see light agents who are CC'd on a ticket. - Be added as a follower and add other agents as   followers - Create tickets on behalf of existing end users. However, the end user won't be   able to see it until another agent adds a public comment. - Edit ticket properties for tickets they're requesters on after the ticket is   created - Add, access, and download attachments - Create, reply to, close, and reopen [email-based side conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746) - Add and remove tags from tickets where they're the requester. They can also bulk   add tags where they're the requester but cannot bulk remove tags. - Use [agent email forwarding](https://support.zendesk.com/hc/en-us/articles/4408836514202) to forward an   email to your support address, creating a ticket with a *private* comment. - Reassign tickets to another agent in any of the light agent's groups, if they   are the requester. - Respond to an approval request if designated as the approver | - Be assigned to tickets - Change the ticket status, unless they're the ticket   requester - Reassign tickets to another group, unless they are the ticket requester - Edit ticket properties, unless they're the ticket requester - CC agents or end users other than themselves, except for when they create a   ticket on behalf of someone else via email - Use the @mention feature - Respond to [CSAT surveys](https://support.zendesk.com/hc/en-us/articles/4408886173338) - Create, send, or be assigned [side conversation child tickets](https://support.zendesk.com/hc/en-us/articles/4408826941850) - Use [agent email forwarding](https://support.zendesk.com/hc/en-us/articles/4408836514202) to forward an   email to your support address, creating a ticket with a *public* comment - Create or withdraw approval requests - View highlighted [entity values](https://support.zendesk.com/hc/en-us/articles/6711181959194) or [redaction suggestions](https://support.zendesk.com/hc/en-us/articles/6669399593882) - View the [pages viewed](https://support.zendesk.com/hc/en-us/articles/4408829170458#topic_ehg_1qz_vkb) by the requester in the   customer context panel |
| People | - View user profiles - View the [Customers page](https://support.zendesk.com/hc/en-us/articles/4408828129946), regardless of their   ticket access (Suite Growth and Professional plans only) | - Edit user profiles - Assume a user's identity - Change a user's password - Create new end users - View a user's [device information](https://support.zendesk.com/hc/en-us/articles/4408829170458) |
| Help center (not available in Team plans) | - View areas of the Help Center knowledge base and community that are restricted   to agents - Add and edit articles in the knowledge base [where agents have permission](https://support.zendesk.com/hc/en-us/articles/4408827952538) - Add and edit articles and posts in the community [where agents have permission.](https://support.zendesk.com/hc/en-us/articles/4408821305498) See [Creating community moderator   groups](../setting-up-and-managing-community/creating-community-moderator-groups.md). | - Be a Knowledge admin (see note at left). - View article revisions |
| Reports | - View Explore dashboards that have been shared with them in Zendesk   (Professional and Enterprise plans only)   - External link sharing is available only on Enterprise plans - Create, edit, and delete reports and dashboards. | - Manage administrative settings and permissions for Explore. |
| Views | - See views - Filter views | - Create or edit views |
| Business rules | - Apply macros - (non-Enterprise plans) View triggers and automations | - Create, view, edit or delete macros. - Create, edit, or delete triggers and automations. On Enterprise plans, light   agents also can't view triggers or   automations. - Typically be used as conditions in business rules For example, you can't   create a ticket trigger notifies the assigned agent when a light agent adds a   comments to a ticket. However, you can define trigger conditions that identify   when the ticket requester is a light agent. |
| Channels |  | - Serve a chat or messaging conversation - Respond to calls - Manage channels |
| Mail API |  | - Use the Mail API |
| Apps | - Use most installed Zendesk apps within Support - Perform permitted actions on their tickets in the Zendesk Support Mobile   app |  |

## Configuring light agent ticket access and reporting permissions

After you understand [when to use the light agent role](https://support.zendesk.com/hc/en-us/articles/4408829504154#topic_cvn_xxq_4fb) and what they can
do, you can configure some of the permissions. The method you use to configure permissions
for light agents varies depending on whether you are on a Suite Growth, Professional, or
Enterprise plan. You can configure options for ticket access for light agents, and, if
you're on Suite Professional or above, you can additionally configure access to reports. The
other light agent permissions shown in the table above can't be changed.

- [Configuring light agent permissions with Suite Growth and Professional](#topic_oxz_qm1_blb)
- [Configuring light agent permissions with Suite Enterprise](#topic_sxz_qm1_blb)

### Configuring light agent permissions with Suite Growth and Professional

If you're using Suite Growth or Professional, you can configure light agent permissions
for reports and ticket access.

**To edit reporting and ticket permissions for light agents (Suite Growth or
Professional)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Agent interface**.
2. Next to **Light Agent access**, select an option for **What kind of tickets can
   this agent access?**:
   - **All within this agent's group(s)** for light agents to access only tickets in
     their groups.
   - **Requested by end users in this agent's organization** for light agents to
     access only tickets requested by end users in their organization. This also means
     the light agent won't be able to update organization fields for end users or lookup
     relationship fields that point to
     organizations.
   - **All** for light agents to access all tickets.
3. If you selected **All within this agent's group(s)** above, and you want light
   agents to still be able to assign tickets to any group when they're the requester, also
   select **Agent can assign to any group**.
4. For **What can this agent do with reports**, set Insights reporting permissions to
   **Can view only** or **Cannot view**.
5. When you are finished, click **Save**.

### Configuring light agent permissions with Suite Enterprise

If you're using Suite Enterprise, you can only configure light agent permissions for
reports, Explore, and ticket access.

**To edit reporting, Explore, and ticket permissions for light agents
(Enterprise)**

You can't clone or modify the light agent role, except for the settings for tickets and
reporting.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Roles**.
2. Next to the **Light agent** role, click **edit**.
3. Under **Tickets**, select an option for **What kind of tickets can this agent
   access?**:
   - **Requested by end users in their organizations** for light agents to access
     only tickets requested by end users in their organization. This also means the
     light agent won't be able to update organization fields for end users or lookup
     relationship fields that point to
     organizations.
   - **All within their groups** for light agents to access only tickets in their
     groups.
     - **Assign tickets to any group** for light agents to be able to assign
       tickets to groups they don't belong to, including private groups.
   - **Within their groups and all public groups**
     - **Assign tickets to any group** for light agents to be able to assign
       tickets to private groups they don't belong to.
   - **All** for light agents to access all tickets.
4. If you selected **All within this agent's group(s)** above, and you want light
   agents to still be able to assign tickets to any group when they're the requester,
   also select **Agent can assign to any group**.
5. For **Reports permissions**, set reporting permissions to **No access** or
   **View only**.

   This setting applies to the Reports tool in Support, not
   reports within Explore.
6. For **Explore permissions**, set permissions to **No access**, **View
   only**, or **Manage reports and dashboards**.
7. Click **Save**.