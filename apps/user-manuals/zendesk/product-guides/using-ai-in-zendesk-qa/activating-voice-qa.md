# Activating Voice QA

Source: https://support.zendesk.com/hc/en-us/articles/8536077648538-Activating-Voice-QA

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Activate Voice QA to review call conversations without listening to entire recordings. It auto-generates transcripts, separates speakers, and provides QA scores in categories like greeting and empathy. Import call recordings via Talk or Partner Edition to analyze them. You can redact sensitive information and boost keyword accuracy for better transcriptions. Connect with pre-built integrations or use the API for custom setups.

There are additional costs involved in recording and transcribing phone calls from Zendesk TPEs. See [Call transcription charges](../talk-basics/zendesk-talk-number-availability-and-pricing.md#h_01J56FNYT9C83VJWPR43BB3SDZ).

[Voice QA in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043759312154) helps you review conversations efficiently without having to listen to the entire phone call recording.

The system automatically generates a transcript for each recording, with speakers clearly separated for easier review. Zendesk QA's [auto scoring](https://support.zendesk.com/hc/en-us/articles/7043747123354) is also available for voice calls in five predefined categories: greeting, closing, empathy, comprehension, and solution offered.

Call recordings must be imported into Zendesk QA before they can be [analyzed](https://support.zendesk.com/hc/en-us/articles/8536308081178). To do this, activate Voice QA with Zendesk Talk or Zendesk Talk Partner Edition (TPE).

This article contains the following topics:

- [Activating Voice QA with Zendesk Talk](#about_voice_qa)
- [Activating Voice QA with Zendesk Talk Partner Edition (TPE)](#activate_voice_qa_via_talk_partner_edition)

## Activating Voice QA with Zendesk Talk

You must [turn on the voice channel](https://support.zendesk.com/hc/en-us/articles/4408838035866) before you can activate Voice QA in Zendesk QA.

**To activate Voice QA with Zendesk Talk**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. On the **Settings** tab, select **Transcribe and summarize call recordings for Zendesk QA**.

   When selected, call transcripts and summaries are sent to Zendesk QA where QA-focused users can review and analyze call interactions in detail. Voice QA evaluates the call transcript and provides a QA score in the same way it does for chat or messaging conversations.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_transcribe_calls.png)

   Tip: If you want your call transcripts and summaries to appear in Support tickets, see [Using generative AI to create call summaries and transcripts on tickets](https://support.zendesk.com/hc/en-us/articles/6170157307162).
3. Under **Select lines**, select the phone lines for which you want to turn transcription and summarization on. You can turn it on for all lines or specific lines only.

   Only phone lines with [call recordings](https://support.zendesk.com/hc/en-us/articles/4408831738266) turned on can be selected. Lines without this setting aren’t listed.
4. (Optional) If you have the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906-About-the-Advanced-Data-Privacy-and-Protection-add-on), you can configure the following redaction options:
   - **Redact personally identifiable information (PII) from transcriptions:** Automatically redact PII data, such as names, locations, and Social Security numbers from all call recording transcriptions.
   - **Redact payment card industry (PCI) data from transcriptions:** Ensure that sensitive credit card information, including credit card number, expiration date, and CVV is redacted from call recording transcriptions.

   Important: PII and PCI data is not redacted from call recording audio files.
   You need to [delete call recording files](https://support.zendesk.com/hc/en-us/articles/4408828042010-Zendesk-Talk-call-recording-FAQ) separately to ensure PII and PCI data is not accessible to Zendesk users using the audio player in tickets.
5. (Optional) If you want to help the transcription service focus on certain words to improve accuracy, select **Boost keywords in transcriptions** and enter individual key words (not phrases or strings of numbers) separated by a comma.

   Speech-to-text technology often struggles with jargon, names, and industry-specific terms. By identifying these unique words that are common in your calls, you can improve the transcription accuracy.
6. Click **Save**.

## Activating Voice QA with Zendesk Talk Partner Edition (TPE)

If you’re using a call center solution other than Zendesk Talk, you can connect it to Voice QA with [Zendesk Talk Partner Edition (TPE)](https://support.zendesk.com/hc/en-us/articles/4408819751194).

TPE currently offers the following pre-built telephony integrations that plug directly into Zendesk QA:

- Genesys
- Amazon Connect
- Talkdesk
- Aircall
- Five9

Alternatively, you can use the [Zendesk Talk Partner Edition API](https://developer.zendesk.com/api-reference/voice/talk-partner-edition-api/introduction/) to connect your own integrations.

To turn on one of these integrations for a trial or paid subscription of Zendesk QA, contact your [Zendesk Sales Representative](https://support.zendesk.com/hc/en-us/articles/4408843597850#h_01FB4BHCQN7EX10B0FK7JBTS78).

After phone call recordings are imported, you can access them on your Conversations page. See [Analyzing phone calls and transcripts in Voice QA](https://support.zendesk.com/hc/en-us/articles/8536308081178).