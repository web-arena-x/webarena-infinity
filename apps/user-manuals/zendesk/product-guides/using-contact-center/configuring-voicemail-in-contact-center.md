# Configuring voicemail in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/10255333454490-Configuring-voicemail-in-Contact-Center

---

Voicemail in Zendesk Contact Center captures caller messages and delivers them as Zendesk tickets with audio playback and optional transcription. Settings are configured in the admin interface and applied at runtime in Amazon Connect contact flows.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Voicemail in Zendesk Contact Center captures caller messages and delivers them as Zendesk
tickets with audio playback and optional transcription. Settings are configured in the
admin interface and applied at runtime in Amazon Connect contact flows.

You can configure voicemail for inbound calls to reduce missed calls and create clear
ownership when agents or queues are unavailable. Voicemail can be configured per queue
or per agent using direct inward dialing (DID) or extension numbers. You can also
control how voicemail tickets are created in Zendesk, and optionally include
transcriptions.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_voicemail_list.png)

Admins can access voicemail settings in the Zendesk for Contact Center admin
interface. If you can't access the settings, then contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to request the activation of the
Voicemail solution on your CloudFormation stack.

This article contains the following topics:

- [Understanding voicemail in Contact Center](#topic_understanding_voicemail_cc)
- [Configuring queue-based voicemail](#topic_queue_based_voicemail)
- [Configuring user-based voicemail](#topic_user_based_voicemail)

## Understanding voicemail in Contact Center

There are two ways to deliver voicemail, depending on whether messages should be
worked by a shared team or by a specific agent:

- **Contact Center queue-based voicemail**: Voicemails are delivered to a
  Zendesk group associated with an Amazon Connect queue. Use this for shared
  contact center queues.
- **User-based voicemail**: Voicemails are delivered to a specific agent
  workflow. You’ll select the agent who owns the direct back office number (DID
  owner) or extension and the agent who should be assigned the resulting ticket.
  This can be the same person or different people.

Voicemail tickets include caller details, call metadata, an audio recording with
playback, and, (if activated) a transcription. They behave like standard Zendesk
tickets, so you can use existing views, triggers, automations, and reporting.

## Configuring queue-based voicemail

Use a queue-based voicemail configuration when callers should leave messages for a
shared team. Voicemails are delivered to a Zendesk group associated with an Amazon
Connect queue.

**To configure queue-based voicemail**

1. In [Contact Center](https://support.zendesk.com/hc/en-us/articles/9696121449114), click **Admin
   Settings**.
2. Click the settings icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_cogs_icon.png)) in the sidebar.
3. Click the **Voicemail** tab at the top to open voicemail settings.
4. Under **Contact Center**, click **Add new configuration**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_voicemail_queue_add.png)
5. Under **Origin queue**, select the Amazon Connect queue this voicemail
   configuration applies to.
6. Select the **Zendesk assignable group** to which newly created voicemail
   tickets will be assigned.
7. Under **Zendesk Tags**, select one or more ticket tags to add to these
   voicemail tickets.

   These tags can be used for routing, automation, and
   reporting.
8. (Optional) Select **Enable transcription** to include an automated
   voicemail transcription in the tickets.
9. Click **Add configuration**.

Tip: Use ticket tags and triggers to automatically route voicemail tickets
to the correct groups.

## Configuring user-based voicemail

Use a user-based (or agent-based) voicemail configuration to assign tickets resulting
from missed calls to an agent’s direct number to a specific agent for follow-up. The
DID owner and the ticket assignee can be the same agent, buto don't have to be.

**To configure user-based voicemail**

1. In [Contact Center](https://support.zendesk.com/hc/en-us/articles/9696121449114), click **Admin
   Settings**.
2. Click the settings icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_cogs_icon.png)) in the sidebar.
3. Click the **Voicemail** tab at the top to open the voicemail
   settings.
4. Click the **Back Office** tab and then click **Add new
   configuration**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_voicemail_agent_add.png)
5. Under **User**, select the agent who owns the direct number this
   voicemail configuration applies to.

   This is the DID owner. To add user
   entries, see [Configuring number assignments and
   voicemail for direct agent routing](https://support.zendesk.com/hc/en-us/articles/10255377209498).
6. Under **Zendesk assignee agent**, select the Zendesk agent to assign
   the voicemail tickets created from calls to this DID.
7. Under **Zendesk tags**, select one or more ticket tags to add to these
   voicemail tickets.

   These tags can be used for routing, automation, and reporting.
8. (Optional) Select **Enable transcription** to include an automated
   voicemail transcription in the tickets.
9. Click **Add configuration**.