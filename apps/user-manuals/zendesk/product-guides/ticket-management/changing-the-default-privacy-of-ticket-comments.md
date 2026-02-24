# Changing the default privacy of ticket comments 

Source: https://support.zendesk.com/hc/en-us/articles/4408822560410-Changing-the-default-privacy-of-ticket-comments

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Learn how to change the default privacy of ticket comments to private, ensuring internal notes are not visible to customers. This feature helps maintain confidentiality and control over ticket information. Additionally, you can restrict agent access to private comments on tickets they request, enhancing privacy for sensitive information. Customize these settings to align with your team's workflow and privacy needs.

Location: Admin Center > Objects and rules > Tickets >
Settings

Your agents reply to customer tickets by adding comments to them. They can do this either through the Zendesk Support web interface, or by responding to the ticket using email or another messaging channel.

This article includes these sections:

- [About public and private comments](#topic_xwn_pcm_x4b)
- [Making agent comments private by default](#topic_k3f_q1f_hlb)
- [Restricting agent access on tickets where they're the requester (Enterprise only)](#topic_km4_33s_dzb)

## About public and private comments

You can configure ticket comments in one of two ways:

- **Public:** Ticket comments can be seen by the customer. Public comments are written on the **Public reply** (or messaging channel) of the ticket comments field. For example, here's where agents can add public replies from the ticket interface

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/comment_public_reply.png)
- **Private:** In general, private comments (known as *internal notes*) can be seen by agents, but cannot be seen by the customer. These are great for discussing tickets internally with your team without having to involve the customer. However, on Enterprise plans, admins can [configure agent access to private comments](https://support.zendesk.com/hc/en-us/articles/4408822560410#topic_km4_33s_dzb) and agent-only fields on tickets they request. For example, here's where agents can add private comments from the ticket interface:

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_comments_internal2.png)

## Making agent comments private by default

By default, when an agent adds a comment, the comment becomes public. For example, if the agent wants to add a private comment to the ticket from the ticket interface, they must first select **Internal note**. If they forget, the customer will see what they write.

Note: There’s one exception to the **Public by default** setting. Tickets that only have internal notes and no public comments will always default to internal notes, even if the setting is turned on.

If you prefer, you can configure ticket comments from agents to be private by default. Then, when an agent adds a comment from the ticket interface, they will need to select a public channel (such as email) instead of an **Internal note** if they want the customer to see the comment.

If CCs are enabled, you can also change the default comment privacy for end user CCs. See [Configuring CC and follower permissions](https://support.zendesk.com/hc/en-us/articles/4408843795482).

Settings to make agent comments private by default do not apply to channels that are considered *live*, including chat, messaging, and social media. See [About channel switching logic in the ticket composer](https://support.zendesk.com/hc/en-us/articles/5924725590682).

**To configure private ticket comments as the default**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Comment options for agents** to expand it.
3. Deselect both these options: **Set composer to public channel by default** and **Allow agent comments via email to be public by default**.

   If the Zendesk Agent Workspace is not [turned on](https://support.zendesk.com/hc/en-us/articles/4408834058010) in your account, the option names vary slightly.
   Deselect both these options: **Allow agent comments by web to be public by default** and **Allow agent comments via email to be public by default**.

Note: For information about comment privacy when email replies are involved, see [Understanding when email replies become public or private comments](https://support.zendesk.com/hc/en-us/articles/4408842992538).

## Restricting agent access on tickets where they're the requester (Enterprise only)

Admins can configure the visibility of private comments on tickets where an agent is the requester, regardless of the tickets' group assignments.

If you restrict agents in your account from seeing internal notes and agent-only fields, they won't be able to access the tickets in Support where they're the requester. Instead, they can use their email or your [help center's customer portal](https://support.zendesk.com/hc/en-us/articles/4408846805530#topic_qgd_mqd_yy) to access tickets where they're the requester.

Consider the following before updating your agent as requester settings:

- For agents to manage their requested tickets in your help center, you must [activate your help center](https://support.zendesk.com/hc/en-us/articles/4408846795674#topic_ckn_wc4_qy) and [enable agents to access request forms](https://support.zendesk.com/hc/en-us/articles/4408828251930).
- If agents submit tickets to brands they don't belong to, consider the agents' visibility to those tickets in your help center's customer portal. You can [update your configuration](https://support.zendesk.com/hc/en-us/articles/9319604460826) to give agents visibility across brands.

**To restrict agent access to tickets they submit as the requester**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Agent interface**.
2. Under **Agent is the requester**, choose the level of access you want agents to have to internal notes on tickets where they're the requester:
   - **Show all internal notes**: No restrictions. Agents can view internal notes on tickets where they're the requester, regardless of group assignment. This applies to tickets in Support only; internal notes aren't visible on their requested tickets in your help center.
   - **Hide internal notes on tickets assigned to private groups**
     - Agent access to internal notes on tickets where they're the requester is restricted if the tickets are assigned to a [private ticket group](https://support.zendesk.com/hc/en-us/articles/4988173561370) or brand they don't belong to. In this case, the agent's internal notes become public.
     - If the agent is the requester and the ticket is assigned to a private ticket group or brand they don't belong to, the agent loses access to the ticket in the Agent Workspace. They can access it in your help center under My Requests, since the system now treats them as an end user for that ticket.
     - Agents in [custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882)
       with access to all tickets can still view internal notes on tickets where they're the requester, even when this option is selected.
   - **Hide all internal notes**:
     - Agent access to internal notes on tickets where they're the requester is restricted if the tickets are assigned to a private ticket group, public ticket group, or brand the agent doesn't belong to. In this case, the agent's internal notes become public.
     - If the agent is the requester and the ticket is assigned to a private group, public ticket group, or brand they don't belong to, the agent loses access to the ticket in the Agent Workspace.
       They can access it in your help center under My Requests, since the system now treats them as an end user for that ticket.
     - Agents in [custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882)
       with access to all tickets can still view internal notes on tickets where they're the requester, even when this option is selected.
3. Click **Save**.