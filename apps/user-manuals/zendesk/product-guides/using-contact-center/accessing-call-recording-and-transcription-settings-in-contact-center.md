# Accessing call recording and transcription settings in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9459045766170-Accessing-call-recording-and-transcription-settings-in-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Access call recording and transcription settings to manage how call data is handled. Choose between redacted or unredacted options for both recordings and transcripts, ensuring sensitive information is protected if needed. Audio files and transcripts can be automatically added to associated tickets, enhancing record-keeping and reference capabilities. Configure these options through Amazon Connect Contact Lens or opt for no recording or transcription if preferred.

This article covers the call recording and transcript settings for Zendesk for Contact Center
voice. Based on your settings, call data, such as audio files and transcripts, can be added to
the Zendesk ticket associated with a call.

These call recording and transcription options use Amazon Connect Contact Lens, which you
must configure separately in your Amazon Console and within Connect Contact Flows. If you do
not want to use Contact Lens, and you have Zendesk QA, you can [use Zendesk QA for call transcriptions](https://support.zendesk.com/hc/en-us/articles/9475134529050) instead of Contact Lens.

This article contains the following topics:

- [Call recording options](#topic_lfs_zkm_yfc)
- [Call transcription options](#topic_uwp_1lm_yfc)

## Call recording options

The Call details section in Contact Center contains settings that control how call
recordings are managed.

**To open and view the call recording options**

1. In the Zendesk ticket view, under the Call details section, find the Contact Center
   voice call log.
2. Select the recording option from the dropdown menu for a call.
3. View the following settings:

   - **Redacted call recording**: A version of the recording where sensitive
     information (such as credit card numbers or personal data) is automatically
     removed. Redaction is done by Amazon Connect Contact Lens (not Amazon Q).
   - **Unredacted call recording**: A full recording of the call, without
     information removed. This uses the native recording functionality in Amazon
     Connect (not Amazon Q).
   - **No call recording**: No recording is saved or added to the Zendesk ticket.
     This option is generally not applicable, as Contact Center requires Amazon Connect
     to function. Therefore, you should use this setting only in exceptional cases. If
     recording is enabled, the audio file is automatically attached to the
     corresponding Zendesk ticket for reference.

## Call transcription options

These settings determine whether and how the call is transcribed and logged:

- **Redacted call transcript**: A text version of the call with sensitive content
  redacted. Redaction is done by Amazon Connect Contact Lens.
- **Unredacted call transcript**: A full transcript of the call without any redaction.
  This is processed by Amazon Connect Contact Lens.
- **No call transcript**: No transcription is generated or attached to the Zendesk
  ticket. This is the preferred option if transcriptions are not required.