# Managing messaging transcript visibility

Source: https://support.zendesk.com/hc/en-us/articles/4408818625690-Managing-messaging-transcript-visibility

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Verified AI summary ◀▼

Manage how agents and end users access messaging conversation transcripts. Allow end users to download transcripts via the Web Widget. Configure agents to add transcripts to tickets as public replies or internal notes, controlling visibility. These settings help you streamline communication and maintain control over transcript access.

In Admin Center, you can manage how agents can add transcripts of messaging conversations
to tickets, and whether they can be viewed by end users. You can also give end users
permission to download conversation transcripts themselves in the Web Widget.

This article includes the following topics:

- [Allowing end users to download messaging conversation transcripts](#topic_fs1_21v_13c)
- [Managing messaging conversation transcripts in tickets](#topic_cm3_21v_13c)

## Allowing end users to download messaging conversation transcripts

You can choose to make messaging conversation transcripts available for download in
the Web Widget. When this feature is turned on, end users can download transcripts
without agent assistance from the Options menu.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/download_transcript_menu.png)

This setting is applied to all messaging Web Widgets on your account.

You can download transcripts from messaging conversations with AI or human agents.
However, for AI agent-only transcripts:

- [AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346) must be turned
  on.
- The [AI agent greeting message](https://support.zendesk.com/hc/en-us/articles/8774095741466#topic_z34_zcd_f2c) may not
  appear in the downloaded transcript.

**To allow messaging transcript downloads**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click **Messaging settings**.
3. Under Advanced, expand the **Downloading transcripts**
   section.
4. Select **End users can download a transcript of the conversation**.
   Deselect this option to prevent transcript downloads.
5. Click **Save settings**.

## Managing messaging conversation transcripts in tickets

Agents can add messaging conversation transcripts to tickets if needed. You can
configure how conversation transcripts are added to the ticket.

There are two ways transcripts can be added to a ticket:

- **As public reply** (default setting) adds the transcript to the ticket
  history as a public reply, which is visible to ticket requesters and any other
  end users CCed on a ticket. Transcripts are included in email notifications and
  within the ticket when viewed in the help center. This setting also allows you
  to [use ticket APIs to fetch conversation data](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/).
- **As internal note** adds the transcript to the [ticket events](https://support.zendesk.com/hc/en-us/articles/4408829602970) as an internal note,
  which is visible only to agents.

**To configure transcript visibility**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.

   Note: For older accounts, transcript visibility is managed in the Chat
   dashboard. From the Chat dashboard, select **Settings > Account >
   Zendesk Support tab**.
2. Click **Comment options for agents** to expand it.
3. Under **Select how transcript will be added to the ticket**, select **As a
   public reply** or **As an internal note**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_transcript_visibility_ac2.png)
4. Click **Save**.