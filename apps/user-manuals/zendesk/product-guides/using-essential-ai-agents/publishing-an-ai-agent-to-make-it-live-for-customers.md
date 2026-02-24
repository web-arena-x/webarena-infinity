# Publishing an AI agent to make it live for customers

Source: https://support.zendesk.com/hc/en-us/articles/7232810932250-Publishing-an-AI-agent-to-make-it-live-for-customers

---

After youcreateorupdatean AI agent, you need to publish the AI agent before it or any changes to its settings are made live for customers.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article applies to [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690) and [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality).

After you [create](https://support.zendesk.com/hc/en-us/articles/4408824263578) or [update](https://support.zendesk.com/hc/en-us/articles/6447052708762) an AI agent, you need to publish the AI agent before it or any changes to its settings are made live for customers.

You must be an admin to publish an AI agent.

This article contains the following topics:

- [About publishing AI agents](#topic_uvm_tlm_dgc)
- [Publishing a new AI agent for the first time](#topic_ads_n1n_3bc)
- [Republishing an existing AI agent](#topic_xfh_f1t_dgc)

Related articles:

- [Viewing and configuring settings for AI agents](https://support.zendesk.com/hc/en-us/articles/6447052708762)

## About publishing AI agents

You can publish an AI agent to any messaging, email, or web form channel where you want to add it. An AI agent can be published to multiple channels, including multiple channel types, at the same time. For example, a single AI agent can be published to two messaging channels and an email channel.

However, multiple AI agents cannot be published to a single channel.

### About publishing to a messaging channel

When you publish an AI agent to a messaging channel, any other response—either the [default messaging response](https://support.zendesk.com/hc/en-us/articles/4500737327258) or another AI agent—is removed from that channel and replaced with the newly published AI agent. The AI agent remains the channel’s default responder until you remove it from that channel.

### About publishing to an email or web form channel

When you first [select an email or web form channel](https://support.zendesk.com/hc/en-us/articles/9543022336794#topic_bmj_nbt_dgc) in your AI agent, the system automatically creates one trigger and two automations, which are all set to Inactive.

- **The trigger** is how the AI agent sends the initial generative response to a customer’s ticket.
- **The automations** are how the AI agent follows up on its initial response to verify that it solved the customer’s question (known as a bump automation)
 and subsequently set the ticket status to Solved (known as a solve automation).

For details about their default configuration, see [Reference: Default ticket trigger and automations created for AI agents on the email channel](https://support.zendesk.com/hc/en-us/articles/9483857396378).

When the system creates the trigger, it also scans your system to determine whether any existing triggers might conflict with the new one. Conflicts might cause multiple emails to be sent to a customer in response to their submitted ticket. If any conflicting triggers are found, you receive a warning with a link to the conflicting triggers so you can deactivate them before finalizing the AI agent publication.

When you publish the AI agent, the trigger and automations are set to Active and begin acting on tickets created from that point on.

If you remove an AI agent from an email or web form channel or delete the AI agent entirely, the ticket trigger that was created when you first published the AI agent is deactivated. However, you must manually [deactive the automations](https://support.zendesk.com/hc/en-us/articles/4408883801626#topic_wsq_xjv_ub) so that they don't continue to act on tickets.

If you republish the AI agent, the trigger and automations are reactivated.
When this happens, the trigger is restored to its default configuration. If you previously customized the default trigger, your customizations are overwritten and must be made again.

If you do not want the trigger or automations to run under any circumstances, you must delete them.

It's not possible to link additional custom triggers or automations directly to the AI agent. You can edit the default trigger and automations, but adding new linked ones is not supported. Additionally, if you disable the default trigger, the AI agent is automatically unpublished and returned to draft status, so the default trigger must remain active if you want the AI agent to remain available to customers.

## Publishing a new AI agent for the first time

The first time you publish an AI agent, you select the channels it’s associated with.
Publishing a new AI agent makes it available to customers on those channels.

**To publish a new AI agent for the first time**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to publish.
3. Click **Publish AI agent**.

   A new dialog opens.
4. Select the channels the AI agent should be available on.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_publish_ai_agent.png)
5. If necessary, address any warnings that appear, such as conflicting triggers for email or web form channels.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_publish_ai_agent_conflicting.png)
6. Click **Publish**.

The AI agent and all of its current settings are made live for customers.

## Republishing an existing AI agent

Republishing an existing AI agent makes it available to customers on the [channels you specified](https://support.zendesk.com/hc/en-us/articles/9543022336794) with its [current settings](https://support.zendesk.com/hc/en-us/articles/6447052708762) applied.

Note: Republishing an AI agent restores the associated trigger to its [default configuration](https://support.zendesk.com/hc/en-us/articles/9483857396378). If you previously customized the default trigger, your customizations are overwritten and must be made again.

**To republish an existing AI agent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to republish.
3. Click **Publish AI agent**.

   If you’re republishing an AI agent that you’ve:

   - Removed from all channels, a confirmation dialogue appears. Review the information and click **Confirm changes**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_unpublish_ai_agent_confirm.png)
   - Added back to one or more channels after having previously removed it from all channels, a channel selector dialogue appears. Review the channels and click **Publish**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_publish_ai_agent.png)

The AI agent and all of its current settings are made live for customers. Or, if you’ve removed the AI agent from all channels, it no longer appears to customers.