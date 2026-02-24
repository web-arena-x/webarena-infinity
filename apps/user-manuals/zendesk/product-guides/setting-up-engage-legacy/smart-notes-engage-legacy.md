# Smart Notes (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731467217306-Smart-Notes-Engage-Legacy

---

# What are Smart Notes?

Smart Notes is a new feature in Engage for Amazon Connect that utilises Generative AI to automatically summarise a contact, and then suggest a note for the Agent to add to the Contact in After Call Work.

‍

Smart Notes aims to significantly reduce the amount of time an Agent spends crafting and submitting notes, whilst ensuring all key details are included in Notes. It is important for notes to be accurate and succinct so that any follow-on from the Contact (e.g. a transfer or a second conversation days later) has the right context.

‍

Note: Smart Notes are suggested to an Agent - they are not automatically added to a Contact.

![](https://support.zendesk.com/hc/article_attachments/9731476141850)

# How to set up Smart Notes

Note that this configuration is for the purposes of the Smart Notes beta. You may be required to change the configuration post beta.

## Prerequisites

Before settings up Smart Notes in Engage, you will need the following:

1. Access to models within an AI Service (e.g. Amazon Bedrock)
2. The AI Service configured as an AI Assist integration in Engage

[Click here](https://support.zendesk.com/hc/en-us/articles/9731462361882) for more information on the above steps.

To use Smart Notes on voice contacts, real-time analytics must be enabled via Contact Lens.

Note that redaction is not available on real time transcripts produced by Contact Lens.

Ensure your AWS CloudFormation Stack is on v5.71.0+

‍

## Channel Availability

Smart Notes is available on the following channels:

- Webchat
- SMS
- Facebook Messenger
- Instagram
- LINE
- WeChat
- Twitter
- Whatsapp
- Line
- Voice (requires Amazon Contact Lens)

Email is currently not supported.

‍

## How to configure Smart Notes in Engage Workflows

1. Navigate to Engage **Settings** page
2. Select the **Workflows** tab
3. Navigate to the relevant **Workflow** (you may only have the default workflow configured)
4. Click the **Edit workflow** button
5. Scroll down to the **Smart ToolsAssist** section
6. Ensure the **Smart Notes** setting is set to **Allow note summary generation during active contacts and After Call Work**

![](https://support.zendesk.com/hc/article_attachments/9731500141082)

‍

## How to use Smart Notes as an Agent in Engage

Transparency is one of our Gen AI Principles (link to principles). We will always make it clear to an Agent whenever Gen AI is used by highlighting the result of Gen AI.

‍

Once an Agent ends a Contact, they will have the option to use Smart Notes within After Call Work.

1. Close the contact
2. Expand the **Notes** section
3. Click the **Summarize Conversation** button
4. If the note displayed is useful, click the **Insert** button
5. To generate a new note, click the **Retry** button

‍

Note that once a Smart Note has been inserted, an Agent will be able to edit the note as required. Agents will still have to save Notes by clicking the ✔️button.

![](https://support.zendesk.com/hc/article_attachments/9731500154266)

‍

‍

‍