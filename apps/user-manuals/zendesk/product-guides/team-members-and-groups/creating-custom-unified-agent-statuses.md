# Creating custom unified agent statuses

Source: https://support.zendesk.com/hc/en-us/articles/4410525357594-Creating-custom-unified-agent-statuses

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Verified AI summary ◀▼

Create custom unified agent statuses to manage availability across email, voice, and messaging channels. This feature allows you to define statuses that fit your team's workflow, with options to set availability for specific groups. Customize statuses to control agent presence and streamline omnichannel routing, ensuring that agents are available when needed and offline when not. This feature is available on Professional and Enterprise plans.

Location:  Admin Center > Objects and rules > Omnichannel routing > Agent statuses

Note: This feature has the following plan restrictions:

- Team and Growth don't support custom unified statuses.
- Professional supports up to five custom unified statuses.

  For
  customers who purchased individual plans for email, chat, and voice
  support, each of your product subscriptions must be on Professional
  plans or above to use this
  feature.
- Enterprise supports up to 100 custom unified statuses.

Unified agent status is part of [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) and allows agents to control
availability for email, voice, and messaging from a single menu. There are four default
agent statuses: online, away, transfers only, and offline, as well as a customizable
[fallback status that's used when agents are
idle](https://support.zendesk.com/hc/en-us/articles/5286614817562).

If you meet the [requirements](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_zlk_c3p_m5b) to use unified agent statuses and
are on a Professional or Enterprise plan, admins can also define custom unified statuses
to suit their workflows. When defining custom agent statuses, you can choose whether
it's available to all agents in your account or only select [groups](https://support.zendesk.com/hc/en-us/articles/4408894175130) of agents.

**To add a custom agent status**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Omnichannel routing > Agent
   statuses**.
2. On the Agent statuses page, click **Create agent status**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocr_agent_status_list.png)
3. On the **Create agent status** page, configure the following:
   1. **Name**: Give the new status a short, unique name. The name
      can't exceed 100 characters. [Dynamic content is supported](https://support.zendesk.com/hc/en-us/articles/5360039903898) if
      you want the status to be displayed in the agent's local language.
   2. **Description**: Optionally, give the new status a description
      that helps you identify it.
   3. **Channel routing > Email**: Define the agent's availability
      for incoming [email tickets (including web form, side
      conversations, and API)](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb) when this custom status is active.
   4. **Channel routing > Talk:** Define the agent’s availability for
      incoming calls when this custom status is active.
   5. **Channel routing > Messaging**: Define the agent's
      availability for incoming Messaging conversations when this custom status is
      active.

   The **Status** section shows a preview of how your agent’s icons will
   look depending on the selected status.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocr_custom_status_icon_preview.png)
4. Under **Groups**, select one of the following options:
   - **All groups**: Makes the custom status available to all agents in your
     account.
   - **Only selected groups**. Restricts access to only the groups you select
     in the accompanying drop-down field.

   Note: Custom statuses created prior to June 10, 2024 are available to all
   groups unless an admin [edits the status](https://support.zendesk.com/hc/en-us/articles/5133588225690) to restrict access by
   group. After this date, admins must specify group accessibility for each status
   they create.

   If an agent is removed from a group while using a
   restricted status, their [idle and disconnect statuses](https://support.zendesk.com/hc/en-us/articles/5286614817562) fallback
   to *Offline* rather than the configured idle and disconnect statuses.
5. When you are finished, click **Create agent status**.