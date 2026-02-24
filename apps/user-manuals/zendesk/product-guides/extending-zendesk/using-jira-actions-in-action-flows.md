# Using Jira actions in action flows

Source: https://support.zendesk.com/hc/en-us/articles/9836794562842-Using-Jira-actions-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306) to external systems, such as Jira, admins can integrate Zendesk with external systems in automated workflows, improving collaboration and maintaining a seamless experience across multiple platforms.

Note: The steps associated with external systems in action flows are referred to collectively as *external actions*.

This article contains the following topics:

- [Connecting Jira to action builder](#topic_czp_zx4_zgc)
- [Using Jira actions in action flows](#topic_rhf_1y4_zgc)

## Connecting Jira to action builder

Before you can include external actions in your action flows, you must connect the action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it is a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect Jira to action builder**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **Jira**.
5. Click **Connect**.
6. Follow Atlassian's prompts to authenticate and complete the connection.

   Note: All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it is a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.

After you've connected to the system, you'll see an indicator that it's connected and details about the instance you're connected to, as well as the actions available for Jira.

## Using Jira actions in action flows

Jira action steps can be used to automatically create and update Jira issues based on tickets. For example, you could automatically create Jira issues for bugs reported in Zendesk tickets, check a Jira issue's status before closing a Zendesk ticket, update Jira issue assignment based on ticket assignment, or move a Jira issue from one status to another when a ticket is being worked.

The following Jira actions are available:

- [Create issue](#topic_fjx_sy4_zgc)
- [Get issue](#topic_fb5_gz4_zgc)
- [Edit issue](#topic_yr1_mz4_zgc)
- [Transition issue](#topic_orm_rz4_zgc)

### Creating a Jira issue

Use the *Create issue* action to create a new issue in the connected Jira project.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `project_id`, `summary`, `issue_type_id`, `assignee_id`, `priority_id`, `description`, `labels` |
| Output | `id`, `key`, `self` |

### Getting a Jira issue

Use the *Get issue* action to retrieve details about a specific Jira issue.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `issue_id` or `issue_key` |
| Output | Full issue metadata |

### Editing a Jira issue

Use the *Edit issue* action to update a Jira issue's details, incuding the summary, assignee, and description.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `project_id`, `summary`, `issue_type_id`, `assignee_id`, `priority_id`, `description`, `labels` |
| Output | `id`, `key`, `self` |

### Updating a Jira issue's status

Use the *Transition issue* action to change a Jira issue's workflow status.
For example, from "To do" to "In progress" when work begins.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `issue_id` or `issue_key`, `transition_id` |
| Output | none |