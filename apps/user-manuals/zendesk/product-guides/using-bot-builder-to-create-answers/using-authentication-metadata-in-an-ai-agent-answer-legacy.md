# Using authentication metadata in an AI agent answer (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/5314129059482-Using-authentication-metadata-in-an-AI-agent-answer-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

This article describes functionality available only to customers who had a drafted or published AI agent as of February 2, 2025.
For information about equivalent functionality in the [AI agents - Advanced add-on](https://support.zendesk.com/hc/en-us/articles/6970583409690), see [Building dialogues for AI agents - Advanced](https://support.zendesk.com/hc/en-us/sections/8264324615322).

[Bot builder variables](https://support.zendesk.com/hc/en-us/articles/5480101976218) let you customize a messaging AI agent's answers based on data related to a conversation. Messaging metadata variables are a type of variable used in the bot builder that contain information about the current customer's identity and authentication status.

Messaging metadata variables get their values from the signed JSON Web Tokens (JWTs) used for [messaging authentication](https://support.zendesk.com/hc/en-us/articles/4411666638746). During a conversation, a messaging AI agent can use this data to customize its responses, display information specific to the customer, or branch the conversation's flow.

This article includes the following topics:

- [Enabling messaging metadata variables](#topic_ktn_xlh_twb)
- [Supported messaging metadata variables](#topic_lwy_kmh_twb)
- [Best practices for using messaging metadata variables](#topic_jzh_pnh_twb)

For a broader overview of the AI agent variables and how you can use them in answers, see [Using variables to personalize AI agent answers](https://support.zendesk.com/hc/en-us/articles/5480101976218).

## Enabling messaging metadata variables

Messaging metadata variables aren't enabled by default. To enable messaging metadata variables, an admin must [create a signing key](https://support.zendesk.com/hc/en-us/articles/4411666638746#topic_pyg_kqx_3sb)
used to generate JWTs for messaging authentication. Messaging authentication and messaging metadata variables are only available for the Web Widget and mobile SDK channels.

For more information about setting up messaging authentication, see [Authenticating end users in messaging for the Web Widget and mobile SDK](https://support.zendesk.com/hc/en-us/articles/4411666638746).

## Supported messaging metadata variables

Unlike other types of AI agent variables, messaging metadata variables have predefined names. You can’t modify a messaging metadata variable’s name or value in an answer flow.

| Messaging metadata variable name | Description |
| --- | --- |
| Provided email | Email address of the customer. This email address is pulled from the JWT used for messaging authentication. |
| Provided name | Name of the customer. This name is pulled from the JWT used for messaging authentication. |
| Authenticated external ID | Unique alphanumeric string that identifies the customer. This ID is pulled from the JWT used for messaging authentication. |
| Authenticated status | If true, the customer is authenticated. Otherwise, false. This variable is always true or false, never empty. When using the **Authenticated status** variable in a **Branch by condition** step, only the **Is** operator is supported. |

### Using the Provided name and Provided email variables

Keep the following considerations in mind when using the **Provided name** and **Provided email** variables:

- Messaging AI agents automatically skip the collection of the **Name** and **Email** variables for authenticated customers in an **Ask for details** step. For authenticated customers, these variables are empty and are skipped in later steps of the conversation. Instead, use the **Provided name** and **Provided email** variables.

 | Skipped **Name** and **Email** variable collection the from **Ask for details** step | **Provided name** and **Provided email** variables |
 | --- | --- |
 | | |
- The JWTs used for messaging authentication don't require a customer's name or email address. If your organization doesn't include a name or email address in its JWTs, the respective **Provided name** and **Provided email** variable are empty and skipped during a conversation.

 In such cases, we recommend updating your JWTs to include a name and email address.
- The **Provided name** and **Provided email** variables are empty for unauthenticated customers. Avoid using these variables in answer steps for unauthenticated customers.

### Using messaging metadata variables with unauthenticated customers

If a customer isn't authenticated, the **Authenticated status** variable's value is false. Other messaging metadata variables are empty for unauthenticated customers and are skipped during a conversation.

## Best practices for using messaging metadata variables

When creating an answer that uses messaging metadata variables, keep the following best practices in mind:

- If you don’t include the customer's name or email address in the JWTs used for messaging authentication, don’t use the **Provided name** and **Provided email** variables.
- To build an answer flow that’s available to both authenticated and unauthenticated customers, use a **Branch by condition** step to check the customer's **Authenticated Status** variables. Only include messaging metadata variables in branches where **Authenticated Status** is true.
- If you’re building an answer that’s only available to authenticated customers and your organization's JWTs include a name and email address, use the **Provided name** and **Provided email** variables for the customer's name and email address. In such cases, you don’t need to collect this information again using an **Ask for details** step.