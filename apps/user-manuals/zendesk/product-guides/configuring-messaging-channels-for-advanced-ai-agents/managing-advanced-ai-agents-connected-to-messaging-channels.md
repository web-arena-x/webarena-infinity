# Managing advanced AI agents connected to messaging channels

Source: https://support.zendesk.com/hc/en-us/articles/10050437105946-Managing-advanced-AI-agents-connected-to-messaging-channels

---

After youcreate an advanced AI agentfor messaging, you can manage settings that affect how it behaves on messaging channels.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

After you [create an advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357749415066) for messaging, you
can manage settings that affect how it behaves on messaging channels.

This article contains the following topics:

- [Viewing all advanced AI agents in a messaging group](#topic_vxf_hcb_g3c)
- [Managing messaging channel settings for an advanced AI agent](#topic_yf3_1gk_jhc)
- [Connecting an advanced AI agent to a different subdomain](#topic_ulq_zk5_33c)

Related article:

- [Setting an advanced AI agent as the default
  responder for a messaging channel](https://support.zendesk.com/hc/en-us/articles/8357757911834)

## Viewing all advanced AI agents in a messaging group

You can see which advanced AI agents are included in your messaging group.

**To view all AI agents in a messaging group**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. Select the **AI agents in this group** tab.

   The table shows you which
   advanced AI agents are part of the group. From here, you can open a specific
   AI agent to view its settings.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_messaging_connect_ai_agents_in_group.png)

## Managing messaging channel settings for an advanced AI agent

You can manage settings that affect how an advanced AI agent behaves on messaging
channels, including:

- The Support group that an AI agent transfers a ticket to when it’s escalated to
  a human agent.
- The avatar the AI agent uses in conversations with a customer.
- Whether the AI agent’s messages can use HTML and Markdown formatting.

Configuring these settings affects only the individual AI agent, not the whole
messaging group it belongs to.

Note: To manage which channels an advanced AI agent is
connected to, see [Setting an advanced AI agent as the default
responder for a messaging channel](https://support.zendesk.com/hc/en-us/articles/8357757911834).

**To manage messaging channel settings for an advanced AI agent**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. Click **Messaging settings**.

   The AI agent settings panel
   opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_messaging_connect_settings.png)
4. In **Transfer group**, select the agent group in Support that the AI
   agent should send escalated tickets to.
5. In **Avatar URL**, enter the URL of an image to be used as the AI agent’s
   avatar within a conversation.

   The avatar must be a JPG, PNG, or GIF
   format.
6. (Optional) Deselect **Activate rich messaging** if you don’t want HTML
   and Markdown formatting to apply in [AI agent message blocks in the dialogue
   builder](https://support.zendesk.com/hc/en-us/articles/8357749494810#topic_krz_vym_g2c).

   For more information, see [About rich-text formatting in
   messaging conversations](https://support.zendesk.com/hc/en-us/articles/9017484189466).
7. Click **Save**.

## Connecting an advanced AI agent to a different subdomain

If you have a [sandbox environment](https://support.zendesk.com/hc/en-us/articles/6150628316058), you might need to switch the AI
agent’s messaging connection from your sandbox subdomain to your production
subdomain, or vice versa.

Note: Changing which subdomain an advanced AI agent is
connected to affects all AI agents in the messaging group, not just the one you
update. To see which AI agents will be affected, you can view all AI agents in
the group.

Additionally, changing the subdomain disconnects the AI agents from all messaging
channels, routing rules, and structured message templates.

**To change an advanced AI agent’s authorized subdomain**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. On the General tab, click **Choose subdomain**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_messaging_switching_subdomain.png)
4. Select the subdomain you want to authorize the AI agent for.