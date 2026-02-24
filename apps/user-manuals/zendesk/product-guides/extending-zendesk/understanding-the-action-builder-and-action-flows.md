# Understanding the action builder and action flows

Source: https://support.zendesk.com/hc/en-us/articles/8855513857306-Understanding-the-action-builder-and-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Action flows are user-defined automated sequences of steps
that perform actions in Zendesk and external systems based on a defined event that
initiates or *triggers* the workflow. Action flows can run in response to their
configured action flow trigger events or be initiated by agents using agent copilot auto
assist. The steps within an action flow can include Zendesk actions as well as actions
that occur in external systems.

The Action flows page in Admin Center includes a visual workflow builder, referred to as
the *action builder*, that is used to create and edit action flows. The action
builder is designed to make it easier to make multi-system workflows that integrate
Zendesk with external systems.

This article contains the following topics:

- [Considerations for using action flows](#topic_vn4_vwf_t2c)
- [Accessing the Action flows page](#topic_umk_wwf_t2c)
- [Related resources](#topic_dmv_xwf_t2c)

## Considerations for using action flows

Consider the following before you start using action flows:

- You can create a maximum of 25 action flows.
- Each action flow can contain a maximum of 50 steps. The action flow trigger
  is excluded from this count.
- The number of action flows and custom actions you can execute per second is
  rate limited. See [Rate limits and bursts](#topic_whg_nnr_j3c).
- When creating branches within an action flow, you can configure only one
  condition per branch.
- The branch step supports the evaluation of conditions only on text, number,
  decimal, true/false, date, and date time variables as well as checking
  arrays of tags.
- You can connect to only one instance of each [external system](https://support.zendesk.com/hc/en-us/articles/9052269929626).
- Most standard ticket, user, and organization fields are supported. All
  custom ticket fields are also supported. However, the following limitations
  apply:
  - Custom lookup relationship fields only support variables or manual
    inputs, and you must use the ID of the related object record to
    specify values.
  - If entering values manually for custom multi-select fields, you must
    use the *tag* value rather than the name.
  - Numeric and decimal custom ticket fields are treated as text
    outputs. This means only conditional operators for text can be used
    to evaluate these fields.
- The following limitations apply to custom actions for agent copilot auto
  assist:
  - Auto assist action flow triggers and custom action steps can be
    added to action flows, but will function only if you have purchased
    the [Zendesk Copilot
    add-on](https://support.zendesk.com/hc/en-us/articles/5715517808026).
  - Only custom actions that were created or updated after March 13,
    2025 are available as steps for action flows.
  - Custom action steps don't support the use of files or
    attachments.
  - Updates made to custom actions that are already used in action flows
    aren't reflected in the action flow's step. To use the updated
    version of a custom action in an existing action flow, you must
    delete the custom action step and re-add it.
- Each account includes an allowance of action credits based on their plan.
  See [Monitoring the usage of action credits
  and action flow activity](https://support.zendesk.com/hc/en-us/articles/10149993578522).

### Rate limits and bursts

The following rate limits apply to action flows and custom actions:

- Custom action flow triggers support up to 100 incoming API requests per
  minute.
- Action flows support bursts of up to 300 action flow executions, for
  example 30 workflows per second for 10 seconds.
- Action flows support 10 executions per second outside of bursts.
- Custom actions support bursts of up to 280 action executions. This
  applies to custom action executions by action flows and auto assist
  cumulatively.
- Custom actions support 6 executions per second outside of bursts.

The burst allowance for action flows and custom actions recharge whenever your
usage for any given second is below the per-second limits described above. The
spare execution count is added back to the burst allowance. For example, if you
run 2 action flows in a second, then 8 action flow executions are added back to
your burst allowance.

Additionally, you don't have to wait for the burst allowance to fully recharge
before using it again. As soon as any portion of the burst allowance is
replenished, that amount is immediately available for use.

## Accessing the Action flows page

The Action flows page in Admin Center is used to create, edit, and delete your action
flows.

**To access the Action flows page**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
  **Apps and integrations** in the sidebar, then select **Actions > Action
  flows**.

## Related resources

The following articles provide more information about creating, using, and managing
action flows:

- [Creating action flows to automate
  processes across Zendesk and external systems](https://support.zendesk.com/hc/en-us/articles/8855601898266)
- [Editing and managing action
  flows](https://support.zendesk.com/hc/en-us/articles/9052312956570)
- [Creating custom action flow
  triggers](https://support.zendesk.com/hc/en-us/articles/9712284817818)
- [Using Confluence actions in action
  flows](https://support.zendesk.com/hc/en-us/articles/9836432286490)
- [Using Google Sheet actions in action
  flows](https://support.zendesk.com/hc/en-us/articles/9836727346970)
- [Using Jira actions in action
  flows](https://support.zendesk.com/hc/en-us/articles/9836794562842)
- [Using Microsoft Calendar actions in
  action flows](https://support.zendesk.com/hc/en-us/articles/9849724302234)
- [Using Microsoft Excel actions in action
  flows](https://support.zendesk.com/hc/en-us/articles/9840801141274)
- [Using Microsoft Outlook actions in action
  flows](https://support.zendesk.com/hc/en-us/articles/9840940606106)
- [Using Microsoft Teams actions in action
  flows](https://support.zendesk.com/hc/en-us/articles/9841034139674)
- [Using OpenAI actions in action
  flows](https://support.zendesk.com/hc/en-us/articles/9841067063834)
- [Using Salesforce actions in action
  flows](https://support.zendesk.com/hc/en-us/articles/9841156736282)
- [Using Shopify actions in action
  flows](https://support.zendesk.com/hc/en-us/articles/9849578907930)
- [Using Slack actions in action
  flows](https://support.zendesk.com/hc/en-us/articles/9849650344730)
- [Using custom code steps in action
  flows](https://support.zendesk.com/hc/en-us/articles/9853782610970)