# Setting up intelligent triage intents

Source: https://support.zendesk.com/hc/en-us/articles/8903424797722-Setting-up-intelligent-triage-intents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Copilot |

As part of [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4964463770650), intents detect what a ticket is about. You can use the intents that appear in tickets to automate your workflows.

To begin, it's helpful to understand the [use cases](https://support.zendesk.com/hc/en-us/articles/5222280338202) where intents can help in ticket workflows. Here are some ways you can use them:

- [Redirect customers to self-serve](intelligent-triage-use-cases-and-workflows.md#topic_ojz_rdx_tvb).

 For example, you can deflect tickets with account password or sign in issues by sending an auto reply with an article that describes how to solve the problem.
- [Route tickets to the right groups](routing-automatically-triaged-tickets-using-standalone-skills-based-routing.md).

 For example, you can assign a refund intent directly to agents who specialize in handling refunds.
- [Increase ticket priority](routing-automatically-triaged-tickets-using-omnichannel-routing.md#topic_k43_4hs_25b).

 For example, you can increase SLA priority for tickets that report scam issues.

To help you get the most out of Zendesk's AI Copilot features, this article provides an overview on how admins can get started with intents. It contains the following sections:

- [Step 1: Set up the channels for intent detection](#topic_nfx_tgn_k2c)
- [Step 2: Use triggers to create workflows based on intents](#topic_usd_cfy_j2c)
- [Step 3: Track your progress with the Intelligent triage dashboard](#topic_gdf_x5y_j2c)

**Related articles**

- [About intelligent triage](https://support.zendesk.com/hc/en-us/articles/4964463770650)
- [Intelligent triage use cases and workflows](https://support.zendesk.com/hc/en-us/articles/5222280338202)
- [Overview of the Intelligent triage dashboard](https://support.zendesk.com/hc/en-us/articles/7934127855002)

## Step 1: Set up the channels for intent detection

You can set which ticket channels include [intent detection](https://support.zendesk.com/hc/en-us/articles/4550640560538#topic_ebn_l4g_htb).

For example, you might want your agents to view intents on email channels, but not messaging channels.

**To set up channels for intents**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Intent**.

   A list of intelligent triage intents appears.
2. Click **Manage settings**.

   A **Manage settings** page appears.
3. For intent detection, add the **Channels** you use the most. Some channels are already added by default.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_gs_intent_channels.png)

   For a full list of channels you can add, see [Turning on and configuring intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538#topic_gpp_p4g_htb).
4. Click **Save**.

## Step 2: Use triggers to create workflows based on intents

Once you are familiar with the use cases where intents can help and configure which channels include intent detection, you can create ticket triggers to manage ticket workflows based on intents. For example, you can create a trigger to automatically route any ticket with an Account activation intent to a group of agents in your company who handle account services.

**To create a trigger based on intent**

To automate ticket workflows, create ticket triggers based on intent.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. On the Triggers page, click the **Ticket** tab, then click **Create trigger**.
3. Enter a **Name**, **Description**, and **Category** for your trigger. See [Creating ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) for details.
4. In trigger **Conditions**, add the **Intent** you want to use as part of the trigger condition.

   You can use the values included on the Intent list to specify a condition. See [Accessing and viewing intelligent triage intents](https://support.zendesk.com/hc/en-us/articles/9488234915610).

   For example:

   **Intent | Is | Account::Account activation**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_gs_intent_trigger_condition.png)
5. In trigger **Actions**, add the actions you want to perform when the condition applies.

   For example:

   **Ticket > Group | Account services**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_gs_intent_trigger_action.png)

   For more information on trigger conditions and actions, see [Ticket trigger conditions and actions reference](https://support.zendesk.com/hc/en-us/articles/4408893545882) and [Zendesk chat and messaging triggers conditions and actions reference](https://support.zendesk.com/hc/en-us/articles/4408842880282).
6. Click **Create trigger**.

Tip: You can incorporate intelligent triage information into your omnichannel routing workflow for email and messaging tickets. See [this article](https://support.zendesk.com/hc/en-us/articles/4766535251610) for details.

## Step 3: Track your progress with the Intelligent triage dashboard

Zendesk Explore includes an [Intelligent triage dashboard](https://support.zendesk.com/hc/en-us/articles/7934127855002) you can use to extract valuable insights into your tickets. Use these insights to improve your workflow and determine how effective your support is.

**To open the Intelligent triage dashboard**

1. Open the [product tray](https://support.zendesk.com/hc/en-us/articles/4408838272410) and select **Analytics**.

   A list of Explore dashboards appears.
2. From the list of dashboards, click the **Zendesk Copilot: Intelligent triage** dashboard.

   As you drive more volume of tickets, the intelligent triage dashboard will help you understand your service operations and provide insights to identify opportunities to improve.

   Tip: You can also view suggestions for improvements in the **Recommendations** section of the Overview: Copilot page.