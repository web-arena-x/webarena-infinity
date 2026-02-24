# Using Google Gemini action in action flows

Source: https://support.zendesk.com/hc/en-us/articles/10306407796122-Using-Google-Gemini-action-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306) to external systems, such as Google Gemini,
admins can integrate Zendesk with external systems in automated workflows, improving
collaboration and maintaining a seamless experience across multiple platforms.

Note: The
steps associated with external systems in action flows are referred to collectively
as *external actions*.

This article contains the following topics:

- [Connecting Google Gemini to action builder](#topic_fcs_gtn_g3c)
- [Using Gemini actions in action flows](#topic_z1q_htn_g3c)

## Connecting Google Gemini to action builder

Before you can include external actions in your action flows, you must connect the
action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the
  external system. Therefore, it's a best practice to use a dedicated service
  account rather than personal credentials when connecting to each external
  system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect action builder to Google Gemini**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action
   flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **Google Gemini**.
5. Click **Connect**.
6. Use an API key to authenticate your account.

   Note:
   - All external actions performed by an action flow are attributed
     to the user who connected the external system. Therefore, it is
     a best practice to use a dedicated service account rather than
     personal credentials when connecting to each external
     system.
   - The connection isn't confirmed until you test or use an action
     flow with a Google Gemini step.

After you've connected to the system, you'll see an indicator that it's connected and
details about the instance you're connected to, as well as the actions available for
Gemini.

## Using Gemini actions in action flows

Gemini action steps can be used to analyze text and send prompts.

The following Gemini actions are available:

- [Analyze sentiment](#topic_lck_r44_zgc)
- [Extract keyword](#topic_ysb_d5c_h3c)
- [Summarize text](#topic_zcg_15c_h3c)
- [Send prompt](#topic_ctn_n5c_h3c)

### Using Gemini to analyze the sentiment of text

Use the *Analyze sentiment* action to detect the emotional tone of text.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `model`, `text` |
| Output | `sentiment` |

### Using Gemini to extract keywords from text

Use the *Extract keywords* action to identify main topics or entities within
text. These keywords can then be used as [ticket tags](https://support.zendesk.com/hc/en-us/articles/4408835059482).

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `model`, `text` |
| Output | `keywords` |

### Using Gemini to summarize text

Use the *Summarize text* action to generate a summary of large quantities of
text.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `model`, `text` |
| Output | `summary` |

### Using Gemini to send a prompt

Use the *Send prompt* action to define a custom prompt and response from the
Google Gemini API.

For example, you might use a prompt such
as:

```
Analyze this ticket and categorize it into one of the following: Billing, Technical Issue, Feature Request, Bug Report, General Inquiry.
Ticket: [description]
```

Where **[description]** is replaced with a variable in the action flow.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `model`, `text` |
| Output | `content` |