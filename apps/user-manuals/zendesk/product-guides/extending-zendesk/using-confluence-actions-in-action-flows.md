# Using Confluence actions in action flows

Source: https://support.zendesk.com/hc/en-us/articles/9836432286490-Using-Confluence-actions-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306) to external systems, such as Confluence,
admins can integrate Zendesk with external systems in automated workflows, improving
collaboration and maintaining a seamless experience across multiple platforms.

Note: The
steps associated with external systems in action flows are referred to collectively
as *external actions*.

This article contains the following topics:

- [Connecting Confluence to action builder](#topic_gg3_dj4_zgc)
- [Using Confluence actions in action flows](#topic_vvf_fj4_zgc)
- [Recipe: Escalate Zendesk tickets by creating incident reports in Confluence](#topic_et5_v12_fhc)

## Connecting Confluence to action builder

Before you can include external actions in your action flows, you must connect the
action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it is a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect action builder to Confluence**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action
   flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **Confluence**.
5. Click **Connect**.
6. Follow Atlassian's prompts to authenticate and complete the
   connection.

   Note: All external actions performed by an action flow are
   attributed to the user who connected the external system. Therefore, it
   is a best practice to use a dedicated service account rather than
   personal credentials when connecting to each external
   system.

After you've connected to the system, you'll see an indicator that it's connected and
details about the instance you're connected to, as well as the actions available for
Confluence.

## Using Confluence actions in action flows

Confluence action steps can be used to create, update, and add comments to Confluence
pages.

The following Confluence actions are available:

- [Create page](#topic_zwf_gl4_zgc)
- [Update page](#topic_hfg_ml4_zgc)
- [Create footer
  comment](#topic_kxk_tl4_zgc)
- [Search for a page](#topic_zkx_zl4_zgc)

### Creating a Confluence page

Use the *Create page* action to create a new Confluence page with the
specified title and text-based content.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `space_id`, `title`, `value` |
| Output | Full metadata |

### Updating an existing Confluence page

Use the *Update page* action to update an existing Confluence page with
specified text-based changes.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `space_id`, `title`, `value` |
| Output | Full metadata |

### Creating a footer comment on an existing Confluence page

Use the *Create footer comment* action to add a comment to an existing
Confluence page.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `page_id`, `value` |
| Output | `id`, `status` |

### Searching for a Confluence page

Use the *Search for a page* action to search for a Confluence page by its
title.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `title` |
| Output | `id`, `title` |

## Recipe: Escalate Zendesk tickets by creating incident reports in Confluence

The following example action flow automatically creates an incident report in
Confluence when a Zendesk ticket is determined to be an incident. Automating these
actions ensures immediate visibility for engineering, consistent documentation of
incidents, and clean handoffs between teams working together to resolve the
incident.

Such an action flow might consist of the following steps:

1. Add an action flow trigger with the following details:
   1. Click **Add trigger**.
   2. In the step sidebar, under **Zendesk**, click
      **Tickets**.
   3. Click **Properties** and select **Ticket type changed**.
   4. Click **Add condition**.
   5. Under **Variable**, select **Ticket type changed** and
      **Type**.
   6. Set the **Operator** to **Is**.
   7. Under **Value**, enter **Incident**.
2. Add a step to look up ticket details:
   1. In the action builder, beneath the action flow trigger, click the
      **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up
      ticket**.
   3. Under **Ticket ID**, click into the field and then click
      **Select a variable instead**.
   4. In the variable menu, select **Ticket assignment changed** as the
      step that output the variable you want to use, and then select
      **Ticket ID**.
3. Add a step to look up user details about the ticket assignee:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up
      user**.
   3. Under **User ID type**, select **Zendesk user ID**.
   4. For **User ID**, click **Add variable**.
   5. In the variable menu, select **Look up ticket** as the step that
      outputs the variable you want to use, and then select **Requester
      ID**.
4. Add a step to lookup details about the ticket requester's organization:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up
      organization**.
   3. Under **Organization ID type**, select **Zendesk organization
      ID**.
   4. For **Organization ID**, click **Add variable**.
   5. In the variable menu, select **Look up user** as the step that
      outputs the variable you want to use, and then select
      **Organization ID**.
5. Add a step that creates a Confluence page based on the information you
   collected for the ticket, requester, and organization:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **External actions**, click
      **Confluence** and then select **Create page**.
   3. Under **Space**, select the appropriate space from the connected
      account in which to create the page.
   4. Under **Title**, enter **Incident report:**  and then click
      **add variable**.
   5. In the variable menu, select **Look up ticket** as the step that
      outputs the variable you want to use, and then select **Ticket
      ID**.
   6. Under **Content**, enter the templated content you want to
      capture for all incidents. Include relevant ticket and user
      information as variables from the Look up ticket, Look up user, and
      Look up organization steps, respectively, to streamline the incident
      resolution. In the following example, all variables are
      italicized:

      ```
      An incident was identified via the following Zendesk ticket: Ticket ID.

      **Incident owner**
      The following team member is serving as the incident owner: Ticket Assignee. They should be included in all decisions.

      **Summary**
      - Incident: Ticket Description
      - Status: Ticket Status ID
      - Reported by: Requester Name (Requester ID)
      - Reporter's Organization: Requester's Organization Name (Organization ID)
      - Reported at: Ticket Created at
      ```
6. Click **Save**.
7. Click **Test** to [test the action flow](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_uyj_qsw_3fc).
8. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Activate** to begin using the
   action flow to automatically create incident reports in Confluence.