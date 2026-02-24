# Activating the voice channel and configuring general settings

Source: https://support.zendesk.com/hc/en-us/articles/4408838035866-Activating-the-voice-channel-and-configuring-general-settings

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

This article describes how to activate the voice channel and configure general settings. Be sure
to read [Preparing to offer voice support](https://support.zendesk.com/hc/en-us/articles/4408827987482) first to
ensure your hardware and network are ready.

This article contains the following topics

- [Activating the voice
  channel](#topic_sns_3x1_2hb)
- [Voice channel general
  settings](#topic_w1l_j14_5fb)
- [Re-activating the voice
  channel](#topic_qdx_xd4_hyb)
- [Next steps](#topic_lfg_phr_v2b)

## Activating the voice channel

Before you can start using the voice channel, you need to turn it on, then configure
some settings that will apply to all of your calls.

**To activate the voice channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. On the welcome page, click **Get Started**.
3. On the **Your number** page, review your assigned number, then click
   **Next**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Talk_suite_number_1.png)

   You can purchase additional numbers or port an existing number
   later, if you want to. If you are on a trial version you can use the
   assigned number only or [add a digital line](https://support.zendesk.com/hc/en-us/articles/1260805715389).

   Note: If you see a list of numbers on this page, you can choose a number
   from the list, change the country or number type, or search for a
   specific number if you'd like.
4. On the **Who will answer the calls** page, select which agents can handle
   calls. You can choose from:
   - **Everyone:** Any agent
   - **Only Me:** Only you
   - **Specific Users:** A new page opens on which you can choose the
     agents who will have access
5. Click **Next**.
6. On the **Let's try your new number** page, follow the on-screen steps to
   simulate a call or click **Skip this step**.
7. If you simulated a call, click **Check out the ticket** to access the ticket
   created from the call or click **Finish**.
8. Configure [general settings](https://support.zendesk.com/hc/en-us/articles/4408838035866#topic_w1l_j14_5fb) as needed, then click
   **Save**.

## Voice channel general settings

On the Settings tab, configure the general settings to your requirements. For
information about the other settings you can configure, see [Configuring voice channel settings](https://support.zendesk.com/hc/en-us/articles/4576052164762).

| Setting | Description |
| --- | --- |
| **Enable Talk** | Select to activate the voice channel. |
| **Maximum queue size** | Your call queue size determines how many incoming calls will be kept waiting for an available agent, whether on hold or in the callback queue, before being sent to voicemail (or an overflow number if it's configured and voicemail is off). You can select from a range of queue sizes, including **0**, **2**, **5**, **10**, or **15**. If you use Professional or Enterprise, you can also select additional queue sizes up to **1,500**.  If you need a larger queue size, [contact us](https://support.zendesk.com/hc/en-us/articles/4408843597850) with your use case, and we'll evaluate your request (Professional and Enterprise plans only).  A maximum queue size of 0 prevents end users from submitting a callback request in the Web Widget (Classic). |
| **Maximum queue wait time** | Callers who wait longer than the time specified in the maximum queue wait time are sent to voicemail. Callers can dial 1 at any time to go straight to voicemail (if on). If voicemail is off, the caller will hear a greeting, then the call will end. Maximum queue wait time is ignored after a call is transferred.  The maximum queue wait time takes precedence over the **Call offering time limit** setting. You can select from a range of wait times between **1** and **20** minutes (or **1** and **60** minutes if you are on an Enterprise plan). If you need a longer wait time, [contact us](https://support.zendesk.com/hc/en-us/articles/4408843597850) with your use case, and we'll evaluate your request (Professional and Enterprise plans only). |
| **New live call recordings are public?** | Selecting this option allows the requester to access recordings from live calls that are added to tickets. For more information, see [Managing call recording options](https://support.zendesk.com/hc/en-us/articles/4408831738266-zug-voice-recording-NEW-Managing-recording-options-in-Voice). |
| **Agent confirmation when forwarding?** | When agents forward calls to their phones, this option requires agents to press a key before the call is connected to indicate that a person is answering the call and not an automated voicemail. This prevents calls from forwarding to an agent's personal voicemail if they do not answer. Forwarded calls not answered with a key confirmation are routed to voicemail and recorded in a ticket.  If your agents forward calls to a phone system where personal voicemail boxes are not an issue, you can disable this option so that agents are immediately connected to callers when they answer. |
| **Transcribe and summarize call recordings on tickets** | For calls that are recorded, you can help your agents with auto generated transcripts and summaries. To configure this and associated options, see [Using generative AI to create call summaries and transcripts on tickets](https://support.zendesk.com/hc/en-us/articles/6170157307162). |
| **Transcribe and summarize call recordings for Zendesk QA** | Select to send call transcripts and summaries to Zendesk QA so that reviewers don't have to listen to entire recordings to evaluate calls. See [Activating Voice QA](https://support.zendesk.com/hc/en-us/articles/8536077648538). |

## Re-activating the voice channel

Deactivated accounts do not display the call icon, as the setting is turned off by
default when the account is deactivated.

1. On the sidebar, click **Text & Talk**.
2. Open the **Summary** tab.
3. In the **Summary** table, find the account you want to reactivate, then
   click **Activate**.

   The call icon will now appear for agents who have
   access.

## Next steps

- [Adding Zendesk phone numbers](https://support.zendesk.com/hc/en-us/articles/4408824192026)
- [Configuring voicemail options](configuring-voicemail-options.md)