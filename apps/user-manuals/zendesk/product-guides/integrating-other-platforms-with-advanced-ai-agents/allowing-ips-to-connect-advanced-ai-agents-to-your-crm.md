# Allowing IPs to connect advanced AI agents to your CRM

Source: https://support.zendesk.com/hc/en-us/articles/8357756859546-Allowing-IPs-to-connect-advanced-AI-agents-to-your-CRM

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

An allowlist helps keep your system protected by specifying which IPs have access to your system. To make sure your AI agent functions correctly, you must add certain IP addresses to your allowlist. These IPs are used by different backend services of the AI agents - Advanced add-on to communicate with your customer relationship management (CRM)
platform.

This article contains the following topics:

- [Managing the allowlist in your AI agent](#topic_scn_xsl_w2c)
- [Managing the allowlist in your CRM](#topic_tp5_ysl_w2c)

Related articles:

- [Managing advanced settings for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/9094002847130)

## Managing the allowlist in your AI agent

In your AI agent’s advanced settings, you can manage which IPs have access to your system. For your AI agent to function correctly, you must add all of the following IPs for your region:

- IPs to allow for the EU:
 - 34.140.214.64
 - 34.140.222.34
 - 35.233.19.208
 - 34.79.189.15
 - 34.78.252.6
 - 34.34.185.160
- IPs to allow for the US:
 - 35.197.70.75
 - 35.233.151.233
 - 34.145.96.207
 - 35.230.1.204
 - 34.168.87.73

**To manage the AI agent allowlist**

1. In AI agents - Advanced, in the top-right corner, use the AI agent drop-down field to select the AI agent you want to manage the allowlist for.
2. In the left sidebar, click **Settings** > **AI agent settings**.
3. Click the **Advanced settings** tab.
4. Under Allowlist IP addresses, click **Add IP**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_advanced_settings_allowlist.png)
5. Enter the IP address you want to allow (see the list above).
6. Repeat steps 4 and 5 until you’ve added all appropriate IPs.
7. Click **Save**.

## Managing the allowlist in your CRM

After you’ve added the IPs to the allowlist in your advanced AI agent, you must also add those same IPs in your CRM platform. For help, see [Restricting access to Zendesk Support and your help center using IP restrictions](https://support.zendesk.com/hc/en-us/articles/4408894156186).