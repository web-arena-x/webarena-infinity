# Using Zendesk QA for call transcriptions in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9475134529050-Using-Zendesk-QA-for-call-transcriptions-in-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Use QA for call transcriptions to generate transcripts and summaries from call recordings in Contact Center. This feature requires specific configurations, including CloudFormation stack version 6.29.0 and call recording in Amazon Connect. Note that transcripts are created post-call, without real-time capabilities or audio redaction. For real-time transcription and redaction, use Contact Lens alongside QA.

If your Zendesk account includes Zendesk QA, you can use it to generate call transcriptions and summaries from the call recordings that are stored in the Zendesk ticket from Contact Center.

If you require both real-time transcription and post-call quality management then you need to use Contact Lens as well as Zendesk QA.

Important: When using both Contact Lens and Zendesk QA, you’ll be charged by Amazon and Zendesk for the transcriptions. For more details on Zendesk charges, see [Call transcription charges](../managing-your-voice-channel/call-transcription-and-summarization-faq.md#:~:text=How%20are%20call%20transcriptions%20priced%3F).

The article contains the following sections:

- [Requirements for using Zendesk QA for call transcriptions](#topic_qzv_vnm_yfc)
- [Understanding call transcription using Zendesk QA without Contact Lens](#topic_hyw_wnm_yfc)

## Requirements for using Zendesk QA for call transcriptions

To use Zendesk QA for call transcriptions, you must meet the following requirements:

- CloudFormation stack version 6.29.0 is required.
- The Call Recording and Analytics flow block must be added to all relevant contact flows.
- Call recording must be enabled in Amazon Connect.
- Zendesk QA must be licensed and configured to use the help desk connection so that Zendesk QA has access to ticket data. To configure the connection, see [Managing help desk connections in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043712839450).

## Understanding call transcription using Zendesk QA without Contact Lens

When Amazon Connect records a voice call, the resulting audio file can be attached to the corresponding Zendesk ticket. If your team is using Zendesk QA, transcripts can be generated after the call has ended using the audio recording, without Contact Lens.

Consider the following points, if you are using Zendesk QA and not using Contact Lens for call transcription:

- Call transcription occurs after the call is completed.
- Call transcription does not occur prior to attaching the call recording to a Zendesk ticket, so any agents with access to the ticket can access the unredacted call recording.
- Transcripts are based on the recorded audio file from Amazon Connect.
- Transcription and analysis are fully integrated into the Zendesk environment.
- Personally Identifiable Information (PII) and Payment Card Industry (PCI) data is not redacted from call recording audio files. You need to [delete call recording files](https://support.zendesk.com/hc/en-us/articles/4408828042010-Zendesk-Talk-call-recording-FAQ) separately to ensure PII and PCI data is not accessible to Zendesk users using the audio player in tickets.

### Comparing Zendesk QA and Contact Lens

Zendesk QA provides post-call transcription integrated directly into Zendesk, making it suitable for teams prioritizing Zendesk-native workflows.

However, it’s important to note that Zendesk QA does not support real-time transcription or audio redaction like Contact Lens. Refer to the following table for a comparison of features.

Table 1.

    | Feature | Zendesk QA | Contact Lens |
| --- | --- | --- |
| Timing | Post-call only | Real-time and post call |
| Redaction | Available for transcriptions only (requires the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906-About-the-Advanced-Data-Privacy-and-Protection-add-on). | Available for transcripts and recordings |
| Sentiment analysis | Available | Available |
| Agent performance insights | Available | Available |
| Licensing | Native to Zendesk QA | Native to Contact Lens |
| Integration | Native to Zendesk | Native to Amazon Connect |

If you still want to turn off Contact Lens transcriptions, then deactivate the ContactLensEventsLambda function and also ensure that Contact Lens isn’t configured in your contact flows. Should you want to turn Contact Lens transcription back on, see [Configuring Contact Center to send call recordings to Zendesk (writeback)](https://support.zendesk.com/hc/en-us/articles/9696142065306).