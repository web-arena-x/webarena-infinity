# Live Voice Transcripts (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731450200474-Live-Voice-Transcripts-Engage-Legacy

---

When on a Voice Contact, Engage can display a live transcript of the interaction.

Engage utilises AWS Contact Lens to perform transcription.

## How to Setup Live Voice Transcripts

In order to use Live Voice Transcripts your Cloud Formation Stack must be on v5.46.0 (or later).

Live Voice Transcripts require [Contact Lens](https://aws.amazon.com/connect/contact-lens/) to be enabled.

1. Ensure that **Contact Lens** is enabled by following [these instructions](https://docs.aws.amazon.com/connect/latest/adminguide/enable-analytics.html)
2. Within the Contact Lens settings, enable the **Real-time and post-call analytics** option
3. Within **Engage**, go to the **Settings** page
4. Select the **Workflows** tab
5. Select the relevant Workflow and click **Edit workflow**
6. Scroll down to the **Voice Transcripts** section
7. Select the **Real-time** option
8. Click **Save Workflow**

![](https://support.zendesk.com/hc/article_attachments/9731462756506)

‍