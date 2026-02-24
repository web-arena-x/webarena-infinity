# Call transcription and summarization FAQ

Source: https://support.zendesk.com/hc/en-us/articles/7470764710298-Call-transcription-and-summarization-FAQ

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

Verified AI summary ◀▼

Call transcription and summarization, available with Copilot and QA add-ons, enhance support by adding transcripts and summaries to tickets or QA tools. You can activate these features in Admin Center for recorded calls, with options for real-time transcription. Costs are per minute, and sensitive data can be redacted. Supported languages include English, Spanish, and more. Troubleshoot accuracy with keyword boosting.

In this article, you'll find frequently asked questions and answers about call transcription and
summarization.

This article contains the following sections:

- [General questions](#topic_kjp_h22_wbc)
- [Troubleshooting questions](#topic_ohk_322_wbc)

## General questions

- **What options are available for call transcription and
  summarization?**

  Call transcription and summarization are included as
  part of the [Copilot](https://support.zendesk.com/hc/en-us/articles/5524125586330) and [Zendesk QA](https://www.zendesk.com/service/quality-assurance/) add-ons. The underlying service which
  transcribes and summarizes calls is the same, but what differs is where the
  resulting transcripts and summaries are viewed and how they are used.
  Copilot and Zendesk QA call transcription and summary settings
  are independent. Activating Copilot, to add transcripts and summaries to
  tickets, does not send anything to Zendesk QA unless the Zendesk QA setting
  is also turned on. Even if your Support to QA connection is active and has
  no filters, transcripts and summaries are only sent to Zendesk QA when the
  QA setting is on.

  Real-time transcription powers the real-time
  suggestions feature for Voice. If this is turned on, the real-time
  transcript is used in place of the post-call transcription on ticket
  comments and in QA.

  - **Copilot add-on**

    Call transcripts and summaries are added to the
    conversation log on tickets in the Agent Workspace. Transcripts and
    summaries provide additional context to voice tickets and reduce the
    requirement for agents to take notes and summarize calls as part of
    their wrap-up activities.
  - **Zendesk QA add-on**

    Call transcripts and summaries appear in Zendesk QA where QA-focused
    users can review and analyze historical call interactions in detail.
    Voice QA evaluates the call transcript and provides a QA Score just
    like it does for chat or messaging conversations which can be used
    to identify the conversations where there’s a churn risk or an agent
    knowledge gap.
- **How do I activate call transcription and summarization?**

  You activate
  call transcription and summarization for recorded calls in Admin Center. If
  you have the [Copilot add-on](https://support.zendesk.com/hc/en-us/articles/5524125586330), you can [activate transcripts and summaries for
  tickets](https://support.zendesk.com/hc/en-us/articles/6170157307162). If you have the [Zendesk QA add-on](https://www.zendesk.com/service/quality-assurance/), you can [activate transcripts and summaries for
  QA](https://support.zendesk.com/hc/en-us/articles/8536077648538). The configuration settings are indepent of one another to
  accommodate for different needs (and subscriptions).
- **Do I need Copilot to get transcripts and summaries in Zendesk QA?**

  No.
  You just need a subscription for Zendesk QA to activate transcripts and
  summaries.
- **Is every phone call transcribed and summarized?**

  No, only
  calls which are [recorded](https://support.zendesk.com/hc/en-us/articles/4408831738266) can be transcribed and
  summarized. Admins can turn on the transcription and summarization
  functionality for some or all phone lines that have turned on call
  recording.
- **How are call transcriptions priced?**

  Call transcription is charged at
  USD$0.01 per minute and real-time transcription is charged at $0.027 per
  minute of transcribed audio. Transcription charges are rounded up to the
  nearest whole minute. If real-time transcription and post-call transcription
  are both activated, customers are charged $0.027 because the call is only
  transcribed once, in real-time. Transcription charges are processed together
  with other usage charges for voice (e.g. phone number charges, call charges,
  recordings charges, etc.) and deducted from an account's credit balance.

  For more pricing information, see the [pricing page for voice](https://support.zendesk.com/hc/en-us/articles/4408846483482).

  Note: If calls are transcribed as part of both [Copilot](https://support.zendesk.com/hc/en-us/articles/5524125586330) and Zendesk QA
  subscriptions, transcription costs will only be processed once for a
  given phone call. You won't be charged twice.
- **Where do call transcripts and call summaries appear?**

  After a phone call
  ends and the call recording audio file becomes available to play in a
  ticket, the call transcript and summary are added to the ticket conversation
  log as internal notes.
- **Can Zendesk automatically redact sensitive customer data from transcripts and
  call summaries?** 

  Yes, if you have the [Advanced Data Privacy and Protection
  add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), you can configure Zendesk to automatically redact
  personally identifiable information (PII) and payment card industry (PCI)
  data from call recording transcriptions and summaries.

  Important: Zendesk Voice can't redact PII/PCI data from call
  recording audio files. To ensure this personal information isn't
  accessible to users through the audio player in tickets, you must [delete call recording files](https://support.zendesk.com/hc/en-us/articles/4408828042010).
  Zendesk Contact Center can redact call recordings, see [call recording settings in Contact
  Center](https://support.zendesk.com/hc/en-us/articles/9459045766170).
- **What languages are supported for call transcription?**

  Post-call
  transcription uses automatic transcription language detection. For supported
  languages, see [Zendesk language support by
  product](https://support.zendesk.com/hc/en-us/articles/4408821324826#h_01K1KAQNCFD5526GMKHJCBAMTK).

  Real-time transcription uses the agents' Zendesk
  profile language. All [Zendesk agent languages](https://support.zendesk.com/hc/en-us/articles/4408821324826) are
  supported.

  If a language spoken during a call isn't supported, the
  generated transcript might be inaccurate.
- **Are voicemail recordings also transcribed?**

  Yes, voicemail recordings
  can also be transcribed to text using the same transcription model used for
  regular call recordings. See [Configuring voicemail
  options](../setting-up-your-voice-channel/configuring-voicemail-options.md).
- **Is the call transcript or call summary shared with or retained by a third
  party? Is customer data used to train the models?**

  The transcription
  and summarization features are powered by Deepgram and OpenAI’s Enterprise
  service. These services do not use Zendesk customers' inputs to train their
  models or otherwise improve their services, and Zendesk customer data will
  not be hosted except briefly for the purpose of providing the service. See
  [Zendesk AI data use information](https://support.zendesk.com/hc/en-us/articles/5729714731290)
  for more information about how your data is protected.
- **How can customers export their transcription charges?**

  From the [usage charges page](https://support.zendesk.com/hc/en-us/articles/4408825620378), users can
  review their transcription charges for a given period and export a CSV file
  containing detailed charges. Users receive an email with a ZIP file
  attachment, which contains the CSV of charges for the period.
- **Is the call transcription and summarization functionality available for Talk
  Partner Edition?**

  Call transcription and summarization works with
  Zendesk Voice only. If you're using a third-party telephony provider with
  Talk Partner Edition, several [Talk Partners](https://support.zendesk.com/hc/en-us/articles/4408819751194) offer transcription
  services, including adding call transcripts to Zendesk tickets.
- **Can agents view the real-time transcript in the Agent Workspace?**

  Agents
  cannot currently view the real-time transcript in the Agent Workspace. The
  real-time transcript is currently used by Zendesk to allow agents to
  generate AI suggestions during live calls.
- **If I activate the real-time AI suggestions feature for voice calls, will the
  call transcript and call summary be automatically added to the ticket (or
  sent to QA) after the call ends?**

  Not automatically. If you want the
  call transcript and call summary to get added to tickets or sent to QA,
  [activate it for tickets](https://support.zendesk.com/hc/en-us/articles/6170157307162) or [activate it for QA](https://support.zendesk.com/hc/en-us/articles/8536077648538) as the settings
  are independent, just like the associated Copilot and Zendesk QA
  add-ons.

## Troubleshooting questions

- **Why do call transcripts sometimes contain errors or inaccuracies?**

  Today, the
  best speech-to-text algorithms are around 90% accurate,
  meaning that for every 100 words processed, only 90 are accurately transcribed.
  Many factors can influence the accuracy of the transcription, including
  background noise, speakers talking over each other, poor quality audio
  connections or network signal, speaker dialects, quiet speech, or words and
  phrases not being in the training model database.
- **How can I improve the accuracy of transcriptions?**

  Use keyword
  boosting to specify words that are expected to occur in your phone
  conversations. This might include product names or industry-specific terms.
  Adding keywords in advance helps improve recognition and the accuracy of
  transcriptions.
- **Why is the call transcript or call summary different to what was spoken on
  the call?**

  On rare occasions AI can "hallucinate" and provide an
  inaccurate answer if it is acting on limited data. The primary cause of
  hallucination lies in the limitations of the training data and neural
  network algorithms that AI models use to 'learn.' AI models, particularly
  those based on deep learning, learn patterns and associations from massive
  datasets. If the training data is biased, incomplete, or contains errors,
  the AI may develop skewed perceptions, leading to hallucinatory outputs. For
  example, hallucinations can happen when there are periods of silence or
  background noise in a phone call, making it challenging for the AI to figure
  out what was actually said.
- **How can I prevent the call transcript from taking up a lot of space on the ticket
  conversation log?**

  For customers with a subscription to [Copilot](https://support.zendesk.com/hc/en-us/articles/5524125586330), there is an option to
  hide the call transcript on tickets.