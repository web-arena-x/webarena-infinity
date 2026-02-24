# Supervisor Monitor & Barge (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731463819802-Supervisor-Monitor-Barge-Engage-Legacy

---

This feature enables an Agent with the relevant permissions to monitor another Agent's ongoing Contact, and barge into it as needed.

This functionality is only supported on Voice Contacts

## Demo

![](https://fast.wistia.com/embed/medias/og8fk6zr3a/swatch)

‍

## Pre-Requisites

- Monitor & barge functionality must be configured in Amazon Connect:
- <https://docs.aws.amazon.com/connect/latest/adminguide/monitor-barge.html>
- The includes both enabling the functionality and ensuring your Agents have the relevant permissions
- The Agent must have both Engage and Amazon Connect open

## How to configure Monitor & Barge in Engage

- Navigate to **Settings**
- Select the **Workflows** option
- Scroll down to the relevant Workflow
- Click the **Edit workflow** button
- Ensure Notes and Resolution Codes are correctly configured in Engage, as per the screenshot below:

![](https://support.zendesk.com/hc/article_attachments/9731467489690)

## How to monitor a Contact

1. In **Amazon Connect**, open the **Real-time Metrics** - Agent dashboard (Analytics and optimization -> Real-time Metrics -> Agents)
2. Scroll to find the **Agent** you wish to monitor
3. Click on the **eye icon** next to the Voice channel for the Agent
4. Go into Engage, where you will now be monitoring the Contact selected in the step above

The Agent being monitored will not be aware that they are being monitored

## How to barge a Contact

You must be in monitoring mode before you can barge into a Contact

As soon as you barge into a Contact, the Agent will know that you have joined the Contact

1. Click on the **Monitoring** button
2. You will now be in barge mode

‍