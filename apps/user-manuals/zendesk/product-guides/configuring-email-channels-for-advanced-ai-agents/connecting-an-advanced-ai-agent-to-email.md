# Connecting an advanced AI agent to email

Source: https://support.zendesk.com/hc/en-us/articles/8357750858010-Connecting-an-advanced-AI-agent-to-email

---

After youcreate an advanced AI agent, you need to connect it to Zendesk Support before the AI agent can begin responding to customers by email. Email responses sent by the AI agent are sent as thesystemuser, meaning no agent seat is required for an advanced email AI agent.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

After you [create an advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357749415066), you need to connect it to
Zendesk Support before the AI agent can begin responding to customers by email. Email
responses sent by the AI agent are sent as the *system* user, meaning no agent seat is
required for an advanced email AI agent.

Note: When you created your AI agent, you must have selected a channel
type of email. If you selected messaging, see [Setting an advanced AI agent as the default responder for a messaging
channel](https://support.zendesk.com/hc/en-us/articles/8357757911834) instead.

You should connect only one advanced AI agent to email. For advice on how to handle
brand-specific information within a single AI agent, see [Can I connect multiple advanced AI agents to a single Zendesk
account?](https://support.zendesk.com/hc/en-us/articles/9828611484826)

This article covers the following topics:

- [Connecting an advanced AI agent to your subdomain](#topic_sp2_3sk_m2c)
- [Creating the automation trigger and turning on the automation engine](#topic_j5r_psk_m2c)
- [Disconnecting an advanced AI agent from email](#topic_jm3_qsk_m2c)

## Connecting an advanced AI agent to your subdomain

The first step in connecting an advanced AI agent to email is to connect to your production
or sandbox environment.

**To connect an AI agent to your subdomain**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. Click **Select your CRM** and select **Zendesk Support**.
4. Select the **Integration** tab.
5. Click **Choose subdomain** and select the subdomain for either your production or
   sandbox environment.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_email_ai_agent_choose_subdomain.png)
6. In the confirmation dialog, click **Continue**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_email_ai_agent_continue_subdomain.png)

## Creating the automation trigger and turning on the automation engine

After you connect to your subdomain, you need to create the automation trigger and turn on
the automation engine. This allows the advanced AI agent to send replies to customer
requests on the email channel.

Important: If you set up the automation trigger, any
replies made by human agents during conversations in which the email AI agent also
participated don't appear in the [conversation logs](https://support.zendesk.com/hc/en-us/articles/8357749580186). As a result, [automated resolutions](https://support.zendesk.com/hc/en-us/articles/5352026794010) might be consumed for conversations they
shouldn't be.

**To create the automation trigger and turn on the automation engine**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. Select the **Integration** tab.
4. Click **Create automation trigger**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_connecting_email_create_trigger.png)

   The trigger is automatically created.
   You can view the details of the JSON in a read-only text window, and [edit the trigger](https://support.zendesk.com/hc/en-us/articles/9985221852954#topic_ahn_kgt_khc) if needed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_connecting_email_create_trigger_default.png)
5. Select the **Overview** tab.
6. Select **Automation engine** to toggle it on.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_connecting_email_automation_engine.png)

Your AI agent is now connected to email. At this point, you may want to:

- [Manage the automation trigger](https://support.zendesk.com/hc/en-us/articles/9985221852954) to reorder it in your list of
  triggers or edit its default configuration.
- [Import ticket data](https://support.zendesk.com/hc/en-us/articles/8357758714906) to populate the AI agent’s conversation logs
  with historical data from Zendesk Support.

## Disconnecting an advanced AI agent from email

If you no longer want an AI agent to be connected to email, you can turn off the automation
engine and deactivate the trigger.

**To disconnect an advanced AI agent from email**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. Select the **Overview** tab.
4. Select **Automation engine** to toggle it off.
5. In the confirmation dialog, select **Turn off**.

   At this point, the AI agent is
   still technically connected to the email channel, but it won’t respond to customer
   requests.
6. Select the **Integration** tab.
7. Click **Deactivate automation trigger**.
8. (Optional) Select the **Overview** tab again, click **Remove integration**, and
   then click **Confirm** in the confirmation dialog.

Your AI agent is no longer connected to email.