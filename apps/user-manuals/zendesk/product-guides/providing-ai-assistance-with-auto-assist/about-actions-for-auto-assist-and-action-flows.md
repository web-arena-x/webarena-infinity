# About actions for auto assist and action flows

Source: https://support.zendesk.com/hc/en-us/articles/9174548349978-About-actions-for-auto-assist-and-action-flows

---

Actions are available for use byauto assist, which is part ofthe Copilot add-on, and byaction flows, which perform a pre-defined series of automated actions. There are two types of actions: standard and custom actions.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

Verified AI summary ◀▼

Explore actions for auto assist and action flows to streamline customer support tasks. Use standard and custom actions to automate processes, like updating ticket fields or integrating with external systems via APIs. Auto assist suggests actions, which you can approve to save time. Remember, actions don't apply to AI agent tickets. Customize actions to fit your workflow and enhance efficiency.

Actions are available for use by [auto assist](https://support.zendesk.com/hc/en-us/articles/7051314237466), which is part of [the Copilot add-on](https://support.zendesk.com/hc/en-us/articles/5524125586330), and by [action flows](https://support.zendesk.com/hc/en-us/articles/8855513857306), which perform a pre-defined series of automated actions. There are two types of actions: standard and custom actions.

This article describes what actions are and how they are used in Zendesk.

This article includes the following topics:

- [Understanding actions for automated tasks](#topic_a12_s5n_xcc)
- [Understanding standard actions for auto assist](#topic_ubt_qyr_k2c)
- [Understanding custom actions](#topic_a5n_ryr_k2c)

Related articles:

- [Creating actions for auto assist and action flows](https://support.zendesk.com/hc/en-us/articles/8013439366810)
- [Managing actions for auto assist and action flows](https://support.zendesk.com/hc/en-us/articles/9156980948250)

## Understanding actions for automated tasks

You must have the [Copilot add-on](https://support.zendesk.com/hc/en-us/articles/5524125586330) to use auto assist.

Auto assist suggests relevant actions and action flows to your agents to help them solve customer requests. When auto assist suggests an action, the agent can approve it and the system carries out the action automatically, saving the agent time.
Similarly, when auto assist suggests an action flow, the agent can approve it and the system carries out all of the [steps](https://support.zendesk.com/hc/en-us/articles/8855601898266#topic_ybr_z3g_t2c) automatically.

Actions and action flows can be linked directly in procedures to ensure that auto assist performs the correct action for a user's request. Additionally, you can include custom actions as steps in action flows.

There are two types of actions: [standard actions for auto assist](#topic_ubt_qyr_k2c) that require no configuration from you and [custom external actions](#topic_a5n_ryr_k2c)
that you configure based on an API.

Standard actions don't appear on the Actions page in Admin Center and can't be modified.

### Auto assist action limits

Auto assist can suggest up to four actions at a time in most cases. Reply suggestions and agent instructions count towards this limit.

For example, if auto assist suggests a reply, agent instructions, and two actions, such as updating the ticket status and the ticket priority. In this case, the action limit will be met.

The exception to this limitation is if auto assist suggests a macro as an action.
When this happens, then the suggestion can include only agent instructions in addition to the macro. Auto assist can't suggest a macro and any other type of action at the same time.

Keep these limitations in mind when [writing procedures](https://support.zendesk.com/hc/en-us/articles/7924047699738#topic_vs3_j44_xcc), especially when including steps that combine multiple actions.

## Understanding standard actions for auto assist

Auto assist includes the following standard actions:

- Update ticket status to any standard or custom status
- Update the priority, type, and tags ticket fields
- Update checkbox, date, decimal, dropdown, number, or regex custom ticket fields
- Leverage a Shopify integration to look up a Shopify order, cancel and refund an entire Shopify order, or refund selected items from a Shopify order. (See [Workflow recipe: Canceling and refunding a Shopify order with auto assist](https://support.zendesk.com/hc/en-us/articles/7719560079642).)

You can also update the ticket assignee and group, but these capabilities don't appear in the standard actions list. To update the ticket assignee or group in a procedure, enter an instruction such as, "Set the ticket assignee to [Agent name]" or "Change the ticket group to [Group Name]." Auto assist recognizes the instruction and applies its built-in logic automatically when the step is triggered.

When you insert a standard action in a procedure, you must specify the value you want auto assist to update the ticket or field to. The reference to value is entered directly after the standard action in the procedure.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_procedure_action_add_value.png)

You can reference the value by entering it in plain text or by using a value from the conversation, another field, or another action.

For example, say you insert the action `Change field 'Language'`. You could enter any of the following to specify a value:

- `Change field 'Language'` to Spanish
- `Change field 'Language'` to the value from "Product language" field
- `Change field 'Language'` to the language used by the customer
- `Change field 'Language'` to language returned by Action or Action flow

If you insert a standard action in a procedure that updates a [conditional ticket field](https://support.zendesk.com/hc/en-us/articles/4408834799770#topic_ydk_2b1_phb), then you must position the action to update the conditional field before the action that updates its parent ticket field. This is because actions are executed sequentially and required fields must be set first for the subsequent actions to succeed.

For example, if the parent field in a conditional ticket field is named "Product" and is configured to display the conditional field "Model" when the value "Laptop" is selected. In this case, you should position the action to update the "Model" field before the action to update the "Product" field.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_ctf_action_position_procedure.png)

## Understanding custom actions

Custom actions allow you to update data outside of Zendesk using an API you define.
These actions allow you to query and modify your internal business systems or perform a third-party action. The more actions you configure, the more options are available to auto assist when it generates suggestions for agents.

### Using Zendesk APIs with custom actions

Because you can create custom external actions using any API, it's possible to create an external action that points to a [Zendesk API](https://developer.zendesk.com/api-reference/). If you do this, however, there are some considerations to keep in mind:

- These API requests count against your overall Zendesk API rate limits. See [Managing API usage in your Zendesk account](https://support.zendesk.com/hc/en-us/articles/4408836402074).
- Custom actions support bursts of up to 280 action executions, and can then continue at a rate of 6 executions per second during a recharge period. This limit applies to custom action executions in action flows and auto assist cumulatively.
- As part of action setup, you’ll [create a connection](https://support.zendesk.com/hc/en-us/articles/5040378297626) to authorize the request, which uses a Zendesk API token or OAuth token. This connection might have greater access privileges than your agents and end users, so you’ll need to be cautious that you don’t accidentally expose information they shouldn’t see.
- In the future, you’ll need to migrate your Zendesk API actions to out-of-the-box Zendesk actions if and when equivalent actions become available.
- Be mindful of how changes made by these API requests may interact with other parts of your Zendesk configuration, such as triggers, automations, and apps.

### About inputs for custom actions

An input for a custom action is the information that the action uses in order to run.

You can create inputs for actions that reference the following types of information:

- **Generated information, based on the conversation between the end user and the agent**

 Auto assist uses generative AI to extract information from the conversation and passes it to an action or action flow as an input.

 For example, say you have an input named "order\_id" with the description “the customer’s order number, which is typically an integer of 9 or 10 digits”. If an agent asks, "Can I please have your order number?" and the end user replies, "Sure, it's 987654321", the action will pass this information to the "order\_id" input.
- **Ticket fields**

 Custom ticket fields, and [certain standard ticket fields listed below](#topic_n3p_gzr_k2c__ul_hgw_czr_k2c), can be used as inputs. When using a ticket field as an input, enter a name and description that's detailed enough that auto assist understands which ticket field you're specifying.

 For example, entering "email" as an input isn't clear enough. Instead, you may want to name an input "requester\_email" with a description such as "the email address of the end user who requested help."
- **Ticket ID**

 When using the ticket ID as an input, you must use the specific name *zendesk\_ticket\_id* and set the type as a number. Auto assist populates that input with the ID of the ticket.

 When making use of the input in your API configuration, you can wrap the input placeholder in quotes to convert it to a string, or incorporate it into a larger string.

 For example, you could have the following property in your API body:

 ```
 "note":"Ticket number {{zendesk_ticket_id}} has been updated!"
 ```

Auto assist has access to read custom ticket fields and the standard ticket fields below:

- Assignee email
- Assignee name
- Brand
- Custom ticket fields
- Priority
- Requester email
- Requester name
- Status
- Subject
- Type

Note: Actions don’t work on [AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346).