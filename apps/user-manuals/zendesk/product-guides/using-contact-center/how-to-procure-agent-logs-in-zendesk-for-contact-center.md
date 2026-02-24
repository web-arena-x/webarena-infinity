# How to Procure Agent Logs in Zendesk for Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/10253969891482-How-to-Procure-Agent-Logs-in-Zendesk-for-Contact-Center

---

Agent logs are a great resource when working with Zendesk Support to diagnose and resolve issues surrounding Zendesk for Contact Center. Zendesk Support may ask for these logs during the investigation, so please view the gif below on how to download them:

![](https://support.zendesk.com/hc/article_attachments/10253969891098)

It is important to download the logs after the issue you are reporting has been reproduced.

Note: Agent logs do not persist through browser refreshes. Refreshing the browser or clearing cache and cookies will cause you to lose existing agent logs.

A txt file named `agent-log.txt` is saved to your browser's default directory. After the file is downloaded, you can change the name of the file the same way you rename any other file on your computer.

## Analyzing the Agent Logs

After downloading the agent logs (also known as Contact Control Panel (CCP) agent logs in Amazon Connect), navigate [Amazon Connect's CCP Log Parser](https://tools.connect.aws/ccp-log-parser/index.html) to analyze them by dragging and dropping the downloaded `agent-log.txt` file:

![The Amazon Connect CCP Log Parser interface showing the file upload area for analyzing agent logs.](https://docs.aws.amazon.com/images/connect/latest/adminguide/images/log-parser.png)

On the **Snapshots & Logs** tab you will see the logs recorded during the agent session, filterable by the type of log. It's important to note that these logs do not persist through browser refreshes.

Normally log entries are collapsed but most log entries contain more information. To see the original log object in JSON format, click the + to expand or collapse the log lines with more information.

![](https://support.zendesk.com/hc/article_attachments/10270316137626)

On the left side of log entry, you can choose Snapshots, which are periodic. The Snapshot displays the agent status that was captured during retrieval periods. Clicking on one Snapshot highlights the section from that snapshot until the subsequent snapshot.

![The CCP Log Parser showing the Snapshots panel with agent status information.](https://docs.aws.amazon.com/images/connect/latest/adminguide/images/log-parser-2.png)

The following image shows a Snapshot log, with a softphone error.

![The CCP Log Parser displaying a Snapshot log with a softphone error message.](https://docs.aws.amazon.com/images/connect/latest/adminguide/images/log-parser-3.png)

On the **Metrics** tab, you can view the following metrics:

- **Skew Metrics** shows difference between the client-side (agent's workstation) local timestamp and server-side (Amazon Connect service) timestamp in milliseconds.
- **API Call Metrics** shows the latency of the API call from CCP.
- **WebRTC Metrics**: Available if the call was made with CCP. **WebRTC Metrics** shows the media stream condition during a call.

![The CCP Log Parser Metrics tab showing Skew Metrics and API Call Metrics data.](https://docs.aws.amazon.com/images/connect/latest/adminguide/images/log-parser-4.png)

![The CCP Log Parser WebRTC Metrics section showing media stream conditions during a call.](https://docs.aws.amazon.com/images/connect/latest/adminguide/images/log-parser-5.png)