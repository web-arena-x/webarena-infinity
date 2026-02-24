# Launch guide for Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/4408836154266-Launch-guide-for-Zendesk

---

Welcome to Zendesk Support! This article provides the framework you need to get your account up and running. It describes the key items you need to set up and gives you guidelines on where to find more information.

This article contains these sections:

- [Defining your organizational structure](#h_28581946111542753890528)
- [Defining your customer support experience](#h_911135750151543353350613)
- [Configuring settings and access](#h_610881057231543353365344)
- [Integrating external apps and services](#h_304821204301543353974002)
- [Defining ticket routing and workflows](#h_675961721371543354651109)
- [Adding people](#h_466179673441543355586497)
- [Going live to customers](#h_603106721511543356869357)

## Defining your organizational structure

After you've done some basic [planning](https://support.zendesk.com/hc/en-us/articles/4408827906202), the next step is to create an organizational and role structure for your staff members.

There are two main roles for your team members: agent and admin. Agents solve tickets and admins, who can also solve tickets, have additional access to the admin features and are able to set up workflows, for example. Also, there are additional roles for different channels and, on Enterprise plans, also create custom roles for more granular control of permissions.

Groups are used for organizing your staff members. Organizations are meaningful collections of your end-users, but they can also include staff members. For more information, see [About organizations and groups](https://support.zendesk.com/hc/en-us/articles/4408886146842).

It’s a good idea to set up your organization structure at the beginning because it will be needed when you define your workflow in upcoming steps. You’ll add your team members, along with end users, later in the setup process. If you want to [add a few users now](https://support.zendesk.com/hc/en-us/articles/4408824587802-Quick-launch-guide#h_01G9DP4GFQH0B9728YYRZMJ9F0) for testing purposes, you can do so, but know that any admins or agents you add now will be notified and have access to Zendesk.

## Add groups

Groups collect agents together, allowing admins to manage agent ticket assignments and access to tools like views and macros at the group level. Agents can be in more than one group at a time. It’s easy to change group members and assignments without messing with group settings.

![](https://support.zendesk.com/hc/article_attachments/7856435772954)

### Prerequisites

Make sure you have completed [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow) for your account before you start creating agent groups.

### Dependencies

Agent groups are important building blocks for creating business rules that impact ticket routing, ticket security, and ticket views. Make sure you create a comprehensive set of agent groups with consistent naming and clear definitions before you continue with the launch setup. This feature is available on all Zendesk Support plans.

### Examples

- You can define groups of agents based on the Zendesk channels they support.  
  **Zendesk Triage Chat, Talk, Support**
- You can define groups based on the functions agents perform, or their level of expertise.  
  **Zendesk Triage Sales, Finance, Shipping**  
  **Zendesk Triage Tier 1 Agents, Tier 2 Agents, Tier 3 Agents**

### Best practice

Groups matter because you can use them to manage ticket routing and define ticket views. Create groups with a clear purpose and give them a name that matches their function.

### Show me how

- The following video gives you an overview of how to arrange teams into groups:

  Arranging teams into groups [0:57]
- [Creating groups](https://support.zendesk.com/hc/en-us/articles/4408894175130-Creating-managing-and-using-groups)
- [About organizations and groups](../../product-guides/end-users-and-organizations/about-organizations-and-groups.md)
- [Managing your escalation queue](https://support.zendesk.com/hc/en-us/articles/4408821995290)

## Define user roles

Roles are a collection of permissions that define the actions Zendesk users can and cannot take. For example, updating tickets, editing user profiles, or running reports. Each user can have only one role.

![](https://support.zendesk.com/hc/article_attachments/7856435773722)

### Prerequisites

Complete [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow) for your account before you start defining user roles.

### Dependencies

Role definitions vary depending on which version of Zendesk Support you’re using. Support Enterprise has a set of predefined agent roles and you can create *custom roles* as needed. Custom roles are unique roles created by admins that include custom permissions and visibility. In Support Professional and all other plans, you have a fixed set of predefined roles, but you can set additional permissions, such as ticket access, for each agent. Roles are available on all Zendesk Support plans.

### Examples

In Support Professional, the roles include:

- **End users**: Internal or external customers who communicate questions or requests.
- **Agents**: Staff members who communicate with end users and solve their support issues.
- **Administrators**: Staff members who configure Zendesk Support to manage workflows.

### Best practice

If possible, avoid creating roles for individual users. It can become difficult to manage a large number of roles as you grow your team. To maintain account control, limit the number of users with Admin permissions (no more than 5).

### Show me how

Make sure you have the roles you need for your users, but don’t assign roles to users, yet.

- [Understanding Zendesk Support user roles](https://support.zendesk.com/hc/en-us/articles/4408883763866-Understanding-Zendesk-Support-user-roles)
- [Creating custom roles and assigning agents](https://support.zendesk.com/hc/en-us/articles/4408882153882-Creating-custom-roles-and-assigning-agents-Enterprise-)

## Customize user fields

To store additional details about your customers, you can add custom user fields to user profiles. Agents can view and edit custom user fields as part of the user’s profile that appears in tickets. Fields you add apply to all users.

![](https://support.zendesk.com/hc/article_attachments/7856435762586)

### Prerequisites

Examine your existing customer records to plan for the custom user fields you want to import into Support. Complete [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow) before you start creating custom user fields.

### Dependencies

Adding custom user fields early in your launch process is important because you can create triggers, automations, macros, and reporting based on user fields. When you’re ready to bulk import users you can map user fields from your source applications into Support. This feature is available on all Zendesk Support plans.

**Important:** Add your custom user fields now, but do not import users, yet.

### Examples

- An airline might include SMS numbers in their user profiles to ensure they can contact customers immediately about flight changes, weather issues, and so on.
- A real estate agency might include business license numbers as part of their user profiles, and a car rental company might include driver’s license numbers as part of the user profile.
- Use a custom field to identify your VIP customers so you can easily recognize them and enhance their customer experience.

### Best practices

- When you add custom fields to user profiles, focus on collecting information that is specific to each individual user (for example, license numbers). Information that applies to collections of users, such as location, time zone, or priority, are best added as part of user [organizations](#intro_orgs).
- Too many user fields can create unnecessary noise when looking at a user profile. Only include information that is necessary to solve, route, or prioritize tickets in Zendesk.

### Show me how

- [Adding custom fields to users](../../product-guides/end-users-and-organizations/adding-custom-fields-to-users.md)
- [Bulk importing users](https://support.zendesk.com/hc/en-us/articles/4408893496218-Bulk-importing-users-)
- [Viewing customer context in a ticket](https://support.zendesk.com/hc/en-us/articles/4408829170458-Viewing-customer-context-in-a-ticket)

## Customize organization fields

Similar to adding custom fields to users, you can add custom fields to organizations to store additional details about your customers and help you manage your ticket workflow. Any custom organization fields you create will apply to all organizations. These fields are visible to agents, but not end users.

![](https://support.zendesk.com/hc/article_attachments/7856435764506)

### Prerequisites

Complete [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow) for your account. Have a clear understanding of the organizations you plan to use before you create custom organization fields. Add custom organization fields first **before**[creating organizations](#intro_orgs).

### Examples

- A company that sells software to other businesses might want to capture a **Contract agreement** (monthly, annual, five year) and **Service level** (gold, platinum, bronze) for each organization they support.
- An IT department might want to capture a **Manager for approval** for each organization they support.

### Dependencies

Custom user and organization fields are available on all Zendesk Support plans.

### Best practices

When you add custom fields to organizations, focus on information that applies to collections of users, such as location, time zone, or priority. Information that applies to individual users, such as license number, is best added as a [custom user](#intro_user_fields) field.

### Show me how

- The following video gives you an overview of how to create custom fields for organizations:

  Creating custom fields for organizations [1:40]
- [Adding custom fields to organizations](../../product-guides/end-users-and-organizations/adding-custom-fields-to-organizations.md)
- [Automatically tagging tickets from specific users and organizations](https://support.zendesk.com/hc/en-us/articles/4408883863450)

## Create organizations

Organizations are meaningful collections of your end-users. You can use organizations to group users from the same company or department, add important information to tickets for routing or reporting, and report on which customers are creating the most tickets.

![](https://support.zendesk.com/hc/article_attachments/7856391213978)

**Important:** In Zendesk, you typically use Groups to create collections of agents and Organizations to create collections of end-users.

### Prerequisites

Complete [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow) for your account and agent groups before you start creating organizations. If needed, add custom organization fields first **before** creating organizations.

### Dependencies

Adding organizations early in your launch process is important because you can create triggers, automations, macros, SLAs, and reporting based on organizations. You can use [group mapping](https://support.zendesk.com/hc/en-us/articles/4408882246298-Creating-managing-and-using-organizations#topic_cfj_gfn_bc) to automatically assign tickets received from users in an organization to a specific group. This feature is available on all Zendesk Support plans.

### Examples

- You can use organizations to separate users by product type or brand.
- You route tickets based on user organizations to make sure customers who speak a specific language are served by agents who speak the same language, and you can route tickets to make sure customers in a specific time zone are served by agents in the same time zone.

### Best practices

- You can be as specific as you need when creating organizations. For example, you could have a separate organization that handles VIP customers in France who have questions about your telecommunications products, then set a trigger that automatically routes that ticket to the appropriate agent.
- If you are using Zendesk for HR issue tracking, make sure that your organizations do not allow users within the organization to see each other’s tickets.
- Rather than adding organizations one at a time, you can [bulk import](../../product-guides/end-users-and-organizations/bulk-importing-organizations.md) organizations from a CSV (comma separated values) file.
- Using apps available in the [Zendesk Apps Marketplace](https://www.zendesk.com/apps/directory/#E-commerce_&_CRM), you can sync your organizations with your CRM to keep them up-to-date.

### Show me how

- The following video gives you an overview of how to create an organization:

  Creating organizations [1:01]
- [Creating, managing, and using organizations](https://support.zendesk.com/hc/en-us/articles/4408882246298-Creating-managing-and-using-organizations)
- [About organizations and groups](../../product-guides/end-users-and-organizations/about-organizations-and-groups.md)
- [Adding custom fields to organizations](../../product-guides/end-users-and-organizations/adding-custom-fields-to-organizations.md)

## Defining your customer support experience

Your customers’ experience of the support you provide to them is a collection of contact points that includes your support email addresses, your help center, your social media presence and other channels you set up, and where you’ve embedded your Zendesk (on any website and also in mobile apps).

In Zendesk, a collection of customer contact points is referred to as a *brand*. Depending on your plan, you can have from 5 to 300 different brands. For example, you may provide support for both B2C and B2B customers and want the experience to be different for each.

Another part of the support experience is how your customers submit their support requests when they’re not directly communicating with you live (via live chat and voice, for example). You can customize the type of data that your customers need to provide to you when submitting a support request and you can customize the email notifications they receive from you with your company brand.

## Create brands

Administrators can support large companies with multiple, unique brands or services using a single Zendesk account. A *brand* is a customer-facing identity, represented by a collection of contact points for your customers. This includes support addresses, help centers, and email replies. Brand is also a ticket value on your tickets. By defining brands, you can route tickets to the appropriate agent groups and ensure that proper identification is included in outgoing messages.

![](https://support.zendesk.com/hc/article_attachments/7856435771418)

### Prerequisites

Complete [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow) for your account and define [user groups](#intro_groups) before you start creating brands.

### Dependencies

Support Enterprise includes up to five brands and the Multibrand add-on includes up to 300 brands. Branding is not supported on Support Professional or other plans. It’s important to define branding early in your account setup because you can use branding to route, view, and manage tickets.

### Examples

- A food service company might use different brands to segment their support across different types of customers. For example, they might have a kosher products brand, a vegan brand, and a healthy choice brand.
- An electronics distribution company might use different brands for their consumer customers and their corporate customers.

### Best practices

Most channels have a brand value, so that you can configure specific channels for specific brands. This includes help center, messaging Web Widget, Web Widget (Classic), Chat, Talk, (formerly Twitter), and Facebook.

### Show me how

- [Multibrand resources](https://support.zendesk.com/hc/en-us/articles/4408833921306-Multibrand-resources-Enterprise-)
- [Setting up multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829476378)
- [Managing multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829486362-Managing-multiple-brands-Enterprise-)
- [Multibranding Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/4408893562266-Multibranding-Zendesk-Chat-(Enterprise))

## Add support addresses

In your account, you already have one related email address to submit tickets: [support@myaccount.zendesk.com](mailto:support@myaccount.zendesk.com), but you can provide your end users with alternative email addresses, called *support addresses*. You can add as many support addresses as you need. Support addresses can be either variations of your Zendesk email address or external email addresses.

![](https://support.zendesk.com/hc/article_attachments/7856435773594)

### Prerequisites

Complete [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow) for your account, define [user groups,](#intro_groups) and add [branding](#intro_brands) (if available) before you start creating support addresses.

### Dependencies

This feature is supported on all Zendesk Support plans. If you plan to use Zendesk email addresses, follow the task in this section to set up alternative email addresses.

If you plan to use your own existing, external email address, you can [Connect your existing support email address](https://support.zendesk.com/hc/en-us/articles/4408824587802#topic_tym_w3m_qqb) later. When you set up an external email address, you have an additional step to set up email forwarding. But *do not* set up [email forwarding](https://support.zendesk.com/hc/en-us/articles/4408886828698), yet. You’ll need time to finish setting up your account before you’re ready to receive emails in Zendesk.

### Examples

- [training@mycompany.zendesk.com](mailto:training@mycompany.zendesk.com), [help@mycompany.zendesk.com](mailto:help@mycompany.zendesk.com)
- [hr@mycompany.com](mailto:hr@mycompany.com), [support@mycompany.com](mailto:support@mycompany.com), [webmaster@mycompany.com](mailto:webmaster@mycompany.com), [ap@mycompany.com](mailto:ap@mycompany.com)

### Best practices

Use support addresses to match your ticket issues. Consider the customer experience when configuring support email addresses. Often, the address alone can communicate the type of service provided.

### Show me how

- [Adding support addresses for users to submit tickets](https://support.zendesk.com/hc/en-us/articles/4408842868506-Adding-support-addresses-for-users-to-submit-tickets)

## Set business schedules

Business schedules define working hours and holidays for your agents. If you don't provide 24/7 support to your customers, you can use business schedules to acknowledge agent availability and give customers a better sense of when they can expect a response to their support requests.

![](https://support.zendesk.com/hc/article_attachments/7856435773338)

### Prerequisites

Complete [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow) for your account before you start creating business schedules.

### Dependencies

Setting business schedules early in your launch process is important because you can create views, SLA policies, triggers, and automations based on your business hours and holidays. This feature is available on Support Professional and Enterprise plans.

### Examples

- If your customer sends a Support request during holiday or weekend hours, you can configure an automated email reply that says you’ll get back to them as soon as business hours resume.
- Business hours are taken into account for SLA calculations, so if a ticket arrives late Friday, it doesn’t trigger an SLA policy countdown until Monday morning.
- Support Managers can set up a 24/7 task force to cover high-priority tickets that arrive after hours.

### Best practices

Define your base schedule first, then add holidays as needed. Enterprise accounts can create multiple schedules. [More…](https://support.zendesk.com/hc/en-us/articles/4408882066202#h_452664270201539034481788)

### Show me how

- [Setting your schedule with business hours and holidays](https://support.zendesk.com/hc/en-us/articles/4408842938522-Setting-your-schedule-with-business-hours-and-holidays-Professional-and-Enterprise-)

## Create custom ticket fields

A ticket is the record of the conversation between the agent and the customer. Ticket fields live in the ticket sidebar and allow you to store information, route, and prioritize each ticket. Zendesk includes a default set of fields for your tickets. You can add custom fields as needed.

![](https://support.zendesk.com/hc/article_attachments/7856435763866)

### Prerequisites

Complete [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow) for your account, define [user groups](#intro_groups), [branding](#intro_brands) (if available), and [support addresses](#intro_address) before you start customizing ticket fields.

### Dependencies

Support Enterprise enables you to have multiple ticket forms, so you can tailor your ticket fields to match your ticket type. Other Support plans allow only one ticket form. You can use ticket field values as input to help you manage workflows and views.

### Examples

- A real estate company might include a custom ticket field for property location.
- Finance and Purchasing departments might include a custom ticket field for PO number.

### Best practices

- When you design ticket fields, think about which fields you need the end user to fill out before submitting the ticket and which fields are required for the agent to solve the ticket. Also consider which fields need to be end-user facing and which need to be internal only.
- Think about the data you want to collect in ticket fields and include in reports. For example, you could add an internal field that tracks what types of issues generate the most tickets.
- Encourage agents to complete ticket fields as early as possible so that the ticket appears in the right views and automated workflows work as intended.
- If you add custom fields, it’s almost always best to use drop-down fields when possible. Drop-downs allow you to have nice clean reporting, apply simple business rules effectively, and simplify the experience for your agents and end users.

### Show me how

- The following video gives you an overview of how to create custom ticket fields:

  Creating custom ticket fields [1:41]
- [About ticket fields](../../product-guides/ticket-management/about-ticket-fields.md)
- [Adding custom fields to your tickets](https://support.zendesk.com/hc/en-us/articles/4408883152794)
- [Viewing ticket fields](https://support.zendesk.com/hc/en-us/articles/4408832419738-Managing-ticket-fields)

## Create ticket forms

If your account allows it, you can set up multiple *ticket forms* to create unique workflows for different situations. A ticket form is a set of predefined ticket fields for a specific support request. The ticket form determines the fields and data a ticket contains.

![](https://support.zendesk.com/hc/article_attachments/7856391214618)

### Prerequisites

Complete [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow) for your account, define [user groups,](#intro_groups) and add [branding](#intro_brands) (if available) before you start creating ticket forms.

### Dependencies

Support Professional and Enterprise plan customers can create multiple ticket forms. Customers on the Team plan have access to a single ticket form and cannot create new ticket forms.

### Examples

- A Human Resources department might have a special ticket form for hiring new employees.
- A Purchasing department might have a special ticket form for resolving purchase order issues.

### Best practices

- Make sure your ticket forms have meaningful names. Each form has two names: a form name for agents and a form name for end users.
- Be conservative when adding ticket forms. Having too many forms to choose from may lead to confusion for your end users or agents.
- Pay close attention to the order of ticket fields in your ticket forms. If you have fields specifically for reporting purposes, it may be best to put them at the bottom of the form. Place information that is important for the agent to see near the top of the form, so they don’t need to scroll.

### Show me how

- [Creating ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858-Creating-ticket-forms-to-support-multiple-request-types-Professional-Add-on-and-Enterprise-)
- [Presenting ticket forms to end users](../../product-guides/ticket-customization/presenting-ticket-forms-to-end-users.md)
- [Managing your ticket forms](https://support.zendesk.com/hc/en-us/articles/4408836460698-Managing-your-ticket-forms-)

## Customize email notifications

You can customize the email notifications sent to customers to give your account a recognizable corporate identity. All the email notifications sent from your Zendesk are formatted for both HTML and plain text emails. You can customize the HTML template to match your branding by making a few simple style changes. You can also edit the information in the text versions of your emails.

If you want to edit the text in a specific email notification, you need to edit the trigger that controls the notification. There are already some [default triggers for email notifications](https://support.zendesk.com/hc/en-us/articles/4408828984346) set up in your account.

![](https://support.zendesk.com/hc/article_attachments/7856435771802)

### Prerequisites

Complete the [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528) and [branding](#intro_brands) (if available) tasks for your account. Also, make sure you set up [security](#intro_security) and [user settings](#intro_user_settings) before you start customizing email notifications.

### Dependencies

The email template includes a {{content}} placeholder that displays the email content, which can include ticket comments and user profile photos. The content is defined in the [trigger](#intro_triggers), [automation](#intro_auto), or anything else that sends email from your account. This feature is available on all Zendesk Support plans.

### Examples

You can change the HTML email template to include your company logo, font type, and font colors.

### Best practices

In general, keep your customization as simple as possible. Designing HTML emails is hard because of the way HTML and CSS are rendered in different web browsers and email clients. Also certain types of formatting can trigger spam filters.

### Show me how

- [Customizing templates for your email notifications](https://support.zendesk.com/hc/en-us/articles/4408886168090-Customizing-templates-for-your-email-notifications)
- Getting started with email: [Part 1](https://support.zendesk.com/hc/en-us/articles/4408888639258-Getting-started-with-email-Part-1-How-the-email-channel-works), [Part 2](https://support.zendesk.com/hc/en-us/articles/4408887388058), [Part 3](https://support.zendesk.com/hc/en-us/articles/4408893474202), [Part 4](https://support.zendesk.com/hc/en-us/articles/4408887479834)

## Create ticket tags

Tags are words, or combinations of words, you can use to add more context to tickets. Adding tags to your tickets gives you even more flexibility to track, manage, and interact with your tickets. Ticket tags are useful for running ticket searches and setting ticket views. You can use business rules to add or remove tags.

![](https://support.zendesk.com/hc/article_attachments/7856391215258)

### Prerequisites

Complete the [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow) and [managing people](#h_28581946111542753890528) tasks for your account. Define [ticket fields](#intro_ticket_fields) and [ticket forms](#intro_ticket_forms) (if applicable) before you start creating ticket tags.

### Dependencies

You can't use special characters, such as #, @, or ! in tags. If you try to add tags with these characters, they disappear when the ticket is updated. You can create a tag with more than one word, but the words must be connected with an underscore (\_). Tags are available on all Zendesk Support plans.

### Example

You can tag all requests that are actually sales inquiries with a tag like 'sales' or 'about\_sales'. You can then create a view or a report to track these requests.

### Best practices

- Avoid manually adding tags for common words like 'and' and 'the', these words will generate a high number of tags in your tickets, making automatic tagging a much less useful tool.
- Use consistent naming conventions for tags (for example, capitalization).

### Show me how

- The following video gives you an overview of how to add tags to your tickets:

  Adding tags to tickets [0:54]
- [About tags](../../product-guides/business-rules/about-tags.md)
- [Enabling and disabling ticket tags](https://support.zendesk.com/hc/en-us/articles/4408829424794-Enabling-and-disabling-ticket-tags)
- [Using ticket tags in macros, triggers, and automations](../../product-guides/business-rules/managing-ticket-tags.md#topic_umd_ona_vb)
- [How agents work with ticket tags](../../agent-guide/ticket-basics/working-with-ticket-tags.md)

## Configuring settings and access

Before you add users to your Zendesk account, team members or customers, you should also define access security and authentication for both.

All staff members must sign in to any part of Zendesk and you can define your password security level and also what type of authentication will be used. Zendesk user authentication is enabled by default, but you can also choose third-party authentication using Microsoft or Google, or single-sign on using a number of different services.

With customers (referred to as end users in Zendesk), if you require them to sign in, you have the same password and authentication options. In addition, you also have the option of allowing them to sign in using their X (formerly Twitter) and Facebook accounts. For an overview of your options for end user access, see [Understanding options for end-user access and sign-in](https://support.zendesk.com/hc/en-us/articles/4408887573274).

Because users may have different security requirements, Zendesk gives you the flexibility to allow multiple authentication methods for each type of user. See [Giving users different ways to sign into Zendesk](https://support.zendesk.com/hc/en-us/articles/5380943678106).

## Configure single sign-on

In addition to native Zendesk authentication for users, you can also choose from a variety of single sign-on (SSO) options. With **enterprise** single sign-on, you can bypass Zendesk and let your users can authenticate externally by signing into a corporate server or a third party identity provider, such as OneLogin or Okta. With **social and business account** single sign-on, users can authenticate with their X (formerly Twitter), Facebook, Google, or Microsoft accounts.

![](https://support.zendesk.com/hc/article_attachments/7856435768986)

### Prerequisites

Complete the following tasks before configuring single sign-on: [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528), [branding](#intro_brands), [user access and security](#h_610881057231543353365344)**,** [other products](#h_304821204301543353974002), and [workflows](#h_675961721371543354651109).

### Dependencies

- Enterprise single sign-on is available on all Support plans.
- Social and business single sign-on is available on all Support plans.

### Examples

You can configure social single sign-on, so that your customers can use their Facebook login credentials to access your Zendesk account as an end user.

### Best practices

The advantage to using enterprise single sign-on is that you have complete control over your users, behind your firewall. You authenticate your users once, against your own user authentication system, and then grant them access to many other resources both inside and outside of your firewall.

### Show me how

Instructions vary depending on the type of SSO you want to configure:

- [Single sign-on options in Zendesk](https://support.zendesk.com/hc/en-us/articles/4408883587226-SSO-single-sign-on-options-in-Zendesk)
- [Enabling social and business single sign-on](https://support.zendesk.com/hc/en-us/articles/4408885847962-Enabling-social-and-business-single-sign-on-SSO-)
- [Enabling SAML single sign-on](https://support.zendesk.com/hc/en-us/articles/4408887505690-Enabling-SAML-single-sign-on-Professional-and-Enterprise-)
- [Setting up SAML single sign-on with Okta](https://support.zendesk.com/hc/en-us/articles/4408821683738-Setting-up-SAML-single-sign-on-with-Okta-Professional-and-Enterprise-)
- [Enabling JWT (JSON Web Token) single sign-on](https://support.zendesk.com/hc/en-us/articles/4408845838874-Enabling-JWT-JSON-Web-Token-single-sign-on)
- [Setting up single sign-on using Active Directory with ADFS and SAML](https://support.zendesk.com/hc/en-us/articles/4408834714650)

## Configure security settings

In Zendesk you can apply security settings to ensure your private information is protected and use custom sign-in settings to configure how customers access your Zendesk account. You can set password security levels for agents, admins, and end users. If desired, you can also [configure single sign-on (SSO)](#intro_sso) for a seamless login experience or multifactor authentication for extra security.

![](https://support.zendesk.com/hc/article_attachments/7856391215770)

### Prerequisites

Complete the [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528) and [branding](#intro_brands) (if available) tasks for your account, before you start configuring security settings.

### Dependencies

Security settings are available on all Zendesk Support plans. All plans support single sign-on solutions using JSON web token ([JWT](https://support.zendesk.com/hc/en-us/articles/4408845838874)) and Secure Assertion Markup Language ([SAML](https://support.zendesk.com/hc/en-us/articles/4408887505690)). Security and [user settings](#intro_user_settings) work together. Make sure you have a comprehensive access plan in place that meets your corporate standards.

### Examples

- You can provide your customers with the option of also signing in to Zendesk using their Facebook, Google, Microsoft, and X (formerly Twitter) accounts. Your customers authorize access with these accounts themselves.

### Show me how

- [Security and sign-in resources](https://support.zendesk.com/hc/en-us/articles/4408887485210)
- [Security best practices](https://support.zendesk.com/hc/en-us/articles/4408888782618-Security-best-practices)

## Configure user settings

End users are also sometimes referred to as customers. They're the people who generate support requests from any of your support channels. Depending on your account, they may be customers, other employees, or business partners. You can configure Zendesk settings to control how these users work with Zendesk, how they update their account profiles, and so on. These settings determine how open or restricted your Zendesk account will be.

![](https://support.zendesk.com/hc/article_attachments/7856391216282)

### Prerequisites

Complete the [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528) and [branding](#intro_brands) (if available) tasks for your account. Also, make sure you set up [security](#intro_security) before you start configuring user settings.

### Dependencies

User and [security](#intro_security) settings work together. Make sure you have a comprehensive access plan in place that meets your corporate standards. This feature is available on all Zendesk Support plans.

### Examples

- You can make your Zendesk account available to anyone by selecting the Anybody can submit tickets setting.
- If you are concerned about spam, you can require users to complete CAPTCHA image verification before submitting a ticket.This setting is enabled by default.
- For self-serve situations, you can allow users to sign up online using a registration form.

### Best practices

As part of user settings, you can enable user tagging. This allows you to add tags to a user's profile. These tags are then added to the user's tickets, which you can then use to control your workflow. For example, you can use a tag to escalate a specific user's tickets.

### Show me how

- [Managing end user settings](../../product-guides/account-access/managing-end-user-settings.md)
- [Configuring end user access and sign-in](https://support.zendesk.com/hc/en-us/articles/4408887573274)

## Integrating external apps and services

If you also rely on external apps and services to help you manage parts of your business and your customers, you can integrate those into your Zendesk account.

For example, if you also use Salesforce, JIRA, or Slack, you can manage user data and ticket flows across those applications. You can also add apps from the Zendesk Marketplace to integrate with popular services such as SurveyMonkey.

It’s also possible to notify external targets when a ticket is created or updated. External targets can include cloud-based applications and services as well as email.

## Add marketplace apps

Zendesk includes a Zendesk Marketplace you can use to customize and extend your Support account. In the Marketplace, you'll find hundreds of apps and integrations. The choices include a range of free and paid apps developed by Zendesk, or others.

![](https://support.zendesk.com/hc/article_attachments/7856435765786)

### Prerequisites

Complete the [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528) and [branding](#intro_brands) (if available) tasks for your account. Also, make sure you set up [security](#intro_security) and [user settings](#intro_user_settings) before you start adding marketplace apps.

### Dependencies

- Depending on the app’s function, installed apps can appear in the Apps panel for tickets and for user and organization profiles. They can also appear in the Zendesk top navigation panel or the main (left) navigation panel.
- Apps from the Apps Marketplace are available for all Zendesk Support plans.

### Examples

- With the JIRA app, agents can escalate tickets and link them to JIRA issues, enabling Engineering and Support teams to communicate and solve problems without having to leave their own workspaces.
- Geckoboard makes it easy to display live Zendesk metrics on a TV, so your team can see at a glance what needs nurturing and respond to problems in real time.
- SurveyMonkey helps you organize customers and contacts into lists, and send surveys to your target audience, all in Zendesk.
- The Zendesk Support Five Most Recent app gives you more context around past support requests made by a customer, by displaying the five most recent tickets the customer has submitted.

### Best practices

Install some of the [most popular apps](https://support.zendesk.com/hc/en-us/articles/4408829182234#topic_rsk_qjl_frb) from the Zendesk Marketplace.

### Show me how

- [Using the Zendesk Marketplace](https://support.zendesk.com/hc/en-us/articles/4408824421146-Using-the-Apps-Marketplace)
- [Extending Zendesk with top apps](https://support.zendesk.com/hc/en-us/articles/4408829182234)
- [Efficiency gains through apps](https://support.zendesk.com/hc/en-us/community/posts/360004230608)

## Add 3rd-party integrations

Depending on your work environment, you may wish to integrate your Zendesk account with one or more popular 3rd-party applications such as Salesforce, JIRA, or Slack. Integrations enable you to manage user data and ticket flows across applications, so you can add features and improve business processes.

![](https://support.zendesk.com/hc/article_attachments/7856435765018)

### Prerequisites

Complete the [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people,](#h_28581946111542753890528) [branding](#intro_brands) (if available), and [security](#intro_security) tasks for your account. Also, make sure you understand how you want to transfer and maintain data between Zendesk and other 3rd-party applications before you start adding integrations.

### Dependencies

This feature is available on all Zendesk Support plans. Typically, you need administrator permission in both Support and the 3rd-party application to configure an integration.

### Examples

- With [Slack for Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408833756698), ticket submissions and status changes appear as notifications in specified Slack channels. You can also create new tickets directly from Slack, and comment on tickets from their Slack notifications.
- The [ZIRA field syncing](https://support.zendesk.com/hc/en-us/articles/4408825394458-Using-the-JIRA-field-syncing-feature) feature enables near real time syncing of data between Zendesk Support and JIRA.

### Best practices

To save time, consider integrating applications that agents usually access in other browser windows. If you have an Enterprise account, consider setting up [contextual workspaces](https://support.zendesk.com/hc/en-us/articles/4408833498906--Update-Setting-up-contextual-workspaces-Enterprise-) to present your agents with ticket tools and features based on specific workflows.

### Show me how

- [Extending Zendesk with top integrations](https://support.zendesk.com/hc/en-us/articles/4408832644122)

## Notify external targets

When a ticket is created or updated it can be useful to notify external systems and services (such as apps or email) when this event occurs. Notifying external targets enables your agents to receive updates across a variety of tools to make sure they have the latest information possible.

![](https://support.zendesk.com/hc/article_attachments/7856435766170)

### Prerequisites

Complete the [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people,](#h_28581946111542753890528) [branding](#intro_brands) (if available), and [security](#intro_security) tasks for your account. Also, make sure you have configured the third-party systems and services you plan to use with your Zendesk account.

### Dependencies

You must be familiar with how to configure a webhook to send notifications and how to configure the external system or service to receive notifications. Once you've set up webhooks, you can use them in automations and triggers. This feature is available on all Zendesk Support plans.

### Examples

- Alert your team in [Slack](https://slack.com/) when an urgent ticket has been unattended for more than 48 hours.
- Notify your own back-end service about an important ticket event.

### Best practices

Be conservative when choosing to notify external systems and services. Too many notifications can produce excessive noise and reduce urgency. Focus on what agents really need to know.

### Show me how

- [Creating webhooks](https://support.zendesk.com/hc/en-us/articles/4408839108378)
- [Notifying external targets](https://support.zendesk.com/hc/en-us/articles/4408883282458)

## Defining ticket routing and workflows

With enough of the building blocks in place, you can now set up your workflows and how incoming and updated tickets will be handled. This is where you’ll start using business rules to define automated workflows, set up ticket routing of tickets agents, and create views of your tickets based on various criteria (by channels, by groups, and so on).

For automated routed, you can set up omnichannel routing to assign tickets generated from email, web form, API, messaging conversations, and calls to the agents most available to work on them, based on status and capacity.

Or, if your Zendesk plan includes skills-based routing, you can creates skills and use them in the business rules you create with triggers and automations, for example. If you plan to use skills, you'll create them now and assign them to agents later.

If you’re not already familiar with the routing and workflow tools in Zendesk, here’s a quick summary:

- **Triggers** are event-based business rules you define that run immediately after tickets are created or updated. For example, a trigger can automatically assign a high priority to tickets received from VIP customers.
- **Automations** are time-based business rules that perform an action in your account based on time elapsed. For example, if a ticket hasn’t been answered in a timely manner, an automation can escalate the priority level and notify a manager.
- **Views** dynamically organize tickets based on specific criteria that you define. For example, you can create a view for unassigned tickets received over 24 hrs ago. You can create views that are shared with all agents and agents can create their own personal views of their tickets.
- **Macros** are a predefined set of actions that agents apply to a ticket with one click. You create macros for support requests that can be answered with a single, standard response.
- **Service Level Agreements** (SLAs) are contracts between you and your customers – a promise to respond to and resolve tickets in a certain amount of time. SLAs enable agents working with tickets to see the time remaining before each ticket is overdue, which makes it easy for them to prioritize.

For an overview of your ticket routing options, see [Routing options for incoming tickets](https://support.zendesk.com/hc/en-us/articles/4408831658650-Routing-options-for-incoming-tickets-).

## Configure omnichannel routing

When you have a larger support team, it’s likely that you'll have agents working different shifts to provide support. With omnichannel routing, tickets generated from email, web form, API, messaging conversations, and calls are assigned to the agents most available to work on them.

Agent availability is determined by both their status and their capacity. On Professional and Enterprise plans, tickets are also routed based on priority. Omnichannel routing doesn't consider skills.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocrdiag22.png)

### Prerequisites

Complete the following tasks before enabling and configuring omnichannel routing: [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528), [branding](#intro_brands), and [user access and security](#h_610881057231543353365344).

### Dependencies

Omnichannel routing is available on all plans. However, some features, such as priority-based routing and custom agent statuses, are only available on Professional and Enterprise plans. Additionally, [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) must be activated for your account and you can't be using live chat. You can't use omnichannel routing and skills-based routing at the same time.

### Examples

- You want inexperienced agents to be assigned fewer open tickets at any given time, so you assign them to the "New Hire" capacity rule.
- You want email tickets that come in from the “Very important bank” organization to be assigned the routing tag,  marked as the highest priority, and assigned to the “VIP” group.

### Best practices

A lot of setting up omnichannel routing is going to be investigating, strategizing, and planning. Figuring out what capacity rules you need, what custom unified agent statuses you need, and how the omnichannel routing configuration replaces existing rules. You can use Zendesk's default capacity rules and unified agent statuses as a starting point, and then adjust based on your observations.

### Show me how

- [About omnichannel routing with unified agent status](https://support.zendesk.com/hc/en-us/articles/4409149119514)
- [Enabling and configuring omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4828787357210)
- [Creating capacity rules to balance agent workloads](https://support.zendesk.com/hc/en-us/articles/4776409839770)
- [About unified agent statuses](https://support.zendesk.com/hc/en-us/articles/5133523363226)

## Create skills for routing

When you have a larger support team, it’s impractical for every agent to be knowledgeable about each product area, let alone providing support in all languages. With skills-based routing, tickets get paired with the right agent and get solved faster.

Skills are characteristics you assign to an agent. Skills can be languages, locations, or technical expertise. Once you define a set of skills and assign them to your agents, tickets are routed to the right agents based on their set of skills.

**Important:** At this point, define a set of skills for your Zendesk account, but don’t assign them to agents, yet.

![](https://support.zendesk.com/hc/article_attachments/7856391218202)

### Prerequisites

Complete the following tasks before creating skills for routing: [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528), [branding](#intro_brands), [user access and security](#h_610881057231543353365344)**,** and [other products](#h_304821204301543353974002).

### Dependencies

Skills-based routing is available only on Support Enterprise plans. If you are using another type of Zendesk account, you can skip this task. You can't use omnichannel routing and skills-based routing at the same time, so you'll want to set up one or the other for now.

### Examples

- You might have agents who are good with different types of operating systems that run your products: Windows, UNIX, Mac, Android, and iOS. With skills-based routing, only agents who have UNIX skills would see UNIX-related tickets in their ticket views, and so on.
- If you have experienced agents, you may want to route them escalated tickets or tickets from VIP customers.

### Best practices

A lot of setting up skills-based routing is going to be investigating, strategizing, and planning. Figuring out what skills you need, who has them, and how they can replace existing rules. Make sure you have a solid set of skill definitions, before adding them to Zendesk.

### Show me how

- [Using skills-based routing](https://support.zendesk.com/hc/en-us/articles/4408838892826)
- [Best practices: Setting up skills-based routing](https://support.zendesk.com/hc/en-us/articles/4408883700122)
- [Skills-based routing: Route your way to success](https://www.zendesk.com/blog/skills-based-routing-route-way-success/)

## Create triggers

You can create triggers to intelligently process tickets and save agents time. Triggers are **event-based** business rules you define that run immediately after tickets are created or updated. At their core, triggers are cause and effect statements. **If** a ticket meets a set of conditions, **then** an action is performed.

You can create an unlimited number of triggers based on your business needs. For example, you might have a trigger that automatically replies to customers when they create a new ticket, or you might have a trigger that automatically assigns a high priority to tickets from VIP customers.

![](https://support.zendesk.com/hc/article_attachments/7856435766682)

### Prerequisites

Complete the following tasks before creating triggers: [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528), [branding](#intro_brands), [user access and security](#h_610881057231543353365344)**,** and [other products](#h_304821204301543353974002). Also, if applicable, [skills-based routing](#intro_skills).

### Dependencies

Zendesk Support has a [few default triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346) that you may want to deactivate or alter. If you don’t check through your list of triggers before you go live, you may end up with an inbox full of unwanted notifications. Triggers are available on all Zendesk Support plans.

### Examples

You can use triggers to:

- Notify customers when you’re out-of-office
- Send customer satisfaction score follow-ups
- Route your priority customers to a specialized support group automatically
- Notify agents when a problem ticket has reached a certain number of incidents

### Best practices

- Be as specific as possible when building triggers. One way to do this is to use the “Ticket is” condition to define whether the trigger fires at ticket creation or update.
- Triggers can affect each other, so it’s important to think about the order of triggers to make sure you don’t have an unexpected, cascading effect. See [Understanding when triggers run and fire](https://support.zendesk.com/hc/en-us/articles/4408822236058-About-triggers-and-how-they-work#h_15524764971513292862138).
- If you are not sure your triggers are behaving as expected, you can [view all events of a ticket](https://support.zendesk.com/hc/en-us/articles/4408829602970-Viewing-all-events-of-a-ticket) to see which triggers have affected that ticket and help you troubleshoot any issues.

### Show me how

- The following video gives you an overview of how to add triggers:

  Automating notifications with triggers [2:02]
- [Creating triggers for automatic ticket updates and notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466-Setting-up-automatic-ticket-updates-and-notifications-with-triggers)
- [About triggers and how they work](https://support.zendesk.com/hc/en-us/articles/4408822236058-About-triggers-and-how-they-work)
- [Triggers best practices and recipes reference](https://support.zendesk.com/hc/en-us/articles/4408884068378-Triggers-best-practices-and-recipes-reference)

## Create automations

Triggers are **event-based** business rules that can fire every time a ticket is created or updated. Automations are **time-based** business rules that perform an action in your account based on time elapsed. Like triggers, automations are cause and effect statements. **If** a ticket meets a set of conditions, **then** an action is performed. For example, if a ticket hasn’t been answered in a timely manner, an automation can escalate the priority level and notify a manager.

![](https://support.zendesk.com/hc/article_attachments/7856435767706)

### Prerequisites

Complete the following tasks before creating automations: [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528), [branding](#intro_brands), [user access and security](#h_610881057231543353365344)**,** and [other products](#h_304821204301543353974002). Also, if applicable, [skills-based routing](#intro_skills).

### Dependencies

Automations only run a maximum of once per hour. This makes it difficult to rely on them for high priority updates. Automations are available on all Zendesk Support plans.

### Examples

- By default, Zendesk Support includes an automation that changes solved tickets to closed after four days.
- You can create an automation that automatically sends customers a reminder if they haven’t replied to a request for feedback after a certain amount of time.

### Best practices

- Test automations and triggers on a small scale before making them live.
- When possible, use **greater than/less than** conditions instead of **is** conditions when creating time-based automations. This eliminates the possibility that a ticket is skipped because your automations did not run during the hour the ticket qualifies. For example, **Ticket = Pending, Greater than 24 hours** is better than **Ticket = Pending, Is 24 hours**.
- Consider using a [Bump, Solve automation process](https://support.zendesk.com/hc/en-us/articles/4408832749210-Using-business-rules-to-send-automated-reminders-to-customers) to manage dormant tickets.

### Show me how

- [Creating and managing automations for time-based events](../../product-guides/business-rules/creating-and-managing-automations-for-time-based-events.md)
- [About automations and how they work](../../product-guides/business-rules/about-automations-and-how-they-work.md)
- [Automations vs. Triggers - When to use what](https://support.zendesk.com/hc/en-us/articles/4408832924314-Automations-vs-Triggers-When-To-Use-What)

## Create SLA policies and targets

A Service Level Agreement (SLA) is like a contract between you and your customer where you promise to respond to and resolve tickets in a certain amount of time. Zendesk helps you create SLA policies and targets so you can provide good service on a consistent basis and avoid SLA breaches. SLAs enable agents working with tickets to see the time remaining before each ticket is overdue, which makes it easy for them to prioritize.

![](https://support.zendesk.com/hc/article_attachments/7856435767194)

### Prerequisites

Complete the following tasks before creating SLA policies: [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528), [branding](#intro_brands), [user access and security](#h_610881057231543353365344)**,** and [other products](#h_304821204301543353974002). Also, [skills-based routing](#intro_skills) (if applicable), [triggers](#intro_triggers), and [automations](#intro_auto).

### Dependencies

- SLA policies are available on Support Professional and Enterprise plans.
- SLA policies take your hours of operation into account, based on the [business schedule](#intro_sched) or calendar hours you apply to the ticket.
- You can use the SLA policies you define in triggers, automations, and agent views.

### Examples

- You can set an SLA policy to make sure agents reply to new, high-priority tickets within 1 hour of when the ticket was created.
- You can set an SLA policy to limit the amount of time an agent spends on a ticket, then automatically escalate difficult tickets that take additional time.

### Best practices

Before you establish structured contracts guaranteeing service to specific customers, hone your teams’ skills by establishing service standards for all tickets. This helps ease your support agents into the pressure of meeting service standards. It also increases overall efficiency for all your customers. For example:

- Set a company goal for initial reply or resolution times and apply an SLA to all tickets. The metrics uses are: **First Reply** and **Requester Wait Time**
- Train new agents by setting goals for how long they should spend with each ticket. The metric used is: **Agent Work Time**

### Show me how

- [Defining and using SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866)
- [Viewing and understanding SLA targets](https://support.zendesk.com/hc/en-us/articles/4408832852122-Viewing-and-understanding-SLA-targets-Professional-and-Enterprise-)
- [SLA reporting dashboard overview](https://support.zendesk.com/hc/en-us/articles/4408883829402-SLA-reporting-dashboard-overview-Professional-and-Enterprise-)

## Create shared views for agents

Use shared views to enhance agent productivity. Views dynamically organize tickets based on specific criteria that you define. Using views can help you determine what tickets need attention from you or your team and plan accordingly. Administrators can create views to share among agents and agents can create their own personal views.

![](https://support.zendesk.com/hc/article_attachments/7856391225242)

### Prerequisites

Complete the following tasks before creating shared views for agents: [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528), [branding](#intro_brands), [user access and security](#h_610881057231543353365344)**,** and [other products](#h_304821204301543353974002). Also, [skills-based routing](#intro_skills) (if applicable), [triggers](#intro_triggers), [automations](#intro_auto), and [SLA policies](#intro_SLA).

### Dependencies

There is a pre-defined set of views provided by default for the day-to-day support workflow, which you can modify as needed. You can also create custom views. This feature is available on all Zendesk Support plans.

### Examples

- Create a view for agents to see the tickets assigned to them. Use **Ticket: Assignee is (current user)** as a condition to have the shared view dynamically change based on the agent who’s logged in.
- Create a triage view for new tickets that need to be assigned.
- Create a view for unassigned tickets received over 24 hrs ago.

### Best practices

- When you define shared views, consider the following: Are there certain tickets that take precedence over others? What are their characteristics?

- Agents can get very attached to their views. Before changing the order of shared  
  views, or the columns and order of a view, consult with your agents.

### Show me how

- The following video gives you an overview of how to add views to filter your tickets:

  Adding views to filter tickets [1:23]
- [Using views to manage agent workflow](https://support.zendesk.com/hc/en-us/articles/4408888828570-Using-views-to-manage-ticket-workflow)
- [Views: Best practice](https://support.zendesk.com/hc/en-us/community/posts/203188553)

## Create agent macros

Embed macros within tickets to help agents save time and provide consistent responses. Macros are a pre-defined set of actions that agents apply to a ticket with one click. Create macros for support requests that can be answered with a single, standard response. This saves your agents the time and effort of crafting a separate response to each customer with the same issue.

![](https://support.zendesk.com/hc/article_attachments/7856435768474)

### Prerequisites

Complete the following tasks before creating shared views for agents: [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528), [branding](#intro_brands), [user access and security](#h_610881057231543353365344)**,** and [other products](#h_304821204301543353974002). Also, [skills-based routing](#intro_skills) (if applicable), [triggers](#intro_triggers), [automations](#intro_auto), [SLA policies,](#intro_SLA) and [shared views](#intro_views).

### Dependencies

Macros are available on all Zendesk Support plans. Unlike triggers and automations, agents must manually apply macros to tickets. Macros cannot be set up for specific channels, but you can [restrict macros by brand](https://support.zendesk.com/hc/en-us/articles/1-Restrict-macros-by-brand).

### Examples

- Your team is receiving a high number of password reset inquiries. You want to send such incoming inquiries a reply with a list of self-service instructions as well as links to help center articles.
- Occasionally, your agents receive an angry support email from unhappy customers demanding certain things. Your legal department requests that agents respond to such inquiries with pre-defined, consistent verbiage.

### Best practices

- Instead of creating a complex macro with lots of actions, create multiple macros, each with a small number of actions.
- Use [placeholders](../../product-guides/business-rules/using-placeholders.md) in macros to personalize customer replies and avoid typos.

### Show me how

- The following video gives you an overview of how to use macros to respond to tickets faster:

  Use quick responses with macros [1:40]
- [Using macros to update tickets](../../agent-guide/ticket-automation-and-collaboration/using-macros-to-update-tickets.md)
- [Creating macros for tickets](https://support.zendesk.com/hc/en-us/articles/4408844187034)
- [Organizing and managing your macros](../../agent-guide/ticket-automation-and-collaboration/organizing-and-managing-your-macros.md)

## Adding people

With your organizational structure in place, you can now add agents to your Zendesk account, assign them roles and skills, if needed, add them to the groups and organizations you created, and set their access to specific channels.

You can also add end users to your account if you already have a database of users that you’re already providing support to (for example, you were using some other system to manage users or provide support before you started using Zendesk).

The other method for adding end users to your account is as they come to you for support. For example, via all the channels you provide, your end users contact you for support and a new user account is automatically created. If the end user already has an account in your Zendesk, a new support request will be paired with their existing account. For more information about end-user accounts, see [Understanding how end user accounts are handled across Zendesk Suite](https://support.zendesk.com/hc/en-us/articles/4408881937306-Getting-Started-with-Zendesk-Suite#topic_n35_155_34b).

The steps you took in [Configuring user access security and authentication](#ariaid-title7) to define password security and user authentication are in place and apply to the users you add to your Zendesk account.

## Add agents

Once your basic Zendesk framework is in place, start adding agents (and administrators). You can add agents and administrators manually, through a bulk import of users, or through the Zendesk API. You must be an administrator to add agents and admins. Each new agent and admin you add receives a welcome email and verification link.

![](https://support.zendesk.com/hc/article_attachments/7856435769498)

**Important:** At this point, don’t add or import end users, only agents and administrators.

### Prerequisites

Complete the following tasks before adding agents: [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528), [branding](#intro_brands), [user access and security](#h_610881057231543353365344)**,** [other products](#h_304821204301543353974002), and [workflows](#h_675961721371543354651109). Also, configure [single sign-on](#intro_sso).

### Dependencies

- Make sure you have enough agent subscriptions in your account for each agent or administrator you want to add.
- If you would like to bulk import both users and organizations, you must [bulk import organizations](../../product-guides/end-users-and-organizations/bulk-importing-organizations.md) first.
- On Support Enterprise, you set the agent's groups in the agent's profile, but you do not set agent permissions or ticket access in the agent's profile. Agent permissions and access (except for groups) are determined by the [agent's custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882).
- This feature is available on all Zendesk Support plans.

### Examples

- You can add an agent and assign them to the Legal group for the North American organization with English as their preferred language.
- When you add agents, you can give senior agents permission to all tickets and give junior agents access to tickets in their group only.

### Best practices

Avoid too many cooks in the kitchen by having just a few administrators (approximately 1-5). It’s good to have more than one administrator for redundancy, but even a large account can work well with fewer than five administrators.

### Show me how

- [Adding agents and administrators](https://support.zendesk.com/hc/en-us/articles/4408886939930)
- [Bulk importing users](https://support.zendesk.com/hc/en-us/articles/4408893496218-Bulk-importing-users-and-organizations)
- [Importing users with the Zendesk API](https://developer.zendesk.com/rest_api/docs/core/users)

## Assign agents to skills

When you have a larger support team, it’s impractical for every agent to be knowledgeable about each area of your product, be fluent in all languages, or understand all areas of your business. With skills-based routing, tickets get routed to the agent best equipped to handle the request and tickets get solved faster. First [create skills for routing](https://docs.google.com/document/d/1wq5psmKfRYLKmU4X81SN1DM2E3askQX5XWJK0jyHJCc/edit#heading=h.4zcqd9gbivzm), then assign them to your agents. Tickets are routed to the right agents based on their set of skills.

![](https://support.zendesk.com/hc/article_attachments/7856391220378)

### Prerequisites

Complete the following tasks before adding agents to skills: [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528), [branding](#intro_brands), [user access and security](#h_610881057231543353365344)**,** [other products](#h_304821204301543353974002), and [workflows](#h_675961721371543354651109). Also, configure [single sign-on](#intro_sso) and [add agents](#intro_agents).

### Dependencies

Skills-based routing is available only on Support Enterprise plans. If you are using another type of Support plan, you can skip this task.

### Examples

Skills can be languages, locations, or technical expertise. If you own a website that sells electronics, you might have agents who have television support skills, cell phone support skills, or computer support skills. You might also have agents who specialize in product warranties or returns.

### Best practices

As you assign agents to skills, check your skills coverage. If there’s only one agent who has a certain popular skill or combination of skills, that agent could get overloaded pretty quickly. Identify common skill combinations, and how many agents would have all of them. You might discover that you need to train or even hire agents to get the coverage you need.

### Show me how

- [Assigning agents to skills](https://support.zendesk.com/hc/en-us/articles/4408838892826-Using-skills-based-routing-Enterprise-#topic_w3m_th2_bbb)
- [Best practices: Setting up skills-based routing](https://support.zendesk.com/hc/en-us/articles/4408883700122)

## Train your agents

Get your agents up-to-speed by making sure they have the knowledge they need to use Zendesk. Well-trained agents provide great service and give you an important competitive advantage. Zendesk provides on-demand pre-recorded training, instructor-lead online courses, live classroom events in locations near you, and options for custom training tailored to your needs.

![](https://support.zendesk.com/hc/article_attachments/7856391221018)

### Prerequisites

Complete the following tasks before training your agents: [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528), [branding](#intro_brands), [user access and security](#h_610881057231543353365344)**,** [other products](#h_304821204301543353974002), and [workflows](#h_675961721371543354651109). Also, configure [single sign-o](#intro_sso)n, [add agents](#intro_agents), and [assign agents to skills](#intro_agents_skills).

### Dependencies

This feature is available on all Zendesk Support plans. Zendesk eLearning courses typically recommend access to a Zendesk account to perform class exercises.

### Examples

A good way to train your agents is to give them a quick demo of your site, encourage them to visit [Zendesk.com](https://www.zendesk.com/) to learn more, let them read more about Zendesk in the [Agent Guide](https://support.zendesk.com/hc/en-us/sections/4405298909338-Agent-Guide), or sign them up for [Zendesk eLearning training courses](https://www.zendesk.com/customer-experience/training/#training).

### Best practices

For the best results, make sure your agents have access to a Zendesk account to practice what they’ve learned. If you’re still setting up your corporate account, consider creating a free [Support trial account](https://support.zendesk.com/hc/en-us/articles/4408823799962-How-do-I-create-a-Support-trial-account-) or [sandbox account](https://support.zendesk.com/hc/en-us/articles/4408828617370-Testing-changes-in-your-sandbox-Enterprise-).

### Show me how

- [Introduction to the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930)
- [eLearning: Zendesk Support for Agents](https://training.zendesk.com/series/zendesk-agents/elearning-zendesk-support-agent-essentials)

## Import end users

Rather than add users manually one at a time, you can add many users in a bulk import. Options for importing users include creating a CSV (comma separated values) file that contains the user’s data, importing users via the Zendesk API, or synching users with popular applications like Salesforce.

![](https://support.zendesk.com/hc/article_attachments/7856391221914)

### Prerequisites

Complete the following tasks before importing end users: [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528), [branding](#intro_brands), [user access and security](#h_610881057231543353365344)**,** [other products](#h_304821204301543353974002), and [workflows](#h_675961721371543354651109). Also, configure [single sign-o](#intro_sso)n, [add agents](#intro_agents), [assign agents to skills](#intro_agents_skills), and [train your agents](#intro_agents_train).

### Dependencies

- This feature is available on all Zendesk Support plans. With Support Professional or Enterprise, you can add users to multiple organizations during your bulk import.
- Before synching users and organizations with Salesforce, you must install the [Zendesk for Salesforce app](https://support.zendesk.com/hc/en-us/articles/1)**.**

### Examples

You can assign primary and secondary email addresses and phone numbers to a single user during a bulk import, using the external\_id column.

![](https://support.zendesk.com/hc/article_attachments/7856391221658)

### Best practices

If you create a list of users to import via a CSV file, you'll probably generate this list from some other user management system such as an employee database. Most of these systems have an option for creating a CSV export file. If you need to create the list from scratch you can use a program like Microsoft Excel, Google Sheets, Numbers, or OpenOffice.org Calc.

### Show me how

- [Bulk importing users](https://support.zendesk.com/hc/en-us/articles/4408893496218)
- [Importing users with the Zendesk API](https://developer.zendesk.com/rest_api/docs/support/users)
- [Configuring user and organization synching in Salesforce](https://support.zendesk.com/hc/en-us/articles/1)

## Going live to customers

## Connect an existing email address

You can use your own existing, external email address for support, if you'd like. To receive support requests at an external email address (instead of your Zendesk Support email address), you need to forward email received at your external email address to an email address in your Zendesk account.

If you are not planning to use an external email address, you can skip this step.

![](https://support.zendesk.com/hc/article_attachments/7856435762074)

### Prerequisites

Complete the following tasks before activating email forwarding: [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528), [branding](#intro_brands), [user access and security](#h_610881057231543353365344)**,** [other products](#h_304821204301543353974002), [workflows](#h_675961721371543354651109), and [access](#h_466179673441543355586497).

### Dependencies

This feature is available on all Zendesk Support plans. You configure email forwarding in your own email account, not in Zendesk Support. Exactly how this is done depends on the email provider you're using. A number of email providers allow you to create email forwarding rules so that you can select the incoming mail that should be forwarded to your Zendesk account. Do not set up forwarding until you are ready for all email sent to that address to become tickets in Zendesk.

### Examples

You can set up email forwarding from Microsoft Exchange and Outlook, Google Gmail, Yahoo Mail, and others.

### Best practices

Be sure to set up automatic forwarding, rather than manually forwarding. Manually forwarding an email that originates from an external support address will result in a suspended ticket.

### Show me how

- The following video gives you an overview of how to connect your existing support email:

  Connecting your existing email account [1:39]
- [Connect an external support email address](https://support.zendesk.com/hc/en-us/articles/4408842868506#topic_glt_l3w_jw)

## Set up and embed the web widget

Web Widget (Classic) helps customers discover support content and submit tickets directly from your website or help center. If you have Zendesk Talk or Chat accounts, customers can also use the widget to request a callback or start a live chat. Your customers get immediate help from a single interface.

![](https://support.zendesk.com/hc/article_attachments/7856435771162)

### Prerequisites

Complete the following tasks before setting up and enabling Web Widget (Classic): [workflow planning](https://support.zendesk.com/hc/en-us/articles/4408827906202--New-Planning-your-workflow), [managing people](#h_28581946111542753890528), [branding](#intro_brands), [user access and security](#h_610881057231543353365344)**,** [other products](#h_304821204301543353974002), [workflows](#h_675961721371543354651109), and [access](#h_466179673441543355586497). Also, activate [email forwarding](#intro_email_forward).

### Dependencies

To set up and embed Web Widget (Classic), you must  install Web Widget code on your website or in your help center. Zendesk provides the code you need. Web Widget (Classic) is compatible with most popular [web browsers](https://support.zendesk.com/hc/en-us/articles/4408836216218#topic_rzl_q2n_4r). This feature is available on all Zendesk Support plans.

### Examples

Your customers can submit a ticket from Web Widget (Classic) and receive an email reply to their inquiry. By default, the contact form includes fields for the customer's name and email address, and a description of the problem. You can change the form to include custom ticket fields or ticket forms.

### Best practices

You can customize the appearance of Web Widget (Classic), if you want for further personalization or clarity (for example, changing the text "Help" or using CSS styling), but you need to this with APIs and add some additional code on your site. For more information, see [Advanced customization of Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408832257562).

### Show me how

- The following video gives you an overview of how to add messaging to your website:

  Adding messaging to your website [1:40]
- [Using Web Widget (Classic) to embed customer service in your website](https://support.zendesk.com/hc/en-us/articles/4408836216218)
- [Configuring components in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408838063258)
- [Web Widget (Classic) resources](https://support.zendesk.com/hc/en-us/articles/4408833907354)
- [Using custom ticket fields and ticket forms with Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408838063258)