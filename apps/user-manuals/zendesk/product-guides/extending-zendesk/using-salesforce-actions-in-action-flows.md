# Using Salesforce actions in action flows

Source: https://support.zendesk.com/hc/en-us/articles/9841156736282-Using-Salesforce-actions-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306) to external systems, such as Salesforce,
admins can integrate Zendesk with external systems in automated workflows, improving
collaboration and maintaining a seamless experience across multiple platforms.

Note: The
steps associated with external systems in action flows are referred to collectively
as *external actions*.

This article contains the following topics:

- [Connecting Salesforce to action builder](#topic_urt_zpw_zgc)
- [Using Salesforce actions in action flows](#topic_ej4_1qw_zgc)

## Connecting Salesforce to action builder

Before you can include external actions in your action flows, you must connect the
action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it is a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect action builder to Salesforce**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action
   flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **Salesforce**.
5. Click **Connect**.
6. Use Salesforce to authenticate the account.

   Note: All external actions
   performed by an action flow are attributed to the user who connected the
   external system. Therefore, it is a best practice to use a dedicated
   service account rather than personal credentials when connecting to each
   external system.

After you've connected to the system, you'll see an indicator that it's connected and
details about the instance you're connected to, as well as the actions available for
Salesforce.

## Using Salesforce actions in action flows

The Salesforce action steps can be used to automate many of the actions an agent
might take as they work tickets. For example, you can use the Salesforce actions in
action flows to automatically create new leads or other Salesforce objects when a
user contacts you, automatically add notes to a Salesforce record after a customer
interaction, clean up duplicated data, look up Salesforce contact data prior to
sending a Slack message or creating a Jira issue, automatically convert highly rated
leads identified by AI scoring models, and more.

The Salesforce actions can be used with the following Salesforce objects: leads,
contacts, accounts, opportunities, cases, and campaigns. The following actions are
available for each of these objects:

- [Create record](#topic_xsx_3qw_zgc)
- [Update record](#topic_sk1_kqw_zgc)
- [Delete record](#topic_mqw_mqw_zgc)
- [Find record](#topic_qjt_nqw_zgc)
- [Convert lead to
  opportunity](#topic_wbr_4qw_zgc)

### Creating a record

Use the *Create record* action to add a new record to object (leads,
contacts, accounts, opportunities, cases, and compaigns).

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `name`, `phone`, `description` |
| Output | `id` |

### Updating a record

Use the *Update record* action to change field values for an existing
Salesforce record.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `name`, `phone`, `description` |
| Output | `id` |

## Deleting a record

Use the *Delete record* action to remove a lead or case from Salesforce.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `object_id` |
| Output | none |

## Finding a record

Use the *Find record* action to search for a record based on identifying
information such as an email address or ID.

The inputs and outputs vary by object:

|  | Variables |
| --- | --- |
| Inputs | - **Accounts**: `name`,   `phone`,   `description` - **Leads**: `first_name`,   `last_name`,   `email` - **Contacts**: `first_name`,   `last_name`,   `email` - **Opportunities**: `name` - **Cases**: `case_number` - **Campaigns**: `name` |
| Output | - **Accounts**: `id`,   `name` - **Leads**: Full lead metadata - **Contacts**: Full contact metadata - **Opportunities**: Pipeline metadata - **Cases**: Case metadata - **Campaigns**: `id`,   `name`, `status` |

## Converting a lead to an opportunity

Use the *Convert lead to opportunity* action to transform a lead record into an
opportunity record in Salesforce.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `lead_id`, `account_id` |
| Output | `opportunity_id` |