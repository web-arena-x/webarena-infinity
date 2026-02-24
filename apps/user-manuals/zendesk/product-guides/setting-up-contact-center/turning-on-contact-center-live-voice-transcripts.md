# Turning on Contact Center live voice transcripts

Source: https://support.zendesk.com/hc/en-us/articles/9696174623770-Turning-on-Contact-Center-live-voice-transcripts

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Enable live voice transcripts to view real-time transcriptions of voice interactions using AWS Contact Lens. Ensure your CloudFormation Stack is version 5.46.0 or later. Activate Contact Lens and enable real-time analytics in its settings. Adjust the workflow settings to include real-time voice transcripts. This feature enhances your ability to monitor and respond to customer interactions effectively.

When on a voice contact, Zendesk for Contact Center can display a live
transcript of the interaction. Contact Center utilises AWS Contact Lens to perform
transcription.

**To turn on live voice transcripts**

In order to use live voice transcripts your CloudFormation Stack must be
v5.46.0 (or later).

1. Ensure that Contact Lens is turned on by following [these instructions](https://docs.aws.amazon.com/connect/latest/adminguide/enable-analytics.html).
2. Within the Contact Lens settings, turn on the **Real-time and post-call
   analytics** option.
3. On the Settings page, select the Workflows tab.
4. Select the relevant workflow and click **Edit workflow**.
5. Scroll down to the **Voice Transcripts** section.
6. Select the **Real-time** option.
7. Click **Save workflow**.