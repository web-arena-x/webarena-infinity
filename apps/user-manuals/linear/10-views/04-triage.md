# Triage

Manage issues created by other teams and customer support integrations.

![Triage](https://webassets.linear.app/images/ornj730p/production/30183e73c9ef009bb8cb14adbe97d9f34a5b9a69-2352x1632.png?q=95&auto=format&dpr=2)

## Overview

Triage is a special inbox for your team. When an issue is created by integration or by a workspace member not belonging to your specific Linear team, it will appear here. Triage offers a opportunity to review, update, and prioritize issues before they are added to your team's workflow. Consider using Triage responsibility to set a rotating schedule of ownership for monitoring incoming issues.

![Watch on YouTube](https://www.youtube.com/watch?v=PvHL2QZ3GFM)

## Configure

Go to your _Team Settings > Triage_. Once you toggle it on, Triage will appear under the team name in the sidebar.

## Basics

Navigate to Triage with `G` then `T`. If you are in another team's views, use `O` then `T` to open the team you want to view first.

### Create issues

New issues will default to Triage status if they are created through an integration (e.g. Slack, Sentry), created when inside of the Triage view, or if members outside of your specific team create the issue.

> [!NOTE]
> Setting default templates in Team Settings > Templates can override the triage status.

### Take actions

Open the issue to review it and take one of the following issue actions: _accept_ with `1`_, mark as duplicate_ with `2`_, decline_ with `3`_, or snooze_ with `H`.

Accepting an issue will offer the option to leave a comment and then move the issue to your team's default status.

To ask for more information from the user who created the issue, comment on the issue and keep it in Triage or snooze it until you're ready to take an action.

**Marking as duplicate** will offer a choice of which existing issue to merge the duplicate into. Taking this action will also move the new issue's attachments to the canonical issue, including [customer requests](https://linear.app/docs/customer-requests) and attachments. Once selected, the new issue is updated to a _Canceled_ status type. The shortcut `MM` also triggers the mark as duplicate action.

**Declining** will update the issue to a _Canceled_ status type and present the option of adding a comment with an explanation.

**Snoozing** will hide the issue from the triage queue to return at a time of your choosing, or when there's new activity on that issue: whichever comes first. See snoozed Triage issues by toggling the preference in View Options. Snoozing hides the issue in Triage from other users by default as well.

### Triage Intelligence

On Business and Enterprise plans, our Triage Intelligence feature allows LLMs to analyze every new issue in triage against your existing issues to suggest properties like assignee and label, and pro-actively surface likely related issues or duplicates based on the analysis of the issue's content against historical behavior in your workspace. Learn more about Triage Intelligence [here](https://linear.app/docs/triage-intelligence).

### Triage rules

> [!NOTE]
> Triage rules functionality is supported on Business and Enterprise plans.

On Business/Enterprise plans, configure custom rules to take automated actions on issues when they enter Triage. Triggered on filterable properties, triage rules can update an issue's team, status, assignee, label, project and priority. 

Once configured, rules are executed in order from the top down. When moving issues to another team's Triage via rule, the new team's rules are applied to the issue as well. If rules conflict, this is surfaced in the interface.

Consider combining triage routing with [custom Asks fields](https://linear.app/docs/linear-asks#creating-additional-fields) to create a scalable system to intake issues from Slack. Users fill out what they know and automations send the issue to the right team or assignee.

To create a rule that triggers on when any condition in a set is true (like Customer name includes any of 3 customers,) hold `Shift` while selecting each customer name in the filter menu.

![two triage rules; if any of three customers set priority to high, and if labeled iOS move to team Mobile](https://webassets.linear.app/images/ornj730p/production/f41716bdc477cee4fadc5fabeff3bf47c09f27bc-1832x934.png?q=95&auto=format&dpr=2)

### Triage responsibility

> [!NOTE]
> Triage responsibility is available on our [Business](https://linear.app/pricing) and [Enterprise](https://linear.app/pricing) plans.

Enable triage responsibility to define who handles incoming issues. You can select specific members of your workspace to receive notifications of new issues or be automatically assigned to them. Configure triage responsibility in your team's Triage settings.

![Triage view of a Linear workspace](https://webassets.linear.app/images/ornj730p/production/c40aa85cbcf9b1ae058bd94c2fb3dd7d2017270a-1784x515.png?q=95&auto=format&dpr=2)

Once triage responsibility is set, optionally connect your PagerDuty, OpsGenie, Rootly, or Incident.io schedules to automate the rotation of first responders. If you use another provider, we have opened up that [API](https://studio.apollographql.com/public/Linear-API/variant/current/schema/reference/objects/Mutation?query=timeScheduleUpsertExternal#timeScheduleUpsertExternal) so you can build a custom schedule.

Members of your team will be able to easily see who is currently assigned to monitor triage when creating issues.

## Integrations

### Asks

Use Triage to seamlessly intake issues reported from non-Linear users through [Asks](https://linear.app/docs/linear-asks).

### Support integrations

Get more out of Triage by connecting it to our support integrations—Intercom, Front, and Zendesk—or Slack. Using these integrations, your support team can create new Linear issues or link customer reports to existing issues directly from their customer support tool.

## FAQ

<details>
<summary>Can I require priority to be set before an issue leaves Triage?</summary>
Yes. Configure this behavior under Team Settings > Triage.
</details>

<details>
<summary>Why are issues in Triage not showing up in my views?</summary>
By default, we exclude triage issues from all views since triage is considered to be outside the normal workflow. To include them in a custom view, you need to explicitly include them by adding a status filter where "Triage" is included.
</details>
