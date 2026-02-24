# Turning on similar tickets

Source: https://support.zendesk.com/hc/en-us/articles/8036381366426-Turning-on-similar-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

The similar tickets feature helps you find related tickets to the one you're working on, using AI to identify matches based on keywords, intent, and entities. This feature supports multiple channels, except live chat and voice. Admins can enable or disable it and control group access. Use it to quickly access past solutions and enhance your response effectiveness.

The similar tickets feature lets agents see a list of similar tickets to the ticket
they’re currently working on. By seeing how similar issues were addressed, agents are
able to solve tickets more efficiently.

This article contains the following topics:

- [About similar tickets](#topic_vlg_33v_xyb)
- [Turning similar tickets on or off](#topic_yfj_rwd_kbc)

Related articles:

- [Finding tickets similar to the current
  ticket](https://support.zendesk.com/hc/en-us/articles/6154115110170)

## About similar tickets

Similar tickets uses generative AI to identify tickets that are considered similar to
the one the agent is currently working on. Similar tickets [appear in the Agent Workspace](https://support.zendesk.com/hc/en-us/articles/6154115110170).

The similar tickets feature supports tickets created across all channels except for
live chat, native messaging, social messaging, and voice channels. Additionally, the
feature works with the languages listed [here](https://support.zendesk.com/hc/en-us/articles/4408821324826#h_01K20KZB81EQ78Y0QKD2P1G2S4).

To be considered similar, tickets must:

- Be in the same brand.
- Be in a status of Solved or Closed.
- Share a significant number of keywords.

If these conditions aren’t met:

- In the Agent Workspace search bar, no **Similar tickets** header
  appears.
- In Related tickets in the context panel, no tickets appear in the **Similar
  resolved tickets** list.

Additionally, to increase the relevance of similar tickets, the system considers the
following additional factors:

- **Intent matching**: Similar ticket candidates with a high-confidence [intent](https://support.zendesk.com/hc/en-us/articles/4550640560538) match to the base ticket
  receive a score boost. This prioritizes alignment with the “why” behind the
  ticket (for example, refund request).
- **Entity matching**: Similar ticket candidates with matching [entities](https://support.zendesk.com/hc/en-us/articles/6711181959194) to the base ticket receive a
  score boost. This prioritizes alignment with the “what” of the ticket (for
  example, iPhone 15).
- **Time decay**: Recent similar tickets are prioritized over older ones,
  ensuring recommendations remain timely and relevant.

For example, say a user opens a ticket to upgrade their current subscription to a
higher-tier plan (called "Premium"). If there’s a high-confidence "Upgrade
subscription" intent and a defined entity for "Premium," agents can quickly access
similar tickets that share the same intent and entity. This allows them to
understand previous upgrade processes, review terms offered to other users, and
ensure a smooth transition for the user.

## Turning similar tickets on or off

Admins can turn similar tickets on or off in Admin Center and choose which groups
have access. By default, this feature is turned on.

**To turn similar tickets on or off**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Agent copilot > Suggestions**.
2. Select **Show similar tickets**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_similar_tickets_groups.png)
3. In the **Who has access** field, search for and select the groups that
   should be able to use the similar tickets feature. By default, all groups
   have access.
4. Click **Save**.