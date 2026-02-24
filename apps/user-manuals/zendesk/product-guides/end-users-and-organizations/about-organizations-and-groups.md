# About organizations and groups

Source: https://support.zendesk.com/hc/en-us/articles/4408886146842-About-organizations-and-groups

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

[Organizations](https://support.zendesk.com/hc/en-us/articles/4408821417114) and [groups](https://support.zendesk.com/hc/en-us/articles/4408831652890) are used to manage your Zendesk Support users and the ticket handling workflow.

This article discusses the following topics:

- [Organizations and groups, defined](#topic_iny_3jg_sz)
- [End users and organizations](#topic_npu_dkx_ac)
- [Agents and groups](#topic_qsg_zkx_ac)
- [How groups support organizations](#topic_mbq_ixx_ac)
- [How to use your organizations and groups](#topic_uhb_xlq_ac)
- [Administrator and agent roles for users, groups, and organizations](#topic_ryf_kmq_ac)

Related articles:

- [Creating organizations](https://support.zendesk.com/hc/en-us/articles/4408882246298)
- [Creating groups](https://support.zendesk.com/hc/en-us/articles/4408894175130)
- [Changing the default group for your account or a team member](https://support.zendesk.com/hc/en-us/articles/4408828237722)

## Organizations and groups, defined

Each collection of users is defined as follows:

- **Organizations**

  Organizations are typically collections of your end users, but they can also include team members. On the Team plan, users can belong to only one organization. On Professional and Enterprise plans, users can belong to up to 300 organizations. The use of organizations is optional, but by arranging your end users into organizations you can keep track of what those organizations are requesting. You can also enable users within an organization to see each other’s tickets. This expands visibility of the organization's support issues and should reduce the number of duplicate tickets.
- **Groups**

  Groups collect team members together based on criteria those team members have in common. Groups can only contain team members; no end users can be included. All agents must be assigned to at least one group, but they can be members of more than one. Groups can be used to support organizations. You can designate one group as the default group for your account and you can also designate a default group for each team member. All new team members you create will be added to the default group.

## End users and organizations

Although you don't have to add your end users to organizations, it can be extremely helpful in managing the workflow. First, let's define what we mean by end user. These are the people that generate support requests. They are your customers in a retail setting and the employees that are supported by an internal help desk in a corporate setting (to name two common types of end users). How you organize your end users is entirely up to you; however, here are a few examples of how organizations can be used:

- **To support service level agreements**

  You can create organizations that mirror the [service level agreements](https://support.zendesk.com/hc/en-us/articles/4408829459866) that you've established with your customers. For example, your paying customers are guaranteed a faster response than those who use your free services and you want to distinguish between the two. Or, perhaps you've set up levels of support based on which version of your products and service levels your customers have purchased (for example: basic, professional, enterprise or silver, gold, platinum). You can create organizations for each set of customers and route them through the support workflow accordingly. You can then create business rules and reports to escalate tickets as needed and to track performance against your service level agreements.
- **To track and manage tickets by company**

  Perhaps you sell your products to other businesses. You can create organizations for each of those companies to manage and track their ticket activity.
- **To manage requests based on email domains**

  You can automatically add end users to organizations based on their email domain. For example, you might have both internal and external end users. You can create an organization for your internal end users and automatically add them to the organization, based on their email domain, the first time they submit a request. The new request is then picked up in the workflow rules you've set up for that organization.

  Note: When you add a domain to an organization, that domain is handled as if it has been added to your [allowlist](https://support.zendesk.com/hc/en-us/articles/4408886840986) and overrides the blocklist. While this raises the threshold from spam detection for all emails from that domain, it doesn't prevent emails from being marked as spam. Emails that appear to be spam may still be marked as spam.
- **To support customers by location and language**

  If you support organizations or individual customers across the globe, you can create organizations for locations and languages and then route those requests to agents that are co-located and speak the same languages.
- **To define access to Help Center**

  You can use organizations to create user segments to define who can see what in your Help Center. You might want most of your Help Center to be viewable by all end users but also create several just for certain groups of users (customers with premium service plans, perhaps). Organizations enable you to do this. For information see [Creating users segments for Guide user permissions](https://support.zendesk.com/hc/en-us/articles/4408837707290).

You can create organizations and add end users to them manually, one at a time, or automate the process by adding users and their organizations in bulk import operations.

Team members can also be added to an organization. You might do this as part of organizing the users in Zendesk Support or to restrict an agent's access to only the organization they belong to (this is an option when setting the agent's privileges).

Once you've gotten organizations set up, they can be used in many ways in Zendesk Support to manage your workflow. See [How to use your organizations and groups](#topic_uhb_xlq_ac) below.

## Agents and groups

Groups are only for team members and every agent must belong to at least one group. Like organizations, how you set up groups depends on your business needs and the support workflow you prefer. Here are some of the common ways that groups are used:

- **To escalate tickets based on complexity**

  You can manage escalation by setting up a tiered support group structure. For example, you can create groups for levels of support based on factors such as urgency and complexity. By default, you could assign all tickets to the Level 1 group and then escalate them to Level 2 manually based on the technical complexity of the issue. The Level 2 agents (who may also be members of the Level 1 group) have the advanced technical skills needed to resolve the issue. For an example of this, see [Managing your escalation queue](https://support.zendesk.com/hc/en-us/articles/4408821995290).
- **To support service level agreements**

  As in the example for organizations above, you can set up corresponding groups to support organizations defined by service levels.
- **To provide support by expertise**

  You can create groups based on expertise. For example, a company that develops both software and hardware might place the team members who support the software into one group and those team members who support the hardware in another. A custom field could be added to the support request form prompting end users to specify the product they're seeking support for and this could be used to route the ticket to the appropriate group.
- **To support customers by location and language**

  As noted above, you can set up organizations by location and language and then assign team members (or groups) to their tickets. Even if you didn't set up organizations for this, you can route to tickets to these groups based on the end user's email domain (*somecompany*.fr, for example) or their language preference.
- **To keep sensitive tickets private (Enterprise only)**

  If you have tickets that contain sensitive or protected information, such as personally identifiable information or security issues, you can create private groups. Only admins and agents in the private group can see tickets assigned to the group. Collaborators and followers, if added to a private ticket, can see all comments, but will not be able to see other tickets within the group. Private groups cannot be converted to public. See [About private ticket groups and how they work](https://support.zendesk.com/hc/en-us/articles/4767122732058).

When you create groups, you can add existing team members to them. You can add new team members to one or more groups when you're adding them to Zendesk Support. You can also bulk import new users and define their role as agent, then manually add them to groups.

### Standard groups

All Zendesk Suite and Support plans start out with one group named *Support*. If that's the only group you have, all agents are assigned to the group and it's treated as the default group for your account. After you start creating groups and assigning agents to them, you must designate one of them as the account's default group.

In addition to the standard *Support* group, Employee Service Suite plans include the following additional groups that are designed to help you arrange your agents based on common HR and IT teams and responsibilities:

- [SAMPLE] HR
- [SAMPLE] Benefits team
- [SAMPLE] Payroll team
- [SAMPLE] IT hardware support
- [SAMPLE] IT software support
- [SAMPLE] Approvers

See [Using the sample data for employee services](https://support.zendesk.com/hc/en-us/articles/9012803758362).

## How groups support organizations

So how do groups support organizations? In the broadest sense, simply by becoming hubs of support for the tickets that are received from the end users in your organizations. What group is assigned to an organization's tickets can be based on the many considerations outlined above (support escalation processes, security, co-location and language, and so on).

You can take a loose approach to this and just allow team members to triage and assign requests to groups based on their reading of the support request or you can create business rules to handle that automatically. See [How to use your organizations and groups](#topic_uhb_xlq_ac) below.

You can also more tightly manage the workflow and create security boundaries by funneling tickets directly to agents who have restricted access. This means that they can only see the tickets that they are allowed to see. You can do this in two ways. The first is to add the agents to groups and then restrict their access to only those groups. You can also add an agent to an organization, which restricts their access to only those tickets that are submitted by end users in that organization.

Note: In Zendesk Support, you'll see references to *non-restricted agents*. These are agents who have not been restricted in these ways and can access all tickets.

## How to use your organizations and groups

Once you've got an organization and group structure in place, you can use it to manage the ticket workflow and monitor your Zendesk Support activity.

Here are some of the ways you can use organizations and groups in your workflow:

- Automatically assign tickets received from users in an organization to a specific group, referred to as *group mapping* (see [Mapping a group to an organization](https://support.zendesk.com/hc/en-us/articles/4408882246298#topic_cfj_gfn_bc)).
- Map incoming new users to an organization based on their email domain, referred to as *user mapping*.
- Allow users within an organization to see all the tickets in their organization, referred to as a *shared organization* (see [Setting up a shared organization for end users](https://support.zendesk.com/hc/en-us/articles/4408882246298#topic_nat_vgn_bc)).
- Assign team members to support a specific organization (see [Adding users to organizations](https://support.zendesk.com/hc/en-us/articles/4408846640410#topic_wyj_dse_bc)).
- Use organization as a condition in a trigger to automatically assign requests to a group or team member (see [Building trigger condition statements](https://support.zendesk.com/hc/en-us/articles/4408893545882)).
- Use a trigger condition to test for tags and then automatically assign requests to a group or team member based on those tags (see [Creating triggers for ticket updates and notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466)).
- Create macros that assign new requests to a group or team member (see [Using macros to update tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602)).
- Create automations that escalate tickets to a group or team member (see [Creating and managing automations for time-based events](https://support.zendesk.com/hc/en-us/articles/4408883801626)).
- Create views by organizations or groups (see [Creating views by organization](https://support.zendesk.com/hc/en-us/articles/4408846640410#topic_kwp_zcf_bc)).
- Create reports by organizations or groups (see [Explore resources](https://support.zendesk.com/hc/en-us/articles/4408846357018)).

## Administrator and agent roles for users, groups, and organizations

Here's a quick overview of who can do what in Zendesk to manage users, groups, and organizations.

**Administrators**

- Add end users manually (one at a time) or add many end users at a time in a bulk import
- Create and edit organizations and groups
- Merge one organization into another
- Add end users to organizations
- Create new team members and add them to one or more groups and one organization
- Limit an agent's access to one or more groups
- Limit an agent's access to requests received from the organization that an agent belongs to
- Set up email mapping (automatically map end users from specific email domains to an organization)
- Set up group mapping (assigning incoming requests from users in an organization to a specific group)
- Set up a shared organization (allow all end users in an organization to view tickets from all users in the same organization)
- Create both shared and personal views by users, groups, and organizations
- Create business rules (automations, macros, and triggers) that include groups
- Create business rules (automations and triggers) that include organizations
- Create reports that include groups and organizations

**Agents**

- Add end users
- Add end users to organizations
- Allow end users to view all the tickets in their organization (if the user belongs to a shared organization, then the user always has access to tickets in the organization)
- Create personal views by users, groups, and organizations
- Create macros to assign tickets to a group