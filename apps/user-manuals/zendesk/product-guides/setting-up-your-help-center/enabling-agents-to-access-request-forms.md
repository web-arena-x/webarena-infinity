# Enabling agents to access request forms

Source: https://support.zendesk.com/hc/en-us/articles/4408828251930-Enabling-agents-to-access-request-forms

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

By default, agents can't use the help center to submit or comment on tickets. Instead, if an agent clicks a link to a ticket form or clicks a ticket in My activities, they are redirected to the agent interface. However, you can enable agents to submit requests and comment on them through the help center. This flow is typically useful in multi-brand or multi-department use cases where an agent may also be an end user. For example, an agent in one department may use a ticket form to request help from another department.

This article covers the following topics:

- [Enabling access to request forms](#topic_mv1_vjn_gnb)
- [Key information for managing requests](#topic_oj1_wjn_gnb)

## Enabling access to request forms

Streamline your workflow by allowing agents to submit requests and comment on them directly through your help center. You may want to turn on this setting if you've [restricted agent access on tickets where they're the requester](https://support.zendesk.com/hc/en-us/articles/4408822560410#topic_km4_33s_dzb).

**To allow agents to manage requests through the help center**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) in the sidebar.
2. Select **Help center settings**.
3. Select the check box to **Enable agents to manage requests from your help center**.

   ![Agent management requests](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_agents_manage_requests.png)
4. If you have [multiple help centers](https://support.zendesk.com/hc/en-us/articles/4408828794778), use the brand drop down menu in the top left corner to switch between the brands and select which help center to apply the setting to.
5. Click **Update** to save your changes.

## **Key information for managing requests**

The agent interface is a powerful system, but for the average requester, submitting ticket forms and using the help center is a simpler experience. There are also a few limitations to the feature regarding the following:

- Ticket form limitation for light agents

 Light agents can submit tickets through a request form, but the tickets are filled out as internal comments, which means it is not visible in the request portal. Subsequent comments to the tickets are also posted as internal notes and are not visible to light agents.
- Ticket permissions and multi-department awareness

 An agent who submits a request can easily find their ticket when they are logged into Support, because tickets submitted through a request form are accessible in the ticket interface.

 Note: For multi-department (multiple groups), use cases that host, for example HR or other departments that handle sensitive information, remember that the submitting agent has access to all conversations on their ticket, (including internal conversations).
- Limited view for agent interactions with ticket forms and ticket fields

 When an agent attempts to submit a request from the help center, only ticket forms that are [Editable for end users](https://support.zendesk.com/hc/en-us/articles/4408882701338?option=2) appear in the list of available forms that the agent can use. In addition, these ticket forms will only include ticket fields that are **Editable for end users** or **Read-only for end users**. Ticket forms and ticket fields that are **Agent only** don’t appear in the help center. To view these settings, go to **Manage > Ticket Forms** or **Manage >
 Ticket Fields**, and then open a ticket form or ticket field for editing.

 Agents cannot submit a request via the help center or the Web Widget (Classic) if the ticket form includes conditional ticket fields that are required for agents that aren’t also required for end users.
 Submission will fail when the agent attempts to submit the request. This only happens with [required conditional ticket fields](https://support.zendesk.com/hc/en-us/articles/4408846008218#topic_ijq_45k_1jb)
 and not with [other types of required ticket fields](https://support.zendesk.com/hc/en-us/articles/4408846008218#topic_x2s_g5k_1jb).
- Agents can’t mark a ticket as solved

 Agents and Light agents can't change a ticket to “Mark as solved” from the help center, this is done in Support. However you can enable agents to manage requests.
- Agents can’t reopen solved tickets with a comment

 If an end user comments on a ticket that has been solved from the request page, the ticket automatically reopens. However the ticket does not automatically reopen when an agent or light agent submits a comment to a solved ticket (the comment is submitted and added to the thread as a comment).
- Agents can't rate tickets

 Only end users can submit satisfaction ratings to tickets.