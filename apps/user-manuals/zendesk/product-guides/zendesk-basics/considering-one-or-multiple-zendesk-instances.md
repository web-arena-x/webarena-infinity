# Considering one or multiple Zendesk instances

Source: https://support.zendesk.com/hc/en-us/articles/4408883091994-Considering-one-or-multiple-Zendesk-instances

---

Your company may have multiple organizations that include a variety of departments with different processes, security needs, and workflows. It's useful to consider if one Zendesk instance will work well for your situation, or if multiple instances would be better. This article describes the benefits, considerations and consequences of using multiple Zendesk instances instead of using just one. It includes the following topics:

- [Feature considerations](#h_4668644872031535056322970)
- [Scoping questions](#h_8232884472121535056343026)
- [Summary](#h_1108117232291535056381715)

## Feature considerations

This topic covers the impact of using one Zendesk instance for multiple teams for the following features:

- [Global settings](#h_6987689601331535049025839)
- [Business rules](#h_4426346181541535049096896)
- [Integrations](#h_1805212981641535049114989)
- [Authentication and access](#h_4083103611731535049132138)
- [End user management](#h_8289472011811535049153997)
- [Agent permissions and ticket access](#h_01GXYEHBC8GHBVFRJX6EBSYDJS)
- [Reporting](#h_8513726261911535049172882)
- [Web Widget (Classic) and Chat widget](#h_5768327541971535049188395)
- [Guide](#h_4578988162021535049200694)

### Global settings

This section describes considerations for global settings.

- **Subscription**If you have one Zendesk instance, all agents must be on the same plan type for Support, Guide, Talk, and Chat. For Guide in particular, all Support agents have to be Guide agents. If only one team leverages Guide, this is a cost saving consideration.
- **Agent Signatures** There is one native global agent signature per Zendesk. As a workaround, you can customize triggers for each team, with the signature in the trigger or Liquid Markup conditions.

- **Email template** There is only one native email template per Zendesk. The workaround is customizing all business rules, which support HTML, CSS, or Liquid Markup. See [Understanding Liquid markup and Zendesk Support.](../business-rules/understanding-liquid-markup-and-zendesk-support.md)
- **Welcome/verification emails** There is only one native end user welcome email/verification that follows the account name added in Settings > Account.
- **Subdomain** You can only have one subdomain for all agents to use and remember. It is not possible to customize the agent subdomain to team names.
- **Anybody can submit requests?** One Zendesk account needs to be either open to all users or closed to all users. If open, anyone can submit a request, login to Guide, or submit a ticket with the widget. If closed, the end user must be an existing user in Support to submit a request, or access Guide. See [Configuring how end users access and sign in to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408887573274-Configuring-how-end-users-access-and-sign-in-to-Zendesk-Support).
- **Account name**
 - There is only one account name. See [How do I change my account name in Zendesk Support?](https://support.zendesk.com/hc/en-us/articles/4408894168602-How-do-I-change-my-account-name-in-Zendesk-Support-).
 - The account name is visible in emails if using *formatted* placeholders. The account name is a part of the email sent and visible to end users. To bypass this, you need to stop using formatted placeholders and use rich content placeholders instead which support rich text. However, this eliminates the aesthetic experience of formatted placeholders.
 - Finally, the account name is visible on login page/prompt and is not editable.

- **Allow users to belong to multiple organizations** If you decide to use one Zendesk instance across different teams, there is one global setting that is enabled or disabled for the entire instance.
- **Satisfaction survey** Even though satisfaction surveys are enabled or disabled for the entire Support instance, you can edit business rules to not fire for certain groups. A satisfaction link can be generated for any ticket using placeholders. See [Using customer satisfaction rating placeholders](https://support.zendesk.com/hc/en-us/articles/4408886173338-Using-customer-satisfaction-rating#topic_hlb_fjw_cc).
- **Data export** Data exports of tickets, users, and organizations are global for the entire account. However, you can use the Zendesk [Core API](https://developer.zendesk.com/rest_api/docs/core/introduction) to fetch more specific data.
- **Tags** In an instance with multiple teams, tags should not be recycled for multiple workflows or resources.

### Business rules

This section describes considerations for business rules.

- **Triggers, automations, views, and SLAs**
 - Business rules run on all tickets, but they can be easily restricted with conditions that look up at ticket group or brand. See [Using groups in business rules.](https://support.zendesk.com/hc/en-us/articles/4408894175130-Creating-managing-and-using-groups#topic_uxo_gag_bc) Admins are global and can create rules for groups outside of the ones they administer. This creates a risk of an admin for one team editing rules that impact other teams' tickets and workflows.
 - If you use different teams within the same Zendesk instance, there is an increasingly large number of rules to manage. Increased complexity requires a change management strategy and on-going cross team collaboration. There is also an increased risk of tickets being misrouted to incorrect groups, which can have implications on SLAs.
 - You also need to make considerations for confidential or secured information being visible to agents who should not have access to it. There isn't a native method to organize business rules by group.
 - To assist with business rule organization/grouping, placeholder triggers or automations can be created that have no function other than a name that helps create the experience of rule categorization by team.
- **Macros** Macro access can be configured to all agents or agents in groups. See [Creating personal macros for tickets](https://support.zendesk.com/hc/en-us/articles/4408844187034#topic_zh2_4nw_4y) for more information.
- **Ticket fields and ticket forms**
 - Ticket fields and ticket forms are global for the entire instance. All teams can see all forms and fields. Custom ticket forms are required to have unique forms for different teams and end user experience.
 - In the agent interface, a custom app could hide or show certain fields depending on the current agent viewing the ticket. You can also consider implementing the recipe outlined in article on [restricting ticket forms](https://support.zendesk.com/hc/en-us/articles/1-Can-I-restrict-a-ticket-form-so-that-it-can-only-be-used-by-agents-in-a-specific-group-).
 - Help center code customizations can hide non-required end user editable fields from the request form.

### Integrations

This section describes considerations for integrations.

- **JIRA** The v3 of the Zendesk JIRA integration is one-to-one. You cannot link multiple JIRA integrations to one Zendesk Support account.
- **Custom integrations** Multiple Support instances require setup and configuration of each custom integration. For example, running data exports or connecting to a user database require development and configuration on both sides for each Support instance.
- **Apps (ZAF)** Apps need to be installed and configured in each Support instance. If native options are not granular enough for your needs, you can code a custom app to check the user group and hide or show the app. It is possible to specify access to apps per group or custom role natively. See [Restricting the visibility of an app by group.](https://support.zendesk.com/hc/en-us/articles/1-Restricting-the-visibility-of-an-app-by-group)

### Authentication and access

This section describes considerations for authentication and access.

- **Basic authentication** With multiple Zendesk instances, logins (username and passwords) are unique to each instance. Agents and end users would need to manage and remember two sets of credentials for multiple instances of Zendesk that use native Zendesk authentication.
- **API access** API tokens are global, which means that any user with an API token can access all resources and data in the account.
- **OAuth** OAuth tokens can be scoped to only access certain resources. However tokens *cannot* be [scoped to agent groups](https://developer.zendesk.com/rest_api/docs/core/oauth_tokens#scopes).
- **Single sign-on (SSO)**
 - The native SSO applies to the entire instance for both agent and end user configurations. Agents and end users for all teams would need to be configured in the SSO identity provider.
 - There are workarounds for users to be able to use different authentication methods (Zendesk auth and SSO), but this would have to be built on the customer side. See [Having the talk: Am I ready for a more advanced authentication option?.](https://support.zendesk.com/hc/en-us/articles/4408836542618-Having-the-talk-Am-I-ready-for-a-more-advanced-authentication-option-)

### End user management

This section describes considerations for user management.

- **Organization and user fields** Organization and user fields are global for the entire instance, which means that all agents can see and possibly edit them all. As with the ticket fields, a custom app can hide or show certain organization/user fields depending on the agent who does the viewing.
- **Organization management**
 - Organizations are global for the entire instance. It is not possible to segment organizations or organization viewing permissions by agent groups.
 - For the [organization ticket sharing feature](https://support.zendesk.com/hc/en-us/articles/4408882246298-Creating-managing-and-using-organizations#topic_nat_vgn_bc), the access permissions are global to all tickets in an organization. If this option is enabled, it impacts all teams’ tickets using Support and Guide.
 - Organization names must be unique. While it is possible for users to belong to multiple organizations, it is not possible to have two organizations with the same name to accommodate multiple teams.
- **End user permissions and access**
 - All end users are global to the entire instance. It is not possible to allow one end user to submit requests to one team in an instance, but not allow requests to another.
 - Only one primary method of end user authentication is supported natively. End users are able to login to all help center instances. There are workflows that bypass this behavior, but they are highly customized and require some development on the customer side.

### Agent permissions and ticket access

- **Agent permissions to edit end users** There are several considerations depending on plan type:
 - **Custom agent roles**: If your plan type includes custom roles, you can allow one group of agents to edit end user profiles but not another. Agents are able to view the user profile of all end users. There are edge-case configurations where an agent does not have access to a ticket in another group, but does have access to edit end users. This includes end user assumption where the agent could see ALL tickets the end user requested.
 - **Agent role**: On plan types without custom agent roles, only agents with access to *all tickets* will be able to add, edit, or assume end users.
 - **Special use cases** where agents for one team are considered end users for another team: Agents cannot submit tickets using the help center, and because of that, any end user forms will not work for agents. Regardless of group permissions, agents have access to tickets where they are the requesters, which means they can access any internal communication for their requester.
- **Groups management and ticket access**
 - Groups are global for the entire instance. It's possible create groups to manage multiple teams and restrict ticket access by group.
 - On Enterprise plans, you can [create private ticket groups](https://support.zendesk.com/hc/en-us/articles/4767122732058). Private ticket groups provide more granular control over the visibility and access to tickets based on group assignment by completely hiding private tickets from agents who don't have permission to view them.
 - Also on Enterprise plans, you can use custom agent roles to control agents' access to private ticket groups, including their ability to assign tickets to private groups.

### Reporting

This section describes considerations for reporting.

- **Reporting** 
 - If using one instance, reporting is centralized. All ticket, user, and organization data is available to all users with access to reporting.
 - In different plans, access to tickets controls access to reporting. Agents need access to all tickets to view reporting.
 - The default reporting dashboards are global to all Support data, which means that reporting broken down by group or some other ticket level attribute (custom ticket field, ticket brand, etc.) would need to be custom built.
- **Native reporting** Native reporting (not Explore) Overview, Leaderboard, Knowledge, Community, Search, & Talk are global analytics for the entire instance.

### Web Widget (Classic) and Chat widget

This section describes considerations for the Web Widget (Classic) and Chat widget. They may not apply to the messaging Web Widget.

- Native customizations and appearance (color, position, button text) are global. It is possible to use the [Widget API](https://developer.zendesk.com/embeddables/docs/widget/api) to customise the widget per team, but this requires custom development.
- Ticket forms would be required to have a tailored form/field experience per team.
- The help center Search in the widget searches the entire knowledge base and only one knowledge base. However, with some custom development, you can [possibly](https://developer.zendesk.com/embeddables/docs/widget/api#ze.sethelpcentersuggestions) customize search results.
- Chat can be either on or off for the widget, which can have implications if only one team uses Chat. You might be able to override this setting with [Widget API](https://developer.zendesk.com/embeddables/docs/widget/api) and [Chat API](https://developer.zendesk.com/rest_api/docs/chat/introduction) customizations.

### Guide

This section describes considerations for guide.

- **Permissions for agents**
 - A collaborative strategy is required if multiple teams are using one Guide. For instance, agents on one team who are managers will be able to manage content and edit themes for other teams, even if you are using [Multibranding](https://support.zendesk.com/hc/en-us/articles/4408833921306-Multibrand-resources-Enterprise-).
 - Article edit and creation permissions are a mix of Support settings and Guide section level settings. Zendesk Support administrators are Guide Managers by default.
 - If you are on a plan type with custom roles, you can create a custom role and set the Guide Manager permission. If you belong to a different plan, you can control who is a Guide Manager or Viewer in the agent's profile page. See [Understanding Guide roles and setting permissions.](https://support.zendesk.com/hc/en-us/articles/4408827842458-Understanding-Guide-roles-and-setting-permissions)
 - Agents can be set as a Viewer in Support, but still create and edit articles in all sections set to managers and agents in section-level permissions.

- **End user experience**
 - If using one Zendesk, all end users would be able to login to all help centers. If there are common end users when multiple teams are using one Zendesk Support instance for ticketing, end users would have one set of login credentials as opposed to multiple login credentials if the teams use separate Support instances.
 - End users can see all tickets in one place if using one Support instance. However, this does not apply if tickets are in different brands.
 - [User segments](https://support.zendesk.com/hc/en-us/articles/4408824005914-Applying-user-segments-to-restrict-access-to-Help-Center-knowledge-base-content) and permission strategy is required to manage who can view what content for all help centers associated with one Support instance.
 - Finally, if agents on one team are end users on another team, they will have a diminished help center experience. They would be redirected to Support to submit and view requests.

## Scoping questions

Before you make a final decision, consider these scoping questions:

### Should all agents have access to all tickets?

If you are using one instance of Support with multiple teams, here are the considerations for allowing access to all tickets, or not allowing access to all tickets.

Allow access to all tickets:

- If agents can access all tickets, how complex/scalable would it be to set up and separate ticket routing using Business Rules (views, triggers, automations, SLAs, email templates) for each team as Business Rules are global for the entire instance?
- For example, if two teams (Support & Sales) use one Zendesk, a routing trigger for each team (as well as separate triggers for each auto-reply/comment update) are required to customize the end user experience for each team.
- Increased risk of a ticket being misrouted in terms of SLAs.

Do not allow access to all tickets:

- Configuration of groups or custom roles is required to restrict access.
- Careful ticket routing management is required so tickets are not accidentally routed to a group that should not access the ticket.
- Limits visibility for agents into the other historic or current requests. Ticket access restriction can also restrict agent access to reporting.
- Depending on your configuration, if restricted agents have the ability to assume end users, they would potentially be able access tickets outside of their group from **My Activities** in help center.

### Is there a centralized or existing user management strategy?

Items to consider for agents and end users include:

- In terms of Zendesk authentication, users who are agents in both instances would have two sets of credentials.
- If you are using SSO, Zendesk needs to be configured as a service provider for both instances. If you are passing custom user data, you need to create user or organization fields in both instances. All custom user fields, organizations, and role have unique IDs, which requires configuring unique SAML/JWT assertions.

Additional considerations for end users include:

- Should end users have access to help center content for both teams (for example, both HR and Support use one instance?
- Should end users have access to all HR and all Support content?

## Summary

Here's a quick overview of the benefits and considerations of using one instance vs. multiple instances:

If you're using one Zendesk support instance, benefits include:

- Unified customer experience.
- Unified reporting.
- Agent cost: agents on both teams only require one license.
- Cross-department escalations or tracking of issues are easier within one Support instance.
- Unified user management and authentication:

- Single source of truth for users.
- 360 view of customer.

Items to consider are:

- On certain plan types, restricting access to tickets is complex.
- Experience of agents who are end users for other teams is diminished.
- Requires a defined change management process and strategy.
- Increased complexity for ticket routing and business rules.
- Many customizable features of Support are globally configured (such as authentication, email template, account name, or welcome emails).

If you're using multiple Zendesk instances, benefits include: 

- Compartmentalization is easier.
- Flexibility to make changes that do not risk impacting other teams.
- Independent and fully customizable Tier 0/self-service and knowledge workflows (KCS, Answer Bot, Team Publishing).
- Fully customizable and tailored end user experience per team (proper end user experience for agents who are end users for other teams).
- Control by team over ticket access and security.

Items to consider are:

- Overhead cost for configuration and analytics for multiple instances.
- Configuration of SSO, apps, and integrations required for all instances.
- End users need to go to different places for submitting requests or self-service.
- Agent collaboration complexity increases due to having to use ticket sharing between Support instances.
- The agent collision feature does not work between two Support instances.
- While Ticket Sharing can allow two teams both using Zendesk to collaborate, the ticket updates would be asynchronous from the ticket of one Support instance to the other.
- On certain plan types, controlling ticket access and security by team can be accomplished in a single instance by creating private ticket groups.