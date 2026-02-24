# Using OpenAI actions in action flows

Source: https://support.zendesk.com/hc/en-us/articles/9841067063834-Using-OpenAI-actions-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306) to external systems, such as OpenAI, admins can integrate Zendesk with external systems in automated workflows, improving collaboration and maintaining a seamless experience across multiple platforms.

Note: The steps associated with external systems in action flows are referred to collectively as *external actions*.

This article contains the following topics:

- [Connecting OpenAI to action builder](#topic_pcg_m4w_zgc)
- [Using OpenAI actions in action flows](#topic_chy_m4w_zgc)

## Connecting OpenAI to action builder

Before you can include external actions in your action flows, you must connect the action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it is a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect action builder to OpenAI**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **OpenAI**.
5. Click **Connect**.
6. Use an [API key](https://platform.openai.com/api-keys) to authenticate the account.

   Note:
   - The connection isn't confirmed until you test or use an action flow with OpenAI steps.
   - All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it is a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.

After you've connected to the system, you'll see an indicator that it's connected and details about the instance you're connected to, as well as the actions available for OpenAI.

## Using OpenAI actions in action flows

The OpenAI action steps make it possible for you to provide things such as AI-generated summaries of long tickets to agents, identify negative emotional tones in tickets so they can be routed to specialized teams, extract keywords that can be used as ticket tags, and use tailored AI models to analyze customer messages.

GPT 5.0 is supported for all of the OpenAI steps. This enhances automation capabilities by providing better contextual understanding and more natural responses.

The following OpenAI actions are available:

- [Analyze senitment](#topic_zf5_w4w_zgc)
- [Summarize text](#topic_igy_x4w_zgc)
- [Extract keywords](#topic_omk_y4w_zgc)
- [Send prompt](#topic_sgx_y4w_zgc)

### Analyzing sentiment

Use the *Analyze sentiment* action to detect the emotional tone of text.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `model`, `text` |
| Output | `sentiment` |

### Summarizing text

Use the *Summarize text* action to conense large quanities of text into a brief summary.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `model`, `text` |
| Output | `summary` |

### Extracting keywords

Use the *Extract keywords* action to identify main topics or entities. These can then be used as tags for tickets.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `model`, `text` |
| Output | `keywords` |

### Sending a prompt

Use the *Send prompt* action to define a custom prompt and response from the OpenAI API. For example, a prompt might be:

```
Analyze this ticket and categorize it into one of the following: Billing, Technical Issue, Feature Request, Bug Report, General Inquiry.
Ticket:[description]
```

where *[description]* is replaced with a value by clicking **Add variable**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/action_flow_openai_prompt_step.png)

| | Variables |
| --- | --- |
| Inputs | `model`, `text` |
| Output | `content` |