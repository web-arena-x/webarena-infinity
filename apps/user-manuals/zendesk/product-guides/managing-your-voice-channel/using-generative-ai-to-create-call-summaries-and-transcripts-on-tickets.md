# Using generative AI to create call summaries and transcripts on tickets

Source: https://support.zendesk.com/hc/en-us/articles/6170157307162-Using-generative-AI-to-create-call-summaries-and-transcripts-on-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Enable generative AI to automatically transcribe and summarize calls, saving you time on manual note-taking. Once activated, transcripts and summaries appear on tickets as internal notes. You can choose specific phone lines, redact sensitive information, and boost keywords for accuracy. This feature enhances call management by providing insights into entity detection, intent, language, and sentiment.

There are additional costs involved in transcribing calls. See [Zendesk number availability and pricing](https://support.zendesk.com/hc/en-us/articles/4408846483482).

You can use generative AI to transcribe and summarize your calls. After a call ends and the recording is available, generative AI transcribes and summarizes the call. This saves agents time otherwise spent writing call notes during and after calls and helps them move efficiently to the next call.

When you turn on this feature, calls are automatically transcribed and summarized, then added to tickets shortly after the call ends. For supported languages, see [Zendesk language support by product](https://support.zendesk.com/hc/en-us/articles/4408821324826#h_01K1KAQNCFD5526GMKHJCBAMTK).
Transcriptions aren't available for calls or recordings made before the feature was turned on.

Your call transcripts are analyzed for entity detection and intent, language, and sentiment predictions depending on how you've [configured intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538).

**To activate call summaries and transcripts**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. On the Settings tab, click **Transcribe and summarize call recordings on tickets**.

   Tip: With this setting, call transcripts and summaries are added to tickets. If you have Zendesk QA, you can also send call transcripts and summaries to be analyzed and scored. To do so, [activate Voice QA](https://support.zendesk.com/hc/en-us/articles/8536077648538) and select the transcribe and summarize setting.
3. Under **Select lines**, select the phone lines to turn on transcription and summarization for.

   You can turn it on for all lines or specific lines only. If you don’t see a phone line in the dropdown menu, call recording isn't turned on for the line. Only lines with call recording enabled are displayed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/call_transcribe.png)
4. (Optional) If you want to show call transcripts on tickets, select **Show call transcripts on tickets**.

   This doesn’t affect generating or adding the call summary; it only controls whether the transcript is displayed on tickets. If displayed, call summaries and transcripts are added as internal notes on the ticket. This means they’re visible only to agents and admins, not to end users.
5. (Optional) If you have the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), you can configure the following redaction options:
   - **Redact personally identifiable information (PII) from transcriptions:** Automatically redact PII data, such as names, locations, and Social Security numbers from all call recording transcriptions.
   - **Redact payment card industry (PCI) data from transcriptions:** Ensure that sensitive credit card information, including credit card number, expiration date, and card verification value (CVV) is redacted from call recording transcriptions.

   Important: If these settings are turned on, PII and PCI data isn't redacted from call recording audio files. You'll need to [delete call recording files](https://support.zendesk.com/hc/en-us/articles/4408828042010)
   separately to ensure PII and PCI data is not accessible to Zendesk users using the audio player in tickets.
6. (Optional) If you want to help the transcription service focus on certain words to improve accuracy, select **Boost keywords in transcriptions** and enter individual keywords (not phrases or strings of numbers) separated by commas.

   Speech-to-text technology often struggles with jargon, names, and industry-specific terms. By identifying these unique words that are common in your calls, you can improve the transcription accuracy.
7. Click **Save**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk-transcript-1-1.png)