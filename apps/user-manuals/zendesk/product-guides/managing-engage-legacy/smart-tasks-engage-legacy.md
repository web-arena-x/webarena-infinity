# Smart Tasks (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731500101914-Smart-Tasks-Engage-Legacy

---

# What is Smart Tasks?

Smart Tasks is a of tool that Agents can use automatically fill fields within Tasks.

Smart Tasks uses Generative AI to extract the relevant data from an ongoing Contact, based on the Task an Agent needs to complete.

Smart Tasks aims to reduce the amount of time an Agent spends completing Tasks, whilst also aiming to improve the quality of data entered into Tasks.

![](https://support.zendesk.com/hc/article_attachments/9731467314714)

# How to set up Smart Tasks

## Prerequisites

Prior to using Smart Tasks, you will need to ensure your AI Integration is configured in Engage.

## Channel Availability

Smart Tasks is available on the following channels:

- Webchat
- SMS
- Facebook Messenger
- Instagram
- LINE
- WeChat
- Twitter
- Whatsapp
- Line
- Voice

Email is currently not supported.

## How to configure Smart Tasks in Engage Workflows

1. Navigate to Engage **Settings** page
2. Select the **Workflows** tab
3. Navigate to the relevant **Workflow** (you may only have the default workflow configured)
4. Click the **Edit workflow** button
5. Scroll down to the **Smart Tasks** section
6. Ensure the **Smart Forms** setting is set to **Allow form field auto-fill**

![](https://support.zendesk.com/hc/article_attachments/9731476213018)

### Tips for Configuring Tasks to use as Smart Tasks

When building a Task that your Agents may complete as a Smart Task, consider the following:

- Smart Tasks will not complete fields that already have a value
- This means that any fields with a default value of a personalisation token will not be updated using Smart Tasks
- Dropdowns need to have a blank value as the first option, so that it can be overwritten by Smart Tasks