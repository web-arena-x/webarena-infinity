# Using variables to personalize AI agent answers (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/5480101976218-Using-variables-to-personalize-AI-agent-answers-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

This article describes functionality
available only to customers who had a drafted or published AI agent as of February
2, 2025. For information about equivalent functionality in the [AI agents - Advanced add-on](https://support.zendesk.com/hc/en-us/articles/6970583409690), see [Building dialogues for AI agents - Advanced](https://support.zendesk.com/hc/en-us/sections/8264324615322).

In the bot builder, a variable is a container for data related to a conversation, such as
a customer's name or a store order ID. During a conversation, an AI agent for messaging
can utilize variables in many ways, including:

- Inserted into AI agent messages to personalize text responses, display dynamic
  information and images, or branch the conversation.
- To set a value for a variable based on an end user's input.
- In tags that are added to tickets during the Transfer to agent
  step.

An AI agent can include up to 46 *unique* variables across all answers. Each unique
variable can be used in an answer as many times as needed.

This article includes the following topics:

- [About variable names and values](#topic_up4_3jh_twb)
- [About variable types](#topic_t2y_bkh_twb)
- [Using variables in an answer](#id_kz3_dqh_twb)
- [Using variables in tags](#topic_yx5_vq5_dbc)

## About variable names and values

In the bot builder, each variable has a *name* and *value*. When
configuring a step in an answer, the name acts as a placeholder for the value. When
the AI agent runs the answer, it replaces the variable's name with the variable's
value. For example, you can use a variable named **Email** as a placeholder for
the customer's email address.

Note: Only the first 280 characters of a variable's value appear in the response
displayed in the messaging conversation.

Variables are global within an AI agent. After they're created, variables are
available in all subsequent answers in the end user's conversation via free text or
the Link to another answer step.

### Handling empty variables

A variable is empty if it has no value. AI agents skip empty variables during a
conversation.

For example, a **Send message** step includes an AI agent message of "Your
package's shipping status is **shipping\_status**." If the
**shipping\_status** variable is empty during a conversation, the AI agent
sends "Your package's shipping status is ."

| AI agent message | Customer view |
| --- | --- |
|  |  |

### Handling missing variables

In the **Make API call** step, if one of the saved variables is missing from
the response, the step's Fail branch is triggered. See [Using the Make API call step in bot builder
(Legacy)](https://support.zendesk.com/hc/en-us/articles/4572971586586).

### Handling variables with no source

Normally, variables in the bot builder appear with a gray background. However, if
a variable's source has been removed, it appears with a red background instead.
For example, consider the following scenario:

1. Within an answer flow, you add a Set variable step and use it to create and
   set a variable called **shipping\_status**.
2. As the next step of the flow, you add a Send message step and include the
   **shipping\_status** variable as part of the message.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aia_variable_gray.png)
3. You delete the Set variable step you created above.

   Because the source of
   the shipping\_status variable no longer exists, it now appears in red in
   the Send message step.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aia_variable_red.png)

## About variable types

Bot builder organizes variables based on how they're created and the data they
store:

- [Customer variables](#topic_yyz_dkh_twb)
- [External service variables](#topic_rq2_tkh_twb)
- [Messaging metadata variables](#topic_eww_3lh_twb)
- [Sunshine conversations
  variables](#topic_lcx_2ft_dyb)

### Customer variables

Customer variables store information provided by a customer during an [Ask for details](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_i5r_grz_n5b) step. For example, the
step may ask a customer to provide their name and email address.

When inserting a variable in a step using the **Add a variable** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add-variable-icon.png)) , customer variables appear
under **Responses from customer**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/flow-builder-customer-variables-ex.png)

### External service variables

External service variables store data received from an external system during a
[Make API call](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_d4z_fwm_2tb) step. For example, the
step can make a REST API request to a shipping provider to fetch the current
status of a package.

Admins create external service variables when configuring the
**Make API
call**
step. As part of the configuration, the admin can set a custom name
for each variable.

When inserting a variable in a step using the
**Add a variable**
icon (
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add-variable-icon.png)), external service
variables appear under
**Responses from external service**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/flow-builder-external-service-variables-ex.png)

### Messaging metadata variables

Messaging metadata variables contain information about a customer's identity and
authentication status. Messaging metadata variables get their values from the
signed JSON Web Tokens (JWTs) used for
[messaging authentication](https://support.zendesk.com/hc/en-us/articles/4411666638746).

Messaging metadata variables aren't enabled by default and are only available for the Web Widget
and mobile SDK channels. For more information about enabling and using messaging
metadata variables, see [Using authentication metadata in an AI agent
answer](https://support.zendesk.com/hc/en-us/articles/5314129059482).

If enabled, messaging metadata variables appear under **Messaging metadata** when
inserting a variable in a step using the **Add a variable** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add-variable-icon.png)) ,

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/flow-builder-metadata-variables-ex.png)

### Sunshine conversations variables

Sunshine conversations variables can be used to connect to your [Sunshine Conversations
integrations](https://support.zendesk.com/hc/en-us/articles/5514406080538).

Available variables include:

- [SunCo user id](https://docs.smooch.io/rest/#tag/Users)
- [SunCo conversation id](https://docs.smooch.io/rest/#tag/Conversations)
- [SunCo app id](https://docs.smooch.io/rest/#tag/Apps)

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bot_builder-sunco_variables.png)

## Using variables in an answer

With the bot builder, you can use inserted variables to:

- [Customize AI agent messages](#topic_jj3_l4h_twb)
- [Send data to external systems](#topic_uzb_w4h_twb)
- [Branch an answer's flow](#topic_tr4_2ph_twb)
- [Set variable values](#topic_kkr_2q5_dbc)

### Customizing AI agent messages

Admins can insert variables to the AI agent message of the following step
types:

- [Present options](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_mnf_gwc_k4b)
- [Add carousel](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_il3_pmj_tvb)
- [Transfer to agent](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_zqr_gwc_k4b)
- [Send message](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_iqz_fwc_k4b)
- [Show help center articles](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_grj_gwc_k4b)

For example, the following AI agent message includes the **Name**
variable.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/flow-builder-bot-message-var-ex.png)

### Sending data to external systems

When making a REST API call to an external system using the **Make API call**
step, admins can add insert variables into the path and query string of the
step's **Endpoint URL** field. For more information, see [Using the Make API call step in the bot
builder](https://support.zendesk.com/hc/en-us/articles/4572971586586).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/flow-builder-bot-message-endpoint-url-ex.png)

### Branching an answer's flow

The **Branch by condition** step lets an admin branch the flow of an answer
based on the value of one or more variables. For more information, see [Understanding branching
conditions](https://support.zendesk.com/hc/en-us/articles/5280598023450).

Note: Custom drop-down ticket fields use the *Tag*
value as the variable’s value.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/flow-builder-bot-message-branch-by-condition-ex.png)

### Setting variable values

Admins can use the **Set variable**  step to create a new variable and assign
a value or to select an existing variable and overwrite its value based on an
end user's actions in a conversation. Variables can be referenced across all
answers in the AI agent.

See [Understanding answer step types: Set
variable](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_utv_jq5_dbc) for usage details.

## **Using variables in tags**

Admins can use variables in the tags that are added to a ticket created as
part of the [Transfer to agent step](https://support.zendesk.com/hc/en-us/articles/4408836323738-Understanding-answer-step-types#topic_zqr_gwc_k4b). These tags can be
used by agents to view, organize, and track tickets, and in automated actions such
as ticket routing and other business rules.

Although they are technically part of an answer, variables in tags are
subject to some rules and restrictions that other variables aren’t.

You can use variables generated from API calls and system variables. Available
variables appear in the selection drop-down:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_variable_tag.png)

However, variables containing input from end users can’t be used in tags. They
will appear in the drop-down list but will be disabled. For example, you can’t refer
to a variable using information collected in an [Ask for details step](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_i5r_grz_n5b) earlier in the
conversation.

The following rules and recommendations apply to using variables in
tags:

**Character limit**

- Hard-coded tags are limited to 80 characters each.

**Special characters**

- Variables containing the following special characters can't be used and won't appear as available variables: **£**, **`**, **´**, **\**,
  **[**, **]**, **{**, **}**, **(**, **)**, **<**, **>**, **%**, **&**, **?**, **+**, **@**, **!**,
  **\***, **$**, **#**, **=**, and **"**
- Space or commas used in variables appear as underscores in tags.

**Additionally, we recommend the following best practices when using variables as tags:**

- Tags are typically used for routing conversations or in trigger conditions. If
  you want to add information to tickets for agent context, we recommend using
  [custom fields](https://support.zendesk.com/hc/en-us/articles/4420210121114).
- Limit the number of possible values for a variable. Too many values can cause unexpected behaviors.
- Keep value options short to avoid having them truncated as tags.
- Avoid having special characters in the values.