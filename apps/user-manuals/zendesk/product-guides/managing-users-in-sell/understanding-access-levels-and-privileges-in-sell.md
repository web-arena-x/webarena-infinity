# Understanding access levels and privileges in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408821340826-Understanding-access-levels-and-privileges-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

With all plans, you can choose between either full access or limited access levels in Sell.

With Professional and Enterprise , if you create a [user hierarchy](https://support.zendesk.com/hc/en-us/articles/4408824266522), you can choose to specify more granular access or you can create [custom roles](https://support.zendesk.com/hc/en-us/articles/4408825410458) to define permissions that can be applied to multiple users.

You need admin rights to work with users. See [creating a user](https://support.zendesk.com/hc/en-us/articles/4408823441050) and [editing user permissions](https://support.zendesk.com/hc/en-us/articles/4408824037658) to set up your users.

This article contains the following topics:

- [Default access levels in Sell](#topic_yv5_fb5_pjb__section_txz_tf5_pjb)
- [Granting administrator rights](#topic_yv5_fb5_pjb__section_k2m_hb5_pjb)
- [Viewing data based on permissions](#topic_yv5_fb5_pjb__section_klb_3b5_pjb)
- [Performing actions based on user permissions](#topic_yv5_fb5_pjb__section_hjd_2yz_pjb)
- [Filtering reports based on user permissions](#topic_yv5_fb5_pjb__section_bry_pgv_pjb)

## Default access levels in Sell

The default access levels in Sell differ depending on the plan that you are subscribed to.

**Default access levels (Team and Growth)**

The default access levels for the Team and Growth plans are **Full access** and **Limited access**.

- **Full access**: view, update, delete, and convert any lead, contact, or deal in the account. You can also manage goals, tasks, appointments, and share documents.
- **Limited access**: view, update, delete, and convert their own leads, contacts, and deals in the account. An administrator can additionally extend their access to contacts and prospects.

**Default access levels (Professional and Enterprise)**

With the Professional and Enterprise plans, you can also enable advanced permissions in Sell. Advanced permissions let you set up custom user roles that you can apply to multiple users in your user hierarchy, see [setting up roles in Sell](https://support.getbase.com/hc/en-us/articles/360035692131).

## Granting administrator rights

Any Sell user, whether they have full or limited access, can be granted administrator privileges. Administrators do not have access to all user data. Administrator privileges relate to managing the account, and include the following areas (as listed in [Settings](https://app.futuresimple.com/settings/)):

- Account information: account name, time zone, account currency, account cancellation
- Subscription: upgrading and downgrading account subscription plan
- Leads, contacts, and deals: adding, editing or deleting custom fields
- Sales goals: resolution period
- Task automation rules
- Integrations
- Voice: call scripts and billing
- Client space setup
- Lead capture form setup and publishing
- Exporting data (admin feature by default, but can be granted to all users)

Only current administrators can grant other Sell users administrative privileges. The data privileges of an administrator are defined by their access level.

## Viewing data based on permissions

Leads, contacts, and deals are the three categories of records that follow the user permissions set for your organization. Other types of data that are related to leads, contacts, or deals also inherit the permissions of a related object. These related types of data include:

- Notes
- Documents
- Tasks
- Appointments
- Call logs and summaries
- Visit summaries

For example, if a user has access to a specific contact, they can also see the call logs and contact notes for that contact.

## Performing actions based on user permissions

Depending on their permissions, users can perform the following actions on data:

- View: the user has read-only access, (this is the most restrictive permission type and a user can't comment on or amend a record in any way)
- Add: the user can enter a new lead, contact, or deal to Sell
- Update: the user can perform a large range of actions, including the ability to:
  - Edit fields
  - Move deals through stages, move leads to statuses
  - Add notes, add log activities, set up appointments
  - Communicate, (send emails, make calls, send text messages)
  - Add and remove documents, add and remove products
- Reassign ownership: the user can, for example, move a deal from one owner to another. They can also convert leads to contacts.
- Delete: the user has delete access. Use caution when granting delete access. Deals, for example, can't be recovered if they have been deleted.

Users only see the options that relate to their permissions. For example, if a user is not allowed to add leads, they won't see the add button or import option for leads.

If a user attempts bulk actions on records that they don't have the correct permissions for, the action is blocked for the invalid records. For example, a user can view any lead their manager can, but can reassign only their own and reportee leads. If they attempt to reassign 20 leads, and only 10 belong to the user themself or to another user that is a reportee, only the 10 valid leads are reassigned.

A user can communicate with their own and any reportees' leads and contacts by default. If a user needed to perform the following actions for a lead or contact outside of this group, they would need the permission set to update any lead or contact they can view:

- Compose and send an email
- Reply to an email
- Make a call
- Compose and send a text message
- Reply to a text message

## Filtering reports based on user permissions

Reports are available to every user on your account, regardless of their permissions configuration or access level. Account users can view reports for only the data that they have access to. For example, a user who only has access to view their own deals, sees only their own deal values in the Total Sales report.

For Professional and Enterprise plans, each report in your account can be filtered according to the groups and teams that you have access to.

Team, group, and tag filters can be combined to produce highly segmented and granular reports.