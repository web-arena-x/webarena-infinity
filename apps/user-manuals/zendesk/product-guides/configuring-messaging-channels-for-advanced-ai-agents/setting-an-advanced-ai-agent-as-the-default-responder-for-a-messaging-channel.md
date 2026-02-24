# Setting an advanced AI agent as the default responder for a messaging channel

Source: https://support.zendesk.com/hc/en-us/articles/8357757911834-Setting-an-advanced-AI-agent-as-the-default-responder-for-a-messaging-channel

---

After youcreate an advanced AI agentfor messaging, you can configure which messaging channels it should be the default responder for.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

After you [create an advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357749415066) for messaging, you
can configure which messaging channels it should be the default responder for.

This article contains the following topics:

- [About a messaging channel’s default responder](#topic_g14_4ns_rgc)
- [Setting an advanced AI agent as the default responder for individual channels](#topic_rl3_pns_rgc)
- [Setting an advanced AI agent as the default responder for all channels](#topic_an2_qns_rgc)
- [Configuring which advanced AI agent responds on specific messaging channels](#topic_k4b_q4j_jhc)
- [Prevent an advanced AI agent from responding on any messaging channel](#topic_bc5_rhb_g3c)

Related article:

- [Managing advanced AI agents connected to
  messaging channels](https://support.zendesk.com/hc/en-us/articles/10050437105946)

## About a messaging channel’s default responder

First, it’s important to understand that setting an advanced AI agent as the default
responder technically sets AI agents - Advanced, as a whole, as the default
responder. If you have more than one advanced AI agent, you need to [use routing rules](#topic_k4b_q4j_jhc) to define which
specific advanced AI agent should respond on each messaging channel.

When you assign the default responder role to an advanced AI agent, it becomes the
first responder in a customer conversation. This means when a customer contacts
support through one of your messaging channels, the AI agent manages the
interaction. It replaces any previously connected AI agent or default response
configuration, which is reverted to Draft mode.

Any time a new channel is added to your instance, the [AI agent with the default label](#topic_an2_qns_rgc) is automatically assigned
as the default responder for that channel. If you assign the default label to
another AI agent, that AI agent becomes the responder for any channels using the
default responder.

When using an advanced AI agent as a default responder in conversations, consider the
following:

- Only one advanced AI agent can be assigned the default responder role in each
  instance.
- The advanced AI agent with the default responder label can't be deleted or
  uninstalled until the label is assigned to another responder.
- If you don't want to use an advanced AI agent as the default responder, you can
  assign the default responder label to an essential AI agent or a [third-party bot](https://support.zendesk.com/hc/en-us/articles/5064149334426).
- If you don't have any advanced AI agents connected to your instance, an
  essential AI agent is the default responder.

## Setting an advanced AI agent as the default responder for individual channels

In Admin Center, you can set an advanced AI agent as the default responder for one or
more messaging channels.

Note: The [Conversation control setting](https://support.zendesk.com/hc/en-us/articles/5514406080538#topic_fwd_ylm_y1c) must be
set to **Release control** for per-channel responders to work.

**To set an advanced AI agent as the default responder for individual
channels**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. In the **Advanced** section, click **AI agents - Advanced**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_default_responder_individual.png)
3. In the **Channels** section, select the channels you want the AI agent to
   be the default responder on.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_default_responder_individual_select.png)
4. Click **Save**.

## Setting an advanced AI agent as the default responder for all channels

You can also set an advanced AI agent as the default responder for all messaging
channels.

**To set an advanced AI agent as the default responder for all channels**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. In the **Advanced** section, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) to the right of **AI agents - Advanced**.
3. Select **Set as default for all channels**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_default_responder_all.png)

   AI agents - Advanced is
   marked as default, and your advanced AI agents become the default responders
   for all configured messaging channels according to the [routing rules you
   configure](#topic_k4b_q4j_jhc).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_default_responder_default.png)

## Configuring which advanced AI agent responds on specific messaging channels

By default, the first advanced messaging AI agent created in your account is the
fallback, meaning this AI agent in particular is the default responder for any
channel where AI agents - Advanced is set as the default responder.

When you have more than one advanced messaging AI agent, you can use routing rules to
configure which specific advanced AI agent should respond on each messaging channel.
A routing rule is a set of one or more conditions based on the source of the
conversation, user metadata, or conversation metadata.

**To configure routing rules for advanced messaging AI agents**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. Select the **Routing rules** tab.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_routing_rules_page.png)
4. Click **Add rule**.

   The Create routing rule panel opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_routing_rule_panel.png)
5. In **Name**, enter a descriptive name for the routing rule.
6. (Optional) Change the dropdown in **Match ALL conditions below** to
   **ANY**, depending on the logic of your rule.
7. Define your first condition:
   - In **Source**, select one of the following options:
     - **Source** (of the conversation)
     - **User metadata**
     - **Conversation metadata**
   - Under **Parameter**, use the parameter name, operator, and value
     fields to define a parameter based on the source you selected above:
     - If you selected Source above, the available parameters are
       **Type** and **Integration ID**.

       Tip: To find the integration
       IDs of any Sunshine Conversations integrations, use the
       [List
       Integrations](https://docs.smooch.io/rest/v1/#list-integrations) endpoint of the Sunshine
       Conversations API.
     - If you selected User metadata or Conversation metadata
       above, define a parameter based on the condition you want to
       create. For help, see [Using parameters in
       advanced AI agents](https://support.zendesk.com/hc/en-us/articles/9522180655386).
8. (Optional) Click the plus (+) icon to insert another condition, and repeat
   the step above.
9. In **Assign to**, select the specific AI agent that should be the default
   responder to the conversation when the conditions listed above are true.
10. (Optional) If you don't want the rule to be active yet, toggle **Rule is
    active** to off.

    When you're ready to make the rule active, return
    to this screen and toggle this setting on.
11. Click **Create**.

## Prevent an advanced AI agent from responding on any messaging channel

You can prevent an advanced AI agent from responding to customers on any messaging
channel. You do this by deactivating or deleting any routing rules assigned to it.
This allows you to configure and test the AI agent without making it live to
customers.

**To prevent an AI agent from responding on any messaging channel**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. Select the **Routing rules** tab.
4. In the **Assigned to agent** column, select a rule that's assigned to the
   AI agent you don't want responding to customers.

   The rule's configuration
   appears.
5. Click the **Rule is active** toggle to deactivate the
   rule.

   Alternatively, if you no longer need the rule at all, click
   **Delete** and **Delete** again to delete the rule
   entirely.
6. Click **Save**.
7. Repeat the steps above for any other rules assigned to the AI agent.