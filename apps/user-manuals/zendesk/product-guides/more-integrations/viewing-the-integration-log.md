# Viewing the integration log

Source: https://support.zendesk.com/hc/en-us/articles/4408819871130-Viewing-the-integration-log

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

The integration log helps you monitor data syncing between your support system and integrations like Salesforce, Jira, and Shopify. It lets you track activities, identify issues, and filter logs by date, time, product, or status. You can view detailed information for each activity, including date, product, status, and a description of the event, to ensure smooth operation and troubleshoot errors effectively.

The integration log in Admin Center provides information about data syncing
between Zendesk Support and your integrations. It enables you to check that the
integrations are running successfully and identify any issues.

This article contains the following sections:

- [About the integration logs](#topic_gzp_snm_qmb)
- [Viewing the integration log](#topic_hsb_44m_qmb)

Related articles:

- [Salesforce integration resources](https://support.zendesk.com/hc/en-us/articles/4408827957274)
- [Shopify integration resources](https://support.zendesk.com/hc/en-us/sections/360005927234)
- [Bot builder for messaging](https://support.zendesk.com/hc/en-us/articles/4408838909210)
- [ZIS integrations](https://developer.zendesk.com/documentation/integration-services/)

## About the integration logs

The integration log lists activities in the last 7 days for the following
integrations:

**Salesforce**

- Ticket sync: Synchronization of Zendesk tickets to Salesforce Cases when
  they are created or modified in Zendesk

  Note: Tickets that are created or
  modified in Salesforce are not included in the integrations
  log.
- Accounts to Organization sync: Synchronization of Salesforce Accounts to
  Zendesk organizations in Support when they are created or modified in
  Salesforce
- Contact to Users sync: Synchronization of Salesforce Contacts to Zendesk
  users when they are created or modified in Salesforce
- Leads to Users sync: Synchronization of Salesforce Leads to Zendesk users
  when they are created or modified in Salesforce

**Jira**

- Informational and error messages for field sync events. These messages appear
  when a Zendesk ticket is updated, or a Jira issue is updated or deleted, and the
  webhook sends data to Zendesk. These events help you track updates that sync
  between Zendesk and Jira.

**Shopify**

- Customer, order, and fulfillment events received by Sunshine profiles and
  events

**Bot builder for messaging**

- API calls made by a conversation bot. For more information, see [Using the Make API call step in a
  conversation bot](https://support.zendesk.com/hc/en-us/articles/4572971586586)

**Custom actions**

- Run and test events for custom actions created for use with the auto assist
  and action flow features. For more information, see [Creating and managing actions for auto
  assist and action flows](https://support.zendesk.com/hc/en-us/articles/8013439366810).

**Action flows**

- Details about action flow run and test events. See [Understanding the action builder and
  action flows (EAP)](https://support.zendesk.com/hc/en-us/articles/8855513857306).

**Private ZIS integrations**

- Executions of the integration's ZIS flow. You can customize related log
  messages using [Succeed](https://developer.zendesk.com/documentation/integration-services/developer-guide/succeed-state/) and [Fail](https://developer.zendesk.com/documentation/integration-services/developer-guide/fail-state/) states

**Messaging, social channels, and Sunshine Conversations API**

- Error logs for messaging and social channels powered by Sunshine
  Conversations.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/integrations_log.png)  
The log contains the following information
for each activity:

| Column | Description |
| --- | --- |
| Date and time | The date and time the activity occurred in the viewer's specified timezone. |
| Product | The integration name |
| Status | The job status: info, warning, error, or debug |
| Description | A description of the event. For failed jobs, a message with error details is displayed |

## Viewing the integration log

You can view the integration log in Admin Center. Activities can be filtered by date
and time and by product or status.

**To view the integration log**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
  **Apps and integrations** in the sidebar, then select **Integrations >
  Logs**.

**To filter the integration log**

1. On the **Integration log** page, click **Filter** and select the date
   and time in **Start date**, **End date**, **Start time**, and
   **End time**.
2. (Optional) Specify a **Status** or **Product**.
3. Click **Apply filters**.

   The Product drop-down list displays only
   products with errors. If there are no errors, the list will be
   empty.

**To view details of a log entry**

- On the **Integration log** page, click on any row to open the details
  panel with more information.