# Turning on and configuring auto assist

Source: https://support.zendesk.com/hc/en-us/articles/8013454025114-Turning-on-and-configuring-auto-assist

---

Auto assist is an AI-powered assistant for your agents. Using large language model (LLM) technology, auto assist understands the contents of submitted tickets and makes suggestions to your agents on how to solve them.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Enable auto assist to empower agents with AI-driven ticket suggestions. Configure access for specific agent groups and set up tags for messaging or email channels using ticket triggers. Ensure tickets have the `agent_copilot_enabled` tag for suggestions to appear. Create procedures and actions to guide agents in resolving issues effectively. Explore related articles for detailed setup instructions.

Auto assist is an AI-powered assistant for your agents. Using large language model (LLM)
technology, auto assist understands the contents of submitted tickets and makes suggestions to your agents on how to solve them.

Before auto assist can help guide agents in solving tickets, you must turn it on, specify which agents can use auto assist, and configure which channels auto assist works with.

This article contains the following topics:

- [Turning auto assist on](#topic_lqr_px3_23c)
- [Configuring auto assist on messaging or email channels using tags added by ticket triggers](#topic_wx3_rww_xcc)
- [Next steps: Creating auto assist procedures and actions](#topic_egf_gbx_xcc)

Related articles:

- [About auto assist](https://support.zendesk.com/hc/en-us/articles/9945148867866)

## Turning auto assist on

You can turn on auto assist and configure who has access in Admin Center.

**To turn on and configure access to auto assist**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Agent copilot > Auto assist**.
2. Select **Show auto assist replies and actions in the agent composer**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_auto_assist_setting.png)
3. In the **Who has access** field, search for and select the groups that should be able to use the suggested replies feature. By default, all groups have access.
4. Click **Save**.

   To configure which channels and tickets auto assist can work on, [add a tag using a ticket trigger](#topic_wx3_rww_xcc). With this setup, auto assist is available to an agent when the conditions specified within your trigger are met.

   Note: If you drafted or published an AI agent before February 2, 2025, you can configure auto assist to work on messaging tickets that originate from an AI agent. See [Configuring auto assist to work with messaging tickets originated from AI agents (Legacy)](https://support.zendesk.com/hc/en-us/articles/9696147377562).

## Configuring auto assist on messaging or email channels using tags added by ticket triggers

Configure auto assist on messaging or email channels by using tags that are added by ticket triggers. This configuration method works by setting the *agent\_copilot\_enabled* tag on tickets based on specified conditions.

Tickets must have the *agent\_copilot\_enabled* tag for auto assist suggestions to appear in the Agent Workspace.

For example, you could create a trigger that adds the auto assist tag to tickets that have a [specific intent predicted by intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538). Assuming you [create a procedure](https://support.zendesk.com/hc/en-us/articles/7924047699738) that describes how agents should solve issues related to that intent, auto assist will be able to guide the agent in solving the customer’s issue.

**To create a trigger that adds the auto assist tag to tickets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click **Add trigger**.
3. In **Trigger name**, enter a descriptive name for your trigger.
4. (Optional) Enter a **Description** for your trigger.
5. (Optional) Select a **Category** for your trigger.
6. In the **Conditions** pane, under **Meet ALL of the following conditions**, add the following conditions:
   - **Ticket > Ticket status** | **Is** | **New**
   - **Ticket > Tags** | **Contains none of the following** | **agent\_copilot\_enabled**

     This condition ensures that your trigger will run only once on each ticket. The trigger will add the tag the first time it runs, and after that, the presence of the tag prevents the trigger from running again.
7. Under **Meet ANY of the following conditions**, add the following conditions:
   - (Optional) **Ticket > Channel** | **Is** | <select the channel you want the trigger to work on>

     Repeat the condition above for additional channels. These conditions ensure that auto assist works only on tickets created through certain channels. For example, you might not want auto assist to apply to email tickets.
   - (Optional) **Ticket > Intent** | **Is** | <select an intent you have created a procedure for>

     Repeat the condition above for additional intents. You don’t need to create separate triggers for each intent. Auto assist will be able to tell which procedure to use based on the contents of the customer’s request as well as the procedure title. Alternatively, add other conditions that fit your organization’s workflows.
8. In the **Actions** pane, add the following action:
   - **Ticket > Add tags** | **agent\_copilot\_enabled**
   - (Optional) Add another tag to identify which [procedure you’ve created](https://support.zendesk.com/hc/en-us/articles/7924047699738) for auto assist to follow in this situation (for example, copilot\_order\_cancellation). Later, you can [create an Explore report](https://support.zendesk.com/hc/en-us/articles/7739110419610) that uses this tag to identify tickets where a specific procedure was followed on a ticket.
9. Click **Create**.

For more help with triggers, see [Creating ticket triggers for automatic ticket updates and notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466).

## Next steps: Creating auto assist procedures and actions

Before auto assist is fully functional for your agents, you need to create procedures and actions that tell auto assist how to properly guide agents in solving tickets.
See the following articles for instructions:

- [Creating procedures for auto assist](https://support.zendesk.com/hc/en-us/articles/7924047699738)
- [Creating custom actions for auto assist and action flows](https://support.zendesk.com/hc/en-us/articles/8013439366810)