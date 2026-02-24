# Updating a ticket when the status of a Jira issue changes (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4408832025114-Updating-a-ticket-when-the-status-of-a-Jira-issue-changes-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Automatically update support tickets when a Jira issue changes status
in a workflow. Configure workflows to add internal notes, change ticket
status, or notify agents when issues progress. Use post functions to
manage updates, and customize notifications with dynamic content placeholders.
This integration enhances communication between support and development
teams, ensuring timely updates on issue resolutions and progress.

Jira can automatically update a Zendesk Support ticket linked to a Jira
issue when the status
of the issue changes in a Jira workflow.

A
[Jira workflow](https://confluence.atlassian.com/adminjiracloud/working-with-workflows-776636540.html)
is the set of statuses and transitions
that an issue goes through during its lifecycle. You can configure a
workflow to
automatically update a linked ticket after a Jira issue moves from one
status to another in
the workflow.

For example, after an engineer changes the Jira workflow status of an
issue from "In
progress" to "Done," Jira can automatically add an internal note to the
linked Zendesk ticket
notifying the agent. The agent can then notify the customer.

Jira can also automatically notify the agent that a developer is now
working on an issue by
adding an internal note to the ticket after the engineer changes the
workflow status of the
issue from "To do" to "In progress."

This article contains the following topics:

- [Understanding how the ticket updates work](#topic_th1_cpp_w4)
- [Configuring a workflow to update tickets](#topic_pjg_hpp_w4)
- [Changing the ticket update settings](#topic_zpg_fqp_w4)
- [Supported comment placeholders](#topic_if4_qmc_zhb)

## Understanding how the ticket updates work

Zendesk tickets are updated from Jira workflows using
*post functions*. Post functions
are a Jira workflow feature used to carry out additional processing
after a workflow
transition is executed. For example, a post function can update the
issue's fields after a
transition.

Post functions are added to workflow transitions, not statuses. They
run after the
transition is complete. Some post functions are essential and can't
be deleted from a
transition or reordered. However, you can insert optional post functions
between them. The
Zendesk integration adds "Notify Zendesk Ticket" to the list of optional
post functions in
Jira.

Note: Post functions can't solve tickets
with empty required fields.

See the
[Atlassian documentation](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/)
to learn more about post
functions.

## Configuring a workflow to update tickets

1. In Jira, click the Settings (cog) icon on the left sidebar, and
   select
   **Issues**.
2. On the Issues page, select **Workflows**
   from the left sidebar.

   ![image](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jiracloud_workflows.png)
3. Locate the workflow used to address issues linked to Zendesk
   tickets, and click
   **Edit** on the right side of the workflow.

   Note: Jira doesn't let you
   edit a live
   workflow. You must edit it in draft mode.
4. In the **Transitions** column, click
   the name of the transition you want to use to
   trigger ticket updates.

   ![image](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jiracloud_workflow_transition.png)
5. Click the **Post Functions** tab, then
   click the **Add post function** link
   on the
   right.

   ![image](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira3_workflow_add_post_fn.png)
6. Select the **Notify Zendesk Support**
   post function from the list and click
   **Add**.
7. Configure the ticket update settings, then click
   **Add**.

   You can change the ticket
   status, add an internal or public comment, add tags, and
   include
   [comment placeholders](#topic_if4_qmc_zhb)
   in the comment
   text.

   ![image](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jiracloud_workflow_config.png)

   **Note**: Deleting
   tags is not supported.
8. Next to the Zendesk Support post function, select the move down
   icon to move it
   underneath the "Add a comment to an issue if one is entered during
   a transition" post
   function.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jiracloud_postfunction.png)
9. Click **Publish Draft** at the top
   of the page, then click **Publish**.

   It's a
   good idea to save a backup copy when prompted.

   **Important**: Your changes
   won't take effect until you publish the draft.

## Changing the ticket update settings

You can change the settings at any time.

1. In Jira, click the Settings (cog) icon on the left panel, and
   select **Issues**.
2. On the Issues page, select **Workflows**
   from the left sidebar.
3. Click **Edit** on the right side of
   the workflow containing the transition you want
   to edit.
4. Select the transition and click the
   **Post Functions** tab.
5. Click the **Edit** (pencil) icon on
   the right side of the post function that updates
   the ticket.

   Note: You can also delete
   the post function by clicking the delete (X)
   icon.
6. Make your changes, then click **Update**.
7. Click **Publish Draft**, then click
   **Publish**.

## **Supported comment placeholders**

You can enter dynamic content placeholders in the comment field of
a post function. For
example, you can enter the following placeholder in the comment field
of a Done transition
function:

```
Issue {{issue.key}} has been resolved.
```

When the issue 'QA-4' transitions to the Done state, all linked tickets
will be updated
with the following comment:

```
Issue QA-4 has been resolved.
```

For more information, see
[Using placeholders](https://support.zendesk.com/hc/en-us/articles/4408887218330).

The Zendesk JIRA integration supports issue-specific, transition-specific,
and
user-specific placeholders. The placeholders are listed in the tables
below. If placeholders
for user profile fields aren't rendering, check your
[profile visibility settings](https://id.atlassian.com/manage-profile/profile-and-visibility)
in Jira because many fields have
restricted visibility by default.

Note: This integration does not
support custom field placeholders.

Table 1. **Issue-specific placeholders**

| Placeholder | Description |
| --- | --- |
| issue.id | Internal id number of the issue |
| issue.key | Issue key. Example: QA-4 |
| issue.fields.summary | Issue summary |
| issue.fields.description | Issue description |
| issue.fields.issuetype.name | Issue type |
| issue.fields.issuetype.description | Issue type description |
| issue.fields.creator.name | User name of the person who created the issue |
| issue.fields.creator.emailAddress | Email address of the person who created the issue |
| issue.fields.creator.displayName | Display name of the person who created the issue |
| issue.fields.creator.timeZone | Time zone of the creator |
| issue.fields.reporter.name | Name of the person who reported the issue |
| issue.fields.reporter.emailAddress | Email address of the person who reported the issue |
| issue.fields.reporter.displayName | Display name of the person who reported the issue |
| issue.fields.reporter.timeZone | Time zone of the reporter |
| issue.fields.assignee.name | User name of the person assigned to the issue |
| issue.fields.assignee.emailAddress | Email address of the person assigned to the issue |
| issue.fields.assignee.displayName | Display name of the person assigned to the issue |
| issue.fields.assignee.timeZone | Time zone of the assignee |
| issue.fields.user.name | Username of the user |
| issue.fields.user.emailAddress | Email address of the user |
| issue.fields.user.displayName | Display name of the user |
| issue.fields.user.timeZone | Time zone of the user |
| issue.fields.created | Date and time the issue was created |
| issue.fields.updated | Date and time the issue was updated |
| issue.fields.priority.name | Issue priority name |
| issue.fields.project.name | Issue project name |
| issue.fields.project.key | Issue project key. For example: QA |
| issue.fields.lastViewed | Date and time the issue was last viewed |
| issue.fields.fixVersions.name | Name of the fix version/s\* |
| issue.fields.fixVersions.description | Description of the fix version/s\* |
| issue.fields.fixVersions.releaseDate | Release date of the fix version/s\* |
| issue.fields.versions.name | Name of the affected version/s\* |
| issue.fields.versions.description | Description of the affected version/s\* |
| issue.fields.versions.releaseDate | Release date of the affected version/s\* |
| issue.fields.components.name | Name of the component/s\* |
| issue.fields.components.description | Description of the component/s\* |
| issue.fields.duedate | Due date |
| issue.fields.timespent | Time spent |
| issue.fields.timeoriginalestimate | The original estimated time required to resolve the issue |
| issue.fields.resolution.name | A record of the issue's resolution |
| issue.fields.resolution.description | A complete description of the resolution |
| issue.fields.resolutiondate | Date of issue resolution |
| issue.fields.watches.watchcount | The number of people watching the issue |
| issue.fields.labels | The label the issue relates to |
| issue.fields.environment | The hardware or software environment the issue relates to |
| issue.fields.votes.votes | The number of votes an issue has |
| issue.last\_comment | Last comment on the issue |

\*A comma-separated list if multiple items are selected.

Table 2. Transition-specific placeholders

| Placeholder | Description |
| --- | --- |
| transition.to\_status | The status an issue has transitioned to. For example: Done |
| transition.from\_status | The status an issue has transitioned from. For example: In Progress |
| transition.transitionName | The transition name that occurred |
| transition.workflowName | The workflow name |

Table 3. User-specific placeholders

| Placeholder | Description |
| --- | --- |
| user.key | Username of the person who caused the transition. This applies for Jira Server users only. |
| user.displayName | The user's display name. This applies to Jira Cloud users only. |