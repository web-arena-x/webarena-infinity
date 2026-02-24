# Zendesk call recording FAQ

Source: https://support.zendesk.com/hc/en-us/articles/4408828042010-Zendesk-call-recording-FAQ

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

Below are some frequently asked questions and answers about call recording in Zendesk. For more
information about configuring call recording, see [Managing call recording options](https://support.zendesk.com/hc/en-us/articles/4408831738266).

Important: You are responsible for using the recording features in Zendesk in
compliance with all applicable laws. Certain jurisdictions may require End-User and/or Agent
consent prior to initiating a recording. By enabling call recording, you agree that you have
received such consent.

This article contains the following sections:

- [Call recording basics](#topic_ns3_dnh_2db)
- [Recording storage](#topic_dcg_3ph_2db)
- [Call recording access and security](#topic_lds_hyh_2db)

## Call recording basics

### How can I turn off call recordings?

You can only turn off call recording for individual phone numbers, not all phone numbers
at the same time. This includes both outgoing and received calls for the phone number. To
learn how to disable call recordings, see [Managing call recording options](https://support.zendesk.com/hc/en-us/articles/4408831738266).

### What calls and parts of calls are recorded?

The parts of calls recorded include:

- Calls answered by an agent via the web browser or on an agent forwarding number
- Calls transferred to an external phone number by an agent
- Voicemails

The parts of calls not recorded include:

- On-hold time and time in queue
- Consultation time before transferring a call to another agent
- A call routed to IVR that then directs the call to a external phone number

Note: The length of a call recording will differ from the length of the overall phone call.
The phone call length includes both recorded and non-recorded events.

### Are call recordings transcribed?

Call transcription is included as part of the [Copilot](https://support.zendesk.com/hc/en-us/articles/5524125586330) and [Zendesk QA](https://www.zendesk.com/service/quality-assurance/) add-ons, in addition to call summarization.

- **Copilot add-on** 

  Call transcripts and summaries are added to the
  conversation log on tickets in the Agent Workspace. Transcripts and summaries provide
  additional context to voice tickets and reduce the requirement for agents to take
  notes and summarize calls as part of their wrap-up activities.
- **Zendesk QA add-on**

  Call transcripts and summaries appear in Zendesk
  QA where QA focused users can review and analyze historical call interactions in
  detail. Voice QA evaluates the call transcript and provides a QA Score just like it
  does for chat or messaging conversations which can be used to identify the
  conversations where there’s a churn risk or an agent knowledge gap.

For more information regarding call transcription, see [Call transcription and summarization FAQs](https://support.zendesk.com/hc/en-us/articles/7470764710298).

### Are call recordings stored in mono or stereo format?

All call recordings are stored in mono format.

## Recording storage

### Where are call recordings stored?

Call recordings are encrypted at rest and initially stored in our voice provider Twilio's
data center. Recordings are then copied to a Zendesk data center hosted by Amazon Web
Services. You can store call recordings in the US, EEA, or Australia, as per the [Zendesk Regional Data Hosting policy](https://support.zendesk.com/hc/en-us/articles/4408883599130).

### Can I delete recordings?

Recordings can be deleted either manually from individual tickets or automatically based
on a set time limit. Deleted recordings cannot be recovered. If you select to
automatically delete recordings, voicemail transcriptions will still remain in the
associated tickets. When you select to automatically delete recordings, the schedule will
apply retroactively and delete recordings.

### How long are call recordings stored?

There is no time limit for how long call recordings are stored. You can either select to
manually delete recordings or to automatically delete them after a set time range. For
help deleting recordings, see [Deleting recordings](https://support.zendesk.com/hc/en-us/articles/4408831738266#topic_w2x_hzc_yt).

## Call recording access and security

### Who can access call recordings?

Any agent with permission to access tickets can access call recordings. You can permit
end-users to access live recordings in their requested tickets by enabling the **New live
call recordings are public?** setting in the **Settings** tab (In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
**Channels** in the sidebar, then select **Talk and email > Talk**.)

For details, see [Enabling the voice channel and configuring general
settings](https://support.zendesk.com/hc/en-us/articles/4408838035866).

### Can I pause call recordings?

If you're on the Professional or Enterprise plan you can use the pause and resume button
in the ticket bar and the call console. For more information, see [Pausing and resuming call recordings with agent recording
controls](https://support.zendesk.com/hc/en-us/articles/4408820271002).

If you're on a different plan, you might be able to use apps available in the Marketplace
like [Intelligent Voice](https://www.zendesk.com/apps/support/intelligent-voice-pci-redaction/?source=app_directory) and [Voicebase](https://www.zendesk.com/apps/support/voicebase-pci-call-redaction/) to automatically detect and redact credit card data
from call recordings.

### Can callers opt-in or opt-out of call recording?

If you're on the Professional or Enterprise plan you can configure opt-in or opt-out for
each of your Zendesk phone numbers. You can find the call recording opt-in or opt-out
settings on the Call recording tab for each phone numbers. For more information, see [Understanding call recording permissions (opt-in and
opt-out)](https://support.zendesk.com/hc/en-us/articles/4408838605210).

### Are end users notified when calls are being recorded?

The default greeting notifies end-users that they will be recorded; however, if you use a
custom greeting, you will need to indicate that calls might be recorded. For outbound
calls, your agents will need to inform end-users as part of their introduction.

When call recording is turned on, the caller will hear a beep indicating that the
recording has started and the call is being recorded. This behavior is standard for all
calls regardless of the country the caller is in.