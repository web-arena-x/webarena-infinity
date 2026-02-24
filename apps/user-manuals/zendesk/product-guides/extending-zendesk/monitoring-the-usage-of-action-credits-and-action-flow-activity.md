# Monitoring the usage of action credits and action flow activity

Source: https://support.zendesk.com/hc/en-us/articles/10149993578522-Monitoring-the-usage-of-action-credits-and-action-flow-activity

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Note: Action credits are in an introductory period until April 15, 2026. During the
introductory period, the limits documented in this article aren't
enforced.

When using action flows, it's important to monitor your usage so you can
plan and budget accordingly.

This article contains the following topics:

- [Monitoring your account's usage of action credits](#topic_fvh_yzb_xhc)
- [Monitoring action flow activity](#topic_svx_jbx_bfc)

Related articles:

- [Understanding action builder and action
  flows](https://support.zendesk.com/hc/en-us/articles/8855513857306)
- [About actions for auto assist and action
  flows](https://support.zendesk.com/hc/en-us/articles/9174548349978)

## Monitoring your account's usage of action credits

Actions are steps or operations performed by [action flows](https://support.zendesk.com/hc/en-us/articles/8855513857306) that create, read, update, or delete
something in Zendesk or a connected external system. Action credits are the unit of
measurement used to calculate your usage of actions. Action credits are consumed by
most actions performed by action flows, with the following exceptions:

- All action flow triggers
- All flow control and utility steps, such as branch and custom code
  steps
- All actions within action flows initiated by the *Action flow suggested by
  [auto assist](https://support.zendesk.com/hc/en-us/articles/7051314237466) approved by
  agent* trigger

  Note: Custom actions performed outside of action flows
  don't consume action credits.

For example, in the following action flow, each step that consumes an action
credit when the action flow runs is highlighted in green:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/action_flow_usage.png)

Each account includes an allowance of action credits based on their plan and aligned
with their subscription term up to 12 months:

- Suite Team and Growth and Support Team plans include 40,000 actions per
  month or 480,000 annually.
- Suite Professional and Support Professional plans include 100,000 actions
  per month or 1,200,000 annually.
- Suite Enterprise and Support Enterprise plans include 225,000 actions per
  month or 2,700,000 annually.
- Suite Enterprise Plus plans include 400,000 actions per month or 4,800,000
  annually.

After the introductory period, if you find you're exceeding these limits and want to
continue using action flows, you must purchase the Action credits add-on in units of
100,000 actions.

### Viewing your action usage

Admins can view the Usage Summary page to monitor your account's use of action
credits.

**To view your action usage**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Usage > Summary**.
2. Refer to the **Actions** box for the number of action credits used
   and remaining per month.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/action_credits_usage_summary.png)

## Monitoring action flow activity

[Action flows](https://support.zendesk.com/hc/en-us/articles/8855513857306) are user-defined integrated
workflows that perform actions in Zendesk and external systems, but are managed
entirely from within Zendesk. After you [create](https://support.zendesk.com/hc/en-us/articles/8855601898266) an action flow, you can monitor its performance
through a 7-day rolling record of action flow activity. See [Viewing the integrations log](https://support.zendesk.com/hc/en-us/articles/4408819871130).

**To monitor action flow activity**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Logs**.
2. Click on a row to view more detailed information about a log entry.

   Within
   the log, action flow entries are labeled with *Action Flows* as the
   product column. When viewing an action flow log entry, the following
   details are available:
   - **workflow\_name**: The name of the action flow.
   - **trigger**: The name of the event that initiated the action
     flow.
   - **step\_executions**: An array of steps that were completed
     successfully, in the order they occurred.